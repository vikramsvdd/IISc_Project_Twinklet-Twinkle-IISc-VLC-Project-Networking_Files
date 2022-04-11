import sqlite3
global month
from datetime import date
dbc=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]  # month name bro
dbcd=[31,28,31,30,31,30,31,31,30,31,30,31]                        # no of days bro

def RealTimeDisplay(conn):
    #today = date.today()
    #print("Today date is: ", today)
    #today = today.strftime("%m")
    #for i in range(len(dbc)):
        #if(int(today)== i+1):
          #  month=dbc[i]
   # conn= sqlite3.connect('winkle.db')
    print("Opened database successfully")             #just displays the current  months database ????/ it is a real time display , it should operate in winkle db and should have some component dependent with time i.e constantly upgrading in nature
    c=conn.cursor()
    c.execute('SELECT * FROM twinkle')
    fetchall=c.fetchall()
    for row in fetchall:
        print(row)

def GenerateAttendanceSheet(month):
    conn= sqlite3.connect(month+'.db')
    print("Opened database successfully")
    c=conn.cursor()
    c.execute('SELECT * FROM twinkle')                              #same as prev except instead of current, any month (some loose definitions, kindly ignore if not clear)
    fetchall=c.fetchall()
    for row in fetchall:
        print(row)
    
    
def QueryDatabase(employee_name,start_month,start_date,end_month,end_date):       
    emp=employee_name
    startm=start_month
    endm=end_month
    startd=start_date                                                 #obtaining the neccessary info from user
    endd=end_date
    emp="devamma"
   # startm="JAN"
    #endm="FEB"
    #startd="12/01/2021"                        #these comments are just for testing purpose, kindly avoid confusing yourself by seeing these!
    #endd="22/02/2021"
    startd=int(str(startd[0:2]))
    endd=int(str(endd[0:2]))
    if(startm==endm):
        conn= sqlite3.connect(startm+'.db')
        print("Opened database successfully")
        c=conn.cursor()
        c.execute('SELECT * FROM twinkle WHERE Name=?',(emp,))
        fetchall=c.fetchall()
        for row in fetchall:
            row=row[startd+2:endd+2+1]           # due to first 2 rows being name and twinklet id which we dont want , iam adding 2
            print(row)



    else:
        ctr=0
        fetchalll=[]        #array for accumulationg all month db for a person
        s,e=0,0
        
        for i in range(len(dbc)):
            if(startm==dbc[i]):
                s=i
            if(endm==dbc[i]):         #To obtain indexes of the months in dbc array to iterate through a loop
                e=i
        for i in range(s,e+1):
            conn= sqlite3.connect(dbc[i]+'.db')
            ctr+=1                                          #counter variable ctr  to help , to assign particular stardate and end date for each month
            print("Opened database "+dbc[i]+" successfully")
            c=conn.cursor()
            c.execute('SELECT * FROM twinkle WHERE Name=?',(emp,))
            fetchall=c.fetchall()
            global enddt
            enddt=dbcd[i]
            if(ctr!=1):
                startd=1
                
            if(ctr==(e-s)+1):
                enddt=endd
                
            for row in fetchall:
                row=row[startd+2:enddt+2+1]          
                print(row)
                fetchalll.append(row)

        print(fetchalll)


def addnewuser(Name):
    twinklet_id,sno=0,0
    today = date.today()
    month = today.strftime("%m")
    conn= sqlite3.connect('winklet.db')
    c=conn.cursor()
    c.execute('SELECT * FROM twinkle')
    fetchall=c.fetchall()
    sno,twinklet_id=len(fetchall)+1,len(fetchall)+1
    c.execute('INSERT INTO twinkle VALUES(?,?)',(sno,twinklet_id,))
    for i in range(len(dbc)):
        conn1=sqlite3.connect(dbc[i]+'.db')
        d=conn1.cursor()
        if(dbcd[i]==30):
            d.execute('INSERT INTO twinkle VALUES(?,?,' ',' ',' ',' ',' ',' ',' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')',(Name,twinklet_id,))
        if(dbcd[i]==28):
            d.execute('INSERT INTO twinkle VALUES(?,?,' ',' ',' ',' ',' ',' ',' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')',(Name,twinklet_id,))
        if(dbcd[i]==31):
            d.execute('INSERT INTO twinkle VALUES(?,?,' ',' ',' ',' ',' ',' ',' ', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')',(Name,twinklet_id,))
    


#QueryDatabase()            
            
        
    
































    
    
    
    
