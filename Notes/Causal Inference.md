What is causal inference and definitions
To visualize causality, we use directed acyclic graphs: [[Using Directed Acyclic Graphs to Visualize Causality]].
## Example of Spurious Associations
Let's assume we want to investigate the relationship between divorce rate $D$, marriage rate $M$, and median age at marriage $A$. First we fit a model which predicts $D$ only based on $A$:

```R
m5.1 <- quap(
	alist(
		D ~ dnorm(mu, sigma),
			mu <- a + bA * A,
			a ~ dnorm(0, 0.2),
			bA ~ dnorm(0, 0.5),
			sigma ~ dexp(1)
		), data = d
)
```

We can see from the posterior distribution, that the mean of $b_A$ is estimated to be $-0.568$, suggesting that older median marriage → lower divorce.

We now to the same for the relationship between divorce rate $D$ and marriage rate $M$:

```R
m5.2 <- quap(
	alist(
		D ~ dnorm(mu, sigma),
			mu <- a + bM * M,
			a ~ dnorm(0, 0.2),
			bM ~ dnorm(0, 0.5),
			sigma ~ dexp(1)
		), data = d
)
```

We can see from the posteriori distribution here, that th mean of $b_M$ is estimated to be $0.35$, suggesting a positive correlation between divorce rate and marriage rate. 

=> The question now is, are these effects causal or spurious? A spurious association is a statistical correlation between $X$ and $Y$ that arises because a third variable $Z$ (the confounder) causally influences both $X$ and $Y$ (a common-cause). Once you control for $Z$, the $X–Y$ association disappears.

For this, we introduce a multiple regression model that accounts for both the effect of $A$ and $M$ on $D$.

``` R
m5.3 <- quap(
	alist(
		D ~ dnorm(mu, sigma),
			mu <- a + bA * A + bM * M,
			a ~ dnorm(0, 0.2),
			bA ~ dnorm(0, 0.5),
			bM ~ dnorm(0, 0.5),
			sigma ~ dexp(1)
		), data = d
)
```

If we look at the estimated means from the posterior distribution, we can see that the effect of $A$ stayed roughly the same ($-0.61$) while the effect of $M$ is now almost zero ($-0.065$).

To analyze the relationship between $M$ and $A$ further we have three options: 
1. Predictor residual plots. These plots show the outcome against residual predictor values. They are useful for understanding the statistical model, but not much else.
2. Posterior prediction plots. These show model-based predictions against raw data, or otherwise display the error in prediction. They are tools for checking fit and assessing predictions. They are not causal tools.
3. Counterfactual plots. These show the implied predictions for imaginary experiments. These plots allow you to explore the causal implications of manipulating one or more variables.
=> TBD 
## Multiple Causation and Masked Relationships
Let's again look at an example to understand what masked relationships are. Let's say we want to predict milk energy $K$ from body mass $M$ and neocortex size $N$. 
- If we model $K$ ~ $M$, $M$’s slope is weak because some of the covariance between M and K comes from $N$’s positive effect, which offsets $M$’s negative direct effect.
- If we model $K$ ~ $N$, $N$’s slope is weak because $N$ is correlated with $M$, which exerts a negative effect.
- If we model $K$ ~ $M + N$, the model isolates:
	- the negative **direct effect of $M$** (holding $N$ fixed), and
	- the positive **direct effect of $N$** (holding $M$ fixed).

Here is the logical intuition behind this: 
=> More $M$ tends to _directly_ reduce milk energy ($K$). But more $M$ also tends to increase neocortex size ($N$), and more $N$ _increases_ milk energy. => If we ignore $N$, then part of $M$’s positive _indirect_ effect via $N$ cancels against its negative _direct_ effect, so the slope looks weaker (masked). The same happens for $N$ but in the opposite direction. 

And here is the statistical explanation for this:
=> In a **simple regression** (say $K \sim M$), the slope $b_M$ reflects **all the covariance** between $M$ and $K$ — both direct and indirect paths. But if $M$ and $N$ are correlated, part of that covariance really belongs to $N$’s influence on $K$. So $M$’s slope in the simple model is **contaminated**.
=> In a **multiple regression** ($K \sim M + N$), the model separates the variance in $K$ that is predictable from $M$ versus the variance that is predictable from $N$.

- **Masked relationship** = arises when there is both a direct effect and an indirect effect that overlap (like M → K and M → N → K).
	
	- If you ignore the indirect path, the direct effect looks weak.
		
	- Once you condition on the indirect cause (N), the direct path is unmasked.

- Even though the graph contains a collider, the _relevant mechanism_ is confounding through the fork M → N → K.
## Interactions
Chapter 8
## Causal Inference Pitfalls
The previous sections tell us what is great about multiple regression. Here is what is bad about it: 
### Multicollinearity
Multicollinearity means very strong correlation between two or more predictor variables. What this means for the posterior distribution, we will show in a second. But first, it is important to note, that there is nothing wrong with multicollinearity. The model will work fine for prediction, it is now just be frustrating to understand it. 

To explain what happens here, let's look at an example, where we try to predict height from the two lengths of the legs of a person. In theory they should both be highly correlated to the height. But when looking at the posterior distribution means of the left (0.2) and the right (1.78) leg we can see that one is seems to be really correlated and the other isn't. 

If we remember that the posterior looks like this: $p(\beta_F, \beta_L \mid \text{data}) \propto p(\text{data} \mid \beta_F, \beta_L) \cdot p(\beta_F, \beta_L)$, we can see that the posterior reflects how well different pairs of coefficients ($\beta_F, \beta_L$) explain the data (likelihood), adjusted by prior beliefs. What is happening here, is that essentially two parameters hold very similar information (this could be both positive like in this case, or one negative and one positive, or both negative). That means **different combinations of** $\beta_F$ **and** $\beta_L$ **give almost the same fitted values** of $y$. This has two effects:
- Because the model can’t distinguish which predictor should carry the weight, there’s **much more uncertainty** in each coefficient. => The posterior distributions widen (standard deviations increase).
- The model can show the combined effect of the coefficients ($\beta_F, \beta_L$) (that's why its still good at predicting), but it cannot show the individual effect (that's why its bad at explaining).
### Post-Treatment Bias
In some senses, post-treatment biases are the opposite of masked relationships and confounders discussed above. Because these two types of mistakes in inference arise from omitting predictor variables, they are sometimes called **omitted variable bias**. Post-treatment biases on the other hand arise from including variables that are consequences of other variables. 

For an example of what a post-treatment bias is, let's assume we want to test the growth of a plant. For this we have the predictor $h_1$ (heigh after experiment) and the parameters $h_0$ (which is the starting height) and some effect on $h_0$, $p$. This $p$ is influenced by the treatment $T$ and the presence of fungus $F$. The complete model looks like this: 
- $h_{1,i} ∼ Normal(µ_i, σ)$
  $µ_i = h_{0,i} × p$
  $p = α + β_TT_i + β_FF_i$
  $α ∼ Log-Normal(0, 0.25)$
  $β_T ∼ Normal(0, 0.5)$
  $β_F ∼ Normal(0, 0.5)$
  $σ ∼ Exponential(1)$
Now if we calculate the posterior distribution for this model, we see that the treatment $T$ does not have any effect on the growth (its mean is $0$). This seems strange. The catch is, that $T$ does have an effect on $h_0$, but *through* $F$, by effecting fungus development. But this is only visible in the model, if we omit $F$ as a variable. 
### Collider Bias
Collider bias arises when we **condition on a variable that is a common consequence of two causes**. Unlike a confounder (a common cause that links two variables), a collider blocks information flow until we condition on it—then it opens a spurious path.

**Example (from Ch. 6.3):**

Age and happiness both influence the probability of being married. If we condition on _marriage status_ (the collider), we see a spurious association: among married people, older individuals appear less happy; among unmarried people, the same pattern appears. But in truth, there is no causal path from age → happiness . The association is an artifact of conditioning on the collider.

**Another example (the “haunted DAG”):**

Grandparents’ education (G) influences parents’ education (P), which influences children’s education (C). But suppose there’s also an unmeasured neighborhood effect (U) that influences both P and C. Now P is a **collider** of G and U. If we condition on P (for example by stratifying or including it in a regression), we create a spurious negative association between G and C, even though G has no direct effect on C .

**Relation to confounders:**

- A **confounder** (fork structure: X ← Z → Y) induces a spurious association unless we _condition on it_ to block the path.
	
- A **collider** (X → Z ← Y) has no association between X and Y unless we _do_ condition on it, which opens the path and induces bias .

- Two variables (say A and B) both influence a third (the collider C).
	
- By default, A and B are independent.
	
- But if we **condition on C** (or on a descendant of C), we induce a spurious correlation between A and B.

Intuitively: the collider doesn’t “discriminate” which parent variable produced its value, so when you restrict the sample by C (e.g., looking only at married people, only admitted students, only survivors), you accidentally couple A and B.

So collider bias = **false correlation created by conditioning on a common effect**.

1. Fork: X <- Z -> Y, Z = confounder, not accounting for Z leads to spurious association between X and Y.

2. Pipe: X -> Z -> Y, Z = mediator, accounting for Z leads to post-treatment bias (we dont see the correlation between X and Y).

3. Descedent: X -> Z -> D, D = descendet of Z, conditioning on D is partially like conditioning on Z.

Now here is where it gets interesting: 

4. Collider: X -> Z <- Y, Z = collider, accounting for Z leads to spurious association between X and Y (collider bias).

But, we have a very similar setup for Multicollinearity: X -> Z <- Y, but with a strong correlation between X and Y. Here accounting for both distributed the effect between the two and leads to uncertainty. So the separation is:
- If X and Y are independent → collider (conditioning induces spurious correlation).    
	- If X and Y are correlated → multicollinearity (conditioning doesn’t induce anything new, but makes the estimates unstable).

We also have a very similar setup for Masked relationships, but even though the graph contains a collider, the _relevant mechanism_ is confounding through the fork M → N → K.
