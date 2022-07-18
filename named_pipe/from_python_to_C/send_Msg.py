import os
import time
path= "MYFIFO2"
os.mkfifo(path)
while True:
    fifo=open(path,'w')
    string=input("Enter String:\t ")
    fifo.write(string)
    if (string=='end' or string=='exit'):
        break
fifo.close()