import time
from tkinter import *

def update():
    global secs
    
    if secs > 1:
        lab['text'] = f"TimeLeft: {int(round(secs/60, 1))}:{secs%60}"
        root.after(1000, update) # run itself again after 1000 ms
        secs -= 1
    else:
        lab["text"] = "Input a new number"
        root.after(1000, update)
        
    
    
    
def getInput():
    global secs
    
    input = entry.get()
    intput = round(float(input), 2)
    secs = intput

global secs
secs = input("Enter a number: ")

while True:
    try:
        secs = int(secs)
        break
    except:
        secs = input("Enter a number: ")

root = Tk()
root.config(background="purple")

lab = Label(root, font=("calibri", 40, 'bold'), background="purple", foreground="white")
lab.pack()

entry = Entry(root, text="Test")
entry.pack()

button = Button(root, text="Set Timer", command=getInput)
button.pack()



# run first time
update()

root.mainloop()
