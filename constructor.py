class histrory:
    def show(self):                  #methos
        print("I'm show method")
    
    def __init__(self):
        print("I'm Constructor")

h=histrory()                #constructor called
h.show() 


# parameterized constructor 
class marathi:
    id=0
    name=""

    def __init__(self,id,name):
        self.id
        self.name


m=marathi(101,"subject")
print(m.id)
print(m.name)