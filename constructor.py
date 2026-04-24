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
    id=0
    name=""

    def show(self):
        print("I am a show method")

a=A()
A.show()

a.id=102
a.name="Java"
