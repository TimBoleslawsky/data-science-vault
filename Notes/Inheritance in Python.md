## Single Inheritance
Here, a child class is derived only from one parent class. It is the simplest type of inheritance.

``` Python
class Vegetable(object):
    def __init__(self):
        print("It is a vegetable.")
        super().__init__()

class Cabbage(Vegetable):
    def __init__(self):
        print("It is a cabbage.")
        super().__init__()
```

## Multilevel Inheritance
In the case of multilevel inheritance, methods and properties of the base class and the derived class are inherited into the new derived class.

``` Python
class Vegetable(object):
    def __init__(self):
        print("It is a vegetable.")
        super().__init__()

class Cabbage(Vegetable):
    def __init__(self):
        print("It is a cabbage.")
        super().__init__()

class RedCabbage(Cabbage):
    def __init__(self):
        print("It is a red cabbage.")
        super().__init__()
```

## Multiple Inheritance
In the case of multiple inheritance, methods and properties of all the base classes are inherited into the derived class.

``` Python
class Vegetable(object):
    def __init__(self):
        print("It is a vegetable.")
        super().__init__()

class Broccoli(Vegetable):
    def __init__(self):
        print("It is a broccoli.")
        Vegetable.__init__(self)

class Cauliflower(Vegetable):
    def __init__(self):
        print("It is a cauliflower.")
        Vegetable.__init__(self)

class Broccoflower(Broccoli, Cauliflower):
    def __init__(self):
        print("It is a broccoflower.")
        Broccoli.__init__(self)
        Cauliflower.__init__(self)
```

**Problem,** this will output: *It is a broccoflower. It is a broccoli. It is a vegetable. It is a cauliflower. It is a vegetable.* To avoid this we will use `super()`

``` Python
class Vegetable(object):
    def __init__(self):
        print("It is a vegetable.")
        super().__init__()

class Broccoli(Vegetable):
    def __init__(self):
        print("It is a broccoli.")
        super().__init__() # "go to parent" -> not the case

class Cauliflower(Vegetable):
    def __init__(self):
        print("It is a cauliflower.")
        super().__init__()

class Broccoflower(Broccoli, Cauliflower):
    def __init__(self):
        print("It is a broccoflower.")
        super().__init__()
```

But why does this work? 
In multiple inheritance, super() does not necessarily refer back to the direct parents. It refers to the next item in the so-called method resolution order (MRO) from the perspective of who made the initial call. We can use `__mro__` or `mro()`to check the method resolution order (MRO).
### Passing Parameters in Multiple Inheritance
One way of doing it is to use keyword arguments in combination with `**kwargs` and "skim off" the parameters you need:

``` Python
class A: 
    def __init__(self, key_a, **kwargs):
        self.key_a = key_a
        super().__init__(**kwargs)

class B: 
    def __init__(self, key_b, **kwargs):
        self.key_b = key_b
        super().__init__(**kwargs)

class C(B, A): # Goal: populate with both parents keys using parent constructors
    def __init__(self, key_a, key_b):
        super().__init__(key_a=key_a, key_b=key_b)

    def print_your_keys(self):
        print(f"key_a = {self.key_a} and key_b = {self.key_b}")
```