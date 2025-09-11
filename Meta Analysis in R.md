Here is a simple example of how to do complete pooling, no pooling, and partial pooling within a meta analysis in R.

``` R
library(lme4)

# Data preparation
load("radonData.RData")

dt$county.name <- factor(dt$county.name)
dt$state.name <- factor(dt$state.name)
dt$county.local <- factor(dt$county.local)

# Complete-pooling
M0 <- lm(radon ~ floor, data=dt)
print("Complete-pooling")
print(summary(M0))

# No-pooling
M1 <- lm(radon ~ floor + county.local - 1, data=dt)
print("No-pooling")
print(summary(M1))

# Partial-pooling
M2<-lmer(radon ~ floor + (1 | county.local), data=dt)
print("Partial-pooling")
print(summary(M2))
```

**Complete Pooling (M0)**
This is a simple linear regression, treating all observations as coming from the same population, assuming no meaningful difference between counties. The only predictor is floor, meaning we estimate one overall effect of floor on radon. Every county has the same estimated intercept and slope.

**No Pooling (M1)**
This model includes county-specific intercept by adding `county.local` as a categorical variable. The -1 removes the overall intercept, so we get one separate intercept per county. Each county gets its own estimate, but they are independent (i.e., estimates for one county do not inform another).

**Partial Pooling (M2)**
This is a mixed-effects model, where floor is a fixed effect and (1 | county.local) is a random effect. The county intercepts are not independent; instead, they are assumed to come from a shared distribution. Each county gets its own estimate, but counties with little data “borrow strength” from the overall population. 
=> This model balances **flexibility (like no pooling)** and **stability (like complete pooling)**.