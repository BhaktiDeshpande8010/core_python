# recursion

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
num=int(input("Enter a number"))
print(fact(num))

def countdown(n):
    if n == 0:   # base case
        return
    print(n)
    countdown(n - 1)   # recursive call

countdown(5)