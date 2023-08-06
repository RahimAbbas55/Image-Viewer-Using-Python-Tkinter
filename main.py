from tkinter import *
from PIL import  Image , ImageTk

root = Tk()

def forward( imgNum ):
    global label1
    global forward
    global back

    label1.grid_forget()
    label1 = Label ( image = image_list [ imgNum - 1])
    forwardButton = Button(root, text=">>", command=lambda: forward(imgNum + 1))
    backButton = Button(root, text="<<", command= lambda: back( imgNum - 1 ))

    if imgNum == 4:
        forwardButton = Button ( root, text = ">>" , state= DISABLED)

    label1.grid (row=0 , column = 0, columnspan=3)
    backButton.grid(row=1, column=0)
    forwardButton.grid(row=1, column=2)
def back( imgNum ):
    global label1
    global forward
    global back

    label1.grid_forget()
    label1 = Label ( image = image_list [ imgNum - 1])
    forwardButton = Button(root, text=">>", command=lambda: forward(imgNum + 1))
    backButton = Button(root, text="<<", command= lambda: back( imgNum - 1 ))

    label1.grid(row=0, column=0, columnspan=3)
    backButton.grid(row=1, column=0)
    forwardButton.grid(row=1, column=2)


my_img1 = ImageTk.PhotoImage ( Image.open("/Users/rahimabbas/Downloads/Images/1.jpeg") )
my_img2 = ImageTk.PhotoImage ( Image.open("/Users/rahimabbas/Downloads/Images/2.jpeg") )
my_img3 = ImageTk.PhotoImage ( Image.open("/Users/rahimabbas/Downloads/Images/3.jpeg") )
my_img4 = ImageTk.PhotoImage ( Image.open("/Users/rahimabbas/Downloads/Images/4.jpeg") )


image_list = [ my_img1 , my_img2 , my_img3 , my_img4 ]
label1 = Label ( image = my_img1)
label1.grid( row = 0 , column = 0 , columnspan = 3)

backButton = Button ( root , text = "<<"  , command = lambda: back(1) , state = DISABLED)
exitButton = Button (root , text = "Exit" , command = root.quit )
forwardButton = Button ( root , text = ">>" , command = lambda: forward(2))

backButton.grid ( row = 1 , column = 0 )
exitButton.grid ( row = 1 , column = 1)
forwardButton.grid ( row = 1 , column = 2 )


root.mainloop()