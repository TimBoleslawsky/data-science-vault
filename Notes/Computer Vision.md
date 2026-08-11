Computer Vision (CV) studies how computers can **perceive, interpret, and reason about visual data** such as images and videos. It lies at the intersection of signal processing, geometry, physics (optics), and machine learning, with modern approaches dominated by deep learning.

Unlike NLP, where inputs are discrete symbols, CV operates on continuous, spatially structured signals. The core challenge is learning representations that are invariant (to translation, scale, illumination) while remaining discriminative for downstream tasks.

CV tasks are typically **non-autoregressive**, operating on full images or frames at once, though some video and generative tasks introduce temporal or sequential structure.
## Most Important Tasks in Computer Vision
**Image Classification**: Here the goal is to assign a single semantic label to an entire image. Image classification is the **foundational task** in computer vision. The model learns a global representation of an image and maps it to one of _K_ predefined classes. Spatial structure is used implicitly during feature extraction but discarded in the final prediction.

From an engineering perspective, classification:
- Is the simplest CV task in terms of labeling and evaluation.
- Serves as the **pretraining objective** for many CV backbones (e.g., ImageNet).
- Produces compact embeddings useful for transfer learning and retrieval.

In this Github repo is an example of a image classification project: https://github.com/TimBoleslawsky/image-classification-with-cnns.

**Object Detection**: The goal of object detection is to locate and classify multiple objects within an image. Object detection extends classification by introducing **localization**. Instead of one global label, the model predicts a variable number of objects, each with a class label or a bounding box.

From an ML engineering standpoint this is much more complex due to structured outputs and requires post-processing steps. 

**Semantic Segmentation**: Here to goal is to assign a class label to every pixel in the image. Semantic segmentation represents the **most fine-grained level of visual understanding** among the three. The model performs dense prediction, producing a full-resolution label map aligned with the input image. Unlike object detection, object instances are not distinguished. The focus is on **scene understanding** rather than object counting.

In this Github repo is an example of a semantic segmentation project: https://github.com/TimBoleslawsky/semantic-segmentation.
## Core Architectures in Computer Vision
The dominant architectures in CV encode spatial structure explicitly:
- **Convolutional Neural Networks (CNNs):**
	- Convolutions enforce **local connectivity** and **weight sharing**.
	- Pooling or striding provides **translation invariance**.
	- Deep hierarchies learn increasingly abstract features.
- **Vision Transformers (ViTs):**
	- Treat images as sequences of patches.
	- Use self-attention to model **global context**.
	- Rely less on hard-coded inductive bias, more on data scale.
- **Hybrid Models:**
	- Combine convolutions for locality with attention for global reasoning.
## Computer Vision Pipeline
Unlike for example NLP tokens, pixels already contain numeric meaning. Therefore we have the three steps of feature extraction (embedding), task-specific heads, and output interpretation in usual CV projects.
### Feature Extraction (Embedding)
Here the model maps images to dense feature representations: Early layers capture edges and color gradients; Mid-level layers capture textures and parts; Deep layers capture objects and semantics.

The output from this can be either a **global embedding vector** (classification, retrieval) or a **spatial feature map** (detection, segmentation). This output (the learned features) play an analogous role to the embeddings in NLP tasks, but they are spatially structured and learned end-to-end without a discrete vocabulary. 
### Task-Specific Heads
On top of shared visual features, task-specific heads are applied:
- **Classification head:** Fully connected + softmax.
- **Detection head:** Bounding box regression + classification.
- **Segmentation head:** Pixel-wise classifiers (often with upsampling).

The same backbone can serve multiple tasks, which is central to **transfer learning** in CV.
### Output Interpretation
Outputs are mapped back to human-interpretable structures like class labels or masks. This means that post-processing is often required.