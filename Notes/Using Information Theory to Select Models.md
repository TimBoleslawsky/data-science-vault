The information theory concepts discussed in this note are explain in more detail here: [Foundations of Information Theory](Foundations%20of%20Information%20Theory.md).
## What is Model Accuracy?
The intuition for the flow below is this:
- **Entropy** = uncertainty in one distribution.
- **Cross-entropy** = expected uncertainty if reality is $p$ but we use $q$.
- **KL divergence** = difference in uncertainty between two distributions.
- **Deviance** = sample-based estimator of that penalty, scaled by -2.
## Predicting Predictive Accuracy
The goal here is to guess how well the model will perform, on average, in predicting new data. This is then used to support the model selection process. 
- Cross-validation (CV, LOOCV, PSIS-LOO): empirical re-use of data to approximate out-of-sample deviance. More on cross-validation here: [Cross-validation](Data%20Usage%20in%20Model%20Selection%20and%20Evaluation.md#cross-validation). The usage of cross-validation in this context differs a little bit, because usually we want to select models based on deviance. So that is what is computed here. 
- Information criteria (AIC, DIC, WAIC, BIC): analytic approximations based on information theory￼. More on that here [Information Criteria Methods for Model Selection](Information%20Criteria%20Methods%20for%20Model%20Selection.md). 

This is (more so in ML and DL models) supplemented with hyperparameter tuning. More on that, here: [Model Selection & Hyperparameter Tuning](Model%20Selection%20&%20Hyperparameter%20Tuning.md).
## Connecting Information Theory to Final Model Evaluation
In the note for final model evaluation ([Final Model Evaluation](Final%20Model%20Evaluation.md)), I talk about the metrics for reporting the performance of a model. One might now ask: "Why is entropy not part of this, if it is the theoretical gold standard for accuracy?".

The problem is, that we cannot compute true entropy, only approximate it. Information criteria and cross-validation are practical tools to estimate the predictive entropy _out-of-sample_, but for reporting purposes these estimations are useless.

That’s why you don’t see people report “entropy = 1234.5” in results sections. They report RMSE, accuracy, etc., for interpretability — and use WAIC/LOO/AIC under the hood to decide _which model_ is most trustworthy.
