When it comes to diagnosing over- and underfitting we have two popular and simple ways of doing this. An example can be seen here: [[Hyperparameter Tuning & Overfitting Analysis in Python]].

First, the learning curve. The learning curve, shows how a model’s performance (e.g., accuracy, loss) changes with increasing training data. This helps to diagnose if more data would improve the model. How this detects over- and underfitting:
- Underfitting: Both training and validation scores are low and close to each other → the model is too simple.
- Overfitting: The training score is high, but the validation score is much lower → the model memorizes training data but generalizes poorly.

Second, the validation curve. The validation curve, shows how a model’s performance changes as a function of a hyperparameter (e.g., regularization strength, tree depth). This helps find optimal hyperparameter values to reduce overfitting or underfitting. How this detects over- and underfitting: 
- Underfitting: Both training and validation scores are low across all hyperparameter values.
- Overfitting: Training score is high, but validation score drops as complexity increases.