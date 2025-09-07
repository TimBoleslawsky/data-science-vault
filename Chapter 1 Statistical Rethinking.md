## Statistical Rethinking
McElreath claims that "_falsification and pre-made tests aren’t enough to do science_". There are three main problems McElreath tries to get at with the statistical practices is modern science:
- First, the use of pre-made black box statistical tests, are not useful for scientists without proper understanding of how these test were created. 
- Second, statistical models are built with associations in mind not causality. This leads to the effect, that statistical models are good at showing correlation and not causation. Also, these statistical models are not one-to-one mappable to the hypothesis. A single hypothesis can give rise to different models, and a single statistical model can be consistent with multiple hypotheses. 
- Third, the challenges of data quality and measurement errors lead to contested falsification, making it a useless practice.
=> McElreath in his book proposed an alternative (additional perspective) on how to do analysis and modeling. This approach is heavily based on Bayesian statistics and therefor differs from "classical" data analysis and machine learning approaches. 
## What Tools Should We Use?
McElreath proposes four tools to implement this statistical rethinking approach based on Bayesian statistics:
1. Bayesian data analysis => processes information!
	- Instead of pretending to falsify hypotheses, Bayesian analysis explicitly encodes assumptions and updates them with data, producing probability distributions for parameters and predictions.
	- This makes uncertainty and prior information transparent, and it avoids the false comfort of p-values.
2. Model comparison => keeps models honest about prediction!
	- Since no single model is “true,” we should compare models in terms of _predictive accuracy_ rather than binary acceptance/rejection.
	- He emphasizes cross-validation and information criteria (like WAIC, PSIS-LOO) as ways to evaluate and compare models.
	- Key insight: complex models often fit better but predict worse (overfitting).
3. Multilevel models => let you model structured, messy real-world data!
	- Also known as hierarchical models.
	- These let us share information across groups, balance underfitting and overfitting, and model structured data (clusters, repeated measures, individual variation).
	- They reduce problems like “overfitting with too many parameters” and allow richer causal questions.
4. Graphical causal models (DAGs) => connect models back to causal reasoning!
	- Directed Acyclic Graphs (DAGs) are introduced as tools for reasoning about causality.
	- They clarify assumptions about which variables cause which, and they show how conditioning on certain variables can create bias (e.g., collider bias, confounding).
	- This helps connect statistical models to actual causal hypotheses.

