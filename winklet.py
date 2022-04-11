import sqlite3
conn=sqlite3.connect('winkle.db')  # also every time you run the program, information gets updated on the existing database
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS twinkle(sno REAL,twinkletid REAL)')  #Create Table
c.execute('INSERT INTO twinkle VALUES(1,1)')   #start inserting values
c.execute('INSERT INTO twinkle VALUES(2,2)')
c.execute('INSERT INTO twinkle VALUES(3,3)')
c.execute('INSERT INTO twinkle VALUES(4,4)')
c.execute('SELECT * FROM twinkle')   #reading from the table
fetchall=c.fetchall()
print(fetchall)              # you might know why the below lines don't work , you first need to select
twinklet_idarray=[]
for row in fetchall:
    twinklet_idarray.append(row[1])
print(twinklet_idarray)
#fetchall=c.fetchall()      # why this does not wrok and prints only []
#print(fetchall)
conn.commit()
c.close()
conn.close()

