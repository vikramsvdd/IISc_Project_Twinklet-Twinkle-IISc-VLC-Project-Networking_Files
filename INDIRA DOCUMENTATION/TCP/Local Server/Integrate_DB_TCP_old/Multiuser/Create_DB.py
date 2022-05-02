import sqlite3
import numpy as np

cnt = 0
np.save("checkpoint",cnt)
conn = sqlite3.connect('Twinkle_Database.db')
print ("Opened database successfully")


#cursor = conn.cursor()
#dropTableStatement = "DROP TABLE TWINKLE_DATA"
#cursor.execute(dropTableStatement)

conn.execute('''CREATE TABLE TWINKLE_DATA
         (SRNO INT PRIMARY KEY     NOT NULL,
          TWINKLERID       INT,
          FLASHPOINTID     INT,
          FLASHPOS         CHAR(25),
          DATETIME         CHAR(25),
          DATA_PACK       CHAR(50),
          REMARKS         CHAR(15));''')
print ("Table created successfully")

conn.close()