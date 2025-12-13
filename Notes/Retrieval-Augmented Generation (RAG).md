RAG is a technique used in artificial intelligence, particularly in natural language processing, to improve the quality and relevance of generated responses by combining two components:
1. **Retrieval**: A retrieval module fetches relevant information or documents from an external database or knowledge base based on a query or context.
2. **Generation**: A generative language model uses the retrieved information to produce a coherent and contextually appropriate response.

This approach leads to the main feature of RAG: **Dynamic Knowledge Integration**. Instead of relying solely on pre-trained knowledge, RAG retrieves real-time, external information to enhance accuracy and relevance. Here is an example of how to implement RAG: [RAG for Obsidian](RAG%20for%20Obsidian.md).
## **How Does RAG Work?**
To make RAG work, we need two things:
- **A retrieval method**
- **A text generation model**
The retrieval step can be implemented in **two major ways**, sparse retrieval and dense retrieval. The generation step usually is pretty standardized. 
### Sparse Retrieval (e.g., BM25, TF-IDF)
Sparse retrieval represents documents as **bags of words**, focusing on exact term overlap. That means, that:
- No embeddings, no neural network.
- Works by matching query words with document words.
- Very fast, interpretable, and strong when queries use similar wording as documents.
=> Sparse retrieval is still widely used in RAG systems, often as a **baseline or hybrid component**.
### Dense Retrieval (Embedding-based)
Dense retrieval uses a **neural embedding model** to transform text into high-dimensional vectors that capture semantic meaning. That means, that:
- Uses learned embeddings to store and retrieve information in a **vector store**.
- Enables semantic search (synonyms, paraphrases, conceptual similarity).
- The main approach behind modern RAG systems (e.g., DPR, E5, OpenAI embeddings).
=> Dense retrieval is especially useful when the wording of queries and documents differs.
### Generation
After relevant information is retrieved, it is passed to the **generative language model**, which produces a coherent and contextually appropriate response.

This completes the core RAG loop: **retrieve → condition → generate**.
## Example Pipeline
Let's look at an example RAG pipeline using dense retrieval. The models we need for this are:
- **Embedding Model**:
	Transforms text into numerical representations (vectors) that encode semantic meaning. These embeddings allow the system to efficiently find the most relevant information (e.g., matching a query to your notes). Example output: a vector like [0.12, -0.45, 0.89, ...].
- **Text Completion Model**:
	A generative model that produces coherent and contextually relevant text based on the retrieved information.

The steps are:
1. Use the **embedding model** to process your notes and convert them into vector representations.
2. Store these vectors in a **vector database**.
3. Convert the user’s query into its own vector. The query vector is compared against stored vectors to find the most semantically similar notes.
4. The retrieved note(s) are passed to the **text completion model**, which crafts a clear, user-friendly response.
