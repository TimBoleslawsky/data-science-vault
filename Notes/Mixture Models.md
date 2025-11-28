Very often, the things we can measure are not emissions from any pure process. Instead,
they are mixtures of multiple processes. Whenever there are different causes for the same
observation, then a *mixture model* may be useful. A mixture model uses more than one
simple probability distribution to model a mixture of causes. In effect, these models use more
than one likelihood for the same outcome variable.
## Over-Dispersion
When counts arise from a mixture of different processes, then there may be more variation — thicker tails — than a pure count model expects. In simpler terms, if the counts of, for example, a binomial distribution do not all have the same probability, the variance of some counts can exceed the expected amount. This implies that some omitted variable is producing additional dispersion in the observed counts. When counts are more variable than a pure process implies, they exhibit *over-dispersion* (the name is because the variance of a variable is sometimes called its dispersion).

Let's look at an example: In this data we look at the applications of male and female applicants and their acceptance rate to different departments: 

``` R
library(rethinking)
data(UCBadmit)
d <- UCBadmit
dat_list <- list(
  admit = d$admit,
  applications = d$applications,
  gid = ifelse(d$applicant.gender == "male", 1, 2)
)
dat_list$dept_id <- rep(1:6, each = 2)
```

If we fit a simple generalized linear model without account for the departments we get the following model: 

``` R
m11.7 <- ulam(
  alist(
    admit ~ dbinom(applications, p),
    logit(p) <- a[gid],
    a[gid] ~ dnorm(0, 1.5)
  ), data = dat_list, chains = 4, cores = 4
)

cat("\nModel 11.7:\n")
print(precis(m11.7, depth = 2))
```

The output shows that the log-odds of male applicants (-0.22) is significantly higher then the log-odds of female applicants (-0.82). This might suggest that male applicants have an easier time, but that is not the case. 

Let's now fit a model that accounts for the departments: 

``` R
m11.8 <- ulam(
  alist(
    admit ~ dbinom(applications, p),
    logit(p) <- a[gid] + delta[dept_id],
    a[gid] ~ dnorm(0, 1.5),
    delta[dept_id] ~ dnorm(0, 1.5)
  ), data = dat_list, chains = 4, cores = 4
)

cat("\nModel 11.8:\n")
print(precis(m11.8, depth = 2))
```

The output now shows almost no difference between the log-odds of male applicants (-0.57) and the log-odds of female applicants (-0.47). That is because male applicants tend to apply to easier departments. This in turn means that the counts for admit for each department have a different probability, leading to over-dispersed counts for some departments. 

We can try to model this by assuming that the admit counts for each gender don't come from a binomial distribution but from a mixture distribution, the beta-binomial distribution. This just means that instead of each count having the same probability (like in the binomial model), the counts have a probability which is distributed according to a beta distribution. 

The mixture model looks like this: 

``` R
m12.1 <- ulam(
  alist(
    admit ~ dbetabinom(applications, pbar, theta),
    logit(pbar) <- a[gid],
    a[gid] ~ dnorm(0, 1.5),
    theta <- phi + 2.0,
    phi ~ dexp(1)
  ), data = dat_list, chains = 4, cores = 4
)

cat("\nModel 12.1:\n")
print(precis(m12.1, depth = 2))
```

If we look at the resulting intercepts, we see that they are again roughly the same (-0.43 for male applicants and -034 for female applicants), even though we did not account for department! 

Here is why: The beta-binomial model allows each row in the data — each combination of department and gender — to have its own unobserved intercept. These unobserved intercepts are sampled from a beta distribution. What the model has done is accommodate the variation among. As a result, it is no longer tricked by department variation into a false inference about gender.
### Information Theory and Model Comparison with Over-Dispersed Models
Beta-binomial and gamma-Poisson (negative-binomial) models extend binomial and Poisson models by adding unobserved parameters for each data row, which makes model comparison using WAIC or PSIS problematic. Unlike standard binomial or Poisson models, these cannot be freely aggregated or disaggregated without altering their assumptions, since the latent variation depends on data structure. 

This issue is largely resolved when using [[The Hierarchy of Linear Models#Multilevel (Hierarchical) Models]], which can handle over-dispersion and heterogeneity across different levels of aggregation.
## Zero-Inflation
Usually within a model (especially a binomial model) a count of zero can arise more than one way. A “zero” means that nothing happened, and nothing can happen either because the rate of events is low or rather because the process that generates events failed to get started. If we are counting scrub jays in the woods, we might record a zero because there were no scrub jays in the woods or rather because we scared them all off before we starting looking. Either way, the data contains a zero.

Let's look at an example of how mixture models can solve this problem: Here is the data we want to use:

``` R
# define parameters
prob_drink <- 0.2 # 20% of days
rate_work <- 1 # average 1 manuscript per day
# sample one year of production
N <- 365
# simulate days monks drink
set.seed(365)
drink <- rbinom( N , 1 , prob_drink )
# simulate manuscripts completed
y <- (1-drink)*rpois( N , rate_work )
```

Here we are interested in the finished manuscripts in a monastery per day. The monastery can produce zero manuscripts 1.) if the monks drink or 2.) if the monks just don't finish one that day even if they worked.

To models this, we can use the zero-inflated Poisson distribution (or ZIPoisson). Here we just assume that the decision if the monks drink is a coin-flip with probability $p$. If the monks don't drink, they finish a Poisson distributed count of manuscripts. Here is how that looks like in R: 

``` R
m12.3 <- ulam(
	alist(
		y ~ dzipois( p , lambda ),
		logit(p) <- ap,
		log(lambda) <- al,
		ap ~ dnorm( -1.5 , 1 ),
		al ~ dnorm( 1 , 0.5 )
	) , data=list(y=y) , chains=4 
)

# Output
post <- extract.samples( m12.3 )
mean( inv_logit( post$ap ) ) # probability drink
mean( exp( post$al ) ) # rate finish manuscripts, when not drinking
```

In the output we can clearly distinguish between times where the monks don't produce manuscripts because they drink and the times where the monks don't produce manuscripts because of the work rate. 