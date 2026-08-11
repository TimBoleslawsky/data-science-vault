In this chapter, we discuss the distribution functions of discrete and continuous variables as well as the different forms of distribution. For the expected values and the variance of the different distributions look here: [Expected Value & Variance](Expected%20Value%20&%20Variance.md).

Two important concepts evolve from these probability distributions: [Likelihood and Posterior Distributions](Likelihood%20and%20Posterior%20Distributions.md).
## Distribution Functions
Distribution functions answer the questions: *What is the probability of a specific value or range of values occurring?* and *What is the probability that the value is less than or equal to a certain number?*
### Probability Mass Function for Discrete Random Variables
The probability mass function (PMF) gives the probability of each possible outcome for a **discrete** random variable $𝐹 ∶ 𝑆 → [0,1]$, it gives the probability $p(𝑥) = 𝑃(𝑋 = 𝑥)$. It answers the question: **What is the probability of a specific value occurring?**
### Cumulative Distribution Function for Discrete Random Variables
The cumulative distribution function (CDF) of **discrete** random variables  
$𝐹 ∶ 𝑆 → [0,1]$, it  gives the probability 𝐹(𝑥) = 𝑃(𝑋 ≤ 𝑥). It answers the question: **What is the probability that the value is less than or equal to a certain number?**

Example:
Let the random variable $X$ map the sums of two fair dice to their probability. 

![Pasted image 20240924103004.png](../Images/Pasted%20image%2020240924103004.png)
Then for PMF, $P(X = 7) = 1/6$ and for CDF, $P(X <= 3) = 1/2$
### Probability Density Function for Continuous Random Variables
The probability density function gives us the probability that the possible outcome lies in a range from $a$ to $b$ for a **continuous** random variable $𝑓 ∶ 𝑆 → [0, ∞)$, it gives the probability $𝑃(𝑎 ≤ 𝑥 ≤ 𝑏) = \int_a^b 𝑓(𝑡)d𝑡$. *Important:* the probability of any given value $P(a = x)$ is always $0$.

So what does the y-axis mean in this case? The y-axis of the PDF means that thought of as a score fore each data point on the x-axis. Higher values on the y-axis mean the value of X is “more likely” at that point relative to other points, but the number itself is not a probability. It can therefore also be called the *likelihood*, but this term also has a different meaning in traditional statistics ([Likelihood and Posterior Distributions](Likelihood%20and%20Posterior%20Distributions.md)).

The PDF must satisfy two conditions:
- **Non-negativity**:  $f(x) \geq 0$ for all $x$ in the domain.
- **Total probability equals 1**: The integral of $f(x)$ over the entire domain must equal 1.
### Cumulative Distribution Function for Continuous Random Variables
The cumulative distribution function gives us the probability that the possible outcome is smaller or equal to $x$ range from $a$ to $b$ for a **continuous** random variable $𝑓 ∶ 𝑆 → [0, ∞)$, it gives the probability $𝑃(X ≤ x) = \int_{-\infty}^x 𝑓(𝑡)d𝑡$. 
## Different Forms of Distribution
The different forms of distribution tell us what we can expect the outcome to be. Are the outcomes integers from a...b, are the outcomes "yes" or "no", are the outcomes multiple "yes" or "no's" (an outcome could be: 2 "yes's"), ... It basically tells us what $X$ will look like.
### Discrete Uniform Distribution for Discrete Random Variables
Suppose $X$ takes its values from $n$ integers $a ... b$ such that each integer is equally likely, that is, $𝑃 (𝑋 = 𝑘) = 1/n$ for all 𝑘. Then 𝑋 has a discrete uniform distribution, denoted 𝑋 ∼ 𝑈{𝑎, 𝑏}. The PMF of the discrete uniform distribution looks something like this: 
![Pasted image 20241030141049.png](../Images/Pasted%20image%2020241030141049.png)
### Bernoulli Distribution for Discrete Random Variables
Bernoulli variables describe the outcome of a single experiment that can be answered “yes” or “no”, that is, that behaves like a Boolean value. Bernoulli distribution is denoted $𝑋 ∼ Bernoulli(𝑝).$

Example, let us throw two fair dice:  
- Let 𝑋 be an indicator variable for the event that the sum of the face values is equal to 8  
- There are 5 outcomes with this property out of 36  
- Thus $𝑋 ∼ Bernoulli(𝑝)$ with $𝑝 = 5/36$
- PMF: $P(X = 1) = 5/36$ and $P(X = 0) = 31/36$
- CDF: 
	- For $x < 0: F(x) = 0$
	- For $0 <= x < 1: F(x) = 31/36$
	- For $x >= 1: F(x) = 1$
- The PMF would look something like this: ![Pasted image 20241030141554.png](../Images/Pasted%20image%2020241030141554.png)
### Categorical Distribution for Discrete Random Variables
The categorical distribution for a random variable $X$  that can take $k$ different categories is typically denoted as: $X \sim \text{Categorical}(p_1, p_2, \dots, p_k)$. This just represents a Bernoulli experiment with more than two possible outcomes. 

Example, suppose you have a categorical distribution with categories (e.g., “Red”, “Green”, “Blue”) and their respective probabilities.
- $X \sim \text{Categorical}(p_1, p_2, p_3)$, with $p_1 = 0.2, p_2 = 0.5, p_3 = 0.3$ 
- The PMF would look like this:                    ![Pasted image 20241111133926.png](../Images/Pasted%20image%2020241111133926.png)
### Binomial Distribution for Discrete Random Variables
Let 𝑋 be the sum of 𝑛 independent and identically distributed Bernoulli variables, that is, each $𝑋 ∼ Bernoulli(𝑝)$ and they are independent. We then say that 𝑋 has a Binomial distribution, denoted $𝑋 ∼ Bin(𝑛, 𝑝)$

Example, let us toss a coin five times:
- $𝑋 ∼ Bin(𝑛, 𝑝)$ which $n=10$ and $p=1/2$
- The probability of observing $k$ heads is: $(noverk) * (p)^k * (1-p)^{n-k}$
- The PMF would look something like this: ![Pasted image 20241030141744.png](../Images/Pasted%20image%2020241030141744.png)
### Multinomial Distribution for Discrete Random Variables
The multinomial distribution is a generalization of the binomial distribution. It models the outcome of experiments in which each trial results in one of several discrete categories, but allows for multiple trials. We denote a multinomial distribution as $X \sim \text{Multinomial}(n, p_1, p_2, \dots, p_k)$

We cannot compute the PMF of all the outcomes in two dimensions, but we can plot the PMF for one of these outcomes. Then it just looks like the PMF of the Binomial distribution.
### Geometric Distribution for Discrete Random Variables
Suppose we perform Bernoulli trials with success probability 𝑝 until we observe the first success. Let 𝑋 be the number of trials until the first success, we then say that 𝑋 has geometric distribution, denoted $𝑋 ∼ Geom(𝑝)$

Unfortunately, there are two different interpretations of this distribution which are both called geometric distribution. 
- probability distribution of the number $X$ of Bernoulli trials needed to get one success. (Counts successes and failures)
- probability distribution of the number $Y=X−1$ of failures before the first success. (Counts just failures)

The PMF of a geometric distribution, in this example with $p=0.3$, could look something like this: ![Pasted image 20241030142154.png](../Images/Pasted%20image%2020241030142154.png)

Example, It is estimated that approximately 105 boys are born per 100 girls. Suppose a couple decides to have as many kids as necessary until they have a girl. Let's find the probability that they need to have five kids (the fifth kid is the first “success”):![Pasted image 20240924112912.png](../Images/Pasted%20image%2020240924112912.png)

We can also interpret the question as "We want to find out the probability that we have 4 failures to have a girl". Then we would only count failures and the probability would be calculated like so: $(1-p)^k*p$. But because $k$ in this case would be four and not five we would still get the same result.
### Poisson Distribution for Discrete Random Variables
Suppose events happen in a fixed interval of time or space at a fixed rate independently, what is the number of events 𝑋? We say 𝑋 follows the Poisson distribution with rate 𝜆, denoted $𝑋 ∼ Poisson(𝜆)$. The PMF can be calculated as follows: 
![Pasted image 20240924113709.png](../Images/Pasted%20image%2020240924113709.png)

Example, suppose there are on average 20 visitors to a webpage in an hour, what is the probability that 21 visitors visit the webpage assuming Poisson distribution: 
- $P(X = 21) = {20^{21} * e^{-20} \over 21!}$
- $P(X = 21) ≈ 0.0847$

The PMF of this example looks like this: 
![Pasted image 20241030142410.png](../Images/Pasted%20image%2020241030142410.png)
We can see that this looks very similar to the binomial distribution. This is because the Poisson distribution is an approximation for the Binomial distribution in cases of large $n$ and small $p$.
### Uniform Continuous Distribution for Continuous Random Variables
A uniform continuous distribution is a probability distribution where all outcomes within a given range are equally likely. The probability density function (PDF) of a uniform distribution is constant within a specified interval $[a, b]$ and zero outside that interval.

Let's look at a example where $a=9$ and $b=10$:
- The PDF is 
	- $1 \over b - a$ for $a \leq x \leq b$ 
	- $0$ everywhere else
- The CDF is 
	- $0$ for $x<a$
	- $x-a \over b-a$ for $a \leq x \leq b$ 
	- 1 for $x>b$
- For example the probability of $9.5$ is $0$, because in continuous distributions, the probability of any specific point is 0.
- For example the probability of $x$ being between $9$ and $9.5$ is $P(9 \leq X \leq 9.5) = \int_9^{9.5} 1 \, dx = 9.5 - 9 = 0.5$
- The PDF in this case would look something like this: ![Pasted image 20241030143316.png](../Images/Pasted%20image%2020241030143316.png)
### Exponential Distribution for Continuous Random Variables
The exponential distribution is the continuous analogue of the geometric distribution. It models the amount of time (or distance) you need to wait for an event to happen. When the exponential distribution is denoted as $𝑋 ∼ Exp(𝜆)$ we say that $X$ is distributed with the rate $𝜆$. For example, if  $\lambda = 0.5$, it means, on average, one event occurs every 2 time units (since the rate of 0.5 events per time unit indicates 1 event every $\frac{1}{0.5} = 2$ units of time). The PDF of the exponential distribution looks something like this:
![Pasted image 20241030143400.png](../Images/Pasted%20image%2020241030143400.png)
### Normal Distribution for Continuous Random Variables
The normal distribution is the familiar bell curve: A lot of natural and social phenomena can be modeled with the normal distribution. It is denoted as $𝑋 ∼ 𝒩(𝜇, 𝜎^2)$. The normal distribution is defined by the parameters 𝜇, the mean of the distribution, and 𝜎, the standard deviation. If $𝜇 = 0$ and $𝜎 = 1$, we say the resulting distribution is the standard normal distribution. 

The normal distribution satisfies the *68%–95%–99%* rule. Sixty-eight percent of the probability mass must lie within the region $±1σ$ of the mean. Further, 95% of the probability is within $2σ$, and 99.7% within $3σ$.

The PDF of the normal distribution looks something like this:
![Pasted image 20241030143440.png](../Images/Pasted%20image%2020241030143440.png)
### Power Law Distribution for Continuous Random Variables
The Power Law distribution is used to describe a wide range of phenomena in social, biological, and physical systems where extreme values play a significant role. It is characterized by *preferential growth*. This means that the richer get richer. An example is the wealth distribution. In the distribution that describes the wealth distribution there must be a probability that there exists a "Bill Gates" with 80 Billion dollars of wealth. 

While the exponential distribution is denoted as something where the exponent is a variable $x$, the power law distribution is defined as $P(x) = C x^{-\alpha}$. This leads to the special characteristic, where big events can still happen more often than expected. 

The similarity in the exponential distribution and the power law distribution can also be seen in the PDF of these two distributions. They look very similar but the power law distribution decreases more slowly and denotes a higher probability to large values: ![Pasted image 20241030151117.png](../Images/Pasted%20image%2020241030151117.png)

