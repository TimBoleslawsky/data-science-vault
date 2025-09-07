## Random Variables
The foundation of random processes are [[Random Variables|random variables]]. These can either be discrete (taking specific values) or continuous (taking any value within a range) and represent possible outcomes from random processes.
## Probability and Statistics
Here is how **probability, inferential statistics, and descriptive statistics** relate to one another:
![[Pasted image 20241016102630.png|500]]

[[Probability]] is inherently theoretical. We use Probability to guess certain characteristics of the population. Probability is how likely a certain outcome of a random variable is. In the context of Data Science, we make use of the predictive power of probability to guess at certain outcomes. The most important metrics for probability theory are described here: [[Expected Value & Variance]]

**Markov’s Inequality** and **Chebyshev’s Inequality** are two further fundamental results in probability theory that provide important bounds on probabilities for random variables. They are especially useful in situations where we have limited information about the distribution of a random variable, and they help quantify the likelihood of extreme deviations from the mean. In data science, they are significant because they provide a theoretical basis for understanding the variability of data and for designing algorithms that account for uncertainty. More here: [[Inequality]].

Although probability and **inferential statistics** are related, they are not the same. Here is the key difference: Probability talks about the theoretical likelihood of, for example, a variance. If we say a population has a variance in terms of probability, we guess at that variance. We use this to understand the likelihood of obtaining a specific sample. Inferential Statistics, on the other hand, calculates the population variance based on all data points in the population and is, therefore, an exact calculation. But, because we usually do not have this information, we infer it from sample characteristics, for example, the sample variance. Here, **descriptive statistics** is involved. Descriptive statistics is concerned with the frequency of past events. Descriptive statistics helps us understand the basic characteristics of data or a data sample. So descriptive statistics would be for computing the sample variance based on a data sample and inferential statistics would be for using this sample variance to make inferences or generalizations about a larger population. More on inference here: [[Inference]].

Within statistics we always talk about a sample of a population that we want to analyze. Here are the basics of [[Sampling|sampling]]. To describe a sample we use [[Descriptive Statistics|descriptive statistics]]. 

It is important to keep in mind, that there exist two approaches to statistics, the **Bayesian approach** and the **Frequentist approach**. The differ in how they interpret probability, approach statistical inference, and handle uncertainty. More on the differences here: [[Two Approaches to Statistics]]
## Correlation Analysis
Another important subject of statistics is [[Covariance & Correlation|correlation analysis]]. Correlation analysis examines the relationship between two or more variables and therefore identifies patterns between features (variables) in a dataset. 
## Distribution
[[Distribution]] is an important part of probability and statistics. The same distributions (e.g., normal, binomial, etc.) are used in both fields but with different goals: predicting or modeling versus describing or estimating.

Now an interesting question might be: Given a data set (a sample), what theoretical distribution best describes my data? For this, we can use the [[Q-Q Plot]]. 

The Q-Q plot gives us an estimate on the family of the probability distribution, but what about the parameters for the probability distribution? Then we use parameter estimation techniques like MLE, described here: [[Parameter Estimation for Probabilistic Models]]