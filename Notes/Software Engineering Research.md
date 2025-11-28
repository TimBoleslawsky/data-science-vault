## Purpose and Goals of Research
The purpose of a piece of research is defined by its *purpose statement*. The purpose statement:
- Describes _why_ the research is being done and _what_ it aims to achieve.
- Should explain the **scientific** and **economic** importance.
- Appears in both **proposals** (as aims and objectives) and **final reports** (in the introduction).
- Uses action-oriented keywords: _discover, identify, evaluate, explore, compare, analyze_.
- **constrains the methodology** you can use.

Here are some examples: 
- Evaluate performance of Java JIT compilers.
- Compare requirements tools (Requisite Pro vs. DOORS).
- Develop a simulation model of district heating networks.
### Relationship Between Problem, Purpose, and Question
- **Problem:** Describes the issue or challenge.
- **Purpose:** Explains what the study aims to accomplish.
- **Research Question:** Specifies what will be investigated.
### Research Questions
In order to meet/reach your purpose, what questions do you need answered? These questions are the *research question* and guide our work. The answers to the research questions should contribute to the body of knowledge!

We usually have one main RQ, supported by a few sub-questions. Although some (e.g. exploratory studies) may not have predefined RQs and in other cases the research questions may change during the process. 

We should always avoid questions that are **unanswerable** or **already answered** (lack novelty)!

Here are some examples:
- _Main RQ:_ How can container terminal performance be improved using agent-based technologies?
	_Sub-RQs:_ Explore control, simulation, and modeling aspects.
- _Architectural RQ:_ Which software architecture best fulfills system quality attributes?
### The GQM Framework
What we have described above is the **conceptual framing** (Problem–Purpose–RQ). Now we need to also talk about **operational measurement** (Goal–Question–Metric). For this the *GQM framework* is popular. 

**GQM (Goal, Question, Metric)** is a structured approach for linking research goals to measurable outcomes. In GQM, a **goal** is defined as a **formalized operational statement** of the purpose. This is how this process could look like:
1. Define business and measurement goals.
2. Generate research questions.
3. Identify required metrics.
4. Develop data collection mechanisms.
5. Collect and analyze data in real time.
6. Perform postmortem analysis for improvements.

Usual are two different goal types:
- Knowledge-seeking research: Generate/evaluate/validate scientific claims; with insights, frameworks, and hypotheses as the outcomes.
- Solution-seeking research: Develop new or improve existing solutions; with artifacts like algorithms, tools, notations, models, etc. as the outcomes.
## Theory in Research
Theory in research is a**model** explaining how things work — used to explain or predict phenomena. Theories can take many forms: mathematical, conceptual, causal, visual, or as theoretical frameworks. Here is how we work with theory in research:
- **Induction:** Observations → Build theory.
- **Deduction:** Theory → Test predictions.
- Knowledge is formed when theories **withstand falsification** (Popper’s philosophy).

In a paper, theory may appear in the introduction, the literature review, after RQs or hypotheses. or as an emergent result (of explicitly stated).  

Theory comes from previously published work!
### Assessing Published Work
Why does this matter? Research builds on prior work. Poor sources can undermine credibility. Critical evaluation ensures **validity and reliability** of our own research! Here are some quality indicators of published work:
- **Indirect:**
	- Peer-reviewed publication? Peer-reviewing is the process, where submitted articles (either to a journal or a conference) undergo review by 2-3 experts. Can be **single-blind** (referees anonymous) or **double-blind** (both anonymous). The experts then (based on clear purpose, relevance, method validity, ...) provide feedback and accept/reject recommendations. The challenges are obviously bias and human factors!
	- Reference quality (did the authors “do their homework”)?
	- Citation impact (used carefully).
- **Direct:**
	- Read and judge: Is it valid, logical, and applicable to your work?

Here is how we usually rank sources by credibility and reliability:
1. **Academic Journals**
	- Highest rigor and peer review.
	- Up-to-date, detailed, but sometimes difficult for beginners.
2. **Books**
	- Broader coverage, may be outdated, not peer-reviewed.
3. **Conference Proceedings**
	- Quality varies; check acceptance rate and reputation.
4. **Theses and Dissertations**
	- Reviewed, variable quality; good starting points for new topics.
5. **Workshops**
	- Preliminary or ongoing research; may still be peer-reviewed.
6. **Manuals and Other Sources**
	- Often commercial or informal (e.g., white papers, company reports, news articles).
## Ethics in Software Engineering Research
First, what are ethics and how do they differ from morals. *Ethics* are externally defined rules of conduct recognized in respect to a particular class of human actions or a particular group or culture. We depend on other (e.g. science) to tell us what the "right thing to do" is. *Morals* on the other hand are intrinsically, they are an individual compass of right and wrong that we fellow because we believe it to be right. 

From this, there exist a few different ethical models to quantify the value of research: 
- **The Value-Free Model**: Rigorous research will yield results that can be used for anyone's benefit, for good or evil, for better or worse, and that in the long run, good will win out over evil if researchers adhere to methodological rigor and consistency.
- **The Social Problems Model**: Research is problem solving, i.e., all about understanding the world we live in a little better, so that we can modify it toward some greater good.
- **The Vulnerable Populations**: Research ought to be used to uplift or empower those social groups who lack power in society, especially by qualitative research giving them a "voice".
- **The Government Pawn Model:** Research ought to be of use to government decision makers so that better public policy can be made .
- ...
=> As there are always external forces effecting research (e.g. political regulations or economic regulations), there is no such thing as totally harmless research. It always costs time and
effort of the participants!
### Rules of Conduct and Code of Ethics
The *rules of conduct* prescribe “what is permitted” in terms of: 
- What research should be done?
- How should research/assignments be conducted?
- How should research/assignments be reported?
=> They are sometimes summarized in a *code of ethics*.

There are a lot of guidelines to follow, but the most common and important ones can be synthesized into: 
- Respect for Persons & the right to informed consent (eligible subjects should be able to make an informed decision of whether they consent to participate in a study).
- Benefice minimization of harm and maximization of benefits.
- Justice equitable distribution of benefits and burdens.
Additionally, we always want to strive for anonymity (redaction of all personal information of study participants), and in case we cannot ensure anonymity, resort back to confidentiality (no study participant will be identifiable individually).
## Implications & Consequence of Software Engineering Research
Here are the important implications and consequences of bad software engineering research:
- Omission (not saying something that should be said) and commission (saying something false).
- Fabrication means making up data and lying about procedures. Keeping field records and logs is a good way to proof what we did!
- Falsification means manipulating data to obtain a desired outcome (e.g. discarding data).
- Plagiarism means taking credit for someone else’s work.
## Empirical Research Strategies in Software Engineering Research
Empirical research strategies in software engineering aim to connect **theory with evidence** through structured observation and analysis.
- **Experiments** provide controlled, causal evidence.
- **Surveys** provide broad, descriptive evidence.
- **Case studies** provide deep, contextual evidence.
=> Together, they form the **methodological backbone** of empirical software engineering.

More details in this note: [[Empirical Research Strategies]].

Additionally, meta-analyses complement experiments, surveys, and case studies — they don’t replace them. They sit “one level above,” turning the _results_ of many primary studies into evidence-based general insights. More on that here: [[Meta Analysis]].