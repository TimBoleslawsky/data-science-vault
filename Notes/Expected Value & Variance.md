## The Expected Value
The expected value is the weighted average of values of random variables. It is the equivalent of the mean in statistics. The expected value can be calculated by multiplying all possible outcomes with their probability and summing these values. If we have a simple example calculating the expected value could look like this:
$E[X] = P(X = 100) * 100 + P(X = 50) * 50 + P(X = 30) * 30$
### Expected Value of Bernoulli Distribution
Let $𝑋 ∼ Bernoulli(𝑝)$
Thus, $𝑃(𝑋 = 1) = 𝑝$ and $𝑃(𝑋 = 0) = 1 − 𝑝$  
Therefore, $E[𝑋] = 1 ⋅ 𝑃(𝑋 = 1) + 0 ⋅ 𝑃(𝑋 = 0) = 𝑝$

Examples Let $𝑋, Y, Z ∼ Bernoulli(𝑝)$
- $E[𝑋+𝑌+𝑍] = 3p$
- $E[(𝑋+𝑌+𝑍)^2] = 3E(X^2) + 6E(XY) = 3p + 6p^2$
### Expected Value of Geometric Distribution
Let's say we have a geometric distribution of form $𝑋 ∼ Geometric(𝑛, 𝑝)$

For the expected value of geometric distribution, we have to differentiate between the two interpretations mentioned here: [[Distribution#Geometric distribution]]

If we define the expected value as the first success we calculate the expected value like this: 
$E[X] = {1-p \over p}$
If we define the expected value as the failures until the first success, we calculate the expected value like this: $E[X] = {1 \over p}$
### Expected Value of Binomial Distribution
Let's say we have a binomial distribution of form $𝑋 ∼ Bin(𝑛, 𝑝)$.
Then the expected value is given by $E[X] = np$.
### Expected Value of Poisson Distribution
Let's say we have a poisson distribution of form $𝑋 ∼ Poisson(𝜆)$.
Then the expected value is given by $E[X] = 𝜆$.
### Expected Value of Uniform Distribution
Let's say we have a poisson distribution of form $𝑋 ∼ U(a, b)$.
Then the expected value is given by $E[X] = {b + a \over 2}$.
### Expected Value of Exponential Distribution
Let's say we have a poisson distribution of form $𝑋 ∼ Exp(𝜆)$.
Then the expected value is given by $E[X] = {1 \over 𝜆}$.
### Expected Value of Normal Distribution
Let's say we have a poisson distribution of form $𝑋 ∼ 𝒩(𝜇, 𝜎^2)$.
Then the expected value is given by $E[X] = 𝜇$.
## The Variance
The variance gives the average spread of the values around the mean. It is calculated either by $Var[X] = E[(𝑋 − E[𝑋])^𝑘]$ or by $Var[X] = E[X^2] - E[X]^2$.

Constants do not matter when talking about variance, therefore $Var[X - 5] = Var[X]$.
But if we have a variance of $Var[5X] = 5^2 Var[X]$.

We can calculate the **standard deviation** (basically Variance in unit of measurement) from the variance by taking the square root: $Std[X] = \sqrt{Var[X]}$

- Variance of Bernoulli distribution: $Var[X] = pq$
- Variance of Geometric distribution: $Var[X] = {1-p \over p^2}$
- Variance of Binomial distribution: $Var[X] = npq$
- Variance of Poisson distribution: $Var[X] = 𝜆$
- Variance of Uniform distribution: $Var[X] = {(b-a)^2 \over 12}$
- Variance of Exponential distribution: $Var[X] = {1 \over 𝜆^2}$
- Variance of Normal distribution: $Var[X] = 𝜎^2$

