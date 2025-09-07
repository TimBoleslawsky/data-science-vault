Clinical trial team (medical lead, biostatistician, PK scientist, etc.) develops clinical  
trial protocol which contains the following important information:  
1. Clear formulation of study objectives
	- Define what the trial aims to prove.
		- Primary objectives: test for superiority, non-inferiority, or equivalence.
		- Secondary objectives: often exploratory purpose.
		- Safety and tolerability are always part of the objectives. 
2. Type of design
	 - E.g., parallel group, crossover, factorial, dose escalation, enrichment, group sequential, or adaptive design.  
3. Primary research hypothesis (for confirmatory trials (Phase III), not so much for exploratory trails (Phase I and II))
	- Analyze the endpoints to determine if the results support the study objective.
4. Study endpoints (outcome variables)
	- Provide measurable outcomes to assess whether the objective is achieved.
5. Choice of control group
	- Placebo control, active control, or multiple controls.  
6. Study population
	 - Healthy volunteers, patients, or special population (e.g. paediatric or geriatric patients).
7. Treatments
	 - How will the treatment be administered and what dose is appropriate? 
8. Blinding and randomization
9. Data collection and analysis
	  - What statistical methods are appropriate for this trail?
## Study Endpoints
The task here is to find the correct measurements to answer the research hypothesis. For example, to evaluate symptoms of heartburn with gastrozole 20 mg vs. placebo there could be any number of approaches:  
- time to sustained absence of heartburn (time to the first of 7 consecutive days free of that symptom)
- maximal intensity of heartburn within the 4 weeks of treatment  
- proportion of subjects with absence of heartburn during the 4 weeks of treatment  
- number of days free from heartburn during the entire 4-week treatment period
- ...
We want a well-established primary efficacy endpoint. If there is non-established the trail usually has a longer development time. 

The efficacy endpoints are one of these four categories:
- Continuous. For example duration of response (DoR).
- Categorical. For example mild, moderate or severe response to a specific treatment.
- Binary. For example if a patient response or not response to a specific treatment.
- Time-to-Event. For example overall survival (OS).
## Study Population
Subjects included in a trial should be a representative homogeneous sample of the target population. It is important that we are able to generalize the results. 
Before the trail we define inclusion and exclusion criteria. To be eligible a patient must meet all inclusion criteria and patients meeting any of the exclusion criteria are excluded from the trial.
## Study Design
Which type of study design we choose might depend on the objective(s) of the study, therapeutic area, time and cost, or regulatory requirements. In general there are either fixed or adaptive trail designs. Fixed trails follow a strict design => conduct => analyze design, while adaptive trails have a review and adapt phase during the conduct-stage of the trail.  
### Parallel Group Designs
![[Pasted image 20250130092959.png|400]]
### Cross-Over Designs
![[Pasted image 20250130093049.png|400]]
Advantages:
- Within subject comparison.  
- Reduced sample size.  
- Good for chronic conditions.  
- Good for pharmaceutical studies.
### Group Sequential Designs
![[Pasted image 20250130093214.png|400]]
## Randomization
When talking about randomization in clinical trails there are a few methods and techniques we can use: 
### Complete Randomization
The idea behind the random procedure here is simple, it is basically tossing a coin between experimental (E) and control (C). This generates a sequence of treatment assignments. 
- Is very dependent on sample size (Central limit theorem). With a small sample size, we do not get a equal number of patients in each of the groups.
- Long sequences with the same treatment could happen. 
### Permuted Blocks
Here the subjects are randomized in blocks of a given size (e.g., b = 2, 4, ...). Each block is a random permutation of the two treatments in equal proportions, for example: EECC, CEEC, CECE, ...
Block size should be small enough to limit possible imbalances, for example imbalance by center and time, but block size should be large enough to avoid predictability towards  
the end of the sequence. Also, the block size must be unknown!
### Stratification
Stratification is used to achieve balance between various groups. These groups could for example be gender, age, location, .... Each of these groups is first defined and divided and then randomized separately. Usually stratification is not extended to more than two groups. 
## Blinding
Randomization does not guarantee that there will be no bias by subjective judgment in evaluating and reporting the treatment effect. Such bias can be minimized by blocking the identity of treatment (blinding). There are three different forms of blinding: 
- Open label: pharmacokinetic studies, studies comparing medical and surgical treatment.  
- Single blind: pharmacokinetic studies.  
- Double blind: confirmatory (phase III) studies.