
from Tkinter import *
import numpy as np
import random
import time
import threading
import argparse
import sqlite3
from datetime import datetime

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_over" ,action = "store_true")
    return parser.parse_args()

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
		Total_data_base[x][y]=' '
        
sensor_data_base = ['Temperature: 23 Degrees Celsius', 'Temperature: 10 Degrees Celsius', 'Temperature: 37 Degrees Celsius', 'Temperature: 45 Degrees Celsius', 'Presuure: 760 mm', 'Presuure: 756 mm', 'Presuure: 736 mm', 'Presuure: 776 mm']

position_data_base = ['Room.no: 1.08 -ECE Department', 'Room.no: 1.09 -ECE Department', 'GSH-ECE Department', 'Wireless Research Lab-SP Building', 'Navacomm Lab-SP Building', 'Room.no: 309 -EE Department', 'Room.no: 315 -EE Department', 'Room.no: 204 -EE Department', 'Seminar Hall-CSA Department', 'Seminar Hall- Main Building',  'Seminar Hall- CeNSE']



data_base = []

element = ['','','','','','','']

for i in range(yc-1):
    data_base.append(element)

width_list=[10, 17, 17, 25, 25, 40, 15]

#bg_list=[ 'light sky blue', 'light gray', 'light sky blue', 'light gray', 'light sky blue']
bg_list=[ 'light sky blue', 'light gray', 'light sky blue', 'light gray', 'light sky blue', 'light gray', 'light sky blue' ]


#class ExampleApp(tk.Tk):
#	
#    def __init__(self):
#        tk.Tk.__init__(self)
#        
#        self.title('Twinkle Display System')
#        self.iconbitmap('IISC_LOGO_ICOFOR.ico')
#        
#        #global gene_countr
#        global Total_data_base 
#        #print(gene_countr)
#        #Total_data_base[gene_countr]=data_string_tf
#        print(Total_data_base)
#        global t
#        global count
#        count = 0
#        t = SimpleTable(self, yc,xc)
#        t.pack(side="top", fill="x")
#        
#        t.setfir(0,0,"S.No")
#        t.setfir(0,1,"Twinkler ID")
#        t.setfir(0,2,"Flash Point ID")
#        t.setfir(0,3,"Flash Point Position")
#        t.setfir(0,4,"Date & Time")
#        t.setfir(0,5,"Data")
#        t.setfir(0,6,"Remarks")
#        t.after(0,Refreshingfun)
     
    
        
def Refreshingfun():
    global count
    global data_base
    global local_count
    local_count+=1
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
    
    
    print(count)
    print(local_count)
    data_element = "%s*%s*%s*%s*%s*%s*%s"%(local_count, twinkler_id,flashpoint_id,pos_vale,now_time,data_vale, data_remarks)
    
    

    data_split = data_element.split('*')
    split_count = data_split[0]
    split_twinkler_id = data_split[1]
    split_flashpoint_id = data_split[2]
    split_pos_vale = data_split[3]
    split_now_time = data_split[4]
    split_data_vale = data_split[5]
    split_data_remarks = data_split[6]

    conn.execute('''INSERT INTO TWINKLE_DATA (SRNO,TWINKLERID,FLASHPOINTID,FLASHPOS,DATETIME,DATA_PACK,REMARKS)
                  VALUES(?,?,?,?,?,?,?)''', (split_count, split_twinkler_id, split_flashpoint_id, split_pos_vale, split_now_time, split_data_vale, split_data_remarks))
    conn.commit()
    print("inserted data ")
    #print(count)
    print(split_count)
    print("\n")
    iter_count=int (local_count)
    
    #if count > yc:
        #data_base.pop(0)
        #data_base.append(data_element)
    #else :
        #data_base.append(data_element)
    #data_base.pop(yc-2)
    #data_base.insert(0,data_element)
    if iter_count<yc:
        cursor = conn.execute("SELECT SRNO, TWINKLERID, FLASHPOINTID, FLASHPOS, DATETIME, DATA_PACK, REMARKS from TWINKLE_DATA WHERE SRNO<:SRNO", {"SRNO": (iter_count+1)})
    else:
        cursor = conn.execute("SELECT SRNO, TWINKLERID, FLASHPOINTID, FLASHPOS, DATETIME, DATA_PACK, REMARKS from TWINKLE_DATA WHERE SRNO BETWEEN ? AND ?", ((iter_count-(yc-2)), iter_count))
    rowx = 0
    for row in cursor:
        for colx in range(xc):
              t.set(rowx+1,colx,row[colx])
        rowx = rowx+1
    count= local_count
    t.after(2000,Refreshingfun)


class SimpleTable(Frame):
    def __init__(self, parent, rows=yc, columns=xc):
        # use black background so it "peeks through" to 
        # form grid lines
        Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Label(self, text=Total_data_base[row][column], bg=bg_list[column], 
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
        
#    def update_table(self,columns,rows):
#        widgets = self._widgets.pop(1)
#        for column in range(columns):
#            widget = widgets[column]
#            widget.destroy()
#            current_row = []
#        for column in range(columns):
#            label = tk.Label(self, text='', bg=bg_list[column], 
#                                 borderwidth=0, width=width_list[column])
#            label.grid(row=rows-1, column=column, sticky="nsew", padx=1, pady=1)
#            current_row.append(label)
#        self._widgets.append(current_row)


class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
    def initialize(self):
        self.geometry("1800x1000+0+0")
        self.title("Twinkle Log and Display System")
        self.configure(background='light sky blue')
        self.txtDisplaya1= Label(self, font=('times new roman',45,'bold'), text="Twinkle VLC Access Control System", fg='linen', bg='dark slate blue')
        self.txtDisplaya1.place(x=290, y=10, width=1000)
        
#        self.txtDisplayb1= Label(self, font=('times new roman',30,'bold'), text="A Project work on VLC", bd=05,  bg='light gray',fg='dark slate blue')
#        self.txtDisplayb1.place(x=1050, y=570, width=500)
#        self.txtDisplayb2= Label(self, font=('times new roman',30,'bold'), text="by", bd=05, bg='light gray',fg='dark slate blue')
#        self.txtDisplayb2.place(x=1050, y=620, width=500)
#        self.txtDisplayb3= Label(self, font=('times new roman',30,'bold'), text="Wireless Research Lab", bd=10, bg='light gray',fg='dark slate blue')
#        self.txtDisplayb3.place(x=1050, y=670, width=500)
#        self.txtDisplayb4= Label(self, font=('times new roman',30,'bold'), text="Department of ECE", bd=10, bg='light gray',fg='dark slate blue')
#        self.txtDisplayb4.place(x=1050, y=720, width=500)
        
        #self.f2= Frame(self, width=500, height=100, bg="light gray", relief='flat')
        #self.f2.pack(side='bottom', anchor="w")
        
        self.canvas = Canvas(self, width = 265, height = 225, bg='dark slate blue')      
        self.canvas.pack(side='top', anchor="w", pady=10, padx=10)      
        
        self.img = PhotoImage(file="IISC_LOGO.ppm")      
        self.canvas.create_image(60,60, image=self.img)
        
        self.img1 = PhotoImage(file="Star_Logo_2.gif")      
        self.canvas.create_image(30,140, anchor='nw', image=self.img1)
        
        self.img2 = PhotoImage(file="Star_Logo_2.gif")      
        self.canvas.create_image(210,180, image=self.img2)
        
        self.img3 = PhotoImage(file="Star_Logo_2.gif")      
        self.canvas.create_image(210,60, image=self.img3)
        
#        self.canvas2 = Canvas(self, width = 170, height = 130)      
#        self.canvas2.pack(side='right', anchor="s", pady=1000 )
#        
#        self.img4 = PhotoImage(file="IISC_LOGO.ppm")      
#        self.canvas2.create_image(560,60, image=self.img4)
        
        
        #self.canvas = Canvas(self.f2, width = 275, height = 260)      
        #self.canvas.pack(side='bottom', anchor="w")      
        
        self.button1 = Button(self,font=('times new roman',30,'bold'), text="Query Database", bg="dark slate blue", fg="cornsilk", command = self.OnButtonClick1)
        self.button1.place(x=620, y=250)
        self.button2 = Button(self, font=('times new roman',30,'bold'),text="View Real Time Display", bg="dark slate blue", fg="cornsilk", command = self.OnButtonClick2)
        self.button2.place(x=550, y=125)
      
        
#        self.wButton = Button(self, text='text', command = self.OnButtonClick)
#        self.wButton.pack()

    def OnButtonClick1(self):
        self.top1 = Toplevel()
        self.top1.title("Query Database ")
        self.top1.geometry("300x150+30+30")
        self.top1.transient(self)
        self.button1.config(state='disabled')

        self.topButton1 = Button(self.top1, text="CLOSE", command = self.OnChildClose1)
        self.topButton1.pack()
        
    def OnButtonClick2(self):
        global local_count
        self.top2 = Toplevel()
        self.top2.title("Real Time Display")
        #self.top2.geometry("300x150+30+30")
        self.top2.iconbitmap('IISC_LOGO_ICOFOR.ico')
        self.top2.transient(self)
        self.button2.config(state='disabled')
        global Total_data_base 
        #print(gene_countr)
        #Total_data_base[gene_countr]=data_string_tf
        print(Total_data_base)
        global t
        global count
        local_count = int (np.copy(count))
        t = SimpleTable(self.top2, yc,xc)
        t.pack(side="top", fill="x")
        
        t.setfir(0,0,"S.No")
        t.setfir(0,1,"Twinkler ID")
        t.setfir(0,2,"Flash Point ID")
        t.setfir(0,3,"Flash Point Position")
        t.setfir(0,4,"Date & Time")
        t.setfir(0,5,"Data")
        t.setfir(0,6,"Remarks")
        #print("Reyyyy Nee Abbba")
        self.topButton2 = Button(self.top2, text="CLOSE", command = self.OnChildClose2)
        self.topButton2.pack(side="bottom")
        t.after(0,Refreshingfun)

        

    def OnChildClose1(self):
        self.button1.config(state='normal')
        self.top1.destroy()
    def OnChildClose2(self):
        self.button2.config(state='normal')
        self.top2.destroy()

if __name__ == "__main__":
    conn = sqlite3.connect('Twinkle_Database.db')
    print "Opened database successfully";
    global count
    count = 0
    args = get_arguments()
    if args.start_over == True:
        count = 0
    else :
        try :
            count = np.load("checkpoint.npy")
        except :
            count = 0
    window = Window(None)

    window.title("Twinkle VLC Access Control System")
    window.iconbitmap('IISC_LOGO_ICOFOR.ico')
    window.mainloop()
    np.save("checkpoint",count)