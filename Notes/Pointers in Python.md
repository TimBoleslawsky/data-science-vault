A pointer is essentially a variable used to store the location of another variable present in the memory, i.e., pointers store memory addresses.
## Pointers and Functions
We have to be careful with pointers and functions because only 'easy' data elements are copied into a function, objects like Lists, Dict, Classes, ... are not and are therefore mutable!

``` Python
def dummy1(x: float):
    x1 = x*2

def dummy2(x: list):
    x2[2] = 5

x1 = 1
dummy1(x1)
x2 = [1,2,3,4]
dummy2(x2)

print(x1, x2)
# Output: 1 [1, 2, 5, 4]
```

In this example, we can see that the float `x1` is not manipulated by the function `dummy1`. On the other hand, the list `x2` is manipulated by the function `dummy2`.
