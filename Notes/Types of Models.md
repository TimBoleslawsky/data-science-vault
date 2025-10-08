## Linear vs. Non-linear Models
Linear models are models where the input and output of the model have a linear relation. This does not necessarily mean that the underlying problem has to be linear.
Pros: Linear models are often interpretable, efficient to compute, and traceable.
Cons: A lot of problems can not be modeled as linear problems.

When we say a model is **linear** or **non-linear**, we’re talking about the shape of the **decision boundary** (or, more generally, the mapping from inputs → outputs).
- A **linear function** in two variables looks like this: $f(x_1, x_2) = w_1 x_1 + w_2 x_2 + b$.
	Its decision boundary (where $f(x_1, x_2) = 0)$ is always a **straight line (or hyperplane)**.
- A **non-linear function** means the relationship between input and output cannot be expressed as just a weighted sum. Its decision boundary can be **curved, complex, and flexible**.
=> This means that even though the sigmoid function is a non-linear function, if you apply it to only the outputs of a model, this model's decision boundary stays linear:
- $p(y=1|x_1,x_2) = \sigma(w_1 x_1 + w_2 x_2 + b)$, has a decision boundary at $p(y=1|x_1,x_2) = 0.5$. Since $\sigma(z)=0.5$ when $z=0$, the boundary is: $w_1 x_1 + w_2 x_2 + b = 0$, which is linear. 
This is the reason, why "normal" machine learning models struggle to capture non-linear problems!

More on linear models here: [[The Hierarchy of Linear Models]].
## Black Box vs. Descriptive Models
A model is a black box if we can observe that the outputs have predictive power, but we cannot explain why the outputs are what they are. Artificial neural networks are black box models, we understand that they are working, but we don't understand why.
## First-principle vs. Data-driven Models
**First-principle models** are based on theoretical understanding of the phenomena in question. **Data-driven models** are based purely on observation of the data. 
## Probabilistic vs. Deterministic Models
**Probabilistic models** purposefully include some kind of random component. We do this because we want to better mimic the real world, which, by definition, is a random place. Instead of a single prediction, they provide probabilities or confidence intervals for possible outcomes.

**Deterministic models** provide a fixed output for a given input. The outcomes are fully determined by the inputs and the model structure. First-principle models often yield only one possible answer. Newton’s laws of motion will tell you exactly how long a mass takes to fall a given distance.
### Parameter Estimation
A really really important part of mathematical modeling is parameter estimation ([[Data Science#The Goals of Data Science]]). Because they are inherently different for probabilistic and deterministic models I want to shine a light on both:
- **Probabilistic models**: Almost always estimated via MLE, MAP, or Bayesian inference (all optimization under the hood) ([[Parameter Estimation for Probabilistic Models]]).
- **Deterministic models**: Almost always estimated via direct optimization of some loss, without reference to a likelihood ([[Parameter Estimation for Deterministic Models]]).
## Flat vs. Hierarchical Models
A **flat model** is one where there is only one problem that is being solved, without subproblems with a parent-child relationship. A **hierarchical model** would be the opposite, for example, hierarchical clustering. More on hierarchical models, here: [[The Hierarchy of Linear Models]].
## Inference Framework
**Frequentist models**: Parameters are fixed but unknown; uncertainty comes from imaginary repeated sampling; probability describes long-run frequencies of data.
**Bayesian models**: Parameters are treated as random variables with probability distributions; uncertainty reflects incomplete information; probability is a measure of plausibility.
=> More on this difference here: [[Two Approaches to Statistics]].
