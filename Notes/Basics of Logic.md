## Definition
"*Logic is the study of correct reasoning. A statement within logic is a sentence or mathematical expression that is definitely true or false.*"

Statements can contain variables:  
- 𝑄(𝑥): The integer 𝑥 is even  
- If the trueness of the sentence depends on a variable, we say it is an **open statement** or a **predicate**  
- For example, 𝑄(2) is true, but 𝑄(3) is false
## Operators
**And, Or, Not**
Statements can be combined with connectives or logical operators to yield more complex statements. The most common connectives are and (∧), or (∨), and not (¬).

**Implication**
"If-then" statements are captured by the implication 𝑃 ⇒ 𝑄  (“𝑄 is true under the condition that 𝑃 is true”). The implication can also be stated as ¬𝑃 ∨ 𝑄.

**Equivalence**
If the two statements always take the same truth values, they are said to be equivalent 𝑃 ⇔ 𝑄. Equivalence is the same as implication in both directions, 
so 𝑃 ⇔ 𝑄 is the same as 𝑃 ⇒ 𝑄 ∧ (𝑄 ⇒ 𝑃).

**De Morgan's law**
• ¬ 𝑃 ∧ 𝑄 ⟺ ¬𝑃 ∨ ¬𝑄  
• ¬ 𝑃 ∨ 𝑄 ⟺ ¬𝑃 ∧ ¬𝑄

**Example**
- 𝑅: “It is raining”  
- 𝑈: “I have an umbrella”  
- 𝑊: “I will get wet”  
- 𝑅 ∧ ¬𝑈 ⇒ 𝑊  “if it is raining AND I do NOT have an umbrella, THEN I will get wet”
Truth table:

| R   | U   | W   | ¬U  | R ∧ ¬U | (R ∧ ¬U) ⇒ W | ¬R ∨ U ∨ W |
| --- | --- | --- | --- | ------ | ------------ | ---------- |
| F   | F   | F   | T   | F      | T            | T          |
| F   | F   | T   | T   | F      | T            | T          |
| F   | T   | F   | F   | F      | T            | T          |
| F   | T   | T   | F   | F      | T            | T          |
| T   | F   | F   | T   | T      | F            | F          |
| T   | F   | T   | T   | T      | T            | T          |
| T   | T   | F   | F   | F      | T            | T          |
| T   | T   | T   | F   | F      | T            | T          |

- We can remove the implication: ¬ 𝑅 ∧ ¬𝑈 ∨ 𝑊  
- We can apply De Morgan’s law: ¬𝑅 ∨ 𝑈 ∨ 𝑊  
- “It is NOT raining OR I have an umbrella OR I get wet

