from tkinter import *

root = Tk()
root.geometry('300x300')

mb = Menubutton(root ,text="Menu")
mb.menu = Menu(mb)
mb["menu"]=mb.menu
#add options
mb.menu.add_command(label="option 1",command=lambda : print("yo choose the first option"))
mb.menu.add_command(label="option 2",command=lambda : print("yo choose the second option"))

mb.pack()

root.mainloop()