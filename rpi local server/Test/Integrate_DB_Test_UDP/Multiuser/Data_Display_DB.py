
from tkinter import *
import numpy as np
import socket
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
    count = np.load("checkpoint.npy")
    local_count = int(np.copy(count))
    iter_count = int(local_count)
    print(iter_count)
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
        #self.top2.iconbitmap('IISC_LOGO_ICOFOR.ico')
        self.top2.transient(self)
        self.button2.config(state='disabled')
        global Total_data_base 
        #print(gene_countr)
        #Total_data_base[gene_countr]=data_string_tf
        #print(Total_data_base)
        global t
        global count
        
        t = SimpleTable(self.top2, yc,xc)
        t.pack(side="top", fill="x")
        
        t.setfir(0,0,"S.No")
        t.setfir(0,1,"TwinkleT ID")
        t.setfir(0,2,"TwinkleR ID")
        t.setfir(0,3,"Location")
        t.setfir(0,4,"Date & Time")
        t.setfir(0,5,"Data")
        t.setfir(0,6,"Remarks")
        
        self.topButton2 = Button(self.top2, text="CLOSE", command = self.OnChildClose2)
        self.topButton2.pack(side="bottom")
        print("Check-1")
        t.after(0,Refreshingfun)

        

    def OnChildClose1(self):
        self.button1.config(state='normal')
        self.top1.destroy()
    def OnChildClose2(self):
        self.button2.config(state='normal')
        self.top2.destroy()

if __name__ == "__main__":
    conn = sqlite3.connect('Twinkle_Database.db')
    print ("Opened database successfully")
    window = Window(None)
    window.title("Twinkle VLC Access Control System")
    #window.iconbitmap('IISC_LOGO_ICOFOR.ico')
    window.mainloop()
