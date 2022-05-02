
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
        
width_list=[10, 15, 15, 25, 20, 17, 25]

#bg_list=[ 'light sky blue', 'light gray', 'light sky blue', 'light gray', 'light sky blue']
bg_list=[ 'light sky blue', 'light gray', 'light sky blue', 'light gray', 'light sky blue', 'light gray', 'light sky blue' ]

        
def Refreshingfun():
    global count
    global data_base
    global local_count
    count = np.load("checkpoint_delay.npy")
    local_count = int(np.copy(count))
    iter_count = int(local_count)
    print(iter_count)
    if iter_count<yc:
            cursor = conn.execute("SELECT SRNO, TWINKLETID, TWINKLERID, DATETIME, DATA_PACK, DELAY, STATISTICS from TWINKLE_DELAY_STATS_DATA WHERE SRNO<:SRNO", {"SRNO": (iter_count+1)})
    else:
            cursor = conn.execute("SELECT SRNO, TWINKLETID, TWINKLERID, DATETIME, DATA_PACK, DELAY, STATISTICS from TWINKLE_DELAY_STATS_DATA WHERE SRNO BETWEEN ? AND ?", ((iter_count-(yc-2)), iter_count))
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
        
        self.button1 = Button(self,font=('times new roman',30,'bold'), text="Query Database", bg="dark slate blue", fg="cornsilk", command = self.OnButtonClick1)
        self.button1.place(x=620, y=250)
#        self.button2 = Button(self, font=('times new roman',30,'bold'),text="View Real Time Display", bg="dark slate blue", fg="cornsilk", command = self.OnButtonClick2)
#        self.button2.place(x=550, y=125)
      
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
        t.setfir(0,3,"Date & Time")
        t.setfir(0,4,"Data")
        t.setfir(0,5,"Delay")
        t.setfir(0,6,"Statistics")
        
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
    conn = sqlite3.connect('Twinkle_Delay_Stats_Database.db')
    print ("Opened database successfully")
    window = Window(None)
    window.title("Twinkle VLC Access Control System")
    #window.iconbitmap('IISC_LOGO_ICOFOR.ico')
    window.mainloop()
