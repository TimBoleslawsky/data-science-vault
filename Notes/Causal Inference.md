Contrary to [[Inference#Descriptive / Statistical Inference]] and [[Inference#Associational / Correlational Inference]], causal inference is which associations represent real cause–effect relations, and to predict the consequences of interventions. There are a few attributes of causal inference that come with this: 
- Causal inference requires a model of the data-generating process (not just associations).
- We divide between causal and spurious associations.
- The goal isn’t just prediction, but counterfactual reasoning: _what if X had been different?_
=> In the end the "result" of causal inference is an overview over the relationships of the attributes in the model and some information about which attributes to account for in the model, depending on our goal with the model!

Below I introduce the important concepts of causality. To visualize causality, we use directed acyclic graphs: [[Using Directed Acyclic Graphs to Visualize Causality]].
## Causal vs. Spurious Associations
A *causal association* is an association between $X$ and $Y$ that reflects a _real causal path_ in the DAG (e.g., $X → Y$, or $X → Z → Y$).

A spurious association on the other hand is an association between $X$ and $Y$ that arises _without a direct causal path_. These come from backdoor paths in the DAG. These can be caused by confounders, colliders, or descendants.
## Confounders
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

We can see from the posteriori distribution here, that th mean of $b_M$ is estimated to be $0.35$, suggesting a positive correlation between divorce rate and marriage rate. => The question now is, are these effects causal or spurious? 

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

This makes $A$ a confounder, because it leads to a spurious association between $D$ and $M$, if not accounted for!
## Mediators and Post-Treatment Bias
In some senses, post-treatment biases are the opposite of masked relationships and confounders. Because these two types of mistakes in inference arise from omitting predictor variables, they are sometimes called **omitted variable bias**. Post-treatment biases on the other hand arise from including variables that are consequences of other variables. 

For an example of what a post-treatment bias is, let's assume we want to test the growth of a plant. For this we have the predictor $h_1$ (heigh after experiment) and the parameters $h_0$ (which is the starting height) and some effect on $h_0$, $p$. This $p$ is influenced by the treatment $T$ and the presence of fungus $F$. The complete model looks like this: 
- $h_{1,i} ∼ Normal(µ_i, σ)$
  $µ_i = h_{0,i} × p$
  $p = α + β_TT_i + β_FF_i$
  $α ∼ Log-Normal(0, 0.25)$
  $β_T ∼ Normal(0, 0.5)$
  $β_F ∼ Normal(0, 0.5)$
  $σ ∼ Exponential(1)$
Now if we calculate the posterior distribution for this model, we see that the treatment $T$ does not have any effect on the growth (its mean is $0$). This seems strange. The catch is, that $T$ does have an effect on $h_0$, but *through* $F$, by effecting fungus development. But this is only visible in the model, if we omit $F$ as a variable. This makes $F$ the mediator in this case. 
## Colliders
Collider bias arises when we **condition on a variable that is a common consequence of two causes**. Unlike a confounder (a common cause that links two variables), a collider blocks information flow until we condition on it—then it opens a spurious path.

The intuition behind this, is that the conditioning couples them even though they are truly independent. Lets's think of two coin flips $X$ and $Y$, and the result $Z$. The result $Z$ is obviously the consequence of the two coin flips so we can say $X → Z ← Y$. This makes $Z$ the collider in this case. Now before conditioning, knowing $X$ tells you nothing about $Y$, but if we know $Z$ and $X$ or $Y$, we are forced to infer on the unknown attribute. The same happens with the model, we can say => conditioning forces the “other variable” to explain whatever the collider doesn’t.

=> This leads to collider bias, which is defined as a false correlation created by conditioning on a common effect.
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

Note: If we think of this as a DAG, we can see that there can be colliders here as well $M → K ← N$, but the _relevant mechanism_ is confounding through the fork $N ← M → K$!
## Multicollinearity
Multicollinearity means very strong correlation between two or more predictor variables. What this means for the posterior distribution, we will show in a second. But first, it is important to note, that there is nothing wrong with multicollinearity. The model will work fine for prediction, it is now just be frustrating to understand it. 

To explain what happens here, let's look at an example, where we try to predict height from the two lengths of the legs of a person. In theory they should both be highly correlated to the height. But when looking at the posterior distribution means of the left (0.2) and the right (1.78) leg we can see that one is seems to be really correlated and the other isn't. 

If we remember that the posterior looks like this: $p(\beta_F, \beta_L \mid \text{data}) \propto p(\text{data} \mid \beta_F, \beta_L) \cdot p(\beta_F, \beta_L)$, we can see that the posterior reflects how well different pairs of coefficients ($\beta_F, \beta_L$) explain the data (likelihood), adjusted by prior beliefs. What is happening here, is that essentially two parameters hold very similar information (this could be both positive like in this case, or one negative and one positive, or both negative). That means **different combinations of** $\beta_F$ **and** $\beta_L$ **give almost the same fitted values** of $y$. This has two effects:
- Because the model can’t distinguish which predictor should carry the weight, there’s **much more uncertainty** in each coefficient. => The posterior distributions widen (standard deviations increase).
- The model can show the combined effect of the coefficients ($\beta_F, \beta_L$) (that's why its still good at predicting), but it cannot show the individual effect (that's why its bad at explaining).

When comparing multicollinearity and colliders, we have a very similar looking setup: $X → Z ← Y$. The difference is, that with multicollinearity, we have a strong correlation between $X$ and $Y$. So the separation is:
- If $X$ and $Y$ are independent → collider (conditioning induces spurious correlation).    
- If $X$ and $Y$ are correlated → multicollinearity (conditioning doesn’t induce anything new, but makes the estimates unstable).
## Plots to Analyze Causal Relationships
There are two main ways to analyze causal relationships using plots in R. Here are the two examples: 
To analyze the relationship between $M$ and $A$ further we have three options: 
### Predictor Residual Plots
This plot shows the outcome against a predictor that has been “purged” of the influence of other predictors. This lets us see the unique association between a predictor and the outcome.

In regression, a **residual** is the difference between the observed value and the value the model predicts. But in this case we do not look at the residuals, but predictor residuals. Let's look at an example:
- Suppose we want to understand the effect of predictor M (marriage rate) on outcome D (divorce rate).
- But we know M is also correlated with A (age at marriage). If we just plot M vs. D, it mixes the effect of M with the part of M that is really explained by A.
- To isolate the unique variation in M, we regress M on A, then compute the predictor residuals: $\text{resid}_M = M - \hat{M}(A)$. This is the “part of M” that cannot be explained by A.
- Then we plot D against these predictor residuals. This plot visualizes whether, after removing the association with A, the remaining variation in M is still related to D.

How to interpret the predictor residual plots:
- **Flat / no slope:** Once we control for the other predictor(s), there is no additional association between this predictor and the outcome. Its effect in the multiple regression will be near zero.
- **Positive slope:** Higher residuals of the predictor (the “extra” beyond what is explained by other variables) are associated with higher outcome values. This indicates a positive partial effect.
- **Negative slope:** The predictor’s unique part is inversely related to the outcome, suggesting a negative partial effect.
But we need to be careful, because:
- **Don’t interpret absolute position:** The residuals are centered around zero by construction, so their scale is relative.
- **Don’t confuse with causal effect:** These plots show statistical associations _after controlling for other predictors_, but they are not causal diagrams. For causal reasoning, you’d need counterfactual plots and DAGs.
### Counterfactual Plots
Here we show the causal implications of manipulating a predictor. What happens to the outcome, when we manipulate a predictor. Here is how we do this: 
1. Fit the full model, including all predictors ($A$, $M$, …) according to our DAG.
2. Generate a sequence of manipulated values of the predictor we want to analyze (for example $A$).    
3. Now we also need to decide what to do with other predictors (like $M$):
	- If you want the **total causal effect of $A$**, you let the model itself propagate the effect of $A$ through $M$ into $D$. That means you don’t hold M constant — you use the model structure ($A → M → D$ and $A → D$) to simulate both.
	- If you want the **direct effect of $A$**, you hold $M$ constant (e.g. at mean 0).    
4. Simulate the outcomes using sim() or link() to generate draws of $D$ for each manipulated $A$.
5. Now plot the mean prediction (posterior mean of $D$ for each $A$) with uncertainty bands.

How to interpret the counterfactual plot:
- The **slope or shape** of the curve tells you the causal effect of $A$ on $D$.
	_If the line is flat → no causal effect. If it slopes downward → higher_ _$A$_ _lowers divorce rates._
- The **vertical spread (interval bands)** shows the posterior uncertainty about that causal effect.
- Crucially, you’re not just plotting correlation: you’re plotting _what the model believes would happen_ to divorce if you could experimentally change age at marriage while leaving everything else in the system as modeled.
