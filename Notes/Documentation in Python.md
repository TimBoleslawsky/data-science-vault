By adding documentation to a function we can access this function via the below shown function call. This is called *docstring*.

This can also be done with standard functions like *print()*.

```
def multiply(x, y):
	"""Multiplies the two integer parameters.
	
	Parameters:
	----------
	x: an integer
	y: an integer
	
	Returns
	-------
	The result of multiplying x and y.
	"""
	
	result = x * y
	return result


print(multiply.__doc__)
```