Feature selection describes the activity of removing irrelevant or redundant features. But why do we do this?
- A large amount of features is undesirable because:
	- Higher computational cost (training time, energy usage)  
	- Difficult to generalize 
	- Less interpretability  
	- ...
- In dataset, where we have a lot more features compared to samples, we might overfit our model. 
## Filter Methods
Select features based on **statistical properties** of the data, independent of any machine learning model. We could for example use the F-score to rank the features: 

``` python
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(X, y)
```

This gives us a fast and model-agnostic way to do feature selection, but it also ignores interactions between features. 
## Wrapper Methods
Use a machine learning model to evaluate feature subsets, selecting those that give the best performance. Train and evaluate models with different feature subsets (e.g., using cross-validation), often using greedy algorithms like forward or backward selection.

``` python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

estimator = LogisticRegression()
selector = RFE(estimator, n_features_to_select=10)
X_selected = selector.fit_transform(X, y)
```

While this does consider feature interactions, it is computationally expensive.
## Hybrid Methods
Combine two or more approaches (usually filter + wrapper) to balance speed and accuracy. Often start with a filter to reduce dimensionality, then apply a wrapper on the reduced set. This could for example look like this: 

``` Python
from boruta import BorutaPy
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_jobs=-1)
selector = BorutaPy(rf, n_estimators='auto', verbose=0)
selector.fit(X.values, y.values)
```

## Embedded Methods
Feature selection is built into the model training process — the algorithm selects features as part of optimization. Models with regularization (like Lasso) naturally shrink coefficients of less useful features to zero. More on regularization here: [[Regularization]].

``` python
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.1)
model.fit(X, y)
selected_features = model.coef_ != 0
```

This is a very efficient method that also takes feature interaction into account. It can depend heavily on the choice of regularization though. 
