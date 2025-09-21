Directed acyclic graphs (DAG) help us visualize causality within [[Causal Inference]]. The nice thing is, no matter how complex, DAGs are built from four _elemental relations_ between variables. These relations also map directly to the pitfalls described earlier in the note on causal inference.
## Elemental Relations
These elemental relations are the backbone of the DAGs and map to the causal pitfalls.
### Fork
- $X ← Z → Y$
- $Z$ is a confounder: a common cause of $X$ and $Y$. If we do not condition on $Z$, $X$ and $Y$ are spuriously associated.
- More on confounders here: [[Causal Inference#Confounders]].
### Pipe
- $X → Z → Y$
- $Z$ is a mediator in a causal chain. Conditioning on $Z$ _blocks the causal path_. This leads to post-treatment bias.
- More on post-treatment bias here: [[Causal Inference#Mediators and Post-Treatment Bias]].
### Collider
- $X → Z ← Y$
- $Z$ is a collider, a common effect of $X$ and $Y$. Conditioning on $Z$ (or its descendants) _opens a non-causal path_ (by default, $X$ and $Y$ are independent), creating collider bias.
- More on collider bias here: [[Causal Inference#Colliders]]. 
### Descendant
- $X → Z → D$
- $D$ is a descendant of $Z$. Conditioning on $D$ is partially like conditioning on $Z$. If $Z$ is a collider, conditioning on $D$ can still open biasing paths (weaker but real).
### Assumptions for DAG Relations
The above rules (concerning DAGs) only hold if some important assumptions are met, which are listed below:
- No spurious correlation: Correlation is not caused by random accident. The law of large numbers dictate that the more data we have, the more credible this assumption is.
- Consistency: The values of X (the treatment) you see are the actual values of X, or “the values of treatment under comparison correspond to well-deﬁned interventions that, in turn, correspond to the versions of treatment in the data”.
- Exchangeability: “the conditional probability of receiving every value of treatment, though not decided by the investigators, depends only on measured covariates”.
- Positivity: in the observed data, there must be a non-zero probability of every individual or unit receiving any level of the treatment or exposure variable.
- Faithfulness: The causal effect does not vary over groups in a way that makes it average to 0 in the data. X does not have a positive effect 50% of the time and an identically powerful negative effect 50% of the time, which would average out to an effect of 0 in the population.
## How to Deal with Elemental Relations
To give a breakdown of how to deal with the various pitfalls indicated by the elemental relations above, we first need to introduce the concept of the *backdoor*. A backdoor is any path in the DAG from $X$ (treatment) to $Y$ (outcome) that begins with an arrow into $X$.  These paths are important because they can transmit spurious associations unless blocked.

Depending on what lies on these backdoor paths, and on what attributes we condition, they are either open or closed. To estimate the causal effect of $X$ on $Y$, we must close all backdoor paths (by conditioning on the right variables).

This is easily done: For each path:
- If it passes through a fork (confounder), condition on it.
- If it passes through a pipe (mediator), do _not_ condition.
- If it passes through a collider (or descendant), do _not_ condition.
## Conditional Independence and Markov Equivalence
**Conditional independence**: Two variables are conditionally independent if their association disappears once you control for (condition on) another variable.
**Markov equivalence**: Two DAGs are Markov equivalent if they imply _exactly the same set_ of conditional independencies.
**Implication**: If two DAGs are Markov equivalent, observational data alone (which can only reveal conditional independencies/dependencies) cannot tell them apart.

Example: 
**Case 1: A → B → C**
- A influences B, and B influences C.
- So A and C are **marginally dependent** (because A “transmits” influence through B).
- But once you know B, A tells you nothing extra about C.
**Case 2: A ← B → C**
- B influences both A and C.
- So A and C are **marginally dependent** (because they share a common cause).
- Again, once you know B, A tells you nothing extra about C.
=> These two DAGs are Markov equivalent!

