## Introduction
With [[Retrieval-Augmented Generation (RAG)]], we can build a ChatGPT like chat that works on our own Obsidian markdown files. This means that as input for this LLM we use the files in this vault. 
## Building the RAG
There are two steps to building the RAG: 
1. First, we have to start a local server in LM-Studio to load the two models. The models we need are one for text completion and one for embedding your notes to be used in a vector store. This looks like this:                                                                                                          ![[Pasted image 20241211111138.png|400]]
3. We need a Flowise chatflow, to create our chat. This can look like this:  ![[Pasted image 20241211111040.png|400]]
## Steps to Start the Chat
1. Start LM-Studio
2. Start the Flowise instance:
	- `npm install nvm` - install nvm, because we need to use an older npm version.
	- `source ~/.nvm/nvm.sh` - needed because of some error
	- `nvm use 20` - Flowise currently only supports npm version 20
	- `sudo npx flowise start` - start the Flowise instance, it can now be reached at http://localhost:3000

When encountering the following error: *listen EADDRINUSE: address already in use :::3000*, take these steps:
- `sudo lsof -i :3000`
- `sudo kill -9 PID`
## Further Improvements
The idea is to merge ChatGPT and this RAG to have answer that first show, what I have written here in this vault and second, show what ChatGPT has to say about it. 

Use RAG as a error analysis tool. Define some constraints for code in Obsidian => Ask RAG, if some code is good or not. 