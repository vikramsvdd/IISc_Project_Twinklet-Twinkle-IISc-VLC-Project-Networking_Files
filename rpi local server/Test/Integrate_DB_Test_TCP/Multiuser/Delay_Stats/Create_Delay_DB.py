import sqlite3
import numpy as np

cnt = 0
np.save("checkpoint_delay",cnt)
conn = sqlite3.connect('Twinkle_Delay_Stats_Database.db')
print ("Opened database successfully")


#cursor = conn.cursor()
#dropTableStatement = "DROP TABLE TWINKLE_DATA"
#cursor.execute(dropTableStatement)

conn.execute('''CREATE TABLE TWINKLE_DELAY_STATS_DATA
         (SRNO INT PRIMARY KEY      NOT NULL,
          TWINKLETID        INT,
          TWINKLERID        INT,
          DATETIME      CHAR(25),
          DATA_PACK     CHAR(50),
          DELAY         REAL,
          STATISTICS        TEXT);''')
print ("Table created successfully")

conn.close()
