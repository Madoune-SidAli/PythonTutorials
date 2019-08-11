from tkinter import *
import tkinter as tk
root = Tk()
root.geometry('300x300')

v = tk.IntVar()
radioButton1= Radiobutton(root, variable=v , value=0, text="Male" ,command=lambda: print(v.get()) )
radioButton2= Radiobutton(root, variable=v , value=1, text="Female" ,command=lambda: print(v.get()) )

radioButton1.pack(side=LEFT)
radioButton2.pack(side=LEFT)

root.mainloop()