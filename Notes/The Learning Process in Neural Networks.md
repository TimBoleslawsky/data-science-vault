Before introducing the learning process, we need to introduce two important concepts that enable neural networks to learn: loss functions and optimization.
## Loss Functions
Loss functions measure how well (or badly) a neural network’s predictions match the actual target values. The goal of training is to minimize the loss, making the model’s predictions more accurate. A loss function takes the predicted output $\hat{y}$ and the actual target $y$ and returns a numerical value representing the error:
- If the loss is high, the model is performing poorly.
- If the loss is low, the model is performing well.

**Types of Loss Functions**
- For regression problems, where we have continuous numerical outputs, popular loss functions are the mean squared error, the mean absolute error, or the Huber Loss, which is a combination of MSE & MAE.
- For classification problems we usually either use log loss or binary cross-entropy (for binary classification) or categorical cross-entropy (for multi-class classification).
## Optimization (Gradient Descent & Variants)
Optimization is the process of adjusting a model’s weights to minimize the loss function. It is about finding the best set of parameters (weights and biases) that minimize the loss function. More on optimization problems in general, here: [[Optimization Problems]]. 

To talk about optimization, we need to introduce two concepts: *objective functions* & *gradients*. 
- Objective functions in machine learning models can have two forms: First, a *loss function* that measures how well the model fits the training data. Second, a *regularizer* that measures how simple/complex the model is.
- In realistic ML, we will have many parameters! Let $w$ be the vector of these parameters. For a single parameter $w_i$, we can define the partial derivative. The vector of all partial derivatives is called the *gradient*.
### Gradient Descent
The idea behind gradient descent is simple: 
- To find the minimum:
	- take a small step in the direction opposite to the gradient.
	- repeat until the gradient is close enough to zero.

One major consideration here is the size of the steps. A smarter versions of gradient ascent/descent tries to adapt the step size so that we don’t go too slow in the beginning, or bounce around the top at the end. One simple solution: start fast, then gradually more slow.
#### Stochastic Gradient Descent
Gradient descent can be slow and computationally very expensive to perform on huge data. Stochastic gradient descent simplifies the computation by computing the gradient using just a small part (in the extreme case, a single training instance or a mini-batch: a few instances).

When to terminate SGD? The simple solution would just be a fixed number of iterations. Another more sophisticated solution would be *early stopping*. This means that we evaluate on a held-out set. The held-out set is a separate data set from the training data. The training stops as soon as the performance on the evaluation set (i.e., the held-out set) does not improve. 

Some more advanced optimization algorithms like Adam (Adaptive Moment Estimation) also follow the gradient, but more intelligently. Adam adjusts the learning rate individually for each parameter. Basically it slows down in tricky spots, and speeds up when it’s safe.
## The Learning Process
The learning process in deep learning consists of iteratively minimizing the loss function by updating the model’s weights using an optimizer. 
At each iteration (or **epoch**) of training, the model follows these steps:
1. Forward Pass (Prediction):
   - The input $x$ passes through the network.
   - Each layer applies transformations: $a^{(1)} = \sigma(Wa^{(0)}+b)$. 
   - The final layer produces the **prediction** $\hat{y}$.
2. Compute the Loss:
   - The prediction $\hat{y}$ is compared to the true target $y$.
   - The loss function $\mathcal{L}(y, \hat{y})$ quantifies the error.
3. Backpropagation (Computing Gradients)
   - To minimize the loss, we compute how much each weight $W$ and bias $b$ contributes to the loss:
	   - First we compute the gradient for the output layer by diffentiating the loss function. 
	   - Then, using the chain rule, we use each gradient from the previous layer to compute the gradients of the remaining layers. => This tells us which direction (increase or decrease) each weight should move to reduce the loss.
4. Weight Update (Using an Optimizer)
   - Once gradients are computed, an optimizer updates the weights. 
5. Repeat Until Convergence
   - The process repeats over multiple epochs until the loss is sufficiently low or stops improving.
   - Early stopping can prevent overfitting by stopping training if the validation loss stops decreasing.
## Loss Functions in Unsupervised and Reinforcement Learning
In unsupervised learning and reinforcement learning, we don’t have a direct ground truth $y$ to compare $\hat{y}$ to, so the concept of loss functions works differently.

**Unsupervised Learning**
Since we don’t have labeled data, the goal is usually to learn structure or patterns in the input data. Loss functions in unsupervised learning are designed to measure how well the model captures this structure. For example, clustering: 
- Loss function: **Within-cluster sum of squares (WCSS)**
	$\mathcal{L} = \sum_{i=1}^{n} \sum_{j=1}^{k} ||x_i - C_j||^2$
	- $C_j$ is the centroid of cluster $j$.
	- The loss is the sum of squared distances between points and their closest cluster center.
	- The model minimizes this loss by adjusting cluster centers.

**Reinforcement Learning**
In reinforcement learning, there’s no labeled dataset. Instead, the model learns through **trial and error**, receiving **rewards** as feedback. The loss functions in RL are designed to:
- **Improve the policy** (choosing better actions over time).
- **Estimate the value function** (predicting expected future rewards).
The are a few different methods to do this, depending on the use case, but I will focus on policy gradient loss. 

**Policy Gradient Loss (Used in Policy-Based Methods)**
The neural network used in policy gradient methods is called a **policy network**. It takes the state of for example a game as an input and outputs a probability distribution over actions, so the final layer has a softmax activation for discrete actions and continuous values for continuous actions. 
Output: $\pi_{\theta}(a | s) = \text{softmax}(W s + b)$, where: $\pi_{\theta}(a | s)$ is the probability of selecting action $a$ given state $s$.

How this effects the learning process:
- **Start with an initial policy** $\pi_{\theta}(a_t | s_t)$.
	- This policy is represented by a deep neural network, parameterized by \theta.
	- At first, $\pi_{\theta}$ is untrained, so it selects actions **randomly** or based on some initial strategy.
- **Follow the policy to play the game**
	- The agent starts at the **initial state** $s_0$.
	- At each step $t$, it **samples an action** $a_t$ based on the current policy: $a_t \sim \pi_{\theta}(a_t | s_t)$
	- The environment responds with a **reward** $r_t$ and a new **state** $s_{t+1}$.
- **Game continues until termination**
	- The agent keeps taking actions and receiving rewards.
	- At the end of the episode (game), the agent collects all rewards $r_t$.
- **Compute the total return for each timestep**
	- The total return from time step t onward is defined as: $R_t = \sum_{k=t}^{T} \gamma^k r_k$, where: 
		- $\gamma$ (gamma) is the **discount factor**, which determines how much future rewards are worth.
		- $R_t$ represents the **discounted cumulative reward** from time $t$ onward.
- **Compute the Policy Gradient Loss Function**
	- Using the collected rewards, we compute the **policy gradient loss**: $L_{\text{PG}} = - \sum_{t} R_t \log \pi_{\theta}(a_t | s_t)$
	- This loss function encourages the network to **increase** probabilities of actions that led to high rewards and **decrease** probabilities of actions that led to low rewards.
- **Compute gradients via backpropagation**
	- Compute the gradient of the loss with respect to the policy parameters $\theta$: $\nabla_{\theta} J(\theta) = \mathbb{E} [ R_t \cdot \nabla_{\theta} \log \pi_{\theta}(a_t | s_t) ]$
	- This step estimates how changing the policy parameters \theta affects the total expected reward.
- **Apply Gradient Ascent to update the policy parameters**
	- Since we want to **maximize** the expected reward, we perform **gradient ascent** instead of descent: $\theta \leftarrow \theta + \alpha \nabla_{\theta} J(\theta)$
	- This updates our policy **so that it assigns higher probability to better actions**.
