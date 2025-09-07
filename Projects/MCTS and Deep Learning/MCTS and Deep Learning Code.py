# %%
import numpy as np
import random
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class PolicyNetwork(nn.Module):
    def __init__(self, board_size):
        super(PolicyNetwork, self).__init__()
        self.board_size = board_size
        self.input_size = board_size * board_size
        self.fc1 = nn.Linear(self.input_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, self.input_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return self.softmax(x)

class TicTacToe:
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype=int)  # 0 = empty, 1 = X, -1 = O
        self.current_player = 1  # X starts

    def get_available_moves(self):
        return [(r, c) for r in range(self.board_size) for c in range(self.board_size) if self.board[r, c] == 0]

    def make_move(self, move):
        r, c = move
        self.board[r, c] = self.current_player
        self.current_player *= -1  # Switch players

    def undo_move(self, move):
        r, c = move
        self.board[r, c] = 0
        self.current_player *= -1

    def check_winner(self):
        # Check rows and columns
        for i in range(self.board_size):
            if np.all(self.board[i, :] == 1) or np.all(self.board[:, i] == 1):
                return 1  # X wins
            if np.all(self.board[i, :] == -1) or np.all(self.board[:, i] == -1):
                return -1  # O wins

        # Check diagonals
        if np.all(self.board.diagonal() == 1) or np.all(np.fliplr(self.board).diagonal() == 1):
            return 1  # X wins
        if np.all(self.board.diagonal() == -1) or np.all(np.fliplr(self.board).diagonal() == -1):
            return -1  # O wins

        # Check for draw
        if not self.get_available_moves():
            return 0  # Draw

        return None  # Game not over

    def is_terminal(self):
        return self.check_winner() is not None

    def clone(self):
        new_game = TicTacToe(self.board_size)
        new_game.board = self.board.copy()
        new_game.current_player = self.current_player
        return new_game

class MCTSNode:
    def __init__(self, state, parent=None, move=None, policy_network=None):
        self.state = state.clone()
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.value = 0  
        self.untried_moves = state.get_available_moves()
        self.policy_network = policy_network
        self.prior_probabilities = self.get_prior_probabilities()

    def get_prior_probabilities(self):
        if self.policy_network is None:
            return {move: 1.0 for move in self.untried_moves}
        board_tensor = torch.FloatTensor(self.state.board.flatten()).unsqueeze(0)
        with torch.no_grad():
            probabilities = self.policy_network(board_tensor).squeeze().numpy()
        return {(r, c): probabilities[r * self.state.board_size + c] for r, c in self.untried_moves}

    def select_child(self):
        def ucb_score(child):
            if child.visits == 0:
                return float('inf')
            exploitation = child.value / child.visits
            exploration = 1.41 * np.sqrt(np.log(self.visits + 1) / child.visits)
            prior = self.prior_probabilities[child.move]
            return exploitation + exploration * prior

        return max(self.children, key=ucb_score)

    def expand(self):
        move = self.untried_moves.pop()
        new_state = self.state.clone()
        new_state.make_move(move)
        child = MCTSNode(new_state, parent=self, move=move, policy_network=self.policy_network)
        self.children.append(child)
        return child

    def backpropagate(self, reward):
        self.visits += 1
        self.value += reward
        if self.parent:
            self.parent.backpropagate(-reward)  

    def best_move(self):
        return max(self.children, key=lambda c: c.visits).move if self.children else random.choice(self.state.get_available_moves())

    def simulate(self):
        temp_state = self.state.clone()
        while not temp_state.is_terminal():
            temp_state.make_move(random.choice(temp_state.get_available_moves()))
        return temp_state.check_winner() or 0

    def run_mcts(self, iterations=1000):
        for _ in range(iterations):
            node = self
            while node.children and not node.untried_moves:
                node = node.select_child()
            if node.untried_moves:
                node = node.expand()
            reward = node.simulate()
            node.backpropagate(reward)
        return self.best_move()

# Training the policy network
def train_policy_network(policy_network, optimizer, games, board_size):
    for game_num in range(games):
        print("Training game:", game_num)
        game = TicTacToe(board_size)
        states = []
        played_moves = []
        while not game.is_terminal(): # play 1 game 
            root = MCTSNode(game, policy_network=policy_network)
            move = root.run_mcts(1000) # get best move according to mcts 
            states.append(game.board.flatten()) # save the states of the game
            move_index = move[0] * board_size + move[1]  # Convert (r, c) to flat index
            played_moves.append(F.one_hot(torch.tensor(move_index), num_classes=board_size * board_size).float()) #One-hot encoding
            game.make_move(move)

        winner = game.check_winner()
        if winner == 1:
            rewards = [1 if i % 2 == 0 else -1 for i in range(len(states))] # each move played gets the reward 1
        elif winner == -1:
            rewards = [-1 if i % 2 == 0 else 1 for i in range(len(states))] # each move played gets the reward -1
        else:
            rewards = [0 for _ in range(len(states))]

        optimizer.zero_grad() # Resets the gradients of the policy network’s parameters to zero, otherwise they add up.
        for state, move_prob, reward in zip(states, played_moves, rewards):
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            predicted_probs = policy_network.forward(state_tensor) # Forward pass: outputs a probability distribution over the 9 possible moves, current "belief" about the best moves for the given state.
            loss = -torch.sum(torch.FloatTensor(move_prob) * torch.log(predicted_probs)) * reward # Computes the policy gradient loss. Are the moves with a high assigned probability leading to victories?
            loss.backward() # Backpropagation 
        optimizer.step() # Updates the policy network’s parameters using the computed gradients from the backpropagation. 

# Simulating against a random opponent
def simulateGame(board_size, policy_network):
    game = TicTacToe(board_size)
    while not game.is_terminal():
        if game.current_player == 1:
            root = MCTSNode(game, policy_network=policy_network)
            move = root.run_mcts(1000)
        else:
            move = random.choice(game.get_available_moves())  # Random opponent
        game.make_move(move)

    return game.check_winner()

# Main execution
board_size = 4  # Change this to any board size (e.g., 4 for 4x4)
policy_network = PolicyNetwork(board_size)
optimizer = optim.Adam(policy_network.parameters(), lr=0.01)

# Train the policy network
train_policy_network(policy_network, optimizer, games=300, board_size=board_size)

# Test the trained network
winners = []
for i in range(1, 101):
    print("Playing game:", i)
    winners.append(simulateGame(board_size, policy_network))

print("Times AI has won: ", winners.count(1))
print("Times opponent has won: ", winners.count(-1))
print("Times a draw happened:", winners.count(0))


