The process how we conduct hypothesis testing is pretty standardized. We now go through all the steps that we need to go through when we talk about hypothesis testing:

**Experiment design**
1. Make a **default statement**. Before formulating the statistical hypothesis, we need to propose a default statement: a “boring” and unsurprising claim that we would like to test. For example: *Drug D is not more effective than a regular diet on average*.
2. Design an **experiment**. Think about how this default statement can be investigated. For example: *Give drug D to N people and record the average weight loss after one month.*
3. Describe the **data** generated from the experiment, the corresponding **random variables**, and the **parameter of interest** and their **estimates**. In this example it could be: 
	- Data: $x_i$ weight loss after one month for $i = 1,··· ,N$ 
	- Random variable: $X_i$ i.i.d.
	- Parameter of interest: the mean of the weight loss $μ_P$
	- Parameter estimate: the sample mean $\hat{μ}_P$.

**Hypothesis definition**
4. Translate the default statement into a statistical hypothesis (a proposed distribution) and call it the **null hypothesis $H_0$**. For example: $H_0:μ_P =2.1$. (This is for the default statement in the example above). 
	- One-sample test: test a data distribution against a theoretical probability distribution, i.e. for a given constant $c$. => $H_0 : θ = c$
	- Two-sample test: test a data distribution against another data distribution. 
	  => $H_0 :θ_1 = θ_2$.
5. Define an **alternative hypothesis $H_A$** (one-tailed or two-tailed). The alternative hypothesis $H_A$ is the complementary (the opposite) to the null hypothesis. For example: $H_A :μ_P > 2.1$. 
	- One-tailed test => $H_A : θ > \beta$ or $H_A : θ < \beta$. Here we make a assumption that the parameter of interest cannot be higher (or lower) than $\beta$. 
	- Two-tailed test => $H_A : θ \ne \beta$ (same as $θ < \beta$ or $θ > \beta$). 

**Express the test statistic, the null distribution and significance level**
6. Find the expression for the **test statistic** $s$. When we calculate the test statistic, we are quantifying the difference between the sample statistic and the parameter stated under the null hypothesis. Its purpose is to determine how plausible the null hypothesis $H_0$ is by observing $s$.                                                                                                                                        The general formula for a test statistic depends on the specific hypothesis test but typically follows this structure: $\text{Test Statistic} = \frac{\text{Observed Value} - \text{Expected Value Under } H_0}{\text{Standard Error of the Statistic}}$ ($\frac{x ̄−2.1}{√σ/N}$, for our example above). 
   The expression could for example be: $s = \frac{x ̄−2.1}{√σ/30}$.
7. Find the expression for the **null distribution** $f(s | H_0)$. When we look at the null distribution, we assume the null hypothesis is true. This means that the parameter of interest (e.g., the population mean) equals the hypothesized value specified in $H_0$ . For example, if  $H_0: \mu = \mu_0$, then the null distribution is centered at $\mu_0$, which we consider the most likely mean of the data under $H_0$.
   The expression could for example be: $f(s \mid H_0) = \frac{1}{\sqrt{2 \pi}} e^{-\frac{s^2}{2}}$.
8. Choose a **significance level $α$**, which defines the rejection region. When choosing a significance level, we need to be mindful: if $H_A$ is one-tailed or two-tailed. A one-tailed $H_A$ is more conservative than a two-tailed, because the rejection region is divided between the two tails. Similar to the confidence interval, $1 − α$ is called the confidence level - “with 95% confidence, rejecting $H_0$ is the right thing to do”. 

**Run the experiment**
1. Run experiments and collect data, Compute the test statistic from data, Compute the p-value.

**Evaluate the experiment**
2. To do this, we need to calculate the **p-value**. The p-value is the probability of obtaining a test statistic at least as extreme as the one observed, assuming that the null hypothesis is true. It helps determine whether the observed data is consistent with the null hypothesis. To calculate the p-value, we can use the CDF of the test statistic $s$ of the null distribution. For a two-tailed test, we multiply this value by two: ![[Pasted image 20241221161149.png]]If $p-value< α$, i.e. the test statistic falls in the rejection region of the null distribution, then we reject the hypothesis $H_0$; otherwise, we fail to reject $H_0$. ![[Pasted image 20241221161331.png]]