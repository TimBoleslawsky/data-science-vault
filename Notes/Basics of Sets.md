## Definition
"*A set is a collection of things, the things are elements of the set.*"
- Set builder definition: 𝑆 = {expression ∣ rule}
		- Example: $S$ = {5𝑥 − 1 | 𝑥 ∈ ℤ} = {... , −6, −1,4,9, ... }
		- Explanation: For the value $4$ we can find a 𝑥 ∈ ℤ such that $5x - 1 = 4$, this value is $x=1$. Let's take the value $3$. There exists no value for 𝑥 ∈ ℤ such that $5x - 1 = 3$. Therefore $3$ is not in the set $S$.
## Intervals
Closed interval \[𝑎, 𝑏] = {𝑥 ∈ ℝ ∣ 𝑎 ≤ 𝑥 ≤ 𝑏}  
Open interval (𝑎, 𝑏) = {𝑥 ∈ ℝ ∣ 𝑎 < 𝑥 < 𝑏}
## Operators
**Subsets**
𝐴 ⊆ 𝐵, 𝐴 is a subset of 𝐵, if all elements of 𝐴 are also elements of 𝐵
- If 𝐴 ⊆ 𝐵, but 𝐴 ≠ 𝐵, then 𝐴 is a proper subset of 𝐵: A ⊊ 𝐵
- Example: The subsets of {1,2,3,4} are  
∅, {1} , {2} , {3} , {4} , {1,2} , {1,3} , {1,4} , {2,3} , {2,4} , {3,4} , {1,2,3} , {1,2,4} , {1,3,4} , {2,3,4} , {1,2,3,4}

**Union**
𝑆 = 𝐴 ∪ 𝐵 is the union of sets 𝐴 and 𝐵 if it contains every element that is a member of 𝐴, 𝐵, or both:  
![test](https://upload.wikimedia.org/wikipedia/commons/3/30/Venn0111.svg)

**Intersection**
𝑆 = 𝐴 ∩ 𝐵 is the intersection of sets 𝐴 and 𝐵 if it contains every element that is a member of both 𝐴 and 𝐵:
![](https://upload.wikimedia.org/wikipedia/commons/9/99/Venn0001.svg)

**Difference**
𝑆 = 𝐴 ∖ 𝐵 is the difference of sets 𝐴 and 𝐵 if it contains every element of 𝐴 that is not in 𝐵:
![](https://upload.wikimedia.org/wikipedia/commons/e/e6/Venn0100.svg)

**Complement**
The complement of 𝐴, denoted Ā, is the set of all elements of the universe not in 𝐴,  
that is Ā = 𝑈 ∖ 𝐴:
![](https://upload.wikimedia.org/wikipedia/commons/e/eb/Venn1010.svg)

**Examples**
Suppose 𝐴 = {4,3,6,7,1,9}, 𝐵 = {5,6,8,4} , 𝐶 = {5,8,4} and and 𝑈 = {0,1,2, ... , 10}
- 𝐴 ∪ 𝐵 = {4,3,6,7,1,9,5,8}  
- 𝐴 ∩ 𝐶 = {4}  
- 𝐴 ∖ 𝐶 = {3,6,7,1,9}
- Ā = {0,2,5,8,10}
## Partitions of Sets
A partition of a set 𝐴 is a set of non-empty subsets of 𝐴 such that their union equals 𝐴 and  
the intersection between any two sets is empty.
Example: Let 𝐴 = {𝑎, 𝑏, 𝑐}. The partitions of 𝐴 are  
- {{𝑎, 𝑏, 𝑐}}  
- {{𝑎}, {𝑏, 𝑐}}  
- {{𝑎, 𝑏}, {𝑐}}  
- {{𝑎, 𝑐}, {𝑏}}  
- {{𝑎} ,{𝑏}, {𝑐}}  

• The number of partitions of a set of 𝑛 elements is known as the Bell number 𝐵"  
• [Equivalence classes](Relations.md#equivalence-relations) form a partition of a set!
