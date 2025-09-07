There exist a lot of popular systems based on MCTS ([[Monte Carlo Tree Search and Game Playing]]). But they have some limitations, especially in large search spaces:
- Inefficient Exploration – The systems treat all moves equally at first and only refines values after many rollouts.
- Lack of Generalization – Every game state is evaluated from scratch, meaning no learning happens across different games.
- Purely Random Rollouts – The game outcome is estimated based on random moves rather than intelligent play.

MCTS can be improved by deep learning in two key ways: 
1. **Step 1: Selection (Improved by the Policy Network)**
	- In standard MCTS, selection is based on UCT, which balances exploration vs. exploitation.
	- In deep learning, a policy network is used to bias the selection toward promising moves, instead of treating all moves equally at first.
	- This helps focus the search on good moves from the start, rather than needing many rollouts to refine the estimates.
2. **Step 3: Simulation (Improved by the Value Network)**
	- In standard MCTS, simulation (rollouts) plays out a game randomly until the end, which can be noisy and inefficient.
	- In deep learning, the value network directly estimates the probability of winning from a given state, eliminating the need for full random rollouts.
	- This makes the search much faster because instead of playing thousands of games per move, the value network provides a strong estimate instantly.

In this project I go into a little more detail how that can be done: [[MCTS and Deep Learning Report.pdf]]. The code for this solution is here: [[MCTS and Deep Learning Code.py]].

