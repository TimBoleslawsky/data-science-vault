The main idea of neural networks is to learn features from data. We could theoretically handcraft additional features and add them to linear classifiers to solve non-linear problems. But instead of doing this, we use neural networks which consist of a series of sub-models (layers) to learn the features and a final model for classification/regression. By combining linear classifiers we can therefore capture non-linear problems. This is an important point I want to further explain: 

- In the logistic regression the thing we need to check (aka the decision boundary) is something of form $w_1 x_1 + w_2 x_2 + b = 0$. So even though we use a non-linear function (sigmoid) the decision boundary is linear (for more detail look here: [[Mathematical Modeling in Data Science]]). 
- In neural networks (with activation function = sigmoid) this decision boundary is something of form $c_1 \cdot \sigma(a_1 x_1 + a_2 x_2 + b_1) + c_2 \cdot \sigma(a_3 x_1 + a_4 x_2 + b_2) + b_3 = 0$. This time the sigmoid function is not only part of the model, but also part of the previous model (aka the input) making the decision boundary of the following model non-linear.  

These complex non-linear patterns are often called **hierarchical features**. Especially deep neural networks extract information from input data across multiple layers. The lower layers capture low-level, general features and each additional layer captures more abstract and complex features, which leads to the power of deep neural networks.

Now that we know why we need deep learning models, I want to discuss everything related. Below is the list of everything basic one needs to know when discussing deep learning models: 
- **Use cases for deep learning models:** Here we discuss what deep learning models are generally used for ([[Use Cases for Deep Learning Models]]).
- **How neural networks work:** This includes the basic structure of neural networks ([[Basic Structure of Neural Networks]]) and how neural networks learn ([[The Learning Process in Neural Networks]])
- **The most important paradigms and frameworks in deep learning:** Here we discuss very common paradigms that cut across different deep learning architectures ([[Deep Learning Paradigms and Frameworks]]).
- **The building blocks of deep learning models:** The building blocks of deep learning models are consolidated in key architecture used across different paradigms and use cases ([[Key Architectures in Deep Learning]]).
## Advanced Topics Regarding Deep Learning Models
Above we discuss the basics of deep learning models. In this chapter I want to focus on the more nuanced and advanced topics related to the work with deep learning models.

Usually, when developing a new deep learning model, we will start with a simple baseline and then optimized iteratively. This can be confusing and overwhelming. Here is a general guideline how to structure this optimization process: [[Neural Network Optimization]].
