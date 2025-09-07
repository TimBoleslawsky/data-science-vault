## Ethical Concerns vs. Utility
With everything we do we have to weigh up if the utility of something is worth the ethical concerns. This is especially relevant in terms of data science, because both the utility and the ethical concerns are so prevelant. 
## The FAT Model
**Fairness**
Fairness is defined as *treating people equally without favoritism or discrimination (the action of perceiving, noting, or making a distinction between things)*. There are multiple conflicting measures of fairness, like unfair bias or discrimination against a sensitive group.

The problem in data science is that data science is inherently discriminator! Because if we want to solve a classification problem we will be making distinctions between things. The key is to avoid unfair discrimination. Whenever we face attributes such as ethnicity, gender, or religion we need to be careful. Because not making a distinction between these attributes is also sometimes wrong, see medical applications for example.   

Data is biased if it is a non-representative sample of the population. ﻿﻿Machine Learning systems learn to replicate the biases in the data because this is precisely the job those systems are meant to do (discriminate). For example, if we want a system to learn what an engineer looks like, and we show pictures of pre-existing engineers, it will learn that engineers look like males.
Historically, most engineers have been male. The bias may be true, so the ethical question may become whether we should reinforce the pre-existing bias (esp. against a sensitive group). It is impossible to satisfy all criteria simultaneously in such a situation.

The right to privacy is also a part of fairness and is defined as the human right to not have one's personal affairs known by others, unless necessary or by consent. In data science, we for example have to be careful if the data we are using does not infringe on the privacy of some persons or groups

**Transparency**
Transparency in data science consists of two aspects. Clarity in the data science process and the ability to explain decisions made by data science models. 

We talk about *explainable Al* if ﻿an Al or ML system is explainable when the reasoning behind decisions taken by the system can be understood by human beings. The problem is that modern neural networks are often black boxes, we understand the mathematics of computation, but it is difficult to come up with intellectually satisfying explanations.

**Accountability**
Accountability means that we can: 
- implement appropriate and effective measures that principles are complied with and be able to demonstrate compliance with the measures upon request.
- recognize potential negative consequences
	- Murphy's law states that anything that can go wrong will go wrong. Because of the complexity of modern DS/AI systems, it is impossible to prepare for all consequences. Therefore we need to have monitoring and safeguards in place to react to all *known unknowns* and *unknown unknowns*.
- answer the question: Who is responsible for the actions of an Al system?
