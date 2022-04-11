#Run Code
import os
import subprocess #Open Other Files

subprocess.run("Database_Open.cmd",shell=False)   #Open Databse store program
subprocess.run(["python.exe","Data_Display_DB.py"],shell=False) #Open GUI Program

#EndRun