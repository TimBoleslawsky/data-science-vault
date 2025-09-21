## What is Model Accuracy?
The intuition for the flow below is this:
- **Entropy** = uncertainty in one distribution.
- **Cross-entropy** = expected uncertainty if reality is $p$ but we use $q$.
- **KL divergence** = difference in uncertainty between two distributions.
- **Deviance** = sample-based estimator of that penalty, scaled by -2.
### Information Entropy
Firstly, we need to introduce *information entropy*. Information entropy is a measure of uncertainty in a probability distribution, more specifically: the uncertainty contained in a probability distribution is the average log-probability of an event. And here is the formula for it: $H(p) = - \sum_i p_i \log p_i$.

Let's look at an example: To compute the information entropy for the weather, suppose the true probabilities of rain and shine are $p_1 = 0.3$ and $p_2 = 0.7$, respectively. Then: $H(p) = −(p_1 log(p_1) + p_2 log(p_2)) ≈ 0.61$. Suppose instead we live in Abu Dhabi. Then the probabilities of rain and shine might be more like $p_1 = 0.01$ and $p_2 = 0.99$. Now the entropy would be approximately $0.06$. Therefore there’s much less uncertainty about any given day, compared to a place in which it rains 30% of the time. It’s in this way that information entropy measures the uncertainty inherent in a distribution of events. 
### Cross Entropy and Divergence
The question now remains, *"How can we use information entropy to say how far a model is from the target?"*. The key lies in *divergence*. 

Before talking about divergence, we need to introduce *cross entropy*. Suppose the true distribution is $p$, but we approximate with a model distribution $q$. The cross-entropy is: $H(p, q) = - \sum_i p_i \log q_i$. This is the expected log-loss we suffer when reality is distributed as $p$, but we assign probabilities according to $q$.

The *Kullback–Leibler (KL) divergence* is now just the difference between cross-entropy and entropy: $D_{\text{KL}}(p \,\|\, q) = H(p, q) - H(p) = \sum_i p_i \log \frac{p_i}{q_i}$.
### Deviance
The above sounds nice, but unfortunately, we rarely know the true $p$, so we can’t compute KL divergence directly. That means we need an estimator relative KL divergence between the true generating process and the model $q$. That is *deviance*. 

The idea here, is that if we compare models relatively much of $p$ cancels out. What matters is each model’s average log-probability of the observed data. So we can compare the average log-probability from each model to get an estimate of the relative distance of each model from the target.

This is called a *log-probability score* or a *log-pointwise-predictive-density* in a Bayesian model (because we have to take the whole posterior distribution into account). Deviance is now just like a lppd score, but multiplied by $−2$ so that smaller values are better (2 for historical reasons).
## Predicting Predictive Accuracy
The goal here is to guess how well the model will perform, on average, in predicting new data. This is then used to support the model selection process. 
- Cross-validation (CV, LOOCV, PSIS-LOO): empirical re-use of data to approximate out-of-sample deviance. More on cross-validation here: [[Data Usage in Model Selection and Evaluation#Cross-validation]]. The usage of cross-validation in this context differs a little bit, because usually we want to select models based on deviance. So that is what is computed here. 
- Information criteria (AIC, DIC, WAIC, BIC): analytic approximations based on information theory￼. More on that here [[Information Criteria Methods for Model Selection]]. 

This is (more so in ML and DL models) supplemented with hyperparameter tuning. More on that, here: [[Model Selection & Hyperparameter Tuning]].
## Connecting Information Theory to Final Model Evaluation
In the note for final model evaluation ([[Final Model Evaluation]]), I talk about the metrics for reporting the performance of a model. One might now ask: "Why is entropy not part of this, if it is the theoretical gold standard for accuracy?".

The problem is, that we cannot compute true entropy, only approximate it. Information criteria and cross-validation are practical tools to estimate the predictive entropy _out-of-sample_, but for reporting purposes these estimations are useless.

That’s why you don’t see people report “entropy = 1234.5” in results sections. They report RMSE, accuracy, etc., for interpretability — and use WAIC/LOO/AIC under the hood to decide _which model_ is most trustworthy.
