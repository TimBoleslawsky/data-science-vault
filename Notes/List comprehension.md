**List comprehension** is a concise and readable way to create lists or generators in Python. It allows you to generate new lists by applying an expression to each item in an existing iterable (like a list, tuple, or range) and optionally including conditions to filter items.

**List**
Example using a for loop:

``` Python
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Example using list comprehension:

``` Python
squares = [x**2 for x in range(10)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Generator**
Example using a for loop:

``` python
def loopGenerator(x):
	for i in range(x):
		yield i**2

gen2 = loopGenerator(6)

for val in gen2:
	print(val, end="\n")
```

Example using list comprehension:

``` python
gen = (x**2 for x in range(6)) # This creates the generator

for value in gen:
	print(value)
```
