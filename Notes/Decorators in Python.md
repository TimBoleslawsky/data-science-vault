## What Are Decorators?
A decorator is a function in Python that:
- takes another function as an argument (the "original function")
- and returns a wrapper function that calls the original function, but also performs additional operations before and after.

Example:

``` Python
def before_after(func):
	def wrapper():
		print("before calling the function")
		func()
		print("after calling the function")
	return wrapper

@before_after # this is equivalent to test = before_after(test)
def test():
	print("just testing ...")

test()
```

The original `test` function is replaced by the `wrapper` function returned by the decorator. And the output would be:
- "before calling the function"
- "just testing ..."
- "after calling the function"
## Decorating Class Methods
With the decorator `@property`, we can do two useful things within class methods:
- it allows us to treat a method like a class attribute:

``` Python
class Circle(object):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than zero!")
        else:
            self.radius = radius

    @property
    def circumference(self):
        return 3.1416 * self.radius * 2
```

- it allows us to implement very readable getter and setter methods:

``` Python
class Circle(): 
    def __init__(self, radius):
        self.__radius = radius
        #self.radius = radius # <- what does this do?

    @property
    def radius(self): 
        return self.__radius

    @radius.setter
    def radius(self, radius): 
        if radius < 0:
            raise ValueError("radius must be greater or equal to zero")
        else:
            self.__radius = radius
```