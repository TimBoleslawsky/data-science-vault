## Linear Data Structures
There exist advanced data structures that are not natively in Python but can still be implemented either by creating an own class or importing a module from a library. These data structures have varied benefits when comparing them to the standard data structures.
### Linked List
In contrast to lists, elements in linked lists are not stored in a contiguous location, they are linked with pointers. Each element in a linked list is called a *node*. Each *Node* consists of *Data* (the value stored) and *Next* (a reference to the next node on the linked list). The first node is called *Head*. 

If we talk about a doubly linked list we mean linked lists that not only have references to the next node but also to the previous. 

Linked lists are much less memory efficient than lists but can be very fast when looking at operations like deletion.
### Stack
A stack stores items in a *Last-In-First-Out (LIFO)* manner. The last element added to the stack will be the first one to be removed. A new element is added at one end/top and an element is removed from the same end. The *insert/add* and *delete* operations are often called *push()* and *pop()*.
### Queue
A queue stores elements in a *First-In-First-Out (FIFO)* manner. The first element added to the queue is the first one to be removed. The *insert/add* and *delete* operations are often called *enqueue()* and *dequeue()*. A new element is added to the rear end and an element is removed from the front of the queue. 

The libraries `collections.deque` and `queuq.Queue` can be helpful when working with queues because using a Python list to implement a queue is inefficient!
## Non-Linear Data Structure
In non-linear data structures, data items are not organized sequentially. This means that a data item could be connected to many data items to reflect a special relationship among these items. Due to its nature, it cannot be traversed during a single run.
### Binary Search Trees
BSTs have the following characteristics: It has a *root* node. Each node has a maximum of two child nodes. *Left*: keys less than or equal to the parent's key. *Right*: keys larger than the parent's key. This means that the values stored in a BST must be orderable. This can be difficult for strings or other more complex data types. 

When working with BST, we often assume distinct keys or no duplicates. When duplicates are allowed, complications will appear here and there during computation.

The running time for a search in a BST is $O(h)$ with $h$ being the height of the tree. In the best case, this height is $log(n)$ in the worst case, this is $n$. This means that ideally, we want the left and right subtrees to be almost the same size.

Some libraries for working with trees include [anytree](https://pypi.org/project/anytree/) and [treelib](https://pypi.org/project/treelib/#description).
### Tries
A trie is a type of tree structure where the nodes store prefixes. This means that each *path*, meaning a path from the root node to the destination, forms something meaningful like a word in predictive text or a prefix of an IP in web routing.

Some libraries for working with tries include [pygtrie](https://pygtrie.readthedocs.io/en/latest/index.html) and [python-trie](https://github.com/bdimmick/python-trie).
### Graphs
A graph $G$ consists of some nodes $V$ and some edges $E$. The graph can either be **directed** or **undirected** depending on if the edges denote some direction. 
The nodes in the undirected graph have the property $deg(v)$ which denotes the number of edges connected to the node $v$. The nodes in the directed graph have the properties $indeg(v)$ and $outdeg(v)$ which denote the ingoing or outgoing number of edges of the node. 
Graphs can also be **weighted**, which means that we have a cost associated with each edge

We have two ways to represent graphs in programming languages:
1. Adjacency Matrix: The adjacency matrix $A$ is a matrix of size $n*n$ with $n$ being the number of nodes. Now in the matrix, we denoted $A_{ij}$ as a $1$ in the position $(i,j)$, if there exists an edge from $v_i$ to $v_j$. The adjacency matrix is symmetrical in an undirected graph but not in a directed graph.
2. Adjacency List: In an adjacency list, each node in the graph stores a list of other nodes that it is connected to by an edge. For directed graphs, save just the outgoing edges in the lists.

**Adjacency Matrix vs. Adjacency List**
Advantages of an adjacency list:
- You can quickly access all neighbors of a node, making it efficient for operations like **traversals** (e.g., depth-first search, breadth-first search).
- If a graph has many vertices but few edges, adjacency lists are more efficient because adjacency lists only store the edges that exist rather than every possible connection.
Advantages of an adjacency matrix:
- Checking whether an edge exists between two specific vertices is fast because we have the coordinates in the matrix.
- For graphs where most vertices are connected to each other (dense graphs), adjacency matrices are an efficient way of storing this data.

**Paths and Cycles**
A **path** from $v_i$ to $v_k$ is a sequence of nodes in $G$ if each node in this sequence is joined by an edge. The **path length** corresponds to the number of edges in a path.
A graph $G$ is **connected** if and only if (iff) for every node can reach every other node via a path.
A **cycle** is a path $v_I = v_k$ with $k > 2$ and no two nodes repeat in the path.

For directed paths: Every pair of nodes in a path or cycle must respect the directionality of edges. A directed graph $G$ is **strongly connected** if and only if, for every pair of nodes, there exists a path in both ways. 

An undirected graph $G$ is a tree if it is connected and does not contain a cycle. 

**Libraries for Graphs**
Several different libraries for graphs:
- [NetworkX](https://networkx.org/): NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
- [PyVis](https://pyvis.readthedocs.io/en/latest/): PyVis is a Python library to construct and visualize network graphs in the same space. Each graph can be interacted with, allowing the dragging, hovering, and selection of nodes and edges.
- [PyG / Torch geometric](https://pytorch-geometric.readthedocs.io/en/latest/): PyG (PyTorch Geometric) is a library built upon [PyTorch](https://pytorch.org/) to easily write and train Graph Neural Networks (GNNs), and represent data for a wide range of applications related to structured data.

