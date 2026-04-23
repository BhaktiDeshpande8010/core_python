dict1={1:"abc",2:"pqr",3:"xyz",4:"mon"}
print(dict1)
print(type(dict1))

print(dict1.keys())
print(dict1.values())

print("first name is",dict1[1])
print("last name is",dict1[4])

# print("last name is",dict1["four"]) # (When key is also a string then this will work)


a=dict1.get(2)
print(a)

# copy
b=dict1.copy()
print(b)


# pop = delete the given index 
dict1.pop(2)
print(dict1)

print(sorted(dict1.items()))

c=dict1.items()
print(c)

dict1.update({5:"uvw",6:"efg"})
print(dict1)

d=dict1.setdefault(1,"nmm")
print(d)

dict1[1]="ijf"
print(dict1)

