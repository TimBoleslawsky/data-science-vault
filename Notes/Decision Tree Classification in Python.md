First we need to load our data, define the classifier and fit the classifier using the training data:

``` python
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.tree import DecisionTreeClassifier, plot_tree

iris = load_iris()

X = iris.data[:, :2]  # Using only the first two features (sepal length and sepal width)
y = iris.target

# Train a DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)
```

Now we can view the classifier in two ways. First we can look at the tree structure:

``` python
# Plot the trained decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names,
          filled=True, rounded=True, precision=2, label='root', impurity=False)
plt.show()
```

This will give us something like this: 
![[Pasted image 20250325113027.png|500]]

Second, we can look at the decision regions:

``` python 
plot_decision_regions(X=X, y=y, clf=clf, legend=2)

# Labeling the axes and title
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Decision Tree Decision Regions')
plt.show()
```

This will give us something like this:
![[Pasted image 20250325113138.png|500]]