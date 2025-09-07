Let's first have a look at a simple VotingClassifier. Here we just list the classification methods we want to use and instantiate our VotingClassifier with this information. We can choose between soft and hard voting, depending on the outcome of the models.

``` python
from sklearn.ensemble import VotingClassifier

ensemble = [
            ('lr', LogisticRegression()),
            ('dt', DecisionTreeClassifier(max_depth=5)),
            ('lr1', LogisticRegression(penalty='l1', solver='liblinear')),
            ('mlp', MLPClassifier(hidden_layer_sizes=(8), max_iter=10000))
           ]

voting = VotingClassifier(ensemble)
#voting = VotingClassifier(ensemble, voting='soft')

voting.fit(Xtrain, Ytrain)

accuracy_score(Ytest, voting.predict(Xtest))
```

A little bit more advanced is the StackingClassifier. But the implementation looks exactly the same.

``` python
from sklearn.ensemble import StackingClassifier

ensemble = [
            ('lr', LogisticRegression()),
            ('dt', DecisionTreeClassifier(max_depth=5)),
            ('lr1', LogisticRegression(penalty='l1', solver='liblinear')),
            ('mlp', MLPClassifier(hidden_layer_sizes=(8), max_iter=10000))
           ]

stacking = StackingClassifier(ensemble)

stacking.fit(Xtrain, Ytrain)

accuracy_score(Ytest, stacking.predict(Xtest))
```

This StackingClassifier will run a little longer than the VotingClassifier, because we use cross-validation in the training of the meta-model.

To show the advantages of bagging and random forest classifiers, let's first look at a simple decision tree classifier. 

``` python
tree = DecisionTreeClassifier()

tree.fit(Xtrain, Ytrain)
accuracy_score(Ytest, tree.predict(Xtest))
```

For this particular dataset, we get an accuracy of 0.8173330876481789. To improve upon this, we can use bagging. This could look like this:

``` python
from sklearn.ensemble import BaggingClassifier

for bootstrap_instances in [False, True]:
    for bootstrap_features in [False, True]:
        bagging = BaggingClassifier(DecisionTreeClassifier(), 
                                    n_estimators=10,     
	                                bootstrap=bootstrap_instances,      
	                                bootstrap_features=bootstrap_features, 
                                    random_state=0, n_jobs=-1)
        

        bagging.fit(Xtrain, Ytrain)

        acc = accuracy_score(Ytest, bagging.predict(Xtest))

# Output:
# Instance bootstrapping: False; feature bootstrapping: False; accuracy: 0.820 
# Instance bootstrapping: False; feature bootstrapping: True; accuracy: 0.846 
# Instance bootstrapping: True; feature bootstrapping: False; accuracy: 0.845 
# Instance bootstrapping: True; feature bootstrapping: True; accuracy: 0.850
```

Here we use the "normal" BaggingClassifier with and without bootstraping and feature bootstraping. We can see that in this case all of these options are superior to a single DecisionTreeClassifier and that they increase in performance with complexity.

The same can be done with a RandomForestClassifier.

``` python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=10, random_state=0, n_jobs=-1)

rf.fit(Xtrain, Ytrain)
accuracy_score(Ytest, rf.predict(Xtest))
```