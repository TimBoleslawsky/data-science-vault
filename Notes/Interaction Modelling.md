Interactions are key to understand how predictors interact with each other. Simple linear models assume independent effects of predictors. _Interactions_ allow slopes or effects to depend on other predictors.

Interactions are **symmetric**: “Effect of ruggedness depends on continent” = “Effect of continent depends on ruggedness.” In practice, humans often choose the interpretation that makes causal sense (e.g., terrain can be altered more easily than a country’s continent). BUT, statistical models don’t encode causality, making interactions very hard to interpret.

One issue, which is seldom discussed, is that for you to use interactions you’d need a much larger sample size (roughly x16) to discover an effect the same size as when you look at population-level effects (i.e., $β$ parameters).
## **Survivor Bias**
The concept of *survivor bias* nicely shows the importance of interactions in statistical models. A prominent example for survivor bias is that of ww2 bombers. Here, bullet holes were mapped on returning planes, but the missing data (planes that didn’t return) meant hits in engines and cockpits were underestimated.

=> Every dataset is conditional. What we observe is shaped by hidden conditions, and interaction models help make these dependencies explicit!
## **Incorporating Interactions in Models**
Interactions are incorporated by multiplying predictors directly in the linear model:

- **Mathematical form:**
	$\mu_i = \alpha + \beta_x x_i + \beta_z z_i + \beta_{xz}(x_i \cdot z_i)$
- **In R (frequentist):**

```
lm(y ~ x * z, data = dat)
```

Note: this also _main effects_ automatically. Without the main effects $\beta_x x_i$ and $\beta_z z_i$, the model would assume that the outcome is just $\alpha$ if $x=0$ or $z=0$. That doe snot make sense.

- **In rethinking (Bayesian):**

```
m <- ulam(
  alist(
    y ~ dnorm(mu, sigma),
    mu <- a + bx * x + bz * z + bxz * x * z,
    a ~ dnorm(0, 1.5),
    bx ~ dnorm(0, 0.5),
    bz ~ dnorm(0, 0.5),
    bxz ~ dnorm(0, 0.5),
    sigma ~ dexp(1)
  ), data=dat
)
```

## Interpreting Interactions with Plots
As I said above, interpreting interactions is hard. But we can use some plotting to make it easier. First we have to differentiate between categorial x continuous and continuous x continuous interactions here. The mathematics is the same (a product term), but the **interpretation** differs:
- **Categorical × continuous**
	- Think of it as _different slopes for different groups_.
	- Example: slope of ruggedness differs between Africa and non-Africa.
	- Plotting: separate regression lines per group.

- **Continuous × continuous**
	- Here, _the slope of one variable depends on the level of another variable continuously_.
	- Example: effect of water on tulip blooms depends on shade.
	- Interpretation: no single slope for water — it varies smoothly with shade.
	- Plotting: requires 3D surfaces, contour plots, or “triptych” plots (low, medium, high levels of the moderator).

Here are two examples: 
- Categorical x continuous: $\mu_i = \alpha + \beta_r \cdot \text{rugged}_i + \beta_c \cdot \text{Africa}_i + \beta{rc} \cdot (\text{rugged}_i \cdot \text{Africa}_i)$.

``` R
m_cx <- ulam(
  alist(
    log_gdp ~ dnorm(mu, sigma),
    mu <- a + br * rugged + bc * cid + brc * rugged * cid,
    a ~ dnorm(0, 1.5),
    br ~ dnorm(0, 0.5),
    bc ~ dnorm(0, 0.5),
    brc ~ dnorm(0, 0.5),
    sigma ~ dexp(1)
  ), data=dat_list, chains=4, cores=4, iter=1000
)

# Posterior predictions
rug_seq <- seq(from=min(dat$rugged), to=max(dat$rugged), length.out=100)
pred_dat <- data.frame(
  rugged = rep(rug_seq, 2),
  cid = rep(0:1, each=100)
)
mu <- link(m_cx, data=pred_dat)

mu_mean <- apply(mu, 2, mean)
mu_PI <- apply(mu, 2, PI, prob=0.89)

# Plot
print(plot(dat$rugged, dat$log_gdp, col=ifelse(dat$cont_africa==1, "red", "blue")))
print(lines(rug_seq, mu_mean[1:100], col="blue"))   # non-Africa
print(lines(rug_seq, mu_mean[101:200], col="red"))  # Africa
```

The resulting image shows that inside Africa, ruggedness is positively associated with GDP, while outside Africa the opposite is the case:![[Pasted image 20250922113028.png]]

- Continuous x continuous: $\mu_i = \alpha + \beta_w \cdot \text{water}_i + \beta_s \cdot \text{shade}_i + \beta{ws} \cdot (\text{water}_i \cdot \text{shade}_i)$

```R
m8.4 <- ulam(
  alist(
    blooms_std ~ dnorm(mu, sigma),
    mu <- a + bw*water_cent + bs*shade_cent + bws*water_cent*shade_cent,
    a ~ dnorm(0.5, 1),
    bw ~ dnorm(0, 0.5),
    bs ~ dnorm(0, 0.5),
    bws ~ dnorm(0, 0.5),
    sigma ~ dexp(1)
  ), data=d, chains=4, cores=4
)

par(mfrow=c(1,3)) # 3 plots in 1 row

for ( s in -1:1 ) {
  idx <- which( d$shade_cent==s )
  
  plot( d$water_cent[idx] , d$blooms_std[idx] ,
        xlim=c(-1,1) , ylim=c(0,1) ,
        xlab="water" , ylab="blooms" ,
        pch=16 , col=rangi2 )
  
  # posterior predictions at water = -1:1, for this shade
  mu <- link( m8.4 , data=data.frame( shade_cent=s , water_cent=-1:1 ) )
  
  # draw 20 regression lines from posterior
  for ( i in 1:20 ) 
    lines( -1:1 , mu[i,] , col=col.alpha("black",0.3) )
  
  title(main=paste("shade =",s))
}
```

In the resulting plot we can see what happens, when we fix shade to -1/0/1. In this case we see, that in low shade water has a positive effect on bloom. This effect vanishes, if we have high shade.![[Pasted image 20250922114436.png]]