# class parent:
#     def add(self,a,b,c):
#         print(a+b+c)

#     def add (self,a,b,c=0):
#         print(a+b+c)

# p=parent()
# p.add()


# method overriding
class logic:
    def swap1(self,m,n):
        temp=m
        m=n
        n=temp
        print(m,n)

class swap(logic):
    def swap(self,m,n):
        super().swap1(m,n)

s=swap()
s.swap1(5,6)


class python:
    def method(self):
        print("First method")

class java:
    def methos(self):
        print("Second Method")