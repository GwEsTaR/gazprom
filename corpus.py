import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pymysql

root = Tk()
root["bg"]='white'
root.title('Регистратура')
#root.wm_attributes('-alpha', 1)
my_tree = ttk.Treeview(root)
root.geometry('900x600')
root.resizable(width=False, height=False)

Label(text="Регистратура", font=('Arial Bold',25)).grid(row=1,column=0, sticky=W, padx=350, pady=5)
Label(text="Имя", font=('Arial Bold',20)).grid(row=2,column=0, sticky=W, padx=10, pady=5)
Label(text="Фамилия", font=('Arial Bold',20)).grid(row=3,column=0, sticky=W, padx=10, pady=5)
Label(text="Отчесвтво", font=('Arial Bold',20)).grid(row=4,column=0, sticky=W, padx=10, pady=5)
Label(text="Телефон", font=('Arial Bold',20)).grid(row=5,column=0, sticky=W, padx=10, pady=5)

nameEntry=Entry(root, width=20, bd=5, font=('Arial',10)).grid(row=2,column=0, sticky=W, padx=170, pady=5)
FamEntry=Entry(root, width=20, bd=5, font=('Arial',10)).grid(row=3,column=0, sticky=W, padx=170, pady=5)
OtcEntry=Entry(root, width=20, bd=5, font=('Arial',10)).grid(row=4,column=0, sticky=W, padx=170, pady=5)
TelephoneEntry=Entry(root, width=20, bd=5, font=('Arial',10)).grid(row=5,column=0, sticky=W, padx=170, pady=5)

addButton=Button(root,text="Добавить", font=('Arial',12)).grid(row=6, pady=320)

#Нерабочая хуйня(лучше не трогать)
'''
style=ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold',30))
my_tree['columns']=("Stud ID", "First")

my_tree.column("#0", width=0, stretch=NO)
my_tree.heading("Stud ID", text="Student ID", anchor=W)
my_tree.column("#0", width=0, stretch=NO)
my_tree.heading("First", text="Name", anchor=W)
'''

root.mainloop()