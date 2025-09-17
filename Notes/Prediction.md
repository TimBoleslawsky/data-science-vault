Just like I did with inference here ([[Inference]]), I want to first look at the basic intuitions behind prediction and how it connects to the statistical modeling approach. 

Also just like in inference, the basis of prediction are the mathematical model and parameter estimation steps outlined here ([[Basics of Probability and Statistics for Data Science#Connecting Probability and Statistics to Modeling]]).
## Bayesian Prediction
In this example I describe the basic intuitions behind Bayesian prediction and how it connects to the statistical modeling approach (an example of how this is done in R can be found here: [[bayesian_regression.rs]]).

- First, model definition. Let’s say we want to predict the body mass of new Gentoo penguins given their flipper length. Our target variable $y$ is body mass, and our feature is $x$ (flipper length). Our model could look like this: $y = \alpha + \beta x$.	
- Second, define random variables and distributions. In Bayesian modeling, _all unknown quantities_ (parameters as well as observations) are treated as random variables. That means we always assign distributions:
	- Likelihood: $y_i \sim \text{Normal}(\mu_i, \sigma^2)$
	- Priors: $\alpha \sim \text{Normal}(0,10), \beta \sim \text{Normal}(0,1), \sigma \sim \text{Exponential}(1)$ (for example).
	  => Together with the deterministic function: $\mu_i = \alpha + \beta x_i$, this makes us our complete model.
- Third, parameter estimation. In Bayesian analysis, parameter estimation means computing the [[Likelihood and Posterior Distributions|posterior distribution]] of the parameters: $p(\alpha, \beta, \sigma \mid y) \propto p(y \mid \alpha, \beta, \sigma) \, p(\alpha, \beta, \sigma)$. This posterior summarizes what we know about the parameters after seeing the data.
- Fourth, prediction. With the posterior in hand, prediction means generating the posterior predictive distribution for a new data point, see here [[Likelihood and Posterior Distributions#Posterior Predictive Distribution]]. Now the prediction is a full distribution that integrates both parameter uncertainty (from the posterior) and observation uncertainty (from the likelihood).
	- Point prediction: Often the posterior mean or median of $y_{\text{new}}$.
	- Uncertainty quantification: Credible intervals (e.g., 89% or 95%) that summarize the posterior predictive distribution.
## Frequentist Prediction
In this example I describe the basic intuitions behind frequentist prediction and how it connects to the statistical modeling approach. 

- First, model definition. Let’s say we want to predict the body mass of new Gentoo penguins given their flipper length. Our target variable $y$ is body mass, and our feature is $x$ (flipper length). Our model could look like this: $y = α + βx$.
- Second (optional), define random variables and distributions: If we want to model some uncertainty, we define random variables and assign a distribution. That means we have either: 
	- Deterministic model: $\mu_i = \alpha + \beta x_i$
	- Stochastic distribution: $\mu_i = \alpha + \beta x_i$ + $y_i \sim \text{Normal}(\mu_i, \sigma^2)$, assuming that $y$ is a random variable and normally distributed. 
- Third, parameter estimation. Use a parameter estimation method for the type of model 
  ([[Parameter Estimation for Deterministic Models|deterministic]] or [[Parameter Estimation for Probabilistic Models|probabilistic]]) estimate parameters.
- Fourth, prediction. If we have the model at this stage, prediction becomes very easy. All that is left to do is to plug in a new data point into the fitted function and observe the target variable: $\hat{y}_{\text{new}} = \hat{α} + \hat{β}x_{\text{new}}$. Now depending on if we have a deterministic or a probabilistic model, the prediction will look differently:
	- Deterministic model: Prediction is a single point. Once we plug in $x_{\text{new}}$, we get exactly $\hat{y}_{\text{new}} = \hat{\alpha} + \hat{\beta} x{_\text{new}}$.
	  There’s no quantified uncertainty. You can still talk about “error” after the fact (residuals, RMSE, etc.), but the model itself doesn’t generate uncertainty.
	- Probabilistic model: Prediction is a distribution, not just a point. When plugging in  $x_{\text{new}}$, we get both the expected mean: $\mu_{\text{new}} = \hat{\alpha} + \hat{\beta} x_{\text{new}}$, and the uncertainty around it: $y_{\text{new}} \sim \text{Normal}(\mu_{\text{new}}, \hat{\sigma}^2)$.
## Prediction and Machine Learning
The workflow described above raises the question: *"Where does machine learning come in?"*. Machine learning is our primary way of doing predictions as data scientist, so how does it connect to the workflow above?

At its very core, machine learning algorithms **are parameter estimation procedures embedded in a predictive framework**.

If you strip away the layers of jargon, a minimal machine learning "model" is:
1. **Model setup**: Define a functional form (linear regression, logistic regression, a tree, a small neural net).
2. **Parameter estimation**: Fit the model to training data by optimizing some criterion (likelihood, loss function, error rate). This is the _machine learning part_.
3. **Prediction**: Take new feature values, plug them into the fitted function, and output the predicted target.

More on machine learning and AI, here: [[Data Science#Data Science, Machine Learning and AI]].