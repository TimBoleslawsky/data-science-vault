These methods described here implement the [[Learning Types in Machine Learning]] and [[Different Task Types for Mathematical Models]] for specific models. Here is where *machine learning* comes into play. 

Machine learning methods are specific implementations of parameter estimation (or function approximation) tailored to a task and a learning paradigm. Here is an example: 
*"In a regression task, the linear regression method implements an optimization procedure to estimate parameters that map features to a continuous target. Other methods, like random forests or neural networks, implement parameter/function estimation differently but for the same underlying task.”*

So here is where we would differentiate between statistical methods and machine learning methods. I will not do such a distinction, because in the end, both methods just try to implement a specific model task. Here are a bunch of approaches categorized by task:
-  [[Approaches for creating Regression Models]]
- [[Approaches for creating Classification Models]]
- [[Approaches for creating Clustering Models]]

Ensemble models in machine learning combine multiple base models to improve predictive performance. The idea is that multiple weak models, when combined, can produce better generalization and reduce overfitting. More here: [[Ensemble Models]].
## Neural Networks and Deep Learning
I said that I would not make any distinctions between statistical methods and machine learning methods to implement model tasks, but I will make this distinction between deep learning methods. Here the difference are noticeable from the models to the project workflow. 

As the basic pipeline management approach differs substantially when looking at deep learning projects compared to data science projects or "simple" machine learning projects, I want to describe the deep learning process in more detail: [[Deep Learning Project Workflow]].

Here I want to mainly focus on the theory behind deep learning. The models mentioned above struggle with complex, highly non-linear patterns, unstructured data like images, audio etc., and large-scale data. That's where deep learning and neural networks come in. Everything related to deep learning models can be found here: [[Deep Learning Models]].