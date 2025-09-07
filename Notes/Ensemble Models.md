Before we go into the techniques how to create ensemble models, we need to talk about **Voting**, **Averaging**, and **Stacking**. All of these are common strategies used to aggregate predictions from multiple models.
- Voting, is used for classification models. We have **hard voting**, where each model makes a prediction and the class that gets the most vote is selected as the final prediction. And we have **soft voting**, where each model outputs class probabilities instead of discrete labels. The class with the highest average probability across all models is chosen.
- Averaging, is like voting but for regression models. Multiple models predict a numeric value. The final prediction is the mean (or weighted mean) of all predictions.
- Stacking, is a more advanced ensemble method that learns how to combine multiple models using a meta-model. We have *base-models* (strong and diverse models) that are trained on the same dataset. And then we have a *meta-model*, which takes the predictions of the base-models as input features and learns how to best combine the base models outputs to make a final prediction.

There are more advanced ways of creating ensemble models (described below), but we can just simply train multiple models and use one of the strategies above to create an ensemble model. When using Voting Classifiers, Averaging Classifiers, or Stacking Classifiers, all base models are typically trained on the same dataset.

Here is an example in Python: [[Ensemble Models in Python]].
## Bagging
Bagging is a technique used to reduce variance by training multiple models independently on different subsets of the training data created by **bootstrap sampling**. This is combined with either voting (classification) or averaging (regression). 

Bootstrap sampling works like this: Given an original dataset with $N$ samples, we generate new datasets of the same size $N$ by randomly drawing samples with replacement. Since we sample with replacement, some samples may appear multiple times, while others may not appear at all in a given bootstrap dataset. The new datasets are then used to train multiple models in an ensemble. 
### Random Forest
Random forest classifiers introduce additional randomness by selecting a **random subset of features** at each node split. This ensures that different trees focus on different aspects of the data, further increasing diversity.

This is done because decision trees are highly sensitive to small changes in data (high variance). By selecting a random subset of features at each split, Random Forest reduces correlation between trees and improves generalization. (=> Random forest is only used for decision trees!)

It is important to note that the BaggingClassifier also has the option to use feature bootstraping. But when used with the BaggingClassifier, the random subset of features is chosen **once per model**, while the RandomForestClassifier chooses the subset of features **at each split**. 
## Boosting
Boosting is an ensemble technique that builds models sequentially. Each new model focuses on correcting the errors made by the previous models. The final prediction is a weighted combination of all models. Popular boosting algorithms like AdaBoost use simple decision trees as models that iteratively improve their weights based on the error of the previous tree. 
### Gradient Boosting
Gradient Boosting is a specific boosting method of boosting. Its sort of a refinement of boosting, where new models are trained to fit the negative gradient of the loss function (i.e., to minimize the loss). It generalizes boosting to a wide range of loss functions, not just classification errors.