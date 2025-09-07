---

### **🔑** 

### **Regularization = A way to prevent a model from overfitting by keeping it “simple.”**

---
When a model learns too much from the training data — including noise and random fluctuations — it **overfits**, regularization helps by:
- **Penalizing** the model for being **too complex** (like using too many features or assigning them huge weights).
- Forcing the model to focus only on the most important patterns.

Regularization is not a separate step in the data science process or separate model all together, it’s a **modification of existing models** to make them generalize better. We use it by applying regularized versions of common models, or by adding regularization terms when training.
## How Does it Work?
During training, a model usually tries to minimize some loss function (like prediction error). Regularization **adds a penalty** to that loss based on how “complicated” the model is. So now the model tries to minimize something like this $Loss = Prediction Error + Penalty for Complexity$.

By adjusting the objective function in such a way we prevent the coefficients to become to large which reduces the impact of highly-correlated features and shrinks the coefficient of unnecessary features towards zero. 

Important: Some regression methods like ridge regression do not set coefficients exactly to zero, meaning it does not perform automatic feature selection!
## What Methods Are Used?
**Methods for Regression**
Two common methods for regularization exists for regression models. 
- L1 Regularization (Lasso):
	- Adds a penalty based on the **absolute values** of the weights.
	- Can shrink some weights to **exactly zero** ⇒ acts like **feature selection**.
2. L2 Regularization (Ridge)
	- Adds a penalty based on the **squared values** of the weights.
	- Shrinks weights but usually doesn’t make them exactly zero ⇒ **smooths** the model.
=> We can also combine these two methods using *Elastic Net regression*!

**Methods for Classification**
Here we can for example do **Logistic Regression (with regularization)**. The logistic regressor common in for example sklearn has a parameter that lets us set the penalty to either L1 or L2.

Also common are Tree-based models. While not using L1/L2 regularization, decision trees, random forests, and gradient boosting models are regularized by controlling complexity through limiting max depth, setting min samples per split, or using early stopping in boosting.
## Implicit Regularization
Implicit regularization refers to any effect during training that reduces overfitting or improves generalization, without explicitly adding a penalty term to the loss function (like L1 or L2 regularization). It’s “regularization” in effect, not in form. Here are a few example methods that would be categorized as implicit regularization:
- **Data Augmentation**: Exposes the model to more data variation, which prevents overfitting and forces the model to be less sensitive to small perturbations. One example would be *noising*, where we add small noise to inputs or hidden layers during training.
- **Early Stopping**: Prevents the model from overfitting to training data by stopping before full convergence. The condition of when to stop can be flexible. 
- **Dropout**: Randomly turn off neurons during training (set their output to zero). This forces the network to learn redundant, more robust representations.
- [[Optimization and Gradient Descent#Stochastic Gradient Descent|Stochastic Gradient Descent]]
- **Batch Normalization**: Is a [[Data Transformation and Scaling#Normalization|normalization]] technique that normalizes the activations (outputs) of each layer within a mini-batch to have zero mean and unit variance, helping stabilize and speed up training. This means that one, this can only properly be done with mini-batch gradient descent and two, this is usually placed after linear or convolutional layers, and before the activation function (like ReLU).

