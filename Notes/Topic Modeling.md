Topic modeling is an unsupervised machine learning task-type used to discover hidden thematic structures in a collection of documents. It identifies topics, where a topic is defined as a probability distribution over words, and associates each document with a mixture of topics.

Key Characteristics:
- Unsupervised: No labeled data is needed.
- Probabilistic: Documents are modeled as combinations of latent topics, and topics are modeled as distributions over words.
- Dimensionality reduction: Helps represent large text corpora in a compact topic-space.
## Latent Dirichlet Allocation
Latent Dirichlet Allocation (LDA) is the **most popular probabilistic topic model**. The end goal is to learn two distributions: 
1. Topic-word distribution: For each topic _k_, LDA learns a probability distribution over all words: φₖ(w) = P(word w | topic k). This tells us: “If you are in topic k, which words are likely to appear?”
2. Document-topic distribution: For each document _d_, LDA learns a probability distribution over topics: $θ_d$(k) = P(topic k | document d). This tells us: “What topics does this document contain, and in what proportions?”

LDA makes two prior assumptions to achieve this:
1. Document–topic distributions $θ_{d}$ follow a Dirichlet prior with parameter $α$: $\theta_d \sim \text{Dirichlet}(\alpha)$.
   This says: "Each document is a mixture of topics, and α controls how _sparse_ or _uniform_ that mixture tends to be."
2. Topic–word distributions $\phi_k$ follow a Dirichlet prior with parameter $β$ $\phi_k \sim \text{Dirichlet}(\beta)$.
   This says: "Each topic is a mixture of words, and β controls whether topics tend to use many words vs. a small focused set."
=> Important: these assumptions are *priors*. The distributions do not follow Dirichlet during inference!

These assumptions lead to the overall generative process of the LDA model. Given that documents are mixtures of topics (θ) and topics are mixtures of words (φ), each word token is created by:
- Picking a topic based on the document: $Z_{dj} \sim \text{Cat}(\theta_d)$
- Picking a word based on that topic: $W_{dj} \sim \text{Cat}(\phi_{Z_{dj}})$
Key parameters for this:
- $\alpha$: Dirichlet prior controlling document-topic sparsity.
- $\beta$: Dirichlet prior controlling topic-word sparsity.
- $K$: Number of topics.

Do achieve this we want the posterior: $P(Z, \theta, \phi \mid W)$. Looking at the Bayes' rule, we can see, that calculating this exactly, is impossible: $P(Z,\theta,\phi \mid w) = \frac{P(Z, w, \theta, \phi)}{P(w)}$. To solve this, we use Gibbs sampling, more here: [[Parameter Estimation for Probabilistic Models#Gibbs Sampling]].

LDA comes in a few different variants: 

| **Variant**                 | **Purpose / Feature**                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------- |
| **Bigram LDA**              | Models sequences of words (n-grams) instead of single words for richer topic semantics.           |
| **Gaussian LDA (GLDA)**     | Uses continuous data features instead of discrete word counts, suitable for embeddings.           |
| **Supervised LDA (sLDA)**   | Incorporates response variables (e.g., document labels or ratings) for supervised learning tasks. |
| **Hierarchical LDA (hLDA)** | Models topics in a hierarchy, capturing sub-topic relationships.                                  |
| **Dynamic LDA (dLDA)**      | Captures how topics evolve over time in a temporal corpus.                                        |