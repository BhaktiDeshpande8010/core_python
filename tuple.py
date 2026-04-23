tuple1=(11,22,33,"hello",True)
print(tuple1)
print(type(tuple1))

tuple2=tuple((1,2,3,4))
print(tuple2)
print(tuple2)

# count -gives the count of given number
number=(2,4,5,4,7,8,6)    
a=number.count(4)
print("count of 4 is",a)

# index
b=number.index(5)
print(b)

# max= Returns largest value
t=(2,15,3,4,7)
print("the original tuple",t)
print(max(t))

# min= Returns smallest value
print(min(t))

# sum = gives sum of all number
print(sum(t))   

# reversed = reverse the string
print(tuple(reversed(t)))


# slicing = the numbers from index 1 to index 3 will print 4 th will not print
print(t[1:4])   

print(t[1:])  # (from index 1 to last will print)

# len = number of elemnts
print(len(t))
