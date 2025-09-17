Likelihood is a tricky concept to wrap ones head around. It can be confusing what likelihood is in relation to probability. But it's actually really simple: Think of it as a “score” for a data point or a parameter value—the higher the score, the better it explains the observed data - It is a measure of how plausible the something is, given some information.

If we look at a PDF for example. As described here [[Distribution#Probability Density Function for Continuous Random Variables]], the y-axis of this function is **NOT** the probability, but it is the likelihood. Similarly, if we redefine this function so that the parameters of the distribution are the unknowns and the data is the given, it is the likelihood of the parameters. 

Another important note is that in both frequentist and Bayesian statistics, the definition of the likelihood is the same: $L(\theta \mid \text{data}) \propto P(\text{data} \mid \theta)$, it’s always the probability of the observed data, conditional on parameter values.
The difference comes in how this likelihood is use:
	- **Frequentist**: Treats the likelihood as a function to be maximized. The peak is the MLE, a single “best” estimate of θ (see [[Parameter Estimation for Probabilistic Models#Maximum Likelihood Estimation (MLE)]]).
	- **Bayesian**: Uses the likelihood to _update_ the prior into the posterior. Instead of a point estimate, you get an entire distribution over θ (see [[Likelihood and Posterior Distributions#Posterior Distribution]]).

Within the modeling context this slots in like so:
- Start with the **deterministic function** (structure).
- Add a **distribution** to capture uncertainty around that structure.
- Once you observe data, the **likelihood** is exactly the same formula as the distribution’s PDF/PMF, but viewed as a function of the parameters, with the data held fixed.
## Posterior Distribution
The posterior distribution is a Bayesian concept and is not found in frequentist statistics. It denotes *the updated beliefs about parameter values after combining prior assumptions with the likelihood from the observed data (sometimes normalized by the denominator ($P(X)$).* 
Mathematically this is expressed like this: $P(\theta \mid X) = \frac{P(X \mid \theta) \, P(\theta)}{P(X)} \propto \; P(X \mid \theta) \, P(\theta)$. Short note on the function. We use the "proportional to" ($\propto$) symbol because we omit the normalization factor we usually know from the Baysian formula ($P(X)$). 

Getting the posteriori distribution is the main goal of [[Parameter Estimation for Probabilistic Models]] in Bayesian statistics.

Now the intuition:
- **Prior** $P(\theta)$**:** before seeing any data, this encodes how plausible different parameter values are.
- **Likelihood** $P(X \mid \theta$)**:** once we see data X, this tells us how compatible those data are with different parameter values.
- **Product:** multiplying prior × likelihood is the [[Probability#Conditional Probabilities on Events|conditional probability]] of the parameters, given the assumed probability of the parameters and the probability of the data given the parameters.
	- A parameter value with high prior plausibility **and** good fit to the data will get boosted.
	- A parameter value that either looked implausible beforehand **or** fits the data poorly will be down-weighted.
### Posterior Predictive Distribution
The **posterior predictive** is like “running the model” multiple times, each time using a different $p$ sampled from the posterior. Each run produces a new outcome according to the model, which captures **observation (or inherent) randomness**. But by sampling $p$ from the posterior, we also capture **parameter uncertainty**. => The resulting collection of outcomes reflects **both sources of uncertainty** together!

In reality this means that the predictive posterior distribution accounts for more uncertainty and its outcomes spread more than the posterior prediction's! This is shown in the graph below: 
![[Pasted image 20250914134303.png]]

Code for this is here: [[posterior_predictive_distribution.ts]].