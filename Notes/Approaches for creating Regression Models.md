In general, regression models are used for making predictions, but they can also be used for inference. In this case they serve a similar function like [[Hypothesis Testing|hypothesis testing]]. For more on inference and regression, look here: [[Inference and Regression]]
## Linear Regression
Linear regression is a bread-and-butter modeling technique that should serve as your baseline approach to building data-driven models for regression problems. These models are typically easy to build, straightforward to interpret, and often do quite well in practice. With enough skill and toil, more advanced machine learning techniques might yield better performance, but the possible payoff is often not worth the effort. Build your linear regression models first, then decide whether it is worth working harder to achieve better results. For some examples of creating simple regression models using Python look here: [[Regression in Python]]

When we fit a linear regression model, we get *coefficients* and an *intercept*. When we view the linear regression model as a linear function of form $y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_n X_n$ the coefficients correspond to $\beta_1 ... \beta_n$ and the intercept corresponds to $\beta_0$. The coefficients and the intercept can usually be directly accessed when fitting a linear regression model via attributes. 

Here are some common approaches to fitting linear regression models:
### Parameter Fitting
Parameter Fitting is not really an approach on its own but more of an overarching term for different ways to determine the parameters (coefficients and intercept) of a linear function to best describe some data. The distinction comes down to the **specific approach** and the **objective function** being optimized. 
#### Least Squares Regression
The least squares regression aims to minimize the sum of the squares of the residuals of all points. A **residual** or **residual error** is defined as the difference between the predicted value and the actual value. 

Minimizing this for a simple single variable $x$ with a function of the form $y= ax+b$ might be somewhat straightforward, but if we want to compute this for a multivariate function, we need to construct complex matrices, which makes this approach very inefficient for complex models. We can technically fit non-linear functions with least squares regression (shown in an example here: [[Regression in Python]]) but this makes the matrices very inefficient. We then speak of **Polynomial Regression**. Another problem with least squares regression is that it is sensitive to outliers.

The advantages of least squares regression are that it is relatively simple to implement and that it is computationally very efficient (for non-complex linear problems).
#### Gradient Descent Search
Because the loss function is a convex function (meaning it has a global minimum) we can find the minima of such a function simply by starting at an arbitrary point, and repeatedly walking in a downward direction. This is the idea behind gradient descent search. 

Gradient descent search is more flexible and scalable, making it suited for large, complex, high-dimensional, or nonlinear problems.
## Nearest Neighbor Regression
The nearest neighbor approach (discussed here: [[Approaches for creating Classification Models]]) can also be used for regression models. We assume that each point is associated with the continuous value of a function, instead of a discrete class label. Then we assign the query point with the same function value as the nearest neighbor (or the mean of the $k$ nearest neighbors)
## Decision Tree Regression
### Definition
The basic idea of decision trees is best explained like this. Let's say we have some input: $[x1 = 1, x2 = 2]$ and we want to predict $y$. We now start at the *root node* of the decision tree. Each node in the tree is associated with some rule and threshold based on the input data and learned from some training data. Depending on the outcome we go down one of the two branches (binary tree) connected to the root node. We continue and work our way down until we reach the end of a branch, called a *leaf node*. Each such final node corresponds to prediction for $y$.

There are two ways to represent a decision tree. First we have a simple tree representation like this shown below. In this case, this is a simple classification tree. The other representation is called a region partition, where each region corresponds to a leaf node in the tree. Each border between regions corresponds to a split in the tree. Each region is colored with the prediction corresponding to that region, and the boundary between red and blue is therefore the decision boundary. 
![[Pasted image 20250325100633.png|600]]
### Training Decision Trees
When training a decision tree we have two goals: 
- Determining the shape of the tree → How the data is split.
- Determining the prediction for each region → What value/class is assigned to each leaf node.

We also need to specify the tree size/depth. This is a hyperparameter in decision tree algorithms. Too small a depth might lead to underfitting, while to large a depth might lead to overfitting. 

For the decision tree regression, the prediction for each region is usually determined by averaging the training data points that fall into this specific region. To determine the shape of the tree we use *recursive binary splitting*. 

Recursive binary splitting works like this:
- At each node, the algorithm considers all possible features and split points. It evaluates which split results in the purest possible child nodes (i.e., most homogeneous groups). This can for example be done using MSE or MAE.
- The dataset is split into two child nodes based on the selected feature and threshold.
- The algorithm repeats steps 1 and 2 for each child node.
- This process continues until a stopping condition is met. This could be a maximum tree depth, node purity, ...
## Issues Specific in Modeling Regression Problems
### Sublinear Target Scaling
Scaling is common issue in data science ([[Data Transformation and Scaling]]), but when it comes to regression models, we need to specifically look at target scaling. 

We have two problems when it comes to target scaling. If we scaled our features with for example the z-scores, we would need very large coefficients to predict large targets. Here it makes sense to look for different presentations for the targets (for example a different unit).

But this only applies to normally distributed targets. Any linear combination of normally-distributed variables cannot effectively realize a power law-distributed target. The solution here is that trying to predict the logarithm of a power law target $y$ is usually better than predicting $y$ itself.
### **Dealing With Highly-Correlated and Unnecessary Features**
As previously discussed, the simplest solution is always the best. This also hold for regression models. The problem with taking every feature to fit our regression model is, that most of these features may be uncorrelated with the target and some might be perfectly-correlated. 

Why are perfectly-correlated features bad? For one, two perfectly-correlated features in your data matrix have no benefit, because if that were the case we could just copy a feature $n$ times and would create the perfect model. But more than that, they are even harmful. Because of the way regression models figure out the best fit, perfectly correlated features heavily impact performance and should be avoided. 

To combat this problem we can use [[Feature Selection]] and more specifically [[Regularization]].
