In this note I want to discuss the implementation and evaluation of **Murmur3_32**, a _practical, non-cryptographic hash function_. The main goal of the Murmur3_32 hash function is to take an input string (of any length), and turn it into a 32-bit integer hash. 

The basic implementation of the Murmur3_32 hash function looks like this: 

```python
def murmur3_32(key, seed):
	"""Computes the 32-bit murmur3 hash"""
	
	key_bytes = key.encode('utf-8')
	length = len(key_bytes)
	nblocks = length // 4
	
	h1 = seed
	c1 = 0xcc9e2d51
	c2 = 0x1b873593
	
	# Body
	for i in range(nblocks):
		i4 = i * 4
		# converting four bytes from a bytes object into a 32-bit integer using little-endian byte order.
		k1 = (
			key_bytes[i4 + 0]
			| (key_bytes[i4 + 1] << 8)
			| (key_bytes[i4 + 2] << 16)
			| (key_bytes[i4 + 3] << 24)
		)
		k1 = (k1 * c1) & 0xffffffff
		k1 = rol32(k1, 15)
		k1 = (k1 * c2) & 0xffffffff
		
		h1 ^= k1
		h1 = rol32(h1, 13)
		h1 = (h1 * 5 + 0xe6546b64) & 0xffffffff
	
	# Tail
	tail = key_bytes[nblocks * 4:]
	k1 = 0
	if len(tail) >= 3:
		k1 ^= tail[2] << 16
	if len(tail) >= 2:
		k1 ^= tail[1] << 8
	if len(tail) >= 1:
		k1 ^= tail[0]
		k1 = (k1 * c1) & 0xffffffff
		k1 = rol32(k1, 15)
		k1 = (k1 * c2) & 0xffffffff
		h1 ^= k1
	
	# Finalization
	h1 ^= length
	h1 ^= h1 >> 16
	h1 = (h1 * 0x85ebca6b) & 0xffffffff
	h1 ^= h1 >> 13
	h1 = (h1 * 0xc2b2ae35) & 0xffffffff
	h1 ^= h1 >> 16
	
	return h1
```

The Murmur3_32 hash function consists of four basic blocks:
- First, we initialize the seed, and some constants. We prepare the key (the string to be hashed) to be UTF-8.
- Second, we process 4 bytes at a time and do some operations on them. 
- Third, we process the left overs (the tail). If the key had more bytes than the multiple of 4 accounted for, these left over bytes also need to be processed.
- Lastly we do some final operations to ensure that every input bit has an effect on the output (this makes the output more uniform).

Murmur3_32 is not strongly universal or k-wise independent in the theoretical sense, but it is empirically very good and it’s fast and practical. We will prove that now by checking two things: Uniformity & Collision Probability. 

We do this by mapping the hash values for some body of text to the buckets they land in and look at how many hash values land in each bucket. We also want to look at the probability of the collisions. Doing this we get the following results: 
- Mean: 3287.26, this is just the total keys to be hashed divided by 128 
- Std Dev: 57.34, this means that most buckets are within a very small margin of error from each other.
  => Uniform distribution is good.
- Collisions: 691,588,133
- Collision probability: 0.007812519, this probability is almost identical to the theoretical probability for a uniform random hash into 128 buckets which is:$\Pr[h(x) = h(y)] = \frac{1}{m} = \frac{1}{128} \approx 0.0078125$.
  => Collision Probability is low. 

