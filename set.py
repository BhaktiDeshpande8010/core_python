set1={23,45,67, 89,"python"}
print(set1)
print(type(set1))


set2=set({6,6,3,5,8,9})

set1.add(40)
print(set1)

set2.remove(6)
print(set2)

a=set1.pop()      #gonna delete any number as it dont have any indexing
print(a)

b=set1.discard("python")
print(set1)

