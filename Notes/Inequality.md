## **Markov’s Inequality**
Markov’s inequality says that the probability that a non-negative random variable exceeds a certain threshold is at most the ratio of its mean to the threshold. It doesn’t require any information about the distribution of $X$ beyond its expectations, making it a very general inequality.

Formula: $P(X \geq a) \leq \frac{\mathbb{E}[X]}{a}$

Example: Suppose a non-negative random variable $X$ has a mean  $\mathbb{E}[X] = 10$ . Markov’s inequality tells us that the probability that  $X \geq 20$  is at most 0.5 (50%).

Used when you have a random variable and only know its expectation, but need to bound the probability that it takes on large values.
## **Chebyshev’s Inequality**
Chebyshev’s inequality provides a general bound on how much a random variable can deviate from its mean, regardless of the underlying distribution. It says that the probability of being more than $k$ standard deviations away from the mean is at most $\frac{1}{k^2}$. This result is particularly useful when little is known about the distribution except for the mean and variance.

Formula: $P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$

Example: Suppose $X$ is a random variable with mean $\mu = 100$ and variance $\sigma^2 = 25$  (standard deviation $\sigma = 5$). For $k = 2$, Chebyshev’s inequality tells us that the probability that $X$ lies outside the range $[90, 110]$ (i.e., 2 standard deviations from the mean) is at most 25%.

Useful for bounding the probability of large deviations from the mean, especially when the distribution is unknown but the variance is finite.
