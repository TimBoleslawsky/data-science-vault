At the core of all computations is binary representation. Computers store data as **bits** (0s and 1s), which are grouped into **bytes** (8 bits). The resulting **bitstrings** have two noteworthy bits, the most-significant bit (MSB) is the left-most bit and the least-significant bit (LSB) is the right-most bit. Bitstrings can be numbered either in Little-Endian (LE) or Big-Endian (BE) order, depending on whether the little (LSB) or big (MSB) end comes first.

Different types of data—integers, floating-point numbers, and characters—are encoded in binary using different schemes:

• **Signed Integers** are a special case when talking about bit representation. We have a few different ways to represent them: 
	- Easiest is the signed magnitude representation, where the MSB is marked as 1. This is easy to understand, but leads to two zeros (+0,-0) and is mathematically impractical.
	- One's complement is the idea to flip all bits. This makes arithmetics simpler, but we still have two zeros.
	- Two's complement is an improvement of one's complement that is constructed by flipping all bits and adding one. This gets rid of the two zeros problem and handles overflow more gracefully.

• **Fractions** also need a special representation when using bit representation. We have two common ways to do this: 
	 - Fixed-point notation means that the binary point (like the decimal point) is fixed at a specific position. We allocate a fixed number of bits to the integer part and the fractional part.
	 - Floating-point notation means that the number is represented as: sign × mantissa × 2^exponent. The binary point “floats” — it’s not in a fixed position, meaning this supports a wide range of values (tiny and huge).
=> The de-facto standard for representing floating points is called IEEE 754 standard. Defines formats like: 32-bit (single precision) or 64-bit (double precision).