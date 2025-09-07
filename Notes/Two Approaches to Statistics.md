The two approaches to statistics are the **Frequentist approach** and the **Bayesian approach**. In general, the Frequentist approach is objective and relies on repeated sampling and long-run frequencies and the Bayesian approach incorporates prior knowledge and updates beliefs with new evidence. 

First let's answer the question of *Why?*.  The existence of both the Frequentist and Bayesian approaches comes from fundamental philosophical differences in how probability and uncertainty are understood. Here is how they differ:

1. **Frequentist Philosophy: The Objective Reality Approach**
- **Core Idea:** Probability is an objective property of the world and is tied to the frequency of events in repeated experiments.
- **View on Parameters:** Parameters (like the mean of a population) are fixed but unknown values. The randomness comes from data, not from the parameters.
- **View on Probability:** The probability of an event is defined as its long-run frequency in repeated, identical experiments.
	
	**Key Implications of Frequentist Thinking**
	- **Data is random, parameters are fixed.**
		- Example: If we flip a coin many times, the probability of heads is **fixed** at 0.5, but the outcomes vary.
		- The coin’s fairness is not assigned a probability—it is either fair or unfair; we just don’t know the truth.
	- **Inference is based on hypothetical repetitions.**
		- A **confidence interval** (e.g., “the true mean is in this interval 95% of the time”) means that if we repeated the experiment many times, 95% of those intervals would contain the true value.
	- **Hypothesis testing is indirect.**
		- We do not assign probabilities to hypotheses (e.g., “there’s a 70% chance this drug is effective”).
		- Instead, we test if data is inconsistent with a null hypothesis and reject it if unlikely enough.
		- The uncertainty is represented by the alpha (this is not needed in Bayesian hypothesis tests).

2. **Bayesian Philosophy: The Subjective Belief Approach**
- **Core Idea:** Probability represents a **degree of belief** in an event, which can be updated with new evidence.
- **View on Parameters:** Parameters are **not fixed** but rather have probability distributions reflecting our uncertainty.
- **View on Probability:** Probability is a measure of **uncertainty** and can change with new information.
	  
	**Key Implications of Bayesian Thinking**
	- **Parameters are random, data is fixed.**
		- Example: If we flip a coin and don’t know its fairness, we assign it a probability distribution (e.g., maybe it has a 70% chance of being fair and a 30% chance of being biased).
		- As we collect data, we update this belief using **Bayes’ theorem**.
	- **Inference is about belief updating.**
		- We start with a **prior belief** about a parameter.
		- We observe new data and compute the **likelihood** of that data.
		- We update our belief to get a **posterior distribution**.
	- **Hypothesis testing is direct.**
	  - Instead of rejecting a null hypothesis based on a p-value, we compute a probability directly (e.g., “there’s an 80% probability the drug is effective”).
	  - This makes Bayesian inference more intuitive in many cases.

Now the question remains: What to do with them? It is not immediately obvious when one of these approaches is preferable over the other. 
- Frequentist methods are simpler and work well for large datasets and controlled experiments. They are at the heart of for example classic hypothesis test and are usually the more sensible approach for large data and simple models.
- Bayesian methods are powerful for cases with limited data, prior knowledge, or complex models. We also cannot express our uncertainty in the Frequentist approach, because for example a hypothesis is or is not rejected. If we want that, we need a Bayesian approach. They also give us one major advantage, predictive power. 