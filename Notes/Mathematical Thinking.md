Mathematical thinking as a concept is composed of **mathematical reasoning**, **mathematical modeling**, and **problem-solving**. 
## Mathematical Reasoning
Mathematical reasoning is about creating a well-defined situation and drawing conclusions in small steps as far as you can!

We have two types of reasoning: *deductive* and *plausible* reasoning. 

Deductive reasoning lets us deduce new true statements from old ones. The hypothesis must be correct/ are assumed to be correct in that case. A chain of deductive arguments is called a **derivation**, and a derivation of a given statement is called a **proof**. Deductive reasoning is the core of mathematics. The ultimate goal is always to explain statements deductively. For example: 
- 'There are infinitely many prime numbers!', 
- 'The square root of 2 is not a rational number!'
- ...
We want to know if these statements are true or false and prove that. 

*Plausible* reasoning, while not ultimately the end goal, is still hugely important for mathematical reasoning. Plausible reasoning lets us draw tentative conclusions (which may not be true but can be investigated further). Plausible reasoning can be divided into *inductive* and *abductive* reasoning. Inductive reasoning 

Why is that important? => To arrive at a hypothesis or conjecture that we can prove with deductive reasoning, we usually need plausible reasoning. 
### Example of Mathematical Reasoning, Proof that $-1^2 = 1$:
- We begin with a statement we know to be true: $(1-1)*(-1) = 0$. We know this needs to be true because $(1-1) = 0$ and something times $0$ is $0$. 
- Now we formulate this problem differently to better serve our purpose: $1*(-1)+(-1)*(-1) =0$. From this follows that: $-1 +(-1)^2 = 0$. 
- For this to hold, $-1^2$ must therefore be $1$. 
## Mathematical Modeling
Applied problems are not mathematical from the beginning. You must identify and formulate them as such. A model serves as a way to represent the complex reality in a convenient way, so that we can draw conclusions about it and gain access to mathematical and computational techniques. For more specific information about what mathematical modeling means in the context of data science, look here: [[Mathematical Modeling in Data Science]].

Usually, the modeling cycle follows this pattern: 
- We have some **aspect of reality**, that we simplify and make more precise. This process is usually inductive and not deductive. 
- The result is a **mathematical model** which we (deductively) analyze. 
-  From this analysis, we get **conclusions** from the model.
- These conclusions can be interpreted to get **explanations and answers**.
- Lastly, we want to very the explanations and answers from the model against the aspect of reality. 
### Example of Mathematical Modeling, Population Growth:
- It is always useful to start simple. A simple approximation of the population growth might be a linear function like this: $p=a*x+b$. 
- The second step is to improve our model. The linear function is obviously not perfect and can be improved. We have two ways of doing this: By deduction or mechanistic modeling (thinking). & By induction or empirical modeling (looking at the data). 
	- We could use empirical modeling to look at the data and see that the growth more resembles exponential growth. 
	- We could use mechanistic modeling to reason that the growth would probably not be infinite, because of natural limitations. 
	=> Both of these conclusions lead to our final model, the logistic function. Which is both better at describing the real-world problem and also more complicated. 
## Problem-Solving
When talking about problem-solving, we mean the process of identifying a challenge, understanding its context and underlying factors, generating potential solutions, and implementing the most effective strategy to resolve it.

Key points of problem-solving are: 
- Create subproblems and work in manageable steps, but don't forget the big picture and be able to think on a strategic level.
- Use effective tools and techniques. 
- Try to investigate extreme cases to get a grasp of the problem.
- Review your progress. 

It is important to know that while knowledge from others can help in problem-solving, there is almost always some degree of knowledge created by own thinking necessary! 

