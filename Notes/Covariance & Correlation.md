## Covariance
The covariance measures how two random variables vary together. They can either be **positive covariance**, then when one variable increases the other increases as well. A **negative covariance**, if one variable increases the other decreases and vice versa. Or a **zero covariance**, then these two variables do not have a linear relationship. 

The covariance is given by the formula $\text{Cov}(X, Y) = E\left[(X - E[X])(Y - E[Y])\right]$.  This formula tells us how the variables $X$ and $Y$ behave in regard to their mean. If $X$ and $Y$ have a positive covariance, that means that on average $X$ and $Y$ are above their means at the same time. The opposite is the case for negative covariance. For a zero covariance the average of the above product is zero because there is no clear direction either positive or negative. 
## Example for Variance and Expected Value
Suppose that we roll two dice, let 𝑋 = the sum of the face values and $Y$ = the product of the  
face values:
![Pasted image 20241006202655.png](../Images/Pasted%20image%2020241006202655.png)

Then:
- $E[𝑋] = 7, E[𝑌] = 12.25$ 
- $E[𝑋𝑌] = {1 \over 36} ⋅ (2 ⋅ 1 + 3 ⋅ 2 ⋯) = 106 {1 \over 6}$ 
- $Cov[X, Y] = E[𝑋𝑌] − E[𝑋] E[𝑌] ≈ 20.4$  
	- This just tells us that there is a positive covariance, it tells us nothing about the direction or the strength of the relationship. For this we would need the correlation.
- $Var[𝑋] = E[𝑋^2] − E[𝑋]^2 ≈ 5.833$  
- $Var[𝑌 ]= E[𝑌^2] − E[𝑌]^2 ≈ 79.9652$
## Correlation
As seen in the example above, the covariance is not useful in determining the strength or direction of the relationship of two random variables. This is why we need the correlation. The correlation standardizes the covariance and makes the relationship easier to interpret. Correlation removes the effect of units and gives a value between -1 and +1. 
### The Pearson Correlation Coefficient
The correlation is given by the Pearson Correlation Coefficient which is: $r = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$
By dividing the covariance by the product of the standard deviations, we standardize the relationship between X and Y. This ensures that the correlation is always a value between -1 and +1.
### The Spearman Rank Correlation Coefficient
The Pearson Correlation Coefficient assumes that the data is **normally distributed** and there is a **linear relationship** between the variables. It is also very sensitive to outliers because it uses the standard deviation in its formula. 

The Spearman Rank Correlation Coefficient on the other hand measures the **monotonic** relationship between two variables, meaning that as one variable increases or decreases, the other does as well, but not necessarily at a constant rate.

Spearman is therefore more appropriate for **non-linear** relationships where the variables move in the same general direction, but not necessarily in a straight line.
### Interpretation of Correlation
Correlation does not imply causation. There can be a multitude of causations that cause correlation which are explained in the following:
- If 𝐴 causes 𝐵, then there is a **direct causation**
- If 𝐵 causes 𝐴, then there is a **reverse causation**
- If 𝐵 causes 𝐴 and 𝐴 causes 𝐵, then there is a **bidirectional causation**
- Suppose 𝐴 causes 𝐶 and 𝐶 causes 𝐵. Then we expect to see a correlation between 𝐴 and 𝐵 even though they are not directly causally related, but **mediated** by the **mediator** 𝐶
- Suppose 𝐴 causes 𝐵 either weakly and or strongly depending on 𝐶. Then we say that $C$ is a **moderator**
- Suppose 𝐶 causes 𝐴 and 𝐶 causes 𝐵. Then we expect to see a correlation between 𝐴 and 𝐵 even though they are not causally related, but there is a **confounding** variable 𝐶
- Suppose 𝐴 and 𝐵 are correlated, and 𝐴 and $C$ are correlated. Furthermore $C$ and $D$ are correlated but $B$ and $D$ are anticorrelated. Then $A$ and $D$ are correlated via the mediators $B$ and $C$ but we don't see an effect because $C$ and $B$ are **suppressors**.
- Sometimes there is absolutely no relationship between the variables and they correlate by chance. This is called a **spurious correlation**.