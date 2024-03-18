import tkinter as tk

getScreenSize = lambda: ((lambda root: (root.winfo_screenwidth(),root.winfo_screenheight(),root.destroy())[:-1])(__import__('tkinter').Tk()))

def changeText():
    change = entry.get()
    greeting.config(text=change)

win = tk.Tk()

greeting = tk.Label(win, text="Test")
entry = tk.Entry(win)
change = tk.Button(win, text="Change", command=changeText)

greeting.grid(row=0, column=0, columnspan=2)  # Adjusted grid placement
entry.grid(row=1, column=0,)  # Added sticky parameter
change.grid(row=1, column=1, )  # Added sticky parameter

win.mainloop()
