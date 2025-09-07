# %%
import numpy as np
import random

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
    def __init__(self, state, parent=None, move=None):
        self.state = state.clone()
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.value = 0  
        self.untried_moves = state.get_available_moves()

    def select_child(self):
        return max(self.children, key=lambda c: c.value / (c.visits + 1e-6) + 1.41 * np.sqrt(np.log(self.visits + 1) / (c.visits + 1e-6)))

    def expand(self):
        move = self.untried_moves.pop()
        new_state = self.state.clone()
        new_state.make_move(move)
        child = MCTSNode(new_state, parent=self, move=move)
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
    
# Playing the game against the AI
# game = TicTacToe()
# while not game.is_terminal():
#     if game.current_player == 1:
#         print("AI (X) is thinking...")
#         root = MCTSNode(game)
#         move = root.run_mcts(1000)
#         print(type(move))
#     else:
#         move = tuple(map(int, input().split())) 
#         print(move)
#     game.make_move(move)
#     print(game.board, "\n")

# print(game.check_winner())

# Simulating against a random opponent
def simulateGame(board_size):
    game = TicTacToe(board_size)
    while not game.is_terminal():
        if game.current_player == 1:
            root = MCTSNode(game)
            move = root.run_mcts(1000)
        else:
            move = random.choice(game.get_available_moves())  # Random opponent
        game.make_move(move)

    return game.check_winner()

board_size = 4
winners = []
for i in range(1,101):
    print("Playing game:", i)
    winners.append(simulateGame(board_size))

print("Times AI has won: ", winners.count(1))
print("Times opponent has won: ", winners.count(-1))
print("Times a draw happened:", winners.count(0))


