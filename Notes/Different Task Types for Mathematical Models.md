  A **task type** defines the **form of the mapping or structure** the model aims to learn from data. Formally, let the data be $(X, Y)$, where $X \in \mathcal{X}$ is input and $Y \in \mathcal{Y}$ is output (possibly unobserved or latent):
## Regression
In mathematical modeling, **regression** is a statistical technique used to describe the relationship between one dependent variable (the outcome you want to predict or explain) and one or more independent variables (the inputs or predictors). The goal is to approximate a continuous mapping $f: \mathcal{X} \to \mathbb{R}$. Mathematically this means: learn $\hat{f}$ such that $\hat{f}(X) \approx Y$ and some loss $L(Y, \hat{f}(X))$ is minimized (e.g., mean squared error).

This key idea can be extended to more complex tasks:
- **Simple regression**: Models the relationship between one predictor $x$ and one outcome $y$. For example, linear regression assumes: $y \approx \beta_0 + \beta_1 x$    
- **Multiple regression**: Extends this to several predictors $x_1, x_2, \ldots, x_p$: $y \approx \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p$. More on the benefits here: [[Multiple Regression]].
- **Nonlinear regression**: The relationship is not restricted to straight lines, e.g. exponential, logistic, or polynomial models.
## Classification
Similarly to regression, the goal is to approximate a mapping. But his time the mapping is to a discrete set of labels $f: \mathcal{X} \to \{1, \dots, K\}$. This is often modeled probabilistically as $\hat{p}(Y|X)$, with a predicted label $\hat{Y} = \arg\max_k \hat{p}(Y=k|X)$.
## Clustering
Clustering is the problem of assigning meaningful labels to unlabeled points by grouping them. The difference between clustering and classification is that in classification we know our labels beforehand, in clustering, we do not. Therefore, clustering is unsupervised learning.

The goal is to uncover latent group structure in $X$ without labels. Mathematically this means, we want to learn a function $g: \mathcal{X} \to \{1, \dots, K\}$ assigning points to clusters, or a latent representation $Z \in \mathbb{R}^d$ where clustering structure is more evident.

**Is data "clusterable"?**
The general idea is to compare the data distribution with a theoretical distribution with no clustering tendency! This can be done with a [[Q-Q Plot]], which is difficult for higher dimensions, or by computing the pairwise distance.

We can categorize our clustering models into four categories:
- Centroid clustering 
- Distribution clustering
- Density clustering 
	=> These three are sometimes more generally categorized into *partitional* clustering.
- Hierarchical clustering
## Dimensionality Reduction
The basic idea of dimensionality reduction is to learn a continuous low-dimensional embedding that preserves essential structure. The question we want to answer is: "How can I summarize or compress the data while retaining structure?" So the goal is to learn a lower-dimensional representation $Z = h(X)$ capturing the essential structure of $X$. Often defined to minimize reconstruction error $\|X - f(h(X))\|$ or preserve certain properties (variance, topology, distances).

This can seem similar to clustering and that is because it is. Many dimensionality reduction methods are used as a preprocessing step for clustering. And some methods attempt to do both simultaneously. So both are unsupervised and often share techniques (e.g., PCA, autoencoders), but their objective functions and outputs differ.
- Clustering = discrete latent structure (categorical assignments).
- Dimensionality reduction = continuous latent structure (coordinates in latent space). 
