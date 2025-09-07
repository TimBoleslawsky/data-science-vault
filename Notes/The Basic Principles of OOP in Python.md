## Abstraction
Abstraction is about hiding the internal complexity of a system and exposing only the necessary parts to the user. Like in this example, where the user does not need to know the logic behind the class `Complex` but can use it anyway.

``` Python
class Complex:
    # Constructor
    def __init__(self, real = 0, imag = 0):
        self.__real = real
        self.__imag = imag

    # Getter and Setter Methods
    @property
    def real(self): 
        return self.__real
    
    @real.setter
    def real(self, real): 
       self.__real = real

    @property
    def imag(self): 
        return self.__imag

    @imag.setter
    def imag(self, imag): 
       self.__imag = imag
    
    # Dunder Methods
    def __str__(self):
        if (self.imag > 0):
            return f'{self.real}+{self.imag}i'
        elif (self.imag < 0):
            return f'{self.real}{self.imag}i'
        else:
            return f'{self.real}'
    
    def __add__(self, other):
        return Complex((self.real + other.real), (self.imag + other.imag))
    
    def __sub__(self, other):
        return Complex((self.real - other.real), (self.imag - other.imag))

# User Input
z1 = Complex(1, 2)
z2 = Complex(5, -2)
z3 = Complex(-2, 3)
print(z1 + z2)
print(z3 - z1)
```

## Encapsulating
Encapsulation is about bundling the data (attributes) and methods (functions) that operate on that data into a single unit or class and restricting direct access to some of the object's components. Like in this example, where the `__balance` attribute is private and can only be accessed or modified through the provided methods

``` Python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}, new balance is ${self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}, new balance is ${self.__balance}")

    def get_balance(self):
        return self.__balance

# Creating an account object
account = Account("Alice", 500)
account.deposit(200)     # Output: Deposited $200, new balance is $700
account.withdraw(100)    # Output: Withdrew $100, new balance is $600
```

## Inheritance
Inheritance allows you to define a new class based on an existing class. This helps to establish a hierarchical relationship between classes and promotes code reusability. Like in this example, where the class `Car`inherits the method `start()`.

``` Python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting...")

class Car(Vehicle):  # Inherits from Vehicle
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  # Call the constructor of Vehicle
        self.num_doors = num_doors

    def open_trunk(self):
        print(f"Opening trunk of the {self.make} {self.model}")

class Motorcycle(Vehicle):  # Inherits from Vehicle
    def __init__(self, make, model, type_of_handlebar):
        super().__init__(make, model)
        self.type_of_handlebar = type_of_handlebar

    def pop_wheelie(self):
        print(f"{self.make} {self.model} is popping a wheelie!")

# Creating instances of Car and Motorcycle
car = Car("Toyota", "Camry", 4)
car.start()           # Output: Toyota Camry is starting...
car.open_trunk()      # Output: Opening trunk of the Toyota Camry
```

## Polymorphism
Polymorphism allows us to treat objects of different types in the same way by establishing a common interface. This can be done in various ways, such as inheritance or [[Abstract classes in Python|abstract classes]]. In the below example, we can iterate over all three objects and use the `color()`method, despite them being of different types. 

``` Python
class Vegetable:
    def color(self):
        print("I don't have a specific color")
        
class Carrot(Vegetable):
    def color(self):
        print("I am orange")

class Broccoli(Vegetable):
    def color(self): 
        print("I am green")

veg = Vegetable()
carrot = Carrot()
broccoli = Broccoli()

for obj in (veg, carrot, broccoli):
    obj.color()
```