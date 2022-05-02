import sqlite3

conn = sqlite3.connect('Twinkle_Database.db')



cursor = conn.cursor()
dropTableStatement = "DROP TABLE TWINKLE_DATA"
cursor.execute(dropTableStatement)

#conn.execute('''CREATE TABLE TWINKLE_DATA
#         (SRNO INT PRIMARY KEY     NOT NULL,
#          TWINKLERID       INT,
#          FLASHPOINTID     INT,
#          FLASHPOS         CHAR(25),
#          DATETIME         CHAR(25),
#          DATA_PACK       CHAR(50),
#          REMARKS         CHAR(15));''')
#print "Table created successfully";

print ("Deleted the desired table successfully")

conn.close()