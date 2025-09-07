Probabilistic data structures are space- and time-efficient data structures that provide approximate solutions to problems where exact answers are either unnecessary or too costly to compute. They trade a small and well-defined probability of error for significant gains in performance and memory usage. They use randomization or [[Hashing#Hash Functions|hash functions]] to manage data.
## Bloom Filters
Problem: Set membership, Is the given object an element of the set (in the dataset)?
- Possible solution => Python set, works, but, since all values are stored explicitly, too much large.
- Another solution are **bit vectors**. They represent a universe as a row of $n$ bits, where $n$ is the size of the universe. For example set $S={1,2,4}$ of universe $|U|=8$ could be presented as: 
  $1101000$. The set 𝑆 could then be written in hex as 0x26. **Bloom filters are an extension of this idea**.

A Bloom filter is a bit vector of specified length 𝑚 that is filled with pre-specified 𝑘  
hash functions $h_1, h_2, ... , ℎ_k ∶ 𝑈 → [𝑚]$. Bloom filters work like so: 
- Initially, all elements of the filter are set 0.
	- Example: $m=11$, $k=3$. => $00000000000$
- Adding the first element 𝑥 gives us the following values for the hash functions: $h_1 = 3, h_2 = 5, h_3 = 11$. => $00101000001$ 
- Adding a second element $y$ gives us the following values for the hash functions: $h_1 =5, h_2=6, h_3 = 9$. => $00101100101$ (5 twice does nothing)
- Querying for element 𝑧 gives us the following values for the hash functions: $h_1 = 5, h_2 = 6, h_3 = 8$ => Because one of these is not set to 1 we conclude that $z$ is not in the set.

It is important to note that Bloom filters are subject to false positives, meaning that sometimes we say that the element is in the set even though it is not. This happens with probability: $P_{fp} \approx \left(1 - e^{-kn/m}\right)^k$

Another important note on the cache behavior of Bloom filters. If 𝑚 is very large, then each bit that needs to be set during insertion is probably going to be in a different cache line, both in time and space leading to cache misses. We can solve this via **blocking**. The idea is that instead of one very long Bloom filter, we store cache-line-length Bloom filters and use the first hash value to select the block and store bits then within the block (this does obviously require more space but does somewhat solve the cache misses problem).
## HyperLogLog
Problem: Estimate the cardinality (number of distinct elements).
- Possible solution => Python set, just add all elements in the hash table and compute len(). Works, but requires potentially a prohibitive amount of space.
- Another solution: We can reinterpret Bloom filters as sketches (a randomized summary that approximates a quantity) for estimating the number of distinct elements by analyzing the fraction of zero bits in the filter. If we reduce the number of hash functions to k = 1, we get a simplified version called **linear counting**, which still allows us to estimate cardinality. However, linear counting requires $O(n)$ space, which limits its scalability for very large datasets. 

The idea behind HyperLogLog is this: 
- we estimates the number of distinct elements by looking at how many **leading zeros** appear in hash values. 
	- These are **rare** patterns. As you process more distinct elements, you’re **more likely** to encounter these rare patterns — and this tells you that your set is large. 
- For estimating the number of leading zeros we use the function $ρ(x)$. 
	- Examples: $\rho(00101\ldots) = 3$, $\rho(00000001) = 8$. 
	- Because we assume the hash values to be uniformly distributed, the probability of seeing a hash with at least r leading zeros is: $\Pr[\rho(x) \geq r] = 2^{-r}$. Looking at this in the context of the geometric distribution, the expected value of the maximum $\rho(x)$ observed among $n$ distinct items is roughly $\max \rho(x) \approx \log_2 n$.
- HyperLogLog improves accuracy by splitting the data into many parts (sub-streams) using a second hash function and tracking the largest number of leading zeros ($ρ(x)$-value) seen in each part (register).
- The estimated number of distinct elements is calculated by taking the harmonic mean of the values stored in the registers.
	- (There are more nuanced solutions within the algorithm for very small and very large estimates.)

When adding a new element to a HyperLogLog data structure: 
- One hash function chooses which register to update.
- A second hash function determines the value of $\rho(x)$.
- The register is updated with the maximum $\rho$-value observed so far.

The result of this is that HyperLogLog achieves major space savings by storing only small summaries (maximum leading zero counts), which take up much less space than the actual elements. While a naive set would require $O(n \log n)$ bits, HyperLogLog only uses $O(m \log \log n)$ bits.

As HyperLogLog is an probabilistic data structure we have some error margin. The standard error of HyperLogLog is approximately $\frac{1.04}{\sqrt{m}}$. So increasing the number of registers reduces the error.