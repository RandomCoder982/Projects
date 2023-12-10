import random
import tkinter as tk

def update():
    x = random.randint(1, 6)
    dice.config(text="You rolled a " + str(x))

win = tk.Tk()

dice = tk.Label(win, text="Hello World")
dice.grid(column=0, row=0)
button = tk.Button(win, text="Press to roll dice", command=update).grid(column=0, row=1)

win.mainloop()
