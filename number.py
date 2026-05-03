import numpy

arr=numpy.array([1,2,3,4,5,6])
print(arr)

print(type(arr))

# array types
a1=numpy.array(56)
print(a1)

a2=numpy.array([11,12,13,14])
print(a2)

a3 = numpy.array([[1,1,2], [3,3,4]])
print(a3)

a4=numpy.array([ [ [6,7,8], [9,0,1] ,[2,3,4],[5,6,7] ] ] )
print(a4)

a5=numpy.arange(1,11)
print(a5)

a6=numpy.array([11,22,33,44,55,66,77,88,99,00,21,45])
# a7=a6.reshape(2,5)
# print(a7)

a8=a6.reshape(2,2,3)
print(a8)


a11=numpy.array([ [ [6,7,8], [9,0,1] ,[2,3,4],[5,6,7] ] ] )

for i in a11:
    for j in i:
        for k in j:
            print(k)


print("-----")

arr12=numpy.array([2,3,4,5,6,7,8,9,0])
a=numpy.where(arr12%2==0)
print(a)

# print(numpy.sort(arr12))


a11=numpy.array([ [ [6,7,8], [9,0,1] ,[2,3,4],[5,6,7] ] ] )

for i in numpy.nditer(a12):
    print(i)


print("-----")


arr12=numpy.array([2,3,4,5,6,7,8,9,0])
a=numpy.where(arr12%2==0)
print(a)

