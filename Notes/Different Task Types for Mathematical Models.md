A task type defines the form of the mapping or structure a model aims to learn from data.
Given data $(X, Y)$, with inputs $X \in \mathcal{X}$ and outputs or latent variables $Y \in \mathcal{Y}$, the task type specifies:
- what is observed
- what is predicted or inferred
- whether supervision is available
- what form the output takes (continuous, discrete, latent, sequential, generative, etc.)
Although some task types might today be very specific to [[Deep Learning Models]], they are in theory model-agnostic. 
## Supervised or Predictive Tasks
In the case of supervised tasks we have labels $Y$ and try to predict $Y$ from $X$. The inherent goal is to learn a mapping $f: X \to Y$ from labeled data $(X, Y)$. These tasks are **discriminative**: they do not attempt to model the full data distribution, only the conditional $P(Y \mid X)$. 
- Supervised tasks include: [[Classification]], [[Regression]], Sequence labeling, etc.
- Design patterns used: Usually simple feed forward models.
## Unsupervised Tasks
Here we do not have any labels $Y$, we try to learn a structure from $X$. It is important to note, that this is a broad group, and the subsequent task types (representation learning and generative modeling) are also unsupervised, but in a more specific manner. 
- Unsupervised tasks include: [[Clustering]], [[Topic Modeling]], Density Estimation (e.g. used for outlier detection or anomaly detection). 
- Design Patterns used: Clustering algorithms, [[Deep Learning Design Patterns#Normalization Flows|Normalization Flows]].
## Representation Learning (Usually Self-Supervised)
The goal here is to learn **latent representations** $Z = g(X)$ that capture meaningful structure. Representation learning is conceptually distinct because the output is not a prediction (like in traditional unsupervised tasks) or sample (like in generative models), but a _latent code_. 
- Representation learning tasks includes: [[Dimensionality Reduction]], [[Neural Compression]], Embedding learning, denoising, etc.
- Design patterns used: [[Deep Learning Design Patterns#Autoencoders|Autoencoders]] like [[Deep Learning Design Patterns#Masked Autoencoders|MAEs]], [[Deep Learning Design Patterns#Autoregressive Models|Autoregressive models]], [[Deep Learning Design Patterns#Normalization Flows|Normalization Flows]], [[Deep Learning Design Patterns#Generative Adversarial Networks (GANs)|GANs]], [[Deep Learning Design Patterns#Diffusion Models|Diffusion Models]].
## Generative Tasks (Usually Self-Supervised)
Here the goal is to learn the data distribution $P(X$) so that we can *generate* data. 
- Generative tasks include: Image generation, Audio synthesis, Text generation, Video prediction, Speech synthesis, etc.
- Design patterns used: [[Deep Learning Design Patterns#Variational Autoencoders|Variational autoencoders (VAE)]], [[Deep Learning Design Patterns#Autoregressive Models|Autoregressive models]], [[Deep Learning Design Patterns#Normalization Flows|Normalization Flows]], [[Deep Learning Design Patterns#Generative Adversarial Networks (GANs)|GANs]], [[Deep Learning Design Patterns#Diffusion Models|Diffusion Models]].
## Sequence-to-Sequence Tasks
Sequence-to-Sequence tasks try to learn the mapping $X₁…Xₙ → Y₁…Yₘ$. 
- Seq2seq tasks include: Translation, Summarization, or Time-Series Forecasting.
- Design patterns used: [[Deep Learning Design Patterns#Encoder–Decoder Pattern|Encoder-Decoder models]].
## Reinforcement Learning Tasks
Reinforcement Learning or RL is characterized by optimizing actions via some reward. The goal is to learn policy $\pi(a \mid s)$ to maximize expected reward. 
RL tasks include: Dialogue agents with RLHF, Policy learning, and Autonomous decision systems.