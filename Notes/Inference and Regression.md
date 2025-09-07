The focus of inference in regression can be a bit different from other approaches like hypothesis testing. Instead of simply predicting $Y$, we use regression to test:
- How does $X$ affect $Y$? (Causal or associative relationships) => Test hypotheses about relationships (e.g., does a treatment improve health?).
- Is this effect statistically significant? => Estimate effect sizes (e.g., how much does smoking increase the risk of lung disease?).
- What is the uncertainty in our estimates? => Control for confounders (e.g., adjusting for age when studying the effect of a drug).
## Example Use-Case for Regression and Inference
Let's look at a simple example of how regression can be used to infer conclusions from some evidence.

We have the following research question: Does exercise reduce blood pressure?. From this we get the null hypothesis ($H_0$): Exercise has no effect on blood pressure ($\beta_1 = 0$) and the alternative hypothesis ($H_A$): Exercise lowers blood pressure ($\beta_1 < 0$). 

The regression model we formulate has the following variables: $Y$ = Blood pressure (mmHg); $X_1$  = Weekly exercise (hours); $X_2$  = Age (years) (used as a control variable); $X_3$  = BMI (used as a control variable): $\text{Blood Pressure} = \beta_0 + \beta_1 \cdot \text{Exercise} + \beta_2 \cdot \text{Age} + \beta_3 \cdot \text{BMI} + \varepsilon$

After running the regression, we get the following values for $\beta_1, \beta_2, \beta_3$ respectively: $-1.8, 0.3, 0.7$. With this we can answer the question about effect size. The coefficient  $\beta_1 = -1.8$  means that **each additional hour of exercise per week reduces blood pressure by 1.8 mmHg**. 

If we want to use these coefficients to test our hypothesis, we need a test statistic. The formula for the test statistic in this case would be: $t_j = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}$ (depending on type of hypothesis tested and regression model used, this formula can change!). If we take this formula to calculate the test statistic for exercise ($\beta_1$) , we would get this: $t_1 = \frac{-1.8}{0.6} = -3.0$. The p-value for exercise ($\beta_1$) would then be 0.005. This means that we reject $H_0$ and conclude that => More exercise is associated with lower blood pressure, **even after controlling for age and BMI.**
