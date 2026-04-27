# return statement
def  add(a,b):
    result=a+b
    return result

print(add(30,60))


# lambda function
mul1=lambda n:n%2==0           #syntax for lambda mul is the varibale 
total=mul1(4)
print("total")

# addition
addition = lambda n1,n2 : n1+n2
total1=addition(4,5)
print(total1)

# substrction
sub= lambda a,b :a-b
answer=sub(5,6)
print(answer)

# check even odd
check_even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
result = check_even_odd(4)
print(result)


# filter methods in list
list1=[2,3,4,5,6,7,8]
newlist1=list(filter(lambda n : n%2==0,list1))
print(newlist1)

# map method in list             it target every element in the list
newlist2=list(map(lambda n3:n3*2,list1))              #square of the number
print(newlist2)