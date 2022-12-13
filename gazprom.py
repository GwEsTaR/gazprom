import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='root',
        db='Bolnica',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=10, column=0, columnspan=5, rowspan=11, padx=10, pady=45)


root = Tk()
root.title("Регистратура")
root.geometry("950x590")
my_tree = ttk.Treeview(root)

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()


def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)
    if num ==6:
        ph6.set(word)
    

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bolnica_db")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    Pacientid = str(PacientidEntry.get())
    name = str(nameEntry.get())
    fam = str(famEntry.get())
    otce = str(otcEntry.get())
    address = str(addressEntry.get())
    phone = str(telephoneEntry.get())

    if (Pacientid == "" or Pacientid == " ") or (name == "" or name == " ") or (fam == "" or fam == " ") or (otce == "" or otce == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Ошибка", "Заполните пустые ячейки")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bolnica_db VALUES ('"+Pacientid+"','"+name+"','"+fam+"','"+otce+"','"+address+"','"+phone+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Ошибка", "Номер пациента уже занят")
            return
        nameEntry.delete(0, tk.END)
        PacientidEntry.delete(0, tk.END)
        famEntry.delete(0, tk.END)
        otcEntry.delete(0, tk.END)
        telephoneEntry.delete(0, tk.END)
        addressEntry.delete(0, tk.END)
    refreshTable()
    

def delete():
    decision = messagebox.askquestion("Предупреждение", "Вы уверены что хотите удалить пациента?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM bolnica_db WHERE PACIENTID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Ошибка")
            return

        refreshTable()

def search():
    Pacientid = str(PacientidEntry.get())
    name = str(nameEntry.get())
    fam = str(famEntry.get())
    otce = str(otcEntry.get())
    address = str(addressEntry.get())
    phone = str(telephoneEntry.get())


    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bolnica_db WHERE PACIENTID='"+
    Pacientid+"' or NAME='"+
    name+"' or FAM='"+
    fam+"' or ADDRESS='"+
    address+"' or PHONE='"+
    phone+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,6):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Ошибка", "Данные не найдены")

    

def update():
    selectedPacientid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedPacientid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Ошибка", "Пожалуйста, выберите пациента")

    Pacientid = str(PacientidEntry.get())
    name = str(nameEntry.get())
    fam = str(famEntry.get())
    otce=str(otcEntry.get())
    address = str(addressEntry.get())
    phone = str(telephoneEntry.get())

    if (Pacientid == "" or Pacientid == " ") or (name == "" or name == " ") or (fam == "" or fam == " ") or (otce == "" or otce == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Ошибка", "Заполните ячейки")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE bolnica_db SET PACIENTID='"+
            Pacientid+"', NAME='"+
            name+"', FAM='"+
            fam+"', OTC='"+
            otce+"', ADDRESS='"+
            address+"', PHONE='"+
            phone+"' WHERE PACIENTID='"+
            selectedPacientid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Ошибка", "Пациент уже существует")
            return

    refreshTable()

def clear():
    nameEntry.delete(0, tk.END)
    PacientidEntry.delete(0, tk.END)
    famEntry.delete(0, tk.END)
    otcEntry.delete(0, tk.END)
    telephoneEntry.delete(0, tk.END)
    addressEntry.delete(0, tk.END)
    refreshTable()

label = Label(root, text="Система регистрации медецинских карт", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

PacientidLabel = Label(root, text="Номер", font=('Arial', 15))
nameLabel = Label(root, text="Имя", font=('Arial', 15))
famLabel = Label(root, text="Фамилия", font=('Arial', 15))
otcLabel= Label(root, text="Отчество", font=('Arial', 15))
addressLabel = Label(root, text="Адрес", font=('Arial', 15))
telephoneLabel = Label(root, text="Телефон", font=('Arial', 15))


PacientidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
nameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
famLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
otcLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
addressLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)
telephoneLabel.grid(row=8, column=0, columnspan=1, padx=50, pady=5)

PacientidEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
nameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
famEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
otcEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
addressEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)
telephoneEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph6)


PacientidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
famEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
otcEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
addressEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)
telephoneEntry.grid(row=8, column=1, columnspan=4, padx=5, pady=0)


addBtn = Button(
    root, text="Добавить", width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=add)
updateBtn = Button(
    root, text="Обновить",width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Удалить", width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=delete)

searchBtn = Button(
    root, text="Поиск",width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=search)

clearBtn = Button(
    root, text="Очистить", width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=clear) 


addBtn.grid(row=9,padx=7, pady=3,rowspan=2)
updateBtn.grid(row=9, padx=7, column=1,rowspan=2)
deleteBtn.grid(row=9, padx=7, column=3,rowspan=2)
searchBtn.grid(row=9, padx=7, column=2,rowspan=2)
clearBtn.grid(row=9, padx=7, column=4,rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("PacientNomer","name","fam","otc","Address","Telephone")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("PacientNomer", anchor=W, width=170)
my_tree.column("name", anchor=W, width=150)
my_tree.column("fam", anchor=W, width=150)
my_tree.column("otc", anchor=W, width=150)
my_tree.column("Address", anchor=W, width=165)
my_tree.column("Telephone", anchor=W, width=150)


my_tree.heading("PacientNomer", text="Номер", anchor=W)
my_tree.heading("name", text="Имя", anchor=W)
my_tree.heading("fam", text="Фамилия", anchor=W)
my_tree.heading("otc", text="Отчество", anchor=W)
my_tree.heading("Address", text="Адреc", anchor=W)
my_tree.heading("Telephone", text="Телефон", anchor=W)

refreshTable()

root.mainloop()