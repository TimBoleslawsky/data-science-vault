When we do sample size calculation, we have two possible goals:
- To achieve a certain power in the test (see here: [[Metrics of Hypothesis Tests]])
- To achieve a certain precision for the CI (see here: [[Hypothesis Testing#Basic statistical Idea behind Hypothesis Testing and Connection to CI]])
## What to Specify for Sample Size Calculation?
Before we begin with sample size calculation we need to make a few notes on what we actually want to test. The necessary input is: 
- Primary variable/endpoint
- Test statistic
- Null hypothesis & alternative (“working”) hypothesis at chosen dose(s)
- Significance level
- Type II error/ power
- Approach to dealing with treatment withdrawals & protocol violations
- Method by which sample size calculated should be given in protocol (precision-based or power-based) and the inputs of the chosen approach.
- Sensitivity of sample size estimate to deviations from assumptions. So how much the required sample size changes when certain **assumptions** about the data or test conditions are not perfectly met.
## **Precision-Based Approach for Confidence Intervals (CIs)**
Before we begin with the precision-based approach, we need to define our input: 
- Desired confidence level (e.g., **95%**).
- Margin of error (ME): Half the width of the CI.
- Standard deviation ($\sigma$).

Now for the actual calculation we take the know formula for the CIs: $\bar{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$. If we reformulate them, so that we can incorporate the ME, this looks like this: $ME = Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$. Now we just solve this for $n$ and we have our formula: $n = \left(\frac{Z_{\alpha/2} \cdot \sigma}{ME}\right)^2$.
## **Power Analysis for Hypothesis Testing**
Again, before we begin with the power-based approach, we need to define our input: 
- Significance level ($\alpha$) – usually 0.05 (5% chance of Type I error).
- Power ($1 - \beta$) – commonly 0.8 or 0.9 (probability of detecting a true effect).
- Effect size ($\delta$) – the minimum difference between groups you want to detect.
- Standard deviation ($\sigma$) – assumed or estimated from previous studies.
- Z-values for $\alpha$ and $\beta$ from the standard normal table.

The formula we need to use now depends on which test we want to perform:
- General Formula for Two-Sample t-Test (Equal Variances): $n = \frac{(Z_{\alpha/2} + Z_{\beta})^2 \cdot 2\sigma^2}{\delta^2}$
- One-Sample t-Test: $n = \frac{(Z_{\alpha/2} + Z_{\beta})^2 \cdot \sigma^2}{\delta^2}$
- One-Tailed Test: Replace $Z_{\alpha/2}$ with $Z_{\alpha}$
- Two-Sample t-Test (Different Variances): $n = \frac{(Z_{\alpha/2} + Z_{\beta})^2 (\sigma_1^2 + \sigma_2^2)}{\delta^2}$
- When we have more than two samples, for example multiple doses versus placebo, we usually calculate $n$ based on 2 groups and then use $n$ for all >2 groups.

