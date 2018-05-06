from PIL import Image
import numpy as np
import matplotlib.image as mpimg

im1 = Image.open('/home/bergloo/桌面/ML (复件)/key1.png')
im2 = Image.open('/home/bergloo/桌面/ML (复件)/key2.png')
im3 = Image.open('/home/bergloo/桌面/ML (复件)/I.png')
im4 = Image.open('/home/bergloo/桌面/ML (复件)/E.png')

#im1.show()
#im2.show()
#im3.show()

k1 = np.array(im1)
k2 = np.array(im2)
I = np.array(im3)
E = np.array(im4)
EP = k1
IP = k1

w = np.array([[3],[5],[2]])

XD = 0.0000001

for i in range(0,299):
    for j in range(0,399):
         wt = w.transpose()
         xk = np.array([[k1[i,j]],[k2[i,j]],[I[i,j]]])
         ak = np.dot(wt,xk)
         print ("i = ",i,"w = ",w," ","wt = ",wt," ","xk = ",xk," ","ak = ",ak[0,0],"E = ",[E[i,j]],"XD = ",XD * ([E[i][j]] - ak)*xk,"\n")
         w = w + (XD * (([E[i,j]] - ak)*xk))
         print ("w = ",w,"\n")

#block2
for i in range(0,299):
    for j in range(0,399):
        EP[i,j] = w[0] * k1[i,j] + w[1] * k2[i,j] + w[2] * I[i,j]
        
im5 = Image.fromarray((EP*255))
im5.show()

me = 0
for i in range(0,299):
    for j in range(0,399):
        if (E[i,j] != 0):
            me += ((EP[i,j] - E[i,j])/float(E[i,j]) )
        print("i = ",i,"j = ",j,"me = ",me,"EP[i,j] = ",EP[i,j],"E[i,j] = ",E[i,j],"\n","(EP[i,j] - E[i,j])/flaot(E[i,j]) = ",(EP[i,j] - E[i,j])/float(E[i,j]),"\n")
me /= (300*400)
print("margin of error = ",me,"\n") 
