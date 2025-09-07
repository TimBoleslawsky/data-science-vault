When doing [[Parallel Programming in Python|parallel programming]] it is important to follow certain principles so that parallelization can be done correctly and without faults. Just like in object-oriented programming, we want to use inheritance, in parallel computing, we want to use MapReduce Programming. 

MapReduce works in two phases:
1. Map Phase
   In the map phase we use data parallelism. We use a mapper to process each piece of input data independently. Mappers then run in parallel across different machines or cores. This could look like so:

``` python
map(f, data)  # Applies f to each piece of data in parallel 
```

2. Reduce Phase
   After mapping, intermediate results are grouped by key (also called shuffled) and then reduced or aggregated. Reducers also run in parallel, but each one handles a distinct key (or group of keys).

A problem with our example is that it can generate a lot of communication. **Combiners** solve this problem. Combiners are essentially “mini-reducers” that are executed locally after the map operation but before shuffling. Combiners perform a reduce operation locally, and only the result is then communicated.
## Performance Considerations
MapReduce only makes sense if the data is sufficiently large such that it cannot neatly fit into the RAM. If the data fits in RAM, then MapReduce only introduces unnecessary overhead. The key to a performant MapReduce algorithm is to limit the amount of I/O. In practice this corresponds to limiting the amount of data that is communicated in the shuffling stage. 

Another thing to consider is that the storage of data matters. If the data is stored evenly distributed, we’re good, but skewed distribution (e.g., all relevant pieces on one node) hurts parallelization. 
## Implementations of MapReduce
The concept of MapReduce can be implemented in different systems. Examples include:
- **Hadoop MapReduce:** The most famous implementation, using the Hadoop ecosystem (HDFS, YARN).
- **MRJob (Python):** A lightweight MapReduce framework for writing and running MapReduce jobs in Python. An example for this here: [[MapReduce Programming.py]]