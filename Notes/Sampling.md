Sampling is the selection of a subset from the population for further statistical analysis and inference on the properties of the population. Sampling can be done **with replacement** or **without replacement**. Sampling with replacement is often easier to analyze probabilistically because then the samples are **independent**. The simplest sampling scheme is **simple random sampling** whereby we include every member of the population equally likely (uniform distribution). The number 𝑛 of samples drawn is the sample size.

**Estimators**
Sampling is often used to estimate the value of some parameter of the underlying population, for example, the population mean 𝜇. An **estimator** for the parameter is a random variable that we compute from the sample or a best guess for the parameter value, in light of the evidence we gather from the sample. A **sample statistic** is the value we get when we calculate the estimator using actual sample data.

Estimators necessarily have error because we omit some part of the population in the  
sampling process. The sampling itself generates sampling error because even in ideal conditions, the randomness of the sampling process means that the values of the estimator vary from sample to sample. If the estimator has tendency to over- or underestimate the value systematically, we say it is **biased**. The bias of the estimator is the expected difference from the true value. If the estimator is equal to the parameter, then we say the estimator is **unbiased**. For example, by the [[Sampling#Law of Large Numbers|law of large numbers]], the arithmetic mean is an unbiased estimator for the population mean. 

**Population Proportion**
We are often interested in the population proportion: the relative fraction of the population that satisfies some condition. To gauge whether or not or sample size is big enough to significantly represent the population proportion, we can make use of the [[Sampling#Central Limit Theorem|Central Limit Theorem]]. The Central Limit Theorem says that the sample proportion $\hat{p}$, which is the number of objects satisfying a condition divided by the number of objects in the sample, if the sample satisfies the success-failure condition: $𝑛\hat{p} ≫ 10$ and $𝑛(1 − \hat{p}) ≫ 10$.
## Central Limit Theorem
Many statistical methods, such as constructing confidence intervals and performing hypothesis tests, rely on the assumption of normality. The Central Limit Theorem justifies using these methods, even for non-normal data, as long as the sample size is large enough.

The **Central Limit Theorem** states that, regardless of the shape of the population distribution, the sample mean will tend to follow a normal distribution as the sample size becomes large enough, provided the samples are independent and identically distributed (i.i.d.). This result holds even if the original population data is skewed or non-normal. 
We denote this like this: $\bar{X} \sim \mathcal{N}(\mu, \frac{\sigma^2}{N})$.

This leads to two interesting observations:
- The sample mean $\bar{X}$ is around the true mean value $μ$.  
- The “deviation” of $\bar{X}$ from $μ$ is $\frac{\sigma^2}{N}$; the larger $N$, the smaller the deviation.

This is important because we are usually interested in estimating the mean value $μ$. The central limit theorem states that we can use the sample mean $\bar{X}$ to estimate the mean value $μ$. Now the question remaining is: How good is this estimation? 

To answer this question we analyze the estimation error $\mathcal{E} = \bar{X} − μ$. To do this, we first need to introduce two concepts: the standard error and confidence intervals. 
## Standard Error
The standard error is a measure of the variability of a sample statistic. Because we most commonly us it for the mean, we use this formula: $SE = \frac{\sigma}{\sqrt{n}}$. But if we were to for example look at the standard error for the sample proportion, this formula would be different! In the rest of this note when we talk about standard error, we talk about the standard error, of the sample mean. 

We get to the formula ($SE = \frac{\sigma}{\sqrt{n}}$) by standardizing the estimation error ($\mathcal{E} = \bar{X} − μ$). 

It tells you how much the sample mean ($\bar{x}$) would vary if you repeatedly took samples from the same population. It is useful if you want to know how accurate a sample mean is as an estimate of the true population mean. We interpret it like this: A standard error of a sample of 50 people when looking at height of 1.41 cm means that, if you were to take many different samples of 50 people from the same population, the sample means would vary by about 1.41 cm on average from the true population mean.

Standard deviation relates to the spread of individual data points, while standard error relates to the spread of sample means.
## Confidence Intervals
A confidence interval (CI) is a range of values, derived from sample data, that’s likely to contain the true value of an unknown population parameter. It is basically an improvement over the point estimate of an unknown parameter (for example the mean).

The confidence interval is built around this point estimate by adding and subtracting a **margin of error**. The margin of error accounts for sampling variability, helping to create a range of plausible values for the population parameter. The formula for a confidence interval is typically: $\text{CI} = \text{Point Estimate} \pm (\text{Critical Value} \times \text{Standard Error})$

The standard error is explained above. The **critical value** depends on the **confidence level**. A typical confidence level would be 95% and the corresponding critical value would be 1,96. This is computed using the z-score. We use a standard Gaussian distribution in the calculations of the confidence intervals. This means we can use a z-table (or any number of computer functions) to calculate the critical value of a confidence level. The critical value then just corresponds to the upper and lower bound of the quantile of the standard Gaussian distribution. 

A 95% confidence interval of (40, 60) for the average weight of a certain population means that we are 95% confident that the true average weight lies somewhere between 40 and 60. It does **not** mean that 95% of the population has a weight between 40 and 60, or that there’s a 95% chance the true value is in this range. Instead, it’s about the reliability of the sampling process.

**Implications of Confidence Intervals and CLT**
The confidence interval for the sample mean is exact when the data distribution is Gaussian, otherwise it is an approximation under the central limit theorem. This means that: 
- For small sample sizes:
	- If the data is **not Gaussian**, the approximation may not hold, and the CI may not be reliable.
	- Use alternative methods (e.g., bootstrapping or non-parametric methods) if the data is far from Gaussian.
- For large sample sizes:
	- Even if the data is non-Gaussian, the CI formula becomes increasingly accurate due to the CLT.

**Confidence Intervals for unknown Standard Deviation**
When $\sigma$ is unknown, which is the most common case, we replace $\sigma$  by its estimate $\hat{\sigma}$ - the sample standard deviation $s$ - random variable $S$. This means that the standardization of the margin of error is now random instead of constant. This again means that the distribution of this margin of error is no longer the standard Gaussian distribution and we can't simply take the critical value from the z-table. It instead follows a Student’s t-distribution $t$. The Student’s t-distribution has one parameter $df = N − 1$ (degrees of freedom). 

This means that when calculating the critical value we do not look at the z-table, but at the t-table instead. And we, in addition to the confidence level, need to define a degree of freedom beforehand. 

Also, if we have a very large sample size, we know that the sample means will follow a Gaussian distribution (CLT). Then we again can use that "easy" way of calculating the critical value.

**Confidence Intervals for unknown Sampling Distribution**
Here we can use **Bootstrap**. The bootstrap method is a robust approach to constructing confidence intervals when the sampling distribution is unknown. It uses resampling with replacement to approximate the error terms and critical values needed for interval estimation. This method is especially useful for statistics where traditional parametric methods fail or are impractical.
## Law of Large Numbers
The Law of Large Numbers states that as the size of a sample increases, the sample mean (average) will get closer and closer to the population mean (true average of the entire population). In other words, with enough data, the sample statistics (like the mean) become accurate estimates of the population parameters.

This is one reason why data scientists emphasize **big data**, more data generally leads to better and more stable models.
## Sampling from Distributions
Simple random sampling is *distribution-agnostic*. This means that it does not aim to create a specific distribution, only to fairly represent the underlying population. For example, if the population is normally distributed, then a simple random sample will also tend to have a normal distribution. 

Generating samples from specific probability distributions means that the samples, not the population, are designed to adhere to a specific probability distribution. In these sampling methods, we’re not assuming that the population has any particular distribution. Instead, we’re using techniques to produce samples that _mimic_ or _follow_ the target distribution we desire.

This is necessary for simulation, modeling, and hypothesis testing among other things. Many statistical models, simulations, and hypotheses require data that adheres to specific distributions to mimic real-world scenarios. 
### Inverse Transform Sampling
Inverse transform sampling is a general technique for sampling from any given probability distribution. The idea here is to generate a random variable $U$ from a uniform distribution over the interval $[0, 1]$. And then using the properties of the CDF of the probability distribution to get the samples. 

This method is widely used in random number generation because it allows us to transform uniform random numbers into numbers following any desired probability distribution. Let's say we have a random number generator that generates numbers from this distribution: $U \sim \text{Uniform}(0,1)$. Given a cumulative distribution function (CDF) $F(x)$, we can obtain random samples from the distribution by computing: $X = F^{-1}(U)$, where: $X$ follows the target distribution. 
