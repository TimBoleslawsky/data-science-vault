The paradigms described here are high-level design principles that can appear in many architectures often combined with one another. The architectures themselves are concrete instantiations of these paradigms for specific tasks or purposes.
## Attention Mechanisms
The idea of *attention* is, that it allows the model to focus on relevant parts of the input when producing each output. Here is how a standard attention layer or *head* works in e.g. transformer models: 
1. We start with a simple embedding layer. These embeddings turn tokens into vectors but do not have inherent meaning in the beginning. The embeddings could look like: cat = \[1,0,0,...], mat = \[0,1,0,0,...], and so on. 
2. We now want to compute three matrices: $Q$, $K$, and $V$. Here is what these matrices represent: 
	- The query $Q$ represents “what matters to me?”
	- The key $K$ represents “what I contain?”
	- The value $V$ represents "what content I pass along to elements that attend to me?"
	The "meaning" is implicit in the following dot products of the embeddings and the learnable vector $W$: 
	- $\mathbf{q}_i = W^Q \mathbf{x}_i$
	- $\mathbf{k}_i = W^K \mathbf{x}_i$
	- $\mathbf{v}_i = W^V \mathbf{x}_i$
3. Using the matrices, we now compute the attention scores. For example for the word "cat" this could look like this: 
	- $\text{score}_{\text{cat,cat}} = \mathbf{q}_{\text{cat}} \cdot \mathbf{k}_{\text{cat}}$
	- $\text{score}_{\text{cat,mat}} = \mathbf{q}_{\text{cat}} \cdot \mathbf{k}_{\text{mat}}$
	- ...
	The goal is to learn the vector $W$ such that: 
	- $\mathbf{k}_{\text{cat}} \cdot \mathbf{q}_{\text{something}}$ is large for queries that should attend to “cat”.
	- $\mathbf{q}_{\text{cat}} \cdot \mathbf{k}_{\text{something}}$ is large for queries where "cat" should attend to the word.
	- $\alpha_{i,j} \cdot \mathbf{v}_j$ provides the correct amount of information from $j$ to $i$.
4. Apply softmax to the attention scores to get attention weights $\alpha_{i,j}$. These just tell us with what probability one word should pay attention to another. 
5. Compute the weighted sum to get new context-aware embeddings: 
	- We do this by multiplying $\alpha_{i,j}$ with each matrix $v_j$. For example: $\mathbf{z}_{\text{cat}} = \sum_j \alpha_{\text{cat},j} \mathbf{v}_j = 0.27 \cdot [1,0] + 0.58 \cdot [0,0] + 0.21 \cdot [0,1]$
	=> This produces a new context-aware embedding, e.g.: $\mathbf{z}_{\text{cat}} = [0.27, 0.21]$.
### Self-Attention
Self-attention means, that each token attends to other tokens in the same sequence, including itself. Q, K, V all come from the same set of embeddings (the same sequence). Purpose is to make each token context-aware by aggregating information from its neighbors.

Masked self-attention is a variant of self-attention, where each token is prevented from attending to future tokens. This is done by adding a mask to the attention scores before softmax:Intuition: when predicting the next word in a sentence, the model should not peek at future words. We do this to ensure causality in generation.
### Cross-Attention
Cross-attention means, that each token in a “target” sequence attends to tokens in a different sequence (often called the “source”). Q comes from the target sequence, K and V come from the source sequence. Purpose here is to allow the target to incorporate relevant information from the source.
## Recurrence
**Idea:** Processes sequences **step by step**, maintaining a **hidden state** that summarizes past inputs.
- **Core principle:** Output at step t depends on input at t and hidden state from t-1.
- **Variants:**
	- Vanilla RNN
	- LSTM (long-term memory)
	- GRU (simpler, fewer parameters)
- **Purpose:** Captures sequential dependencies in time-series, text, or speech.
- **Limitation:** Harder to parallelize; can struggle with long-range dependencies
## Convolutional Processing
**Idea:** Exploits **local structure** in data (e.g., images, audio) via **filters/kernels** that slide over the input.
- **Core principle:** Apply shared kernels to detect local patterns → build hierarchical features.
- **Components:**
	- Convolution layers
	- Pooling layers (downsampling)
	- Optional normalization or residual connections
- **Purpose:** Efficiently capture spatial or temporal hierarchies; translation-equivariant
- **Used in:** CNNs, UNet, ResNet, video/audio processing
=> Input → Convolution → Activation → Pooling → Feature maps → Next layers! 
## Residuals
**Idea:** Allow layers to learn _refinements_ instead of complete transformations by adding the input of a layer back to its output. A residual block computes: $\text{output} = x + F(x)$; where $F(x)$ is a learnable transformation (e.g., a few layers of a network).

**Core principle:** The model learns the _difference_ from the identity mapping, not the full mapping. This greatly stabilizes training in deep networks.

**Why it works:**
- Helps gradients flow backwards without vanishing
- Allows very deep networks (50–1000+ layers) to train reliably
- Encourages layers to make small, meaningful updates to representations
- Prevents degradation, where deeper networks perform worse than shallow ones

**Used in:**
- ResNets (origin)
- Transformers (every attention and feed-forward sublayer)
- Many modern architectures across vision, NLP, and multimodal models

=> Residuals act as “shortcut paths” that make optimization easier and enable very deep neural networks to converge.