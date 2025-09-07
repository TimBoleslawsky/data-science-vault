Data Science is my main topic of study while studying at Gothenburg University. In this Map of Content everything from basic theory to relevant programming languages regarding the topic of "Data Science" is documented.
## Theory
### Principles of Data Science
Firstly a definition of what Data Science is: [[Data Science, a Definition]]. Now we obviously need to take a closer look at what data is, and how we can describe it: [[Data]].
#### The Goals of Data Science
Data science is about **building and using models of the world** to support decision-making. These models help us extract insights, forecast outcomes, and guide actions.

A big part of data science is to mathematically represent real world problems. For this we use *modeling*. The basics of this idea can be found here: [[Mathematical Modeling in Data Science]]. To categorize these models we usually define these different types: [[Types of Models]]. 

[[Data Science#Data Science, Machine Learning and AI|Machine learning]] provides algorithms and frameworks to construct models ([[Basic Intuition for Modeling in ML]]). The line between *traditional* mathematical modeling and machine learning can be confusing. For a general definition, the difference is really one of intention:
- Build a linear regression with explicit causal assumptions → that’s mathematical modeling.
- Train a linear regression purely to minimize error on test data → that’s machine learning.
Same math, different framing.

Data science uses these models for **extracting insights from data and solving problems** in two primary ways:
1. [[Inference]]: learning about unknowns in the model (parameters, causal effects).
2. Prediction: predicting or simulating data that hasn't been observed (more in this, see here [[Data Science#Theory behind Machine and Deep Learning]]). 
Both are complementary: inference provides understanding, prediction provides foresight. Together, they inform **decision-making**, the overarching purpose of most data science projects. 

Beyond these, data science also involves preparing data for analysis, ensuring ethical use, communicating findings effectively, and often generating new insights or questions through exploration.
- [[Data Munging]]
	- In my opinion, a big part of data munging is [[Exploratory Data Analysis|exploratory data analysis]]. It can be seen as informing the data cleaning process of data munging.
- [[Data Preprocessing]], builds on top of cleaned data and focuses on preparing data specifically for modeling.
- [[Data Visualization]]
	- To convey our findings, we need [[Visualization Tools|visualization tools]].
- There are a lot of reasons one might have ethical concerns when talking about data science. Here we discuss some of them: [[Ethics in Data Science]].
### Data Science, Machine Learning and AI
In this part I want to differentiate the topics Data Science, Machine Learning and AI. I want to look at what Machine Learning and AI are, how they differ from Data Science, and how Data Scientists can use Machine Learning and AI: [[Differentiating Data Science, Machine Learning and AI]].
#### Theory behind Machine and Deep Learning
Like I mentioned here ([[Data Science#The Goals of Data Science]]) machine learning in its most basic understanding is just a tool-box for creating models. They can be used for both inference and prediction. Because in practice, it is much more common to use these models for prediction tasks, the chapters below focus on this. 

We categorized the models we build into regression-models, classification-models, and clustering-models.
- Approaches (Algorithms) for creating Models:
	- [[Approaches for creating Regression Models]]
	- [[Approaches for creating Classification Models]]
	- [[Approaches for creating Clustering Models]]
- There are a few different approaches to evaluating models. What they are, when to use them, and which methods are appropriate for each approach is documented here: [[Evaluating Models]]
- While building models a common pitfall is overfitting the model. [[Regularization]] can help with that.
- As we are talking about machine learning models, it becomes obvious that we need to introduce the different learning types: [[Learning Types in Machine Learning]].

Ensemble models in machine learning combine multiple base models to improve predictive performance. The idea is that multiple weak models, when combined, can produce better generalization and reduce overfitting. More here: [[Ensemble Models]].
##### Neural Networks and Deep Learning
As the basic pipeline management approach differs substantially when looking at deep learning projects compared to data science projects or "simple" machine learning projects, I want to describe the deep learning process in more detail: [[Deep Learning Project Workflow]].

Here I want to mainly focus on the theory behind deep learning. The models mentioned above struggle with complex, highly non-linear patterns, unstructured data like images, audio etc., and large-scale data. That's where deep learning and neural networks come in. Everything related to deep learning models can be found here: [[Deep Learning Models]].
#### Applications of AI and Machine Learning
A very popular use-case for data science and AI is recommendation systems. Recommendation systems try to solve the problem of personalizing the display policy on websites. More on that here: [[Recommendation Systems]].

Another popular use-case for AI systems are dialogue systems. These systems aim to mimic human interaction to provide some service or conversation to a human user. More on this topic here: [[Dialogue Systems and AI]]

Game playing focuses on the interaction between a player (AI) and some opponent (random, human, ...). AI can be taught a variety of games and this has been the focus in improving AI for quite some time. 
- Here is an example using the [[Monte Carlo Tree Search and Game Playing|Monte Carlo Tree Search algorithm]]: [[Game Playing with MCTS and Deep Learning]]. 

Retrieval-Augmented-Generation (RAG) is a popular technique used in artificial intelligence. The basics of what RAG is and how it works can be found here: [[Retrieval-Augmented Generation (RAG)]] and a demo use case using this obsidian vault can be found here: [[RAG for Obsidian]].
##### Current Research & Application Areas for Machine Learning
The applications above are mostly outdated to some extend or basic use cases which are being built upon today. In this note I discuss the current research & application ares for machine learning: [[Current Research & Application Areas for Machine Learning]].

Besides the development of task-specific deep learning models, the most popular application of deep learning models (in the form of foundation models) is [[AI Engineering]].

Right now most of the research done in this area is focused on model-centric AI. A promising new movement is called *data-centric AI*. More on that here: [[Data-Centric AI vs. Model-Centric AI]]
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
Here I want to lay to mathematical foundation for almost all the data science problems and approaches. The foundational mathematical concepts of mathematical modeling and data science are sets, logic, and functions. Upon these probability and statistics are built. We also have supporting but central concepts. Lastly I also want to emphasize [[Data Science#Mathematical Thinking|mathematical thinking]].
#### Foundational Concepts
Basically all of data science is built upon sets, logic, and functions. **Sets** provide the universe of objects we reason about (sample spaces, datasets, feature sets). **Logic** rules for combining and reasoning about statements (algorithms, inference, queries). **Functions**, as the backbone of mathematical modeling, formalize mappings and transformations (models, feature engineering, predictions).
##### Sets
Sets are a basic mathematical concept that underpins most data structures and operations in data science: [[Basics of Sets]].
- [[Special sets]]
- Relations extend the idea of sets by linking elements from two or more sets, which is key in structuring and analyzing data: [[Relations]].
##### Logic
Mathematical logic is the backbone of reasoning and formalization in data science: [[Basics of Logic]].
##### Functions
Functions describe relationships between variables and are at the heart of mathematical modeling and mapping in data science: [[Functions]].
- [[Special functions]]
#### Statistics & Probability
Statistics is at the heart of Data Science. From characterizing data sets to making predictions based on probability and inferential statistics, without statistics data science is worthless. The basics of statistics for data science can be found here: [[Basics of Probability and Statistics for Data Science]].
#### Supportive Mathematical Concepts
These concepts are less of a backbone and more serve more specific purposes. Nonetheless they are essential for data science. 
- [[Distances|Distances]] needed for geometry of data. These are important because they, for example, tell us how far apart and therefore how different two points are. This comes especially in handy when dealing with [[Approaches for creating Clustering Models|clustering]].
- Linear algebra for vector/matrix representation of data and models.
- Calculus / Optimization for learning models (gradient descent, likelihood maximization).
#### Mathematical Thinking
As discussed here, [[Data Science, a Definition]], the purpose of data science is to tackle real-world problems. Mathematical thinking is the ability to formulate real-world problems and interpret the results of mathematical solutions in a meaningful way. It is not about solving mathematical problem XY, but how we arrive at that problem from a non-mathematical problem. That's why it is so important for data scientists to be able to apply mathematical thinking. The basics of mathematical thinking are described here: [[Mathematical Thinking]]

Some insights and lessons learned form the course *Applied Mathematical Thinking* are summarized in this report: [[The Mathematical Thinking Handbook for Data Scientists]].
### Applications of Data Science
In this chapter I want to document various the different fields where I have knowledge of the application of data science. 
#### Data Science in Biomedicine
I will mainly focus on the context of drug development when talking about biomedicine (more specifically, drug development at AstraZeneca). 

To understand data science in the context of biomedicine, we first have to look the basics of [[Clinical Trails|clinical trails and controlled randomized experiments]].

To evaluate the outcomes of clinical trails and answer research questions, we use [[Inference|hypothesis testing]]. Additionally multiplicity as big issue when using hypothesis testing in the context of clinical trails, more on that here: [[Multiplicity in Clinical Trails]]. 

Here are some more interesting topics regarding data science in biomedicine:
- [[Survival Analysis]]
- [[Simulation in Data Science for Biomedicine]]
## Programming
### Python
#### Basics
The basics of Python, which are discussed in this chapter, are not specific to the domain of Data Science and are useful beyond that scope.
- [[Data Structures in Python]]
	- [[Advanced Data Structures in Python]]
- [[Different Method Types in Python]]
- [[Special Functions in Python]]
- [[Documentation in Python]]
- [[Runtimes in Python]]
- [[Inheritance in Python]]
- [[The Basic Principles of OOP in Python]]
- [[Pointers in Python]]
#### Data Science in Python
In the chapter [[Data Science#Principles of Data Science]], we discuss the basic principles of Data Science. Especially for implementing algorithms and creating models, we use Python. Some use cases and examples are listed below:

**Basics Steps of the Data Science Process in Python**
- [[Transformation and Scaling in Python]]
- [[Visualizing Data in Python]]
- [[Data Analysis in Python]] 
- [[The Data Science Process in Python]]

**Inference in Python**
- [[Hypothesis Testing in Python]] 

**Machine Learning in Python**
- [[Regression in Python]]
- [[Decision Tree Classification in Python]]
- [[Final Model Evaluation in Python]]
- [[Hyperparameter Tuning & Overfitting Analysis in Python]]
- [[Simple Machine Learning Task in Python]]
- [[Ensemble Models in Python]]

**Concepts of Computer Science in Python**
- [[Parallel Programming in Python]]
### R (and SAS)
R and SAS are primarily used in research and bioinformatics. Here I want to collect a few examples of how statistical ideas can be represented in R and SAS:
- Basic hypothesis testing and data analysis in R: [[Data Analysis in R.pdf]]
- [[Linear Mixed Models in R and SAS]]
- [[Meta Analysis in R]]
- Survival Analysis in R: [[Survival Analysis.pdf]]
	- Simulation and Survival Analysis in R: [[Simulation and Survival Analysis.pdf]]
### UNIX
UNIX is an integral part of working with Python or any Data Science programming language. Why that is, and what it can do is discussed here: [[Why use UNIX as a Data Scientist?]]
#### Theory
First let's discuss what UNIX it and what it does: [[Basics of UNIX]]. We can create scripts in UNIX by using [[Shell Scripts]].

As discussed here [[Motivation for Computational Methods for Large Scale Data]], [[Notes/Parallel Computing|parallel computing]] is a necessary technique for many modern systems. Here is how we can implement parallel computing: [[SLURM]].

