import sqlite3 as sq 
con=sq.connect("reg.db")
cur=con.cursor()

# cur.execute("create table student(id int (10), name varchar(10))")         #creating a table
# cur.execute("insert into student values(101,'python')")        

# cur.execute("insert into student values(?,?)",(102,'Java'))                #flask syntax

# user input
# a=int(input("Enter you ID :"))
# b=input("Enter Your Name :")
# cur.execute("insert into student values(?,?)",(a,b))

list1=[(105,'Angular'),(106,'Testing'),(107,'AWS')]

cur.executemany("Insert into Student values(?,?)",list1)

con.commit()        #commit the changes
con.close()         # close the program