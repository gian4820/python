from tkinter import *

root = Tk()

def Click():
    #Creating a label wdget
    myLabel =  Label(root, text="Click the button")
    myLabel.pack()

button = Button(root, text="Click me", command=Click, fg="blue")
button.pack()

root.mainloop()