from operator import add
from tkinter import *
import time
from tkinter import ttk

import ttkthemes
from tkinter import ttk,messagebox
import pymysql

#fuctionality part

def add_student():
    def add_data():
        if idEntry.get()=="" or nameEntry.get()=="" or phoneEntry.get()=="" or emailEntry.get()=="" or addressEntry.get()=="" or genderEntry.get()=="" or dobEntry.get()=="" or dobEntry.get()=="":
            messagebox.showerror('Error','ALL Feilds are required',parent=add_window)

        else:
            currentdate = time.strftime("%d/%m/%Y")
            currenttime = time.strftime("%H:%M:%S")
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),currentdate,currenttime))
            con.commit()
            result= messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=add_window)
            print(result)
            if result:
                idEntry.delete(0,'end')
                nameEntry.delete(0, 'end')
                phoneEntry.delete(0, 'end')
                emailEntry.delete(0, 'end')
                addressEntry.delete(0, 'end')
                genderEntry.delete(0, 'end')
                dobEntry.delete(0, 'end')
            else:
                pass


    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)
    idLabel=Label(add_window,text='ID',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15)
    idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(add_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(add_window, text='DOB', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    add_student_button=ttk.Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7, columnspan=2,pady=15)

def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='Asha@8141')
            mycursor=con.cursor()

        except:
            messagebox.showerror("Error","Invalid Details",parent=connectWindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query=('create table student(id int not null primary key, name varchar(30), mobile varchar(10),'
                   'email varchar(30),address varchar(100), gender varchar(20), dob varchar(20),date varchar(50), time varchar(50))')
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo("Success", "Database Connection is Successful", parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLable=Label(connectWindow,text='Host Name', font=('arial',20,'bold'))
    hostnameLable.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,pady=20,padx=40)

    usernameLable = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLable.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, pady=20, padx=40)

    passwordLable = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLable.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, pady=20, padx=40)

    connectButton = ttk.Button(connectWindow, text='CONNECT',command=connect)
    connectButton.grid(row=3, columnspan=2)


count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)

def clock():
    date=time.strftime("%d/%m/%Y")
    currenttime=time.strftime("%H:%M:%S")
    datetimeLabel.config(text=f'    Date:{date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)


#GUI part

root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0, 0)
root.title('Student Management System')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'  #s[count]=t when count is 1
sliderLabel=Label(root,text=s,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student.png')
logo_label = Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Student',width=25,state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,state=DISABLED)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','DOB','Added Date'
                                                  ,'Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('DOB',text='DOB')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.config(show='headings')

root.mainloop()