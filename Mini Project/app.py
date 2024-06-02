from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import time
#file imports
import pdfGenerator
import backend
import getMenu
import quote
import graph

 #----------------------------TOP BAR---------------------------#
time1 = ''
class heading:
    
    def __init__(self, root):
        self.root = root    

        headFrame = Frame(self.root,bg="")
        headLabel = Label(headFrame, text="Mukikumuki RESTAURENT", font=("Times New Roman", 28, "bold"), foreground="white" )
        headLabel.config(bg="black")
        headLabel.pack(pady=(10,0))
        dateLabel = Label(headFrame, text="--Dynamic date will be printed here--" , bg="black", font=("Times New Roman", 12, "bold"),foreground="white" )
        dateLabel.pack(pady=10)
       
        def tick():
            global time1
            # get the current local time (keep internet on)
            d = datetime.datetime.now()

            time2 = d.strftime("%A, %d %B %Y ------ %I:%M:%S %p " )
            # if time string has changed, update it
            if time2 != time1:
                time1 = time2
                dateLabel.configure(text=time2)
            # calls itself every 200 milliseconds
            # to update the time display as needed
            dateLabel.after(200, tick)
        tick()

        quoteLabel = Label(headFrame, text ="Quote of the day: " +  quote.getQuote()   , bg="black", font=("Helvetica 12 bold italic"), foreground="white" )
        quoteLabel.pack(pady=10)
        headFrame.pack()
    
        
#------------------------Admin Login Window---------------------------#

class topLevel:
    def __init__(self, root):
         self.root = root
        
    def AdminLogin(self):
        self.login = Toplevel(self.root)
        self.login.geometry("500x300+500+300")
        self.login.configure(background="")
        self.login.title("ADMIN LOGIN")
        self.usernamelbl = Label(self.login, text="Enter Username", width = 20, bg="white", font=("Times New Roman", 15, "bold"))
        self.usernamelbl.pack(pady=(50,10))
        self.usernameEnt = Entry(self.login, width = 23)
        self.usernameEnt.pack(pady=(0,30))
        self.passLbl = Label(self.login, text="Enter Password", width = 20, bg="white", font=("Times New Roman", 15, "bold"))
        self.passLbl.pack(pady=(0, 10))
        self.passEnt = Entry(self.login, show = "*", width = 23)
        self.passEnt.pack(pady=(0,30))
        self.LoginButton = Button(self.login, text = "LOGIN", command = self.check, width = 20, bg="gray", activebackground = "blue", font=("Times New Roman", 10, "bold"))
        self.LoginButton.pack()
        
    #-------------Function to verify user credentils-----------------------#
    def check(self):
        username = self.usernameEnt.get()
        password = self.passEnt.get()
        if username == "admin" and password ==  "123":
            messagebox.showinfo("CORRECT CREDENTIALS", "LOGIN SUCCESFULL!")
            self.login.withdraw()
            self.adminPanel()
        else:
            messagebox.showerror("INVALID CREDENTIALS", "LOGIN NOT SUCCESFULLY")
            self.login.deiconify()
            
    #---------------If user credentials are verified ADMIN PANEL will be opened--------------#
    def adminPanel(self):

        def insertMenuLB():
            self.LB.delete(0, END)
            backend.InsertMenuIntoLB(self.LB)

        def insertEmpLB():
            self.LB.delete(0, END)
            backend.InsertEmpIntoLB(self.LB)


        self.login.withdraw()
        self.root.withdraw()
        self.adminDashBoard = Toplevel(self.root)
        self.adminDashBoard.geometry("680x700+400+50")
        self.adminDashBoard.title("ADMIN DASHBOARD")
        self.adminDashBoard.configure(background="black", bd=10)

        self.newFrame = Frame(self.adminDashBoard, bg="black")
        self.MainLabel = Label(self.newFrame, text = "ADMIN PANEL",  font=("Times New Roman", 20, "bold"), foreground="white" )
        self.MainLabel.config(bg="black")
        self.MainLabel.grid(row=0, column=3)

        
        self.EmployeeLabel = Label(self.newFrame, text = "Employee Management",  font=("Times New Roman", 15, "bold"), foreground="white" )
        self.EmployeeLabel.config(bg="black")
        self.EmployeeLabel.grid(row=3, column=1, pady=20)
        self.ViewEmployee = Button(self.newFrame, text="View Employee", width=20, font=("Times New Roman", 10, "bold"), bg="gray", command= insertEmpLB, foreground="black"  )
        self.ViewEmployee.grid(row=4, column=1, pady=10)
        self.AddEmployee = Button(self.newFrame, text="Add Employee", width=20,  font=("Times New Roman", 10, "bold"), bg="gray", command = self.addEmployee)
        self.AddEmployee.grid(row=5, column=1, pady=10)
        self.RemoveEmployee = Button(self.newFrame, text="Remove Employee", width=20, font=("Times New Roman", 10, "bold"), bg="gray", command=self.removeEmployee, foreground="black")
        self.RemoveEmployee.grid(row=6, column=1, pady=10)
        
        self.MenuLabel = Label(self.newFrame, text = "Menu Management",  font=("Times New Roman", 15, "bold") , foreground="white" )
        self.MenuLabel.config(bg="black")
        self.MenuLabel.grid(row=3, column=5, pady=20)
        self.ViewMenu = Button(self.newFrame, text="View Menu", width=20, font=("Times New Roman", 10, "bold"), bg="gray", command= insertMenuLB , foreground="black" )
        self.ViewMenu.grid(row=4, column=5, pady=10)
        self.AddMenu = Button(self.newFrame, text="Add Menu", width=20,  font=("Times New Roman", 10, "bold"), bg="gray", command= self.addMENU , foreground="black")
        self.AddMenu.grid(row=5, column=5, pady=10)
        self.RemoveMenu = Button(self.newFrame, text="Remove Menu", width=20, font=("Times New Roman", 10, "bold"), bg="gray", command = self.removeMenu , foreground="black")
        self.RemoveMenu.grid(row=6, column=5, pady=10)
        self.newFrame.grid(padx=20)
        
        self.LB = Listbox(self.adminDashBoard,  font=("Times New Roman", 12, "bold"))
        self.LB.config(width=60,height=12, bg="gray")
        self.LB.grid(row=8, padx=10, pady=20)

        self.backButton = Button(self.adminDashBoard, text="BACK", width=20, font=("Times New Roman", 10, "bold"), bg="gray", command= self.back, foreground="black")
        self.backButton.grid(row=10, pady=10)

        self.gTotal = Label(self.adminDashBoard, text = "Total Sales:"+ str(item.grandTotal),  font=("Times New Roman", 15, "bold"), foreground="white" )
        self.gTotal.config(bg="black")




                        
        self.gTotal.grid(row = 12, pady=10)

        self.getChart = Button(self.adminDashBoard, text="Get Chart", width=20, font=("Times New Roman", 10, "bold"), bg="gray", command = graph.getGraph , foreground = "white")
        self.getChart.grid(row=13, pady=10)

    #----------------when back button is pressed on ADMIN PANEL--------------#
    def back(self):
        self.adminDashBoard.withdraw()
        self.root.deiconify()

    #-------------When ADD MENU button is pressed on ADMIN PANEL----------------#

    def addMENU(self):
        self.addMenu = Toplevel(self.adminDashBoard)
        self.addMenu.title("ADD Menu.")
        self.addMenu.geometry("400x300+1000+400")
        self.lblDish = Label(self.addMenu, text="Enter DISH NAME", width = 20, font = ('arial', 10))
        self.entDish = Entry(self.addMenu, bd=5, width = 20, font = ('arial', 10))
        self.lblRate = Label(self.addMenu, text="Enter RATE", width = 20, font = ('arial', 10))
        self.entRate = Entry(self.addMenu, bd=5, width = 20, font = ('arial', 10))
        
        self.saveBtn = Button(self.addMenu, text="SAVE", width = 20, font = ('arial', 10), command =lambda: self.getAndEnter("menu"))
        self.backBtn = Button(self.addMenu, text="BACK", width = 20, font = ('arial', 10), command = self.backMenu1)
        self.lblDish.pack(pady=10)
        self.entDish.pack()
        self.lblRate.pack(pady=10)
        self.entRate.pack()
        self.saveBtn.pack(pady=10)
        self.backBtn.pack(pady=10)

        #-------------When ADD EMPLOYEE button is pressed on ADMIN PANEL----------------#
    def addEmployee(self):
        self.addEmp = Toplevel(self.adminDashBoard)
        self.addEmp.title("ADD Emp.")
        self.addEmp.geometry("400x300+100+400")
        self.lblID = Label(self.addEmp, text="Enter Employee ID", width = 20, font = ('arial', 10))
        self.entID = Entry(self.addEmp, bd=5, width = 20, font = ('arial', 10))
        self.lblName = Label(self.addEmp, text="Enter EMPLOYEE NAME", width = 20, font = ('arial', 10))
        self.entName = Entry(self.addEmp, bd=5, width = 20, font = ('arial', 10))
        self.lblSalary = Label(self.addEmp, text="Enter Salary", width = 20, font = ('arial', 10))
        self.entSalary = Entry(self.addEmp, bd=5, width = 20, font = ('arial', 10)) 

        self.saveBtn = Button(self.addEmp, text="SAVE", width = 20, font = ('arial', 10), command =lambda: self.getAndEnter("emp"))
        self.backBtn = Button(self.addEmp, text="BACK", width = 20, font = ('arial', 10), command = self.backMenu2)
        self.lblID.pack(pady=10)
        self.entID.pack()
        self.lblName.pack(pady=10)
        self.entName.pack()
        self.lblSalary.pack(pady=10)
        self.entSalary.pack()
        self.saveBtn.pack(pady=10)
        self.backBtn.pack(pady=10)

        #-------------When REMOVE EMPLOYEE button is pressed on ADMIN PANEL----------------#

    def removeEmployee(self):
        self.removeEmp = Toplevel(self.adminDashBoard)
        self.removeEmp.title("REMOVE Emp.")
        self.removeEmp.geometry("400x300+100+300")
        self.lblID = Label(self.removeEmp, text="Enter Employee ID", width = 20, font = ('arial', 10))
        self.entID = Entry(self.removeEmp, bd=5, width = 20, font = ('arial', 10))
        self.deleteBtn = Button(self.removeEmp, text="DELETE", width = 10, font = ('arial', 10), command =lambda: self.getAndDelete("emp"))
        self.backBtn = Button(self.removeEmp, text="BACK", width = 10, font = ('arial', 10), command = self.backMenu3)
        self.lblID.pack()
        self.entID.pack()
        self.deleteBtn.pack(pady=10)
        self.backBtn.pack(pady=10)

    #-------------When REMOVE MENU button is pressed on ADMIN PANEL----------------#

    def removeMenu(self):
        self.removeM = Toplevel(self.adminDashBoard)
        self.removeM.title("REMOVE Menu.")
        self.removeM.geometry("400x300+700+300")
        self.lblDish = Label(self.removeM, text="Enter DISH NAME", width = 20, font = ('arial', 10))
        self.entDish = Entry(self.removeM, bd=5, width = 20, font = ('arial', 10))
        self.deleteBtn = Button(self.removeM, text="DELETE", width = 10, font = ('arial', 10), command =lambda: self.getAndDelete("menu"))
        self.backBtn = Button(self.removeM, text="BACK", width = 10, font = ('arial', 10), command = self.backMenu4)
        self.lblDish.pack()
        self.entDish.pack()
        self.deleteBtn.pack(pady=10)
        self.backBtn.pack(pady=10)


    def backMenu1(self):
        self.addMenu.withdraw()
    def backMenu2(self):
        self.addEmp.withdraw()
    def backMenu3(self):
        self.removeEmp.withdraw()
    def backMenu4(self):
        self.removeM.withdraw()

    #-------------Get user entered details and enter them into database------------#

    def getAndEnter(self, op):
        if op == "emp":
            ID = self.entID.get()
            name = self.entName.get()
            name = name.upper()
            salary = self.entSalary.get()
            #backend function is called
            backend.addIntoEmp(ID, name, salary)
            
        elif op == "menu":
            dish = self.entDish.get()
            dish = dish.upper()
            rate = self.entRate.get()
            #backend function is called
            backend.addIntoMenu(dish, rate, table.entDish, table.entRate)

    #-------------Get user entered details and delete them from database------------#

    def getAndDelete(self, op):
        if op == "emp":
            ID = self.entID.get()
            #backend function is called
            backend.deleteFromEmployee(ID, table.entID)
            
        elif op == "menu":
            dish = self.entDish.get()
            dish = dish.upper()
            #backend function is called
            backend.deleteFromMenu(dish, table.entDish)



    #----------------(STRUCTURE OF RESTAURENT TABLES ARE WRITTEN IN THIS CLASS)---------#

class tables(topLevel):
    test = 0
    def __init__(self, root):
        self.root = root   

        self.tableFrame = Frame(self.root, bg="black", borderwidth=10, relief=RAISED) #main frame created

        self.table1 = Button(self.tableFrame,text = "Table 1", height=3, width=8, bg="spring green", font=("Times New Roman", 15, "bold"), command=lambda: self.activate(1))
        self.table1.grid(row=0, column=1,padx=10, pady=10)
        self.table2 = Button(self.tableFrame,text = "Table 2", height=3, width=8, bg="spring green", font=("Times New Roman", 15, "bold"), command=lambda: self.activate(2))
        self.table2.grid(row=0, column=2,padx=10, pady=10)

        self.table3 = Button(self.tableFrame,text = "Table 3", height=3, width=8, bg="spring green", font=("Times New Roman", 15, "bold"), command=lambda: self.activate(3))
        self.table3.grid(row=1, column=1,padx=10, pady=10)
        self.table4 = Button(self.tableFrame,text = "Table 4", height=3, width=8, bg="spring green", font=("Times New Roman", 15, "bold"), command=lambda: self.activate(4))
        self.table4.grid(row=1, column=2,padx=10, pady=10)

        self.table5 = Button(self.tableFrame,text = "Table 5", height=3, width=8, bg="spring green", font=("Times New Roman", 15, "bold"), command=lambda: self.activate(5))
        self.table5.grid(row=2, column=1,padx=10, pady=10)
        self.table6 = Button(self.tableFrame,text = "Table 6", height=3, width=8, bg="spring green", font=("Times New Roman", 15, "bold"), command=lambda: self.activate(6))
        self.table6.grid(row=2, column=2,padx=10, pady=10)


        self.admin = Button(self.tableFrame,text = "ADMIN", height=2, width=30, bg="violet", command= self.AdminLogin)
        self.admin.grid(row=3,column=1, columnspan=2, padx=10, pady=20)



        self.tableFrame.pack(side=LEFT, padx=50)    #main frame is closed

    #-------When any of above table is clicked it gets OCCUPIED(activated)---------#

    def activate(self, btnId):
        
        if btnId == 1:
            self.table1.configure(bg="red")
            self.table1.configure(text="Table1\n(occupied)") #to change table status from available to occupied
            item.activeTable.configure(text="Serving Table 1", bg="light green")
            item.totalLabel.configure( text = "Total = "+str(item.table1amount))
            item.tkvar.set('Select Dish')
            item.tkquan.set("Select Quantity")
            item.releaseButton.configure(state=NORMAL)
            tables.test = 1
            item.listBox.delete(0, END)  #clear the listbox
            self.Insert(1)              #update list box with respective table data from database
            

        elif btnId == 2:
            self.table2.configure(bg="red")
            self.table2.configure(text="Table2\n(occupied)") #to change table status from available to occupied
            item.activeTable.configure(text="Serving Table 2", bg="light green")
            item.totalLabel.configure( text = "Total = "+str(item.table2amount))
            item.tkvar.set('Select Dish')
            item.tkquan.set("Select Quantity")
            item.releaseButton.configure(state=NORMAL)
            tables.test = 2
            item.listBox.delete(0, END)
            self.Insert(2)      #update list box with respective table data from database
            

        elif btnId == 3:
            self.table3.configure(bg="red")
            self.table3.configure(text="Table3\n(occupied)") #to change table status from available to occupied
            item.activeTable.configure(text="Serving Table 3", bg="light green")
            item.totalLabel.configure( text = "Total = "+str(item.table3amount))
            item.tkvar.set('Select Dish')
            item.tkquan.set("Select Quantity")
            item.releaseButton.configure(state=NORMAL)
            tables.test = 3
            item.listBox.delete(0, END)
            self.Insert(3)      #update list box with respective table data from database
            

        elif btnId == 4:
            self.table4.configure(bg="red")
            self.table4.configure(text="Table4\n(occupied)") #to change table status from available to occupied
            item.activeTable.configure(text="Serving Table 4", bg="light green")
            item.totalLabel.configure( text = "Total = "+str(item.table4amount))
            item.tkvar.set('Select Dish')
            item.tkquan.set("Select Quantity")
            item.releaseButton.configure(state=NORMAL)
            tables.test = 4
            item.listBox.delete(0, END)
            self.Insert(4)      #update list box with respective table data from database
            

        elif btnId == 5:
            self.table5.configure(bg="red")
            self.table5.configure(text="Table5\n(occupied)") #to change table status from available to occupied
            item.activeTable.configure(text="Serving Table 5", bg="light green")
            item.totalLabel.configure( text = "Total = "+str(item.table5amount))
            item.tkvar.set('Select Dish')
            item.tkquan.set("Select Quantity")
            item.releaseButton.configure(state=NORMAL)
            tables.test = 5
            item.listBox.delete(0, END)
            self.Insert(5)      #update list box with respective table data from database
           

        elif btnId == 6:
            self.table6.configure(bg="red")
            self.table6.configure(text="Table6\n(occupied)") #to change table status from available to occupied
            item.activeTable.configure(text="Serving Table 6", bg="light green")
            item.totalLabel.configure( text = "Total = "+str(item.table6amount))
            item.tkvar.set('Select Dish')
            item.tkquan.set("Select Quantity")
            item.releaseButton.configure(state=NORMAL)
            tables.test = 6
            item.listBox.delete(0, END)
            self.Insert(6)      #update list box with respective table data from database
            
    def Insert(self, tableNo):
        if tableNo == 1:
            tableName = "table1"
        elif tableNo == 2:
            tableName = "table2"
        elif tableNo == 3:
            tableName = "table3"
        elif tableNo == 4:
            tableName = "table4"
        elif tableNo == 5:
            tableName = "table5"
        elif tableNo == 6:
            tableName = "table6"
        
        #calling backend function to insert the items ordered by customer into respective table list
        backend.InsertIntoListBox(tableName, item.listBox)

#--------------------(STRUCTURE OF MENU LIST IS WRITTEN IN THIS CLASS)--------------------#
class items(tables):
    def __init__(self, root):
        self.root = root 

        self.itemFrame = Frame(self.root, bg ="black") #main frame is created

        self.tkvar = StringVar(self.itemFrame)
        self.choices = {'------------TEA------------':20, 'SPECIAL----------IDLI':30,'MASALA   -----   DOSA':50,'MEDU---------WADA':30,
        'VG.MANCHURIAN':120,'VEG FRIED- RICE':130,'PANER FRD.RICE':150, 'VEG------NOODLES':110, 
        'CHINESE NOODLES':170,'PANEER -- TIKKA':150, 'CHICKEN BIRYANI':200, 'CHICKEN ---- TIKKA':150,
        'CHICKEN TANDORI':210}

        self.tkquan = IntVar(self.itemFrame)
        self.q = [1,2,3,4,5,6,7,8,9]
        self.tkvar.set('Select Dish') # set the default option for dish
        self.tkquan.set("Select Quantity")  # set the default option for dish
        self.amount = 0.0 # set the initial respective table amount to display on label
        self.i = 1  # set the initial item number for respective table to display in list

        # set the initial amount for respective table to add to listbox
        self.table1item, self.table2item, self.table3item, self.table4item, self.table5item, self.table6item = 1,1,1,1,1,1
        # set the initial amount for respective table to add to gand total
        self.table1amount, self.table2amount, self.table3amount, self.table4amount, self.table5amount, self.table6amount = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 
        self.grandTotal = 0.0   # initializing the grand total amount when the app is started

        
        self.activeTable = Label(self.itemFrame, text= "No Table Selected", bg="red", width=20, font=("Times New Roman", 15, "bold") )
        self.activeTable.grid(row=0, column=0, pady=10)
        
        self.dropFrame = Frame(self.itemFrame)
        self.popupMenu = OptionMenu(self.dropFrame, self.tkvar, *self.choices)
        self.popupMenu.config(width=25, bg="peach puff", activebackground="sandy brown", font=("Times New Roman", 11, "bold"))
        self.popupMenu.grid(row=1,column=0)
        
        self.popupPlate = OptionMenu(self.dropFrame, self.tkquan, *self.q)
        self.popupPlate.config(width=25, bg="peach puff",activebackground="sandy brown", font=("Times New Roman", 11, "bold"))
        self.popupPlate.grid(row=1,column=1)
       
        self.addBtn = Button(self.dropFrame, text="ADD", width=20, bg="cyan",activebackground="blue", command=self.additem)
        self.addBtn.grid(row=1,column=2)
        self.dropFrame.grid(pady=15)
   

        self.dropFrame1 = Frame(self.itemFrame) #Nested frame is created to contain some elements

        self.itemNolbl = Label(self.dropFrame1, text = "Item No" ,width = 10, bg="light blue", font=("Times New Roman", 10, "bold"))
        self.dishNamelbl = Label(self.dropFrame1, text = "Dish Name" ,width = 10, bg="light blue", font=("Times New Roman", 10, "bold"))
        self.ratelbl = Label(self.dropFrame1, text = "Rate" ,width = 10, bg="light blue", font=("Times New Roman", 10, "bold"))
        self.quantitylbl = Label(self.dropFrame1, text = "Quantity" ,width = 10, bg="light blue", font=("Times New Roman", 10, "bold"))
        self.amountlbl = Label(self.dropFrame1, text = "Amount" ,width = 10, bg="light blue", font=("Times New Roman", 10, "bold"))
        self.itemNolbl.grid(row=2, column = 0, padx=(0,65))
        self.dishNamelbl.grid(row=2, column = 1, padx=5)
        self.ratelbl.grid(row=2, column = 2, padx=(47,0))
        self.quantitylbl.grid(row=2, column=3, padx=5)
        self.amountlbl.grid(row=2, column = 4, padx=5)
        self.dropFrame1.config(bg="light blue")

        self.dropFrame1.grid()  #nested frame is closed
        
        
        self.listBox = Listbox(self.itemFrame,font=("Times New Roman", 12, "bold"))
        self.listBox.config(width=70,height=15, bg="light blue")
        self.listBox.grid(row=3,padx=1)

        self.totalLabel = Label(self.itemFrame, text = "Total = 0.0" ,width = 25, bg="peach puff", font=("Times New Roman", 15, "bold") )
        self.totalLabel.grid(row=4)
        self.releaseButton = Button(self.itemFrame, text="Release Table/Generate Bill",state=DISABLED, width=35, bg="red",font=("Times New Roman", 15, "bold"), command= self.release )
        self.releaseButton.grid(row=5)

        self.itemFrame.pack(side=LEFT, padx=50) #Main frame is closed

        
    #--------When add button is clicked after selecting dish and quantity-----------#

    def additem(self):
        if tables.test != 0: 
            try:

                if tables.test == 1:
                    tableName = "table1"
                    self.i = self.table1item
                    self.amount = self.table1amount
                elif tables.test == 2:
                    tableName = "table2"
                    self.i = self.table2item
                    self.amount = self.table2amount
                elif tables.test == 3:
                    tableName = "table3"
                    self.i = self.table3item
                    self.amount = self.table3amount
                elif tables.test == 4:
                    tableName = "table4"
                    self.i = self.table4item
                    self.amount = self.table4amount
                elif tables.test == 5:
                    tableName = "table5"
                    self.i = self.table5item
                    self.amount = self.table5amount
                elif tables.test == 6:
                    tableName = "table6"
                    self.i = self.table6item
                    self.amount = self.table6amount


                dish = self.tkvar.get()
                if dish!= "Select Dish":
                    quan = self.tkquan.get()
                    itemAmount = quan*self.choices[dish]
                    if dish in self.choices:
                        self.amount = self.amount + itemAmount
                        self.listBox.insert(END, str("              "+ str(self.i) + "              "+ dish  + "                "+   str(self.choices[dish])+ "                  " +str(quan) +"               "+ str(itemAmount)))
      
                    self.totalLabel.configure( text = "Total = "+str(self.amount)) #Updating the total label whenever new items are ordered by customer
                    #calling backend function to insert into respective table
                    backend.InsertIntoTable(tableName, self.i, dish,  self.choices[dish]  , quan, itemAmount)
                    self.tkvar.set('Select Dish') # set the default option for dish
                    self.tkquan.set("Select Quantity")  # set the default option for dish
                    self.i = self.i + 1 
                    if tables.test == 1:
                        self.table1item = self.i
                        self.table1amount = self.amount
                    elif tables.test == 2:
                        self.table2item = self.i
                        self.table2amount = self.amount
                    elif tables.test == 3:
                        self.table3item = self.i
                        self.table3amount = self.amount
                    elif tables.test == 4:
                        self.table4item = self.i
                        self.table4amount = self.amount
                    elif tables.test == 5:
                        self.table5item = self.i
                        self.table5amount = self.amount
                    elif tables.test == 6:
                        self.table6item = self.i
                        self.table6amount = self.amount
                else:
                    messagebox.showwarning("NOT SELECTED", "Please Select Dish")
            except Exception as e:
                messagebox.showwarning("NOT SELECTED ", "Please select Quantity")                
        else:
            messagebox.showerror("Error", "Please Select Table")

#---------When relese button is pressed (This means the customer has paid the bill and table status
# is changed from occupied to available)
# also bill is generated in PDF format -----------------#

    def release(self):
        if tables.test == 1:
            tableName = "table1"
            self.grandTotal = self.grandTotal + self.table1amount
            self.table1item = 1
            self.table1amount = 0.0
            table.table1.configure(bg="spring green", text="Table 1")  #table status is updated by changing its color and text
        elif tables.test == 2:
            tableName = "table2"
            self.grandTotal = self.grandTotal + self.table2amount
            self.table2item = 1
            self.table2amount = 0.0
            table.table2.configure(bg="spring green", text="Table 2")   #table status is updated by changing its color and text
        elif tables.test == 3:
            tableName = "table3"
            self.grandTotal = self.grandTotal + self.table3amount
            self.table3item = 1
            self.table3amount = 0.0
            table.table3.configure(bg="spring green", text="Table 3")   #table status is updated by changing its color and text
        elif tables.test == 4:
            tableName = "table4"
            self.grandTotal = self.grandTotal + self.table4amount
            self.table4item = 1
            self.table4amount = 0.0
            table.table4.configure(bg="spring green", text="Table 4")   #table status is updated by changing its color and text
        elif tables.test == 5:
            tableName = "table5"
            self.grandTotal = self.grandTotal + self.table5amount
            self.table5item = 1
            self.table5amount = 0.0
            table.table5.configure(bg="spring green", text="Table 5")   #table status is updated by changing its color and text
        elif tables.test == 6:
            tableName = "table6"
            self.grandTotal = self.grandTotal + self.table6amount
            self.table6item = 1
            self.table6amount = 0.0
            table.table6.configure(bg="spring green", text="Table 6")   #table status is updated by changing its color and text
        self.totalLabel.configure(text="Total = 0.0")
        self.releaseButton.configure(state=DISABLED)
        print("Grand Total = ",self.grandTotal)

        #calling pdfGenerator 
        pdfGenerator.generatePdf(tableName)
        if pdfGenerator.done == 1:
            #calling delete function from backend clear the list from respective table
            backend.deleteFromTable(tableName)
            tables.test = 0
            item.listBox.delete(0, END) #clearing the listbox
            self.activeTable.configure(text="No Table Selected", bg="red")  #updating the indicator label
        elif pdfGenerator.done == 0:
            messagebox.showinfo("Data is not lost", "1. Close PDF from another tab \n2.Select Table and generate bill again")

    def getTotal(self):
        return self.grandTotal

#-------------FETCHING THE MENU IS WRITTEN IN THIS CLASS---------------#        

class menu:
    def __init__(self, root):
        self.root = root
        getMenu.image()
        self.loadImg()
    def loadImg(self):
        imageFrame = Frame(self.root, bg="red" )
        load = Image.open("menu.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(imageFrame, image=render)
        img.image = render
        img.pack()
        imageFrame.config( height=0)
        imageFrame.pack(side=LEFT, pady=50)


#-----------FINALLY INSTANTIATING ALL THE CLASSES AND INITIALIZING ROOT WINDOW-------------#

if __name__ == "__main__":
    root = Tk()
    root.geometry("1400x750")
    root.configure(background="SkyBlue1")
    head = heading(root)    # OBJECT FOR HEADFRAME
    table = tables(root)    # OBJECT FOR TABLERAME
    item = items(root)      # OBJECT FOR ITEMSFRAME
    m = Menu(root)          # OBJECT FOR MENU FRAME
    top = topLevel(root)    # OBJECT FOR TOPLEVEL (ADMIN LOGIN, ADMIN DASHBOARD)
    root.mainloop()
