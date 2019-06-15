from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()

root.geometry("500x500")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
frame = tk.Frame(root,width=400,height=400,bg="yellow")
frame.grid_propagate(0)
frame.grid_columnconfigure(0,weight=1)
frame.grid_rowconfigure(0,weight=1)
frame.grid_columnconfigure(1,weight=1)
frame.grid_rowconfigure(1,weight=1)
frame.grid()

# keyboard=Frame(frame,padx=5,pady=5,bg="red")
# keyboard.grid(row=0,column=0, sticky=NSEW)

keyboard=Frame(frame,padx=5,pady=5,bg="pink")
keyboard.grid_rowconfigure(1, weight=1)
keyboard.grid_columnconfigure(1, weight=1)
keyboard.grid(row=1,column=0,columnspan=2, sticky=NSEW)

# for row, row_buttons in enumerate([['%', '√x', 'x²', '1/x'], ["C", "←", "÷"]]):
#     keyboard.grid_rowconfigure(row, weight=1)
#     for col, text in enumerate(row_buttons):
#         keyboard.grid_columnconfigure(col, weight=1)
#         Button(keyboard, padx=5, pady=5, text=text).grid(row=row, column=col, sticky='EWNS')
root.mainloop()