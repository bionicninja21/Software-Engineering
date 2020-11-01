from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("CashItOut setup file")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
lab1=Label(root,text='Welcome to the CashItOut setup file',font='Times 30').pack()

def admin():
    conn=sqlite3.connect('admin.db')                                          #Connects to the database
    print("Opened Admin Database")

    adm=conn.cursor()                                                         #Creates a cursor

    #Creating Login table
    adm.execute("""CREATE TABLE login                                         
                    (username text,
                    password text)""")

    adm.execute("INSERT INTO login VALUES ('ROHIT','bionicninja21')")
    adm.execute("INSERT INTO login VALUES ('AMRIT','tronix309')")
    adm.execute("INSERT INTO login VALUES ('SANJANA','doggo2$')")       

    print("Admin Login Table created")

    #Creating Admin Log table
    adm.execute("""CREATE TABLE log 
                    (username text,
                    access text )""")

    print("Admin Log table created")

    conn.commit()                                                           #commits the changes
    conn.close()                                                            #closes the database


def gadgets():
    conne = sqlite3.connect('gadgets.db')  # Connects to the database
    print("Opened Gadgets Database")

    gad = conne.cursor()                                                       # Creates a cursor

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

    print ("Customer Login table created")

    #Creating Customer details table
    cust.execute("""CREATE TABLE details
                        (username text,
                        name text,
                        emailid text,
                        mobile text,
                        address text,
                        zipcode integer)
                        """)

    print("Customer Details table created")


def setup():
    print ("Welcome to CashItOut Setup File")

    if res==True:
        admin()
        lab2=Label(root,text='Admin database created successfully',font='Times 20').pack()
        print("Admin Database Created")
        gadgets()
        lab3=Label(root,text='Gadgets database created successfully',font='Times 20').pack()
        print("Gadget Database Created")
        customer()
        lab4=Label(root,text='Customer database created successfully',font='Times 20').pack()
        print("Customer Database Created")
        messagebox.showinfo('Database Creation', 'Process Successfull')
res = messagebox.askyesno('CashItOut database creation','Do you wish to continue?')
setup()

root.mainloop()
