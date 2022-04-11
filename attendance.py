import sqlite3
dbc=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC","ref1","ref2","ref3"]  # month name bro
dbcd=[31,28,31,30,31,30,31,31,30,31,30,31,31,28,30] 
conn=sqlite3.connect('JAN.db')   #also, kindly ignore some comments if they are programs, they were just used for some testing purposes!!!
c=conn.cursor()
#c.execute('CREATE TABLE IF NOT EXISTS twinkle(Name TEXT,twinkletid REAL)')
#c.execute('CREATE TABLE IF NOT EXISTS twinkle(Name VARCHAR(255),twinkletid REAL,day1 TEXT,day2 TEXT,day3 TEXT,day4 TEXT,day5 TEXT,day6 TEXT,day7 TEXT,day8 TEXT,day9 TEXT,day10 TEXT,day11 TEXT,day12 TEXT,day13 TEXT,day14 TEXT,day15 TEXT,day16 TEXT,day17 TEXT,day18 TEXT,day19 TEXT,day20 TEXT,day21 TEXT,day22 TEXT,day23 TEXT,day24 TEXT,day25 TEXT,day26 TEXT,day27 TEXT,day28 TEXT)')
#c.execute('INSERT INTO twinkle VALUES(Devamma',1)')
#c.execute('''INSERT INTO twinkle VALUES("devamma",1,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
#c.execute('''INSERT INTO twinkle VALUES("lakshmamma",2,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
#c.execute('''INSERT INTO twinkle VALUES("manjula n",3,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
#c.execute('''INSERT INTO twinkle VALUES("venkat ramanamma",4,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
#c.execute('''INSERT INTO twinkle VALUES("lakshmamma",2,'a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a')''')
c.execute('SELECT * FROM twinkle')  
fetchall=c.fetchall()
#ctr=0
for row in fetchall:
     print(row)
#     ctr+=1
     #print(row[1])
#print("The no of rows is  " ,ctr)
#print("Length of fetchh  ",len(fetchall))
#conn.commit()
#c.close()
#conn.close()


def markabsentinitial(): #initially when the day starts, i mark absemt for everybody, if they are present, this 'a' will get replaced!!!!
    today = date.today()
    day=today.strftime("%d")
    #month = today.strftime("%m")
    #for i in range(len(dbc)):
      #  if(int(month)== i+1):
         #   month=dbc[i]
    month="FEB"     
    conn2= sqlite3.connect(month+'.db')
    d=conn2.cursor()
    d.execute('SELECT * FROM twinkle')
    day1="day"+day
    d.execute('UPDATE twinkle SET '+day1+'="a"')
    conn2.commit()
    d.close()
    conn2.close()



def createNewDatabase():   # actually create sample dbs for each month type and just copy them na ! 
     for i in range(len(dbc)):
         conn=sqlite3.connect(dbc[i]+'.db')
         c=conn.cursor()
         if(dbcd[i]==31):
             c.execute('CREATE TABLE IF NOT EXISTS twinkle(Name VARCHAR(255),twinkletid REAL,day1 TEXT,day2 TEXT,day3 TEXT,day4 TEXT,day5 TEXT,day6 TEXT,day7 TEXT,day8 TEXT,day9 TEXT,day10 TEXT,day11 TEXT,day12 TEXT,day13 TEXT,day14 TEXT,day15 TEXT,day16 TEXT,day17 TEXT,day18 TEXT,day19 TEXT,day20 TEXT,day21 TEXT,day22 TEXT,day23 TEXT,day24 TEXT,day25 TEXT,day26 TEXT,day27 TEXT,day28 TEXT,day29 TEXT,day30 TEXT,day31 TEXT)')
             c.execute('''INSERT INTO twinkle VALUES("devamma",1,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
             c.execute('''INSERT INTO twinkle VALUES("lakshmamma",2,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
             c.execute('''INSERT INTO twinkle VALUES("manjula n",3,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
             c.execute('''INSERT INTO twinkle VALUES("venkat ramanamma",4,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')

         if(dbcd[i]==30):
               c.execute('CREATE TABLE IF NOT EXISTS twinkle(Name VARCHAR(255),twinkletid REAL,day1 TEXT,day2 TEXT,day3 TEXT,day4 TEXT,day5 TEXT,day6 TEXT,day7 TEXT,day8 TEXT,day9 TEXT,day10 TEXT,day11 TEXT,day12 TEXT,day13 TEXT,day14 TEXT,day15 TEXT,day16 TEXT,day17 TEXT,day18 TEXT,day19 TEXT,day20 TEXT,day21 TEXT,day22 TEXT,day23 TEXT,day24 TEXT,day25 TEXT,day26 TEXT,day27 TEXT,day28 TEXT,day29 TEXT,day30 TEXT)')
               c.execute('''INSERT INTO twinkle VALUES("devamma",1,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
               c.execute('''INSERT INTO twinkle VALUES("lakshmamma",2,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
               c.execute('''INSERT INTO twinkle VALUES("manjula n",3,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
               c.execute('''INSERT INTO twinkle VALUES("venkat ramanamma",4,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')


         if(dbcd[i]==28):
               c.execute('CREATE TABLE IF NOT EXISTS twinkle(Name VARCHAR(255),twinkletid REAL,day1 TEXT,day2 TEXT,day3 TEXT,day4 TEXT,day5 TEXT,day6 TEXT,day7 TEXT,day8 TEXT,day9 TEXT,day10 TEXT,day11 TEXT,day12 TEXT,day13 TEXT,day14 TEXT,day15 TEXT,day16 TEXT,day17 TEXT,day18 TEXT,day19 TEXT,day20 TEXT,day21 TEXT,day22 TEXT,day23 TEXT,day24 TEXT,day25 TEXT,day26 TEXT,day27 TEXT,day28 TEXT)')
               c.execute('''INSERT INTO twinkle VALUES("devamma",1,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
               c.execute('''INSERT INTO twinkle VALUES("lakshmamma",2,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
               c.execute('''INSERT INTO twinkle VALUES("manjula n",3,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')
               c.execute('''INSERT INTO twinkle VALUES("venkat ramanamma",4,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')''')

         conn.commit()
         c.close()
         conn.close()

#createNewDatabase()

























    

