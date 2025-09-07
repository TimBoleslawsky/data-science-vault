**Modeling** is the process of encapsulating information into a tool that can forecast and make predictions (more Information about the theory behind mathematical modeling can be found here [[Mathematical Thinking]]).

Example of a model:
In this example, we model a super simple classifier that takes a threshold $w$ and claims that all penguins are lighter than $w$ are Adelie penguins and all penguins heavier are Gentoo penguins.

``` Python
def simple_classifier(df, w):
    return df['body_mass_g'].apply(lambda x: 'Gentoo' if x > w else 'Adelie')
```

This example in the bayesian world.
## Statistical Intuition
In essence, every model is just a function! If we want to make it more specific, we can say that a model is a **function meant to represent a generative process** (a “small world” that produces the data).

In the **small world**, a statistical model contains all nominated possibilities. Surprises are excluded by definition. Here, we can judge whether a model is logically consistent. The small world is where models are built, tested, and understood.

The **large world** is the broader context of reality, where models inevitably face events and structures not imagined in their design. A model that performs perfectly in the small world may fail in the large world because of unanticipated complexities, omitted factors, or incorrect assumptions. Thus, logical coherence inside the model is no guarantee of real-world success.

=> Passing between these two worlds is the central challenge of statistical reasoning!
### Connecting Statistics and Modeling
At its core when we do mathematical modeling we model uncertainty (because we want to infer or predict something we have no certainty about). => Random variables represent the uncertain quantities (observations, parameters, noise). So the random variable tells us _what_ is uncertain (e.g., customer spend, class label, weight!

Now while the function models deterministic structure (e.g., “weight increases with height”), the distributions model uncertainty around that structure (e.g., “even given height, weights vary normally around the line”). So the distributions tell us _how_ that uncertainty is structured (what values are more likely, how spread out they are)!

=> Together, function + distribution = full statistical model. *That’s why every statistical model is, at its core, a collection of random variables tied together by functional and distributional assumptions!*

Example
## Terminology
In data science, we describe mathematical models like this: $y = g(x;θ | h)$

Left-hand side:
- $y$: target or label - what you want to predict; a result that answers the question at hand. 
Right-hand side:
- $x$: variables or features (input) - placeholder for data in order to solve a range of problems.
- $g$: model (known) - a mathematical function that is used to solve a given range of problems.
- $h$: hyperparameters (known) - part of the model $g$ (given or derived from your assumption).
- $θ$: parameters (unknown) - part of the model $g$; needs to be estimated from data.

