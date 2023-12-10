import tkinter as tk

def update():
    global x
    x += 1
    num.config(text=x)

x = 0
win = tk.Tk()
win.grid()

num = tk.Label(win, text=x)
num.grid()

button = tk.Button(win, text="Click to increment", command=update).grid()


win.mainloop()