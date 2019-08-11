from tkinter import *

root = Tk()
root.geometry('300x300')
l = Label(root,text="Hello World!")
l.pack()

def printHello():
    print("Hallo world!")

b = Button(root,text="Click me!",command=printHello)
b.pack(side=BOTTOM)
root.mainloop()
