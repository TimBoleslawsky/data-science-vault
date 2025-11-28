Clustering is the problem of assigning meaningful labels to unlabeled points by grouping them. The difference between clustering and classification is that in classification we know our labels beforehand, in clustering, we do not. Therefore, clustering is unsupervised learning.

The goal is to uncover latent group structure in $X$ without labels. Mathematically this means, we want to learn a function $g: \mathcal{X} \to \{1, \dots, K\}$ assigning points to clusters, or a latent representation $Z \in \mathbb{R}^d$ where clustering structure is more evident.

**Is data "clusterable"?**
The general idea is to compare the data distribution with a theoretical distribution with no clustering tendency! This can be done with a [[Q-Q Plot]], which is difficult for higher dimensions, or by computing the pairwise distance.

We can categorize our clustering models into four categories:
- Centroid clustering 
- Distribution clustering
- Density clustering 
	=> These three are sometimes more generally categorized into *partitional* clustering.
- Hierarchical clustering