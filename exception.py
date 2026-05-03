try:
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))

    c=a/b

    print("C: ",c)                #if there is an error in this block the next block will print rather that termination the entire code

except:
    print("there was an error thus value of was not return")
    print("Code execuated successfully ")



# example- 2 Exception raise

try:
    num=int(input("Enter your age :"))
    if num<=18:
        raise ValueError("There is an value error")    #manually raises a ValueError.

    else:
        print("Yout are eligible for voting")

except ValueError as v:           #type of an error developer should know
    print(v)
