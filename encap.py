# encapsulation 
# access modifier :public

class python:
    id=0;
    name=""

    def __init__(self,id,name):
        self.id=id
        self.name=name

        # print(self.id)
        # print(self.name)

p=python(101,"program")
print(p.id)
print(p.name)


# private access modifier
class temp:      
    __id=0;                               #use to __(sunder )
    __name=""

    def __init__(self,__id,__name):
        self.__id=__id
        self.__name=__name

        print(self.__id)
        print(self.__name)

t=temp(101,"program")


class fortune:
    _cyber="security"
    _wifi="5g"

class cravita(fortune):
    # def __init__(self):
    #     print(self._wifi)
    #     print(self._cyber)

    def profile(self):
        print(self._wifi)
        print(self._cyber)

c=cravita()



print("-----------------")

class Student:
    name = ""
    rollno = 0

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

s = Student("Rahul", 25)

print("Public Data")
print(s.name)
print(s.rollno)


# Private Access Modifier
class Bank:
    __balance = 0

    def __init__(self, balance):
        self.__balance = balance

    def showBalance(self):
        print("Balance =", self.__balance)

b = Bank(50000)

print("\nPrivate Data")
b.showBalance()

# print(b.__balance)   # Error because it is private


# Protected Access Modifier
class Employee:
    _salary = 45000
    _department = "IT"

class Manager(Employee):

    def display(self):
        print("\nProtected Data")
        print("Salary =", self._salary)
        print("Department =", self._department)

m = Manager()
m.display()