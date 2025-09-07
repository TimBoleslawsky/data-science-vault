## Range
The range is easily calculated and defines the difference between the maximum and minimum values in the dataset. Formula: $\text{Range} = \text{Max} - \text{Min}$
## Variance
**Population Variance**
Is just the equivalent of the variance in probability: $\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$. Be careful that this formula is dependent on the underlying distribution. More about the different formulas for variance depending on the distribution here: [[Expected Value & Variance]].

**Sample Variance**
We don’t usually have access to the whole population, so we need to estimate the variance from a sample. We do this by applying the formula for the population variance on the sample but applying **Bessel’s correction** so we get the unbiased sample variance: $s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2$
## Standard Deviation
The standard deviation is the square root of the variance, bringing the measure back to the same unit as the original data. This is generally more intuitive and less prone to outliers. 
Formula: $\sigma = \sqrt{\sigma^2}, \quad s = \sqrt{s^2}$

