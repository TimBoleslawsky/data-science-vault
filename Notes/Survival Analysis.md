For a hands-on example of survival analysis in R, look here: [[Survival Analysis.pdf]]
## **What Is Survival Analysis?**
Survival analysis deals with data where the outcome of interest is **the time until an event occurs** (e.g., death, disease progression, equipment failure). It’s used in:
- Medicine (e.g., time until death after diagnosis)
- Life insurance (e.g., predicting policyholder longevity)
- Engineering (e.g., time until machine failure)

A key characteristic of survival data is **censoring**, meaning some individuals don’t experience the event before the study ends. This, among other things, leads to the need of special statistical methods => We need special estimation techniques! Here's why:
- **Censoring (Incomplete Observations)**: In a typical continuous variable analysis (e.g., linear regression), we assume we observe the full value for each subject. However, in survival analysis, not all subjects experience the event within the study period. Some subjects might survive or drop out.
- **Skewed Distributions & Non-Normality**: Many statistical methods assume normally distributed continuous variables. Survival times often follow skewed distributions (e.g., exponential, Weibull) rather than a normal distribution.

Important functions and notation for survival analysis: 
- $T_i$: Event time (e.g., time until death)
- $C_i$: Censoring time (e.g., study ends before event occurs)
- $X_i = \min(T_i, C_i)$: Observed time (event or censored)
- $\Delta_i = I(T_i \leq C_i)$: Indicator variable (1 = event occurred, 0 = censored)
- $Z_i(t)$: Covariates (e.g., age, treatment group)
- $S(t) = P(T > t)$: Survival function (probability of surviving past time $t$)
- $F(t) = P(T \leq t)$: Cumulative distribution function
- $h(t) = \frac{f(t)}{S(t)}$:  Hazard function, measures instantaneous risk of an event at time $t$, given survival up to $t$.
## Estimating the Survival Function
Since patients enter studies at different times, survival time must be adjusted accordingly. The **Kaplan-Meier estimator** is widely used. The first idea is to use time in study instead of actual time: 
![[Pasted image 20250301160735.png|00]]

The second idea is to produce a stepwise survival curve that decreases at event times. This can look like this: 
![[Pasted image 20250301160855.png|400]]

The steps to produce this look like this. Let's say we have the following observations: order event times: 59 115 156 268 329 431 | 638 and ordered non-event times: 448 477 | 803 855 1040 1106. This means that for example at time 59 there was an event and at time 448 there was a censoring (end of observation, withdrawal, ...). We can now calculate the following for each step:
- $d_k$: Number of events at time $t_k$.
- $m_k$: Number of censored observations in ($t_k$,$t_{k+1}$)
- $n_k$: Number of patients at risk just prior to $t_k$. 
=> the estimation of the survival function $s(t)$ is then the product of ($1-\frac{d_k}{n_k}$) of all $t$'s up until now. Example: 
![[Pasted image 20250301161841.png|600]]
## Comparing Survival Functions: Log-Rank Test
To compare survival between groups (e.g., two treatment arms), the **Log-Rank Test** is used. It tests whether there is a significant difference in survival times between groups by checking if the hazard functions are proportional over time. 

The key assumption of the log-rank-test is that **the hazard ratio between groups remains constant over time** (i.e., proportional hazards assumption).

**Step 1**: Order the observations and calculate necessary statistics: 
- First we order the event and non-event times of both groups. 
- At each event time $t_k$ we then want to calculate:
	- $d_{1k}$ number of events at time $t_k$ for group 1.
	- $n_{1k}$: number of patients at risk just prior to $t_k$ for group 1. 
	- $e_{1k} = \frac{n_{1k} d_k}{n_k}$:  expected number of $d_{1k}$. 
	- $v_{1k}$: variance of $d_{1k}$ (formula is not that important).
	- $d_1$: sum of $d_{1k}$ for all $k$.
	- $e_1$: sum of $e_{1k}$ for all $k$.
	- $v_1$: sum of $v_{1k}$ for all $k$.
**Step 2:** Formulate hypothesis and compute the test statistic:
- The hypothesis we want to test is: $H_0: h_1(t) = h_2(t)$ for all $t$. 
- For this, we want to check if the ratio of observed vs. expected events is proportional across the groups. 
- The test statistic is then $X_{LR} = \frac{(d_1-e_1)^2}{v_1}$. This follows an approximate chi-square distribution with 1 degree of freedom.
## Cox Proportional Hazards Model (Cox PH Model)
The problem with the log-rank test is, that it cannot account for continuous covariates. The Cox PH model is a semi-parametric model used in survival analysis to examine the effect of multiple covariates on survival time. Unlike other parametric models, it does not assume a specific distribution for survival times. => We estimate the *relative* risk of an event given a specific time by comparing two groups.

**Proportional Hazards Assumption**
The **“proportional hazards”** assumption means that the ratio of hazards between two individuals remains constant over time. This means that:
- The effect of covariates does not change over time.
- The hazard ratio (HR) between two groups is constant.
	=> If receiving treatment A halves the risk of death compared to treatment B, this remains true at all time points.

Since the Cox model assumes hazards are proportional, this needs to be checked. For example, this can be checked graphically. For example like this: 
![[Pasted image 20250302094520.png]]
- Compute Kaplan-Meier estimate for each group.
- Plot separate lines log(-log(KM\$surv)) versus log(KM\$time) for each group.

**Model Architecture**
The Cox model describes the hazard function $h(t | Z)$ as:
$h(t | Z) = h_0(t) \exp(\beta_1 Z_1 + \beta_2 Z_2 + \dots + \beta_p Z_p)$

where:
- $h(t | Z)$ = hazard at time $t$ for a subject with covariates $Z$.
- $h_0(t)$ = baseline hazard function, representing the hazard when all covariates are zero.
- $\beta_1, \beta_2, \dots$ = regression coefficients, estimating the effect of covariates on the hazard.
- $Z_1, Z_2, \dots$ = covariates (e.g., treatment, age, disease severity).
=> The key idea is, that thee hazard at time $t$ is a product of: A baseline hazard $h_0(t)$ and an exponential function of covariates (which determines relative risks).

**Hypothesis Testing with Cox PH Model**
The hypothesis being tested in the Cox model could for example be:
- Null hypothesis ($H_0$): The covariate (age) has no effect on the hazard function.
- Alternative hypothesis ($H_A$): The covariate (age) significantly affects the hazard function.

Mathematically, this means testing whether the regression coefficient for age ($\beta_{\text{age}}$) is zero:
- $H_0: \beta_{\text{age}} = 0$
- $H_A: \beta_{\text{age}} \neq 0$

