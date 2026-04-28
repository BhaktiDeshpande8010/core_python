from abc import ABC,abstractclassmethod

class Payment(ABC):
    def print_slip(self,amount):
        print("Your payment was done with Rs.",amount)

    @abstractclassmethod
    def payment(self):
        print("a")      #this section will not get print this is the abstract code the hidded  one

class credit(Payment):
    def payment(self,amount):
        print("Credit crd payment done with Rs.",amount)

c=credit()
c.payment(1000)
c.print_slip(5000)  


# Example2
class vehicle(ABC):
    def start_engine(self):
        print("Engine started")

    @abstractclassmethod
    def fuel_type(self):
        pass

class petrolcar(vehicle):
    def fuel_type(self):
       print("Fuel type : Petrol")

class Electric(vehicle):
    def fuel_type(self):
       print("Fuel type : Electric")


p=petrolcar()
p.fuel_type()

e=Electric()
e.fuel_type()


from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def info(self):
        print("This is a shape")



# Child class 1
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# Child class 2
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Usage
c = Circle(5)
print("Circle Area:", c.area())
c.info()

print("-----")

r = Rectangle(4, 6)
print("Rectangle Area:", r.area())
r.info()
