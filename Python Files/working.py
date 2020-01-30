#------------------------------------------TYPO DRAFT---------------------------------------------#
from tkinter import *
import mysql.connector as sc
from tkinter import messagebox

root=Tk()
root.title("TYPO DRAFT")
main=Label(root,text='TYPO DRAFT',height="1",width="10",bg='white',fg='black',font=('Typo Draft Demo','70'))
main.place(x=280,y=10)
root.configure(bg='white')
root.geometry('1920x1080')

#-----------------------------------------ADD NEW NOTES-------------------------------------------#
        
def addnotes():
    root=Tk()
    root.title("ADD NOTES")
    root.geometry("1920x1080")
    l1=Label(root,height='22',width="100",bg='white',font=('Mistrain','20'))
    l1.pack()
    l2=Label(root,height="2",width="15",bg='black',fg="white",text="CREATE NOTE ID : ",font=('Marvel','20','bold'))
    l2.place(x=200,y=38)
    root.configure(bg="black")
    e1=Entry(root,width='61',relief="solid",borderwidth=5,font=('Mistrain','19'))
    e1.place(x=200,y=90)
    t1=Text(root,width='76',relief="solid",borderwidth=5,height='15',font=('Mistrain','15'))
    t1.place(x=201,y=150)
    
    def makenotes():
        try:
            global nid
            nid=e1.get()
            msg=t1.get("1.0", "end")
            con=sc.connect(host="localhost",database='Notes',user='root',password='1234')
            cur=con.cursor()
            query1="insert into new_notes(id,text) values('%s','%s')"%(nid,msg)
            if nid=='':
                messagebox.showinfo("ADDITION STATUS", "Note canot be added")
                root.withdraw()
                root.deiconify()
            elif nid!='':
                cur.execute(query1)
                con.commit()
                messagebox.showinfo("ADDITION STATUS", "Note added Successfully")
                root.withdraw()
                root.deiconify()
                
        except sc.DatabaseError as err:
            if con:
                con.rollback()
                print(err)
        finally:
            con.close()
            cur.close()
            
        e1.delete(0,'end')
        t1.delete('1.0','end')

    b2=Button(root,text="SAVE",command=makenotes,bg="black",padx=50,pady=10,fg='white',font=('Marvel','20','bold'))
    b2.place(x=400,y=570)
    b3=Button(root,text="QUIT",command=root.destroy,bg="black",padx=50,pady=10,fg='white',font=('Marvel','20','bold'))
    b3.place(x=700,y=570)
    root.mainloop()
b1=Button(root,text="ADD NOTES",command=addnotes,bg="black",padx=50,pady=10,fg='white',font=('Marvel',20,'bold'))
b1.place(x=137,y=130)

#--------------------------------------------EDIT NOTES-------------------------------------------#
def editnotes():
    root=Tk()
    root.title("EDIT NOTES")
    root.geometry("1930x1080")
    l1=Label(root,height='22',width="100",bg='white',font=('Mistrain','20'))
    l1.pack()
    l2=Label(root,height="2",width="15",bg='black',fg="white",text="ENTER NOTE ID : ",font=('Marvel','20','bold'))
    l2.place(x=200, y=38)
    root.configure(bg="black")
    e1=Entry(root,relief="solid",borderwidth=5,width='61',font=('Mistrain','19'))
    e1.place(x=200, y=90)
    t1=Text(root, width='76',relief="solid",borderwidth=5,height='15',font=('Mistrain','15'))
    t1.place(x=201, y=150)

    def updatenotes():
        try:
            nid=e1.get()
            msg=t1.get("1.0", "end")
            con=sc.connect(host="localhost", database='Notes', user='root', password='1234')
            cur=con.cursor()
            q="select id from new_notes"
            cur.execute(q)
            data=cur.fetchall()
            query2="update new_notes set text='%s' where id='%s'" % (msg,nid)
            print(data)
            for i in data:
                if nid in i:
                    cur.execute(query2)
                    messagebox.showinfo("UPDATE STATUS", "Note Updated")
                    con.commit()
                    root.withdraw()
                    root.deiconify()
                    break
                elif nid=='':
                    messagebox.showinfo("UPDATE STATUS", "Note not found")
                    root.withdraw()
                    root.deiconify()
                    break
                else:
                    messagebox.showinfo("UPDATE STATUS", "Note not found")
                    root.withdraw()
                    root.deiconify()
                    break
            
        except sc.DatabaseError as err:
            if con:
                con.rollback()
                print(err)
        finally:
            cur.close()
            con.close()
        
        e1.delete(0,'end')
        t1.delete('1.0','end')

    b2=Button(root,text="SAVE",command=updatenotes,bg="black",padx=50,pady=10,fg='white',font=('Marvel','20','bold'))
    b2.place(x=400,y=570)
    b3=Button(root,text="QUIT",command=root.destroy,bg="black",padx=50,pady=10,fg='white',font=('Marvel','20','bold'))
    b3.place(x=700,y=570)
    root.mainloop()
b2=Button(root,text="EDIT NOTES",command=editnotes,bg ="black",padx=55,pady=10,fg='white',font=('Marvel',20,'bold'))
b2.place(x=900,y=130)

#-------------------------------------------LIST BOX----------------------------------------------#
lb1=Listbox(root,width='82',height='5',font=('Mistrain','15'),borderwidth=5,relief="solid")
lb1.place(x=135,y=430)

#--------------------------------------------SEARCH-----------------------------------------------#
l1=Label(root,text='ENTER NOTE ID : ',bg='black',fg='white',font=('Marvel','20','bold'))
l1.place(x=140,y=280)
l2=Label(root,text='LIST ALL MESSAGES : ',bg='black',fg='white',font=('Marvel','20','bold'))
l2.place(x=520,y=190)
e1=Entry(root,borderwidth=5,width='65',relief="solid",font=('Mistrain','19'))
e1.place(x=140,y=310)
def searchnotes():
    try:
        nid=e1.get()
        con=sc.connect(host="localhost",database='Notes',user='root',password='1234')
        cur=con.cursor()
        q="select id from new_notes"
        cur.execute(q)
        data=cur.fetchall()
        query3="select * from new_notes where id={}".format(nid)
        print(data)
        for i in data:
            if nid in i:
                cur.execute(query3)
                data=cur.fetchone()
                lb1.insert(END,data)
                break
            elif nid=='':
                messagebox.showinfo("SEARCH STATUS", "Enter ID to search")
                break
            else:
                messagebox.showinfo("SEARCH STATUS", "Note not found")
                break
        if data==[]:
            messagebox.showinfo("SEARCH STATUS", "No data in database")
            
        con.commit()
    except sc.DatabaseError as err:
        if con:
            con.rollback(err)
            print(err)
    finally:
        cur.close()
        con.close()
    e1.delete(0,'end')
b3=Button(root,text="SEARCH",bg="black",padx=25,pady=5,fg='white',font=('Marvel','20','bold'),command=searchnotes)
b3.place(x=220,y=370)

#-----------------------------------------------DELETE--------------------------------------------#
def deletenotes():
    try:
        nid=e1.get()
        con=sc.connect(host="localhost",database='Notes',user='root',password='1234')
        cur=con.cursor()
        q="select id from new_notes"
        cur.execute(q)
        data=list(cur.fetchall())
        query4="delete from new_notes where id={}".format(nid)
        for i in data:
            if nid in i:
                cur.execute(query4)
                messagebox.showinfo("DELETION STATUS", "Note Deleted")
                break
            elif nid=='':
                messagebox.showinfo("DELETION STATUS", "Enter ID to delete")
                break
            else:
                messagebox.showinfo("DELETION STATUS", "Notes not found to be deleted")
                break
        if data==[]:
            messagebox.showinfo("DELETION STATUS", "No data in database")
        con.commit()
        
    except sc.DatabaseError as err:
        if con:
            con.rollback()
            print(err)
            
        
    finally:
        con.close()
        cur.close()
    e1.delete(0,'end')

b4=Button(root,text="DELETE",bg="black",padx=25,pady=5,fg='white',font=('Marvel','20','bold'),command=deletenotes)
b4.place(x=900,y=370)

#--------------------------------------------SORT NOTES-------------------------------------------#
def sortalphabet():
    try:
        con=sc.connect(host="localhost",database='Notes',user='root',password='1234')
        cur=con.cursor()
        query5="select * from new_notes order by text asc"
        cur.execute(query5)
        data=cur.fetchall()
        result=list(data)
        root=Tk()
        root.title("List of notes")
        scrollbar=Scrollbar(root)
        scrollbar.pack(side=RIGHT,fill=Y)
        root.geometry("500x800")
        mylist=Listbox(root,width="900",yscrollcommand=scrollbar.set,font=('Mistrain','15'))
        for i in result:
            mylist.insert(END,i)
        mylist.pack(side=LEFT,fill=BOTH)
        scrollbar.config(command=mylist.yview)
        root.mainloop()
        con.commit()
    except sc.DatabaseError as err:
        if con:
            con.rollback()
            print(err)
    finally:
        con.close()
        cur.close()
b5=Button(root,text="BY ALPHABETS",bg="black",padx=25,pady=5,fg='white',font=('Marvel', '20', 'bold'),command=sortalphabet)
b5.place(x=420,y=230)

def sortbynum():
    try:
        con=sc.connect(host="localhost",database='Notes',user='root',password='1234')
        cur=con.cursor()
        query6="select * from new_notes order by id asc"
        cur.execute(query6)
        data=cur.fetchall()
        result=list(data)
        root=Tk()
        root.title("List of notes")
        scrollbar=Scrollbar(root)
        scrollbar.pack(side=RIGHT,fill=Y)
        root.geometry("500x800")
        mylist=Listbox(root,width="900",yscrollcommand=scrollbar.set,font=('Mistrain','15'))
        for i in result:
            mylist.insert(END,i)
        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)
        root.mainloop()
        con.commit()
    except sc.DatabaseError as err:
        if con:
            con.rollback()
            print(err)
    finally:
        con.close()
        cur.close()
b6=Button(root,text="BY NUMBERS",bg="black",padx=25,pady=5,fg='white',font=('Marvel','20','bold'),command=sortbynum)
b6.place(x=650,y=230)

#---------------------------------------------EXIT------------------------------------------------#
b7=Button(root,text="EXIT",command=root.destroy,bg="black",fg='white',padx=50,pady=10,font=('Marvel', '18', 'bold'))
b7.place(x=550,y=584)
root.mainloop()
