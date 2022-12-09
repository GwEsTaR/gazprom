from tkinter import *
from tkinter import ttk
import time


root = Tk()

root["bg"]='white'
root.title('Регистратура')
root.wm_attributes('-alpha', 1)
root.geometry('400x100')

root.resizable(width=False, height=False)

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)


btn = Button(root, text='da')
btn.pack()

root.mainloop()