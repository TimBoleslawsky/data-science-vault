Here is a very simple example of how we can do hyperparameter tuning for a few classifiers and an overfitting analysis for a regression model. 
## Hyperparameter Tuning
For the hyperparameter tuning example, we want to first get some data (in a train-test split), then we want to train a few classifiers (could also be done with just one) and make a guess for the hyperparameters and make some evaluation with a final model evaluation metric.

After that we use RandomizedSearchCV to go through a few options for the hyperparameters and pick the best ones according to a specified metric.

``` python
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.2, random_state=RANDOM_SEED)

dtree_clf = DecisionTreeClassifier(random_state=RANDOM_SEED, max_depth=5)
dtree_val_score = cross_val_score(dtree_clf, Xtrain, Ytrain)
dtree_mean_score = np.mean(dtree_val_score) # Compute the mean accuracy

rforest_clf = RandomForestClassifier(random_state=RANDOM_SEED, max_depth=5)
rforest_val_score = cross_val_score(rforest_clf, Xtrain, Ytrain)
rforest_mean_score = np.mean(rforest_val_score) # Compute the mean accuracy

scaler = StandardScaler()
Xtrain_scaled = scaler.fit_transform(Xtrain) # Use a scaler to normalize the feature values. This ensures that we don't get a convergence warning.
Xtest_scaled = scaler.fit_transform(Xtest)
lg_regression = LogisticRegression(max_iter=100)
lg_regression.fit(Xtrain_scaled, Ytrain)
lg_score = lg_regression.score(Xtest_scaled, Ytest)

# Decision Tree Classifier average accuracy over 5 folds: 0.9282352941176469
# Random Forest Classifier average accuracy over 5 folds: 0.9241176470588236
# Logistic Regression Classifier accuracy: 0.8755868544600939

# Hyperparameter Tuning
from sklearn.model_selection import RandomizedSearchCV

param_grid = {
'max_depth': [None, 5, 10, 20]
}
random_search = RandomizedSearchCV(dtree_clf, param_grid, n_iter=4, cv=5, scoring='accuracy', random_state=RANDOM_SEED)
random_search.fit(Xtrain, Ytrain)
print("Best Parameters:", random_search.best_params_)

param_grid = {
'max_depth': [5, 10, 20, None]
}
random_search = RandomizedSearchCV(rforest_clf, param_grid, n_iter=4, cv=5, scoring='accuracy', random_state=RANDOM_SEED)
random_search.fit(Xtrain, Ytrain)
print("Best Parameters:", random_search.best_params_)

param_dist = {
'max_iter': [100, 200, 300, 400]
}
random_search = RandomizedSearchCV(lg_regression, param_dist, n_iter=4, cv=5, scoring='accuracy', random_state=RANDOM_SEED)
random_search.fit(Xtrain_scaled, Ytrain)
print("Best Parameters:", random_search.best_params_)
```

## Overfitting Analysis
Let's say we have some regressor (SomeRegressor) and we want to see if the model is overfitting or not. We can do this with the following for-loop.

``` python
# Investigating Over- and Underfitting
train_scores = []
test_scores = []

for i in range(1, 12):
	regr = SomeRegressor(max_depth=i, threshold=0.01) # Placeholder
	regr.fit(Xtrain, Ytrain)
	train_scores.append(mean_squared_error(Ytrain, regr.predict(Xtrain)))
	test_scores.append(mean_squared_error(Ytest, regr.predict(Xtest)))


plt.figure(figsize=(10,6))
plt.plot(range(1, 12), train_scores, 'o-', label="Training")
plt.plot(range(1, 12), test_scores, 'o-', label="Validation")
plt.title("Validation Curve for Tree Regressor")
plt.xlabel("Max Depth")
plt.ylabel("Mean Squared Error")
plt.legend()
plt.grid(True)
plt.show()
```