The first rule of thumb is a model's performance needs to be evaluated on data that was never used to train the model. We call this the test set (in contrast to the training set). *Never ever evaluate the model on the training set!*
## Train-test Split
The idea behind the Train-test split is to divide our data so that we have a **training set** to develop and train our model, an optional **validation set** to help with parameter selection to optimize our model if needed, and a **test set** where we can run final tests. Usually, the split is 75/25 if we have two sets and 50/25/25 if we have three sets. 
## Cross-validation
But what if we have very little data? Then we can use cross-validation to repeatedly partition our data into test data and training data and train/test on each of these iterations. One example, of how we can do this is **k-fold cross-validation**.

When using k-fold cross-validation, we divide the entire dataset into k approximately equal-sized folds. Each fold serves as a test set exactly once, while the remaining k-1 folds form the training set. Repeat this process k times, each time using a different fold as the test set. **Leave-One-Out Cross-Validation (LOOCV)** is a special case of k-fold where k equals the number of data points (i.e., each fold contains one data point).

The problem with LOOCV, is that it requires re-fitting the model _n_ times (once per observation), which is computationally expensive, especially in Bayesian models where each fit may require MCMC. In Bayesian models, we have a solution for this: Pareto Smoothed Importance Sampling or PSIS. Here is how it works:
- Instead of refitting, we re-weight the posterior draws we already have (from the full model) to approximate what the posterior would look like if each observation had been left out.    
- These re-weightings can be unstable, so Pareto smoothing is applied to stabilize the importance weights. 
- The result is **PSIS-LOO**, an efficient and reliable approximation of exact LOO cross-validation.

It is important to note, that cross-validation, is a framework that can be used for multiple purposes. We can use it for model selection and then compare metrics like deviance ([[Using Information Theory to Select Models#Deviance]]), or we can use it for actual model evaluation and then we usually use metrics like the RMSE, $R^2$, accuracy.