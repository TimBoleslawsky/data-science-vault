## Generators
*At its most basic, a generator is a function that returns an iterable set of values. Generators avoid creating a list or other data structure in memory to store the values as they are produced, instead replacing them one by one over time. This makes them more efficient than loops for large datasets and allows for code that runs in linear time.*

Definition: 

``` python
def loopGenerator(x):
	for i in range(x):
		yield i

gen = loopGenerator(6)

for val in gen:
	print(val, end=" ")
```

We can also use [[List comprehension]] to create generators.
### Advantages of Generators

- **Efficient**: Python Generators are more efficient than loops for large datasets, as they produce values one by one instead of storing them in memory before returning them.
- **Memory Management**: As generators produce values one by one rather than storing them in a list or other data structure, they also require less memory and can process large datasets without much RAM.
- **Time-Saving**: Generators in Python can also save time as they do not need to wait for the entire sequence to be generated before returning them, allowing code to execute in linear time.
- **Infinite Sequences**: Generators can produce infinite sequences, which is helpful for tasks such as stream processing or other activities requiring continuing input.
## Lambda Functions

- We can use *lambda* functions when a small anonymous function is required for a short period of time. 
- Lambda functions are mostly used inside another function such as map(), filter(), or reduce(). 
- Can take any number of arguments, but can only have one expression.

Example: 

``` python
def square(x):
	return x**2

numbers = [1, 2, 3, 4]

# Apply square function to each item of numbers
sqrList = map(square, numbers)

while True:
	try:
		print("Received on next(): ", next(sqrList))
	except StopIteration:
		break
```

``` python
# We can shorten the code in the above cell using map with lambda expression
sqrList = map(lambda x: x**2, [1, 2, 3, 4])

while True:
	try:
		print("Received on next(): ", next(sqrList))
	except StopIteration:
		break
```
