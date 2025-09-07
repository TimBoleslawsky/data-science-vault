Meta analysis is a method for summarizing and integrating results from several sources (studies, articles, ...). It is used in clinical research to combine available information on a treatment. We need to take into account variability added by different sources, otherwise we could just add all the values up and gain nothing. We usually do meta analysis using hierarchical models. Here is an example of how to do this in R: [[Meta Analysis in R]]
## Pooling
So the question remains: How do we take into account variability from the different sources? For this, we need to introduce pooling. Pooling can be done either complete, partial, or not at all. 
- Complete Pooling: Here the data is analyzed without taking into account group information. Meaning we disregard that the data comes from different sources. This could for example look like this: 
	- Model: $y_i = α + βx_i + ε_i$
	- Estimates: $\hat{α} = 1.33; \hat{β} = −0.61$
- No Pooling: This means that we fit a separate models to each group. The model and the estimates could then look like this:
	- Model: $y_{ij} = α_j + βx_i + ε_i$
	- Estimates: $\hat{α_1} = 0.84, \hat{α_2} = 0.87,...; \hat{β} = −0.72$
- Partial Pooling: This can be seen as a compromise between the other two approaches. The idea is that each group has its own parameter $\mu_j$, but these parameters come from a shared higher-level distribution. This allows information to be shared across groups while preventing extreme estimates for small sample sizes (no pooling tends to overfit for small sample size). This concept is also called **shrinkage**. Here's why:
	- Let's say the model is this: 
		- $y_{ij} \sim \mathcal{N}(\mu_j, \sigma^2)$
		- $\mu_j \sim \mathcal{N}(\mu_0, \tau^2)$
	- If a school has very little data, its estimate of $\mu_j$ is **shrunk toward** $\mu_0$ (the overall mean).
	- If a school has a lot of data, its estimate of $\mu_j$ is **closer to the raw group mean**.

Example:
![[Pasted image 20250308092504.png|600]]
- The dashed-lines are complete pooling, the dotted-lines are no pooling, and the solid line is partial pooling. 