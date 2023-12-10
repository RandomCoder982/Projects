from tkinter import *
import time

root = Tk()
lab = Label(root, font=("calibri", 40, 'bold'), background="purple", foreground="white")
lab.pack()

def update():
   lab['text'] = time.ctime()
   root.after(1000, update) # run itself again after 1000 ms

# run first time
update()

root.mainloop()