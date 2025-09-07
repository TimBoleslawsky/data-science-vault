## Decision Tree Classification
The basic idea of decision trees is described in the regression model note: [[Approaches for creating Regression Models#Definition]].

Recursive binary splitting, the main method to train decision trees, is also described in the link above. But when talking about decision tree classification, we have some differences compared to the way we train regression decision trees. 

Firstly, we use a majority vote instead of an average to compute the prediction associated with each region.

Secondly, we need a different splitting criterion than the squared prediction error to take into account the fact that the output is categorical. For this there exist a few different options:
- Misclassification Rate: The proportion of incorrectly classified samples.
- Entropy (Information Gain): Measures the impurity of a node based on class probabilities.
- Gini Index: Measures the probability of incorrect classification if a random sample is chosen.

Here is an example in Python how a decision tree classifier can be trained and visualized: [[Decision Tree Classification in Python]].
## Linear Classifiers
When we say a regressor or a classifier is linear, we mean that the output is a linear function of the input features. A linear classifier predicts discrete classes based on whether the linear combination of features crosses a certain threshold. We can think of this process as finding the decision boundary in a hyperplane in feature space.

The main difference between different linear classifiers lies in their loss functions and optimization objectives, even though they all learn a linear decision boundary of the form $\mathbf{w}^\top \mathbf{x} + b$.

Below the linear classifier "logistic regression" is explained in detail. Because in practice all linear classifiers work relatively similarly, I will only explain one. Another very popular linear classifier is the **Support Vector Classifier (SVC)**. In practice we want to use logistic regression if we want probabilities or interpretability and use SVC if we care more about classification accuracy and margin-based generalization.

Linear classifiers can become inefficient when using high-dimensional, noisy, or text-based data. We can help this by using *sparse* classifiers that aim to reduce many weights to zero and therefore having fewer active features. In practice we achieve this using [[Regularization|L1 regularization]]. Most popular linear classifiers in scikit-learn support this (via 'l1' penalty).
### Logistic Regression
Unfortunately, we can not just simply use linear regression for classification problems. Imagine we add a number of “very negative” examples to the training data. The regression line will tilt towards these examples, putting the correct classification of more marginal examples at risk.
Unlike [[Approaches for creating Regression Models#Linear Regression|linear regression]], which is used to predict a continuous value (like house prices), logistic regression predicts the **probability** that a given input belongs to a particular class. To do this, it uses the **logistic function (sigmoid function)** to ensure that the output is always a probability between 0 and 1.

Logistic regression starts by calculating a linear combination of the input features. This is similar to linear regression and looks like this $f(x) = w_0 + w_1x$. Now we use the sigmoid function to convert this linear output into a probability between 0 and 1. The sigmoid function looks like this 
$g(x) = \frac{1}{1 + e^{-f(x)}}$. 

For example, let's say our linear combination looks like this $f(x) = -4+1x$ for predicting if students pass or fail based on the hours of study. Then our sigmoid function would look like this $g(x) = \frac{1}{1 + e^{-(-4+1x)}}$. Now we want to predict if a student that studied 3 hours likely passes or fails. Our $f(3) = -1$ and our $g(3) = 0.27$. This means the model predicts that the student who studied 3 hours has about a **27% chance of passing**. Since 27% is less than 0.5, we predict that the student will **fail** (classification = 0).

![[Pasted image 20241008085552.png|400]]

**Model Definition of Form $y = g(x;θ | h)$**
Left-hand side:
- $y$: categorical (binary or multinomial) - each category is a class label.
Right-hand side:
- $x$: typically continuous numerical, can also include categorical features (preprocessed).
- $g$: Logistic function (sigmoid for binary, softmax for multinomial).
- $h$: regularization hyperparameters (e.g., L1 or L2 regularization strength).
- $\theta$: learned weights and biases for the features.

**Training the model**
The only remaining question is how to fit the coefficient vector $w$ to the training data. We construct a loss function that covers two possibilities: false positives and false negatives. If we denote positive as $1$ and negative as $0$ we want a function that:
- for false positive is $0$ when $f(x) = 1$ and gets exponentially higher when nearing $0$. This function is $-log(f(x))$.
- for false negative is exactly the opposite. This function is $f(x) = −log(f(x)$.

If we combine these two functions for all $f(x)$ we get: $J(w) = - { 1 \over n} [ ∑ y_i log f (xi, w) + (1 − yi) log(1 − f (xi, w))]$ 

Because this function is convex, we can find the parameters $w$, which best fit the training examples, using gradient descent.
## Nearest Neighbor Classification
The idea behind the nearest neighbor classification is very simple. We have an arbitrary amount of points on a feature space. When we want to determine the class of a new point, or *query point,* we just look which point is the closest to the new point and assume the new point has the same class as the nearest point. Which distance function (discussed here: [[Distances]]) is used, is up to the programmer. 

**Advantages**:  
- Simplicity: Easy to understand.  
- Interpretability: It is immediately clear why we get the answers we get.
- Non-linearity: Classification boundaries need not be linear.
**Disadvantages**:  
- Space cost: We need to potentially store the entire dataset.
- Running time: With the curse of dimensionality, running times of queries in high-dimensional spaces become linear.
- Sensitivity to outliers: An outlier can become a nuisance as it may attract a large number of query points and distort the output.

The simplest way to implement NN is the **linear scan**. Simply compute the distance from the query point to every element in the training set, and pick the minimum. In high dimensions, this is hard to beat because the number of ways that two points can be close to each other increases rapidly with the dimensionality. In low dimensions, **space-partitioning methods** are useful. An example of a space-partitioning method would be the K-d tree.

**Model Definition of Form $y = g(x;θ | h)$**
Left-hand side:
- $y$: categorical (nominal) - each category is a class label.
Right-hand side:
- $x$: typically continuous numerical or categorical (distance metric must support the data type).
- $g$: Nearest Neighbor decision rule based on the distance metric (e.g., Euclidean, Manhattan).
- $h$: number of neighbors  k  and the distance metric.
- $\theta$: training data points (feature vectors and their corresponding labels).
## $k$ Nearest Neighbor Classification
The robustness of nearest neighbor classification can be increased by taking into account not just the one nearest neighbor but $k$ nearest neighbors. The class label is then set to match that of the majority. In binary classification (classification into exactly two classes), using an odd $k$ means there will be no ties. 

**How to choose $k$?**
Increasing $k$ tends to produce larger regions with smoother boundaries, representing more robust decisions. However, the larger we make $k$, the more generic our decisions are with $k=n$ being just a majority classifier. So too large $k$'s lead to underfitting and too low $k$'s lead to overfitting. 
## Naïve Bayes Classification
The idea behind Naïve Bayes classification is really simple. We have two steps. 
In the training phase, Naïve Bayes calculates the probabilities. The *prior probability* for each class is typically the proportion of the training data that belongs to that class. The *likelihood* for each feature, which is the likelihood of the feature given the class.
In the prediction phase, we classify a new data point by calculating the posterior probability (maximum a posteriori estimation of the label) for each class using the Bayes theorem and assigning the class with the highest posterior probability. For more information about posterior probability and maximum a posteriori estimation, look here: [[Parameter Estimation for Probabilistic Models]].

This means that for each variation of the Naïve Bayes classifier, we start with something like this: $P(C_k | X) \propto P(C_k) \cdot P(X | C_k)$. For each variation of the Naïve Bayes classifier the assumption we make for the distribution of the underlying data changes. This means that the way we calculate the likelihood differs. The way we calculate the prior is the same across all variations ($P(C_k) = \frac{\text{Number of samples in class } C_k}{\text{Total number of samples}}$). More on the variations here: ([[Approaches for creating Classification Models#Variations of Naïve Bayes Classification]])

The “naïve” part of Naïve Bayes refers to the assumption that all features (predictors) are conditionally independent given the class label. This independence assumption simplifies the computation significantly. Even though it’s often unrealistic (features are usually not completely independent), Naïve Bayes still works well in practice.

**Model Definition of Form $y = g(x;θ | h)$**
Left-hand side:
- $y$: categorical (nominal) - each category is a class label.
Right-hand side:
- $x$: features, typically continuous or categorical (depending on the type of Naive Bayes, e.g., Gaussian, Bernoulli, Multinomial).
- $g$: Naive Bayes decision rule using Bayes’ theorem.
- $h$: feature independence assumption.
- $\theta$: probabilities $P(y)$ and $P(x_i \mid y)$ estimated from the training data.
### Zero-values and Laplace Smoothing
If one of the values in some of the features is not observed for some class in the training  
set, the estimated value $𝑃(𝑋|𝐶) = 0$, which means that the posterior probability becomes  
necessarily zero This might not be what we wanted: some values (e.g., some words) might be exceedingly rare but still occur in practice (although rarely). 

We can deal with this by **Laplace smoothing** also called **discounting**. The idea is that we adjust counts for yet-unseen events, by explicitly leaving probability mass available for them. We do this by choosing a parameter $𝛼 > 0$ and adding 𝛼 imaginary observations of each value. 𝛼 is then a hyperparameter of this classifier. 
### Variations of Naïve Bayes Classification
1. Multinomial Naïve Bayes is commonly used for discrete data, especially for document classification or text data where the features represent word counts or frequencies. Assumes that the features follow a multinomial distribution, which is appropriate when the features represent categorical data (e.g., word occurrences). This classifier is ideal for **bag-of-words** models.
   - Formula for the likelihood:  $\prod_{i=1}^k P(word_i | class)^{x_i}$, which is just the number of times a word occurs in the class divided by total words in the class. This is multiplied for each word (or summed in case of log likelihood).
   
2. Bernoulli Naïve Bayes is similar to Multinomial Naïve Bayes but used for binary features, where the features represent whether a word (or event) occurs or not (1 or 0). Instead of word counts, this model considers whether a word is present or absent in a document.
   - Formula for the likelihood: $P(x_i = 1 | y) = \frac{\text{Count of documents in class } y \text{ containing word } i}{\text{Total number of documents in class } y}$ the product of this is the likelihood. 

3. Gaussian Naïve Bayes is particularly useful for tasks where you need to classify continuous features that are assumed to have a bell-shaped distribution, making it suitable for problems where the data can be modeled using continuous, normally distributed features. We for example use it in text or image classification.
   - Formula for the likelihood: likelihood function of the gaussian distribution, more [[Parameter Estimation for Probabilistic Models#Maximum Likelihood Estimation (MLE)|here]].
## Issues Specific in Modeling Classification Problems
**Balanced training classes**
In a lot of real word classification problems, there exists an unbalance in training classes. For example, if we want to classify terrorists, there are way more non-terrorists than terrorists. If we fit our classifier with an unbalanced data set, we will likely miss all of the terrorists because their contribution to the loss function is so minimal. It is generally best to use equal numbers of positive and negative examples. We could use a workaround like replicating some of the scarce data or weighing the rare training examples by adding coefficients, but in each case, we bias the classifier, which can lead to problems. More on handling imbalanced classes here: [[Handling Imbalanced Classes]].

**Multi-class Classification**
It is also no rarity that we need to classify between more then two classes. This is a problem for most classifiers. A workaround is to build many one-vs.-all classifiers.