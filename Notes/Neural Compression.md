Neural compression is the use of neural networks to implement or improve both **lossless and lossy compression**. The idea is to leverage the representation learning and generative modeling capabilities of modern networks to:
- Learn **efficient latent representations**
- Model **probabilities of latent or raw data**
- Perform **entropy coding** more effectively
- Enable both high-fidelity reconstruction and low bitrate
## Differentiating Neural Compression and Dimensionality Reduction
The two concepts neural compression and dimensionality reduction can seem pretty similar, as they are both part of the larger representation learning task group. The aim of dimensionality reduction is to map high-dimensional data into a lower-dimensional continuous space without concern for bitrates, quantization, or entropy. Its goal is to preserve *geometric or statistical* structure (variance, manifold structure, local neighborhoods). Neural compression is fundamentally a communication problem: how to *minimize bits while preserving information relevant to a target* (usually reconstruction, sometimes a downstream task).
## History Of Neural Compression
Neural compression evolved naturally from advances in representation learning and generative modeling. Early neural networks focused on reconstruction, but as probability modeling improved, true compression became possible.

Autoencoders (1980s-2000s) introduce the idea of using models to learn a latent representation of $z = f(x)$ from input data $x$. At this point, this is basically just dimensionality reduction and no probability modeling of latent variables, so we cannot entropy-code (no “real” compression). => Autoencoders showed that neural networks can learn compact representations, laying the groundwork for modern neural compression.

Variational autoencoders (2013-2015) learn a specific latent distribution, which connects neural representation learning to the rate-distortion theory introduced by information theory. This enables first advances in learned latent distributions that can support real compression (usually lossless here). Another advancement which was introduced around the same time are autoregressive models. These models explicitly model the joint probability of the data: $p(x) = p(x_1) \cdot p(x_2|x_1) \cdot p(x_3|x_{1:2}) \dots$, which is perfect for lossless compression when paired with entropy coders like ANS or arithmetic coding.

Large-scale self-supervised learning models (2018–present) like transformers, MAEs and diffusion models enabled two main advancements specific to lossy compression:
- **Better latent representations** → lower bitrate for same distortion
- **Improved probability modeling** → more efficient entropy coding
These models build the backbone of modern neural lossy compression research!
## Neural Lossless Compression
Neural lossless compression builds upon the established compression pipeline present in information theory (more detail here: [[Foundations of Information Theory]]): 
- Model data distribution <= Here is where neural compression comes in!
- Entropy-code the symbols <= This remains largely the same!

Neural lossless compression extends this by **learning the probability model with a neural network**. These three design principles are relevant here (more on them here: [[Deep Learning Design Patterns]]):
- **Latent variable models** (VAEs, bits-back) → encode latent codes efficiently
- **Normalizing flows** → learn exact, invertible transformations $f(x)$ with tractable likelihoods
- **Autoregressive models** → model exact probabilities for sequences or images
=> These models feed entropy coders ([[Foundations of Information Theory#Entropy Coding and Lossless Compression]]) to produce near-entropy-optimal codes and allow data-driven modeling of distributions, surpassing hand-engineered statistical models.
## Neural Lossy Compression
Just like neural lossless compression, neural lossy compression builds upon a pipeline established by information theory (more detail here: [[Foundations of Information Theory]]): 
- Decorrelation strategy
- Model distribution 
- Entropy coding

Here is where neural networks can improve upon this pipeline:
- Transforming in the decorrelation strategy: A neural network (often a convolutional neural network, autoencoder, or other architecture) “learns” a transform that maps input to a compact latent representation.
- Modeling the distribution: Neural compressors often learn a probability model (latent distribution / entropy model) over the quantized latents. This allows more accurate entropy coding.
  => Quantization in the decorrelation strategy and entropy coding remain largely the same!