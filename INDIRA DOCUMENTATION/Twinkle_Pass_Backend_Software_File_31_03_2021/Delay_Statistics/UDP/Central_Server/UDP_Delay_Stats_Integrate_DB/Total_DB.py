import Tkinter as tk
import numpy as np
import random
import time
import threading
from datetime import datetime
import sqlite3

def binary_to_decimal(arr):
	num = 0
	for i in range(len(arr)):
		num += arr[i]*np.power(2,i)
	return num

def binary_to_char(arr):
	num = 0
	for i in range(len(arr)):
		num += int(arr[i])*np.power(2,len(arr)-1-i)
		#print(num)
	return str(chr(num))

gene_countr=1
	
def binary_to_char_dec(arr):
	num = 0
	for i in range(len(arr)):
		num += int(arr[i])*np.power(2,len(arr)-1-i)
		#print(num)
	return num	
	
global xc
global yc

xc, yc = 7, 25;
Total_data_base = [[0 for x in range(xc)] for y in range(yc)] 
#print(np.shape(Total_data_base))
#print(xc)
#print(yc)
for x in range(yc):
	for y in range(xc):
		Total_data_base[x][y]='- '
	
sensor_data_base = ['Temperature: 23 Degrees Celsius', 'Temperature: 10 Degrees Celsius', 'Temperature: 37 Degrees Celsius', 'Temperature: 45 Degrees Celsius', 'Presuure: 760 mm', 'Presuure: 756 mm', 'Presuure: 736 mm', 'Presuure: 776 mm']

position_data_base = ['Room.no: 1.08 -ECE Department', 'Room.no: 1.09 -ECE Department', 'GSH-ECE Department', 'Wireless Research Lab-SP Building', 'Navacomm Lab-SP Building', 'Room.no: 309 -EE Department', 'Room.no: 315 -EE Department', 'Room.no: 204 -EE Department', 'Seminar Hall-CSA Department', 'Seminar Hall- Main Building',  'Seminar Hall- CeNSE']
#print(len(position_data_base))
#for x in range(10):
  #print random.randint(0,7)


data_base = []

element = ['','','','','','','']

for i in range(yc-1):
    data_base.append(element)

	
#char_bits_dec = [ord(x) for x in name_rand]
#print(char_bits_)
#print(char_bits_dec)




#char_bits = np.split(splits[-1],list(range(8,len(splits[-1]),7)))



#gps_coord = binary_to_decimal(splits[2])
#date_time = binary_to_decimal(splits[3])
#root = tk.Tk()
#count = 0
    
    
#width_list=[15,15, 40, 25, 60]
width_list=[10, 17, 17, 25, 25, 40, 15]

#bg_list=[ 'light sky blue', 'light gray', 'light sky blue', 'light gray', 'light sky blue']
bg_list=[ 'light sky blue', 'light gray', 'light sky blue', 'light gray', 'light sky blue', 'light gray', 'light sky blue' ]


class ExampleApp(tk.Tk):
	
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title('Twinkle Display System')
        self.iconbitmap('IISC_LOGO_ICOFOR.ico')
        
        #global gene_countr
        global Total_data_base 
        #print(gene_countr)
        #Total_data_base[gene_countr]=data_string_tf
        print(Total_data_base)
        global t
        global count
        count = 0
        t = SimpleTable(self, yc,xc)
        t.pack(side="top", fill="x")
        
        t.setfir(0,0,"S.No")
        t.setfir(0,1,"Twinkler ID")
        t.setfir(0,2,"Flash Point ID")
        t.setfir(0,3,"Flash Point Position")
        t.setfir(0,4,"Date & Time")
        t.setfir(0,5,"Data")
        t.setfir(0,6,"Remarks")
        #print("Reyyyy Nee Abbba")
        t.after(0,Refreshingfun)
        #self.Refreshingfun()
        #checkerfun()
        #print("Reyyyy Jeffa Na Jeffada")
        #gene_countr=gene_countr+1
    
        
def Refreshingfun():
    global count
    global data_base
    count+=1
    #print(count)
    random_array = (np.random.uniform(0,1,32) > 0.5 ).astype(np.int32)
    splits = np.split(random_array,[16])
    name_rand = sensor_data_base[random.randint(0,7)]
    #print(name_rand)
    char_bits_ = [format(ord(x),'b') for x in name_rand]
    position_rand = position_data_base[random.randint(0,7)]
    #print(position_rand)
    #print(count)
    position_bits_ = [format(ord(x),'b') for x in position_rand]
    twinkler_id = binary_to_decimal(splits[0])
    #print(twinkler_id)
    flashpoint_id = binary_to_decimal(splits[1])
    #print(flashpoint_id)
    char = []
    for i in range(len(char_bits_)):
	     char.append(binary_to_char(char_bits_[i]))
	
    data_vale=''.join(char)
    #print(data_vale)

    pos_char= []
    for i in range(len(position_bits_)):
	     pos_char.append(binary_to_char(position_bits_[i]))
	
    pos_vale=''.join(pos_char)
    #print(pos_vale)
    #print("\n")
    now_time= datetime.now()
    data_remarks= "-No- "
    data_element = "%s*%s*%s*%s*%s*%s*%s"%(count, twinkler_id,flashpoint_id,pos_vale,now_time,data_vale, data_remarks)
    #print(data_element)
    #data_element = [count, twinkler_id,flashpoint_id,pos_vale,now_time,data_vale, data_remarks]
    data_split = data_element.split('*')
    split_count = data_split[0]
    split_twinkler_id = data_split[1]
    split_flashpoint_id = data_split[2]
    split_pos_vale = data_split[3]
    split_now_time = data_split[4]
    split_data_vale = data_split[5]
    split_data_remarks = data_split[6]
#    print(split_count)
#    print(split_twinkler_id)
#    print(split_flashpoint_id)
#    print(split_pos_vale)
#    print(split_now_time)
#    print(split_data_vale)
#    print(split_data_remarks)
#    print('\n')
#    conn.execute('''INSERT INTO TWINKLE_DATA (SRNO,TWINKLERID,FLASHPOINTID,FLASHPOS,DATETIME,DATA_PACK,REMARKS)
#                  VALUES(?,?,?,?,?,?,?)''', (count, twinkler_id , flashpoint_id, pos_vale, now_time,  data_vale, data_remarks))
#    conn.commit()
    conn.execute('''INSERT INTO TWINKLE_DATA (SRNO,TWINKLERID,FLASHPOINTID,FLASHPOS,DATETIME,DATA_PACK,REMARKS)
                  VALUES(?,?,?,?,?,?,?)''', (split_count, split_twinkler_id, split_flashpoint_id, split_pos_vale, split_now_time, split_data_vale, split_data_remarks))
    conn.commit()
    print("inserted data ")
    print(count)
    print(split_count)
    
    #if count > yc:
        #data_base.pop(0)
        #data_base.append(data_element)
    #else :
        #data_base.append(data_element)
    #data_base.pop(yc-2)
    #data_base.insert(0,data_element)
    if count<yc:
        cursor = conn.execute("SELECT SRNO, TWINKLERID, FLASHPOINTID, FLASHPOS, DATETIME, DATA_PACK, REMARKS from TWINKLE_DATA WHERE SRNO<:SRNO", {"SRNO": (count+1)})
    else:
        cursor = conn.execute("SELECT SRNO, TWINKLERID, FLASHPOINTID, FLASHPOS, DATETIME, DATA_PACK, REMARKS from TWINKLE_DATA WHERE SRNO BETWEEN ? AND ?", ((count-(yc-2)), count))
    rowx = 0
    for row in cursor:
#        if (row[0]==count):
#              print "SRNO= ", row[0]
#              print "TWINKLERID = ", row[1]
#              print "FLASHPOINTID = ", row[2]
#              print "FLASHPOS = ", row[3]
#              print "DATETIME = ", row[4]
#              print "DATA_PACK = ", row[5]
#              print "REMARKS = ", row[6], "\n"
        for colx in range(xc):
              t.set(rowx+1,colx,row[colx])
        rowx = rowx+1
        
    t.after(2000,Refreshingfun)

    
    
           
#class checkerfun():
#      def __init__(self):
#        print("Hello")
#        after(2000, checkerfun)     



class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=yc, columns=xc):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text=Total_data_base[row][column], bg=bg_list[column], 
                                 borderwidth=0, width=width_list[column])
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def setfir(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value, font='Helvetica 12 bold')
        
    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value, )    
        
    def update_table(self,columns,rows):
        widgets = self._widgets.pop(1)
        for column in range(columns):
            widget = widgets[column]
            widget.destroy()
            current_row = []
        for column in range(columns):
            label = tk.Label(self, text='', bg=bg_list[column], 
                                 borderwidth=0, width=width_list[column])
            label.grid(row=rows-1, column=column, sticky="nsew", padx=1, pady=1)
            current_row.append(label)
        self._widgets.append(current_row)
        
   
    #ExampleApp()
    


if __name__ == "__main__":
       
          conn = sqlite3.connect('Twinkle_Database.db')
          print "Opened database successfully";
          #app = ExampleApp()
          root = ExampleApp()
          #Refresher()
          root.mainloop()
          #time.sleep(20)


