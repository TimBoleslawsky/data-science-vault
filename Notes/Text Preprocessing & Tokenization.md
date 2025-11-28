Text preprocessing prepares raw text for NLP models. The first and most crucial step is **tokenization**, which breaks text into smaller, consistent units (tokens) that can be mapped to numbers.

An important concept for text preprocessing is the *vocabulary*. The vocabulary is the list of all tokens known to the tokenizer. Each token has a unique ID used by the model’s embedding layer. We kann also add unknown or padding tokens with with a special symbol (e.g., \<unk>). One such a special symbol is usually a padding symbol, which defines some empty space. To indicate which tokens are valid text vs. empty paddings in a batch, we can use *attention masks*. 
## Tokenization
Tokenization is the process of splitting text into _tokens_ — typically words, subwords, or characters — that form the basis for all further text processing. The goal is to convert raw text to structured input usable by neural network models.

**Examples of tokens:**
-  Words: “NLP”, “language”, “model”
- Subwords: “play”, “##ing”		
- Characters (in some languages or models)

There are two common types of tokenization methods:
- **Rule-based tokenization:** Uses manually designed rules (spaces, punctuation, abbreviations).
	- Example:
		“Mr. Smith bought cheapsite.com shares for \$20,000.” => \[“Mr.”, “Smith”, “bought”, “cheapsite.com”, “shares”, “for”, “$”, “20,000”, “.”]

- **Subword tokenization:** Data-driven; learns frequent character sequences from corpora	
	- Algorithms: **BPE (Byte-Pair Encoding)**, **WordPiece**, **Unigram LM**		
	- Example: “cheapsite.com” → \[“cheap”, “site”, “.”, “com”]
	- Solves the **unknown word problem** and reduces vocabulary size.

We today want to usually work with pre-trained tokenization models like BERT or GPT. But, these only work, if they match our needed vovabulary! Alternatively we can train our own custom tokenizers (e.g. Hugging Face Tokenizers), where we need to define the corpus, algorithm, vocabulary size, etc. Once trained, the tokenizer is fixed and used consistently across training and inference.
