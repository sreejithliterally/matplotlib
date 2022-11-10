from asyncore import read
import matplotlib.pyplot as plt
from numpy import double
y1=[]
y2=[]

STATE = 0
STATE2 = 0
fd = open("data.txt","r")
for line in fd:
    for word in line.split():
        if 1 == STATE:
            t = word
            y1.append(float(t))
           
            STATE = 0
        if word == "val_accuracy:":
        #if word == "taccuracy:":
        #if word == "val_loss":
        #if word == "tloss:":
            STATE = 1



     

print(y1)



