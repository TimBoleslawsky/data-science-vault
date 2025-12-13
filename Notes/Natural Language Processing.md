Natural Language Processing (NLP) studies how computers can analyze, understand, and generate human language. It draws from linguistics, computer science, and machine learning to handle tasks like translation, summarization, and sentiment analysis. Eisenstein introduces NLP as centered around two unifying concepts — _learning_ and _search_ — which underpin most computational methods for language.

The field lies between linguistics and artificial intelligence, using probabilistic and statistical models to connect language data to meaning and decision-making. Despite its variety of tasks, NLP is unified by three central **themes**:
1. **Learning vs. Knowledge:** Balancing data-driven machine learning with structured linguistic knowledge.
2. **Search and Learning:** Combining optimization and inference techniques (e.g., Viterbi, CKY, beam search) with parameter learning (e.g., logistic regression, backpropagation).
3. **Relational, Compositional, and Distributional Perspectives:** Understanding language as structured relations (syntax), compositional meaning (semantics), and statistical co-occurrence (distributional semantics).

The most common tasks within the domain of NLP are autoregressive tasks (more on that here: [Different Task Types for Mathematical Models](Different%20Task%20Types%20for%20Mathematical%20Models.md)). These involve predicting the next token based on previous ones:
- **Language modeling** (predict next word): GPT-style models.
- [Text generation / completion](Generating%20Text%20with%20LLM%27s.md): Write or continue text step by step.
- **Machine translation (decoder side):** Generate target sentence token by token.
- **Speech recognition (in some setups):** Predict next phoneme or word autoregressively.
- [Retrieval-Augmented Generation (RAG)](Retrieval-Augmented%20Generation%20%28RAG%29.md)
- [Topic Modeling](Topic%20Modeling.md)

The two most common architectures that are used for NLP tasks, are RNN's and transformer models. More on these architectures, here: [Key Architectures in Deep Learning](Key%20Architectures%20in%20Deep%20Learning.md).
## NLP Pipeline
Deep learning models are combined with two important concepts to complete the NLP pipelines: [Tokenization](Text%20Preprocessing%20%26%20Tokenization.md) and [Embeddings](Word%20Embeddings.md). Without tokenization, the model wouldn’t know how to break text into processable parts; without embeddings, it couldn’t interpret those parts meaningfully. Here is how the three components work in tandem:

**Step 1 — Tokenization**
- **Goal:** Convert raw text into discrete, standardized units (tokens).
- The tokenizer:
	1. **Splits** text into tokens (words, subwords, or characters).
	2. **Maps** each token to a unique integer ID based on the vocabulary.

**Example:**
Text: “I love NLP.”
→ Tokens: \[“I”, “love”, “NLP”, “.”]
→ Token IDs: \[101, 102, 103, 104]
These IDs are purely symbolic — they contain no semantic meaning yet.

**Step 2 — Embedding Layer**
- **Purpose:** Transform discrete token IDs into **dense numerical vectors** that capture _meaning_ and _relationships_ between words.
- Each token ID corresponds to a **row in the embedding matrix** E ∈ ℝ^(V × d)
	- V: vocabulary size (e.g., 30,000)
	- d: embedding dimension (e.g., 768 for BERT)

The model looks up the vector for each token ID, so the sentence “I love NLP.” becomes a sequence of vectors. Each embedding is a learned representation — during training, the model adjusts these vectors so semantically similar tokens end up close together (e.g., “cat” and “dog”).

**Step 3 — Feeding into the Model** (Contextualize Embedding)
- The embedding vectors form the **input layer** to the neural network (e.g., Transformer, RNN).
- In Transformer models, embeddings are combined with **positional encodings**, which give the model information about word order.
	- Final input = _token embedding + position embedding_.
- The model then computes attention and transformations over these embeddings to produce contextualized representations.

*Note:* This is where *embedding models* stop. They store the contextualized embeddings for further use. The loss we use here can be predictive, but does not have do be!

**Step 4 — Generation / Output (Detokenization)**
- During text generation e.g., the model predicts **token IDs** sequentially.
- Each predicted ID is **decoded** back to a token, and then to human-readable text:
	Token IDs → Tokens → Text string.

**Example:**
Model output: \[101, 105, 106, 104]
→ Tokens: \[“I”, “study”, “NLP”, “.”]
→ Text: “I study NLP.”
## Evaluating Language Models
We can evaluate language models in an *intrinsic* manner (measure model quality directly on linguistic criteria) or in an *extrinsic* manner (measure downstream task performance). The extrinsic metrics are the common metrics we know form other classification tasks (Accuracy, Precision, F1-score, ...). For the intrinstic metrics, the most common one is *perplexity*.
### Perplexity
Perplexity (PP) is the standard **intrinsic evaluation metric** for language models. It measures how well a model predicts a sequence of words and can be interpreted as the model’s _average uncertainty_ or _“surprise”_ when encountering the test data.

$PP(W) = P(w_1, w_2, \dots, w_N)^{-\frac{1}{N}} = \left(\prod_{i=1}^N \frac{1}{P(w_i | w_1, \dots, w_{i-1})}\right)^{\frac{1}{N}}$

This is the **inverse geometric mean** of the predicted word probabilities. Here is what that means: 
- At each step, the model predicts a probability distribution over the vocabulary that **sums to 1** (e.g., “dog”: 0.6, “cat”: 0.3, “fish”: 0.1).  
- But perplexity looks only at the probabilities of the _true_ next words in the test text (e.g., if the true word was “cat”, we use 0.3).
- We then multiply all those “true” probabilities together — or, equivalently, take their **geometric mean** — and invert it to express _how surprising_ the model found the whole sequence.
=> So lower perplexity → model assigns higher probability to the observed data → better fit.

There are three distinct factors that influence perplexity: 
1. **Vocabulary Size** = Fewer possible next tokens make the probability distribution easier to model (less uncertainty).
2. **Domain Mismatch (Train vs. Test Data)** = If the test set contains words, expressions, or syntax not seen in training (e.g., scientific vs. everyday text), $P(w_i | w_{<i}) \downarrow \quad \Rightarrow \quad PP \uparrow$ => The model becomes uncertain and “surprised.”
3. **Treatment of Unseen Words** =  Collapsing many unseen or rare words into a single "unknown" token **lowers perplexity artificially**. Since all unknown words now share the same probability mass, the model predicts the "unknown" token confidently, even though it hasn’t truly learned those words.

These difference in influence can be confusing, so let's look at an example:

Let’s say we have a test sentence: the cat sat on the mat. The model predicts each word with some probability between 0 and 1, so the cross entropy is this: $H = - \frac{1}{6} (\log_2 0.3 + \log_2 0.2 + \log_2 0.15 + \log_2 0.1 + \log_2 0.3 + \log_2 0.05)$. This is roughly $2.7$, $2^2.7$ is roughly $6.5$ - this is the perplexity.

Now if the test sentence is instead: photosynthesis occurs in chloroplasts, it would probably be tokenized into something like this: \<UNK> \<UNK> in \<UNK>. Now depending on with what probability the model predicts “unk”, this changes the perplexity. I think it is reasonable to assume, that this probability is lower than the one shown above, lets say: $H = -\frac{1}{4} (\log_2 0.05 + \log_2 0.05 + \log_2 0.1 + \log_2 0.05)$. This would lead to a perplexity being higher (roughly $17$). 

Now what happens, if we do not use unk-handling is this: The model would predict the unknown words with probability 0 and the perplexity would be infinity. This is never done in modern NLP. But in this case the previous example obviously has a lower perplexity than infinity. 

So if we assume we use a standard model and just switch out the test data, the perplexity would rise with a more domain mismatched test set. If we for some reason would use a model without unk-handling, then we might see higher perplexity with a more complex test set. 

