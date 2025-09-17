Let's say we have the following task. We have a dataset on growth of 11 girls and 16 boys. The dataset includes the age, sex, and growth measurements of the boys and girls. We now want to fit the following model: $Y_{ij} = \beta_0 + \beta_{01} x_i + \beta_{10} (1 - x_i) t_{ij} + \beta_{11} x_i t_{ij} + b_{0i} + b_{1i} t_{ij} + \varepsilon_{ij}$.
- $Y_{ij}$ = measurement of individual $i$ at time $j$.
- $x_i$ = sex of individual $i$ (coded as 0 = boy, 1 = girl).
- $t_{ij}$ = time (AGE) for individual $i$ at time $j$.
- $b_{0i}$ = individual-specific random intercept.
- $b_{1i} t_{ij}$ = individual-specific random slope.
- $\varepsilon_{ij}$ = residual error.
## Fitting the Model
**R**
In R we fit such a model using this function: `lmer(response ~ fixed_effects + (random_effects | grouping_factor), data = dataset)`.  

Our model looks something like this: `model <- lmer(MEASURE ~ sex + (1 - sex) * AGE + sex * AGE + (AGE | INDIV), data = growth2)`

Let's break it down:
- fixed effects: `sex + (1 - sex) * AGE + sex * AGE`. 
	- Our model tells us that we want different intercepts (starting heights) for boys and girls by specifying this: $\beta_0 + \beta_{01} x_i$
	- The R function incorporates this by specifying: `sex +`
	- Our model also tells us that the slopes (so the growth rate) should be different for boys and girls: $\beta_{10} (1 - x_i) t_{ij} + \beta_{11} x_i t_{ij}$
	- The R function incorporates this by specifying: `(1 - sex) * AGE + sex * AGE`
- random effects: `(AGE|INDIV)`.
	- If you only use `(1 | ID)`: Everyone has a different **starting height** but shares the same **growth rate**.
	- If you use `(AGE | ID)`:  Everyone has a different **starting height** and a different **growth rate**.
	- If you use `(0 + AGE | ID)`: Everyone has the same **starting height**, but each individual has a **different growth rate**.
	- If we omit this term, no random effects will be taken into account (same as lm()).

**SAS**
In Sas a linear mixed model looks like this:
`PROC MIXED DATA = gv;` 
	`CLASS group child;`
	`MODEL height = age group age*group / SOLUTION`
	`RANDOM intercept age / TYPE=UN SUBJECT=child;`
	`REPEATED / TYPE=UN (1) SUBJECT=child R RCORR;`
`RUN;`
Here the individual components are:
- `CLASS`: Tells us which variables are categorical. 
	- In R that would be: `gv$group <- as.factor(gv$group)`.
- `MODEL`: Models the fixed effects. So in the example above we have age, group, and the interaction between age and group as fixed effects. 
- `RANDOM`: Models the random effects. `intercept`needs to be specified for a random intercept for each subject. After that the other fixed effects can be listed. The `TYPE=UN`means a unstructured covariance is model (usual). We could also have nested random effects `Leaf(Plant)`.
	- In R that would b: `(age | child)`.
- `REPEATED`: Specifies the structure of within-subject residuals. We can add something like this, `REPEATED visits/ ...`this tells the model, how repeated measures are specified (usually time, visits, ...). If we omit this, we just model correlation among all repeated measurements within each subject, without focusing on any specific variable. 
	- In R this is not possible!
=> If we only have `RANDOM`we have a hierarchical model, if we only have `REPEATED`we have a marginal model, if we have both it is a mix!

Here is what a possible output could look like:
- Fit statistics: AIC/BIC (lower is better), LogLikelihood (higher is better)
- Tests for fixed effects: Have predictors an significant effect on model?
- Estimates for fixed effects: For example, age = -0.75 means that for each unit increase in age, the outcome variable decreases by 0.75 (if the effect is linear).
- Covariance parameter estimates: Tells us about the variability in the random effects, small p-value indicates that the random effect contributes significantly to the model.
- Residuals
- Optional: LSMeans: Represents the estimated means of the dependent variable for each level of a factor, adjusted for the other variables in the model, e.g.:
	Effect    Level        Estimate   Standard Error   DF   t Value   Pr > |t|
	age       0            10.25      0.50             100  20.50     <.0001
	age       1            9.75       0.50             100  19.50     <.0001
	group     1            12.00      0.60             100  20.00     <.0001
	group     2            11.50      0.60             100  19.00     <.0001

