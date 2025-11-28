## Encoder–Decoder Pattern
The encoder-decoder pattern introduces the *encoder model* and the *decoder model*. The encoder compresses the input into a latent representation (a compact, informative summary). The decoder generates the output from the latent representation.

Key points:
- Separates input processing (encoder) from output generation (decoder).
- Works naturally for sequence-to-sequence tasks like text, but also for images, graphs, etc.
- Often paired with attention mechanisms to allow the decoder to look back at the input.

Below is a more detailed description of the encoder and decoder models, the encoder-decoder model just combines these two concepts in one model! Encoder-decoder models are sometimes also called *sequence-to-sequence or seq2seq* models. This refers to the task type they are usually applied to: [[Different Task Types for Mathematical Models]].
### Encoder Models
Encoders are models that take input data and produce a latent representation. Their structure is as follows: Input → Layers (e.g., CNN, RNN, Transformer encoder) → Latent vector(s). Encoders do not generate the final output themselves; they just encode the input into a representation.

Examples:
1. **RNN Encoder:** reads a sequence token-by-token → outputs final hidden state
2. **CNN Encoder:** extracts feature maps from an image → global feature vector
3. **Transformer Encoder:** stack of self-attention layers → contextual embeddings for each input token
### Decoder Models
Decoders are models that generate output from a latent representation. Their structure is as follows: Latent representation → Layers → Output. Decoders often condition on latent information and may also use autoregression or other sequential generation methods.

Examples:
1. **RNN Decoder:** generates one token at a time, often autoregressively, optionally attending to encoder outputs
2. **CNN Decoder:** generates images, e.g., in autoencoders or GAN generators
3. **Transformer Decoder:** generates tokens using self-attention + cross-attention to encoder outputs
## Autoencoders
Autoencoders use a very similar architecture to the encoder-decoder models, but they are trained to reconstruct the input, whereas encoder–decoder models generally translate from one representation to another. Importantly, autoencoders learn a latent representation by reconstructing its own input, so training target = input. That is not the case in encoder-decoder models, where task-specific outputs are expected. 

An autoencoder is in its most basic sense a neural network trained to copy its input $x$ to its output (reconstruction) $r$. Internally, it passes through a “code” or latent representation $h$. In formula: $h = f(x), r = g(h)$, where $f$ is the encoder, $g$ the decoder. Two important clarifications: 
- The hope isn’t just to copy — but that the network learns a representation $h$ that captures **meaningful structure** of the data. To make this happen, autoencoders are typically constrained so they _can’t_ simply learn the identity function. 
- Training is done by minimizing a **reconstruction loss** $L(x, g(f(x)))$, for example mean squared error (MSE) between original input and reconstruction.

Traditional autoencoders are usually used for dimensionality reduction or feature learning!
### Variational Autoencoders
Variational autoencoders (VAEs) extent the classic assumption “Given $x$, compute a single code $h$, then reconstruct a single $\hat{x}$.” to a probabilistic one “Given $x$, infer a _distribution_ over latent variables $z$. Given $z$, infer a _distribution_ over possible $x$.” So very basically, instead of a deterministic function that maps $x$ to $h$ and $h$ to $z$, we assume there is a conditional probabilistic distribution that does this. This idea is borrowed from *latent variable models* (which VAEs are, but is a broader category). More formally latent variable models like VAEs assume:
1. There is an unobserved latent variable $z$.
2. The observed data are generated from a conditional distribution $p(x \mid z)$.
3. Learning involves inferring the posterior $p(z \mid x)$.

While VAEs can also be used for representation learning, the primary design goal is _generative capability_. We generate new data by sampling from the latent space $z \sim p(z)$ and decoding.
### Masked Autoencoders
We can view MAEs as masked self-supervision, which is builds on the same principle as autoregressive modeling in that both predict missing information from context.

The main idea is, that they apply massive masking to the input. For example:
- mask 75% of image patches.
- only feed the remaining 25% into the encoder, the encoder never sees the full input. This makes the encoder very lightweight.
- decoder reconstructs the missing patches
This were the similarities with autoregressive modeling lay! This is also were the difference to VAEs is, the latent space is not a probabilistic latent variable.

MAEs are used for representation learning tasks like embedding or compression. By masking large portions of the input, the network must capture global structure and semantic relationships to reconstruct the missing parts, which is helpful for exactly these kinds of tasks. 
## Autoregressive Models
Autoregressive models use a sequential design pattern, where the network predicts the next element in a sequence given previous elements. Unlike autoencoders, where the network reconstructs the entire input from a latent code, autoregressive models **factorize the joint probability of a sequence into a product of conditional probabilities**:

$p(x_1, x_2, \dots, x_T) = \prod_{t=1}^{T} p(x_t \mid x_1, \dots, x_{t-1})$

So very basically, instead of trying to reconstruct its own input or infer a latent distribution, the model is trained to **predict the next part of the data given what it has seen so far**.

**Key points:**
- The network is trained **with the target = next element in sequence**, not the input itself.
- Architecturally, autoregressive models can be implemented with **RNNs, LSTMs, Transformers, or causal convolutional networks**, depending on the domain.
- Training is done by **maximizing the likelihood** (or minimizing negative log-likelihood) of each element given its context:
	$\mathcal{L} = -\sum_{t=1}^{T} \log p_\theta(x_t \mid x_1, \dots, x_{t-1})$

**Conceptual intuition:**
- The model learns **how sequences are structured**, capturing temporal or spatial dependencies.
- By predicting the next element, it can generate new sequences **autoregressively**: starting from an initial token, the model predicts the next, appends it to the context, predicts the following one, and so on.
- This makes autoregressive models particularly strong for **generative tasks in sequences**, such as:
	- Text generation (e.g., GPT)
	- Audio synthesis (e.g., WaveNet)
	- Time series forecasting

**Relation To Masked Prediction / MAEs:**
- Like masked autoencoders, autoregressive models predict **missing information from context**, but with a key difference:
	- **Autoregressive models are sequential**, predicting one element at a time from previous elements.
	- **MAEs predict multiple masked elements in parallel**, not necessarily in sequence.
- Both methods are **self-supervised**, in that the network learns from parts of the input without external labels.
## Normalization Flows
Instead of learning a latent variable model with an **intractable posterior** (as in VAEs), normalizing flows learn **exact probability distributions** by constructing an invertible mapping:
$z = f(x), x = f^{-1}(z)$. Very basically, this works like so: 
- $z$ is drawn from a simple prior $p_Z(z)$.
- $x$ is a data point.
- we apply $f$ is an invertible transformation (a “flow”) to $x$ to get $z$. The idea is, that flow is a chain of invertible functions: $f = f_K \circ f_{K-1} \circ \dots \circ f_1$, which is applied to $x$ until we get to $z$, which corresponds to a simple distribution. The functions correspond to layers in the neural network (implemented using specific *flow layers*). The nice thing about this, is that they are invertible. This enables for example lossless compression or sampling/generation, because we can retrace our exact steps. 
## Diffusion Models
Diffusion models are a class of **generative models** that learn to reverse a gradual noising process. Unlike VAEs (probabilistic latent variable models), autoregressive models (sequential factorization), or normalizing flows (invertible transformations with exact likelihood), diffusion models model data generation as **denoising a signal step-by-step**.

The core idea is this: we slowly destroy structure in the data by adding noise, and then train a neural network to reverse this process. This means diffusion models can be viewed as two separate processes. 
1. The forward process (diffusion / corruption)
	- You start from a data point $x_0$.
	- You gradually add Gaussian noise over T steps: $q(x_t \mid x_{t-1}) = \mathcal{N}(x_t; \sqrt{1 - \beta_t}\, x_{t-1}, \beta_t I)$
	- After many steps, $x_T$ is essentially pure noise.
	=> Two important properties:
		- The forward process is **fixed** (not learned).
		- Because it is Gaussian, we can jump directly from $x_0$ to any step $x_t$ analytically.
2. The reverse process (denoising / generation), a neural network $\varepsilon_\theta(x_t, t)$ is trained to reverse the diffusion:
	- The network predicts the noise that was added at step $t$ (this is essentially the training objective).
	- Using this predicted noise, you denoise a little bit.
	- Repeat for all steps from $T \to 0$.
	=> This gradually reconstructs a clean data sample. Essentially, the model learns: “What clean data looks like at different noise levels.”

This is applied to two main use cases: sampling/generating and compressing
1. Sampling:
	- Sampling starts from pure noise $x_T \sim \mathcal{N}(0, I)$, then iteratively denoises: $x_{t-1} = \text{denoise}(x_t, \varepsilon_\theta)$
	- Eventually, we reach $x_0$, a generated sample.
2. Compression: 
	- Diffusion models can be used for _neural compression_ because they are extremely good at reconstructing clean data from **corrupted or partial information**. The key idea is: Instead of storing the full data, we store a compact latent (or even a highly corrupted version of the data), and let a diffusion model denoise and reconstruct it during decoding.
	There are two common approaches how diffusion models are used in compression:
	1. Latent Diffusion Compression: The key intuition is, that the diffusion happens inside the bottleneck of an autoencoder. So we can think of the autoencoder to be wrapped around the diffusion model:
	   - **Encoder:** compresses the image into a small latent space.
	   - **Diffusion model:** operates only in that latent space, gradually denoising or generating a plausible latent code.
	   - **Decoder:** maps the refined latent back to the original high-resolution pixel space.
		=> We do this, because it is computationally efficient, compared to doing diffusion directly in pixel space. 
	2. "Noisy Code" Compression: Here we only use a diffusion model to intentionally store a **noised version** of the e.g. the image. This noised image can then be quantized and stored efficiently because it has reduced structure. At decoding time, the diffusion model runs the reverse-denoising steps to recover $x_0$.
## Generative Adversarial Networks (GANs)
Generative Adversarial Networks (GANs) approach generative modeling through **adversarial learning**: two neural networks compete in a zero-sum game. One network tries to generate realistic data, while the other tries to detect fakes. Through this competition, the generator learns to produce highly realistic samples.

This means, that GANs consist of two components:
1. **Generator** $G(z)$
	- Takes a random vector $z \sim p(z)$ (usually Gaussian or uniform).
	- Produces a sample $x = G(z)$ meant to resemble real data.
	=> The generator tries to minimize this ability by producing realistic samples.
2. **Discriminator** $D(x)$
	- Takes an input (real or generated).
	- Outputs a scalar representing the probability that the input is **real** rather than fake.
	=> The discriminator tries to maximize its accuracy at detecting real vs fake.
The two networks are trained simultaneously with **opposing objectives**. When training succeeds, the generator distribution matches the data distribution.

This is applied to e.g. generation and compression tasks. But, while this is a highly effective and efficient strategy, the big problem with GANs is, that they can easily hallucinate!