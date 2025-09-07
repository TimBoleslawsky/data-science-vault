There are a few different ways we can teach a neural network to "learn". Here is as summary of the most important ones (there are many more):
- **Supervised Learning**
	- **How the system learns**: The model learns from labeled data, meaning each input has a corresponding output (label).
	- **Objective**: Minimize the error between predictions and actual labels (e.g., using loss functions like cross-entropy or mean squared error).
	- **Examples**:
		- [[Approaches for creating Regression Models]]
		- [[Approaches for creating Classification Models]]
	=> This approach is very depend on good and enough training data!
- **Reinforcement Learning**
	- **How the system learns**: The model (called an agent) interacts with an environment, taking actions and receiving rewards or penalties. It learns through trial and error.
	- **Objective**: Maximize cumulative rewards over time using techniques like **Q-learning** or **policy gradient methods**.
	- **Examples**:
		- AlphaGo (game-playing AI).
		- Robotics (self-learning robots).
		- Autonomous driving.
	=> We don't have the necessity of a lot of training data anymore! 
- **Unsupervised Learning**
	- **How the system learns**: Since there is again no target variable $y$, the system must discover structure in the data on its own. We do this by for example identifying clusters or reducing dimensionality. 
	- **Objective**: Instead of minimizing a loss function based on the difference between $\hat{y}$ and $y$, unsupervised learning minimizes some internal measure of structure (for example cluster compactness).
	- **Examples**:
		- [[Approaches for creating Clustering Models]]
		- Dimensionality Reduction
- **Transfer Learning**
	- **How the system learns**: A pre-trained model (usually trained on a large, general dataset like ImageNet) is reused and **fine-tuned on a new, typically smaller, task-specific dataset**. The model retains general features learned from the original task and adapts them to the new one.
	- **Objective**: Leverage prior knowledge to improve performance on a new task with **less training data** and faster convergence. Often only the final layers are retrained while earlier layers are kept frozen.