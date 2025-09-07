## Constraint Satisfaction Problems
The basic idea of CSPs is simple: A **Constraint Satisfaction Problem (CSP)** is a mathematical problem defined by:
1. **Variables**: A set of variables  $X_1, X_2, …, X_n$.
2. **Domains**: Each variable has a domain of possible values (e.g.,  $D_1, D_2, …, D_n$).
3. **Constraints**: Rules that specify which combinations of values for the variables are valid.
=> The goal in CSPs is to assign values to all variables while satisfying all constraints.
## Constraint Programming
Constraint programming is a tool to solve CSPs or [[Optimization Problems|optimization problems]]. When solving these problems we usually take one of two approaches:
- Refinement model: variables in the problem are initially unassigned, and each variable is assumed to be able to contain any value included in its range or domain. 
- Perturbation model: variables in the problem are assigned a single initial value. At different times one or more variables receive perturbations (changes to their old value), and the system propagates the change trying to assign new values to other variables that are consistent with the perturbation.

Based on these approaches, the following methods exist:
- **Backtracking**: A **systematic search algorithm** for CSPs. It incrementally assigns values to variables and checks if the constraints are satisfied. If a conflict arises, it **backtracks** to the previous variable and tries a different value.
	- Simple but can be slow for large problems.
- **Constraint Propagation**: A technique to **reduce the search space** by inferring new constraints from existing ones. It updates the definition of constraints to eliminate values that violate constraints, making it easier to solve the problem.
- **Local Search**: A **heuristic-based approach** that works by iteratively improving a complete but possibly invalid solution. It starts with an initial assignment and makes small changes (e.g., swapping variable values) to reduce constraint violations.
	- Doesn’t guarantee a solution but is fast and effective for large-scale CSPs.
- **Dynamic programming**: A method that refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a manner.