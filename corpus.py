from tkinter import *
from tkinter import ttk
import time
#HUI

def btn_click():

    print("eblan")


root = Tk()

root["bg"]='white'
root.title('Регистратура')
root.wm_attributes('-alpha', 1)
root.geometry('400x100')

root.resizable(width=False, height=False)

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)


btn = Button(root, text='net', comman=btn_click)
btn.pack()

root.mainloop()