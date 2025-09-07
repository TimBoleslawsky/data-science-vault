## What is RAG?
RAG is a technique used in artificial intelligence, particularly in natural language processing, to improve the quality and relevance of generated responses by combining two components:
1. **Retrieval**: A retrieval module fetches relevant information or documents from an external database or knowledge base based on a query or context.
2. **Generation**: A generative language model uses the retrieved information to produce a coherent and contextually appropriate response.

This approach leads to the main feature of RAG: **Dynamic Knowledge Integration**. Instead of relying solely on pre-trained knowledge, RAG retrieves real-time, external information to enhance accuracy and relevance.
## How Does RAG Work?
We need two models, to make RAG work: 
- **Embedding Model**: This model transforms text into numerical representations (vectors) that capture semantic meaning. These embeddings are used to store and retrieve information efficiently in a **vector store**. This model ensures that the system can find the most relevant information (e.g., matching query to notes).
- **Text Completion Model**: This is a generative model designed to produce coherent and contextually relevant text based on a given input or prompt. This model ensures that the retrieved information is presented in a natural and coherent way.

The steps we need to do are: 
1. Use the **embedding model** to process your notes and convert them into numerical vectors that capture their semantic meaning. Embedding model output: A vector like [0.12, -0.45, 0.89, ...].
2. Store these vectors in a **vector database**.
3. The embedding model processes this query into a vector like [0.10, -0.40, 0.85, ...]. The query vector is matched against the stored vectors in the vector database to find the most semantically similar notes.
4. The retrieved note is passed to the **text completion model**, which crafts a user-friendly response.