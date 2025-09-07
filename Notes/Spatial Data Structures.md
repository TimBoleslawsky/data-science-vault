Just like [[Probabilistic Data Structures]], spatial data structures are specialized data structures to solve a specific problem. In the case of spatial data structures these problems are spatial queries like nearest neighbor. The idea is to preprocess the list of data points of interest into a data structure that enables faster queries.

Spatial data structures are useful in lower dimensions (we will specifically look at one and two dimensions here). For higher dimensions the methods described below will become worse than linear scan due to the curse of dimensionality (look [[Distances#The Curse of Dimensionality|here]]), and methods like [[Locality-Sensitive Hashing]] are preferred. 
## Range Queries in 1D
The objective of the range search in one dimension, is to find the numbers in the set $P$ that satisfy the condition $x < p < y$. 

The simplest solution would be the linear scan, which just means to go through each data point in the set and compare them to $x$ and $y$. This takes $O(n)$, and is obviously very inefficient with a lot of queries. Here is where spatial data structures come into play. 
### Range Trees
The range tree is a balanced binary tree that splits the list we want to analyze in halve at each node. Traversal works by finding split nodes until we get to the leafs of the tree. Range queries on range trees takes $O(logn + k)$ time. $O(log n)$ for the tree traversal (finding the split node and subtrees to recurse into) and $k$ for outputting the points (one unit of time per point found).
## Range Queries in 2D
The objective of range search in two dimensions, is to find the points in $P$ which lie in a rectangle, delimited by two points (𝑥, 𝑦) and (𝑥′, 𝑦′). A point 𝑝 = (𝑝𝑥, 𝑝𝑦) lies in the rectangle if and only if it satisfies 𝑥 ≤ 𝑝𝑥 ≤ 𝑥′ and 𝑦 ≤ 𝑝𝑦 ≤ 𝑦′. Therefore an alternative interpretation of this problem is that we need two range queries, one along each axes.

Linear scan is again a trivial solutions, we just iterate over all points 𝑝 ∈ 𝑆, compute $||𝑝 − 𝑞||$, and return the points satisfying $||𝑝 − 𝑞||$ ≤ 𝑟. In small dimensions, this is again obviously an 𝑂(𝑛) routine, so for very large datasets and very large numbers of queries, this is prohibitively expensive.

It is important to note however that this approach is flexible, being applicable to all sorts of distance functions, and cache-friendly, making it easily parallelizable. This can sometimes lead to the fact that it is hard to beat in higher dimensions. 
### K-d Trees
The idea behind k-d trees is the following:
- alternate between the $x$ and $y$ coordinates
- Sort all points by that coordinate  
- Select the median point  
- Split the points into two equal-sized (up to 1 difference) subsets on whether their coordinate is less than or greater than that of the median  
- Create a node in a tree that stores the median  
- Recurse on the lesser set (including the median) as the left subtree, and the remaining points as the right subtree
The resulting data structure is a binary tree, where the leaf nodes store the actual points and the non-leaf nodes store the median value (along the specific coordinate axis). 

With k-d trees we also need to take construction into account when talking about efficiency. Construction of k-d trees takes $O(nlogn)$. That's because there are $𝑂(log 𝑛)$ levels of recursion and on each level we need to perform a total of 𝑂(𝑛) work to determine the median and split  
the points into two subsets. The size of k-d trees is $O(n)$. 
### 2D Range Trees
The extension of range trees into two dimensions means that we first build a range tree on one axis ($x$) and then each node stores a secondary range tree on the other axis $(y)$. The trade-off here is that we have faster query time $O(log² n + k)$ but higher space $O(nlogn)$ when compared to the k-d trees. 
### Quadtrees and Octrees
The idea of quadtrees and octrees is very simple. We take the region of space and divide it exactly into four sub-boxes (in two dimensions), or eight sub-boxes (in three dimensions), hence the name. Then if the sub region encompasses a data point we again divide the space into four/eight sob-boxes, and so on. The advantage is that it may be easier to modify them on-the-fly due to their regular structure, but the disadvantage is that k-d trees are usually faster and more space efficient. 

