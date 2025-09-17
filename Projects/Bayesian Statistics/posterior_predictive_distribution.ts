library(rethinking)
data(Howell1)
d <- Howell1

# Model
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

weight.seq <- seq(25, 70, 1)

# Posterior of population mean (mu)
post_mu <- link(m4.5, data=list(weight=weight.seq))
mu.mean <- apply(post_mu, 2, mean)
mu.PI89 <- apply(post_mu, 2, PI, prob=0.89)

# Posterior predictive (new heights)
post_y  <- sim(m4.5, data=list(weight=weight.seq))
y.mean  <- apply(post_y, 2, mean)
y.PI89  <- apply(post_y, 2, PI, prob=0.89)

# Base scatter
plot(height ~ weight, data=d2, col=col.alpha(rangi2, 0.3), main="Population vs Predictive Uncertainty",
     xlab="Weight", ylab="Height")

# Draw predictive interval first (wider)
shade(y.PI89, weight.seq, col=col.alpha("steelblue", 0.20))

# Draw population mean interval (narrower)
shade(mu.PI89, weight.seq, col=col.alpha("orange", 0.40))

# Lines
lines(weight.seq, y.mean, lwd=2, col="steelblue")
lines(weight.seq, mu.mean, lwd=2, col="orange")

legend("topleft",
       legend=c("Predictive mean (E[y])", "Population mean (mu)",
                "Predictive 89% PI", "Population 89% PI"),
       lwd=c(2,2, NA, NA),
       pch=c(NA,NA,15,15),
       pt.cex=2,
       col=c("steelblue","orange","steelblue","orange"),
       bty="n")

