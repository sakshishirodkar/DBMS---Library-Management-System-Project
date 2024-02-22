#from dbm import _Database
from email.mime import message
from msilib import Table
from msilib.schema import ListBox 
from multiprocessing.sharedctypes import Value
#from ssl import _PasswordType
from tkinter import  *
import tkinter as ttk
from tkinter import ttk
from tkinter.ttk import Combobox
from webbrowser import get
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


class LibraryManagementSystem():
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1440x700+0+0")


        #==============================================variable=====================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowerd_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.actualprice_var=StringVar()





        lbltitle=Label(self.root,text="Library Management System",bg ='powder blue',fg="black",bd=20,relief=RIDGE,font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=110,width=1530,height=400)
        
        #==================================Data Frame Left===================================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg ='powder blue',fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=0,width=700,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember= Combobox(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.member_var,width=22,state="readonly")
        comMember["value"]=("Admin staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        
        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)

        txtPRN_No=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.prn_var,width=25)
        txtPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)

        txtTitle=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.id_var,width=25)
        txtTitle.grid(row=2,column=1)

        
        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)

        txtFirstName=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.firstname_var,width=25)
        txtFirstName.grid(row=3,column=1)


        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)

        txtLastName=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.lastname_var,width=25)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)

        txtAddress1=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.address1_var,width=25)
        txtAddress1.grid(row=5,column=1)


        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)

        txtAddress2=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.address2_var,width=25)
        txtAddress2.grid(row=6,column=1)

        lblPostcode=Label(DataFrameLeft,bg="powder blue",text="Post code:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblPostcode.grid(row=7,column=0,sticky=W)

        txtPostcode=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.postcode_var,width=25)
        txtPostcode.grid(row=7,column=1)


        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)

        txtMobile=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.mobile_var,width=25)
        txtMobile.grid(row=8,column=1)


        lblBookID=Label(DataFrameLeft,bg="powder blue",text="Book ID:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblBookID.grid(row=0,column=2,sticky=W)

        txtBookID=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.bookid_var,width=25)
        txtBookID.grid(row=0,column=3)


        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)

        txtBookTitle=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.booktitle_var,width=25)
        txtBookTitle.grid(row=1,column=3)

        lblAuthorName=Label(DataFrameLeft,bg="powder blue",text="Author Name:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblAuthorName.grid(row=2,column=2,sticky=W)

        txtAuthorName=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.author_var,width=25)
        txtAuthorName.grid(row=2,column=3)


        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)

        txtDateBorrowed=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.dateborrowerd_var,width=25)
        txtDateBorrowed.grid(row=3,column=3)

        lblDueDate=Label(DataFrameLeft,bg="powder blue",text="Due Date:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblDueDate.grid(row=4,column=2,sticky=W)

        txtDueDate=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.datedue_var,width=25)
        txtDueDate.grid(row=4,column=3)
        
        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days on Book:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)

        txtDaysOnBook=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.daysonbook_var,width=25)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("times of roman",10,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)

        txtLateReturnFine=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.latereturnfine_var,width=25)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("times of roman",10,"bold"))
        lblDateOverDue.grid(row=7,column=2,sticky=W)

        txtDateOverDue=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.dateoverdue_var,width=25)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("times of roman",10,"bold"))
        lblActualPrice.grid(row=8,column=2,sticky=W)

        txtActualPrice=Entry(DataFrameLeft,font=("times of roman",10,"bold"),textvariable=self.actualprice_var,width=25)
        txtActualPrice.grid(row=8,column=3)
        #==================================Data Frame Right===================================
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg ='powder blue',fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=710,y=0,width=600,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head first book','Learn python the easy way','Python programming','Machine tecno','Advance python','Machine python','CPP','Object oriented programming','HTML','CSS','Javascript','PHP','Ruby','Data structure','Operating system','Computer graphics','Java']
        
        def selectbook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head first book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python mannual")
                self.author_var.set("Paul Berry")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.788")

            elif (x=="Learn python the easy way"):
                self.bookid_var.set("BKID6485")
                self.booktitle_var.set("Python fundamentals")
                self.author_var.set("Emma Smith")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=16)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(16)
                self.latereturnfine_var.set("Rs.35")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.900")

            elif (x=="Python programming"):
                self.bookid_var.set("BKID2354")
                self.booktitle_var.set("Python World")
                self.author_var.set("Sam Kaif")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.1000")

            elif (x=="Machine tecno"):
                self.bookid_var.set("BKID3590")
                self.booktitle_var.set("Technology")
                self.author_var.set("Carry Maxwell")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.500")

            elif (x=="Advance python"):
                self.bookid_var.set("BKID6686")
                self.booktitle_var.set("Python Level II")
                self.author_var.set("Paul Watson")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.45")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.853")

            elif (x=="Machine python"):
                self.bookid_var.set("BKID3455")
                self.booktitle_var.set("Python")
                self.author_var.set("Harry Jenner")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.500")
            
            elif (x=="CPP"):
                self.bookid_var.set("BKID3754")
                self.booktitle_var.set("CPP fundamentals")
                self.author_var.set("Jonny Roy")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.700")

            elif (x=="Object oriented programming"):
                self.bookid_var.set("BKID5410")
                self.booktitle_var.set("OOP")
                self.author_var.set("Joe root")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.900")
            
            elif (x=="HTML"):
                self.bookid_var.set("BKID3777")
                self.booktitle_var.set("Web technology")
                self.author_var.set("Henry Warner")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.964")

            elif (x=="CSS"):
                self.bookid_var.set("BKID5400")
                self.booktitle_var.set("Web technology II")
                self.author_var.set("Henry Warner")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.35")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.1268")
            
            elif (x=="Javascript"):
                self.bookid_var.set("BKID1234")
                self.booktitle_var.set("Web technology III ")
                self.author_var.set("Henry Warner")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.1500")
            
            elif (x=="PHP"):
                self.bookid_var.set("BKID8888")
                self.booktitle_var.set("PHP Basics")
                self.author_var.set("Merry Rowlling")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.487")

            elif (x=="Ruby"):
                self.bookid_var.set("BKID4444")
                self.booktitle_var.set("Ruby basics")
                self.author_var.set("Jane Austen")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.48")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.555")

            elif (x=="Data structure"):
                self.bookid_var.set("BKID3333")
                self.booktitle_var.set("Fundamentals of data structures")
                self.author_var.set("George Woolf")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.529")

            elif (x=="Operating system"):
                self.bookid_var.set("BKID2625")
                self.booktitle_var.set("OS basics")
                self.author_var.set("Ruskin Milton")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.688")

            elif (x=="Computer graphics"):
                self.bookid_var.set("BKID9222")
                self.booktitle_var.set("Graphical World")
                self.author_var.set("Dan Brown")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.10")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.999")

            elif (x=="Java"):
                self.bookid_var.set("BKID7000")
                self.booktitle_var.set("Java")
                self.author_var.set("John Donney")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowerd_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.36")
                self.dateoverdue_var.set("No")
                self.actualprice_var.set("Rs.1777")



        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=25,height=16)
        listBox.bind("<<ListboxSelect>>",selectbook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=Listbox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        #==================================Buttons Frame ===================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=500,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.show_data,text="Show Data",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
        #==================================Information Frame ===================================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=570,width=1530,height=195)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1320,height=175)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","Lastname","Address1","Address2","PostID","Mobile","BookID","BookTitle","Author","Dateborrowed","Datedue","Days","lastreturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("Lastname",text="Last Name")
        self.library_table.heading("Address1",text="Address1")
        self.library_table.heading("Address2",text="Address2")
        self.library_table.heading("PostID",text="Post ID")
        self.library_table.heading("Mobile",text="Mobile")
        self.library_table.heading("BookID",text="Book ID")
        self.library_table.heading("BookTitle",text="Book Title")
        self.library_table.heading("Author",text="Author")
        self.library_table.heading("Dateborrowed",text="Date Borrowed")
        self.library_table.heading("Datedue",text="Date Due")
        self.library_table.heading("Days",text="Days")
        self.library_table.heading("lastreturnfine",text="Last Return Fine")
        self.library_table.heading("dateoverdue",text="Date over due")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("Lastname",width=100)
        self.library_table.column("Address1",width=100)
        self.library_table.column("Address2",width=100)
        self.library_table.column("PostID",width=100)
        self.library_table.column("Mobile",width=100)
        self.library_table.column("BookID",width=100)
        self.library_table.column("BookTitle",width=100)
        self.library_table.column("Author",width=100)
        self.library_table.column("Dateborrowed",width=100)
        self.library_table.column("Datedue",width=100)
        self.library_table.column("Days",width=100)
        self.library_table.column("lastreturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)


        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    
    def add_data(self):
        myconn=mysql.connector.connect(host= "localhost",user= "root",passwd= "Admin@123",database= "library1")
        my_cursor=myconn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.member_var.get(),
                                                                                    self.prn_var.get(),
                                                                                    self.id_var.get(),
                                                                                    self.firstname_var.get(),
                                                                                    self.lastname_var.get(),
                                                                                    self.address1_var.get(),
                                                                                    self.address2_var.get(),
                                                                                    self.postcode_var.get(),
                                                                                    self.mobile_var.get(),
                                                                                    self.bookid_var.get(),
                                                                                    self.booktitle_var.get(),
                                                                                    self.author_var.get(),
                                                                                    self.dateborrowerd_var.get(),
                                                                                    self.datedue_var.get(),
                                                                                    self.daysonbook_var.get(),
                                                                                    self.latereturnfine_var.get(),
                                                                                    self.dateoverdue_var.get(),
                                                                                    self.actualprice_var.get()
        ))
        
        myconn.commit()
        self.fatch_data()
        myconn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

    def update(self):
        myconn=mysql.connector.connect(host= "localhost",user= "root",passwd= "Admin@123",database= "library1")
        my_cursor=myconn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s ,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostID=%s,Mobile=%s,BookID=%s,BookTitle=%s,Author=%s,Dateborrowed=%s,DueDate=%s,Daysonbook=%s,Latereturnfine=%s,Dateoverdue=%s,Actualprice=%s  where PRN_NO=%s",(
                                                                                    self.member_var.get(),
                                                                                    self.id_var.get(),
                                                                                    self.firstname_var.get(),
                                                                                    self.lastname_var.get(),
                                                                                    self.address1_var.get(),
                                                                                    self.address2_var.get(),
                                                                                    self.postcode_var.get(),
                                                                                    self.mobile_var.get(),
                                                                                    self.bookid_var.get(),
                                                                                    self.booktitle_var.get(),
                                                                                    self.author_var.get(),
                                                                                    self.dateborrowerd_var.get(),
                                                                                    self.datedue_var.get(),
                                                                                    self.daysonbook_var.get(),
                                                                                    self.latereturnfine_var.get(),
                                                                                    self.dateoverdue_var.get(),
                                                                                    self.actualprice_var.get(),
                                                                                    self.prn_var.get(),
        ))

        myconn.commit()
        self.fatch_data()
        self.reset()
        myconn.close()

        messagebox.showinfo("Success","Member has been updated successfully")

        
    def fatch_data(self):
        myconn=mysql.connector.Connect(host= "localhost",user= "root", passwd="Admin@123", database="library1")
        my_cursor=myconn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            myconn.commit()
        myconn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowerd_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.actualprice_var.set(row[17])

    def show_data(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No\t\t"+self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No\t\t"+self.id_var.get() + "\n")
        self.txtBox.insert(END,"First Name\t\t"+self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name\t\t"+self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post code\t\t"+self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile\t\t"+self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID\t\t"+self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author\t\t"+self.author_var.get() + "\n")
        self.txtBox.insert(END,"Date Borrowed\t\t"+self.dateborrowerd_var.get() + "\n")
        self.txtBox.insert(END,"Due Date\t\t"+self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"Days on book\t\t"+self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"Late return fine\t\t"+self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"Date over due\t\t"+self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"Actual Price\t\t"+self.actualprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowerd_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.actualprice_var.set(""),

    
    def iExit(self):
        iExit= tkinter.messagebox.askyesno("Library management system","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return 

    
    def delete(self):
        if self.prn_var.get()==" " or self.id_var.get()==" ":
            messagebox.showerror("Error","First select the member")
        else:
            myconn=mysql.connector.connect(host="localhost",user="root",passwd="Admin@123",database="library1")
            my_cursor=myconn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            myconn.commit()
            self.fatch_data()
            self.reset()
            myconn.close()

            messagebox.showinfo("Success","Member has been deleted successfully")







                                                                                    

if __name__=='__main__':
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()