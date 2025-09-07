Below are the most common use cases for deep learning models categorized by skills needed to work within these use cases. This is done, because we can nicely see the distinction between model development and software engineering this way. 
## Task-specific Self Trained Models
The core skills: Data preprocessing, feature engineering, architecture choice (CNNs, RNNs, Transformers, auto-encoders), model training, evaluation.

Some more niche use cases that fit here are:
	- Data Compression & Representation Learning (auto encoders, VAEs → generative tools).
	- Anomaly Detection (unsupervised density modeling, predictive error modeling).
### Predictive Models
The core idea here is to learn statistical patterns between input features and (usually) known outcomes to map the input to the output with the goal of prediction.
### Generative Models
Instead of learning statistical patterns like with predictive models, generative models learn the underlying distribution of data to generate new, plausible samples. Example use cases could be  Synthetic data generation, or image synthesis (GANs, diffusion models).
### Causal Models
The goal here is to capture _mechanisms_ that describe how variables influence each other. We aim to answer questions about interventions and counterfactuals. For the training this often combines statistical estimation with causal constraints (using causal graphs, invariant risk minimization, counterfactual data augmentation).
## RL Models
The main goal here is optimization — “Which actions lead to the best long-term outcome?” The RL “product” is a trained policy that decides actions to optimize long-term outcomes, typically delivered as a control module within a larger system (robot, process simulation, or agent). This is often achieved by starting with a pre-trained model and fine-tuning it (transfer learning).

Core skills: Policy gradient methods, environment design/simulation, exploration strategies, stability tuning, reward shaping. Mostly an extension of RL, but with safety, interpretability, and domain integration being extra skill demands.

Niche use cases that fit here:	
- Model Predictive Control with Learned Dynamics
- Safety-Critical RL (control with constraints)
- Traffic flow optimization, fleet control
- Constraint satisfaction via RL/heuristics
## Generic Agentic Systems
Agentic systems built on large pre-trained models (foundation models). The goal is to be flexible across many tasks. Mainly focused on automation — streamlining human workflows like writing, coding, scheduling, answering queries. Some examples could be: Chatbots, task planners, workflow assistants.

Core skills: Software engineering, orchestration frameworks (LangChain, AutoGen, MCP), tool APIs, prompt engineering, memory design.

