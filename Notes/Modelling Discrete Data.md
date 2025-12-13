 First, it needs to be said, that the problems discussed in this note are universal and depend not on if we use a Bayesian or a frequentist model. The problems might show themselves in different ways or be handle differently, but the underlying structural challenges are the same. 
## The Geometry of the Likelihood
The mapping of parameter to probability in a Gaussian linear model is linear. Each parameter value corresponds exactly to the difference in probability of the Gaussian likelihood. This is not the case with discrete data. 

In the case of discrete data, we have a *nonlinear* link, which means that discrete likelihoods often have very steep or flat regions on the link scale. This introduces two challenges:

 First, the nonlinear link scales introduces sensitivity. In Bayesian models, it appears as overly extreme implied priors. In frequentist models, it shows up as unstable or infinite estimates when the likelihood is poorly constrained. => The cure in both cases is the same principle: **regularization** (explicit priors or penalized likelihoods). Here is an example that shows this: 

``` R
library(rethinking)
set.seed(2405)

data(chimpanzees)
d <- chimpanzees

# Build index varaiable
d$treatment <- 1 + d$prosoc_left + 2 * d$condition

# Data list for convenience
dat_list <- list(
	pulled_left = d$pulled_left,
	actor = d$actor,
	treatment = as.integer(d$treatment)
)

# Simple logistic regression as a binomial GLM
m11.1 <- quap(
	alist(
		pulled_left ~ dbinom(1, p),
		logit(p) <- a,
		a ~ dnorm(0, 10)
	), data = d
)

# Prior predictive simulation with logit scale
prior <- extract.prior(m11.1, n = 1e4)
p <- inv_logit(prior$a)
dens(p, adj = 0.1)
```

The resulting prior predictive check looks like this: ![Pasted image 20251010093558.png](../Images/Pasted%20image%2020251010093558.png)
This is the result of the extreme prior:  a ~ dnorm(0, 10)!

Second, the nonlinear link creates _two scales of meaning_ — one for parameters and one for outcomes. Every generalized linear model has:
- A **linear predictor scale** (the unbounded, additive space where parameters live), and
- An **outcome scale** (bounded or nonlinear, where we interpret probabilities, counts, etc.).
Additionally there is the scale of the parameters the log-odds scale. This is not interpretable for us humans!

Example for a binomial GLM: $\text{logit}(p) = a + b \cdot \text{treatment}$, where treatment = 0 → no medicine and
treatment = 1 → medicine.
- Now lets say parameter $b[0] = 0$ and $b[1] = -1$. This means: “Taking the medicine decreases the _log-odds_ of getting sick by 1.” That’s abstract — we can’t easily think in log-odds.
- On the odds scale, this looks like this: $exp(0) = 1$ and $exp(–1) ≈ 0.37$. This means the _odds_ of getting sick are multiplied by 0.37 when taking the medicine. This is the *relative* effect.
- On the probability scale this means we convert the odds into probabilities: $p = \frac{\text{odds}}{1 + \text{odds}}$. Untreated: odds: $1 → p = 0.5$ and treated: odds: $0.37 → p = 0.27$. This now means: The probability of getting sick drops from 0.50 to 0.27 — an _absolute decrease_ of 0.23 (23 percentage points). That’s your *absolute effect*.

Here is an example in R that shows this: 

``` R
m11.2 <- quap(
  alist(
    pulled_left ~ dbinom(1, p),
    logit(p) <- a + b[treatment],
    a ~ dnorm(0, 1.5),
    b[treatment] ~ dnorm(0, 0.5)
  ), data = dat_list
)

post <- extract.samples(m11.2)

# Log-odds of each treatment
print(precis(m11.2, depth = 2))

# These are the relative effects of treatment 4 vs treatment 2:
relative_effects <- mean(exp(post$b[, 4] - post$b[, 2]))
print(relative_effects)

# These are the absolute effects of each treatment:
p <- link(m11.2, data=list(treatment=1:4))
p_mu <- apply(p, 2, mean)
print(p_mu)
# And the absolute effect of treatment 4 vs treatment 2 is:
abs_effect <- p_mu[4] - p_mu[2]
print(abs_effect)
```

## Two Representations (aggregated and not)
The idea here is to aggregate the data, so that each row does not correspond to one trail, but to however many trails for each person were conducted. The only thing that changes in the model is this part: $dbinom(18, p)$, if we assume 18 trails per person. 

So why do this? There are times when this makes sense, like with multilevel models. But usually this is not beneficial. It can actually make WAIC and PSIS comparison more complicated. So if we want to calculate WAIC or PSIS, we should use a logistic regression data format, not an aggregated format. Otherwise we are implicitly assuming that only large chunks of the data are separable. 
## Ordered Categorical Outcomes
Ordered categorical outcomes outcomes, like rating scales, differ from counts or continuous variables because while their order matters, the spacing between categories is not necessarily equal. Treating them as continuous (e.g., by using linear regression) can mislead inference.

An ordered categorical variable is conceptually a **multinomial outcome** with an **ordering constraint**. This means as a predictor increases, the probability mass should shift progressively through the ordered levels (e.g., from 3 → 4 → 5). To enforce this monotonic behavior, we use a cumulative link (ordered logit) model. Here the likelihood is defined by cut-points and a latent mean. This is how such a model looks like in R: 

``` R
dat <- list(
	R = d$response,
	A = d$action,
	I = d$intention,
	C = d$contact 
)

m12.5 <- ulam(
	alist(
		R ~ dordlogit( phi , cutpoints ),
		phi <- bA*A + bC*C + BI*I,
		c(bA,bI,bC) ~ dnorm( 0 , 0.5 ),
		cutpoints ~ dnorm( 0 , 1.5 )
	) , data=dat , chains=4 , cores=4 
)
```

Added to the usual intercepts for the features in this model, the ordered-logit model also produces **posterior estimates for each cut-point**, representing how much of the latent scale must be crossed to move from one category to the next.

One nice thing is, ordered models naturally handle skewed or uneven distributions of category frequencies by estimating **unequal distances** between cut-points. The model does **not assume symmetry** or equal spacing — it lets the data decide how probabilities accumulate across categories. Hence, skewed categorical responses (e.g., most responses are 6 or 7) are modeled correctly by asymmetric cumulative probabilities rather than by forcing symmetry, as a Gaussian model would.
## Ordered Categorical Predictors
Not only our outcome can be ordered categorical, also our predictors. If that is the case, we need to take a few things into account. 

Let's assume we have a very similar model as above, but with education as an ordered categorical predictor: 

``` R
dat <- list(
	R = d$response ,
	action = d$action,
	intention = d$intention,
	contact = d$contact,
	E = as.integer( d$edu_new ), # edu_new as an index
	alpha = rep( 2 , 7 ) # delta prior
) 

m12.6 <- ulam(
	alist(
		R ~ dordlogit( phi , cutpoints ),
		phi <- bE*sum( delta_j[1:E] ) + bA*action + bI*intention + bC*contact,
		cutpoints ~ normal( 0 , 1.5 ),
		c(bA,bI,bC,bE) ~ normal( 0 , 1 ),
		vector[8]: delta_j <<- append_row( 0 , delta ),
		simplex[7]: delta ~ dirichlet( alpha )
	), data=dat , chains=4 , cores=4 
)
```

In the data list, we see two additions:
- E: the **ordered categorical predictor**, “education level,” converted to an integer index 1–8.
- alpha: a vector of 7 twos — the prior for a **Dirichlet(2,2,2,2,2,2,2)** distribution.

In the linear combination we add the education as a cumulative sum of the δ’s up to the person’s education level E. This sum gives how much of the total education effect applies at that level — i.e., the partial cumulative effect. Multiplying by bE gives the expected contribution of education for that person on the latent scale (phi).

In the priors, we first add a zero in the beginning to delta_j (to make it 8 long, so the first level has no effect). And we have delta. Delta is a **simplex of 7 elements**, one for each _step_ between 8 education levels (Simplex = nonnegative numbers summing to 1 (Dirichlet prior)).

We interpret the resulting estimates as:
- The δ’s tell _where_ along the education scale the effect accumulates.
- bE tells _how strong_ the total effect of education is from lowest to highest level.
