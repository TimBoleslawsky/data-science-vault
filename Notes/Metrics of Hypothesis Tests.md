**Type I Error ($\alpha$)**
Type I error occurs when the null hypothesis ($H_0$) is rejected when it is actually true (a “false positive”). The probability of committing a Type I error is controlled by the significance level ($\alpha$), which is the threshold used for rejecting the null hypothesis. For example, a significance level of 0.05 means that there is a 5% chance of incorrectly rejecting $H_0$.

A lower $\alpha$ reduces the chance of a Type I error, but at the cost of increasing the chance of a Type II error (failing to reject $H_0$ when it is false).

**Type II Error ($\beta$)**
Type II error occurs when the null hypothesis ($H_0$) is **not rejected** when the alternative hypothesis ($H_a$) is actually **true** (a “false negative”).

**Power**
The power of a hypothesis test is essentially the test’s ability to detect an effect, given that the effect exists. The higher the power, the more likely the test is to detect a true effect (if one exists) and correctly reject the null hypothesis. => $\text{Power} = 1 - \beta$. 

There are a multitude of factors that influence the power of a hypothesis test. For example 
- the **Sample Size** ($n$): Larger sample sizes typically result in higher power because they reduce the standard error (i.e., variability in the data), making it easier to detect a true effect. Smaller sample sizes increase variability, leading to lower power.
- the **Effect Size**: The larger the true effect size (i.e., the difference between the null and alternative hypotheses), the higher the power of the test. A small effect size makes it more difficult to detect a difference and decreases power.