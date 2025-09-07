The basic idea of approaching a game playing problem with AI is that we can take some actions according to a policy and through that reach states. The minimax optimization for example aims to minimize the maximum success of your opponent to guarantee success against the best possible opponent. But such approaches have two problems, especially in *large state spaces*:
- State Space and Feasibility: We can’t explore every state => We won’t experience everything in feasible time spans. 
	- Possible solution: Reducing breadth by sampling actions from a probability distribution rather than considering all possible moves. We can for example use sampling techniques like Monte Carlo rollouts or policy-based methods to handle large state spaces.
- Storage Limitations: We can’t store the value of each state  => A table housing all state-value pairs would be too huge. 
	- Possible solution: Truncating search depth with an approximate value function (deep learning), to reduce the number of states considered.
## Monte Carlo Tree Search (MCTS)
Monte Carlo Tree Search (MCTS) is a decision-making algorithm used for planning in complex environments. MCTS models actions, or more specifically state-action pairs, in a game as nodes in a tree. While traversing through the nodes we collect metrics, most importantly: $q_i$ (number of wins from a specific node $i$) and $n_i$ (number of times this node has been visited). How a MCTS implementation could look like in practice can be seen in this report [[MCTS.pdf]] and this code snippet [[MCTS.py]]. 

The basic idea of MCTS can be broken down into four steps: 
1.  **Selection**
	- Start from the **root node** (current game state).
	- Based on what we know so far, traverse down until an unexplored child node is reached. 
	- The traversal uses a **tree policy**:
		- One popular tree policy is upper confidence bound or UCT (upper confidence bound applied to trees). The idea is to balance **exploration** and **exploitation** during the traversal. The formula looks like this: $UCT_i = \frac{q_i}{n_i} + C \cdot \sqrt{\frac{\ln N}{n_i}}$, with $N$ being the total number of visits to the parent node and $C$ being an exploration constant (A higher $C$ prioritizes exploration, while a lower $C$ favors exploitation). We know select the child with the highest UCT value in the traversal until reaching a node that is not fully explored.
2. **Expansion**
	- Expand the tree by adding a new (unvisited) child node. This is critical to avoid leaving out good moves.
	- MCTS only expands nodes when needed, keeping the tree size manageable.
3. **Simulation (Rollout)** 
	- From the new node, **simulate a random playthrough** (also called a **rollout**) until reaching a terminal state (win/loss/draw).
	- Based on a simulation policy, typically a simple random policy. 
	- Simulations provide an estimate of how good the state is without evaluating all possibilities.
4. **Backpropagation**
	- In general backpropagation refers to the process of propagating information **backwards through a structure** (e.g., a tree or a neural network) to **update values** based on outcomes.
	- In the case of MCTS this means we update our idea of how good moves were (by updating $n_i$ and $q_i$).
	- This has the effect that nodes that consistently lead to good results get higher priority in future selections.!
