import os

year = 2023

# create the directories with the empty dayX.py and input.txt files 
for i in range(25):
    s = str(i+1)
    if len(s)==1:
        s = '0'+s
    os.makedirs("./"+str(year)+"/day"+s)
    open("./"+str(year)+"/day"+s+"/day"+s+".py", mode='x')
    open("./"+str(year)+"/day"+s+"/input.txt", mode='x')