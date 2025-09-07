The purpose of **hashing** is to map data of arbitrary size to fixed-size values, typically for faster data lookup, comparison, or storage. In simple terms, hashing transforms input (like a string or file) into a short, usually unique code called a **hash value** or **hash code**.

This means that hashing is **not** meant to recover the original data. Hashing is meant to identify or verify the original data — without needing to store or reveal it.

Take this example: 
- without hashing, you could store key-value pairs as a simple list of (key, value) pairs. This could look like this \[("apple", 1), ("banana", 2), ("cherry", 3)]. When you want to find "banana", you’d have to scan the whole list, checking one by one — this is called linear search and it is slow if you have thousands or millions of keys.
- with hashing, the dictionary computes a hash of the key (like “banana” → 874593) and jumps directly to where the value is stored.

Important: This also means that, for example in a Python dictionary, both the hash **and** the original key need to be saved to be able to retrieve the original values as well as make us of the hash functionalities. 

A Python dictionary is an example for a hash table. More on hash tables here: [[Hash Tables]].

An implementation and evaluation of the popular **Murmur3_32** hash function, as well as the connection to the theory outline in this note, can be found here: [[Hashing in Python]].
## Hash Functions
A hash function $ℎ ∶ 𝑈 → 𝑅$ maps the elements of a universe $𝑈$ to some fixed number of values $𝑅.$ This becomes interesting in the case when $R$ < $U$. Then we can have **hash collisions**, meaning two elements of the universe are mapped to the same hash value.

It is important to note that sometimes hash functions are used to implement randomness. But the hash functions themselves are inherently deterministic. Randomness is then in the choice of the hash function (over the distribution of the hash function family).

We define a few theoretical properties of a good hash functions, that we try to aim at:
- A good hash function should be fast to compute (we often need to compute the hash values for all elements in a dataset).
- Collisions cause performance degradation (more searching, chaining, etc.) and should be minimized while still maintaining randomness!
- We would like the hash function to behave as if it was uniformly random. This means that for $m$ bins:
	- Each bin is equally likely to receive a given input $x$, namely $\frac{1}{m}$
	- The hash value for $x$ doesn’t affect the value for $y$, pairwise independence.
	- The probability of a collision happening is $\frac{1}{m}$.

=> To summarize, we want hash functions to turn strings (or whatever) into same-sized integers that behave in a way that supports uniformity and collision resistance. We want that because evenly spread out hash values avoid collisions, which in turn leads to faster lookups. All this needs to be done deterministic, yet unpredictable. Hash functions must always give the same output for the same input, but that output should seem unrelated to the input structure. This is why we use XORs, bit operations, shifts, ...
### Universal Hashing
Because the above mentioned theoretical properties are usually not feasible in the real world, we introduce universal hashing. Universal hashing describes a hash function (family) where collisions between any two keys are guaranteed to be rare (≤ $1/m$), no matter which two keys you pick. 

We say the family is 𝑐-approximately universal if the family satisfies (for some $𝑐 > 0$) that collisions happen on average with a probability of $c/m$. 

**Strong universality** now means that besides the condition of the universal hashing strategies being fulfilled, the hash families also need to fulfill the pairwise independence condition. We can again generalize this too have c-approximately strongly universal hashing families. An example for a hashing strategy that fulfills these constraints is *strongly universal multiply-shift*.

Lastly, we define **k-wise independent** hashing families as expanding the strong universality constraints to more than two inputs. Here is an example of how all the strategies behave:
- **Universal hashing**: Each input value has a $1/m$ chance to land in each bin.
- **Strong universality hashing**: Any two inputs are independent in which bin they end up in.
- **k-wise independence hashing**: Any $k$ inputs are independent in which bin they end up in. 