In mathematical modeling, **regression** is a statistical technique used to describe the relationship between one dependent variable (the outcome you want to predict or explain) and one or more independent variables (the inputs or predictors). The goal is to approximate a continuous mapping $f: \mathcal{X} \to \mathbb{R}$. Mathematically this means: learn $\hat{f}$ such that $\hat{f}(X) \approx Y$ and some loss $L(Y, \hat{f}(X))$ is minimized (e.g., mean squared error).

This key idea can be extended to more complex tasks:
- **Simple regression**: Models the relationship between one predictor $x$ and one outcome $y$. For example, linear regression assumes: $y \approx \beta_0 + \beta_1 x$
- **Multiple regression**: Extends this to several predictors $x_1, x_2, \ldots, x_p$: $y \approx \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p$. More on the benefits here: [Multiple Regression](Multiple%20Regression.md).
- **Nonlinear regression**: The relationship is not restricted to straight lines, e.g. exponential, logistic, or polynomial models.
## Time-Series Regression
Time-series regression predicts continuous-valued targets given temporal sequences as input. Unlike standard regression where observations are assumed independent, time-series data exhibits temporal structure: past values influence future values, and observations are ordered in time.

Given a time series $X = (x_1, x_2, \ldots, x_T) \in \mathbb{R}^{T \times D}$ where $T$ is the sequence length and $D$ is the number of features, we aim to predict a continuous target $Y \in \mathbb{R}^{M}$. The target can be either a single scalar value (predicting one time step ahead or an aggregate property of the sequence) or a vector of future values (multi-step forecasting).
### Approaches
**Autoregressive Models** use past values of the target variable to predict future values. A simple autoregressive model of order $p$ is: $\hat{y}_{t+1} = \beta_0 + \beta_1 y_t + \beta_2 y_{t-1} + \cdots + \beta_p y_{t-p+1} + \epsilon_t$. This approach assumes the recent history contains sufficient information for prediction and is interpretable but may struggle with long-range dependencies.

**Exogenous Variable Regression** incorporates external features alongside temporal patterns. A window-based approach extracts context from the time series: given features from windows $X_{[t-W:t]}$ of length $W$, predict a target $y_{t+h}$ at forecast horizon $h$. This can be modeled as standard regression with hand-crafted temporal features or learned automatically through neural networks.

**Multi-step Forecasting** extends single-step prediction to multiple future time steps. This can be formulated recursively (predict one step, feed back into the model) or directly (train a model to output multiple steps simultaneously). Direct approaches avoid error accumulation but require more training data.
