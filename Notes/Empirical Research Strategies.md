To categories our knowledge-seeking research strategies in software engineering we adopt an **ABC framework** (more on knowledge-seeking, here: [Software Engineering Research](Software%20Engineering%20Research.md). ABC stands for goals toward: 
- Actors (generalizability over people)
- Behaviour (precise measurement/control of behaviour)
- Context (realism of context). 
Important: you cannot maximize A, B and C simultaneously — improving precision/control (B) usually reduces realism (C) and/or generalizability over actors (A)!

The ABC framework places strategies on a 2D plane defined by:
- **Obtrusiveness / control** (how much the researcher manipulates the setting), and	
- **Generalizability** (how broadly results can be generalized across actors / settings).	
=> These two dimensions determine where each strategy lies and what it can deliver. 

We distinguish between *research strategies* and *research methods*:
- Research strategy = a _category / archetype_ of research activities that share similar trade-offs on the two dimensions (e.g., “Field study”, “Sample study”, “Laboratory experiment”). It’s a high-level design choice about control/realism/generalizability.
- **Research methods / techniques** = the concrete tools and procedures you use inside a strategy. These again be categorized into the three major approaches: case study, controlled experiment, survey research.

Although distinctive, it is recommended to combine strategies (triangulation across A/B/C) rather than rely on a single strategy. For example: a field study to discover phenomena → lab experiment to test causation → survey to measure prevalence.
## Validity Threats
Each of the discussed empirical research strategies face validity threats. We want to address possible criticism before the readers have had a chance to formulate it. We do this so that we ensure:
- Quality: Ensure that we think of what may go wrong before you conduct the study.
- Credibility: Have room to argue about decision made. 

Here is how different types of validity threats can creep into different stages of the experiment setup:
- Conclusion Validity: Conclusion validity concerns the **soundness of the statistical relationship** we infer from our data. It asks whether our conclusions about an effect (or lack of one) are _statistically justified_.
	- Threats: Low statistical power, Violated assumptions of statistical tests, Measurement unreliability (error in instruments).
- Internal Validity: Internal validity addresses **causality** — whether the observed effect is truly due to our treatment or might be explained by **other uncontrolled factors**.
	- Threats: 
		- Single-group threats: testing (pretests influence posttest behavior), instrumentation (changes in measurement tools), ...
		- Multiple-group threats: groups differ before the treatment, ...
		- Social threats: compensatory equalization (control group receives extra attention),  compensatory rivalry (control group tries harder), ...
- Construct Validity: Construct validity is about **conceptual correctness** — ensuring that what you _intend_ to measure and what you _actually_ measure are aligned. It checks if your operationalizations truly represent the theoretical constructs.
	- Threats:
		- Design threats: Inadequate definition of constructs (wrong theoretical basis), Mono-operation bias (only one version of the treatment), Mono-method bias (only one measurement method), Confounding constructs or treatment levels, ...
		- Social threats: Hypothesis guessing by subjects, researcher expectancy effects (bias from experimenter’s expectations), ... 
- External Validity: External validity deals with **generalizability** — whether your results apply beyond the study context (to other people, settings, or times).
	- Threats: 
		- Interaction of selection and treatment: results might not hold for people with different characteristics.
		- Interaction of setting and treatment: results might not hold in another environment or organization.
		- Interaction of testing and treatment: pretesting influences how the treatment works.
		- Interaction of history and treatment: external events alter the treatment effect.

Addressing one type of threat may increase the risk of another. For example, more homogeneous subjects may increase conclusion validity but decrease external validity. Therefore we sometimes have to prioritize which validity threats we care more about. Sometimes the priority amongst these threats, can shift depending on the context:
- Within theory (testing): Internal validity > Construct validity > Conclusion validity.
- Within applied research: Internal validity > External validity > Construct validity.
## Empirical Research Strategies
And now to go into more detail on each specific research strategy, what research methods they use and what validity threats they face. 
### Field Study (Method: Case Study)
Field studies investigate behaviors and phenomena in their real‐life context, with the setting pre‐existing the research intervention. We want to rely on field studies, when we want deep understanding of “how/why” things happen in realistic settings.

Example: Studying how distributed agile teams coordinate via Slack in a large company over 6 months; collecting interview data, code repository activity, meeting logs.

Validity / Threats:
- **Construct validity:** Are you measuring the “coordination” phenomena you intend? Might mis‐operationalize.
- **Internal validity:** Because there’s no manipulation/control, alternative explanations abound (history, maturation).
- **External validity:** Generalizing from one (or few) settings is hard—context may be unique.
- **Reliability:** Replicating exactly is difficult; documentation must be rigorous.
- **Trade‐off:** High realism (C) but lower control (B) and generalizability (A).
### Field Experiment (Method: Experiment)
Field experiments manipulate something (treatment) in a real world setting (rather than lab) and observe effects. More control than a pure field study, but still in natural context. (Often expensive/harder to arrange). Useful, when we wish to test causal hypotheses in real practice but can arrange intervention.

Example: In a software firm, teams are randomly assigned to “pair programming” vs “solo programming” for a sprint; outcomes in defects and time are tracked.

Validity / Threats:
- **Internal validity:** Still many confounders (organizational changes, team differences) difficult to isolate in field.
- **External validity:** Gains realism, but may still be context‐specific.
- **Construct validity:** Ensuring the manipulated “treatment” actually reflects the theoretical construct (e.g., “pairing”).
- **Conclusion validity:** Statistical issues if sample size small or randomization imperfect.
### Experimental Simulation (Method: Experiment)
Experimental simulations use contrived settings that mimic real situations (e.g., simulation environment) to study behaviour under conditions close to practice—but still under researcher control. Useful, when full field experiment is impossible but we need more realism than pure lab.

Example: A lab‐like simulation of a micro-service development process, with teams working in a “simulated company” environment for 2 days, then measuring their collaboration patterns.

Validity / Threats:
- **External validity:** Even though more realism than pure lab, still simulation; generalizing to real practice is limited.
- **Construct validity:** Does the simulation reflect real world sufficiently? Ecological validity risk.
- **Internal validity:** Better control than field, but some confounders may still persist (participant behaviour may differ in simulation).
- **Reliability:** Simulation setup needs to be well documented to replicate.
### Laboratory Experiment (Method: Experiment)
Laboratory experiment are the classic controlled experiment in software engineering: high control, maybe low realism. Used, when we want strong causal inference under controlled conditions.

Example: University students are given two versions of a refactoring tool; one group uses new interface, the other uses old; measured for number of defects fixed and time.

Validity / Threats:
- **Internal validity:** High potential for causal inference; but if randomization flawed, threats still present (selection, history, maturation).
- **Construct validity:** Needs careful operationalization of treatment, metrics; threats include mono‐method bias, subject knowledge variability.
- **Conclusion validity:** Ensure sufficient power, correct statistical tests, avoid “fishing” or p-hacking.
- **External validity:** Big concern: using students or toy tasks may not reflect professional practice; low realism and narrow actor/population generalizability.
- **Reliability:** Replication easier than field, but still needs full protocol, replication package.
### Judgment Study (Method: Surveys)
We want to ask experts or sampled participants to give structured judgments about artifacts or scenarios rather than performing full behaviour tasks (e.g., Delphi, focus groups). This is useful, when behaviour is hard to observe or manipulate, but expert judgments are meaningful.

Example: A group of senior software architects evaluate 10 code smells; they rate severity and cost of refactoring; results are analysed for patterns.

Validity / Threats:
- **Construct validity:** Are the judgments truly reflecting the construct (e.g., “severity” of smell)? Are experts representative?
- **Internal validity:** Less about causation; focus on collecting consistent judgments. Threats include bias (anchoring, social desirability), group dynamics.
- **External validity:** How generalizable are expert judgments to broader population of developers?
- **Reliability:** If judgments vary widely, inter‐rater reliability matters (use measures like Krippendorff’s α).
### Sample Study (Method: Surveys)
Collect standardized data from a representative sample of actors to generalize across actors (high A) but less control of behaviour and often less context realism. This is used, when we want breadth (many actors), understand prevalence, attitudes, correlations—not necessarily cause.

Example: Online survey of 500 professional developers about adoption of microservices; measure attitudes, reported practices, obstacles.

Validity / Threats:
- **External validity (generalizability):** Key challenge is sampling bias and non-response bias. Use probabilistic sampling, large response rates.
- **Construct validity (instrument):** Are survey items measuring intended constructs? Pre‐test, use validated scales, pilot.
- **Reliability:** Internal consistency of scales, test–retest reliability, coding reliability for open questions.
- **Conclusion validity:** Avoid over‐interpreting correlations as causation; ensure appropriate statistical tests for data type.
- **Internal validity:** Lower priority as causation typically not the aim (but must avoid confounding influences when interpreting relationships).
### Computer Simulation / Modeling
Build a computational replica of a system and simulate its behaviour under various conditions. Is used, when real systems are too large/slow/costly to experiment and useful for “what if” analysis. A typical analysis is performance modeling of large-scale distributed architectures.

Example: Simulate queueing of bug reports in a large open‐source project; vary number of triage team members and measure average delay.

Validity / Threats:
- **Construct validity:** Are model assumptions valid? Are parameters realistic? Ecological/internal model validity.
- **External validity:** Will simulation results transfer to real systems? Need calibration/validation with empirical data.
- **Reliability:** Model implementation must be reproducible; sensitivity analyses needed.
- **Internal validity:** Less traditional; the simulation is deterministic/parametric rather than subject to random errors; however, interpretation may still suffer from mis‐specification.
### Formal Theory
Here the goal is non‐empirical derivation of models, proofs, mathematical frameworks. For example theorem proving. We use it, when the focus is on precise fundamental understanding or tool/method derivation rather than empirical behaviour.

Example: Formal proof of the correctness of a refactoring transformation; derive conditions under which behaviour is preserved.

Validity / Threats:
- **Construct validity:** Theory must be grounded in meaningful constructs; if disconnected from practice, its usefulness is limited.
- **External validity:** Generalization to practical/software engineering contexts may fail; empirical validation needed later.
- **Reliability:** Clear, reproducible proofs.
- **Internal validity:** The logical consistency of the theory (proof soundness) is essential.
## Empirical Research Methods
Research methods are the concrete tools used by research strategies. Here we describe the three most important ones. But first, an overview: 

| **Feature**                | **Experiment**              | **Survey**                  | **Case Study**                      |
| -------------------------- | --------------------------- | --------------------------- | ----------------------------------- |
| **Main Goal**              | Test causal hypotheses      | Describe & correlate        | Explore & understand                |
| **Control**                | High                        | None                        | Low                                 |
| **Realism**                | Low                         | Medium                      | High                                |
| **Generalizability**       | Medium                      | High                        | Low–medium                          |
| **Data Type**              | Quantitative                | Quantitative                | Qualitative/mixed                   |
| **Research Question Type** | “Does X cause Y?”           | “What do people think/do?”  | “How/Why does X happen in context?” |
| **Typical Output**         | Statistical inference       | Population trends           | Rich contextual insight             |
| **Primary Validity Focus** | Internal validity           | External validity           | Construct validity                  |
| **Typical Example**        | Compare algorithms or tools | Developer experience survey | In-depth study of agile adoption    |

### Experiments
An **experiment** is an empirical study in which researchers **manipulate one or more independent variables (treatments)** and **observe the resulting effects** on one or more **dependent variables**. Within an experiment we have **subjects** (participants of the study) and **objects** (entities being worked on).
- It is the most **controlled** and **causally oriented** empirical method. If we address:
	- **Randomization:** Assigning treatments randomly to subjects to eliminate bias.
	- **Control:** Keeping non-relevant factors constant.
	- **Replication:** Four replication dimensions:
		1. **Operationalization** (how variables are defined),
		2. **Population** (different participants),
		3. **Protocol** (changes in procedures),
		4. **Experimenter** (different researchers).
- It aims to **test hypotheses** and establish **cause–effect relationships**.

The experiment process looks like this:
1. **Scoping:**
	- Define goals, hypotheses, and context (often using the GQM structure).
	- Identify dependent and independent variables.
2. **Planning:**
	- Select participants, design, and procedures.
		- **Between-subjects (independent measures):** Different subjects per treatment.
		- **Within-subjects (repeated measures):** Same subjects experience multiple treatments.
		- **Crossover design:** Each subject receives both treatments, but in reversed order.
	- Decide on randomization, blocking, or balancing.
	- Prepare instruments (tasks, surveys, tools).
	- Plan for validity evaluation.
3. **Operation:**
	- Recruit participants and conduct the experiment according to protocol.
	- Record execution details and any deviations.
4. **Analysis and Interpretation:**
	- Apply descriptive statistics to summarize results.
	- Use inferential statistics (e.g., t-tests, ANOVA, regression) to test hypotheses.
	- Interpret results in light of research questions.
5. **Presentation and Packaging:**
	- Report results transparently and include replication material (datasets, scripts).
	- Discuss validity threats and potential improvements.

Like with every research method, we have limitations and threats to validity. Beside the threats to validity, we have two main limitations of experiments:
- Difficult or impossible to apply in uncontrolled industrial contexts.
- High setup cost and limited scope (few variables, short duration).
### Surveys
A **survey** is an empirical method used to **collect information from a population or sample** to **describe, compare, or explain attitudes, behaviors, experiences, or characteristics**. Surveys are **observational** (no variable manipulation) and aim to obtain a **broad understanding** of phenomena as they occur in practice.
- It is the most **descriptive** and **generalization-oriented** empirical method.
- They often employ **questionnaires** or **structured interviews** to gather data from  **respondents** resulting in large sample size and small amount of data per individual.
- Surveys can be:
	- **Supervised** or **unsupervised/ self-administered**.
	- **Cross-sectional** (single point in time) or **longitudinal** (over time).
		- Longitudinal surveys use either a cohort (tracks groups with shared characteristics) or a panel (follows the same individuals over time).
	- **Descriptive** (quantify facts, opinions, or frequencies) or **explanatory** (explore relationships or test theories).

The survey process typically follows these steps:
1. **Scoping:**
	- Define the **research objectives**, target **population**, and **unit of analysis** (individual, team, organization).
	- Formulate research questions and map constructs to measurable variables.
2. **Planning:**
	- Design the **questionnaire** (question wording, scale types, ordering, open-ended vs. close-ended).    
	- Select **sampling strategy**:
		- _Probabilistic_ (random, stratified) → enables generalization.
		- _Non-probabilistic_ (convenience, snowball) → practical but less representative.
	- Validate the instrument via pilot testing or focus group.
3. **Operation:**
	- **Distribute** the questionnaire (online, mail, in-person).
	- **Collect responses** while monitoring response rate and dropout.
4. **Analysis and Interpretation:**
	- Use **descriptive statistics** for summarization (means, frequencies).    
	- Use **inferential statistics** (correlations, regressions, χ² tests) for hypothesis testing.
	- Check reliability (consistency of measurement) using test–retest, internal consistency, Krippendorff’s α & validity (accuracy of measurement) using content, criterion, and construct validity.
5. **Presentation and Packaging:**
	- Report instrument design, sampling details, response rate, and representativeness.
	- Discuss implications, limitations, and provide access to the questionnaire for replication.

The limitations for surveys are as follows:
- **Low control** over environment and respondent behavior.
- **Risk of bias:** Non-response, self-selection, and social desirability.
- **Measurement validity:** Misinterpretation of questions, inconsistent scales.
### Case Study
A **case study** is an empirical method that involves the **in-depth investigation of a contemporary phenomenon** within its **real-life context**. The researcher **does not manipulate variables**, but **observes, analyzes, and interprets** events, processes, or decisions as they naturally occur.
- It is the most **context-rich** and **exploratory/explanatory** empirical method.
- It allows both **qualitative and quantitative** data collection.
- Multiple **units of analysis** (projects, teams, organizations) and multiple **cases** can be studied to increase robustness.
- It aims to **understand “how” and “why”** phenomena occur. Purpose is to gain an **in-depth understanding** rather than statistical generalization.
- Should be used when; 1. there are **more variables than data points** 2. real-life phenomena cannot be manipulated.

The case study process typically looks like this:
1. **Scoping:**
	- Define **objectives**, **research questions**, and **case selection criteria**.
	- Identify **theoretical framework** to guide observation and data interpretation.
2. **Planning:**
	- Select **case(s)** (single, multiple, embedded) and **context** (industrial, academic).
	- Design **data collection strategy** (interviews, observations, documents, logs).
	- Prepare data collection protocols and define data triangulation approach.
3. **Operation:**
	- Collect **multiple sources of evidence** with different levels of interaction:
		-  _First-degree:_ direct (interviews).
		- _Second-degree:_ indirect (video, telemetry).
		- _Third-degree:_ archival analysis.
	- Maintain a **chain of evidence** through documentation and notes.
4. **Analysis and Interpretation:**
	- Interpret data qualitatively or quantitatively.	
	- Apply **triangulation** for validity:
		- **Data triangulation:** Use multiple data sources or times. 
		- **Observer triangulation:** Involve several researchers.                       
		- **Methodological triangulation:** Combine qualitative and quantitative data.     
		- **Theory triangulation:** Interpret data using different theoretical lenses.
	- Relate findings to theory and identify causal mechanisms or explanations.
5. **Presentation and Packaging:**
	- Present context, data, analysis steps, and findings transparently.
	- Include rich **descriptive narratives** and visual models.
	- Reflect on **lessons learned**, **limitations**, and **transferability** of results.
  
The limitations for case studies are as follows:
- **Time- and resource-intensive**; limited number of cases.
- **Potential subjectivity** in data interpretation.
- **Limited generalizability** — strong on depth, weak on breadth.

Common misunderstandings:
1. Case studies cannot generalize → _They can, through analytical generalization_.
2. They are only for hypothesis generation → _They also test theory_.
3. They are biased → _Transparency and triangulation counter this_.
4. They are descriptive only → _They can explain and evaluate_.