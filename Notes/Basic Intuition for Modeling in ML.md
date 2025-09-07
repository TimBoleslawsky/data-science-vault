In machine learning, **mathematical modeling** is about creating a **function** that maps inputs $x$ to outputs $y$. The goal is to **learn this function from data**.
- **Classification:** The output y is categorical (e.g., spam/not spam).
- **Regression:** The output y is continuous (e.g., predicting house prices).

In the case of classification, the model separates the plane using a decision boundary. Example: For two features $x_1$ and $x_2$, a linear model might give a line: $w_1 x_1 + w_2 x_2 + b = 0$. While this does not look like a typical line in 2D space (it can be written as such: $x_2 = -\frac{w_1}{w_2} x_1 - \frac{b}{w_2}$) it defines the constrains of points that dissect the plane to create a decision boundary.

In regression, instead of a boundary, we’re interested in the **curve or surface** that fits the data. Example: Linear regression fits a line: $y = w_1 x_1 + w_2 x_2 + b$.

An important point here is *linearity*. In machine learning, when we say a model is **linear** or **non-linear**, we’re talking about the shape of the **decision boundary** (or, more generally, the mapping from inputs → outputs).
- A **linear function** in two variables looks like this: $f(x_1, x_2) = w_1 x_1 + w_2 x_2 + b$.
	Its decision boundary (where $f(x_1, x_2) = 0)$ is always a **straight line (or hyperplane)**.
- A **non-linear function** means the relationship between input and output cannot be expressed as just a weighted sum. Its decision boundary can be **curved, complex, and flexible**.
=> This means that even though the sigmoid function is a non-linear function, if you apply it to only the outputs of a model, this model's decision boundary stays linear:
- $p(y=1|x_1,x_2) = \sigma(w_1 x_1 + w_2 x_2 + b)$, has a decision boundary at $p(y=1|x_1,x_2) = 0.5$. Since $\sigma(z)=0.5$ when $z=0$, the boundary is: $w_1 x_1 + w_2 x_2 + b = 0$, which is linear. 
This is the reason, why "normal" machine learning models struggle to capture non-linear problems!
## Philosophies of Modeling
There is a trade-off between model accuracy and complexity. Adding parameters can improve performance but at the cost of increased complexity, which may not always be justified. While simplicity is desired, it should not compromise model performance. A model should be as simple as possible while still being effective.

1. We want to minimize the number of parameters in a model to avoid **overfitting**. Overfitting occurs when a model is too complex, capturing noise and outliers in the training data rather than generalizing well to new data. Data-driven models are more prone to this. Overfitted models perform well on training data but poorly on independent test data.
2. Bias is the error from incorrect assumptions built into the model. These models perform lousy on both training and testing data and are called underfit. They fail to capture the phenomena in question.