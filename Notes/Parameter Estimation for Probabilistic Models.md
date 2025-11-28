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
Parameter estimation in the Bayesian sense is a little more complex. When talking about the parameter estimation in the Bayesian sense, we usually mean the [[Likelihood and Posterior Distributions|posterior distribution]]. This posterior distribution can be calculated analytically by multiplying the priors with the likelihood and normalizing it with the denominator, but this is usually not feasible in the real world. Here is why:
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
The idea here is to simulate *chains* that wanders through parameter space, spending time in regions proportional to posterior probability. Collecting samples from the chain approximates the posterior. 

The basic intuition behind all MCMC algorithms, is, that calculating actual probabilities is often infeasible (because of the denominator in the Bayes' rule). E.g.:

$P(Z,\theta,\phi \mid w) = \frac{P(Z, w, \theta, \phi)}{P(w)}$, $P(w)$ is way to large to calculate. 

so we look to *relative probabilities*. MCMC algorithms never calculate exact probabilities, but always see, if a probability of state a is better or worse than probability of state b. E.g.:

$\frac{P(Z^{(1)},\theta^{(1)},\phi^{(1)} \mid w)} {P(Z^{(2)},\theta^{(2)},\phi^{(2)} \mid w)} = \frac{P(Z^{(1)}, w, \theta^{(1)}, \phi^{(1)})} {P(Z^{(2)}, w, \theta^{(2)}, \phi^{(2)})}$, this gives us the comparison of probabilities between two states.

This leads to two things: (1) We can spend more time in high probable areas of the posterior distribution, because we can compare each new state to the old one. (2) Therefore the behaviour automatically normalizes, even if we do not know the denominator. 
#### The Metropolis Algorithm
The Metropolis algorithm serves as the foundation of Markov Chain Monte Carlo (MCMC). The idea is, that instead of calculating the full posterior distribution directly, we generate samples that approximate it. Here is how it works:
- **Procedure**:
	1. Start with an initial guess for parameters.
	2. Propose a small random change (a “jump”).
	3. Compute the probability ratio between the new parameter values and the old ones using the posterior (likelihood × prior).
		- Given some data, a likelihood, and a prior
		- Put in the value of the parameter for the current guess ($\text{posterior}(\mu)$)
		- Put in the value of the parameter for the next guess ($\text{posterior}(\mu’)$)
		- Compute the ratio: $r = \frac{\text{posterior}(\mu’)}{\text{posterior}(\mu)} = \frac{0.218}{0.169} \approx 1.29$ 
		  => Since $r > 1$, the new proposed parameter value is **more likely under the posterior**, so we always accept it. If the new value had $r < 1$ (say $r=0.3$), we would still accept it 30% of the time. This prevents the chain from only climbing uphill (like greedy hill-climbing).
	4. Accept the new value with that probability, otherwise stay at the current value.
- Over many iterations, the chain “wanders” through parameter space in proportion to posterior density.

Unfortunately, this becomes very inefficient in high dimensions, because the jumps or walks are random and can get stuck.
#### Hamilton Monte Carlo
Hamilton Monte Carlo or HMC is introduced as a solution to Metropolis inefficiency. The idea is, that instead of random small jumps, use physics (Hamiltonian dynamics) to propose moves. So the computation of the probability ratio is exactly the same, just the proposal generation differs.
- Imagine parameters as positions in space and introduce **momentum** variables that help guide movement.
- By simulating the dynamics (like a ball rolling across a landscape shaped by the posterior), HMC proposes distant points that still have high acceptance probability.
- **Advantages over Metropolis**:
	- Moves faster through correlated parameter spaces.
	- Reduces random-walk behavior.
	- Samples are less correlated, giving more “independent” draws.
#### Gibbs Sampling
Gibbs sampling is an alternative MCMC algorithm to HCM. Here is how it differs from Hamilton Monte Carlo.

Gibbs sampling works by **iteratively sampling each variable from its conditional distribution** given the current values of all other variables.

**Procedure:**
1. Initialize all variables $\theta_1, \theta_2, …, \theta_d$ to some values.
2. For each iteration:
	- Sample $\theta_1$ from $P(\theta_1 \mid \theta_2, …, \theta_d, X)$
	- Sample $\theta_2$ from $P(\theta_2 \mid \theta_1, \theta_3, …, \theta_d, X)$
	- Continue for all variables $\theta_d$.
3. Repeat until convergence; the collected samples approximate the **joint posterior distribution**.

=> Both HCM and Gibbs sampling are MCMC methods, so they solve the same **posterior sampling problem**, but Gibbs holds all but one parameter of the distribution fixed so it moves *coordinate-wise*. 

**Collapsed Gibbs Sampling**: In many Bayesian models (e.g., LDA), directly sampling all parameters can be inefficient or unnecessary. Some parameters can be **integrated out** (collapsed) to reduce dimensionality.

**How it works:**
1. Integrate out parameters like $\theta$ and $\phi$ in LDA.
2. Sample only the **latent assignments** $z$ (e.g., topic assignments for words).
3. Posterior distributions of the collapsed variables can be computed **directly from counts**, improving convergence and mixing.
#### Diagnostics and Plotting
Investigating MCMC through plotting is almost always a good idea. These plots can show is, if the algorithm (and each individual chain) converges to reasonable and similar distributions. 

**Diagnosing with Trace Plots**
- A **trace plot** shows how sampled values evolve across iterations.
- For well-mixing chains:
	- The trace looks like a “hairy caterpillar,” bouncing freely across the posterior region.
- For poorly mixing chains:
	- The trace sticks in one region, then slowly drifts—sign of strong autocorrelation.
- Helps detect convergence issues and if multiple chains are exploring the same posterior region.

**Diagnosing with Pair Plots**
- A **pair plot** visualizes correlations among parameters in the posterior samples.
- Shows 2D scatter plots of samples from two parameters at a time.
- Useful for:
	- Detecting **correlations** between parameters.
	- Identifying “funnels” or “banana shapes” in the posterior geometry that can make sampling hard.
- With HMC, pair plots often look cleaner compared to Metropolis because HMC handles correlations better.

Important diagnostics to know:
- Effective sample size. A good rule of thumb is 10% of the total sample size, i.e., 4 chains running for 1000 iterations leaves us with 4000 samples, of which half are thrown away as warmup; thus 200 is a minimum in this case.
- Divergences mean that the geometry of the posterior is problematic, so HMC trajectories can’t follow it accurately, and the chain fails to explore all of the posterior. One common cause is that weak priors allow extreme parameter values, creating pathological shapes. Making priors more informative can sometimes help, but the standard fix is to reparameterize the model (e.g. non-centered parameterization) and/or adjust HMC tuning (like adapt_delta).
- $\hat R$ compares within-chain variance to between-chain variance.
	- If all chains mix well and explore the same posterior region, they should look like random draws from the same distribution. Then within-chain and between-chain variance will be nearly equal → $\hat R \approx 1$.
	- Modern practices require $\hat R < 1.01$. If it’s above 1.01, the chains have not converged, meaning different chains are stuck in different regions, or not mixing well.
	- What can we do? The easiest fix is to run longer chains. This allows more time to mix. But sometimes only reparameterizing the model can actually help.

