Information theory answers a few important questions: How is information defined, and how can we capture uncertainty? How can we compress information in a lossless and lossy way? What characteristics does information have, when communicating via a channel? 

In this note, I will focus on the foundations, lossless compression, and lossy compression. Communication and Channel theory is not relevant to my work. 
## Foundations
Firstly, we need to introduce *information entropy*. Entropy measures the uncertainty of a random variable and is computed from its probability distribution. More specifically: the uncertainty contained in a probability distribution is the average log-probability of an event. And here is the formula for it: $H(p) = - \sum_i p_i \log p_i$.

Let's look at an example: To compute the information entropy for the weather, suppose the true probabilities of rain and shine are $p_1 = 0.3$ and $p_2 = 0.7$, respectively. Then: $H(p) = −(p_1 log(p_1) + p_2 log(p_2)) ≈ 0.61$. Suppose instead we live in Abu Dhabi. Then the probabilities of rain and shine might be more like $p_1 = 0.01$ and $p_2 = 0.99$. Now the entropy would be approximately $0.06$. Therefore there’s much less uncertainty about any given day, compared to a place in which it rains 30% of the time. It’s in this way that information entropy measures the uncertainty inherent in a distribution of events. 

Here is how that influences compression: 
- High-entropy data is less predictable → harder to compress.
- Low-entropy data has redundant patterns → easier to compress.
=> Entropy gives the **lower bound** (in bits per symbol) for _any_ lossless coding scheme. (Side note: Depending on what logarithm base we use, the unit of entropy changes. If we use log₂, then we measure in bits (usually done in information theory), if we use ln, then we measure in natural units (sometimes used in physics, statistics, or ML theory))
### Cross Entropy and Divergence
On question we want to answer with information theory is: *"How can we use information entropy to say how far a model is from the target?"*. The key lies in *divergence*. 

Before talking about divergence, we need to introduce *cross entropy*. Suppose the true distribution is $p$, but we approximate with a model distribution $q$. The cross-entropy is: $H(p, q) = - \sum_i p_i \log q_i$. This is the expected log-loss we suffer when reality is distributed as $p$, but we assign probabilities according to $q$. Or if we want to express it in compression terms, the average number of bits needed to encode samples from $p$ using a code optimized for $q$. Cross entropy is often used as a loss function in ML models and importantly is an upper bound on the true entropy. 

The *Kullback–Leibler (KL) divergence* is now just the difference between cross-entropy and entropy: $D_{\text{KL}}(p \,\|\, q) = H(p, q) - H(p) = \sum_i p_i \log \frac{p_i}{q_i}$. This can be interpreted as the additional bits required when $q$ is used instead of $p$ or how “far apart” two probability distributions are.
### Deviance
The above sounds nice, but unfortunately, we rarely know the true $p$, so we can’t compute KL divergence directly. That means we need an estimator relative KL divergence between the true generating process and the model $q$. That is *deviance*. 

The idea here, is that if we compare models relatively much of $p$ cancels out. What matters is each model’s average log-probability of the observed data. So we can compare the average log-probability from each model to get an estimate of the relative distance of each model from the target.

This is called a *log-probability score* or a *log-pointwise-predictive-density* in a Bayesian model (because we have to take the whole posterior distribution into account). Deviance is now just like a lppd score, but multiplied by $−2$ so that smaller values are better (2 for historical reasons).
## Entropy Coding and Lossless Compression
The general goal of lossless compression is, to represent data using as few bits as possible *without losing information*. The main idea is to assign shorter codes to more probable outcomes, longer codes to rare outcomes. The best possible lossless compression approaches entropy!

Common approaches include:
- Hufmann coding, symbol code that works with Hufmann trees.
- Arithmetic coding or range coding, is a streaming code. Streaming codes differ from symbol code in that they assign codewords to entire messages and individual symbols do not have unique codewords
- Asymmetric Neural Systems (ANS), modern alternative to arithmetic coding. Used in most neural compression systems due to speed and parallelism.

This leads to the following general pipeline for lossless compression after Shannon’s source coding theorem:
1. Model the data distribution. The model gives us an estimate of the true probability distribution $p(x)$. Could be hand-engineered (e.g., statistical counts, prediction, context models) or could be learned (in modern [[Neural Compression]]).
2. Entropy-code the symbols (Huffman, arithmetic, ANS). The **entropy coder** produces a code whose expected length is close to $H(p) = -\sum p(x)\log_2 p(x)$ aka. the entropy.
## Lossy Compression
The goal of lossy compression is to compress data with some allowed distortion while minimizing bitrate. So in contrast to lossless compression, we allow distortion to reduce bitrate by discarding “irrelevant” or “imperceptible” information. Another difference to lossless compression is, that lossy compression is not governed by entropy, but by **rate–distortion theory**. 

Rate-distortion theory defines the minimum average number of bits per symbol needed to encode $X$ with distortion ≤ $D$. This means we have an inherent trade-off between bitrate and quality! The distortion measure can be chosen freely and determines $R(D)$ as well as practical codec behavior (although MSE is a common choice).

This changes the general pipeline introduced for the lossless compression: 
- **Decorrelation strategies:** The goal here is to reduce redundancy / decorrelate the signal, which leads to lower entropy, which enables more efficient entropy coding.
- **Model distribution:** Estimate probability distribution of quantized coefficients. Largely the same as before, just using different input.
- **Entropy coding:** This stays largely the same as before (Huffman, arithmetic, ANS).
So the main change is the addition of the decorrelation strategy, why do we do this? To understand, we must introduces *quantization*.
### Quantization
Quantization is the process of mapping a **continuous or high-precision signal** to a **finite set of discrete levels**, usually integers, so it can be represented using a limited number of bits. A very simple example is the uniform quantizer (most common scalar quantizer):
- Quantization step size: $\Delta$
- Map each input $z$ to the nearest multiple of $\Delta$: $Q(z) = \Delta \cdot \text{round}\left(\frac{z}{\Delta}\right)$

There are three reason, why quantization is essential for lossy compression: 
1. Quantization is what actually reduces the precision of the signal. It introduces controlled distortion.
2. Most entropy coders (Huffman, arithmetic, ANS) only work on discrete symbols. Quantization converts continuous-valued coefficients into integers that can be encoded as bits. 
3. Introducing rate control, the coarser the quantization (larger $\Delta$), the fewer bits needed.

Quantization can be done in three main ways: 
- Scalar Quantization (most common): Each coefficient is quantized independently. This is quite simple and efficient, if done after a transform step. Simple JPEG or MP3 do this.
- Vector Quantization (less common): Maps multi-dimensional vectors to a codebook of representative vectors. Can theoretically minimize distortion for a given bitrate, but is very computationally expensive.
- During training of [[Neural Compression]]: This has become in modern approaches, where we use training tricks to optimize the rate-distortion objective end-to-end.
### Decorrelation Strategies
As said above, the introduction of these is the main difference between lossless and lossy compression, so why do we do this? The high level intuition is, we do this to reshape the data so that quantization throws away the least important information for a given distortion measure. As we introduce above, quantization is the _only_ part of lossy compression that actually removes information.

If we quantize the raw data directly:
- important structure gets damaged.
- distortion becomes large.
- the rate–distortion trade-off is poor.
=> So instead we normalize to turn correlated data into uncorrelated components. Very basically, we create a linear or nonlinear mapping that spreads out information so each component is simpler.

The most common strategies to do this are discussed below. The choice which strategy to use, depends on computational resources, data structure, and latency requirements.
#### Vector Quantization
NOTE: This is technically also a decorrelation strategy, but often infeasible in practice. More common are the transform + scalar quantization alternatives described below!

Vector Quantization (VQ) is a decorrelation and compression strategy that maps input vectors to the closest points in a finite codebook.
- **How it works:** The encoder chooses the nearest codebook vector for each input vector, and the decoder reconstructs the input from that codebook entry.
- **Key idea:** By clustering similar input vectors, VQ removes redundancy and compresses the data efficiently.
- **Pros:** Theoretically optimal if codebook size is large enough; directly minimizes distortion for a given bitrate.
- **Cons:** Exponentially expensive in high dimensions; impractical for large data without structured approximations.
#### Transform Encoding
Transform coding applies a linear or nonlinear transform to the data to decorrelate it and concentrate its “energy” into fewer components.
- **How it works:** An analysis transform $f$ maps the input $x$ to coefficients $z = f(x)$. Then scalar quantization is applied to each coefficient independently ($\hat{z} = [[z]]$). 
- **Key idea:** By decorrelating the data, transform coding allows simple scalar quantization to approximate the optimal vector quantization, making compression computationally feasible.
- **Examples:** DCT in JPEG, wavelet transforms in JPEG2000, learned transforms in neural compression.
#### Predictive Encoding
Predictive coding removes redundancy by predicting each data point from previously encoded points and encoding only the residual.
- **How it works:** For a sequence $x_t$, a predictor estimates $\hat{x}t = P(x{<t})$, and the residual $r_t = x_t - \hat{x}_t$ is quantized and entropy-coded.
- **Key idea:** Residuals are smaller and less correlated than the original data, leading to lower entropy and more efficient compression.
- **Examples:** DPCM in audio, PNG scanline prediction in images, motion-compensated prediction in video.
