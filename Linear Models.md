A **Linear Model (LM)** is the simplest type of regression model where the response variable $Y$ is assumed to be a **linear** function of the predictor variables $X$, plus some normally distributed error term.

Equation: $Y = X\beta + \varepsilon, \quad \varepsilon \sim N(0, \sigma^2)$
where:
- $Y$ is the response variable (continuous)
- $X$ is the matrix of predictor variables
- $\beta$ is the vector of coefficients
- $\varepsilon$ is the normally distributed residual error

Example: Predicting **house prices** based on square footage.
$\text{Price} = \beta_0 + \beta_1 \cdot \text{SquareFootage} + \varepsilon$
## Linear Mixed Models
A **Linear Mixed Model (LMM)** extends the **linear model** by adding **random effects**, which account for dependencies in hierarchical or grouped data (e.g., repeated measurements on the same subject). They are called mixed models, because the incorporate both the fixed-effects part, like the LM's, and also the random effects. Here is an example of how to work with LMMs in R and SAS: [[Linear Mixed Models in R and SAS]]

Equation: $Y = X\beta + Zb + \varepsilon$
where:
- $X\beta$ is the fixed-effects part (like in a standard linear model)
- $Zb$ is the **random effects** term, where: $b \sim N(0, D)$  (random effects have their own variance)
- $\varepsilon \sim N(0, \Sigma_i)$ is the residual error

Example: Modeling **student test scores**, where each student belongs to a different school.
$\text{Score} = \beta_0 + \beta_1 \cdot \text{StudyTime} + b_{\text{School}} + \varepsilon$, where $b_{\text{School}}$ is a random effect that captures school-specific variation.

**Formulation of LMM's**:
1. We start by modeling the response vector $Y_i$ for each subject $i$, using a standard linear model: $Y_i = Z_i \beta_i + \epsilon_i$.
	-  $Z_i$ is a design matrix for subject $i$, which relates the predictors (e.g., fixed effects, covariates) to the response. 
	- $\beta_i$ is the vector of unknown regression parameters (fixed effects or subject-specific effects) for subject $i$.
	- $\epsilon_i$ represents the **residual error**, assumed to be normally distributed.
	  => This first stage treats each subject as having their own regression model, meaning we estimate a separate set of regression coefficients $\beta_i$ for each individual. However, this approach does not yet incorporate any structure that accounts for similarities across subjects.
2. The second stage models the between-subject variability. For this we use the following equation: $\beta_i = K_i \beta + b_i$. This means we assume that $\beta_i$ is composed of a fixed effect $\beta_0$ (common across all subjects) and a random effect $b_i$ (subject-specific deviation from $\beta_0$).
	- $K_i$ is a design matrix for subject $i$, which relates the subject-specific parameters $\beta_i$ to the overall population-level parameters $\beta$.
	- The random effect $b_i$ captures the individual subject’s deviation from the average model.
3. The third stage is to combine these models to a single model. For this we have two interesting equations: $Y_i = Z_i \beta_i + \epsilon_i = Z_i (K_i \beta + b_i) + \epsilon_i$, this equation is just the stages one and two put together. $Y_i = X_i \beta + Z_i b_i + \epsilon_i$, this equation is the same just multiplied out. 
	-  $X_i$ is the design matrix for subject $i$ based on the fixed effects. This matrix is just $Z_i \times K_i$.
- But this described model does not account for group-specific variation! To incorporate this, instead of just defining the subject-specific regression coefficients $\beta_i$ as: $\beta_i = \beta_0 + b_i$, we introduce **group-level predictors** (e.g., Low, High, and Control groups, denoted by $L_i, H_i, C_i$) and modify the equation to: $\beta_{i} = \beta_1 L_i + \beta_2 H_i + \beta_3 C_i + b_{i}$.

**Assumptions of LMM's**:
- The relationship between the predictor variables (fixed effects) and the response variable is assumed to be linear.
- Errors are assumed to follow a structured covariance pattern rather than being independent.
- Random effects and errors have normal distribution.
### Why Are LMM's Important?
Suppose we are studying **weight changes over time** for 100 patients, measuring weight every 3 months.
4. **Using Linear Model (LM)**
	$\text{Weight} = \beta_0 + \beta_1 (\text{Time}) + \varepsilon$
	- Assumes all patients start at the **same weight** ($\beta_0$).
	- Assumes all patients have the **same rate of weight change** ($\beta_1$). 
	- Assumes errors ($\varepsilon$) are **independent**. 

5. **Using Linear Mixed Model (LMM)**
	$\text{Weight}{it} = \beta_0 + \beta_1 (\text{Time}) + b_i + \varepsilon{it}$
	- Each patient has their **own baseline weight** ($b_i$). 
	- Can extend to allow **individual weight change rates** (random slopes). 
		=> $\text{Weight}{it} = \beta_0 + \beta_1 (\text{Time}) + b{0i} + b_{1i} (\text{Time}) + \varepsilon_{it}$
		$\beta_1$  is still the **average weight change rate across all individuals**. 
		$b_{1i}$  captures **individual deviations** from that average.
	- Accounts for correlation between repeated measures of the same patient. By introducing the same $b{0i}$ to each measurement of a patient $i$ and thereby introducing correlation. 
=> LMMs are particularly useful for modeling **hierarchical** (nested) and **grouped** data, such as **longitudinal** (repeated measures) data.
#### Simpsons Paradox
Simpson’s Paradox occurs when a trend that appears in different groups of data reverses or disappears when the groups are combined. This happens due to confounding variables that affect the relationship between the variables of interest. LMMs handle Simpson’s Paradox by explicitly modeling group-level variability (random effects), instead of treating all data points as independent. 
### The Frequentist and Bayesian Question
LMMs sit at an interesting intersection between frequentist and Bayesian approaches because of the way they treat fixed and random effects.

**Fixed Effects (Frequentist Perspective)**:
- Fixed effects in an LMM are estimated using maximum likelihood (ML) or restricted maximum likelihood (REML), just like in ordinary least squares (OLS) regression.
- These estimates are treated as deterministic parameters, meaning that in the frequentist framework, they are not assumed to have a probability distribution—they are just estimated from the data.

**Random Effects (Bayesian-Like Perspective)**:
- Random effects are assumed to follow a probability distribution, typically a normal distribution with mean zero and some variance.
- Instead of estimating each group-specific effect directly, we estimate the parameters of the distribution (mean and variance), which is a Bayesian-like approach.
- The assumption that the effects come from a distribution rather than being fixed parameters aligns with Bayesian thinking, where parameters themselves are random variables.
### Hierarchical vs. Marginal Formulation
The models we discussed above are hierarchical models ($Y_i = X_i \beta + Z_i b_i + \epsilon_i$,). The hierarchical formulation expresses the model **in two levels** (stages 1 and 2 above). It is called **hierarchical** because we model both **group-level** and **individual-level** variation.

For the marginal formulation we integrate out the random effects $b_i$ to get a marginal distribution for $Y_i$ => $Y_i \sim N(X_i \beta, Z_i D Z_i^T + \Sigma_i)$.
This means that the marginal formulation focuses on population level effects instead of the subject-specific effects (like the hierarchical formulation). So the marginal formulation basically aims to answer the same question as a normal linear model (population-averaged effects), while adjusting for the correlation between repeated measurements within subjects or clusters. It does not explicitly model subject-specific random effects. This makes the marginal formulation better for repeated measures, use linear models when independence holds!
#### Estimation of the Marginal Formulation
We use parameter estimation methods from normal regression (for more look here: [[Parameter Estimation for Probabilistic Models]]). But, because in the marginal formulation (or LMM's in general) we have correlated errors and random effects, this estimation is a bit harder.

We technically could use MLE to estimate the marginal formulation, but ML **underestimates variance components** because it does not account for the loss of degrees of freedom when estimating $\beta$, leading to bias. => Therefore we prefer REML.

REML or restricted maximum likelihood estimation corrects the bias in variance estimates that occurs with MLE. Instead of maximizing the full likelihood, it **first removes the fixed effects**  $\beta$ and then estimates the variance components.
### Inference for LMM's
So let's say we have some experiment on growth. I now formulate a LMM to model the data (either hierarchical or marginal). I use REML to estimate the parameters. I can now perform inference on three key components:
- **Fixed Effects** ($\beta$) → Population-level effects (e.g., treatment effect on growth), test with hypothesis tests.
- **Variance Components** ($D, \Sigma$) → Random-effect variability (e.g., how much individuals differ), test with hypothesis tests.
- **Random Effects** ($b_i$) → Subject-specific deviations (e.g., how much a particular plant differs), no direct hypothesis tests

**Inference for Fixed Effects**:
The **Wald test** is the most commonly used method for testing fixed effects in linear mixed models (LMMs). The formula for the test statistic in the Wald test is: $W = \frac{\hat{\beta}}{\text{SE}(\hat{\beta})}$. This might look familiar. Then why does this work for LMMs and the other does not? The key is that the standard error accounts for random effects variance. 

Problem: In LMMs, we estimate both fixed effects ($\beta$) and random effects ($\alpha$). The Wald test assumes that the variance components are known and fixed when testing fixed effects. However, in reality, we estimate them from the data, introducing additional uncertainty. Because the uncertainty in estimating $\alpha$ (random effects) is not fully accounted for, the standard errors of fixed effects are underestimated.
=> Now ironically the solution can be t-tests (or F-tests for multiple parameters) that look like this: $t = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}$. Instead of using a normal distribution (Wald test), we use a t-distribution with adjusted degrees of freedom (for example through Satterthwaite’s approximation).

Another alternative are likelihood ratio tests (LRTs). The idea behind the LRT is to check if the model works as well, when the inputs are restricted as if the inputs are "full". The formula for the LRT is: $\Lambda(x) = \frac{\sup\{L(\theta | x) : \theta \in \Theta_0\}}{\sup\{L(\theta | x) : \theta \in \Theta\}}$. 
- $L(\theta | x)$ is the **likelihood function** of the observed data $x$, given the parameter $\theta$.
- $\sup\{L(\theta | x) : \theta \in \Theta_0\}$ is the **maximum likelihood** under the **null hypothesis** $H_0$, where $\theta$ is restricted to a smaller parameter space $\Theta_0$ (e.g., $\beta = 0$).
- $\sup\{L(\theta | x) : \theta \in \Theta\}$ is the **maximum likelihood** under the **full model** (unrestricted $\theta$).
The test statistic is then: $\Lambda^* = -2 \log \Lambda(x) = -2 \log \left( \frac{\sup L(\theta | x) \text{ under } H_0}{\sup L(\theta | x) \text{ under full model}} \right)$. This follows a $\chi^2$-distribution with degrees of freedom equal to the number of fixed effects being tested. 
=> Be careful, this only works on nested models and if the models are not fitted using REML! If the model is not nested we can use AIC/BIC for example. 

**Inference for Variance Components**
We also use the Wald test and LRTs. LRTs in this case can even be used when fitted using REML!

**Inference for Random Effects**
We use Baysien inference for the inference of random effects. More on Baysien inference here: [[Bayesian Inference]].