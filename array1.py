# from array import *

# # in python we use array only for number
# a=array('i',[1,2,3,4,5])   #here i is the datatype 
# print(a)
# print(type(a))


# remaning array
import array as arr
b=arr.array('i',[4,5,6,7,8,9])
print(b)

b[2]=78
print(b)                              #Index b is change

b[3:6]=arr.array('i',[22,33,66])      #from index 3 to index 5 values are changed
print(b)


# deleting element 
num=arr.array('i',[1,2,3,4,5,6])
del num[2]
print(num)

# concate 2 array
c=arr.array('d',[2,3,4.5,6.7,8])
d=arr.array('d',[2.4,3.3,6,8,9])

f=c+d
print("F=",f)