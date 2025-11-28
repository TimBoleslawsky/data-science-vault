Data Science is my main topic of study while studying at Gothenburg University. In this Map of Content everything from basic theory to relevant programming languages regarding the topic of "Data Science" is documented. 
## Theory
### Principles of Data Science
Firstly a definition of what Data Science is: [[Data Science, a Definition]]. Now we obviously need to take a closer look at what data is, and how we can describe it: [[Data]].
#### The Goals of Data Science
Data science is about **building and using models of the world** to support decision-making. These models help us extract insights, forecast outcomes, and guide actions.

A big part of data science is to mathematically represent real world problems. For this we use the already mentioned *mathematical modeling*. For more on mathematical modeling look here: [[Data Science#Mathematical Modeling]].

Beyond modeling, data science also involves preparing data for analysis, ensuring ethical use, communicating findings effectively, and often generating new insights or questions through exploration.
- [[Data Munging]]
	- In my opinion, a big part of data munging is [[Exploratory Data Analysis]]. It can be seen as informing the data cleaning process of data munging.
- [[Data Preprocessing]], builds on top of cleaned data and focuses on preparing data specifically for modeling.
- [[Data Visualization]]
	- To convey our findings, we need [[Visualization Tools]].
- There are a lot of reasons one might have ethical concerns when talking about data science. Here we discuss some of them: [[Ethics in Data Science]].
### Mathematical Modeling
The inherent goal of mathematical modeling, statistical modeling, as well as machine learning, is to represent a underlying **data-generating process** via a model. In general (at least in probabilistic models) we have two frameworks to do this: Frequentist or Bayesian ([[Two Approaches to Statistics]]).

The basics of intuition behind the idea of mathematical modeling I describe here: [[Mathematical Modeling in Data Science]]. 

When talking about mathematical modeling and the models we produce here, there are distinct dimensions to discuss, which are not always clearly separated. Here is my attempt: 
1. **Model types =** _What functional form or distributional assumptions define the model family?_ 
2. **Learning paradigm =** _How does the model learn from data (parameter/structure estimation)?_
3. **Task type =** _What mapping or structure is the model supposed to capture in the data?_
	- **Method type** = Which algorithm or method is used to perform the task?
4. **Use cases =** _For what purpose do we use the fitted model?_
So a holistic description of a model could be: “I am using a **linear parametric model**, trained in a **supervised** way, on a **regression task**, implemented with the **linear regression** method, and I’m applying it for **inference**.” This would define the model in the following way:
- Model construction (form): _Linear model_ → specifies the function family (parametric, linear).
- Learning paradigm (estimation method): _Supervised_ → parameters estimated from labeled input–output pairs.
- Task type (mapping/structure to capture): _Regression_ → continuous target prediction.
	- Method type (specific implementation): *Linear Regression*.
- Use case (purpose of the fitted model): _Inference_ → interpret coefficients, quantify uncertainty, test hypotheses.
#### Model Types
Model types define how we specify function space/distributional assumptions to build our model. Based on how we construct our models, we can categorize them in a few different ways: [[Types of Models]]. 
#### Learning Paradigms
The existing learning paradigms define how the model adapts to data. The *learning* here just means parameter and structure estimation. Here I introduce the different learning types: [[Learning Types in Machine Learning]].
#### Task Types
The *task type* of a model specifies the kind of relationship or structure the model is intended to capture in the data, defining the _problem formulation_ (e.g., predicting a continuous outcome, grouping similar items, or uncovering latent structure). More on task types here: [[Different Task Types for Mathematical Models]].

At this point, it is also very important to talk about model evaluation. Depending on the task type, we have a few different ways we want to evaluate our models. Here is a summary: [[Evaluating Models]].

The *method type* describes the specific algorithm or estimator used to implement that task, and is where distinctions like “statistical” versus “machine learning” approaches become relevant. More on method types here: [[Different Method Types for Mathematical Models]].  

=> Together, task and method type separate _what the model aims to do_ from _how it is achieved_!
#### Use Cases for Mathematical Models
Data science uses these models for **extracting insights from data and solving problems** in two primary ways: [[Inference]] and [[Prediction]]. 
- **Core foundation:** Both inference and prediction start from a model of the **data-generating distribution**, which has parameters that we try to estimate ([[Parameter Estimation for Deterministic Models]] and [[Parameter Estimation for Probabilistic Models]]).
- **Inference:** We use the estimated parameters to **answer questions about the underlying process** (e.g., “Does weight influence height?” or “What’s the average height in the city?”).
- **Prediction:** We use the estimated parameters to **generate outcomes for new, unseen data points** (e.g., “Given weight = 80 kg, predict height”).
So the heart of both is the same — modeling the data-generating distribution — but the **goal differs**: Inference = **understanding**; Prediction = **forecasting**. Together, they inform **decision-making**, the overarching purpose of most data science projects. 

These use cases are the foundation for more advanced and elaborate task types. For more on these task types, see here: [[Different Task Types for Mathematical Models]].
### Theoretical Knowledge in Computer Science
Computer Science gives us as Data Scientists many relevant tools like databases, querying, algorithms, ... to achieve what we want to achieve as Data Scientists. Basics of computer science:
- [[Computer Architecture]]
- [[Character encodings]]
- [[Data Representation in Computers]]
- [[Data Storage and Handling]]
- Specialized Data Structures and LSH:
	- [[Probabilistic Data Structures]]
	- [[Spatial Data Structures]]
	- [[Locality-Sensitive Hashing]]
#### Computational Methods for Large Scale Data
First I want to introduce, why it is important to discuss specific computational methods for large scale data: [[Motivation for Computational Methods for Large Scale Data]].

From the motivation it becomes apparent that parallel computing is necessary for almost all modern systems. What parallel computing is and what forms it can take is described here: [[Parallel Computing]].
#### Algorithms
An **algorithm** is a set of rules, instructions, or steps designed to solve a particular problem or perform a specific task. It is the procedure or method used to process data and achieve a desired outcome. 
- [[Basics of Algorithms]]
- 'Support'-Algorithms:
	- Sort algorithms: [[Sort Algorithms]]
	- Search algorithms: [[Search Algorithms]]
	- Graph algorithms: [[Graph Algorithms]]
#### Computational Problem Solving
Computational problem solving bridges math, data science, machine learning, and computer science. In general what I mean by this are algorithmic and mathematical techniques to efficiently model, analyze, and solve both continuous and discrete problems in data science and related fields.

Optimization problems, dynamic programming, and constraint satisfaction problems are fundamental to data science because they enable efficient and accurate solutions to complex analytical tasks. They appear in almost all aspects of data science and are therefore crucial to understand. For more, see these articles.
- [[Constraint Satisfaction Problems and Constraint Programming]]
- [[Optimization Problems]]
- [[Basics of Algorithms#Dynamic Programming|Dynamic Programming]]
### Mathematical Concepts of Data Science
Here I want to lay to mathematical foundation for almost all the data science problems and approaches. The foundational mathematical concepts of mathematical modeling and data science are sets, logic, and functions. Upon these probability and statistics are built. We also have supporting but central concepts. Lastly I also want to emphasize mathematical thinking.
#### Foundational Concepts
Basically all of data science is built upon sets, logic, and functions. **Sets** provide the universe of objects we reason about (sample spaces, datasets, feature sets). **Logic** rules for combining and reasoning about statements (algorithms, inference, queries). **Functions**, as the backbone of mathematical modeling, formalize mappings and transformations (models, feature engineering, predictions).
##### Sets
Sets are a basic mathematical concept that underpins most data structures and operations in data science: [[Basics of Sets]].
- [[Special Sets]]
- Relations extend the idea of sets by linking elements from two or more sets, which is key in structuring and analyzing data: [[Relations]].
##### Logic
Mathematical logic is the backbone of reasoning and formalization in data science: [[Basics of Logic]].
##### Functions
Functions describe relationships between variables and are at the heart of mathematical modeling and mapping in data science: [[Functions]].
- [[Special Functions]]
#### Statistics & Probability
Statistics is at the heart of data science. From characterizing data sets to making predictions based on probability and inferential statistics, without statistics data science is worthless. The basics of statistics for data science can be found here: [[Basics of Probability and Statistics for Data Science]].
#### Supportive Mathematical Concepts
These concepts are less of a backbone and more serve more specific purposes. Nonetheless they are essential for data science. 
- [[Distances|Distances]] needed for geometry of data. These are important because they, for example, tell us how far apart and therefore how different two points are. This comes especially in handy when dealing with [[Approaches for creating Clustering Models|clustering]].
- Linear algebra for vector/matrix representation of data and models.
- Calculus / Optimization for learning models (gradient descent, likelihood maximization).
- [[Foundations of Information Theory]] provide formal, mathematically provable limits on what compression, communication, and inference systems can achieve.
#### Mathematical Thinking
As discussed here, [[Data Science, a Definition]], the purpose of data science is to tackle real-world problems. Mathematical thinking is the ability to formulate real-world problems and interpret the results of mathematical solutions in a meaningful way. It is not about solving mathematical problem XY, but how we arrive at that problem from a non-mathematical problem. That's why it is so important for data scientists to be able to apply mathematical thinking. The basics of mathematical thinking are described here: [[Mathematical Thinking]]

Some insights and lessons learned form the course *Applied Mathematical Thinking* are summarized in this report: [[The Mathematical Thinking Handbook for Data Scientists]].
## Programming
### Python
Python is the main language used by data scientists. It provides a wide variety of supported libraries to do basically any analysis, inference, or machine learning task. The basics of Python, which are discussed in this chapter, are not specific to the domain of Data Science and are useful beyond that scope.
- [[Data Structures in Python]]
	- [[Advanced Data Structures in Python]]
- [[Different Method Types in Python]]
- [[Special Functions in Python]]
- [[Documentation in Python]]
- [[Runtimes in Python]]
- [[Inheritance in Python]]
- [[The Basic Principles of OOP in Python]]
- [[Pointers in Python]]

Furthermore, here are two extensive examples of machine learning tasks implemented in Python: [[The Data Science Process in Python]], [[Simple Machine Learning Task in Python]].
### R (and SAS)
R and SAS are primarily used in research and bioinformatics. Examples of how to do inference and data analysis with R can be seen throughout this vault. 
### UNIX
UNIX is an integral part of working with Python or any Data Science programming language. Why that is, and what it can do is discussed here: [[Why use UNIX as a Data Scientist?]]
#### Theory
First let's discuss what UNIX it and what it does: [[Basics of UNIX]]. We can create scripts in UNIX by using [[Shell Scripts]].

As discussed here [[Motivation for Computational Methods for Large Scale Data]], [[Notes/Parallel Computing|parallel computing]] is a necessary technique for many modern systems. Here is how we can implement parallel computing: [[SLURM]].
## Research & Applications
In this chapter I want to document how we do research as data scientist/ software engineers and how important theories described above connect to research and practice. 
### Empirical Software Engineering Research
The basics for how we do research and what research is within a software engineering context is discussed here: [[Software Engineering Research]].
### Machine Learning and AI In Practice
In this part I want to differentiate the topics Data Science, Machine Learning and AI. I want to look at what Machine Learning and AI are, how they differ from Data Science, and what applications use ML and AI today: [[Differentiating Data Science, Machine Learning and AI]].

Right now most of the research done in this area is focused on model-centric AI. A promising new movement is called *data-centric AI*. More on that here: 
[[Data-Centric AI vs. Model-Centric AI]].
### Data Science in Biomedicine
I will mainly focus on the context of drug development when talking about biomedicine (more specifically, drug development at AstraZeneca). 

To understand data science in the context of biomedicine, we first have to look the basics of [[Clinical Trails|clinical trails and controlled randomized experiments]].

To evaluate the outcomes of clinical trails and answer research questions, we use [[Inference|hypothesis testing]]. Additionally multiplicity as big issue when using hypothesis testing in the context of clinical trails, more on that here: [[Multiplicity in Clinical Trails]]. 

Here are some more interesting topics regarding data science in biomedicine:
- [[Survival Analysis]]
- [[Simulation in Data Science for Biomedicine]]