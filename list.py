list11=[56,76.65,"Hello",True,"a"]

print(list11)
print(type(list11))


# using list function
list2=list([65,89,78,56,89])
print(list2)
print(type(list2))

# addition/contcatination
list3=list11+list2
print(list3)

# multiplication
list4=list2*3
print(list4)

# indexing
# positive indexing
list5=list2[3]
print(list5)

# negative indexing
list6=list11[2]
print(list6)


# slicing






# list method
# append
sub=["sql","web","c","testing"]
score=[98,78,54,67]
sub.append("Python")
print(sub)

sub.append(score)
print(score)


# list
fruit=["banana","orange","pineapple"]
fruit.clear()
print(fruit)

#copy
fruit=["banana","orange","pineapple"]
x=fruit.copy()
print(x)

# count
fruit=["banana","orange","pineapple"]
y=fruit.count("banana")
print(y)

# count
number=[2,3,4,5,6,6,7,8,8,8]
z=number.count(8)
print(z)

i=score.index(78)
print(i)

# to insert the value
score.insert(3,100)
print(score)

score.pop(2)
print(score)

newscore=score.pop()
print(newscore)

score.pop()
print(score)

# reverse
fruit.reverse()
print(fruit)

cars=["Fort","BMW","Volvo"]
cars.sort()
print(cars)

cars=["Fort","BMW","Volvo"]
cars.sort(reverse=True)
print(cars)