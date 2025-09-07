## Quantile Function and CDF
Before talking about the Q-Q plot, we have to introduce an important fact: The quantile function $Q$ of a probability distribution function, is the inverse of the CDF of this probability distribution function. $F_x(Q(p)) = p$ and $Q(F_x(q)) = q$

In other words, let's say we have a normally distributed random variable. The CDF gives us that $F(5.10) = 0.17$, meaning that the probability $p$ that $X$ is smaller or equal to $5.10$ is $0.17$. The quantile function gives us that $Q(0.17) = 5.10$, meaning that the value that incapsulates the 0.17-quantile is $5.10$. Both describe this in different ways, $P(X \leq 5.10) = 0.17$. 

In Python, the function `stats.norm.ppf` in the `scipy.stats` module computes the **percent-point function** (PPF) which is the same as the quantile function. 
## Q-Q Plot
Given what we know about the quantile function and the CDF, the intuition is that similar distributions should have similar quantiles. We make use of this with the Q-Q plot (or quantile-quantile plot). The Q-Q plot is a scatter plot of two sets of quantiles and it's purpose is to compare two distributions. 

Usually, we compare a data distribution (of a sample) to a theoretical probability distribution **(one sample test)** or two samples, to see if they are from the same distribution (**two sample test**). 

We plot the Q-Q plot by first taking a set of $m$ probabilities $p_1,p_2,...,p_m$ and making sure that they are evenly spread between 0 and 1. Now for each $i = 1,2,...,m$ we compute the quantile $q1_i$ and $q2_i$ of both distributions we want to evaluate and compare them in a scatter plot with points ($q1_i,q2_i$). 

When interpreting a Q-Q plot there can be different cases: 
- If the points lie on a 45-degree straight line, the distributions are identical. 
- If the points lie on a straight line, which is not 45 degrees, it indicates that our data follows the shape of the theoretical distribution but with different scale (variance) or location (mean) parameters (also denoted as they are from the same **location-scale family**). 
- If the points do not lie on a straight line, the two distributions are from different families of distribution. 