from tkinter import *
from tkinter import messagebox
import sqlite3
import smtplib
import datetime
import random
import math

def customer_login():
    def newlogin():
        newlog=Tk()
        newlog.geometry('350x250')
        newlog.title("New User")


        label1 = Label(newlog, text="Username", font='Times 15').grid(row=1)
        label2 = Label(newlog, text="Email ID", font='Times 15').grid(row=3)
        label3 = Label(newlog, text="Password", font='Times 15').grid(row=5)
        label4 = Label(newlog, text="Name", font='Times 15').grid(row=7)
        label5 = Label(newlog, text="Mobile", font='Times 15').grid(row=9)
        label6 = Label(newlog, text="Address", font='Times 15').grid(row=11)
        label7 = Label(newlog, text="Zip Code", font='Times 15').grid(row=13)

        entry1 = Entry(newlog, font='Times 15')
        entry2 = Entry(newlog, font='Times 15')
        entry3 = Entry(newlog, font='Times 15')
        entry4 = Entry(newlog, font='Times 15')
        entry5 = Entry(newlog, font='Times 15')
        entry6 = Entry(newlog, font='Times 15')
        entry7 = Entry(newlog, font='Times 15')

        entry1.grid(row=1, column=3)
        entry2.grid(row=3, column=3)
        entry3.grid(row=5, column=3)
        entry4.grid(row=7, column=3)
        entry5.grid(row=9, column=3)
        entry6.grid(row=11, column=3)
        entry7.grid(row=13, column=3)

        def createuser():
            cust_name = entry4.get()
            cust_username = entry1.get()
            cust_pwd = entry3.get()
            cust_add = entry6.get()
            cust_mob = entry5.get()
            cust_id = entry2.get()
            cust_zip = entry7.get()

            conn = sqlite3.connect('customer.db')
            adm = conn.cursor()
            adm.execute('INSERT into details VALUES(?,?,?,?,?,?)', (cust_username,cust_name,cust_id,cust_mob,cust_add,cust_zip))
            adm.execute('INSERT into login VALUES (?,?)',(cust_username,cust_pwd))
            conn.commit()
            conn.close()
            newlog.destroy()
            messagebox.showinfo('User Created', 'Congratulations! Please log in with your credentials')

        c=Button(newlog, text="Create Account", font='Times 15', command=createuser).grid(row=16,columnspan=5)

        newlog.grid_rowconfigure(15,minsize=10)
        newlog.mainloop()

    def recover():
        rec=Tk()
        rec.title("Password Recovery")

        label1 = Label(rec, text="Username", font='Times 15')
        label2 = Label(rec, text="Email ID", font='Times 15')

        entry1 = Entry(rec, font='Times 15')
        entry2 = Entry(rec, font='Times 15')

        label1.grid(row=1)
        label2.grid(row=3)

        entry1.grid(row=1, column=3)
        entry2.grid(row=3, column=3)
        rec.grid_rowconfigure(2, minsize=5)
        rec.grid_rowconfigure(4, minsize=20)

        def mail():
            username = entry1.get()
            email=entry2.get()
            conn = sqlite3.connect('customer.db')
            cust = conn.cursor()
            cust.execute('SELECT * from login')
            info = cust.fetchall()
            user = False
            creds = False
            for uname in info:
                if creds != True:
                    if uname[0] == username:
                        user = True
                        password=uname[1]
                    else:
                        messagebox.showerror('Error', 'Username not found')


            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()

            s.login("cashitouthelp@gmail.com", "payussanjana")

            subject = 'Password Recovery for your CashItOut account'
            body = 'Dear User,\n Your request for password recovery has been acknowledged.\n Your account password is:\n' + password + '\n\nPlease take care of your account credentials next time.\nThank you\nRegards,\nCashItOut Team'
            msg = 'Subject:{}\n\n{}'.format(subject, body)

            s.sendmail("cashitouthelp@gmail.com", email, msg)

            s.quit()
            rec.destroy()
            messagebox.showinfo('Password Recovery', 'Please check your email for your password')

        button2 = Button(rec, text="Send Mail", font='Times 15', command=mail)
        button2.grid(row=6, columnspan=10)

        rec.grid_rowconfigure(7,minsize=20)
        rec.grid_rowconfigure(0,minsize=20)

    def oldlogin():
        custlog.destroy()
        oldlog=Tk()
        oldlog.title("Customer Login")
        def checkcreds_user():
            username = entry1.get()
            password = entry2.get()

            conn = sqlite3.connect('customer.db')
            cust = conn.cursor()
            cust.execute('SELECT * from login')
            info = cust.fetchall()
            user = False
            creds = False
            for uname in info:
                if creds != True:
                    if uname[0] == username:
                        user = True
                        if uname[1] == password:
                            creds = True
                            print("Login Success")
                            hellouser = "Hello " + username
                            messagebox.showinfo('Login Successful', hellouser)
                            closewindow()
                            #adlog.destroy()
                            #customermenu(username)
                        else:
                            print("WRONG PASSWORD,try again")
                            messagebox.showerror('Login Failed', 'Wrong Password')
                            entry2.delete(0, END)
                    else:
                        creds = False
            if user == False:
                messagebox.showerror('Login Failed', 'Username not found')
                entry1.delete(0, END)
                entry2.delete(0, END)

            conn.commit()
            conn.close()

        label1 = Label(oldlog, text="Name", font='Times 15')
        label2 = Label(oldlog, text="Password", font='Times 15')

        entry1 = Entry(oldlog, font='Times 15')
        entry2 = Entry(oldlog, show='*', font='Times 15')

        label1.grid(row=1)
        label2.grid(row=3)

        entry1.grid(row=1, column=3)
        entry2.grid(row=3, column=3)
        oldlog.grid_rowconfigure(2, minsize=5)
        oldlog.grid_rowconfigure(4, minsize=20)

        button2 = Button(oldlog, text="Forgot Password", font='Times 10',command=recover)
        button2.grid(row=6, columnspan=10)
        button1 = Button(oldlog, text="Login", font='Times 15',command=checkcreds_user)
        button1.grid(row=8, columnspan=10)
        oldlog.grid_columnconfigure(5,minsize=10)
        oldlog.grid_rowconfigure(7,minsize=5)
        oldlog.grid_rowconfigure(9,minsize=20)
        oldlog.grid_rowconfigure(0,minsize=20)

        oldlog.mainloop()

    custlog=Tk()
    custlog.title("Customer Login")


    new=Button(custlog,text="NEW USER",font="Times 15",command=newlogin)
    new.grid(row=1,column=2,columnspan=5)

    old=Button(custlog,text="EXISTING USER",font="Times 15",command=oldlogin)
    old.grid(row=3,column=2,columnspan=5)

    custlog.grid_columnconfigure(1,minsize=10)
    custlog.grid_columnconfigure(8,minsize=10)
    custlog.grid_rowconfigure(0,minsize=20)
    custlog.grid_rowconfigure(2, minsize=20)
    custlog.grid_rowconfigure(4,minsize=40)

    custlog.mainloop()
def admin_login():
    adlog = Tk()
    adlog.title("Admin Login")

    def addlog(username,now):
        conn = sqlite3.connect('admin.db')
        adm = conn.cursor()
        adm.execute('INSERT into log VALUES(?,?)',(username,str(now)))
        conn.commit()
        conn.close()


    def checkcreds_admin():
        username = entry1.get()
        password = entry2.get()

        conn = sqlite3.connect('admin.db')
        adm = conn.cursor()
        adm.execute('SELECT * from login')
        info = adm.fetchall()
        user=False
        creds = False
        for uname in info:
            if creds != True:
                if uname[0] == username:
                    user=True
                    if uname[1] == password:
                        creds = True
                        print("Login Success")
                        helloadmin="Hello "+username
                        messagebox.showinfo('Login Successful',helloadmin)
                        now = datetime.datetime.now()
                        adlog.destroy()
                        addlog(username,now)
                        adminmenu(username)
                    else:
                        print("WRONG PASSWORD,try again")
                        messagebox.showerror('Login Failed','Wrong Password')
                        entry2.delete(0,END)
                else:
                    creds = False
        if user==False:
            messagebox.showerror('Login Failed', 'Username not found')
            entry1.delete(0,END)
            entry2.delete(0,END)

        conn.commit()
        conn.close()

    label1 = Label(adlog, text="Name", font='Times 15')
    label2 = Label(adlog, text="Password", font='Times 15')

    entry1 = Entry(adlog, font='Times 15')
    entry2 = Entry(adlog, show='*', font='Times 15')

    label1.grid(row=0)
    label2.grid(row=3)

    entry1.grid(row=0, column=3)
    entry2.grid(row=3, column=3)
    adlog.grid_rowconfigure(2, minsize=5)
    adlog.grid_rowconfigure(4, minsize=20)

    button1 = Button(adlog, text="Login", font='Times 15', command=checkcreds_admin)
    button1.grid(row=6, columnspan=10)


    adlog.mainloop()

def printphone():
    printl = Tk()
    printl.title("Mobile Database")
    printl.geometry("400x600")

    lab1 = Label(printl, text='CashItOut', font='Times 50').grid(row=0, column=3, columnspan=2)

    conn = sqlite3.connect('gadgets.db')
    adm = conn.cursor()

    adm.execute('SELECT * from mobile')
    logdetails = adm.fetchall()
    access = ''
    count=1
    for i in logdetails:
        combine = ''
        combine = str(count)+'.'+i[0] + ' ' + i[1] + '\n'
        access = access + combine
        count+=1

    lab2 = Label(printl, text=access, font='Times 10').grid(row=2, column=3,columnspan=4)

def printlaptop():
    printl = Tk()
    printl.title("Laptop Database")
    printl.geometry("400x600")

    lab1 = Label(printl, text='CashItOut', font='Times 50').grid(row=0, column=3, columnspan=2)

    conn = sqlite3.connect('gadgets.db')
    adm = conn.cursor()

    adm.execute('SELECT * from laptop')
    logdetails = adm.fetchall()
    count = 1
    access = ''
    for i in logdetails:
        combine = ''
        combine = str(count) + '.' + i[0] + ' ' + i[1] + '\n'
        access = access + combine
        count+=1

    lab2 = Label(printl, text=access, font='Times 10').grid(row=2, column=3, columnspan=4)


def printcamera():
    printl = Tk()
    printl.title("Camera Database")
    printl.geometry("400x600")

    lab1 = Label(printl, text='CashItOut', font='Times 50').grid(row=0, column=3, columnspan=2)

    conn = sqlite3.connect('gadgets.db')
    adm = conn.cursor()

    adm.execute('SELECT * from camera')
    logdetails = adm.fetchall()
    count=1
    access = ''
    for i in logdetails:
        combine = ''
        combine = str(count)+'.'+i[0] + ' ' + i[1] + '\n'
        access = access + combine
        count+=1

    lab2 = Label(printl, text=access, font='Times 10').grid(row=2, column=3,columnspan=4)


def adminmenu(username):
    def closewindow1():
        admenu.destroy()

    def checklog():
        closewindow1()
        printlog=Tk()
        printlog.title("Admin Log")
        printlog.geometry("400x600")

        lab1 = Label(printlog, text='CashItOut', font='Times 50').grid(row=0, column=3, columnspan=2)

        conn = sqlite3.connect('admin.db')
        adm=conn.cursor()

        adm.execute('SELECT * from log')
        logdetails=adm.fetchall()
        access=''
        for i in logdetails:
            combine=''
            combine=i[0]+':'+i[1]+'\n'
            access=access+combine

        lab2=Label(printlog,text=access,font='Times 10').grid(row=2,column=3)

    def viewdatabase():
        closewindow1()
        view=Tk()
        view.title("CashItOut")
        view.geometry("400x600")

        lab1 = Label(view, text='CashItOut', font='Times 50').grid(row=0, column=3, columnspan=2)

        button4 = Button(view, text="MOBILE", font='Times 15',command=printphone)
        button4.grid(row=3, column=4, columnspan=3)
        button1 = Button(view, text="LAPTOP", font='Times 15',command=printlaptop)
        button1.grid(row=5, column=4, columnspan=3)
        button2 = Button(view, text="CAMERA", font='Times 15',command=printcamera)
        button2.grid(row=7, column=4, columnspan=3)

        view.grid_columnconfigure(1, minsize=10)
        view.grid_rowconfigure(2, minsize=250)
        view.grid_rowconfigure(5, minsize=20)
        view.grid_rowconfigure(4, minsize=20)
        view.grid_rowconfigure(6, minsize=20)

        view.mainloop()

    def adddb():
        closewindow1()
        view = Tk()
        view.title("CashItOut")
        view.geometry("400x600")

        lab1 = Label(view, text='CashItOut', font='Times 50').grid(row=0, column=3, columnspan=2)

        def addphone():
            newlog = Tk()
            newlog.geometry('350x250')
            newlog.title("New Mobile")

            label1 = Label(newlog, text="Brand", font='Times 15').grid(row=1)
            label2 = Label(newlog, text="Model", font='Times 15').grid(row=3)
            label3 = Label(newlog, text="Price", font='Times 15').grid(row=5)

            entry1 = Entry(newlog, font='Times 15')
            entry2 = Entry(newlog, font='Times 15')
            entry3 = Entry(newlog, font='Times 15')

            entry1.grid(row=1, column=3)
            entry2.grid(row=3, column=3)
            entry3.grid(row=5, column=3)

            def add():
                b=entry1.get()
                m=entry2.get()
                p=entry3.get()
                pr=int(p)

                conn = sqlite3.connect('gadgets.db')
                adm = conn.cursor()
                adm.execute('INSERT into mobile VALUES(?,?,?)',(b.m.pr))
                conn.commit()
                conn.close()

                messagebox.showinfo('Gadget Added', 'New Mobile has been added')
            bu=Button(newlog,text="ADD",font='Times 15',command=add).grid(row=7)


        def addlaptop():
            newlog = Tk()
            newlog.geometry('350x250')
            newlog.title("New Laptop")

            label1 = Label(newlog, text="Brand", font='Times 15').grid(row=1)
            label2 = Label(newlog, text="Model", font='Times 15').grid(row=3)
            label3 = Label(newlog, text="Price", font='Times 15').grid(row=5)

            entry1 = Entry(newlog, font='Times 15')
            entry2 = Entry(newlog, font='Times 15')
            entry3 = Entry(newlog, font='Times 15')

            entry1.grid(row=1, column=3)
            entry2.grid(row=3, column=3)
            entry3.grid(row=5, column=3)

            def add():
                b=entry1.get()
                m=entry2.get()
                p=entry3.get()
                pr=int(p)

                conn = sqlite3.connect('gadgets.db')
                adm = conn.cursor()
                adm.execute('INSERT into laptop VALUES(?,?,?)',(b.m.pr))
                conn.commit()
                conn.close()

                messagebox.showinfo('Gadget Added', 'New Laptop has been added')
            bu=Button(newlog,text="ADD",font='Times 15',command=add).grid(row=7)


        def addcamera():
            newlog = Tk()
            newlog.geometry('350x250')
            newlog.title("New Camera")

            label1 = Label(newlog, text="Brand", font='Times 15').grid(row=1)
            label2 = Label(newlog, text="Model", font='Times 15').grid(row=3)
            label3 = Label(newlog, text="Price", font='Times 15').grid(row=5)

            entry1 = Entry(newlog, font='Times 15')
            entry2 = Entry(newlog, font='Times 15')
            entry3 = Entry(newlog, font='Times 15')

            entry1.grid(row=1, column=3)
            entry2.grid(row=3, column=3)
            entry3.grid(row=5, column=3)

            def add():
                b=entry1.get()
                m=entry2.get()
                p=entry3.get()
                pr=int(p)

                conn = sqlite3.connect('gadgets.db')
                adm = conn.cursor()
                adm.execute('INSERT into camera VALUES(?,?,?)',(b.m.pr))
                conn.commit()
                conn.close()

                messagebox.showinfo('Gadget Added', 'New Camera has been added')
            bu=Button(newlog,text="ADD",font='Times 15',command=add).grid(row=7)


        button4 = Button(view, text="PHONE", font='Times 15', command=addphone)
        button4.grid(row=3, column=4, columnspan=3)
        button1 = Button(view, text="LAPTOP", font='Times 15', command=addlaptop)
        button1.grid(row=5, column=4, columnspan=3)
        button2 = Button(view, text="CAMERA", font='Times 15', command=addcamera)
        button2.grid(row=7, column=4, columnspan=3)

        view.grid_columnconfigure(1, minsize=10)
        view.grid_rowconfigure(2, minsize=250)
        view.grid_rowconfigure(5, minsize=20)
        view.grid_rowconfigure(4, minsize=20)
        view.grid_rowconfigure(6, minsize=20)

        view.mainloop()

    root.destroy()
    admenu=Tk()
    admenu.title("CashItOut : Admin")
    admenu.geometry("400x600")
    lab1 = Label(admenu, text='CashItOut', font='Times 50').grid(row=0,column=3,columnspan=2)

    lab2 = Label(admenu,text='Logged in as : '+username,font='Times 10').grid(row=2,column=4)

    viewdb=Button(admenu,text="VIEW DATABASE",font="Times 15",command=viewdatabase)
    viewdb.grid(row=4,column=4,columnspan=3)


    ydb = Button(admenu, text="ADD GADGET", font="Times 15",command=adddb)
    ydb.grid(row=6, column=4, columnspan=3)

    log=Button(admenu,text="ADMIN LOG",font="Times 15",command=checklog)
    log.grid(row=8,column=4,columnspan=3)

    logout=Button(admenu,text="EXIT",font="Times 15",command=closewindow1)
    logout.grid(row=10,column=4,columnspan=3)

    admenu.grid_rowconfigure(3, minsize=100)
    admenu.grid_rowconfigure(5, minsize=20)
    admenu.grid_rowconfigure(7,minsize=20)
    admenu.grid_rowconfigure(9, minsize=20)
    admenu.grid_rowconfigure(11, minsize=20)

    admenu.mainloop()


def closewindow():
    root.destroy()

def setupfile():
    def admin():
        conn = sqlite3.connect('admin.db')  # Connects to the database
        print("Opened Admin Database")

        adm = conn.cursor()  # Creates a cursor

        # Creating Login table
        adm.execute("""CREATE TABLE login                                         
                        (username text,
                        password text)""")

        adm.execute("INSERT INTO login VALUES ('ROHIT','bionicninja21')")
        adm.execute("INSERT INTO login VALUES ('AMRIT','tronix309')")
        adm.execute("INSERT INTO login VALUES ('SANJANA','doggo2$')")

        print("Admin Login Table created")

        # Creating Admin Log table
        adm.execute("""CREATE TABLE log 
                        (username text,
                        access text )""")

        print("Admin Log table created")

        conn.commit()  # commits the changes
        conn.close()  # closes the database

    def gadgets():
        conne = sqlite3.connect('gadgets.db')  # Connects to the database
        print("Opened Gadgets Database")

        gad = conne.cursor()  # Creates a cursor

        # Creating Laptop table
        gad.execute("""CREATE TABLE laptop                                         
                        (brand text,
                        model text,
                        price integer)""")

        gad.execute("INSERT INTO laptop VALUES ('Apple','Macbook Air 128GB',54999)")
        gad.execute("INSERT INTO laptop VALUES ('Apple','Macbook Air 256GB',61299)")
        gad.execute("INSERT INTO laptop VALUES ('Apple','Macbook Pro 128GB',81441)")
        gad.execute("INSERT INTO laptop VALUES ('Apple','Macbook Pro 256GB',91100)")
        gad.execute("INSERT INTO laptop VALUES ('HP','Pavilion 11-S002TU',13204)")
        gad.execute("INSERT INTO laptop VALUES ('HP','15-BU004TU',21990)")
        gad.execute("INSERT INTO laptop VALUES ('HP','15Q-DS0009TU',39990)")
        gad.execute("INSERT INTO laptop VALUES ('HP','Pavilion x360(11-AD 105TU)',28166)")
        gad.execute("INSERT INTO laptop VALUES ('DELL','Inspiron 15 3352',13990)")
        gad.execute("INSERT INTO laptop VALUES ('DELL','Latitude 3180',13056)")
        gad.execute("INSERT INTO laptop VALUES ('HP','Inspiron 15 5567',21105)")
        gad.execute("INSERT INTO laptop VALUES ('HP','3467 Notebook',18990)")

        print("Laptop table created")

        conne.commit()
        # Creating Camera table
        gad.execute("""CREATE TABLE camera                                         
                        (brand text,
                        model text,
                        price integer)""")

        gad.execute("INSERT INTO camera VALUES ('SONY','Alpha ',29471)")
        gad.execute("INSERT INTO camera VALUES ('SONY','Alpha A3000K',35403)")
        gad.execute("INSERT INTO camera VALUES ('SONY','NEX-3K',42009)")
        gad.execute("INSERT INTO camera VALUES ('SONY','Alpha A6000Y ILCE-6000Y',48455)")
        gad.execute("INSERT INTO camera VALUES ('Canon','IXUS 285 HS',7495)")
        gad.execute("INSERT INTO camera VALUES ('Canon','EOS 1200D',13900)")
        gad.execute("INSERT INTO camera VALUES ('Canon','EOS 750D',36780)")
        gad.execute("INSERT INTO camera VALUES ('Canon','PowerShot G3X',41195)")
        gad.execute("INSERT INTO camera VALUES ('Nikon','Coolpix B700',17999)")
        gad.execute("INSERT INTO camera VALUES ('Nikon','D3300',15999)")
        gad.execute("INSERT INTO camera VALUES ('Nikon','D5600 DSLR',31876)")
        gad.execute("INSERT INTO camera VALUES ('Nikon','D5200',32255)")

        print("camera table created")

        # Creating Mobile table
        gad.execute("""CREATE TABLE mobile                                         
                        (brand text,
                        model text,
                        price integer)""")

        gad.execute("INSERT INTO mobile VALUES ('Apple','iPhone 5',17129)")
        gad.execute("INSERT INTO mobile VALUES ('Apple','iPhone 5S',18449)")
        gad.execute("INSERT INTO mobile VALUES ('Apple','iPhone 6',29999)")
        gad.execute("INSERT INTO mobile VALUES ('Apple','iPhone 7',31300)")
        gad.execute("INSERT INTO mobile VALUES ('Apple','iPhone SE',18561)")
        gad.execute("INSERT INTO mobile VALUES ('Samsung','Galaxy J8',13990)")
        gad.execute("INSERT INTO mobile VALUES ('Samsung','Galaxy J6',9899)")
        gad.execute("INSERT INTO mobile VALUES ('Samsung','Galaxy A6',11490)")
        gad.execute("INSERT INTO mobile VALUES ('Samsung','Galaxy S6',17655)")
        gad.execute("INSERT INTO mobile VALUES ('Samsung','Galaxy Note 5',29999)")
        gad.execute("INSERT INTO mobile VALUES ('HTC','Desire 826',5500)")
        gad.execute("INSERT INTO mobile VALUES ('HTC','Desire 12',10990)")
        gad.execute("INSERT INTO mobile VALUES ('HTC','One M8',11999)")
        gad.execute("INSERT INTO mobile VALUES ('HTC','One X9',12770)")
        gad.execute("INSERT INTO mobile VALUES ('HTC','U11',32999)")
        gad.execute("INSERT INTO mobile VALUES ('OnePlus','OnePlus One',9999)")
        gad.execute("INSERT INTO mobile VALUES ('OnePlus','OnePlus 2',10999)")
        gad.execute("INSERT INTO mobile VALUES ('OnePlus','OnePlus X',12999)")
        gad.execute("INSERT INTO mobile VALUES ('OnePlus','OnePlus 3',14999)")
        gad.execute("INSERT INTO mobile VALUES ('OnePlus','OnePlus 3T',21699)")
        gad.execute("INSERT INTO mobile VALUES ('OnePlus','OnePlus 5T',26999)")
        gad.execute("INSERT INTO mobile VALUES ('OnePlus','OnePlus 5',27900)")
        gad.execute("INSERT INTO mobile VALUES ('Motorola','Moto Z',16990)")
        gad.execute("INSERT INTO mobile VALUES ('Motorola','Nexus 6',14999)")
        gad.execute("INSERT INTO mobile VALUES ('Motorola','Moto E5',7490)")
        gad.execute("INSERT INTO mobile VALUES ('Motorola','Moto C',4711)")
        gad.execute("INSERT INTO mobile VALUES ('Motorola','Moto X4',12475)")
        gad.execute("INSERT INTO mobile VALUES ('Motorola','Moto G6',10899)")

        print("Mobile table created")

        conne.commit()
        conne.close()

    def customer():
        connc = sqlite3.connect('customer.db')
        print("Opened Customer Database")

        cust = connc.cursor()

        # Creating Customer login table
        cust.execute("""CREATE TABLE login                                         
                            (username text,
                            password text)""")

        print("Customer Login table created")

        # Creating Customer details table
        cust.execute("""CREATE TABLE details
                            (username text,
                            name text,
                            emailid text,
                            mobile text,
                            address text,
                            zipcode integer)
                            """)

        cust.execute("""CREATE TABLE order_phone
                                (username text,
                                order_id integer,gadget text,address text,date text,slot text,price integer,display text,screen text,camera text,button text,speaker text,charging text,wifi text,charger text,earphones text,box text,bill text,age text,overall text)
                                """)

        cust.execute("""CREATE TABLE order_laptop
                                (username text,
                                order_id integer,gadget text,address text,date text,slot text,price integer,display text,keyboard text,cd_drive text,touchpad text,charging text,speakers text,wifi text,charger text,bill text,age text,overall text)
                                """)

        cust.execute("""CREATE TABLE order_camera
                                (username text,
                                order_id integer,gadget text,address text,date text,slot text,price integer,display text,scratch text,focus text,aperture_exposure text,charging text,speaker text,buttons text,flash text,charger text,bill text,age text,overall text)
                                """)

        print("Customer Details table created")

    def setup():
        print("Welcome to CashItOut Setup File")

        if res == True:
            admin()
            print("Admin Database Created")
            gadgets()
            print("Gadget Database Created")
            customer()
            print("Customer Database Created")
            messagebox.showinfo('Database Creation', 'Process Successfull')

    res = messagebox.askyesno('CashItOut database creation', 'Do you wish to continue?')
    setup()



root=Tk()
root.title("CashItOut")
root.geometry("400x600")
lab1=Label(root,text='CashItOut',font='Times 50').grid(row=0,column=3,columnspan=2)

button4=Button(root,text="SETUP",font='Times 15',command=setupfile)
button4.grid(row=3,column=4,columnspan=3 )
button1=Button(root,text="ADMIN LOGIN",font='Times 15',command=admin_login)
button1.grid(row=5,column=4,columnspan=3 )
button2=Button(root,text="CUSTOMER LOGIN",font='Times 15',command=customer_login)
button2.grid(row=7,column=4,columnspan=3)
button3=Button(root,text="EXIT",font='Times 15',command=closewindow)
button3.grid(row=9,column=4,columnspan=3)

root.grid_columnconfigure(1,minsize=10)
root.grid_rowconfigure(2,minsize=250)
root.grid_rowconfigure(5,minsize=20)
root.grid_rowconfigure(4,minsize=20)
root.grid_rowconfigure(6,minsize=20)
root.grid_rowconfigure(8,minsize=20)


root.mainloop()