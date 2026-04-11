import os

f=open("demo.txt","r")

print(f.read())           #read entire data from the file
print(f.read(10))         #this will read the first 10 char from the file   gaps are also gonna be count

print(f.readline())
print(f.readline())
print(f.readline())

for i  in f:
    print(i)



# Write opertion
f1=open("demo1.txt","w")
f1.write("This is April")  # writes this conent in another file

f1=open("demo1.txt","a")
f1.write("march just ended")  # writes this conent after the "This is April"

f1=open("demo1.txt","w")
f1.write("April")          # if we do w afan its gonna delete the first content and add this "April"



#  to remove a file
f2=open("demo2.txt","x")
os.remove("demo3.txt")    # to remove a file

if os.path.exists("demo3.txt"):
    os.remove("demo.txt")
else:
    print("File Alredy Deleted")