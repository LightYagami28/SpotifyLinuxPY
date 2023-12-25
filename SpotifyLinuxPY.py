#start call import
import os
import time
import subprocess

#set path of the script
enfolder = 'lang/en/linux.py'
itfolder = 'lang/it/linux.py'

#ask language
lang=input("Which language do you prefer? \n1. English \n2. Italian \n")
if lang == "1":
    subprocess.run(['python', enfolder])
elif lang == "2":
    subprocess.run(['python', itfolder])
else:
    print("Not a valid choise")
    exit()