In **Chapter 6.4 (“Confronting confounding”)**, the book shows that every DAG, no matter how complex, is built from four _elemental relations_ between variables. These help us see when to condition and when not to condition. They map directly to the pitfalls described earlier (confounders, colliders, post-treatment bias, selection distortion, etc.).

Here are the four types :

1. **Fork (X ← Z → Y)**
	
	- Z is a **confounder**: a common cause of X and Y.
		
	- If we do not condition on Z, X and Y are spuriously associated.
		
	- Conditioning on Z _blocks_ the backdoor path, removing the spurious correlation.
		
	- Links back to Ch. 5 discussions of controlling for confounds (e.g., regional wealth affecting both education and wages).

2. **Pipe (X → Z → Y)**
	
	- Z is a **mediator** in a causal chain.
		
	- Conditioning on Z _blocks the causal path_. This leads to **post-treatment bias** (Ch. 5 plant–fungus–growth example).
		
	- The pitfall: adding “too many controls” can remove part of the causal effect you are trying to estimate.

3. **Collider (X → Z ← Y)**
	
	- Z is a **collider**, a common effect of X and Y.
		
	- By default, X and Y are independent.
		
	- Conditioning on Z (or its descendants) _opens a non-causal path_, creating **collider bias**.
		
	- This is exactly the “selection–distortion effect” discussed earlier (Ch. 5 & 6.3): restricting analysis to a subgroup (e.g., only married, only admitted students, only survivors) introduces spurious associations.

4. **Descendant (X → Z → D)**
	
	- D is a **descendant of Z**. Conditioning on D is _partially like conditioning on Z_.
		
	- If Z is a collider, conditioning on D can still open biasing paths (weaker but real).
		
	- This links to measurement error and proxy variables (Ch. 5 & 15), where using imperfect descendants as controls can distort inferences.

**How these map to earlier concepts:**

- Fork → classic confounding, “control it.”
	
- Pipe → post-treatment bias, “don’t control it.”
	
- Collider → selection bias, “never control it.”
	
- Descendant → weaker versions of the same problems, “be cautious with proxies or downstream variables.”

The big lesson: the rule “always control for more variables” is wrong. Whether conditioning helps or hurts depends on the type of path. The four elemental relations give a diagnostic grammar to avoid the pitfalls described earlier.

And as always, relying on approach introduces assumptions that
we need to keep in mind. The above rules (concerning DAGs) only
hold if some important assumptions are met, which are listed below.
(For details see Hernan and Robins (2024).)
• No spurious correlation: Correlation is not caused by random
accident. The law of large numbers dictate that the more data we
have, the more credible this assumption is.
• Consistency: The values of X (the treatment) you see are the actual
values of X, or “the values of treatment under comparison corre-
spond to well-deﬁned interventions that, in turn, correspond to the
versions of treatment in the data” (Hernan and Robins, 2024).
• Exchangeability: “the conditional probability of receiving every
value of treatment, though not decided by the investigators, de-
pends only on measured covariates” (Hernan and Robins, 2024).
speak math 3
• Positivity: in the observed data, there must be a non-zero probabil-
ity of every individual or unit receiving any level of the treatment
or exposure variable.
• Faithfulness: The causal effect does not vary over groups in a way
that makes it average to 0 in the data. X does not have a positive
effect 50% of the time and an identically powerful negative effect
50% of the time, which would average out to an effect of 0 in the
population.
If either of these assumptions are not met, it can potentially break the
relationship between the causal effect and observed data described by
these rules.
## How to Deal with Them:
Great — so in **6.4.1–6.4.3** McElreath gives a structured way to decide which variables to condition on, using DAGs and the four elemental relations we discussed. The process is often called the **backdoor path criterion**.

Here’s the breakdown:

**6.4.1 Forks and Backdoors**

- A **backdoor path** is any non-causal path between treatment (X) and outcome (Y) that _starts with an arrow into X_.
	
- Confounders lie on these backdoor paths (fork structures).
	
- To estimate the causal effect of X on Y, you must **block all backdoor paths** (by conditioning on the right variables).
	
- Example: If wealth influences both education (X) and wages (Y), wealth is a backdoor path confounder. Condition on wealth to block it .

**6.4.2 Pipes and Post-Treatment Bias**

- You should **not block pipe paths** that represent the causal process itself.
	
- If you condition on a mediator (Z in X → Z → Y), you are destroying part of the causal effect you actually want to measure.
	
- This is post-treatment bias, already illustrated in Ch. 6.2 with the fungus–plant example .

**6.4.3 Colliders and M-Bias**

- You must also **not condition on colliders**.
	
- If Z is a collider (X → Z ← Y), conditioning on it or its descendants _opens_ a backdoor path that otherwise would not exist.
	
- A special case is **M-bias**, where two forks are connected through a collider, forming an “M”-shaped path. Conditioning in the wrong place opens the whole M.
	
- Example: grandparents’ education and neighborhood quality both influence parents’ education (the collider), which then influences child’s education. Conditioning on parents’ education creates a spurious correlation between grandparents’ and child’s education .

**Practical recipe (the backdoor criterion):**

1. Draw the DAG of your causal assumptions.
	
2. Identify the treatment (X) and outcome (Y).
	
3. List all backdoor paths from X to Y.
	
4. For each path:
	
	- If it passes through a fork (confounder), condition on it.
		
	- If it passes through a pipe (mediator), do _not_ condition.
		
	- If it passes through a collider (or descendant), do _not_ condition.

5. Once all backdoor paths are blocked, you can estimate the causal effect of X on Y without bias (given your DAG is correct).

So the core insight is:

- Control confounders (forks).
	
- Don’t control mediators (pipes).
	
- Don’t control colliders or their descendants.

Would you like me to make a **comparison table** that lines up: (a) the four elemental relations, (b) what happens if you condition, and (c) whether they correspond to confounding, post-treatment bias, or selection distortion? That might give you a single overview of all these concepts.

Which of these graphs is right? We can’t tell from the data alone, because these graphs
imply the same set of conditional independencies. In this case, there are no conditional
independencies—each DAG above implies that all pairs of variables are associated, regardless
of what we condition on. A set of DAGs with the same conditional independencies is known
as a Markov equivalence set.