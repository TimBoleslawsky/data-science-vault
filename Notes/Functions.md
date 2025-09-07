## Definition
Let 𝐴 and 𝐵 be sets. A function from 𝐴 to 𝐵, denoted 𝑓 ∶ 𝐴 → 𝐵, is a relation from 𝐴 to 𝐵  
satisfying the property that for each 𝑎 ∈ 𝐴, the relation 𝑓 contains exactly one ordered pair  
of form (𝑎, 𝑏). The statement (𝑎, 𝑏) ∈ 𝑓 is abbreviated 𝑓(𝑎) = 𝑏

Functions are also called **maps**: a function unambiguously maps a value from one set to a  
value in another set.  
For a function, 𝑓 ∶ 𝐴 → 𝐵, the set 𝐴 is called the **domain** of the function (“What kind of values  
are mapped?”). The set 𝐵 is called the **codomain** of the function (“What kind of values do they map to?”). The **range** or **image** of the function is the set {𝑓 𝑎 ∣ 𝑎 ∈ 𝐴}, the set of all values mapped to by 𝑓. The image of the function is a subset of the codomain. The **preimage** correspondingly is the set of elements in 𝐴 that are mapped to the values in 𝑌 by 𝑓.
Example:  
- Suppose 𝐴 = {𝑎, 𝑏, 𝑐, 𝑑}, 𝐵 = {2,3,4,5,6}, and 𝑓 = {(𝑎, 2), (𝑏, 3), (𝑐, 4), (𝑑, 5)}  
- The domain of 𝑓 is 𝐴  
- The codomain of 𝑓 is 𝐵  
- The range of 𝐵 is {2,3,4,5} ⊊ 𝐵  
- The preimage of $B$ is {a, b, c, d}
- 𝑓(𝑏) = 3  
- 𝑓(𝑑) = 5
## Characteristics of Functions
**Equality**
Two functions 𝑓 ∶ 𝐴 → 𝐵 and 𝑔 ∶ 𝐴 → 𝐷 are equal if 𝑓(𝑥) = 𝑔(𝑥) for every 𝑥 ∈ 𝐴.

**Injectivity**
A function 𝑓 ∶ 𝐴 → 𝐵 is injective (“one-to-one”) if there are no two distinct values in the domain that map to the same value in the codomain.

**Surjectivity**
A function 𝑓 ∶ 𝐴 → 𝐵 is surjective (“onto 𝐵”) if every value in the codomain is mapped to.

**Bijectivity**
A function 𝑓 ∶ 𝐴 → 𝐵 is bijective (“one-to-one correspondence”) if 𝑓 is both injective and  
surjective. That is, there is an unambiguous correspondence between the elements of the domain and the codomain.
- Bijective functions are invertible: every element in the domain is mapped to exactly one element in the codomain and vice versa.

=> The Pigeonhole Principle:
- Consider 𝐴 as the set of pigeons and 𝐵 as the set of holes. 
- Then:
	- If |𝐴| > |𝐵|, 𝑓 cannot be injective  
	- If |𝐴| < |𝐵|, 𝑓 cannot be surjective

