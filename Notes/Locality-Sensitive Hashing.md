Locality-Sensitive Hashing (LSH) is a powerful technique designed to efficiently find similar items in high-dimensional data, especially when exact nearest neighbor search becomes too slow or impractical. 

The basic problem we want to solve with LSH is known as the nearest neighbor search. In high-dimensional spaces, exact methods, more on them here: [[Spatial Data Structures]], become computationally expensive or even infeasible due to the curse of dimensionality.

This is where Approximate Nearest Neighbor (ANN) techniques come in. LSH is one such technique that allows sublinear-time retrieval of similar items by sacrificing a small amount of accuracy. Just like with spatial data structures, we build a specialized data structure to do this.
## Approximate Nearest Neighbor
First we want to clearly define the problem that LSH tries to solve. LSH solves the **(c, r, δ)-Approximate Near Neighbor** problem. This problem is defined as:
- given some metric space $M=(X,D)$, a dataset $P \subseteq X$, a query point $q \in X$, a distance threshold $r > 0$, an approximation factor $c> 1$, and a failure probability $\delta \in (0,1)$.
- if there exists a point $p^* \in P$ such that the distance between query point $q$ and $p^*$ is at most $r$, return any point $p \in P$ such that the distance between query point $q$ and $p$ is at most $cr$, with probability at least $1 - \delta$.  

We do not specify what happens upon failure (though it would be expected that we return a point too far away, or report none).
## Data Structure
The fundamental idea behind LSH is to hash similar items into the same bucket with high probability, and dissimilar items into the same bucket with low probability.

This contrasts with traditional hash functions (like cryptographic ones) which aim to uniformly distribute data and avoid collisions. => In LSH, collisions are desirable for similar items.

The data structure we construct for this consists of $L$ multiple hash tables, which in turn use a has function $g_i$ constructed by concatenating $k$ base hash functions drawn independently from hash family $H$. This hash family $H$ should be ($r$,$cr$,$p_1$,$p_2$)-sensitive, this means that:
- if the distance between points $x$ and $y$ is below or equal to $r$ ($D(x,y) \leq r$), then the probability of $x$ and $y$ landing in the same bucket is higher or equal to $p_1$. 
- if the distance between points $x$ and $y$ is above $cr$ ($D(x,y) > cr$), then the probability of $x$ and $y$ landing in the same bucket is lower or equal to $p_2$.
We call the quality of the hash family $H$: $\rho = \frac{\log(1/p_1)}{\log(1/p_2)}$, where $\rho < 1$ is desirable.

We construct the data structure by drawing the $Lk$ hash functions from $H$ and initializing the $L$ hash tables. Now we store each data point $x$ in all $L$ hash tables, each using a different hash function $g_i$.

When we want to run a query on this for query point $q$ we:
- compute its hashes $g_1(q), …, g_L(q)$,
- look up the corresponding buckets in each of the $L$ tables,
- collect all points from these $L$ buckets (possibly with duplicates),
- compare $q$ to the collected points by computing the actual distance $D(q, x)$,
- return the closest point within distance $cr$, with probability $\geq 1 - \delta$ — if any exist.
Important note, in the ($c$, $r$, $δ$)-approximate nearest neighbor setting, we are not required to return the exact nearest neighbor — only some point within distance $cr$, if one within $r$ exists.
## Comparison To an Alternative: KD-Trees
KD-Trees are another structure for nearest neighbor search, especially in low-dimensional Euclidean spaces. For more information see here: [[Spatial Data Structures]].

| **Feature**              | **LSH**                               | **KD-Tree**                               |
| ------------------------ | ------------------------------------- | ----------------------------------------- |
| Best for                 | High-dimensional, approximate search  | Low-dimensional, exact or approximate     |
| Space                    | $O(Ln)$                               | $O(n)$                                    |
| Query time               | Sublinear for approximate search      | $O(\log n)$ in low dimensions             |
| Handles high dimensions? | Yes (especially with good LSH family) | No (suffers from curse of dimensionality) |
| Data-independent?        | Yes                                   | No (requires tree construction on data)   |
| Tunable tradeoffs        | Yes (via $k$, $L$, $\rho$)            | Limited                                   |

=> LSH is a probabilistic data structure that may fail, but k-d trees return exact answers. However, due to curse of dimensionality, k-d trees’ performance decays very rapidly  
as the number of dimensions grows, so they are only appropriate for small dimensions. In contrast, LSH provides good theoretical guarantees even in high dimensions
## Random Hyperplane LSH
A special use case for LSH is the use case with cosine similarity. Cosine similarity means, we care about the angle between vectors, not their magnitude. Vectors pointing in similar directions are considered similar, regardless of their length. This is for example important for document similarity, recommendation systems, ...

For the data structure this means:
- If two vectors point in the same direction (small angle), they should hash to the same value with high probability.
- If they point in opposite directions (large angle), they should hash to the same value with low probability.
To construct such a data structure we use hyperplanes. A hyperplane divides a plan in two half-spaces. This means a hyperplane in 2D is a line, in 3D it is a plane, ... 

The main process of construction and querying is very similar to standard LHS. 
- We have $L$ hash tables. 
- For each of the $L$ hash tables, we sample $k$ independent random hyperplanes (i.e., normal vectors). These serve as the hash function: $h(x) = \text{sign}(\langle x, \mathbf{n} \rangle)$, which returns +1 if $x$ lies on one side of the hyperplane and -1 if it lies on the other side. 
- Concatenated, these define the composite hash function $g_i(x)$. 
- For each point $x \in P$ we again go through each table once and compute a hash value that stores the difference based on +1/-1 for each of the $k$ hyperplanes. 
- We do the same for the query point $q$ to find the most similar.

