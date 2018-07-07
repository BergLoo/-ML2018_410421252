#block1 for training w
from PIL import Image
import numpy as np
import matplotlib.image as mpimg
import random
import os
add = os.getcwd()
im1 = Image.open(add+'/image/key1.png')
im2 = Image.open(add+'/image/key2.png')
im3 = Image.open(add+'/image/I.png')
im4 = Image.open(add+'/image/E.png')

#im1.show()
#im2.show()
#im3.show()

k1 = np.array(im1)
k2 = np.array(im2)
I = np.array(im3)
E = np.array(im4)
EP = k1
IP = k1

#will add random function to creat different w  
w = np.array([[13],[5],[2]])

XD = 0.0000001

#training by gradient descent  
for p in range(0,1):
    for i in range(0,299):
        for j in range(0,399):
             wt = w.transpose()
             xk = np.array([[k1[i,j]],[k2[i,j]],[I[i,j]]])
             ak = np.dot(wt,xk)
             #print ("i = ",i,"w = ",w," ","wt = ",wt," ","xk = ",xk," ","ak = ",ak[0,0],"E = ",[E[i,j]],"XD = ",XD * ([E[i][j]] - ak)*xk,"\n")
             w = w + (XD * (([E[i,j]] - ak)*xk))
             #print ("w = ",w,"\n")
    print ("w = ",w,"\n")


#block2 for test and generate  

#generate E prime  
for i in range(0,299):
    for j in range(0,399):
        IP[i,j] =((E[i,j] - w[0] * k1[i,j] - w[1] * k2[i,j] +1) / w[2])
im5 = Image.fromarray(IP)
im5.show()

#check accuracy by calculate average difference between E[x,y] and EP[x,y]
me = 0
for i in range(0,299):
    for j in range(0,399):
        if IP[i,j] > I[i,j]:
            me += IP[i,j] - I[i,j]
        else:
            me += I[i,j] - IP[i,j]
        #print("i = ",i,"j = ",j,"me = ",me,"EP[i,j] = ",EP[i,j],"E[i,j] = ",E[i,j],"\n")
me = float(me)
me /= (300*400)
print("margin of error = ",me,"\n")
