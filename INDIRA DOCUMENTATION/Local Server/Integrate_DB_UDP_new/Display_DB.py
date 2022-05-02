import sqlite3
import numpy as np
global count
conn = sqlite3.connect('Twinkle_Database.db')
dis_count = np.load("checkpoint.npy")
print "Opened database successfully";
#dis_count = int (np.copy(count))
cursor = conn.execute("SELECT SRNO, TWINKLERID, FLASHPOINTID, FLASHPOS, DATETIME, DATA_PACK, REMARKS from TWINKLE_DATA WHERE SRNO<:SRNO", {"SRNO": (dis_count+1)})
for row in cursor:
   print "SRNO= ", row[0]
   print "TWINKLERID = ", row[1]
   print "FLASHPOINTID = ", row[2]
   print "FLASHPOS = ", row[3]
   print "DATETIME = ", row[4]
   print "DATA_PACK = ", row[5]
   print "REMARKS = ", row[6], "\n"

print "Operation done successfully";
np.save("checkpoint",dis_count)
conn.close()