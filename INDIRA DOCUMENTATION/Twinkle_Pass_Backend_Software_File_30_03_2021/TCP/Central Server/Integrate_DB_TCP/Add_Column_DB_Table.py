import sqlite3
import numpy as np

conn = sqlite3.connect('Twinkle_Database.db')
print ("Opened database successfully")

#cursor = conn.cursor()
#dropTableStatement = "DROP TABLE TWINKLE_DATA"
#cursor.execute(dropTableStatement)

#ALTER TABLE TWINKLE_DATA
#ADD COLUMN DAILY STATISTICS

#conn.execute("ALTER TABLE TWINKLE_DATA ADD COLUMN CUMULATIVE STATISTICS")

conn.execute("ALTER TABLE TWINKLE_DATA RENAME COLUMN DAILY to DAILY_DELAY_STATISTICS")
conn.execute("ALTER TABLE TWINKLE_DATA RENAME COLUMN CUMULATIVE to CUMULATIVE_DELAY_STATISTICS")
print ("Attributes added successfully")

conn.close()

