## Dijkstra's Algorithm
Dijkstra’s algorithm is used for finding the shortest (lowest weight) path from a source node to all other nodes in a graph with non-negative weights.

**Steps of the Dijkstra's algorithm**
- We create a dictionary where we save the nodes and the distances. We initially set the distance of the start node to 0 and the distances of the other nodes to infinity. 
- Then we create some data structure to keep track of the visited nodes. 
- Then while not all nodes are visited we find the node with the minimum distance in the dictionary, add this node to the visited data structure, and update the distance for the neighbors of this current node. 
- We repeat this until we have computed the shortest path for all nodes. 
## Prims Algorithm
Prim’s algorithm is used to find the **minimum spanning tree** (MST) of a graph, which is the subset of edges connecting all vertices with the minimum possible total weight.
## Breadth-First Search Algorithm
BFS is used to find the shortest path (in terms of the number of edges) in an **unweighted graph** (while Dijkstra's algorithm works for weighted graphs).

