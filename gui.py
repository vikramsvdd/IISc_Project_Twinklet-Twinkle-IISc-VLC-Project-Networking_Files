
from tkinter import *
import numpy as np
import socket
import random
import time
import threading
import argparse
import sqlite3
from datetime import datetime
#import array as arr
#from tkcalendar import Calendar, DateEntry
#from tkcalendar import calendar, dateEntry

from attendancefunctions import *

xs, ys = 7,1000;  


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_over" ,action = "store_true")
    return parser.parse_args()

global xc
global yc
xc, yc = 2,5;                                                # no of rows and cloumns in winhkle.db, same will be in the "real time display" in GUI.
Total_data_base = [[0 for x in range(xc)] for y in range(yc)] 
for x in range(yc):
    for y in range(xc):
        Total_data_base[x][y] = ' '


width_list=[10, 17]

bg_list = ['light sky blue', 'light gray' ]

def Refreshingfun():
    global count
    global data_base
    cursor = conn.execute("SELECT* FROM twinkle")
    rowx = 0
    for row in cursor:
         for colx in range(xc):                            #function for creating the real time display table and stuff
             t.set(rowx+1, colx, row[colx])
         rowx = rowx+1
    t.after(2000, Refreshingfun)



class SimpleTable(Frame):
    def __init__(self, parent, rows=xc, columns=yc):
        Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Label(self, text=Total_data_base[row][column], bg=bg_list[column], 

                                 borderwidth=0, width=width_list[column])
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)              #basic tkinter bible procedure here like creation etc
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
        self.geometry("1000x650+0+0")
        self.title("Twinkle Log and Display System")
        self.configure(background='light sky blue')
        self.txtDisplaya1 = Label(self, font=('times new roman', 35, 'bold'), text="Twinkle VLC Access Control System", fg ='linen', bg='dark slate blue')
        self.txtDisplaya1.place(x=240, y=10, width=770)
        
        self.canvas = Canvas(self, width=215, height=225, bg='dark slate blue')
        self.canvas.pack(side='top', anchor="w", pady=10, padx=10)      
        
        self.img = PhotoImage(file="IISC_LOGO.ppm")      
        self.canvas.create_image(60, 60, image=self.img)
        
        self.img1 = PhotoImage(file="Star_Logo_2.gif")      
        self.canvas.create_image(20, 125, anchor='nw', image=self.img1)        #Has to do with attaching the images in the tkinter table
        
        self.img2 = PhotoImage(file="Star_Logo_2.gif")      
        self.canvas.create_image(170, 170, image=self.img2)
        
        self.img3 = PhotoImage(file="Star_Logo_2.gif")      
        self.canvas.create_image(170, 60, image=self.img3)

        self.button1 = Button(self, font=('times new roman', 25, 'bold'), text="View Real Time Display", bg="dark slate blue", fg="cornsilk", command=self.OnButtonClick1)
        self.button1.place(x=420, y=125)

        self.button2 = Button(self, font=('times new roman', 25, 'bold'), text="Query Database", bg="dark slate blue", fg="cornsilk", command=self.OnButtonClick2)
        self.button2.place(x=480, y=250)

        self.button3 = Button(self, font=('times new roman', 25, 'bold'), text="Generate Attendance Sheet", bg="dark slate blue", fg="cornsilk", command=self.OnButtonClick3)
        self.button3.place(x=410, y=375)

    def OnButtonClick1(self):
        global local_count
        self.top1 = Toplevel()
        self.top1.title("Real Time Display")
        # self.top1.geometry("300x150+30+30")
        self.top1.iconbitmap('IISC_LOGO.ppm')              #button 1 fn
        self.top1.transient(self)
        self.button1.config(state='disabled')
        global Total_data_base
        global t
        global count

        t = SimpleTable(self.top1, yc, xc)
        t.pack(side="top", fill="x")

        t.setfir(0, 0, "S.No")
        t.setfir(0, 1, "TwinkleT ID")
        self.topButton1 = Button(self.top1, text="CLOSE", command=self.OnChildClose1)
        self.topButton1.pack(side="bottom")
        print("Check-1")
        t.after(0, Refreshingfun)

    def OnButtonClick2(self):
        self.top2 = Toplevel()
        self.top2.title("Query Database ")
        self.top2.geometry("375x230+30+30")
        self.top2.transient(self)
        self.button2.config(state='disabled')

        OptionList = [                                                          #button 2 func
            "devamma",
            "lakshmamma",
            "manjula n",
            "venkat ramanamma"
        ]

        Label(self.top2, text="Choose the employee:").place(x=105, y=10)
        self.variable = StringVar(self.top2)
        self.variable.set("Choose the employee")

        self.opt = OptionMenu(self.top2, self.variable, *OptionList)
        self.opt.config(width=25, font=('Helvetica', 12),)
        # self.opt.pack(side="top")
        self.opt.place(x=56, y=30)
        self.variable.trace("w", self.get_name)


        self.label2 = Label(self.top2, text="Enter start month:")
        self.label2.place(x=15, y=100)
        self.label3 = Label(self.top2, text="(first 3 letters)")
        self.label3.place(x=25, y=115)
        self.e2 = Entry(self.top2, width=5)
        self.e2.place(x=140, y=100)

        self.label3 = Label(self.top2, text="Enter start date:")
        self.label3.place(x=15, y=130)
        self.e3 = Entry(self.top2, width=5)
        self.e3.place(x=140, y=130)


        self.label5 = Label(self.top2, text="Enter end month:")
        self.label5.place(x=190, y=100)
        self.label5 = Label(self.top2, text="(first 3 letters)")
        self.label5.place(x=200, y=115)
        self.e5 = Entry(self.top2, width=5)
        self.e5.place(x=315, y=100)

        self.label6 = Label(self.top2, text="Enter end date:")
        self.label6.place(x=190, y=130)
        self.e6 = Entry(self.top2, width=5)
        self.e6.place(x=315, y=130)

        self.query_gen_btn = Button(self.top2, text="GENERATE", command=self.query_gen_btn_fn)
        self.query_gen_btn.place(x=150, y=160)

        self.topButton2 = Button(self.top2, text="CLOSE", command=self.OnChildClose2)
        self.topButton2.place(x=163, y=190)


    def get_name(self, *args):
        global employee_name
        employee_name = self.variable.get()

    def query_gen_btn_fn(self, *args):
        #name = self.variable.get()
        start_month = self.e2.get()                                                                 #functions that button functions use
        start_date = self.e3.get()
        end_month = self.e5.get()
        end_date = self.e6.get()
    
        print("name:",employee_name,"\tstart month:",start_month,"\tstart date:",start_date)
        print("\tend month:",end_month,"\tend date:",end_date)


        QueryDatabase(employee_name,start_month,start_date,end_month,end_date)
        print("Generated")


    def OnButtonClick3(self):
        self.top3 = Toplevel()
        self.top3.title("Generate Attendance Sheet")
        self.top3.geometry("300x150+30+30")
        self.top3.transient(self)
        self.button3.config(state='disabled')
        self.label2 = Label(self.top3, text="Enter month:")
        self.label2.place(x=10, y=40)
        self.label3 = Label(self.top3, text="(first 3 letters)")
        self.label3.place(x=5, y=55)                                                # button 3 func
        self.e2 = Entry(self.top3)
        self.e2.place(x=110, y=40)

        self.genbtn = Button(self.top3, text="GENERATE", command=self.get_month_ip)
        self.genbtn.place(x=110, y=70)

        self.topButton3 = Button(self.top3, text="CLOSE", command=self.OnChildClose3)
        self.topButton3.place(x=120, y=105)

    def get_month_ip(self):
        month = self.e2.get()
        print("month: ", month)
        GenerateAttendanceSheet(month)

    def OnChildClose1(self):
        self.button1.config(state='normal')
        self.top1.destroy()

    def OnChildClose2(self):
        self.button2.config(state='normal')
        self.top2.destroy()

    def OnChildClose3(self):
        self.button3.config(state='normal')
        self.top3.destroy()


if __name__ == "__main__":
    print("In main")
    conn = sqlite3.connect('winkle.db')
    print("Opened database successfully")
    window = Window(None)
    window.title("Twinkle VLC Access Control System")
##    window.iconbitmap('IISC_LOGO_ICOFOR.ico')
    window.mainloop()


