Before going into detail on how hierarchical models work, here is what they bring us: 
- Improved estimates for repeat sampling. When more than one observation arises from the same individual, location, or time, then traditional, single-level models either maximally underfit or overfit the data.
- Improved estimates for imbalance in sampling. When some individuals, locations, or times are sampled more than others, multilevel models automatically cope with differing uncertainty across these clusters. This prevents over-sampled clusters from unfairly dominating inference.
- Estimates of variation. If our research questions include variation among individuals or other groups within the data, then multilevel models are a big help, because they model variation explicitly.
- Avoid averaging, retain variation. Frequently, scholars pre-average some data to construct variables. This can be dangerous, because averaging removes variation, and there are also typically several different ways to perform the averaging. Averaging therefore both manufactures false confidence and introduces arbitrary data transformations. Multilevel models allow us to preserve the uncertainty and avoid data transformations.

But having said that, hierarchical models also come with their own challenges. Luckily we usually have a good solution for them: 
- New assumptions: We have to define the distributions (priors) from which the characteristics of the clusters arise ([maximum entropy](Using%20Information%20Theory%20to%20Select%20Models.md) helps us here).
- Estimation/ fitting is harder ([MCMC](Parameter%20Estimation%20for%20Probabilistic%20Models.md#markov-chain-monte-carlo-mcmc) helps us here).
- Harder to understand, because they make predictions at different levels of the data and model comparison techniques like WAIC ( more here [Information Criteria Methods for Model Selection](Information%20Criteria%20Methods%20for%20Model%20Selection.md)) are harder to apply.
## Simpsons Paradox
Simpson’s Paradox occurs when a trend that appears in different groups of data reverses or disappears when the groups are combined. This happens due to confounding variables that affect the relationship between the variables of interest. LMMs handle Simpson’s Paradox by explicitly modeling group-level variability (random effects), instead of treating all data points as independent. 
## Pooling
The main benefit of hierarchical models is that they take variability from different sources into account. For this, we need to introduce pooling. Pooling can be done either complete, partial, or not at all. 
- Complete Pooling: Here the data is analyzed without taking into account group information. Meaning we disregard that the data comes from different sources and estimate a common intercepts. 
	=> Problem: We discard information, never a good idea!
- No Pooling: This means that we fit a separate models to each group. The model has "amnesia".
	=> Problem. Groups with little data will overfit!
- Partial Pooling: This can be seen as a compromise between the other two approaches. The idea is that each group has its own parameter $\mu_j$, but these parameters come from a shared higher-level distribution. This allows information to be shared across groups while preventing extreme estimates for small sample sizes. This concept is also called **shrinkage**, because groups with low data are *shrunk* towards a global mean.
### Examples
Let's look at some specific examples that show the pooling concept. In this example we look to model the survival probability of tadpoles that come from different tanks.

**Complete pooling**
All tanks share a **single** survival probability p — no differences among tanks.

$\begin{aligned} S_i &\sim \text{Binomial}(N_i, p) \\ \text{logit}(p) &= \alpha \\ \alpha &\sim \text{Normal}(0, 1.5) \end{aligned}$

- One intercept $\alpha$ for all tanks
- All tanks are treated as identical
- This ignores cluster structure → **complete pooling**

**No pooling**
Each tank has its own intercept with _independent priors_ — no sharing of information.

$\begin{aligned} S_i &\sim \text{Binomial}(N_i, p_i) \\ \text{logit}(p_i) &= \alpha_{j[i]} \\ \alpha_j &\sim \text{Normal}(0, 1.5) \end{aligned}$

- Every tank $j$ has its own parameter $\alpha_j$    
- Priors independent → data from one tank tells nothing about another
- **No pooling** = maximum flexibility, but risk of overfitting small groups

**Partial pooling**
Each tank still has its own intercept, **but they’re linked** by a shared distribution.

  $\begin{aligned} S_i &\sim \text{Binomial}(N_i, p_i) \\ \text{logit}(p_i) &= a_{j[i]} \\ a_j &\sim \text{Normal}(\bar{a}, \sigma) \\ \bar{a} &\sim \text{Normal}(0, 1.5) \\ \sigma &\sim \text{Exponential}(1) \end{aligned}$

- $\bar{a}$: population-level mean (shared across tanks)
- $\sigma$: population-level SD (how much tanks differ)
 - Tanks are **partially pooled** via the shared hyperparameters ($\bar{a}$, $\sigma$), the priors for the hyperparameters are called *hyperpriors*.
#### Interpretation of Parameters
Just like in the no pooling scenario, we get an alpha for each group with partial pooling. The interpretation of these is the same, only the way these parameters is estimated changes (shared distribution). But with partial pooling, we get two additional population-level hyperparameters:
1. $\bar{a}$: the **overall mean intercept**
	- This represents the _average log-odds_ of survival across all tanks — the grand mean.
2. $\sigma$: the **standard deviation among group intercepts**
	- This quantifies how much tanks differ from each other in their survival probability.
	- Small $\sigma$ → tanks are similar (near-complete pooling).
	- Large $\sigma$ → tanks differ substantially (approaching no pooling).
#### More than One Hierarchy
It is possible, and in fact very common, to have more than one hierarchy. Let's for example assume that the specific tanks also come from specific countries. We could model this. Here is what that would look like:

  $\begin{aligned} S_i &\sim \text{Binomial}(N_i, p_i) \\ \text{logit}(p_i) &= a_{\text{tanks}[i]} + b_{\text{countries}[i]} \\ a_j &\sim \text{Normal}(\bar{a}, \sigma_a) \\ \bar{a} &\sim \text{Normal}(0, 1.5) \\ \sigma_a &\sim \text{Exponential}(1) \\ b_j &\sim \text{Normal}(0, \sigma_b) \\ \sigma_b &\sim \text{Exponential}(1) \end{aligned}$

- The only interesting thing is that we only have one hyperparameter for the means. This is because we can’t identify a separate mean for each varying intercept type, because both intercepts are added to the same linear prediction (if we do it's not the end of the world though, it just wont add anything).
