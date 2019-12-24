#TYPO DRAFT starting user interface.

import tkinter as tk
from tkinter import *
import mysql.connector as sc

root=Tk()
root.title("TYPO DRAFT")
p=Label(root,text=" TYPO \nDRAFT", height="3",width="250",bg='white',fg='black',font=('Typo Draft Demo','80'))
p.pack()
root.configure(bg='white',borderwidth=5, relief="solid")
root.geometry('400x600')
def notes():
    import working
def dest():
    root.destroy()
def create():
    try:
        con=sc.connect(host="localhost",database='Notes',user='root',password='1234')
        cur=con.cursor()
        query1="create database if not exists Notes;"
        query2="create table if not exists new_notes(id varchar(50) primary key,text text(4294967295));"
        cur.execute(query1)
        cur.execute(query2)
        con.commit()
    except sc.DatabaseError as err:
        if con:
            con.rollback()
            print(err)
    finally:
        con.close()
        cur.close()
def func():
    dest()
    create()
    notes()

b1=Button(root,text="START APP",command=func,bg ="black",fg='white',padx=40,pady=10,font=('Marvel','15','bold'))
b1.pack()
b2=Button(root,text="EXIT",command=root.destroy,bg ="black",fg='white',padx=40,pady=10,font=('Marvel','15','bold'))
b2.pack(padx=20,pady=10)
root.mainloop()
