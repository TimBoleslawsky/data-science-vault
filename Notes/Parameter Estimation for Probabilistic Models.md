If we have some data sample, and we know what underlying distribution this data follows (how this can be for example known: [[Q-Q Plot]]), how do we know the parameter of this distribution? In other words: Suppose we have 𝑛 samples 𝑋1, 𝑋2, ... , 𝑋𝑛 from a probability distribution with a parameter 𝜃 (e.g., 𝑝 for Bernoulli(𝑝) distribution, or 𝜆 for Exp(𝜆) distribution). Now, what is the most likely value $\hat{𝜃}$ for the parameter to have generated the observations?

The probabilistic topics discussed here built upon the basics laid out here: [[Basics of Probability and Statistics for Data Science#Probability and Statistics]], and more specifically, here: [[Likelihood and Posterior Distributions]].
## Frequentist Parameter Estimation Techniques
In the frequentist sense, parameter estimation is pretty simple, its usually MLE.
### Maximum Likelihood Estimation (MLE)
Once we have the likelihood function, all that's left is to formulate the derivative of this function and maximize it. This is why Maximum Likelihood Estimation is an optimization problem. The maximum likelihood estimator is the value for 𝜃 that maximizes the likelihood. Here is an example: 
- PMF: $f(x \mid \mu, \sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$
- Let's say we know a data point $x=4$ and that $\sigma = 2$. 
- Then our likelihood function looks like this: $L(\mu | x=4, \sigma=2) = \frac{1}{\sqrt{8\pi}} e^{-\frac{(4 - \mu)^2}{8}}$

In the above example, we assumed that we only have one data point. This is obviously not realistic or practical. When we have more than one data point, we have to look at the **joint probability distributions** of the random variables. This is defined as so: 
- $X, Y$ discrete: joint PMF $f_{X,Y} (x,y) = P(X = x,Y = y)$
- $X, Y$ continuous: joint PDF $f_{X,Y}(x,y) = P(X ≤x,Y ≤y)$
The problem is, that this quite hard to obtain, therefore we assume [[Probability#Independence|independence]] (in practice this is usually a reasonable assumption). Because of the properties of independence the terms for PMF/PDF generalize to the product of the PMF/PDF of all random variables. 

In the above example, we also assume, that $\sigma$ is known. If we have multiple unknown parameters, we just need to solve the likelihood function for all of them. The good thing here is that the parameters usually are independent and therefore the maximization (minimization) is not affected by either parameter. 

An additional important note is, that we usually minimize for the **negative log likelihood**. This is mainly so the calculations are easier (product => sums) and for standardization. This leads to the objective function: $\hat{θ}_{MLE} = arg min −logL(θ|data)$.
## Bayesian Parameter Estimation Techniques
Parameter estimation in the Bayesian sense is a little more complex. When talking about the parameter estimation in the Bayesian sense, we usually mean the [[Likelihood and Posterior Distributions|posterior distribution]]. This posterior distribution can be calculated analytically by multiplying the priors with the likelihood and normalizing it with the denomintor, but this is usually not feasible in the real world. Here is why:
- The denominator $P(X)$ is just the probability of seeing the observed data, under the entire model.
- Since the model allows many possible parameter values $\theta$, you must average (integrate) the likelihood across all of them, weighted by how plausible each $\theta$ was a priori. That's how we get => $\int P(X \mid \theta) P(\theta) d\theta$ (for continues variables).
- In most realistic models, that integral is **not analytically tractable**!

This means that we have different techniques to estimate the posterior distribution in Bayesian parameter estimation. 
### Maximum A Posteriori (MAP) Estimation
MAP is different from the other parameter estimation techniques, because it only gives a point estimate, not the full posterior distribution. It is essential a short cut, when we don't want to calculate the full distribution. But when doing this, we also lose the uncertainty!

MAP estimation incorporates both the observed data (through the likelihood, as in MLE) and prior beliefs (through the prior). It is particularly useful when the sample size is small, or when we have prior information that we want to use in the estimation. When no prior is used (or an uninformative prior is assumed), MAP simplifies to MLE.

The MAP estimation is based on Bayesian statistics and is therefor calculated as: $P(\theta \mid X) = \frac{P(X \mid \theta) P(\theta)}{P(X)}$. But $P(X)$ is independent of $\theta$ and can therefore be ignored. This leaves us with $P(X \mid \theta)$, which is the likelihood of the observations, given parameter value 𝜃, like in MLE, and $P(\theta)$ which is the prior probability of the parameter value (the degree of belief in a particular value before observing the evidence). *Note: this is just the posterior distribution described here ([[Likelihood and Posterior Distributions#Posterior Distribution]]). MAP gives us a point estimate from this distribution.* This leads us to the objective function: $\hat{θ}_{MAP} = arg min −logL(θ|data)-logf_θ(θ)$.
### Grid Approximation
The idea behind grid approximation is quite simple. Unfortunately it does not hold up in practice, as it becomes computationally infeasible with more than ~2–3 parameters (curse of dimensionality).

Here is how it works:
- Define our model and our priors and distributions. We want to estimate the parameters of this distribution. 
- Assume that the parameters can only assume certain values (the grid). 
- Compute the prior for each assumed value. 
- Compute the likelihood for each parameter, by plugging in the data and parameter for each assumption. 
- Compute the unnormalized posterior for each grid point $\theta_i$: $\text{UnnormalizedPosterior}(\theta_i) = \text{Likelihood}(\theta_i) \times \text{Prior}(\theta_i)$
- Normalize the posterior by dividing each unnormalized posterior value by the sum of all values: $\text{Posterior}(\theta_i) = \frac{\text{UnnormalizedPosterior}(\theta_i)}{\sum_j \text{UnnormalizedPosterior}(\theta_j)}$. (This is the same as the denominator of the Bayesian formula, just numerically and not analytically!)
### Quadratic Approximation (quap)
The idea is, that the region near the peak of the posterior distribution will be nearly Gaussian—or “normal”—in shape. This means the posterior distribution can be usefully approximated by a Gaussian distribution. A Gaussian approximation is called “quadratic approximation” because the logarithm of a Gaussian distribution forms a parabola.

Here is how it works:
- Find the posterior mode. This is usually accomplished by some optimization algorithm like [[Parameter Estimation for Probabilistic Models#Maximum A Posteriori (MAP) Estimation|MAP]].
- Once you find the peak of the posterior, you must estimate the curvature near the peak. This curvature is sufficient to compute a quadratic approximation of the entire posterior distribution. In some cases, these calculations can be done analytically, but usually your computer uses some numerical technique instead.

=> Problem: Only accurate if the true posterior is close to Gaussian and needs enough data points (common frequentist problem).
### Markov Chain Monte Carlo (MCMC)
**Idea**: Simulate a Markov chain that wanders through parameter space, spending time in regions proportional to posterior probability. Collecting samples from the chain approximates the posterior. => TBD