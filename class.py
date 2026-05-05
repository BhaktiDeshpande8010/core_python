class abc:                          #creating a class
    id=102                          #attribute
    name="Python class"

    def hello(self):
        print("I am a method")

a=abc()                             #object of the class
print(a.id)
print(a.name)
a.hello()                           #calling a method

b=abc()                             # we can create multiple object of the class
print(b.id)
print(b.name)


class xyz:
    id=0
    name=""

setattr(xyz,'id',101)
setattr(xyz,'name',"arjun")        # setattr is used to set the value

print(getattr(xyz,'id'))
print(getattr(xyz,'name'))         #getatter is used to get the value
