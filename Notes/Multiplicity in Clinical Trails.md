**Multiplicity** in this case refers to the **increased risk of false positives** (Type I errors) due to **multiple comparisons**. When researchers perform **multiple hypothesis tests** (e.g., comparing multiple treatments, endpoints, or subgroups), the chance of finding a **statistically significant result by chance** increases.

When we have multiple hypotheses we want to test, we usually denote it like this: 
- Family of a priori stated null hypothesis: ￼$F = {H_1,...,H_N}$
- p-values: $p_1, …, p_n$
We then want to control the type 1 family-wise error rate (FWER):
- $P(\text(Reject at least one true H_i) \leq \alpha$. This is the same as $1 - P(Reject none in error)$ if we assume independence this leads to the following calculation: $1 - (P(Not reject first))^5$ = all tests performed on same level = $1 - (1 - 0.05)^5 ≈ 0.23$
## Types of Multiplicity
In general there are four types of multiplicity in clinical trails: multiple endpoints, multiple treatment arms/doses, interim analysis, and subgroup analysis. Here I only focus on multiple endpoints and multiple treatment arms/doses.
- Multiple Endpoints
	- Many trials test a drug’s effect on **multiple outcomes** (e.g., survival, quality of life, biomarker changes). Each additional test increases the risk of false positives.
	- General strategy: Arrange in three families: primary (needed for regulatory support), secondary (only assed after success on primary), exploratory.
- Multiple Treatment Arms
	- If a trial compares **three drugs vs. placebo**, performing separate tests for each drug increases the risk of false positives.
	- General strategy: Arrange in order of importance. Importance can be if the part of the comparisons is confirmatory or exploratory analysis.
## Comparison Methods
We can categorize the comparison methods into two categories: **p-value-based methods** and **fixed-sequence procedures**. These two categories (there are technically more) reflect different ways of controlling for multiplicity in hypothesis testing. Here’s how they differ and when each is useful:
### P-value-based Methods
The most famous p-value-based methods are the Bonferroni method, the Holm method, and the Hochberg method. Here is how they work: 
![[Pasted image 20250221093449.png]]
- For Bonferroni, we just multiply each p-value times N.
- For Holm, we go from the best/worst p-value and multiply by N, then by N-1. ...
	- If the adjusted p-value of the current $i$ is smaller than the previous one, take the previous one.
- For Hochberg, we go from the worst/best p-value and multiply by 1, then 2, ... until N. 
	- If the adjusted p-value of the current $i$ is higher than the previous one, take the previous one. 
### Fixed-sequence Procedures
The idea behind fixed-sequence procedures is to order the hypotheses after importance. Then check $H_1$ (the most important). If, and only if, we reject $H_1$, check $H_2$. Continue this for all hypotheses. 
