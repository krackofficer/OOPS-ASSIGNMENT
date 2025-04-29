
# OOPS Assignment Solutions

# 1. What are the five key concepts of Object-Oriented Programming (OOP)?
# - Encapsulation
# - Abstraction
# - Inheritance
# - Polymorphism
# - Composition

# 2. Write a Python class for a `Car` with attributes for `make`, `model`, and `year`. Include a method to display the car's information.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

# 3. Explain the difference between instance methods and class methods. Provide an example of each.
class Example:
    count = 0

    def __init__(self):
        Example.count += 1

    def instance_method(self):
        print("This is an instance method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method. Total instances: {cls.count}")

obj = Example()
obj.instance_method()
Example.class_method()

# 4. How does Python implement method overloading? Give an example.
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

op = MathOperations()
print(op.add(5))
print(op.add(5, 10))
print(op.add(5, 10, 15))

# 5. What are the three types of access modifiers in Python? How are they denoted?
class Employee:
    def __init__(self):
        self.name = "John"       # Public
        self._salary = 50000     # Protected
        self.__ssn = "123-45-6789"  # Private

# 6. Describe the five types of inheritance in Python. Provide a simple example of multiple inheritance.
class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: Painting")

c = Child()
c.skills()

# 7. What is the Method Resolution Order (MRO) in Python? How can you retrieve it programmatically?
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())

# 8. Create an abstract base class `Shape` with an abstract method `area()`. Then create two subclasses `Circle` and `Rectangle` that implement the `area()` method.
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

c = Circle(5)
r = Rectangle(4, 6)
print(c.area())
print(r.area())

# 9. Demonstrate polymorphism by creating a function that can work with different shape objects to calculate and print their areas.
def print_area(shape):
    print(f"The area is {shape.area()}")

circle = Circle(3)
rectangle = Rectangle(2, 5)

print_area(circle)
print_area(rectangle)

# 10. Implement encapsulation in a `BankAccount` class with private attributes for `balance` and `account_number`. Include methods for deposit, withdrawal, and balance inquiry.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

acc = BankAccount("12345")
acc.deposit(1000)
acc.withdraw(500)
print(acc.get_balance())

# 11. Write a class that overrides the `__str__` and `__add__` magic methods.
class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Number: {self.value}"

    def __add__(self, other):
        return Number(self.value + other.value)

num1 = Number(10)
num2 = Number(20)
result = num1 + num2
print(result)

# 12. Create a decorator that measures and prints the execution time of a function.
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    print("Function Complete!")

slow_function()

# 13. Explain the concept of the Diamond Problem in multiple inheritance. How does Python resolve it?
# The Diamond Problem occurs when a class inherits from two classes that both inherit from a common base class.
# Python resolves this using the C3 Linearization (MRO).

# 14. Write a class method that keeps track of the number of instances created from a class.
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
print(Counter.get_instance_count())

# 15. Implement a static method in a class that checks if a given year is a leap year.
class Calendar:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(Calendar.is_leap_year(2024))
print(Calendar.is_leap_year(2023))
