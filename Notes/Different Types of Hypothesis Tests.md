## Z-Test
The z-test is a statistical test used to determine whether there is a significant difference between means or proportions.

- Used when the population variance ($\sigma^2$) or population standard deviation ($\sigma$) is known.
	- This is only important, if we want to test the mean. If we want to test the proportion, we don’t deal with a population standard deviation directly. Instead, the standard deviation (standard error, SE) is computed based on the sample proportion ($\hat{p}$) and the hypothesized population proportion ($p_0$).
- Suitable for **large samples** (n > 30) because the sampling distribution of the mean approximates a normal distribution by the Central Limit Theorem.
- Assumes the data follows a **normal distribution**. For large sample sizes, this is often satisfied regardless of the population distribution due to the Central Limit Theorem.
- Uses the **z-distribution**, which is a standard normal distribution ($N(0, 1)$) with a mean of 0 and a standard deviation of 1.
- Applications:
	- Testing the difference between a sample mean and a population mean (when $\sigma$ is known). Either one or two sample z-test.
	- Comparing proportions (e.g., two-sample Z-test for proportions).
## T-Test
The t-test is a statistical test used to determine whether there is a significant difference between means.

- Used when the population variance or standard deviation is **unknown**, and the sample standard deviation ($s$) is used as an estimate.
	- When we have a two-sample t-test, we usually use the **Welch's t-test**. Technically we could also have two-sample t-test that are not Welch's t-test (sometimes called **pooled t-tests**) but because Welch's t-test is more robust, and we usually cannot guarantee that the variance of both samples is the same, we tend to prefer the Welch's t-test.
- Designed for **small samples** ($n \leq 30$), where the sampling distribution of the mean follows a **t-distribution**, which is broader and has heavier tails than the normal distribution.
- Does not require the sample to follow a normal distribution but assumes the population is approximately normal, especially for small sample sizes.
- Uses the **t-distribution**, which depends on the **degrees of freedom** ($df = n - 1$) and becomes similar to the z-distribution as the sample size increases.
- Applications:
	- Comparing a sample mean to a population mean (one-sample t-test).
	- Comparing means of two independent groups (independent two-sample t-test).
	- Comparing means of two related groups (paired t-test).
		- We use this, when we want to compare two related samples or repeated measurements of the same group to determine whether there is a significant difference between their means. The key aspect of a paired t-test is that the data in the two groups are **dependent**.
	=> Although the general approach for each of these tests is the same, the rejection region differ!
## Binomial Test
The idea behind the binomial test is not very different from the z-test. In the case of the binomial test we want to investigate the proportion of success from a given sample. 

The null distribution is then just a binomial distribution. The formula for the test statistic is:
- when $n$ is small, the test statistic is the exact number of success derived from the sample.
- when $n$ is big, the formula is: $s = \frac{k_0 - N\pi}{\sqrt{N\pi(1 - \pi)}}$, which is the same formula as the z-test uses (simplified).
## McNemar's Test
The McNemar's test in general is used to test if an action have different effects on two different groups. The data we analyze looks like this: ![[Pasted image 20250114192555.png|400]]
- We have two groups ($x_i = 0, x_i = 1$) and two possible effects ($y_j = 0, y_i = 1$). 
- $n_{01}$ counts the subjects of group $0$ that after the action now belong to group $1$. 
- $n_{10}$ counts the subjects of group $1$ that after the action now belong to group $0$. 

McNemar’s test is primarily used to assess whether there is a significant difference in the discordance between the two conditions! We want to test if there is a significant difference between $\frac{n_{01}}{n_{01} +n_{10}}$ and $\frac{n_{10}}{n_{01} +n_{10}}$.

In the McNemar's test the **parameter of interest** is the **discordance**. Discordance is defined as the number of pairs where the before and after groups don't match ($n_{01}, n_{10}$). Because this discordance can vary, we need two versions of the McNemar's test:
1. **Small Discordance: Exact Test**
   - In cases where the number of discordant pairs (**b** and **c**) is small, the **exact test** is used because the assumptions needed for the approximate test (e.g., the chi-square distribution approximation) are not valid. 
   - For small discordance, the test statistic follows the **binomial distribution**, which provides precise p-values without relying on approximations. This ensures the test remains accurate even for small samples or small differences in the discordant counts.
   - The **exact version** is computationally more intensive but necessary for small discordance to maintain statistical validity.

2. **Large Discordance: Approximate Test**
   - When the number of discordant pairs is large, the **approximate test** is more efficient. Due to the **central limit theorem**, the binomial distribution of the test statistic can be approximated by a **chi-square distribution** with 1 degree of freedom.
   - The approximate test is less computationally demanding and faster to compute, making it suitable for large samples where exact methods are unnecessary and computationally expensive.
   - For large discordance, the approximation works well because the difference between the exact binomial and the approximate chi-square distribution becomes negligible.
## F-Test
The F-test is a statistical test used to compare two or more population variances (or standard deviations) to see if they are significantly different from each other. It is most commonly used in the context of **analysis of variance (ANOVA)**, **analysis of covariance (ANCOVA)** and regression analysis.
### ANOVA
The main idea behind and use case for ANOVA is to generalizes the t-test beyond two groups. When talking about ANOVA, we differentiate between a one-way ANOVA test and a two-way ANOVA test. 

**One-Way ANOVA**
The hypotheses for a one-way anova test look something like this: The null hypothesis ($H_0$) assumes all group means are equal, while the alternative hypothesis ($H_1$) states that at least one group mean is different:
- $H_0: \mu_1 = \mu_2 = … = \mu_k$
- $H_1: \text{At least one } \mu_i \text{ is different}$

The idea we use to test these hypothesis is to look if we find evidence that there exists more variation **between** groups than **within** groups, meaning at least one group mean is likely different. For this we need to calculate the mean square due to treatment (between groups) and the mean square due to error (within groups):
-   $MSA = \frac{SSA}{k - 1}$
-   $MSE = \frac{SSE}{N - k}$

Here $k$ is the number of groups/treatments and $N$ is the total number of observations. The $SSA$ and $SSE$ stand for the sum of squares due to treatment ($SSA$) and the sum of squares due to error ($SSE$). $SSA$ and $SSE$ make up the deviation of each individual observation from the overall sample mean ($X_{ij} - \bar{X}$, for each observation in each group). Therefore they are calculated like this: 
-   $SSA = \sum_{i=1}^{k} n_i (\bar{X}_i - \bar{X})^2$
-   $SSE = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_i)^2$

The F-statistic is then calculated like this: $F = \frac{MSA}{MSE}$. A **large F-value** suggests more variation **between** groups than **within** groups, meaning at least one group mean is likely different. A **small F-value** suggests that group means are similar.

**Two-Way ANOVA**
The two-way ANOVA test extends the one-way ANOVA test to consider a second factor. The first factor could for example be the treatment and the second the center. The hypotheses for such a test could then look like this: 
-  $H_0: \alpha_i = 0$ => the treatment has no effect on the mean.
-  $H_0: \beta_j = 0$ => the center has no effect on the mean.
- $H_0: (\alpha\beta)_{ij} = 0$ => the treatment and center combination has no effect on the mean.
### ANCOVA
ANCOVA (Analysis of Covariance) is an extension of ANOVA that includes both categorical and continuous independent variables. It is used to compare group means while controlling for the effect of a covariate (continuous variable). It helps answer: “Do the group means differ after adjusting for a continuous variable?”
For example:
- In a clinical study, if we want to compare the effect of three drugs on blood pressure, but some patients have different initial blood pressure levels, ANCOVA can adjust for the initial blood pressure (covariate) before comparing drug effects.

We do this by combining ANOVA, compares means across categorical groups, and regression, adjusts for a continuous covariate.
## Nonparametric Methods
All statistical inference discussed so far assumes that the data follows a **known distribution**. If this assumption does not hold, the validity of the statistical tests may be questionable. In that case we use nonparametric methods. Here are some examples:
- Wilcoxon Signed Rank Test: This test is the nonparametric equivalent to the paired t-test. 
- Wilcoxon Rank Sum Test: Nonparametric equivalent to the two sample independent t-test. 
- Kruskal-Wallis Test: Nonparametric equivalent to the one-way ANOVA. 

