Dialogue systems can be divided into **chatbots** and **digital assistants**. Chatbots aim to have arbitrary conversations, while digital assistants are build for specific tasks. In modern AI these can also be combined in the form of for example ChatGPT. For an example implementation look at this report [[Dialogue Systems and AI.pdf]] and this code snippet [[Dialogue Systems and AI.py]]. 
## Difficulties in Human Dialogues
First there are different so called *speech acts*. We have for example directives, acknowledgments, and so on. The system has to interpret these correctly. These speech acts usually also have some sort of dialogue structure that is apparent for us humans but might not be for systems. 

Another topic that needs to be addressed is *initiative*. Should the system initiate, should the user initiate, should there be a mixed initiative? These are important questions to solve. 

Lastly a big part of human conversation is *inference* and *implication*. Humans know instinctively, what another human means, even if that specific thing is not said, through inference. This is very difficult to model. 
## Task-based Dialogue Systems for Digital Assistants
The basic architecture of a dialogue systems (that assumes spoken inputs) looks like this: 
- We have a speech recognition (SR) unit. This unit is usually NN-based and is supposed to turn speech into written hypotheses. 
- Second we have a natural language understanding (NLU) unit. The NLU has the task to extract meaning of the written hypotheses of the SR unit. This unit is rule-based or increasingly ML-based. 
- The dialogue manager (DM) to manage the dialogue so that the user does not have to give all information in one statement. Sometimes the DM works together with a task manager.
- The natural language generation unit (NLG). This unit formulates an answer. 
- The text-to-speech synthesis unit (TTS). This unit finally converts the output of the NLG into spoken words. 

**NLU**
The three main tasks of a NLU are: **domain classification**, **intent recognition**, and **entity extraction**.

The goal of domain classification is to determine the general category of the request. If the system supports multiple topics (e.g., flight booking, restaurant reservations, and weather info), it must first classify the user’s input into one of these domains. Dialogue systems usually use **text classification models** (e.g., Naïve Bayes, SVMs, Deep Learning like BERT) trained on labeled examples. If the confidence score is low, the system may ask clarifying questions.

Intent recognition means identifying the user’s desired specific action within the domain. Within a domain, multiple **intents** exist (e.g., “BookFlight”, “CancelFlight”, “CheckFlightStatus”). Dialogue systems use **multi-class classification models** (e.g., Logistic Regression, Random Forest, Deep Learning) to do this. Sometimes, a **rule-based approach** works for simple cases (e.g., keywords like “book” → “BookFlight”). 

Finally, entity extraction extracts relevant details (entities) from the user’s sentence. Entities are structured pieces of information needed to fulfill the intent. The approaches here can be for example rule-based (keyword matching) or machine learning models. 

**DM**
The dialogue manager and task manager work together like this: The DM determines what should happen next—whether to continue the conversation, ask for clarification, or call the task manager. If the request requires an action (e.g., booking, searching, retrieving data), the TM executes it. Therefore the purpose of the dialogue manager is to maintain the conversation’s state and ensure coherent and contextually appropriate responses. 

Dialogue management can be done in two ways **finite-state-based** and **frame-based (form-based)**. 
- In finite-state-based dialogue management the conversation follows a predefined **state machine**, where each state represents a step in the dialogue. The user must progress through the states in a fixed sequence, like a flowchart. Therefore the system dictates the flow, and user flexibility is limited.
- In frame-based dialogue management the system uses a **frame (form)** with multiple **slots** that need to be filled. The user can provide information in any order. and the system asks only for missing details instead of following a strict sequence. This works especially well for task-based systems but is more complicated to implement. 

