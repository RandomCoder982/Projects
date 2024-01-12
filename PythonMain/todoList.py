import tkinter as tk
from tkinter import ttk
from customtkinter import CTk, CTkButton#, CTkScrollableFrame

amount = 0
maxLen = 0
items = []

def width():
    global maxLen
    lenghts = [len(string) for string in items]
    maxLen = max(lenghts)

def addList():
    global amount
    items.append(entry.get())
    todoList.insert(amount, entry.get())
    width()
    amount += 1

def removeList():
    global amount
    idx = todoList.get(0, tk.END).index(entry.get())
    items.pop(idx)
    todoList.delete(idx)
    width()
    amount -= 1
    

win = CTk()

todoList = tk.Listbox(win, width=maxLen)
entry = ttk.Entry(win, text="Test")
add = CTkButton(win, text="Press to Add", command=addList,width=40,height=30)
remove = CTkButton(win, text="Press to Remove", command=removeList)
scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL)
todoList.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=todoList.yview)


todoList.grid(row = 2,sticky='nsew')
entry.grid(row=0,sticky='nsew')
add.grid(row=1, column=0, sticky='nsew')
remove.grid(row=1, column=1, sticky='nsew')
scrollbar.grid(row=2, column=1, sticky='nsew')

win.mainloop()