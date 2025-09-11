## Random Variables
The foundation of random processes are [[Random Variables|random variables]]. These can either be discrete (taking specific values) or continuous (taking any value within a range) and represent possible outcomes from random processes.
## Probability and Statistics
Here is how **probability, inferential statistics, and descriptive statistics** relate to one another:
![[Pasted image 20241016102630.png|500]]
*It is important to keep in mind, that there exist two approaches to statistics, the **Bayesian approach** and the **Frequentist approach**. The differ in how they interpret probability, approach statistical inference, and handle uncertainty. More on the differences here: [[Two Approaches to Statistics]].*

[[Probability]] is inherently theoretical. We use Probability to guess certain characteristics of the population. Probability is how likely a certain outcome of a random variable is.

Through probability we can construct probabilistic concepts, describing relationships between random variables. These are then made concrete using statistics.
- [[Expected Value & Variance]]
- [[Covariance & Correlation|Correlation analysis]] examines the relationship between two or more variables and therefore identifies patterns between features (variables) in a dataset. 

While random variables define what is uncertain, distributions model uncertainty. More on distributions here: [[Distribution]].

Now all these inherently theoretical probabilistic concepts are made concrete using [[Descriptive Statistics|descriptive statistics]]. We use descriptive statistics to describe a sample. Within statistics we always talk about a sample of a population that we want to analyze. Here are the basics of [[Sampling|sampling]].
### Connecting Probability and Statistics to Modeling
First, *probability* defines the **theoretical framework of uncertainty**. It defines constructs such as random variables, distributions, expectation, variance, covariance, correlation, etc. and ells us _what outcomes could happen and with what probabilities_ if we knew the true population model.

Second, *sampling* probability to statistics and introduces randomness: each sample is one realization from the underlying population distribution. We don’t observe the full population distribution, only a **sample**.

Third, *descriptive statistics* make the probabilistic concepts observable in practice. With a sample in hand, we **compute empirical estimates** of the probabilistic quantities (mean, variance, correlations, etc.). These are **concrete, data-driven summaries** of uncertainty.

Lastly, *modeling*. We use descriptive statistics (and likelihoods, optimization, etc.) to **estimate parameters of models**. This can be deterministic (optimization) or probabilistic (MLE, MAP, Bayesian posterior). Once we have parameters, we can:
- **Infer** relationships (understand the data-generating process) => [[Inference]]
- **Predict** outcomes on new data => [[Prediction]]

**Markov’s Inequality** and **Chebyshev’s Inequality** are two further fundamental results in probability theory that provide important bounds on probabilities for random variables. They are especially useful in situations where we have limited information about the distribution of a random variable, and they help quantify the likelihood of extreme deviations from the mean. In data science, they are significant because they provide a theoretical basis for understanding the variability of data and for designing algorithms that account for uncertainty. More here: [[Inequality]].

