A **Linear Model (LM)** is the simplest type of regression model where the response variable $Y$ is assumed to be a **linear** function of the predictor variables $X$, plus some normally distributed error term.

Equation: $Y = X\beta + \varepsilon, \quad \varepsilon \sim N(0, \sigma^2)$
where:
- $Y$ is the response variable (continuous)
- $X$ is the matrix of predictor variables
- $\beta$ is the vector of coefficients
- $\varepsilon$ is the normally distributed residual error

Example: Predicting **house prices** based on square footage.
$\text{Price} = \beta_0 + \beta_1 \cdot \text{SquareFootage} + \varepsilon$

There are a few different denominations one encounters when talking about linear models. Below I describe the "hierarchy" present in linear model theory.
## Generalized Linear Models (GLMs)
GLMs generalize linear regression by allowing different outcome distributions (e.g. Gaussian, Binomial, Poisson) and link functions between predictors and expected outcome. They are mainly descriptive models of associations.

_Example (Binomial GLM in R):_ Logistic regression predicting outcome $y$ (0/1) from predictor $x$.

```
m_glm <- ulam(
  alist(
    y ~ dbinom(1, p),
    logit(p) <- a + b*x,
    a ~ dnorm(0, 1),
    b ~ dnorm(0, 1)
  ),
  data = d, chains = 4
)
```

There are two important distinctions here when comparing it against the "simple" Gaussian LM:
- First, the likelihood is binomial instead of Gaussian. We use the binomial distribution in this case, because, for a count outcome $y$ for which each observation arises from $n$ trials and with constant expected value $np$, the binomial distribution has maximum entropy. 
- Second, we need a *link function* (logit in this case). We do not need a link function with gaussian linear models, because the parameter of interest ($\mu$) is unbounded in both directions. That is not the case for (among others) the parameter $p$ of the binomial distribution. The probability mass $p$ must lie between zero and one, the link functions provides a solution for this. Almost always we have one of two link functions: 
	- Logit Link: If we want the parameter to be between 0 and 1. Can be reversed through the logistic (in this context also called inverse-logit) function. 
	- Log Link: If we want to prevent the parameter from taking on a negative value. Can be reversed through the exponential. 

To decide which distributions gives the most appropriate model for our specific likelihood, we can use *maximum entropy*. The intuition behind maximum entropy is simple: The distribution that can happen the most ways is also the distribution with the biggest information entropy (see [[Using Information Theory to Select Models|here]] for more on that). Call this distribution the maximum entropy distribution. 

We want to use this maximum entropy distribution because: The distribution with the biggest entropy is the most conservative distribution that obeys its constraints!
### Gaussian Linear Model (special case of GLM)
A GLM where the outcome is Gaussian and the link is the identity, i.e. ordinary regression. It assumes constant variance and normally distributed errors.

_Example (Gaussian LM in R):_ Ordinary regression of $y$ on $x$, assuming Gaussian likelihood.

```
m_gauss <- ulam(
  alist(
    y ~ dnorm(mu, sigma),
    mu <- a + b*x,
    a ~ dnorm(0, 10),
    b ~ dnorm(0, 1),
    sigma ~ dexp(1)
  ),
  data = d, chains = 4
)
```

## Multilevel (Hierarchical) Models
These extend GLMs by introducing varying (random) effects, so parameters can differ across groups but still share information through partial pooling. They are more generative and reduce overfitting.

_Example (multilevel Gaussian in R):_ Varying intercepts across groups (say gid).

```
m_hier <- ulam(
  alist(
    y ~ dnorm(mu, sigma),
    mu <- a[gid] + b*x,
    a[gid] ~ dnorm(a_bar, sigma_a),
    a_bar ~ dnorm(0, 1),
    b ~ dnorm(0, 1),
    sigma_a ~ dexp(1),
    sigma ~ dexp(1)
  ),
  data = d, chains = 4
)
```

More on multilevel/hierarchical models here: [[Multilevel & Hierarchical Models]].