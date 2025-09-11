**Modeling** is the process of encapsulating information into a tool that can forecast and make predictions (more Information about the theory behind mathematical modeling can be found here [[Mathematical Thinking]]).
## Statistical Intuition
In essence, every model is just a function! If we want to make it more specific, we can say that a model is a **function meant to represent a generative process** (a “small world” that produces the data).

In the **small world**, a statistical model contains all nominated possibilities. Surprises are excluded by definition. Here, we can judge whether a model is logically consistent. The small world is where models are built, tested, and understood.

The **large world** is the broader context of reality, where models inevitably face events and structures not imagined in their design. A model that performs perfectly in the small world may fail in the large world because of unanticipated complexities, omitted factors, or incorrect assumptions. Thus, logical coherence inside the model is no guarantee of real-world success.

=> Passing between these two worlds is the central challenge of statistical reasoning!

**To make this more concrete and introduce some statistical concepts, we can frame it like:**

At its core when we do mathematical modeling we represent relationships between quantities. Sometimes we also want to model **uncertainty** (because we want to infer or predict something we have no certainty about).

- In a **deterministic model**, the relationship is captured entirely by a function, e.g., $y = \alpha + \beta x$. Once inputs are known, the output is fixed. There are no random variables.
	
- In a **probabilistic model**, we add uncertainty. Random variables represent the uncertain quantities (observations, parameters, noise). So the random variable tells us _what_ is uncertain within a function (e.g., customer spend, class label, weight).

Now while the function models deterministic structure (e.g., “weight increases with height”), the distributions model uncertainty around that structure (e.g., “even given height, weights vary normally around the line”). So the distributions tell us _how_ that uncertainty is structured (what values are more likely, how spread out they are).

=> Together, function + (optionally) distribution = full statistical model. _That’s why every statistical model is, at its core, a set of variables tied together by functional assumptions, and in probabilistic models also by distributional assumptions!_

More on this from the statistical side, here: [[Basics of Probability and Statistics for Data Science#Connecting Probability and Statistics to Modelling]].
## Terminology
In data science, we describe mathematical models like this: $y = g(x;θ | h)$

Left-hand side:
- $y$: target or label - what you want to predict; a result that answers the question at hand. 
Right-hand side:
- $x$: variables or features (input) - placeholder for data in order to solve a range of problems.
- $g$: model (known) - a mathematical function that is used to solve a given range of problems.
- $h$: hyperparameters (known) - part of the model $g$ (given or derived from your assumption).
- $θ$: parameters (unknown) - part of the model $g$; needs to be estimated from data.
### Notational Differences in Bayesian vs. Frequentist Modeling
**Frequentist example**
Linear regression with Gaussian errors: $y = \beta_0 + \beta_1 x + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \sigma^2)$
- $y$: target variable
- $x$: feature
- $\beta_0, \beta_1$: fixed but unknown parameters
- $\varepsilon$: random noise
- Inference: estimate $\hat{\beta}_0$, $\hat{\beta}_1$ from data (point estimates or confidence intervals).

**Bayesian example**
Bayesian linear regression: $\begin{aligned} y \mid x, \beta_0, \beta_1 &\sim \mathcal{N}(\beta_0 + \beta_1 x, \sigma^2) \\ \beta_0 &\sim \mathcal{N}(0, 10^2), \quad \beta_1 \sim \mathcal{N}(0, 10^2) \end{aligned}$
- $y$: target variable
- $x$: feature
- $\beta_0$, $\beta_1$: random variables with prior distributions
- $\sigma^2$: usually fixed or also treated as a random variable with a prior
- Inference: compute **posterior distributions** $p(\beta_0, \beta_1 \mid \text{data})$ to quantify uncertainty.

