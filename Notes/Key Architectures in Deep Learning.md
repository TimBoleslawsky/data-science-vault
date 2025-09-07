## Convolutional Neural Networks
CNNs are designed for grid-like data (e.g., images) to detect local patterns (edges, textures, shapes). Instead of flattening an image, CNNs preserve its spatial structure by using filters (kernels) that scan through small patches of the image. For an example of how to do image classification using CNNs, look here [[Image Classification with CNN.py]]. 

Here is how these kernels work. A kernel is basically a small window that is applied on different parts of an image. A kernel could for example look like this: 

```
[[-1, 0, 1],
 [-1, 0, 1],
 [-1, 0, 1]]
```

These weights (-1,0,1) within this kernel are a representation of a pattern and are learned in the training process. In a convolutional layer we now apply multiple of these kernels to detect multiple local patterns. 

By taking the output of one convolutional layer as input to the next convolutional layer, we can increase the receptive field of the model even thought the size of the kernels stays the same (usually 3x3). By increasing the receptive field the complexity of the patterns we can detect also grows (e.g. from *edge* to *eye*).

This whole process is just the feature extraction. We can think of it like this: The convolutional layers extract that the image contains two eyes, a nose, hair, ... and so on. These features are the input for the fully connected layer which then classifies the image based on these features.
### Subsampling in CNNs
 The core idea behind all subsampling methods is to reduce the spatial size of the feature maps (i.e., the height and width). One popular one is pooling.

The pooling layer serves to downsample the feature maps produced by the convolutional layers. It reduces the spatial size (height × width) of the input feature map, keeping only the most important information. This increases translation invariance — slight translations or distortions in the image don’t affect the output significantly.
- Common types of pooling:
	- Max pooling: Keeps the maximum value in each region.
	- Average pooling: Takes the average of the values in the region.
### Architecture of CNNs
The basic architecture of CNNs follows this principle:
- Convolutional layer, for feature extraction as described above.
- Subsampling, to reduce the spatial size of the feature maps.
  => These two follow each other for how many layers we want.
- Fully connected layer, for the final classification task (like an FNN layer).
## Recurrent Neural Networks
We can think of RNNs as FNNs reused across time steps, with shared weights. That reuse is what gives RNNs the ability to learn temporal dependencies. Therefore they are especially relevant in time series analysis. TBD
## **1. Predictive Models (input → Output mapping)**

**Goal:** learn statistical patterns to make predictions.

- **Base architectures:**
	
	- MLPs
		
	- CNNs (+ ResNet, U-Net, RCNN)
		
	- RNNs (+ LSTM, GRU)
		
	- Transformers (+ BERT, GPT [in predictive contexts], ViT)

---

## **2. Generative Models (learn Distribution, Create data)**

**Goal:** capture data distribution and generate new samples.

- **Base architectures inside them:**
	
	- CNNs (GANs, VAEs for images)
		
	- Transformers (diffusion, text generation, multimodal models)

---

TBD