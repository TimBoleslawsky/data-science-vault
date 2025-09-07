## Clustering
Clustering is the problem of assigning meaningful labels to unlabeled points by grouping them. The difference between clustering and classification is that in classification we know our labels beforehand, in clustering, we do not. Therefore, clustering is unsupervised learning.

Clustering can be useful for a number of reasons. When dealing with millions or billions of records, clustering can be a good way to perform *data reduction*. The idea is to cluster the points by similarity and then appoint the centroid of each cluster to represent the entire cluster. *Outlier detection* is the problem of ridding a data set of discordant items, so the remainder better reflects the desired population. Clustering is a useful first step to finding outliers. The cluster elements furthest from their assigned cluster center don’t really fit well there but also don’t fit better anywhere else. This makes them candidates to be outliers. Another useful application for clustering is image compression. 

**Is data "clusterable"?**
The general idea is to compare the data distribution with a theoretical distribution with no clustering tendency! This can be done with a QQ-plot, which is difficult for higher dimensions, or by computing the pairwise distance.

We can categorize our clustering models into four categories:
- Centroid clustering 
- Distribution clustering
- Density clustering 
	=> These three are sometimes more generally categorized into *partitional* clustering.
- Hierarchical clustering
### Centroid Clustering
#### $k$-means Clustering
The idea behind $k$-means clustering is to take $k$ cluster centers, for example at random. Then we map the points to the nearest cluster center and compute a new cluster center. We repeat this until we cannot improve the cluster centers (this can be seen as a simplified version of the Expectation-Maximization algorithm). We call this convergence. Important is that $k$-means clustering solves for the **local optimum** and not the **global optimum**. 

**Model Definition of Form $y = g(x;θ | h)$**
Left-hand side:
- $y$: categorical (nominal) - each category is called cluster.
Right-hand side:
- $x$: typically continuous numerical.
- $g$: K-means
- $h$: the number of centroids k
- $θ$: k centroids

**Centroids vs. Medioids**
There are at two possible criteria for computing a new estimate for the center point. When the data is numerical, we often talk about the cluster centers as **centroids**. The centroid is the geometric mean of a set of points using an appropriate $L_k$-metric. Sometimes this makes no sense, such as when some features are categorical; then instead of centroids, we can take the **medioids** as cluster centers. Unlike a **centroid**, which is the **average** of all points in the cluster and may not correspond to an actual data point, a **medioid** is always an **actual data point** from the dataset. Medioids minimize the **sum of distances** (or dissimilarities) to all other points in the cluster, making them less sensitive to outliers and noise compared to centroids. We are therefore flexible in which distance function we want to use and don't have to rely on an $L_k$-metric.

**How to determine $k$ and our initial centroids/medioids?**
For more on hyperparameter tuning, see here [[Model Selection & Hyperparameter Tuning]].
### Distribution Clustering
#### Gaussian Mixture Model (GMM)
The idea behind the GMM is similar to the [[Approaches for creating Classification Models#Naïve Bayes Classification|naive Bayes classifier]]. We calculate a set of K posterior probabilities. Each data point $x$ is assigned to all clusters with a posterior probability. One major difference between GMM and naïve Bayes, is that we do not assume independence for the feature dimensions in GMM! 

In contrast to k-means clustering, the Gaussian mixture model is *soft clustering*, meaning that $x$ is assigned to all clusters with a probability - the posterior. 

Two understand the GMM, we need to understand these two formulas:
- The formula for the PDF in a GMM is: $P(x_i) = \sum_{k=1}^{K} \pi_k \mathcal{N}(x_i \mid \mu_k, \Sigma_k)$ =>  **overall likelihood** of observing a data point $x_i$.
- The formula for the GMM is: $\gamma_{ik} = \frac{\pi_k \mathcal{N}(x_i \mid \mu_k, \Sigma_k)}{\sum_{j=1}^K \pi_j \mathcal{N}(x_i \mid \mu_j, \Sigma_j)}$ => calculates the **posterior probability** for each cluster.
The general formula for the GMM is very similar to the naïve Bayes formula. We have a prior (in this case denoted as $\pi_k$) also known as the mixing coefficient and the likelihood. 
- The first difference, is that the PDF and the likelihood used in the formula are not the same. This is because the PDF is the likelihood over all assumed Gaussian distributions. 
- The second difference, is that we do not ignore the denominator like in naïve Bayes. In GMMs, the sum in the denominator is required to normalize the probabilities across multiple Gaussian components. 

**Expectation-Maximization Algorithm**
For the parameter estimation for GMM, we use the EM algorithm. The basic idea is that we have an E-step and a M-step, which we repeat until convergence. We use the EM algorithm to estimate: 
- mixing coefficients $\pi_k$ (basically the prior)
- means $\mu_k$ of the Gaussian distributions 
- covariance matrices $\Sigma_k$ of the Gaussian distributions. For one dimension, this is just the standard deviation, but for multiple dimensions, this looks like this: $\Sigma_k = \begin{bmatrix} \sigma_{k,11} & \sigma_{k,12} & \dots & \sigma_{k,1d} \\ \sigma_{k,21} & \sigma_{k,22} & \dots & \sigma_{k,2d} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{k,d1} & \sigma_{k,d2} & \dots & \sigma_{k,dd} \end{bmatrix}$

Before iterating over the E-step and the M-step, we need to initially assume some values for $\pi_k$, $\mu_k$, and $\Sigma_k$. The E-step (expectation) is just the calculating of the posterior for all data points given each cluster (see function for $\gamma_{ik}$). The M-step (maximization) is to update the parameters for each cluster. The definitions are given as follows: 
- Mixing Coefficients: $\pi_k = \frac{\sum_{i=1}^N \gamma_{ik}}{N}$
- Means: $\mu_k = \frac{\sum_{i=1}^N \gamma_{ik} x_i}{\sum_{i=1}^N \gamma_{ik}}$
- Covariances: $\Sigma_k = \frac{\sum_{i=1}^N \gamma_{ik} (x_i - \mu_k)(x_i - \mu_k)^T}{\sum_{i=1}^N \gamma_{ik}}$
We reach convergence, when the objective function stops changing, or the parameters stop changing. 

**Model Definition of Form $y = g(x;θ | h)$**
Left-hand side:
- $y$: categorical (nominal) - each category is called cluster.
Right-hand side:
- $x$: typically continuous numerical.
- $g$: K-means
- $h$: the number of Gaussian components k
- $θ$: k priors, k Gaussian likelihood

**How to choose $K$?**
The idea is to find the best K that balances the “error” and the complexity of the model - Occam’s Razor. There are two metrics, that we can use: Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC). BIC penalizes the complexity more than AIC - BIC increases more as $K$ gets larger. For more on hyperparameter tuning, see here [[Model Selection & Hyperparameter Tuning]].

