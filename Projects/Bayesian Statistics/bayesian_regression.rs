library(rethinking)
data(Howell1)
d <- Howell1
d2 <- d[d$age >= 18, ]  # restrict to adults

# 1. Simple Gaussian model (constant mean)
m4.1 <- quap(
    alist(
        height ~ dnorm(mu, sigma),
        mu ~ dnorm(178, 20),
        sigma ~ dunif(0, 50)
    ),
    data = d2
)

# Plot posterior distribution of parameters
post <- extract.samples(m4.1)
plot(post, main="Posterior")

# 2. Extended model with weight as predictor
m4.3 <- quap(
  alist(
    height ~ dnorm(mu, sigma),
    mu <- a + b * weight,
    a ~ dnorm(156, 100),
    b ~ dnorm(0, 10),
    sigma ~ dunif(0, 50)
  ),
  data = d2
)

# Plot data and regression line
plot(height ~ weight, data=d2)
post <- extract.samples(m4.3, 100)
a_map <- mean(post$a)
b_map <- mean(post$b)
curve( a_map + b_map*x , add=TRUE )

# 3. Log-transform weight and fit model
m4.5 <- quap(
  alist(
    height ~ dnorm(mu, sigma),
    mu <- a + b * log(weight),
    a ~ dnorm(156, 100),
    b ~ dnorm(0, 10),
    sigma ~ dunif(0, 50)
  ),
  data = d
)

# Plot data and regression line by sampling from posterior
plot(height ~ weight, data=d2)
post <- extract.samples(m4.5, 100)
a_map <- mean(post$a)
b_map <- mean(post$b)
curve( a_map + b_map*log(x) , add=TRUE )

# 4. Predict the population mean height and visualize predictions with uncertainty intervals
weight.seq <- seq(from=25, to=70, by=1)
mu <- link(m4.5, data=list(weight=weight.seq)) 
mu.mean <- apply(mu, 2, mean)
mu.PI <- apply(mu, 2, PI, prob=0.89)

plot(height ~ weight, data=d2, col=col.alpha(rangi2, 0.3))
lines(weight.seq, mu.mean)
shade(mu.PI, weight.seq)

# For a specific weight
w_pop <- 55 
mu_samp <- link(m4.5, data=list(weight=w_pop))
mu_mean <- mean(mu_samp)
mu_PI <- PI(mu_samp, prob=0.89)

print(c(mu_mean, mu_PI))

# 5. Simulate heights for a new weight and visualize predictions with uncertainty intervals
y <- sim(m4.5, data=list(weight=weight.seq)) 
y.mean <- apply(y, 2, mean)
y.PI <- apply(y, 2, PI, prob=0.89)

plot(height ~ weight, data=d2, col=col.alpha(rangi2, 0.3))
lines(weight.seq, y.mean)
shade(y.PI, weight.seq)

# For a specific weight
w_new <- 55
y_pred <- sim(m4.5, data=list(weight=w_new))   # draws of height
y_mean <- mean(y_pred)
y_PI <- PI(y_pred, prob=0.89)

print(c(y_mean, y_PI))