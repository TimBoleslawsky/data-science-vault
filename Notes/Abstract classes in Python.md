Abstract classes serve a very similar purpose to inheritance regarding polymorphism. The difference is that with abstract classes we establish a "contract" for polymorphism by requiring subclasses to provide their own implementation for abstract methods.

Python does not have abstract classes by default. But, it has a module (called ABC) that defines Abstract Base Classes (therefore the name ABC).

``` Python
from abc import ABC, abstractmethod

class Vegetable(ABC):
    @abstractmethod
    def color(self):
        print("I am a vegetable")

# This does not work
class Carrot(Vegetable):
    pass

# This works
class Carrot(Vegetable):
    def color(self):
        super().color()
        print("I am orange")
```