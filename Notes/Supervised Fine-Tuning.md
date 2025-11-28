Supervised fine-tuning (SFT) refers to adapting a pretrained model using labeled examples so it performs well on a specific task. In classical deep learning and transfer learning, this usually means freezing most layers, replacing or adjusting the final layer, and training it on labeled data — which is indeed a form of SFT. 

In modern large language models, however, SFT is broader: the entire model (or large parts of it) is fine-tuned on high-quality instruction–response pairs to teach behaviors such as following instructions, reasoning, and maintaining a helpful style. That means, that in this case the goal is to  shape the model’s broader capabilities and behavior (e.g. instruction handling).
## Adapters & LoRA
These are tools for doing SFT or transfer learning _efficiently_ by only training a small set of added parameters.

Adapters in general are small trainable modules inserted into the layers of a large pretrained model. During training, **only the adapter parameters are updated**, while the original model weights stay frozen. This makes fine-tuning cheaper, faster, and less likely to overfit.

 LoRA or Low-Rank Adaptation) is essentially a specialized type of adapter. But instead of inserting separate neural modules like classic adapters, LoRA:
- keeps the pretrained weights frozen
- adds _low-rank matrices_ that modify the weight updates