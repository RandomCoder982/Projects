import tkinter as tk
from functools import partial

def calculateBMI(weight, height):
    userWeight = int(weight.get())
    userHeight = int(height.get())
    userHeight = (userHeight/100)**2
    BMI = userWeight/userHeight
    return BMI

def changeBMI():
    bmi = calculateBMI(weight, height)
    output.configure(text="Your BMI is " + str(round(bmi, 2)))

def reset():
    age.delete(0, "end")
    weight.delete(0, "end")
    height.delete(0, "end")

win = tk.Tk()
win.title("Bmi Calculator")
buttonPressed = tk.IntVar()

tk.Label(win, text = "How old are you (2-120) ").grid(column=0,row=0)
age = tk.Entry(win)

tk.Label(win, text="Select gender").grid(column=0, row=2)
male = tk.Radiobutton(win, text="Option 1", variable=buttonPressed, value=1)
fmale = tk.Radiobutton(win, text="Option 2", variable=buttonPressed, value=2)

tk.Label(win, text="Enter height (cm)").grid(column=0, row=3)
height = tk.Entry(win)

tk.Label(win, text="Enter Weight (kg)").grid(column=0, row=4)
weight = tk.Entry(win)

output = tk.Label(win, text="Your BMI is ")

calculateCallable = partial(calculateBMI, weight, height)

exit = tk.Button(win, text="Exit", command=win.destroy)
exit.grid(column=0, row=7)
exit.config(width=20)

Calculate = tk.Button(win, text="Calculate", command=changeBMI)
Calculate.grid(column=1, row=7)
Calculate.config(width=20)

reset = tk.Button(win, text="reset", command=reset)
reset.grid(column=2, row=7)
reset.config(width=20)


age.grid(column = 1, row = 0)
male.grid(column=1, row=2)
fmale.grid(column=2, row=2)
height.grid(column=1, row=3)
weight.grid(column=1, row=4)
output.grid(column=1, row=6)

win.mainloop()