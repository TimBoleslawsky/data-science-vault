Other than cross-validation methods, information criteria methods try to construct a theoretical estimate of the relative out-of-sample K-L divergence. 

From information theory we know that log-likelihood is an excellent measure of surprise/entropy ([[Using Information Theory to Select Models]]). *Information criteria* modifies this penalties for complexity to estimate out-of-sample predictive accuracy.

Here are common methods to do this. In practice WAIC and PSIS-LOO are preferred for Bayesian models, because they use the entire posterior distribution and handle hierarchical/complex models better than AIC, BIC, or DIC.
## AIC (Akaike Information Criterion)
$\text{AIC} = -2 \,\ell(\hat\theta) + 2k$
- $\ell(\hat\theta)$ = maximized log-likelihood.
- $k$ = number of free parameters.
- Intuition: raw fit (log-likelihood) minus penalty for parameter count.
- Good for large-sample, regular models, but has a bunch of assumptions that make it unsuitable for complex models.
## BIC (Bayesian Information Criterion)
$\text{BIC} = -2 \,\ell(\hat\theta) + k \,\ln(n)$
- Same first term: maximized log-likelihood.
- Penalty: $k \ln(n)$ — harsher than AIC when $n$ is large.
- Motivation: derived as an approximation to the log marginal likelihood (Bayes factor), not truly Bayesian despite the name.
- Tends to favor simpler models as $n$ grows.
## WAIC (Watanabe–Akaike Information Criterion)
$\text{WAIC} = -2 \,\text{lppd} + 2p_{\text{WAIC}}$, where $\text{lppd} = \sum_{i=1}^n \log \Big( \frac{1}{S} \sum_{s=1}^S p(y_i \mid \theta^{(s)}) \Big)$ and $p_{\text{WAIC}} = \sum_{i=1}^n \text{Var}_s \big[ \log p(y_i \mid \theta^{(s)}) \big]$.
- Uses full posterior samples $\theta^{(s)}$, not just point estimates.
- Penalty term arises from variability in log-likelihood across posterior draws → effective complexity.
- Fully Bayesian, asymptotically equivalent to LOO cross-validation.
## Interpreting Information Criteria
Now that we have these scores and more importantly difference between models we compare, what do we do with them? 

Two important take-aways:
- A model that predicts well may not reflect the true causal relationships. Therefore, model comparison for predictive accuracy is distinct from identifying causal effects. Predictive-focused models might include confounding variables that improve prediction but misrepresent causality.
- Model comparison is a guide for choosing models that balance fit and generalizability. It informs which models are likely to predict well out-of-sample, but should be used in conjunction with domain knowledge and, when causal inference is the goal, careful causal modeling.
