## Linear vs. Non-linear Models
Linear models are models where the input and output of the model have a linear relation. This does not necessarily mean that the underlying problem has to be linear.
Pros: Linear models are often interpretable, efficient to compute, and traceable.
Cons: A lot of problems can not be modeled as linear problems.
## Black Box vs. Descriptive Models
A model is a black box if we can observe that the outputs have predictive power, but we cannot explain why the outputs are what they are. Artificial neural networks are black box models, we understand that they are working, but we don't understand why.
## First-principle vs. Data-driven Models
**First-principle models** are based on theoretical understanding of the phenomena in question. **Data-driven models** are based purely on observation of the data. 
## Probabilistic vs. Deterministic Models
**Probabilistic models** purposefully include some kind of random component. We do this because we want to better mimic the real world, which, by definition, is a random place. Instead of a single prediction, they provide probabilities or confidence intervals for possible outcomes.

An important part of probabilistic models is that they assume an underlying probability distribution. Therefore it is sometimes necessary to estimate the parameters of said probability distribution. Here are some methods that do this: [[Parameter Estimation for Probabilistic Models]]

**Deterministic models** provide a fixed output for a given input. The outcomes are fully determined by the inputs and the model structure. First-principle models often yield only one possible answer. Newton’s laws of motion will tell you exactly how long a mass takes to fall a given distance.
## Flat vs. Hierarchical Models
A **flat model** is one where there is only one problem that is being solved, without subproblems with a parent-child relationship. A **hierarchical model** would be the opposite, for example, hierarchical clustering.
## Inference Framework
**Frequentist models**: Parameters are fixed but unknown; uncertainty comes from imaginary repeated sampling; probability describes long-run frequencies of data.
**Bayesian models**: Parameters are treated as random variables with probability distributions; uncertainty reflects incomplete information; probability is a measure of plausibility.
=> More on this difference here: [[Two Approaches to Statistics]].
