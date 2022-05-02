#Reset Database
import os
import subprocess

subprocess.run(["python.exe","Delete_DB.py"],shell=False)
subprocess.run(["python.exe","Create_DB.py"],shell=False)

#EndOfDBReset
