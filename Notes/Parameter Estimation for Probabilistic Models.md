If we have some data sample, and we know what underlying distribution this data follows, how do we know the parameter of this distribution? In other words: Suppose we have 𝑛 samples 𝑋1, 𝑋2, ... , 𝑋𝑛 from a probability distribution with a parameter 𝜃 (e.g., 𝑝 for Bernoulli(𝑝) distribution, or 𝜆 for Exp(𝜆) distribution). Now, what is the most likely value $\hat{𝜃}$ for the parameter to have generated the observations?

Short note on the function: $P(C_k | X) \propto P(C_k) \cdot P(X | C_k)$. We use the "proportional to" ($\propto$) symbol because we omit the normalization factor we usually know from the Baysian formula        ($P(X)$). So the function means that $P(C_k | X)$ is proportional to $P(C_k) \cdot P(X | C_k)$.
## Maximum Likelihood Estimation (MLE)
The first terminology we have to define is **likelihood**. The likelihood denotes, how likely a certain parameter value 𝜃 is, given some data. We can read the likelihood from the PMF/PDF of a discrete/continuous random variable. Because we want to maximize the likelihood, we need the likelihood function.

The **likelihood function** denotes the probability of observing the particular values for the sample, assuming a certain parameter value 𝜃. To do this we take the PMF/PDF of a random variable and redefine it, so that 𝜃 is the unknown variable. For a Gaussian distribution, this could look like this: 
- PMF: $f(x \mid \mu, \sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$
- Let's say we know a data point $x=4$ and that $\sigma = 2$. 
- Then our likelihood function looks like this: $L(\mu | x=4, \sigma=2) = \frac{1}{\sqrt{8\pi}} e^{-\frac{(4 - \mu)^2}{8}}$
Now all that's left is to formulate the derivative of this function and set it to $0$ to maximize it. This is why Maximum Likelihood Estimation is an [[Optimization Problems|optimization problem]]. The **maximum likelihood estimator** $\hat{𝜃}$ is the value for 𝜃 that maximizes the likelihood.

In the above example, we assumed that we only have one data point. This is obviously not realistic or practical. When we have more than one data point, we have to look at the **joint probability distributions** of the random variables. This is defined as so: 
- $X, Y$ discrete: joint PMF $f_{X,Y} (x,y) = P(X = x,Y = y)$
- $X, Y$ continuous: joint PDF $f_{X,Y}(x,y) = P(X ≤x,Y ≤y)$
The problem is, that this quite hard to obtain, therefore we assume [[Probability#Independence|independence]] (in practice this is usually a reasonable assumption). Because of the properties of independence the terms for PMF/PDF generalize to the product of the PMF/PDF of all random variables. 

In the above example, we also assume, that $\sigma$ is known. If we have multiple unknown parameters, we just need to solve the likelihood function for all of them. The good thing here is that the parameters usually are independent and therefore the maximization (minimization) is not affected by either parameter. 

An additional important note is, that we usually minimize for the **negative log likelihood**. This is mainly so the calculations are easier (product => sums) and for standardization. This leads to the objective function: $\hat{θ}_{MLE} = arg min −logL(θ|data)$

In the image below different relevant concepts are depicted. By comparing them we can clearly see what the differences are. 
![[Pasted image 20241120130819.png|400]]
## Maximum A Posteriori (MAP) Estimation
MAP estimation incorporates both the observed data (through the likelihood, as in MLE) and prior beliefs (through the prior). It is particularly useful when the sample size is small, or when we have prior information that we want to use in the estimation. When no prior is used (or an uninformative prior is assumed), MAP simplifies to MLE.

The MAP estimation is based on baysian statistics and is therefor calculated as: $P(\theta \mid X) = \frac{P(X \mid \theta) P(\theta)}{P(X)}$. But $P(X)$ is independent of $\theta$ and can therefore be ignored. This leaves us with $P(X \mid \theta)$, which is the likelihood of the observations, given parameter value 𝜃, like in MLE, and $P(\theta)$ which is the prior probability of the parameter value (the degree of belief in a particular value before observing the evidence). This leads us to the objective function: $\hat{θ}_{MAP} = arg min −logL(θ|data)-logf_θ(θ)$

**Choice of the Prior**
If we want to use MAP, sometimes the prior is given, for example, when we have domain knowledge, but sometimes we need to choose it ourselves. 
1) The first thing we need to keep in mind, is to choose a suitable distribution for the prior. If it’s unknown, we typically use something called a **conjugate prior**. A conjugate prior is a type of prior distribution, that when combined with a specific likelihood function, results in a posterior distribution that belongs to the same family as the prior. We can look up conjugated priors on the internet. 
2) We also need to choose the parameters for the priors. These are hyperparameters. But, given enough data, MAP returns the same estimate even for different priors.

**MLE vs. MAP**
The big difference between MLE and MAP is that MLE is a frequentist approach ([[Two Approaches to Statistics]]), while MAP is a bayesian approach. This means that MLE does not assume $θ$ to be drawn from a random distribution, but MAP does. This also means that MAP has hyperparameters, while MLE does not. The objective functions are relatively similar with the exception of the **regularization** ($f_θ(θ)$)

