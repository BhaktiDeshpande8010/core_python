# class histrory:
#     def show(self):                  #methos
#         print("I'm show method")
    
#     def __init__(self):
#         print("I'm Constructor")

# h=histrory()                #constructor called
# h.show() 


# # parameterized constructor 
# class marathi:
#     id=0
#     name=""

#     def __init__(self,id,name):
#         self.id=id
#         self.name=name


# m=marathi(101,"subject")
# print(m.id)
# print(m.name)


# assign out of block
class A:
    id = 0
    name = ""

    def show(self):
        print("I am a show method")

a = A()
a.show()

# assign values outside class
a.id = 102
a.name = "Java"

print(a.id)
print(a.name)


print("----------------")

# default
class car:
    def __init__(self):
        self.make="toyata"
        self.model="corolla"
        self.year = 2020
    
c=car()
print(c.make)
print(c.model)
print(c.year)
              
print("----------------")



class bike:
    def __init__(self, make,model,year):
        self.make= make
        self.model=model
        self.year= year

b=bike("honda","civic",2022)
print(b.make)
print(b.model)
print(b.year)

        