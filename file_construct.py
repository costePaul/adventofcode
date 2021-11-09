import os

year = 2020

# create the directories
for i in range(25):
    os.makedirs("./"+str(year)+"/day"+str(i+1))

# create the empty dayX.py and input.txt files 
for i in range(25):
    open("./"+str(year)+"/day"+str(i+1)+"/day"+str(i+1)+".py", mode='x')
    open("./"+str(year)+"/day"+str(i+1)+"/input.txt", mode='x')