Evaluating models is essential in determining how good and how valuable a model is. The basic theories are explained in this note. 
## Overfitting and Underfitting
Central to evaluating a model, are the amount of features/predictors we include in the model. Adding a feature/predictor to a model can be a good thing or a bad thing and is heavily dependent on what the goal of the model should be (causal inference, prediction, ...). 

**Overfitting** occurs when a model learns too much from the sample. What this means is that there are both regular and irregular features in every sample. The regular features are the targets of our learning, because they generalize well or answer a question of interest. Regular features are useful, given an objective of our choice. The irregular features are instead aspects of the data that do not generalize and so may mislead us. Overfitted models learn both.

**Underfitting** produces models that are inaccurate both within and out of sample. They have learned too little, failing to recover regular features of the sample.
## Robustness and Generalization
If we manage both overfitting and underfitting, we get robust models that generalize well. Here is, what that means:

The **robustness** of the model is defined as the ability to handle unexpected or noisy inputs, including small changes in data distribution.

The **generalization** of the model is defined as the ability to perform well on truly unseen data, not just the training/validation/test set.
## Navigating Between Underfitting and Overfitting
To navigate between underfitting and overfitting to create robust models that generalize well, we us use two complementary toolkits:
1. Methods to _prevent_ overfitting. For preventing overfitting, two common methods are [[Regularization]] and building [[Ensemble Models]].
2. Predictive accuracy measures to _diagnose/compare_ models. More on that, here: [[Using Information Theory to Select Models]]. 

An important question to ask, is: "*What data do we use for model evaluation and selection?*". More on that here: [[Data Usage in Model Selection and Evaluation]].

Once we have build a few robust models using regularization or ensemble methods and selected the "best" one by predicting predictive accuracy, we can do: [[Final Model Evaluation]].
## Model Evaluation and Tuning Process in ML and DL
The techniques and methods described above, are far more systemized in machine learning and deep learning projects. In such projects there usually exists a standardize model evaluation process. Here is what such a process could look like:
- Step 1: Train Initial Model: 
  Here we want to: choose a baseline model (e.g., simple logistic regression, decision tree), train this model using a sensible initial set of hyperparameters, get an initial understanding of the performance by using a train-validation split or cross-validation (final model evaluation).
- Step 2: Model Selection & Hyperparameter Tuning:
  In most cases, we would want to compare and improve our model. Model selection means that optimally we want more than one model for problem and compare. Hyperparameter tuning means, that we want to improve our model by adjusting the input values. 
- Step 3: Diagnose Over- & Underfitting
  Just a model might be performing good or better than other models, does not mean, that it might not be over- or underfitted. (Deep Learning specific example: [[Diagnosing Over- and Underfitting in Deep Learning Models]])
- Step 4: Ensure Model Robustness & Generalization
  To ensure that our model works with different data and under different circumstances, we can for example do out-of-distribution data tests or tests on augmented data. 
- Step 5: Final Model Evaluation
  After all that is done, we want a final assessment of a completely trained model on completely unseen test data and compare this to some baseline model.