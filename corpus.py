import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#import mysql.connector
import pymysql
1
def connection():
    con=pymysql.connect(host='localhost', user='root', password='', db='Bolnica')
    return con

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for arry in read():
        my_tree.insert(parent='', index='end', iid=arry, text="", values=(arry), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial',12))
    my_tree.grid(row=6, column=0, padx=1, pady=1, sticky=W+E)

def read():
    con=connection()
    cursor=con.cursor()
    cursor.execute('SELECT * FROM Reg')
    result=cursor.fetchall()
    con.commit()
    con.close()
    return result


root = Tk()
root["bg"]='white'
root.title('Регистратура')
#root.wm_attributes('-alpha', 1)
my_tree = ttk.Treeview(root)
root.geometry('875x550')
root.resizable(width=False, height=False)

Label(text="Регистратура", font=('Arial Bold',25)).grid(row=1,column=0, sticky=W, padx=350, pady=5)
Label(text="Имя", font=('Arial Bold',20)).grid(row=2,column=0, sticky=W, padx=10, pady=5)
Label(text="Фамилия", font=('Arial Bold',20)).grid(row=3,column=0, sticky=W, padx=10, pady=5)
Label(text="Отчество", font=('Arial Bold',20)).grid(row=4,column=0, sticky=W, padx=10, pady=5)
Label(text="Телефон", font=('Arial Bold',20)).grid(row=5,column=0, sticky=W, padx=10, pady=5)

nameEntry=Entry(root, width=20, bd=5, font=('Arial',10)).grid(row=2,column=0, sticky=W, padx=170, pady=5)
FamEntry=Entry(root, width=20, bd=5, font=('Arial',10)).grid(row=3,column=0, sticky=W, padx=170, pady=5)
OtcEntry=Entry(root, width=20, bd=5, font=('Arial',10)).grid(row=4,column=0, sticky=W, padx=170, pady=5)
TelephoneEntry=Entry(root, width=20, bd=5, font=('Arial',10)).grid(row=5,column=0, sticky=W, padx=170, pady=5)

addButton=Button(root,text="Добавить", font=('Arial',12)).grid(row=7, pady=3)


style=ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold',30))
my_tree['columns']=("Имя", "Фамилия", "Отчество", "Телефон")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Имя", width=170)
my_tree.column("Фамилия",  width=170)
my_tree.column("Отчество",  width=170)
my_tree.column("Телефон", width=170)

my_tree.heading("Имя", text="Имя", anchor=W)
my_tree.heading("Фамилия", text="Фамилия", anchor=W)
my_tree.heading("Отчество", text="Отчество", anchor=W)
my_tree.heading("Телефон", text="Телефон", anchor=W)

refreshTable()

root.mainloop()