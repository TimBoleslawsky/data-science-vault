## What is an Algorithm?
*An Algorithm is a well-defined computational procedure that takes some value, or a set of values, as input and produces some value, or set of values as output. An algorithm is thus a sequence of computational steps that transform input into output.

For examples of sort and searching algorithms look here: [[Sort Algorithms]]
## Analysis of Algorithms
**Correctness
- Does the algorithm do what it is supposed to do?
- Is it enough to test an algorithm on some instances?

**Running time or Complexity
- How much 'time' does the algorithm take?
- How do we measure the running time?
-> To measure the complexity of an algorithm we use *Big Oh*!
### Big Oh
Big Oh is a simplified analysis of an algorithm's complexity or efficiency. 
- The complexity is measured in terms of the input size $n$
- Big Oh is machine-independent
- Big Oh always assumes the worst case

Basic Examples:

``` Python
x = 5 + 10 # This line of code has a complexity of O(1) or constant time

for x in l:
	print x # this for loop has a complexity of O(n) or linear time

for x in l:
	for y in l:
		print x*y # this nested loop has a complexity of O(n^2) or quadratic time
```

Rules for working with Big Oh:
- We ignore constants:

``` Python
x = 5 + 10 
y = 10 + 5 # These two lines of code have 2*O(1) but because we don't care about constants we still say they have O(1)
```

- certain terms 'dominate' others:

``` Python
x = 5 + 10 # O(1)

for x in l:
	print x # O(n)

for x in l:
	for y in l:
		print x*y # Because this has the highest complexity O(n^2) we say that the whole code block has a complexity of O(n^2).
# o(1) < O(log(n)) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!)
```

## Design Principles of Algorithms
### Greedy
A **greedy algorithm** makes a series of choices, each of which looks optimal at the moment (**locally optimal**), with the hope that the end result will be a globally optimal solution. The algorithm does not reconsider previous decisions, assuming that choosing what looks best at each step, will lead to the optimal solution overall (**Non-reversible**.

Example, Knapsack Problem:
- Given n objects and a *knapsack*.
- Each object (also called item) i has weight $w_{i} \gt 0$ and has value $v_{i}$.
- Knapsack has capacity of $W$.
- Goal is to maximise total value without overfilling knapsack.

-> Greedy approach could e.g. be to take the most valuable item until knapsack is full.
### Divide & Conquer
**Divide and Conquer** involves breaking a problem into smaller sub-problems, solving each sub-problem independently, and then combining their results to solve the original problem. This approach is effective when the sub-problems are similar in nature but smaller in scale.

Examples would be binary search or merge sort algorithms.
### Dynamic Programming
**Dynamic Programming** solves complex problems by breaking them down into overlapping sub-problems and solving each sub-problem only once. It stores the results of these sub-problems (usually in a table). 
- **Overlapping Sub-problems:** The same sub-problems are solved multiple times. DP solves each sub-problem only once and stores its result.
- **Optimal Substructure:** The optimal solution to a problem can be constructed from the optimal solutions to its sub-problems.

Example, Knapsack Problem:
- Given n objects and a *knapsack*.
- Each object (also called item) i has weight $w_{i} \gt 0$ and has value $v_{i}$.
- Knapsack has capacity of $W$.
- Goal is to maximise total value without overfilling knapsack.

-> Dynamic programming approach would be to iterate over all items and the capacity and evaluate all possible solutions by storing them in a table and comparing them. 