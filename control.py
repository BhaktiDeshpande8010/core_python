num=45
if num%2==0:
    print("This is even number")
else:
    print("This is an Odd Number")


# take number from user
a = int(input("Enter a number"))
if a%2== 0:
    print("This is even number")
else:
    print("This is an Odd Number")


# elif program
marks=int(input("Enter your marks"))
if marks==60:
    print("Average marks")

elif marks==70:
    print("Good marks")

elif marks==80:
    print("best marks")

elif marks==90:
    print("Ecllent Marks")

else:
    print("invalid marks")



# nested if
num =56
if num>0:
    print("Its an positive number")

    if num%2==0:
        print("Its also an even number")
    
    else:
        print("Its an odd number")

else:
    print("its n negative number")


# nested if -- if i want to take number from user
num =int(input("Enter a number"))
if num>0:
    print("Its an positive number")

    if num%2==0:
        print("Its also an even number")
    
    else:
        print("Its an odd number")

else:
    print("its n negative number")



marks=80

# if marks >= 80:
#     print("Distinction")
#     if marks >=60:
#         print("good")
#     else:
#         print("better")
# else:
#     print("better luck next")