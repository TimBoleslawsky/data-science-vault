Bayesian inference is a method of statistical inference where we update our beliefs (probabilities) about an unknown parameter based on observed data. The key idea is that we start with a prior belief, observe data, and then update our belief using Bayes’ theorem to obtain a posterior belief. It is distinctly different to the Frequentist approach to inference, where we rely on hypothesis tests and confidence intervals.
## **Key Components of Bayesian Inference**
Bayesian inference revolves around three main distributions: the **prior**, the **posterior**, and the **predictive distribution**.

**Prior Distribution** $P(\theta)$
The prior represents our initial belief about the unknown parameter $\theta$ before seeing any data. It is often chosen based on past knowledge, expert opinion, or convenience. The choice of prior can significantly impact the inference, especially with small datasets. Because of this we make a distinction between **non-informative prior** and **informative prior**. A non-informative prior (no strong belief) could be $\theta \sim \text{Uniform}(0,1)$, meaning we consider all probabilities equally likely. An informative prior (based on past experience) might be $\theta \sim \text{Beta}(2,2)$, which slightly favors fair coins.

**Posterior Distribution** $P(\theta | D)$
The posterior represents our updated belief about $\theta$ after incorporating observed data $D$. It is obtained using Bayes’ theorem. For example, we could use a Beta prior ($\theta \sim \text{Beta}(2,2)$) and a Binomial likelihood, from which we then compute the posterior distribution for $\theta$. This updated posterior tells us the most probable values of $\theta$ given our prior knowledge and observed data.

**Predictive Distribution** $P(\tilde{D} | D)$
The predictive distribution answers: **“Given the observed data, what do we expect for future observations?”**. It is obtained by integrating over the posterior distribution. The predictive distribution then follows a combination of prior and posterior distribution, for example Beta-Binomial. 
## Hypothesis Test Example
This is how a hypothesis test using the Bayesian approach could look like:
- Define the Hypotheses
	- $H_0$: The null hypothesis (e.g., a coin is fair, $\theta = 0.5$).
	- $H_1$: The alternative hypothesis (e.g., the coin is biased, $\theta \neq 0.5$).
- Obtain the Posterior Distribution
	- Use Bayes’ theorem to update our prior belief based on observed data. The posterior distribution could for example be $\theta | D \sim \text{Beta}(10,4)$ suggesting $\theta$ is likely greater than 0.5.
- Compute the Predictive Distribution
	- Use the posterior to make predictions about future observations. This means we, for example, simulate more coin flips using the posterior.
- Assess the Evidence Against $H_0$
	- We then compare the results of the simulation with the null hypothesis. This answers the question: "How likely is it that what happened in the simulation, happens under the null hypothesis?". We then use the posterior to assess the plausibility of H₀. For example, if the posterior assigns very low probability mass to θ = 0.5, this indicates the coin is very unlikely to be fair. In Bayesian inference, we express results in terms of posterior probabilities rather than binary rejection.

