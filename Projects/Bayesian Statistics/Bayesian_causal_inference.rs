library(rethinking)

# Load reviewer-level data
reviewers <- read.csv(
    "/Users/timboleslawsky/Documents/Empirical Software Engineering/Assignment/reviewers.csv"
)

# Load review-level data
reviews <- read.csv(
    "/Users/timboleslawsky/Documents/Empirical Software Engineering/Assignment/reviews.csv"
)

data_analysis <- FALSE # Set to FALSE to skip data analysis section
model <- "quality" # Choose "extent" or "quality" model to run
set.seed(2405)

# Merge on reviewer.id (since both tables have it)
d <- merge(reviews, reviewers, by = "reviewer.id")

if (data_analysis == TRUE) {
  print(precis(d[, c("age", "skill",
                     "used.cr.technology", "complexity",
                     "extent", "quality")]))

  hist(d$quality)
}

# Standardize function
d$age_s        <- standardize(d$age)
d$skill_s      <- standardize(d$skill)
d$complexity_s <- standardize(d$complexity)

d$log_extent <- log(d$extent)

dat_list <- list(
  extent = d$log_extent,
  used_cr_technology = d$used.cr.technology,
  age_s = d$age_s,
  skill_s = d$skill_s,
  complexity_s = d$complexity_s,
  quality = as.integer(d$quality),
  K = 5
)

if (model == "extent") {
  # Model 1: Causal effect of tech on extent
  m_extent <- ulam( # For direct effect of technology on extent
    alist(
      extent ~ dnorm(mu, sigma),
      mu <- a +
        b_tech * used_cr_technology +
        b_age * age_s +
        b_skill * skill_s +
        b_complexity * complexity_s,
      a ~ dnorm(0, 1),
      c(b_tech, b_age, b_skill, b_complexity) ~ dnorm(0, 0.5),
      sigma ~ dexp(1)
    ), data = dat_list, chains = 4, cores = 4
  )

  m_extent_min <- ulam( # For total effect of technology on extent
    alist(
      extent ~ dnorm(mu, sigma),
      mu <- a + b_tech * used_cr_technology + b_skill * skill_s,
      a ~ dnorm(0, 1),
      b_tech ~ dnorm(0, 0.5),
      b_skill ~ dnorm(0, 0.25),
      sigma ~ dexp(1)
    ), data = dat_list, chains = 4, cores = 4
  )

  m_extent_test <- ulam( # Test model without skill to see confounding effect
    alist(
      extent ~ dnorm(mu, sigma),
      mu <- a + b_tech * used_cr_technology,
      a ~ dnorm(0, 1),
      c(b_tech) ~ dnorm(0, 0.5),
      sigma ~ dexp(1)
    ), data = dat_list, chains = 4, cores = 4
  )

  # Prior predictive checks for m_extent_min
  prior <- extract.prior(m_extent_min)

  skill_seq <- seq(-2, 2, length.out = 50)
  newdat <- list(
    used_cr_technology = rep(c(0, 1), each = length(skill_seq)),
    skill_s = rep(skill_seq, times = 2)
  )

  mu_prior <- link(m_extent_min, post = prior, data = newdat)

  plot(NULL, xlim = c(-2, 2), ylim = c(-3, 3),
       xlab = "Skill (standardized)", ylab = "Extent (prior predictive)",
       main = "Prior predictive checks")

  for (i in 1:50)
  lines(
    skill_seq,
    mu_prior[i, seq_along(skill_seq)],
    col = col.alpha("blue", 0.3)
  )
  for (i in 1:50)
  lines(
    skill_seq,
    mu_prior[i, (length(skill_seq) + 1):(2 * length(skill_seq))],
    col = col.alpha("red", 0.3)
  )

  legend("topleft", legend = c("No technology", "Uses technology"),
         col = c("blue", "red"), lwd = 2, bty = "n")

  # Traceplot for m_extent_min
  traceplot(m_extent_min)

  Print summaries and exponentiated coefficients
  cat("\nDirect effect model summary:\n")
  print(precis(m_extent))

  post <- extract.samples(m_extent)
  print(mean(exp(post$b_tech)))
  print(HPDI(exp(post$b_tech), 0.89))

  cat("\nTotal effect model summary:\n")
  print(precis(m_extent_min))

  post <- extract.samples(m_extent_min)
  print(mean(exp(post$b_tech)))
  print(HPDI(exp(post$b_tech), 0.89))

  cat("\nTest model (tech only) summary:\n")
  print(precis(m_extent_test))

  post <- extract.samples(m_extent_test)
  print(mean(exp(post$b_tech)))
  print(HPDI(exp(post$b_tech), 0.89))
}

if (model == "quality") {
  # Model 2: Causal effect of tech on quality
  m_quality <- ulam( # Direct effect with controls
    alist(
      quality ~ ordered_logistic(eta, cutpoints),
      eta <- a +
        b_tech * used_cr_technology +
        b_age * age_s +
        b_skill * skill_s +
        b_complexity * complexity_s,
      a ~ dnorm(0, 1),
      c(b_tech, b_age, b_skill, b_complexity) ~ dnorm(0, 0.5),
      cutpoints ~ dnorm(0, 1.5)
    ), data = dat_list, chains = 4, cores = 4
  )

  m_quality_min <- ulam( # Total effect
    alist(
      quality ~ ordered_logistic(eta, c),
      eta <- a + b_tech * used_cr_technology + b_skill * skill_s,
      a ~ dnorm(0, 1),
      b_tech ~ dnorm(0, 0.5),
      b_skill ~ dnorm(0, 0.25),
      ordered[K - 1]:c ~ dnorm(0, 1.5)
    ), data = dat_list, chains = 4, cores = 4
  )

  Prior predictive checks for m_quality_min
  prior <- extract.prior(m_quality_min)

  skill_seq <- seq(-2, 2, length.out = 50)
  newdat <- list(
    used_cr_technology = rep(c(0, 1), each = length(skill_seq)),
    skill_s = rep(skill_seq, times = 2)
  )

  y_tilde <- sim(m_quality_min, data = newdat, post = prior)
  print(hist(y_tilde))

  # Traceplot for m_quality_min
  traceplot(m_quality_min)

  m_quality_test <- ulam( # Tech only
    alist(
      quality ~ ordered_logistic(eta, cutpoints),
      eta <- a + b_tech * used_cr_technology,
      a ~ dnorm(0, 1),
      b_tech ~ dnorm(0, 0.5),
      cutpoints ~ dnorm(0, 1.5)
    ), data = dat_list, chains = 4, cores = 4
  )

  cat("\nQuality model (direct) summary:\n")
  print(precis(m_quality, depth = 2))

  post <- extract.samples(m_quality)
  print(mean(exp(post$b_tech)))
  print(HPDI(exp(post$b_tech), 0.89))

  cat("\nQuality model (total) summary:\n")
  print(precis(m_quality_min, depth = 2))

  post <- extract.samples(m_quality_min)
  print(mean(exp(post$b_tech)))
  print(HPDI(exp(post$b_tech), 0.89))

  cat("\nQuality model (tech only) summary:\n")
  print(precis(m_quality_test, depth = 2))

  post <- extract.samples(m_quality_test)
  print(mean(exp(post$b_tech)))
  print(HPDI(exp(post$b_tech), 0.89))
}