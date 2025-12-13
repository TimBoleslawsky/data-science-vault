There are a few different ways we can teach a model to "learn". The *learning* here just means parameter and structure estimation. These heavily influence the task types for mathematical models. More on these here: [Different Task Types for Mathematical Models](Different%20Task%20Types%20for%20Mathematical%20Models.md). Here is as summary of the most important ones (there are many more):
## Supervised Learning
- **How the system learns**: The model learns from labeled data, meaning each input has a corresponding output (label).
- **Objective**: Minimize the error between predictions and actual labels (e.g., using loss functions like cross-entropy or mean squared error).
- **Example Tasks**:
	- Regression
	- Classification
=> This approach is very depend on good and enough training data!
## Semi-Supervised Learning
- **How the system learns**: The model learns from a **small amount of labeled data** combined with a **large amount of unlabeled data**.
- **Objective**: Exploit the structure of unlabeled data to improve learning efficiency and generalization, often using techniques like pseudo-labeling, graph-based methods, or consistency regularization.
- **Example Tasks**:
	- Classification with limited labels (e.g., medical image classification with few annotated scans)
	- Semi-supervised regression or clustering        
=> Useful when labeled data is scarce but unlabeled data is abundant.
## Unsupervised Learning
- **How the system learns**: Since there is no target variable $y$, the system must discover structure in the data on its own. We do this by for example identifying clusters or reducing dimensionality. 
- **Objective**: Instead of minimizing a loss function based on the difference between $\hat{y}$ and $y$, unsupervised learning minimizes some internal measure of structure (for example cluster compactness).
- **Example Tasks**:
	- Clustering
	- Dimensionality Reduction
=> Focused on understanding latent structure, not predicting specific outcomes.
## Self-Supervised Learning
- **How the system learns:** The model learns from **unlabeled data**, but creates its own _supervisory signals_ by constructing a prediction task from the data itself. This is done by e.g. masking parts of the input and predicting the masked parts (BERT, MAE) or predicting the next token or next frame (autoregressive models).
- **Objective:** Solve a _pretext task_ that forces the model to learn meaningful structure. Typical losses include cross-entropy, contrastive losses, or reconstruction losses. This is especially important in modern models, because of the vast amount of available unlabeled data. Self-supervised learning provides a way to create sensible training data using unlabeled data. 
- **Example Tasks:**
	- Representation learning like autoencoders. 
	- Generative tasks like autoregressive models (GPT).
=> Enables turning unlabeled data into meaningful training data for large data quantities.
## Reinforcement Learning
- **How the system learns**: The model (called an agent) interacts with an environment, taking actions and receiving rewards or penalties. It learns through trial and error.
- **Objective**: Maximize cumulative rewards over time using techniques like **Q-learning** or **policy gradient methods**.
- **Example Tasks**
	- Policy learning
=> Does not require labeled datasets; performance emerges from interaction and feedback.
## Transfer Learning
- **How the system learns**: A pre-trained model (trained on a large, general dataset) is reused and fine-tuned on a new, typically smaller, task-specific dataset.
- **Objective**: Leverage prior knowledge to improve performance on a new task with less data and faster convergence. Often only the final layers are retrained, while earlier layers remain frozen.
- **Example Tasks**:
	- Image classification using ImageNet-pretrained CNNs
	- Natural language processing using pre-trained transformers (BERT, GPT)
=> Especially effective when labeled data for the target task is limited.