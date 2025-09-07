As described here ([[Data Munging]]), data preprocessing is an important step in the data science process. The two main techniques we use are **transformation** and **scaling**. Transformations like the log, square root, Box-Cox, and rank-based transformations are used to **reshape** data to approximate normality or reduce skewness, while **standardization** and **normalization** are scaling techniques to **adjust data for comparison**. Here is a python example of how to use the techniques described in this note, [[Transformation and Scaling in Python]].
## Transformation
Transforming data that is not normally distributed into a normal distribution is a common goal in data analysis, especially when we need to meet the assumptions of statistical tests or models that require normality. One common transformation is the **log transformation**.

The log transformation works by taking the logarithm of each dat point ($Y = \log(X)$). What this does, is that it compresses the right tail of the distribution, often bringing it closer to normal. Note that this transformation only applies to **positive** values of $X$.

The basic intuition behind transformation is that we want to **reduce skewness** in our data. Skewed data is asymmetrical. Positively skewed data has a long tail on the right (e.g., income, population) and negatively skewed data has a long tail on the left. The log transformation for example works very well for right skewed data. Here is how that could look:

![[Pasted image 20241219094412.png]]
## Scaling
Because standardization and normalization serve such a similar purpose, it usually does not make sense to use them together. Here
### Standardization
No matter what we are discussing, be it regression models, classification models, computing distances, or just handling data in general, it is important that our data is standardized. Standardization transforms data to have a mean of 0 and a standard deviation of 1. This allows comparisons across datasets or variables with different units or scales. The shape of the distribution remains **unchanged** by standardization, but the scale and center of the data are adjusted. *Z-scores* will be our primary method of standardization. 

The Z-score transform is computed: $Z_i = (a_i − μ)/σ$

Z-scores transform arbitrary sets of variables to a uniform range and accomplish two goals.
- First, they aid in visualizing patterns and correlations by ensuring that all fields have an identical mean (zero) and operate over a similar range. 
- Second, the use of Z-scores makes it easier on our machine learning algorithms by making all different features of a comparable scale.

**Z-scores best work on normally distributed data. Be careful when dealing with anything else!** As we can see in our example above, the data is almost standardized (mean is almost at 0) but we can shape it to be properly standardized with the z-score:

![[Pasted image 20241219095752.png|400]]
### Normalization
The general purpose of **normalization** is to scale the data so that it fits within a specific range, typically between 0 and 1, or sometimes between -1 and 1. This is done to ensure that all features or variables in our dataset have the same scale. 

One popular method to do this is Min-Max-Scaling. Min-Max-Scaling works like this:  $\text{Normalized Value} = \frac{x - \min(x)}{\max(x) - \min(x)}$. If we use this to normalize our previous example it would look something like this:

![[Pasted image 20241219101531.png|400]]

