First it is important to distinguish between two things: 
- Turning a word token into a vector in embedding space. 
- Learning the *meaning or context* of a word. 
Usually our NLP models have an architecture that is similar to this: Tokenized Text => Embedding => Contextual Embedding (RNN/LSTM/Transformers/...) => Output. The embedding layer is responsible for the mapping of the word tokens into the vectors of the embedding space. This is usually pretty similar and simple compared to the contextual embedding layer. The contextual embedding layer, is responsible for learning the *meaning or context* of a word, this is usually the focus of modern embedding models and advancements. 

Embeddings are _dense, continuous vector representations_ of discrete symbols (like words or tokens). They serve a similar purpose as one-hot vectors ([Data Encoding](Data%20Encoding.md)]), but allowing neural networks to learn from _geometry_ rather than discrete IDs. They encode semantic or syntactic similarity — words that appear in similar contexts are close in embedding space (cosine(“king”, “queen”) ≈ high).

The basic intuition behind contextual word embeddings is, that meaning can be inferred from usage: “You shall know a word by the company it keeps.” If “dog” and “cat” share similar context words (“pet”, “food”, “fur”), their embeddings should become similar.
## Evolution of Embedding Methods
Here is an overview over different embedding methods and which are used in modern NLP tasks. These methods all focus on the contextual embedding layer!
### Count-Based Embeddings (Statistical Models)
Early models built **co-occurrence matrices** of word–context pairs and compressed them with [dimensionality reduction](Dimensionality%20Reduction.md) methods like **SVD** or **PCA**. These are static, interpretable, but not context-aware.
### Predictive Embeddings (Neural Models)
Word2Vec and GloVe (2013–2015) marked the _neural embedding era_. Instead of counting, these learn embeddings by predicting. They capture linear semantic relationships (e.g., _king − man + woman ≈ queen_). However, each word has only one vector, regardless of context. While neural networks where used in some of these models, they were not recurrent yet!
### Contextualized Embeddings (RNN-Based)
The next step was to capture meaning in context. Here models like ELMo (2018) used RNN's. The advantage of these models is, that a single word can have multiple embedding vectors based on the context around the word. More on RNN's here: [Key Architectures in Deep Learning](Key%20Architectures%20in%20Deep%20Learning.md).
### Transformer-Based Embeddings
The transformer architecture (2017) replaced recurrence with self-attention, allowing parallelized training and better long-range dependency modeling. 

Two main embedding paradigms emerged:
- Autoregressive Transformers (e.g., GPT, 2018– )
	- Use only the **decoder** part of the Transformer.
	- Predict the next token given all previous ones (unidirectional).
	- Excellent for _text generation_ and completion.
- Bidirectional Transformers (e.g., BERT, 2018– )
	- Use the **encoder** part of the Transformer.
	- Train with **masked language modeling (MLM)** so each token can attend to _both left and right_ context.
	- Excellent for _understanding tasks_ (semantic search, classification).

Transformers solved two major RNN/LSTM problems:
1. **Parallelization** — all tokens processed at once (no sequential bottleneck).
2. **Global context** — attention connects distant tokens directly.

The way in which transformers work is a lot more complicated, than described here. More on the transformer architecture, here: [Key Architectures in Deep Learning](Key%20Architectures%20in%20Deep%20Learning.md).
## Embedding Use in Practice
Depending on data and task scale, we either use pre-trained embeddings or train the embeddings ourselves. 

When we train your own embeddings, we use layers like nn.Embedding to create the embeddings and then choose an architecture of our choice and train on the specific vocabulary. This can be useful for demo purposes or if we have a very specific dataset. 

When we use pre-trained embeddings (like GloVe, BERT, ...), we can either replace both the embedding and the contextual embedding layer or just the former. If we do not see any reason in fine tuning the contextual embeddings, we can just feed our text into the pretrained model and take the contextual outputs as embeddings. If we do want to fine tune the pre-existing embeddings, we replace our embedding layer (nn.Embedding) and add our own contextual embedding layer (RNN/LSTM/Transformer/...).

