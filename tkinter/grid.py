from tkinter import *

root = Tk()

#Creating a label wdget
myLabel =  Label(root, text="Hello world")
myLabel1 = Label(root, text="This is me")
myLabel2 = Label(root, text="Gianfranco")

#Showing into the screen
myLabel.grid(row=0, column=0)
myLabel1.grid(row=1, column=2)
myLabel2.grid(row=2, column=4)

root.mainloop()