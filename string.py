str="python"
print(str)
print(type(str))

# print(str[5])
# print(str[3:5])
# print(str[-4:-2])

# Reassigning string
str1="CorePython"
# str1[2]="R"             we are not able to change r to capital R. so we made a diffrent string.
# print(str1)

str1="corepython"       # this is how we reassign the sting
print(str1)


# # Deleting a string
# del str1
# print(str1)

# Escape character
nstr="\"Java\" is an programming language"
print(nstr)

s="Fortune Cloud"
print(s)

s1=s.capitalize
print(s1)

s2=s.isupper
print(s2)

s3=s.islower
print(s3)

print(len(s))

s4=s.replace('Cloud','Tech')
print(s4)

s5=""
l=['j','a','v','a']
print(s5.join(l))

s6=s.index("o")
print(s6)

s7=s.index('o',7,12)
print(s7)

tem="python is easy to learn"
tem1=tem.partition("easy")
print(tem1)

str8=tem.split()
print(str8)

# String Function
str9=tem.count('n')
print(str9)

str10=tem.count