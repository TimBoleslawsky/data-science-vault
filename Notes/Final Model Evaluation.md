Final model evaluation happens ones all other evaluation of the model is done and a final model is trained. We want to see how well this model performs. How this can be done in Python is documented here: [[Final Model Evaluation in Python]]
## What Data Do We Use for the Evaluation?
The first rule of thumb is a model's performance needs to be evaluated on data that was never used to train the model. We call this the test set (in contrast to the training set). *Never ever evaluate the model on the training set!*
### Train-test Split
The idea behind the Train-test split is to divide our data so that we have a **training set** to develop and train our model, an optional **validation set** to help with parameter selection to optimize our model if needed, and a **test set** where we can run final tests. Usually, the split is 75/25 if we have two sets and 50/25/25 if we have three sets. 

**Cross-validation**
But what if we have very little data? Then we can use cross-validation to repeatedly partition our data into test data and training data and train/test on each of these iterations. One example, of how we can do this is **k-fold cross-validation**.

When using k-fold cross-validation, we divide the entire dataset into k approximately equal-sized folds. Each fold serves as a test set exactly once, while the remaining k-1 folds form the training set. Repeat this process k times, each time using a different fold as the test set. **Leave-One-Out Cross-Validation (LOOCV)** is a special case of k-fold where k equals the number of data points (i.e., each fold contains one data point).
## What Model Do We Use for the Evaluation?
The model we evaluate against is usually called a **baseline model**. A baseline model can be a dummy model  
- For classification, we can use a model that always predicts the most common label  
- If we have no idea what the most common label is, we can always guess at random 
- ... 

Other possibilities for a baseline include A simple or trivial model that we know how to build or somebody else’s model (a pre-existing model).
## What Do We Use for Evaluation?
We use **metrics** for evaluating models. A metric is a function or measure that defines a way to quantify the “distance” or difference between two elements in a set. A measure must meet some criteria to qualify as a metric:
- Non-negativity:  the distance between any two points is always non-negative.
- Identity of Indiscernibles: the distance is zero if the two elements are identical.
- Symmetry: the distance from x to y is the same as from y to x
- Triangle Inequality: the direct distance from x to z is always less than or equal to going through another point y.
## Evaluating Classification Models
The performance of a classification model can often be presented using a confusion matrix  
- True Positives (TP) are correctly identified positives  
- True Negatives (TN) are correctly identified negatives  
- False Positives (FP) are incorrectly identified positives  
- False Negatives (FN) are incorrectly identified negatives

**Metrics**
1. Accuracy measures the fraction of correct classifications out of all classifications. The worst accuracy in this case would be 0.5, so a coin toss. Formula = ${TP + TN} \over {TP+TN+FP+FN}$
	- Accuracy is useful when classes are balanced (i.e., both positive and negative classes are present in similar proportions). However, if one class is significantly more frequent than the other, accuracy can be misleading. For example, if 95% of emails are not spam, a model that always predicts “not spam” will be 95% accurate, but it’s not helpful in identifying spam.
2. Precision indicates how many of the model’s positive predictions are actually correct. Formula = ${TP} \over {TP+FP}$
	- Precision is important when false positives are costly.
3. Recall/ Sensitivity measures how many of the relevant items are retrieved. It measures the model’s ability to capture all actual positive cases. Formula = ${TP} \over {TP+FN}$
	- Recall is useful when false negatives are costly.
4. Specificity measures how likely we are to pick up a negative result. It indicates how well the model identifies instances of the negative class. Formula = ${TN} \over {TN+FP}$
5. F-score combines precision and recall into a single score. Formula = $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$

**Receiver-Operator Characteristic (ROC)**
The **Receiver-Operator Characteristic (ROC)** plots the recall (or *True Positive Rate*) vs. False Positive Rate, which is 1 - Specificity (or *True Negative Rate*) depending on the given threshold. By examining the ROC we can determine that we have some influence over the precision and the recall, depending on what threshold we use.
The behavior of the classifier is often characterized by the Area Under Curve (AUC), the perfect classifier would have area 1, tossing a coin would have area 0.5.
![File:Roc curve.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Roc_curve.svg/512px-Roc_curve.svg.png?20210909040029)

**Hypothesis Testing as a Tool to evaluate Classification Models**
Hypothesis testing, as discussed here: [[Inference]], provides a framework for understanding whether the observed performance differences are due to the *models’ real capabilities* or due to *random chance*. It helps you assess whether the observed improvements in evaluation metrics are statistically significant or not.
## Evaluating Regression Models
The main problem for evaluating regression models is that we don't have a one size fits all solution. But we have some good candidates. Suppose ($x$ is the predicted value and 𝑦 is the correct value.

**Metrics:**
- Plain difference $x$ − 𝑦 is simple but signed, so it is inappropriate if the signedness is not significant  
- Absolute error |$x$ − 𝑦| is a simple statistic, but is sensitive to, e.g., variations in scale  
- Relative error |${x-y} \over {y}$| can be used even in the presence of variable scales (or missing information of scale), but behaves erratically near 0  
- Squared error ($x$ − 𝑦)$^2$ is always positive and penalizes large deviations more

Another way of looking at it. If we don't want to evaluate the errors but how well your model explains the variance we can use the coefficient of determination $R^2$. This metric is evaluating the model’s ability to capture the relevant relationships in the data. Therefor if we have bad data, this metric will also be bad. The $R^2$ metric can be interpreted as follows: If our model has an **R-squared (R²) value of 0.8 (or 80%)**, this means 80% of the variation in output variables can be explained by the input variables and our model.
## Evaluating Clustering Models
A popular way of doing this, is the ***Silhouette score***. The idea is that a good clustering should have compact clusters with a large separation between different clusters. This is characterized by the within-cluster distance and between-cluster distance. When calculating the Silhouette score, we get a graph that looks like this: 

![[Pasted image 20241205143119.png]]

What we seek from the Silhouette score graph, is the highest point. 

The **Purity score** measures how well each cluster contains only members of a single ground-truth class. Here is a step-by-step instruction of how to compute the purity score:
- For each cluster, find the most frequent true label (the majority class in that cluster).
- Count how many points in the cluster belong to that majority class.
- Sum this count over all clusters.
- Divide by the total number of points $N$.
=> This is very easily interpretable but requires some ground truth labels!