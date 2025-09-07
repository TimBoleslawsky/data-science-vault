Hash tables are associative arrays where key-value pairs are stored in an array, as indicated by a hash function.
## Collision Handling
If there is already an element in the bin (a hash collision occurs), collision resolution  
is needed. There are two main strategies to solve this problem:
1. **Separate Chaining**
	- Each slot in the table holds a **linked list (or similar structure)** of entries.
	- When a collision occurs, the new key-value pair is **appended to the list** at that index.
   **Pros:**
	- Simple to implement.
	- Handles high load factors relatively gracefully.
	- No clustering effect (collisions don’t propagate).
   **Cons:**
	- Requires additional memory for pointers.
	- Worse cache performance due to pointer chasing.
2. **Open Addressing**
	- All elements are stored directly in the hash table array.
	- When a collision occurs, the table searches for the **next available slot** using a **probing strategy** (like linear, quadratic, or double hashing).
   **Pros:**
	- Better cache locality (data is stored in contiguous memory).
	- No extra memory for chains.
   **Cons:**
	- Performance degrades sharply as the load factor increases.
	- Clustering can occur, especially with simple probing like linear probing.
	- Deletion is trickier (requires “tombstone” markers or rehashing).
## Considerations when Using Hash Tables
Hash tables are mainly used because they enable very fast insert, delete, and lookup for key value pairs. Obviously if we do not have key value pairs and just simple values, we would not use hash tables. It would be possible to store key value pairs without hash tables, which might take a little less space, but would be much slower. 

The main reason why hash tables take more space is the overhead for collision handling. A hash table typically allocates more space than needed to avoid too many collisions. Additionally, depending on if we use chaining or open addressing:
- In chaining, each slot stores a list (which needs pointers and memory allocation).
- In open addressing, some slots are wasted due to probing and deleted markers (“tombstones”).

The hash value itself is usually not stored and does therefore not impact space usage negatively. If stored, this again obviously introduces some overhead.

