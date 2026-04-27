# class parent:
#     print("I am a parent")

# # p=parent()

# class child:
#     print("I am a child")

# c=child()

class parent:
    def parent_method(self):
        print("i am a parent")

# p=parent()
# p.parent_method()                        no need of creating a object for parent 

class child(parent):                            # we can use inherit parent class in child class and call the methos once
    def child_method(self):
        print("i am a child")

c=child()
c.parent_method()
c.child_method()


class animal:
    def eat(self):
        print("eating")
    
class dog(animal):
    def bark(self):
        print("barking")


d = dog()
d.eat()  # inherited
d.bark()  # own method


# Multilevel inheritance
class A:
    def show1(self):
        print("grandparent")

class B(A):
    def show2(self):
        print("Parent")
    
class C(B):
    def show3(self):
        print("Child")

c1=C()
c1.show1()
c1.show2()
c1.show3()

print()
# multiple inheritance
class father:
    def gardnening(self):
        print("gradening")
    
class mother:
    def badminton(self):
        print("badmintion")

class child(father,mother):
    pass

a=child()
a.badminton()
a.gardnening()