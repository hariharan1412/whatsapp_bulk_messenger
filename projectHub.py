from tkinter import *
from PIL import Image, ImageTk
from spamMsger import spam
from bulkMsg import bulk


def start():
    root.destroy()

    c  = Tk()
    
    B = Button(c, text=" SPAM MSG "  ,command=spam.spamMain , width=50 , height=10 )
    B.grid(row=0 , column=1 , columnspan=4 )

    
    B1 = Button(c, text=" BULK MSG "  ,command=bulk.bulkMain , width=50 , height=10 )
    B1.grid(row=1 , column=1 , columnspan=4 )

    c.mainloop()

root = Tk()
root.title(" PROJECT HUB ")
photo = PhotoImage(file = r"./myimage (1).png")
photo = photo.subsample(3, 3)
rB = Button(root, image = photo ,command=start)
rB.pack(side = TOP)

root.mainloop()