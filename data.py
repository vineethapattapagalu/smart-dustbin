import numpy as np
import csv
n=3
moisture=list()
height=list()
width=list()
file=open("testing.txt")
clean=list(file)
cl=[i.split(':') for i in clean]
out=np.concatenate(cl).tolist()
del out[-1]
for i, val in enumerate(out):
    x=i%n
    if (x==0):
        moisture.append(val)
    elif(x==1):
        height.append(val)
    else:
        width.append(val)
print(moisture)
print(height)
print(width)

csvfile=open('sensordata.csv','w',newline='')
obj=csv.writer(csvfile)
for data in moisture,height,width:
    obj.writerow(data)
csvfile.close()
#print(out)
