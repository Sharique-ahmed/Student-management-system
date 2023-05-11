from tkinter import *
from tkinter import ttk
import datetime
import tkinter.font as tkf
from tkcalendar import Calendar , DateEntry
import sqlite3
from tkinter import messagebox


screen = Tk()
screen.title('Student Management System')
screen.geometry("660x500")
screen.configure(bg="black")
screen.resizable("False","False")
tkf.families()

#Setting up the title
titl = Label(screen,text="Student Management System",bg="cyan",font=("Comic Sans Ms",14),height=2)
titl.grid(row=0,column=0,ipadx=200,columnspan=4)


#Creating the Database
# Database needs to be created once then add values after commenting this out
#creating a database
connect = sqlite3.connect('studentdata.db')

#creating a cursor for keeping track on rows or column
cursor = connect.cursor()

#Creating the rows and columns
#cursor.execute("""
#               CREATE TABLE studentdata(
#                   Name text,
#                   Reg_no integer,
#                   class text,
#                   ph_no integer,
#                   Address text,
#                  email text,
#                   Gender text,
#                   Dateofbirth integer)
#                   """) 

# Data types in python sql are text,blob(images),integer,realno,null

#Adding values to the rows and column

#setting the main labels

Name = Label(screen,text="Name of student",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
Name.grid(row=1,column=0,ipadx=98,columnspan=2,pady=3)
Reg_No = Label(screen,text="Register Number",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
Reg_No.grid(row=2,column=0,ipadx=96,columnspan=2,pady=3)
clas = Label(screen,text="Class",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
clas.grid(row=3,column=0,ipadx=142,columnspan=2,pady=3)
phno = Label(screen,text="Phone Number",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
phno.grid(row=4,column=0,ipadx=108,columnspan=2,pady=3)
address = Label(screen,text="Address",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
address.grid(row=5,column=0,ipadx=130,columnspan=2,pady=3)
email = Label(screen,text="Email",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
email.grid(row=6,column=0,ipadx=130,columnspan=2,pady=3)
gender = Label(screen,text="Gender",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
gender.grid(row=7,column=0,ipadx=130,columnspan=2,pady=3)
DOB = Label(screen,text="Date of birth",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
DOB.grid(row=8,column=0,ipadx=110,columnspan=2,pady=3)

#setting the main entry's

Nentry = Entry(screen,width=47)
Nentry.grid(row=1,column=2,columnspan=2,ipady=4)

Rentry = Entry(screen,width=47)
Rentry.grid(row=2,column=2,columnspan=2,ipady=4)

Centry = Entry(screen,width=47)
Centry.grid(row=3,column=2,columnspan=2,ipady=4)

Pentry = Entry(screen,width=47)
Pentry.grid(row=4,column=2,columnspan=2,ipady=4)

Aentry = Entry(screen,width=47)
Aentry.grid(row=5,column=2,columnspan=2,ipady=4)

Eentry = Entry(screen,width=47)
Eentry.grid(row=6,column=2,columnspan=2,ipady=4)

#combobox creation
data = StringVar()
data.set("Select Gender")
Gender = ttk.Combobox(screen,width=44,textvariable=data)
Gender['values'] =("Male",
"Female",
"Other"
)
Gender.grid(row=7,column=2,columnspan=2,ipady=3)

Dentry = DateEntry(screen,width=43)
Dentry.grid(row=8,column=2,columnspan=2)





#setting up the Save button

def save():

    if Nentry.get()=="" or Rentry.get() == "" or Centry.get()=="" or Pentry.get() =="" or Aentry.get() == "" or Eentry.get() == "" or data.get() =="Select a Gender":
        messagebox.showerror("Error","Please fill all the fields")
    else:
        #creating a database
        connect = sqlite3.connect('studentdata.db')
        #creating a cursor for keeping track on rows or column
        cursor = connect.cursor()

        # Adding the values                            naming the widgets 
        cursor.execute('INSERT INTO studentdata VALUES(:Name,:Regno,:Class,:PH_no,:Address,:Email,:Gender,:DateOfBirth)',
        {
            "Name":Nentry.get(),
            "Regno":Rentry.get(),
            "Class":Centry.get(),
            "PH_no":Pentry.get(),
            "Address":Aentry.get(),
            "Email":Eentry.get(),
            "Gender":data.get(),
            "DateOfBirth":Dentry.get_date()
        })
        
        
        #commiting the changes done 
        connect.commit()
        #closing the database
        connect.close()


        Nentry.delete(0,END)
        Rentry.delete(0,END)
        Centry.delete(0,END)
        Pentry.delete(0,END)
        Aentry.delete(0,END)
        Eentry.delete(0,END)
        data.set("Select a Gender")
        Dentry.delete(0,END)
    
Save = Button(screen,text="Save record",command=save)
Save.grid(row=9,column=1,columnspan=2,pady=(20,0),ipadx=190,ipady=5)

#Setting up the Show record button

def show():
    newscreen = Toplevel()
    newscreen.title("Student Data")
    newscreen.geometry("950x600")
    newscreen.config(bg="black")
    newscreen.resizable("False","False")

    tree = ttk.Treeview(newscreen,selectmode="browse",height=25)
    tree.grid(row=0,column=0,columnspan=2)
    style = ttk.Style(newscreen)
    style.theme_use('clam')
    style.configure("Treeview",background="black",fieldbackground="black",foreground="white")


    tree["columns"] = ("1","2","3","4","5","6","7","8","9")
    tree["show"] = "headings"


    tree.column("1",anchor="center",width=60)
    tree.heading("1", text="ID")

    tree.column("2",anchor="center",width=110)
    tree.heading("2",text="Name")

    tree.column("3",anchor="center",width=73)
    tree.heading("3",text="Register No")

    tree.column("4",anchor="center",width=60)
    tree.heading("4",text="Class")
    
    tree.column("5",anchor="center",width=110)
    tree.heading("5",text="Phone Number")
    
    tree.column("6",anchor="center",width=165)
    tree.heading("6",text="Address")

    tree.column("7",anchor="center",width=150)
    tree.heading("7",text="Email")
    
    tree.column("8",anchor="center",width=110)
    tree.heading("8",text="Gender")
    
    tree.column("9",anchor="center",width=110)
    tree.heading("9",text="Date of birth")



    
    #creating a database
    connect = sqlite3.connect('studentdata.db')
    #creating a cursor for keeping track on rows or column
    cursor = connect.cursor()

    # Adding the values                            
    cursor.execute('SELECT oid,* FROM studentdata')
    records = cursor.fetchall()
    for row in records:
        tree.insert("",'end',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

    #commiting the changes done 
    connect.commit()
    #closing the database
    connect.close()

    #deleting a row 
    def deletes():
        #creating a database
        connect = sqlite3.connect('studentdata.db')
        #creating a cursor for keeping track on rows or column
        cursor = connect.cursor()
        selected = tree.selection()[0]
        print(type(selected))
        id = ""
        if selected[2] != "0":
            id = selected[2:4]
        else:
            id = selected[3]
        tree.delete(selected)

        # Adding the values                            
        cursor.execute("DELETE from studentdata WHERE oid="+id)
        
        
        #commiting the changes done 
        connect.commit()
        #closing the database
        connect.close()

    dell = Button(newscreen,text="Delete",command=deletes,bg="red",foreground="black")
    dell.grid(row=1,column=0,ipadx=40,ipady=10)

    def update():
        editor = Toplevel()
        editor.title("Update")
        editor.geometry("690x380")
        editor.configure(bg="black")
        editor.resizable("False","False")

        #setting the main labels

        Name = Label(editor,text="Name of student",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
        Name.grid(row=1,column=0,ipadx=98,columnspan=2,pady=3)
        Reg_No = Label(editor,text="Register Number",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
        Reg_No.grid(row=2,column=0,ipadx=96,columnspan=2,pady=3)
        clas = Label(editor,text="Class",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
        clas.grid(row=3,column=0,ipadx=142,columnspan=2,pady=3)
        phno = Label(editor,text="Phone Number",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
        phno.grid(row=4,column=0,ipadx=108,columnspan=2,pady=3)
        address = Label(editor,text="Address",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
        address.grid(row=5,column=0,ipadx=130,columnspan=2,pady=3)
        email = Label(editor,text="Email",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
        email.grid(row=6,column=0,ipadx=130,columnspan=2,pady=3)
        gender = Label(editor,text="Gender",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
        gender.grid(row=7,column=0,ipadx=130,columnspan=2,pady=3)
        DOB = Label(editor,text="Date of birth",bg="black",font=("Comic Sans Ms",12,"italic"),foreground="white")
        DOB.grid(row=8,column=0,ipadx=110,columnspan=2,pady=3)

        #setting the main entry's


        global Nentry2
        global Rentry2
        global Centry2
        global Pentry2
        global Aentry2
        global Eentry2
        global Gentry2
        global Dentry2


        Nentry2 = Entry(editor,width=47)
        Nentry2.grid(row=1,column=2,columnspan=2,ipady=4)

        Rentry2 = Entry(editor,width=47)
        Rentry2.grid(row=2,column=2,columnspan=2,ipady=4)

        Centry2 = Entry(editor,width=47)
        Centry2.grid(row=3,column=2,columnspan=2,ipady=4)

        Pentry2 = Entry(editor,width=47)
        Pentry2.grid(row=4,column=2,columnspan=2,ipady=4)

        Aentry2 = Entry(editor,width=47)
        Aentry2.grid(row=5,column=2,columnspan=2,ipady=4)

        Eentry2 = Entry(editor,width=47)
        Eentry2.grid(row=6,column=2,columnspan=2,ipady=4)

        #combobox creation
        global data2
        data2 = StringVar()
        data2.set("Select a Gender")
        Gender2 = ttk.Combobox(editor,width=44,textvariable=data2)
        Gender2['values'] =("Male",
        "Female",
        "Other"
        )
        Gender2.grid(row=7,column=2,columnspan=2,ipady=3)

        Dentry2 = DateEntry(editor,width=43)
        Dentry2.grid(row=8,column=2,columnspan=2)

        #converting the id into single value
        selected = tree.selection()[0]
        id = ""
        if selected[2] != "0":
            id = selected[2:4]
        else:
            id = selected[3]

        #creating a database
        connect = sqlite3.connect('studentdata.db')
        #creating a cursor for keeping track on rows or column
        cursor = connect.cursor()

        # Adding the values                            
        cursor.execute('SELECT * FROM studentdata WHERE oid='+id)
        records = cursor.fetchall()      
        
        for row in records:
            Nentry2.insert(0,row[0])
            Rentry2.insert(0,row[1])
            Centry2.insert(0,row[2])
            Pentry2.insert(0,row[3])
            Aentry2.insert(0,row[4])
            Eentry2.insert(0,row[5])
            data2.set(row[6])



        #Updating sql Command
        def updat():
            #creating a database
            connect = sqlite3.connect('studentdata.db')
            #creating a cursor for keeping track on rows or column
            cursor = connect.cursor()


            selected = tree.selection()[0]
            id = ""
            if selected[2] != "0":
                id = selected[2:4]
            else:
                id = selected[3]
            # updating the values                            
            cursor.execute('''UPDATE studentdata SET
            Name=:naam,
            Reg_no=:reg ,
            class=:clas ,
            ph_no=:phn ,
            Address=:addres ,
            email=:emails,
            Gender=:gend ,
            Dateofbirth=:dob

            WHERE oid = :oid''',
            {
                "oid":id,
                "naam":Nentry2.get(),
                "reg":Rentry2.get(),
                "clas":Centry2.get(),
                "phn":Pentry2.get(),
                "addres":Aentry2.get(),
                "emails":Eentry2.get(),
                "gend":data2.get(),
                "dob":Dentry2.get_date()

            })
            
            records = cursor.fetchall()      
            #commiting the changes done 
            connect.commit()
            #closing the database
            connect.close()

            Nentry2.delete(0,END)
            Rentry2.delete(0,END)
            Centry2.delete(0,END)
            Pentry2.delete(0,END)
            Aentry2.delete(0,END)
            Eentry2.delete(0,END)
            data2.set("Select a Gender")
            Dentry2.delete(0,END)


        
        upd = Button(editor,text="Update",command=updat)
        upd.grid(row=9,column=2,columnspan=2,pady=(20,0),ipadx=80,ipady=5)

    
        #commiting the changes done 
        connect.commit()
        #closing the database
        connect.close()



            





    Edits = Button(newscreen,text="Edit",command=update,bg="yellow",foreground="black")
    Edits.grid(row=1,column=1,ipadx=40,ipady=10)


showall = Button(screen,text="Show Data",command=show)
showall.grid(row=10,column=1,columnspan=2,pady=(20,0),ipadx=190,ipady=5)



#commiting the changes done 
connect.commit()
#closing the database
connect.close()
   

screen.mainloop()
