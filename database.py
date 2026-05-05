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


#to insert many data 
list1=[(105,'Angular'),(106,'Testing'),(107,'AWS')]

cur.executemany("Insert into Student values(?,?)",list1)        #to insert many data 


# # retrive data from Database
# data=cur.execute("select * from student")
# print(data)

# for i in data:
#     print(i[0],i[1])



# # fetchall method
# cur.execute("select * from student")
# data=cur.fetchall()

# for i in data:
#     print(i)

# print("-------------")

# # fetchone
# cur.execute ("Select * from student where id=102")
# data=cur.fetchone()

# print(data)


# rename
cur.execute("update student set name='cloud' where id=104")
cur.execute("delete from student where name='AWS'")





con.commit()        #commit the changes
con.close()         # close the program