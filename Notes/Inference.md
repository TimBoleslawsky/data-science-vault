After defining a mathematical model and estimating its parameters ([[Basics of Probability and Statistics for Data Science#Connecting Probability and Statistics to Modeling]]) we can use it to do inference. Inference is the _interpretation of parameter estimates under uncertainty_:
- Frequentist → uncertainty comes from sampling distribution. 
- Bayesian → uncertainty comes from both the sample and what you knew before seeing the data (the prior).
## Different Types of Inference
Based on the goal of the inference, we can differentiate between three major branches of inference: 
### Descriptive / Statistical Inference
Here the goal is to purely summarize or characterize the data and estimate parameters of a model. We would for example estimate the average effect of a drug on blood pressure, along with a 95% confidence interval.
### Associational / Correlational Inference
Now we want to also identify associations or correlations between variables, often using regression or correlation measures. Hypotheses might be about whether two variables are correlated, or whether a regression coefficient is significantly different from zero.
### Causal Inference
Goal here is to estimate the effect of interventions, counterfactual outcomes, or treatment effects. While correlational inference only tells us “$X$ and $Y$ move together", causal inference asks: _"What would $Y$ have been if we had intervened on $X$?"_.

More on causal inference here: [[Causal Inference]].
## Bayesian Inference
In this example I describe the basic intuitions behind Bayesian inference and how it connects to the statistical modeling approach. 

- First, model definition. Let's say we are interested in the body mass of Gentoo penguiins. Our target variable $y$ is the typical body mass of Gentoo penguins. So we want a model that describes how these body masses are generated.
- Second, we define the random variables $y$ (target variable), $μ$ (population mean), $σ$ (population standard deviation). 
- Third, we need to define the distribution underlying these random variables to model the uncertainty. Here we just take our best guess for now. This is the prior in Bayesian terms. For $μ$ and $σ$ we might define, for example: $\mu \sim \text{Normal}(4000, 500), \quad \sigma \sim \text{Exponential}(1/500)$.  This encodes our uncertainty about these parameters **before seeing data**. 
  => We now have our model or ‘function’ to infer or predict the typical body mass of Gentoo penguins.
- Fourth, now we do parameter estimation. We here assume that $σ$ is known. In this case we use MCMC (for inference we usually do not use [[Parameter Estimation for Probabilistic Models#Maximum A Posteriori (MAP) Estimation|MAP]], because this only gives us a point estimate). The result in this case is not a point estimate for the parameters (like in the frequentist approach), but a posterior distribution for $μ$. In our example this looks like this: $\mu \mid y \sim \text{Normal}\Big(\frac{\frac{\mu_0}{\sigma_0^2} + \frac{n \bar{y}}{\sigma^2}}{\frac{1}{\sigma_0^2} + \frac{n}{\sigma^2}}, \;\; \frac{1}{\frac{1}{\sigma_0^2} + \frac{n}{\sigma^2}}\Big)$, where 
	- $\mu_0$, $\sigma_0^2$ are the prior mean and variance of $μ$
	•	$n$ is the sample size
	•	$\bar{y}$ is the sample mean
	•	$\sigma^2$ is the known variance of the data
- Fifth, using this posterior distribution, we can directly infer about point estimates and interval estimates. In reality it is often useful to use sampling to summarize the posterior, rather than relying solely on closed-form analytical solutions. This gives a practical, flexible way to perform Bayesian inference:
	- Point estimations: You can summarize the posterior by a single representative value of a parameter. Through sampling this is just computing the mean or median of your posterior samples.    
	- Interval estimations: Instead of just a point, you summarize the **uncertainty** around a parameter (credible intervals). Sampling lets you directly compute intervals: e.g., take the 2.5th and 97.5th percentiles of your posterior samples.
	- Probability estimations (probabilistic statements): This could for example be: $P(μ > 4500,g \mid \text{data})$. Using samples, you simply count the fraction of posterior draws satisfying the condition.
=> The results are our general assumptions about the population given our assumptions, previous knowledge and the data we observed.
## Frequentist Inference
In this example, I describe the basic intuitions behind frequentist inference and how it connects to the statistical modeling approach.

- First, model definition. Let’s say we are again interested in the body mass of Gentoo penguins. Our target variable $y$ is the typical body mass of Gentoo penguins. So we want a model that describes how these body masses are generated (same as Bayesian).
- Second, we define the random variables $y$ (target variable). The population mean $\mu$ and the population standard deviation $\sigma$ are constants describing the population but whose values we do not know.
- Third, we need to define the distribution underlying these random variables to model the uncertainty. Here we take an assumption about the population, for example: $y_i \sim \text{Normal}(\mu, \sigma^2)$. This encodes our assumptions about the population before seeing data, but unlike Bayesian priors, these are fixed unknown parameters rather than probability distributions.
  => We now have our model or ‘function’ to infer or predict the typical body mass of Gentoo penguins.
- Fourth, now we do parameter estimation. In the frequentist approach, this is usually done using [[Parameter Estimation for Probabilistic Models#Maximum Likelihood Estimation (MLE)|MLE]]. The goal is to find the parameter values that make the observed data most probable. Assuming $\sigma^2$ is known, the MLE for $\mu$ is: $\hat{\mu} = \bar{y} = \frac{1}{n}\sum_{i=1}^{n} y_i$
	Here:
	- $n$ is the sample size
	- $\bar{y}$ is the sample mean
	The key difference from Bayesian estimation: $\hat{\mu}$ is a point estimate, not a distribution. These are called **estimators** in frequentist inference.
- Fifth, inference. Inference is based on the **sampling distribution** of the estimator. The sampling distribution says: *"If I estimate some function of the data repeatedly, what distribution does that estimator have under repeated sampling?*". In our example this would look like this: $\hat{\mu} \sim \text{Normal}\Big(\mu, \frac{\sigma^2}{n}\Big)$.
	We use this distribution to make statements about the unknown parameter $\mu$:
	- Point estimate: $\hat{\mu} = \bar{y}$
	- Interval estimate (confidence interval): A 95% confidence interval for $\mu$ is $\bar{y} \pm 1.96 \frac{\sigma}{\sqrt{n}}$, which means that if we repeated the experiment many times, 95% of such intervals would contain the true $\mu$.
	- Hypothesis tests / probabilities: Here we need a **test statistics and a null models**. Here is how we construct this and how we test hypothesis with it:
		- The null model is a restriction on the generative model we defined earlier. For example if our generative model is $y_i \sim \text{Normal}(\mu, \sigma^2)$, our null model could be $\mu = \mu_0$, with $\mu_0 = 4500g$. So this is just an "instance" of the generative model. 
		- The test statistic is supposed to capture the difference between some estimated parameter and the corresponding parameter in the null model. This could for example be $\hat{y}-\mu_0$.
		- To test the hypothesis described by the null model, we now calculate the probability of seeing a test statistic at least as extreme as the one we actually observed, given the null hypothesis: $p = P_{H_0}\big( |T| \ge |t_{\text{obs}}| \big)$. This corresponds to the [[Distribution#Cumulative Distribution Function for Continuous Random Variables|CDF]] in relation to $t_{obs}$!
			- Here $t_{obs}$ is the calculated test statistic with our data and $T$ is the random variable describing the test statistic according to the null model aka the sampling distribution. So we observe how $t_{obs}$ compares to the distribution $T$ would have, if the hypothesis would be true. 
			- The p-value here measures how far out in the tail our point lies. So a p-value of $0.03$ for example could mean that if the null hypothesis were true, there would be a 3% probability of observing a test statistic as extreme or more extreme than what you actually observed. 
		=> This whole hypothesis testing framework in the frequentist approach is pretty standardized. More on this here: [[Hypothesis Testing Framework in Frequentist Inference]] .
=> The results in this case are statements about the behavior of estimators over repeated sampling, not direct probabilities.
## Interpreting Inference
Both Bayesian and frequentist inference can be thought of as providing three kinds of results:
- Point estimates
- Interval estimates
- Probability / Hypothesis-based estimates

But the **meaning and interpretation** of each is different between the two frameworks as shown below:
1. Point estimates
	- Bayesian: “Given the data and prior assumptions, the most plausible value(s) of the parameter.” => This means the inference is about the parameter itself. In reality the Bayesian point estimate is the summary of a distribution not really a point estimate and is usually more stable because it incorporates prior knowledge. 
	- Frequentist: "The single parameter value that would make the observed data most likely (MLE). If we assume repeated samples, the expected sample mean converges to the true $μ$”” => In this case inference is about the estimator’s behavior. 
2. Interval estimates
	- Bayesian (Credible Interval): Defined directly from the posterior distribution. A $95$% credible interval for $μ$ is an interval $[a,b]$ such that $P(\mu \in [a,b] \mid \text{data}) = 0.95$. We interpret this as: “There is a $95$% probability that the true $μ$ lies in this interval, given data + prior.”
	- Frequentist (Confidence Interval): Defined from the sampling distribution of the estimator. A $95$% CI is $\bar{y} \pm 1.96 \frac{\sigma}{\sqrt{n}}$ (if $σ$ known). We interpret this as: “If we repeated this experiment infinitely many times, and constructed a confidence interval each time, then $95$% of those intervals would include the true mean $μ$.”
3. Probability / Hypothesis-based estimates
	- Bayesian (Posterior probabilities): You can compute the probability of hypotheses directly; no formal hypothesis testing "ritual" is necessary. Example: $P(\mu > 4500 \mid \text{data}) = 0.85$ => “Given the data and prior, there is an 85% probability that the average Gentoo mass exceeds 4500 g”.
	- Frequentist (Sample probabilities): You cannot assign probability to hypotheses; instead, you compute the probability of the data under a null hypothesis. Example: Testing $H_0: \mu = 4500$: $p = 0.04$ means “If $μ = 4500$ were true, data this extreme or more would occur 4% of the time.”
## Meta Analysis
When we want to infer some knowledge from more than one source (study, article, ...) we can use meta analysis. Here is how we do that: [[Meta Analysis]]
