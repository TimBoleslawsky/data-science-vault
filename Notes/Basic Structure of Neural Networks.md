Artificial Neural Networks (ANNs) are the foundation of deep learning. In theory, they are just a large function that takes some input and produces some output.  

The very basic computational unit within a neural network is called *neuron*. Neurons are connected between the layers, the other key elements within a neural network, and serve as midway-points for the values in the network.  
## Layers
Layers combine and connect the neurons in different ways. The basic structure of ANNs looks like this:
- **Input layer:** Takes the input, for example an image.  
- **Hidden layer(s):** Process the input (extract features or learn representations) to get to a desired output.  
- **Output layer:** Produces the final result, such as classifying an image, predicting whether a student passes, or generating a continuous value in regression tasks.  

The transformation of values from one layer to the next can be described as:  
$a^{(1)} = \sigma(Wa^{(0)}+b)$, where:
- $a^{(0)}$ is the input layer and $a^{(1)}$ is the first hidden layer.  
- $W$ represents the weights of the connections.  
- $b$ represents the bias term.  
- $\sigma$ is an activation function, which introduces non-linearity.  

How these layers are constructed and connected, is the main deciding factor in how the neural network functions!
- The layer-level architecture and different ways to connect the layers are the fundamental design paradigms of deep learning models. More here: [Deep Learning Paradigms and Building Blocks](Deep%20Learning%20Paradigms%20and%20Building%20Blocks.md).
- The model-level architecture and what different layers are combined in which way, define the overarching architecture types of deep learning models. More here: [Key Architectures in Deep Learning](Key%20Architectures%20in%20Deep%20Learning.md).
## Activation Functions
Activation functions play a crucial role in neural networks by introducing **non-linearity**, allowing the model to learn complex patterns. Without them, a neural network would be just a linear model, regardless of how many layers it has!

We can think of the whole neural network as a list of linear functions (or just one big linear function, if we concatenate them). Now this is linear until we add a small part in the middle, the activation function, which makes the complete process non-linear.

**Example Activation Functions:**
- **Rectified Linear Unit (ReLU)**: This is the standard activation functions for most hidden layers. The function looks like this: $f(x) = \max(0, x)$. This means that if the neuron has a general function of form: $a^{(1)} = \sigma(Wa^{(0)}+b)$, the activation function would look like this: $a^{(1)} = \max(0, Wa^{(0)} + b)$.
- **Sigmoid**: Another popular activation function, especially for binary classification. The function looks like this: $f(x) = \frac{1}{1 + e^{-x}}$.
- **Softmax**: Softmax helps for multi class classification. The function looks like this: $\sigma(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$. Converts raw outputs into probabilities so that each class has a probability score.

