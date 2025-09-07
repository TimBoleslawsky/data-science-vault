Evaluating models is essential in determining how good and how valuable a model is. The basic theories are explained in this note. 

First we need to define that there a different ways of evaluating a model:
- *Final Model Evaluation*: Assessing the trained model’s performance on unseen data using task-specific metrics. More on final model evaluation here: [[Final Model Evaluation]]
- *Model Selection & Tuning Hyperparameters*: Choosing a good model and optimizing this model’s configuration (e.g., tree depth, regularization) to improve performance. More on hyperparameter tuning here: [[Model Selection & Hyperparameter Tuning]]
- *Diagnosing Over- and Underfitting*. More on diagnosing over- and underfitting here: [[Diagnosing Over- and Underfitting]]
- *Ensuring Model Robustness & Generalization*: Ensure reliability on unseen data. More on model robustness and generalization here: [[Model Robustness & Generalization]]
## Model Evaluation and Tuning Process
Let's put all these methods into a process from start to finish:
- Step 1: Train Initial Model: 
  Here we want to: choose a baseline model (e.g., simple logistic regression, decision tree), train this model using a sensible initial set of hyperparameters, get an initial understanding of the performance by using a train-validation split or cross-validation (final model evaluation).
- Step 2: Model Selection & Hyperparameter Tuning:
  In most cases, we would want to compare and improve our model. Model selection means that optimally we want more than one model for problem and compare. Hyperparameter tuning means, that we want to improve our model by adjusting the input values. 
- Step 3: Diagnose Over- & Underfitting
  Just a model might be performing good or better than other models, does not mean, that it might not be over- or underfitted. 
- Step 4: Ensure Model Robustness & Generalization
  To ensure that our model works with different data and under different circumstances, we can for example do out-of-distribution data tests or tests on augmented data. 
- Step 5: Final Model Evaluation
  After all that is done, we want a final assessment of a completely trained model on completely unseen test data and compare this to some baseline model.