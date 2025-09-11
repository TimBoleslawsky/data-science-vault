For deterministic models we do not divide between frequentist and Bayesian because there is no assumption that the data comes from a probability distribution. The goal is purely to find parameter values of a model (function) that minimize some **loss function** measuring the discrepancy between predictions and observed data (in essence this is purely an [[Optimization Problems|optimization problem]]).

Here is how that works:
1. Define a **model function** $f_\theta(x)$ with parameters $\theta$.
2. Choose a **loss function** $L(y, f_\theta(x))$ that measures prediction error.
3. Form the **empirical risk** (average loss across training data):
	$R(\theta) = \frac{1}{n} \sum_{i=1}^n L(y_i, f_\theta(x_i))$
4. Solve an **optimization problem**:
	$\hat{\theta} = \arg \min_\theta R(\theta)$
5. Use optimization techniques (gradient descent, greedy splits, quadratic programming, etc.) to find $\hat{\theta}$.

There a lot of models that work this way. Linear regression for example works by minimizing squared error, decision trees work by minimizing for example impurity, and simple neural networks minimize some loss with gradient descent. 
## How Deterministic Methods Connect to Probabilistic Methods
Suppose we have 3 data points: 

| **Height** x | **Weight** y |
| ------------ | ------------ |
| 160          | 55           |
| 170          | 65           |
| 180          | 75           |

We want a line $y = \beta_0 + \beta_1 x$.

**Step 1: Deterministic Estimation (least squares)**
- We minimize squared errors:
	$\text{SSE} = \sum_i (y_i - (\beta_0 + \beta_1 x_i))^2$
- From simple calculations (or “eyeballing”), the line that fits perfectly here is:
	$\beta_1 = 1, \quad \beta_0 = -105$
	
=> So deterministic prediction: $\hat{y} = -105 + 1 \cdot x$
- Example: For $x = 175$, predicted weight:
	$\hat{y} = -105 + 175 = 70$

**Step 2: Probabilistic view (MLE under Gaussian noise)**
- Assume **random noise** in weights:
	$y_i = \beta_0 + \beta_1 x_i + \epsilon_i, \quad \epsilon_i \sim \mathcal{N}(0, \sigma^2)$
- **Likelihood function:** Probability of observing the weights given $\beta_0, \beta_1$:
	$L(\beta_0, \beta_1) = \prod_{i=1}^3 \frac{1}{\sqrt{2\pi\sigma^2}} \exp\Big[-\frac{(y_i - (\beta_0 + \beta_1 x_i))^2}{2\sigma^2}\Big]$
- **Log-likelihood** (simpler to work with):
	$\ell(\beta_0, \beta_1) = -\frac{1}{2\sigma^2} \sum_{i=1}^3 (y_i - (\beta_0 + \beta_1 x_i))^2 + \text{constants}$
 
 => maximizing this log-likelihood **is exactly the same as minimizing squared errors**! The line that “makes the observed data most likely” under Gaussian noise is the same line that minimizes squared distance from points.

**Why would we want to do this?** => **Uncertainty in parameters**
- The slope $\beta_1 = 1$ and intercept $\beta_0 = -105$ are now **random variables**:
	$\hat{\beta}_1 \sim \mathcal{N}(\beta_1, \sigma^2 / \text{Var}(x)), \quad \hat{\beta}_0 \sim \mathcal{N}(\beta_0, \sigma^2 \cdot \text{some factor})$
- You can compute **confidence intervals**, e.g., slope might be $1 \pm 0.1$.
- New height $x_*=175$: prediction is $70$ (deterministic).
- Probabilistic view: account for noise in data → range of plausible weights, e.g., $70 \pm 5$.

