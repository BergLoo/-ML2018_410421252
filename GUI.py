from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import os
address = os.getcwd()
im1 = Image.open(address+'/image/key1.png')
im2 = Image.open(address+'/image/key2.png')
k1 = np.array(im1)
k2 = np.array(im2)


if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)


    #function to be called when mouse is clicked
    def printcoords():
        File = filedialog.askopenfilename(parent=root, initialdir='C:/',title='Choose an image.')
        im3 = Image.open(File)
        filename = ImageTk.PhotoImage(im3)
        canvas.image = filename  # <--- keep reference of your image
        canvas.create_image(0,0,anchor='nw',image=filename)
        E1 = np.array(im3)
        w = np.array([[0.24994724],[0.66296781],[0.09225696]])
        IP = np.zeros(shape=(300,400))
        for i in range(0,300):
            for j in range(0,400):
                IP[i,j] =((E1[i,j] - w[0] * k1[i,j] - w[1] * k2[i,j]+1) / w[2])
        im5 = Image.fromarray(IP)
        im5.show()
    
    Button(root,text='choose',command=printcoords).pack()
    
    root.mainloop()
