When it comes to model selection & hyperparameter tuning, we both want to check, which hyperparameters perform the best and which models (either different in hyperparameters or completely different) perform the best. We have methods that are only used for hyperparameter tuning and we have methods that are used for both, hyperparameter tuning and model selection. An example can be seen here: [[Hyperparameter Tuning & Overfitting Analysis in Python]].

It needs to be said that of course a sensible and easy way to do this for all types of models is just comparing different inputs (hyperparameters, model types, ...) and outputs (final model evaluation metrics). For example a common method for $k$-means clustering is taking the silhouette score (see picture below) and just comparing different $k$ values for that. The methods below are just more sophisticated applications of this principle.
## Hyperparameter Tuning
### GridSearchCV
GridSearchCV trains models for all possible hyperparameter combinations in a pre-defined grid. This leads to an exhaustive search and has a high chance of finding the best combination. But it is computationally expensive and scales poorly. 
### RandomizedSearchCV
RandomizedSearchCV randomly selects hyperparameter combinations from a search space and evaluates them. This leads to a faster runtime compared to grid search, but also a less exhaustive search. It may miss the absolute best combination.
### Validation Curve
Plots training and validation performance as a function of a hyperparameter (e.g., regularization strength). Helps visualize **overfitting vs. underfitting**.
### Elbow Method
In clustering, especially $k$-means, the elbow method is a popular model selection The elbow method is based on the **MSE**. When we perform $k$-means and evaluate the resulting clustering of different values for $k$ according to the MSE of the points from their centers, we get a graph that looks something like the one in the picture below.

![[Pasted image 20241205143119.png]]

What we seek from the error curve is the value $k$ where the rate of decline decreases drastically, or the *elbow*. 
## Model Selection (and Hyperparameter Tuning)
Like said above the most popular and the easiest way to select a model is by comparing final model evaluation metrics (MSE, Silhouette Score, Accuracy, ...). The methods below have more specific use-cases.
### AIC and BIC
AIC BIC 

