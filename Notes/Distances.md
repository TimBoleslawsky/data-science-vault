## Points and Vectors
Points are representations of **locations** in a feature space. Each point is defined by an array of numbers (coordinates) that represent its position in that space. Vectors, while also represented as arrays of numbers, emphasize both **magnitude and direction**. Vectors can be understood as a line from the origin to the point.

Vectors are particularly useful when normalizing the magnitude to focus solely on the direction of the vector, which allows for comparing the orientation of data points without considering their absolute scale.

Let's look at an example:
Suppose you are comparing two articles based on the number of times specific keywords (topics) are mentioned. Each article can be represented as a **point** in a high-dimensional space, where each dimension corresponds to a keyword.

Let’s assume the articles are analyzed for two keywords: **machine learning (ML)**, **data science (DS)**. We represent each article with a 3D point where each coordinate represents the frequency of these keywords in the article.
- **Article 1**: Contains 20 mentions of ML and 15 mentions of DS. This can be represented as the point  A = (20, 15).
- **Article 2**: Contains 10 mentions of ML and 8 mentions of DS. This can be represented as the point  B = (10, 8).

![[Pasted image 20241016194504.png|400]]

These points give us the absolute frequencies of each keyword but don’t tell us much about how similar the two articles are in terms of topic distribution.

Now, let’s think of each article as a **vector** pointing from the origin (0, 0, 0) to their respective points in space.
- **Vector A** has a magnitude and direction that correspond to the point  (20, 15).
- **Vector B** has a magnitude and direction corresponding to the point  (10, 8).

The key difference is that **vectors allow us to compare direction and magnitude**, which can be particularly useful when normalizing for comparison purposes. To compare the two articles based on topic **distribution** rather than just raw keyword counts, we can normalize the vectors:
- **Normalized Vector A**:  $\left(\frac{20}{\sqrt{20^2 + 15^2}}, \frac{15}{\sqrt{20^2 + 15^2}}\right)$ 
- **Normalized Vector B**:  $\left(\frac{10}{\sqrt{10^2 + 8^2}}, \frac{8}{\sqrt{10^2 + 8^2}}\right)$
This is also known as the $𝑳_𝟐$-norm and alternatively denoted $||𝑥||_2$. As with the $𝐿_𝑘$ distances, the $𝐿_𝑘$-norm generalizes to any 𝑘. After such normalization, the length of each vector will be 1, turning it into a point on the unit sphere about the origin.

![[Pasted image 20241016194640.png|400]]

By comparing these normalized vectors, we focus on the **topic distribution** (the proportion of keywords) rather than the raw counts. If the vectors have a similar direction, the articles are similar in topic distribution, even if one article is longer or contains more keywords overall.
## The $L_k$-Metric
If we want to measure the distance of points in a space we have different metrics we can choose from. The most familiar one is the $L_k$-Metric (especially $L_2$ aka the Euclidean Distance). 

The $L_k$-Metric is calculated like this: 
![[Pasted image 20241016195625.png|400]]
### Euclidean Distance
The Euclidean Distance is a special case of the $L_k$-Metric where $k = 2$. Distance is basically measured as a line between the two points.
### Manhattan Distance
The Manhatten Distance is a special case of the $L_k$-Metric where $k = 1$. Distance is basically measured as the steps we would need to take in a grid or the steps on the x-axis plus the steps on the y-axis. 
### Chessboard Distance
The Chessboard Distance is a special case of the $L_k$-Metric where $k = ∞$. The Chessboard Distance returns the largest single dimensional difference as the distance.
### Which $k$ to Choose?
This choice of distance metric is most important in high-dimensional data spaces. Of course, we can always stick with $L_2$-Distance, which is a safe and standard choice. But sometimes we do not want this: 
- If we want to reward points for being close on many dimensions, we prefer a metric leaning more towards $L_1$. If we are concerned about random added noise $L_1$ is not desirable because we will add up the noise from all dimensions.
- If instead things are similar when there are no single fields of gross dissimilarity, we perhaps should be interested in something closer to $L_∞$. On the other hand a substantial error in any single column will come to dominate the entire distance calculation.
## Other Metrics
Besides the $L_k$-Metric, there exist other metrics to measure distance. Here are some examples:
- **Hamming distance** is the number of coordinates in which two vectors disagree.
- **Jaccard distance** measures the dissimilarity between two sets.
- **Edit distance** or **Levenshtein distance** is the number of single-character edits (insertions, deletions, or substitutions) to change one character sequence into the other.
## The Curse of Dimensionality
The curse of dimensionality is the phenomena that arise with high numbers of dimensions of the observations. These phenomena includes the fact that there are a vast number of possible choices (combinatorial explosion) for combinations of discrete values, volumes grow exponentially (and the volume is concentrated, e.g., around a thin annulus around the surface of a hypersphere), all vectors become approximately orthogonal, and everything is approximately “equally far apart”.
