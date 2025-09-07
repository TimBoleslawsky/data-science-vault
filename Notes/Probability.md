## Interpretations of Probability
- **Frequentist interpretation** states that probability is the relative frequency of an event, subject to an infinite number of repetitions of a random experiment  
- **Bayesian interpretation** states that probability is the degree of belief in a hypothesis, subject to prior assumptions and observation of evidence
## Sample Space and Events
Probability is typically defined in terms of some **experiment**. An experiment must be **well-defined** and **random**. The **sample space**, Ω, of the experiment is the set of all possible outcomes (or sample points) of the experiment. All outcomes are **mutually exclusive** and the outcomes are **collectively exhaustive.** The **event**, E, is any subset of the sample space.
Example:
- Experiment: a die is rolled twice, each outcome (or sample point) is denoted by a pair $(i,j)$.
- Sample space: $Ω = {(1,1), (1,2), (1,3), ..., (6,6)}$
- Event: $𝐸 = {(1, 3), (2, 2), (3, 1)}$
## Probability
Given a sample space Ω, we can talk about the probability of event 𝐸, written P {𝐸 }. The probability of event 𝐸 is the probability that the outcome of the experiment lies in the set 𝐸.

Probability on events is defined via the Probability Axioms:
- Non-negativity: P {𝐸 } ≥ 0, for any event 𝐸. 
- Additivity: If 𝐸1, 𝐸2, 𝐸3, . . . is a countable sequence of events, with 𝐸𝑖 ∩𝐸 𝑗 = ∅, ∀𝑖 ≠ 𝑗, then P {𝐸1 ∪ 𝐸2 ∪ 𝐸3 ∪ · · · } = P {𝐸1} + P {𝐸2} + P {𝐸3} + · · · . 
- Normalization: P {Ω} = 1.

We say two Events $E1$ and $E2$ are **mutually exclusive** or **disjoint** if $𝐸1 ∩ 𝐸2 = ∅$. Then the probability $P$ of these two events can be calculated as P{$𝐸1$ ∪ $E2$} = P{$E1$} + P {$E2$}
Let's now say that Event $E$ and Event $F$ are not mutually exclusive Events. 
Then:  P{𝐸 ∪ 𝐹} = P{𝐸} + P{𝐹} − P{𝐸 ∩ 𝐹}
### Independence
Two events are independent if there is a chance that both events can happen at the same time.
The events 𝐴 and 𝐵 are independent if 𝑃 (𝐴 ∩ 𝐵) = 𝑃 (𝐴) * 𝑃(𝐵). 
Mutually exclusive events can not be independent because:
If $A$ and $B$ are mutually exclusive then P(𝐴 ∩ 𝐵) = ∅.

Example, let us roll a die twice:
- $𝐸1$ = Second roll is 4  
- $𝐸2$ = Difference between the two rolls is 4  
- $𝐸3$ = Difference between the two rolls is 3

$P(E1)$ = $1/6$ * $1$ = $1/6$
$P(E2)$ = $4/36$ = $1/9$
$P(E3)$ = $6/36$ = $1/6$

$E1 ∩ E2$ = ∅, therefore $P(E1 ∩ E2)$ = 0 which is not $P(E1) * P(E2)$ = $1/6 * 1/9$ 
$E1$ and $E2$ are not independent.

$E1 ∩ E3$ = {(1,4)}, therefore $P(E1 ∩ E3)$ = $1/36$ which is $P(E1) * P(E3)$ = $1/6 * 1/6$ 
$E1$ and $E3$ are independent.
### Conditional Probabilities on Events
The conditional probability of event 𝐸 given event 𝐹 is written as 
$P${$𝐸 | 𝐹$} and is given by the following, where we assume $P${𝐹} $> 0$: 
$P${$𝐸 | 𝐹$} = $P${$𝐸 ∩ 𝐹$} $/$ $P${𝐹} which is the same as $P${$𝐸 | 𝐹$} = $P${$F|E$} * $P$ {$E$} $/$ $P${𝐹} (Baye's theorem).

$P$($𝐸 | 𝐹$) should be thought of as the probability that event 𝐸 occurs, given that we have narrowed our sample space to points in 𝐹.

If two events are conditional then we calculate the scenario "E and F" as follows: 
$P$($𝐸 ∩ 𝐹$) = $P(E|F) * P(F)$

Example:
A bomb detector alarm lights up with a probability of 0.99 if a bomb is present. If no bomb is present, the bomb alarm still (incorrectly) lights up with a probability of 0.07. Suppose that a bomb is present with a probability of 0.05.

Given
- $P(Alarm∣Bomb)=0.99$ — the probability that the alarm goes off if a bomb is present (true positive).
- $P(Alarm∣¬Bomb)=0.07$ — the probability that the alarm goes off if there is no bomb (false positive).
- $P(Bomb)=0.05$ — the probability that there is a bomb.
- $P(¬Bomb)=0.95$ — the probability that there is no bomb.

Calculations
- $P(Alarm∩Bomb)=P(Alarm∣Bomb)⋅P(Bomb) =  0.99⋅0.05 = 0.0495$
- $P(Alarm∩¬Bomb) = P(Alarm∣¬Bomb)⋅P(¬Bomb)=0.07⋅0.95=0.0665$
- $P(¬Alarm∩Bomb)=P(¬Alarm∣Bomb)⋅P(Bomb)=0.0005$
- $P(¬Alarm∩¬Bomb)=P(¬Alarm∣¬Bomb)⋅P(¬Bomb) = 0.93⋅0.95=0.8835$
- $P(A) = P(Alarm∣Bomb) * P(Bomb) + P(Alarm∣¬Bomb) * P(¬Bomb) = 0.99 * 0.05 + 0.07 * 0.95 = 0.116$
- $P(B | A) =  P(A|B) * P(B) / P(A) = 0.99 * 0.05 / 0.116 = 0.4267$

Table of probabilities: 

|             | **Alarm** | **No Alarm** | **Total** |
| ----------- | --------- | ------------ | --------- |
| **Bomb**    | 0.0495    | 0.0005       | 0.05      |
| **No Bomb** | 0.0665    | 0.8835       | 0.95      |
| **Total**   | 0.116     | 0.884        | 1.00      |