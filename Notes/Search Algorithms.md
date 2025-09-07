## Linear Search:

``` Python
def linear_search(L, element):
    for i in L:
        if i == element:
            return True
    return False
# Time complexity = O(n)
```

## Binary search for Sorted List:
- Pick an index `i`, that divides the list into two halves.
- Check if `L[i] == element`.
- If not, check if `L[i] > element` or `L[i] < element`.
- Depending on the answer, search left or right half of L for the element.
-> Time complexity = O(log(n))
## MCTS
The Monte Carlo Tree Search algorithm is a popular algorithm for game playing and decision-making problems especially in combination with machine learning and AI. More on MCTS here: [[Monte Carlo Tree Search and Game Playing]].