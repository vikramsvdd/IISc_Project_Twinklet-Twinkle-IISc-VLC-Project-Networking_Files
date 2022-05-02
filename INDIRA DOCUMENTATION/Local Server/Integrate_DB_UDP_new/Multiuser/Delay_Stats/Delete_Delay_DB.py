import sqlite3

conn = sqlite3.connect('Twinkle_Delay_Stats_Database.db')

cursor = conn.cursor()
dropTableStatement = "DROP TABLE TWINKLE_DELAY_STATS_DATA"
cursor.execute(dropTableStatement)

print ("Deleted the desired table successfully")

conn.close()
