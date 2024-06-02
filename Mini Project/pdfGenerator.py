from fpdf import FPDF
from tkinter import messagebox
import datetime
import time
import random
import mysql.connector

done = 2

def generatePdf(tableName):
    global done
    con = None
    cursor = None
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Redranger@123",
            database="Kishore"
        )
        cursor = con.cursor()
        sql = "SELECT * FROM " + tableName + " ORDER BY itemNo"
        cursor.execute(sql)
        data = cursor.fetchall()
        
        if cursor.rowcount == 0:
            print("Order was empty, PDF not generated!")
            return

        li, ld, lr, lq, la = [], [], [], [], []
        for d in data:
            li.append(d[0])
            ld.append(d[1])
            lr.append(d[2])
            lq.append(d[3])
            la.append(d[4])

        # Getting total amount
        q = "SELECT SUM(itemamount) FROM " + tableName
        cursor.execute(q)
        amount = cursor.fetchone()[0]

        # Getting amount after adding 9% tax
        amount_to_pay = amount + amount * 0.09

        # Getting date and time
        d = datetime.datetime.now()
        dt = d.strftime("%d / %m / %Y")
        t = d.strftime("%I:%M:%S %p")

        # Getting random 3-digit number for receipt number
        rno = random.randint(100, 999)

        # Creating PDF object
        pdf = FPDF('P', 'mm', (150, 260))
        pdf.add_page()
        pdf.set_font("Times", 'BI', 18)

        # Adding header
        pdf.set_xy(38.0, 7)
        pdf.write(15, "Python Developers' Restaurant")
        
        pdf.set_font("Arial", 'B', 9)
        pdf.set_xy(10, 19)
        pdf.write(5, "Date : " + dt)

        pdf.set_xy(10, 23)
        pdf.write(5, "Time : " + t)

        pdf.set_xy(110, 19)
        pdf.write(5, "Table : " + tableName)

        pdf.set_xy(110, 23)
        pdf.write(5, "Receipt No : " + str(rno))

        pdf.set_font("Arial", 'B', 12)
        pdf.set_xy(10.0, 30)
        pdf.dashed_line(10, 30, 140, 30, dash_length=1, space_length=1)
        pdf.write(10, "Item no           Dish Name              Rate        Quantity       Amount")
        pdf.dashed_line(10, 40, 140, 40, dash_length=1, space_length=1)

        # Printing the content of dish on PDF
        m = 40
        for k in range(len(li)):
            pdf.set_xy(14.0, m)
            pdf.write(10, str(li[k]))
            pdf.set_xy(30.0, m)
            pdf.write(10, str(ld[k]))
            pdf.set_xy(80.0, m)
            pdf.write(10, str(lr[k]))
            pdf.set_xy(100.0, m)
            pdf.write(10, str(lq[k]))
            pdf.set_xy(124.0, m)
            pdf.write(10, str(la[k]))
            m = m + 10
        pdf.dashed_line(10, m, 140, m, dash_length=1, space_length=1)

        pdf.image("stamp.jpg", x=80, y=150, w=50, h=40)

        # Adding footer
        pdf.dashed_line(10, 200, 140, 200, dash_length=1, space_length=1)
        pdf.set_xy(60.0, 201)
        pdf.write(10, "Total amount                     = Rs. " + str(amount))
        pdf.set_xy(60.0, 205)
        pdf.write(10, "SGST                                   = 4.5%")
        pdf.set_xy(60.0, 210)
        pdf.write(10, "CGST                                   = 4.5%")

        pdf.dashed_line(10, 219, 140, 219, dash_length=1, space_length=1)
        pdf.set_xy(60.0, 217)
        pdf.write(10, "TOTAL AMOUNT TO PAY = Rs. " + str(amount_to_pay))
        pdf.dashed_line(10, 225, 140, 225, dash_length=1, space_length=1)
        pdf.set_xy(42.0, 225)
        pdf.set_font("Courier", 'BI', 17)
        pdf.write(8, "Please Visit Again")
        pdf.set_font("Times", 'BIU', 10)
        pdf.set_xy(45.0, 232)
        pdf.write(5, "Kubulakshmi restaurent")
        pdf.set_line_width(1)
        pdf.line(10, 10, 140, 10)
        pdf.line(10, 10, 10, 250)
        pdf.line(140, 10, 140, 250)
        pdf.line(10, 250, 140, 250)

        try:
            pdf.output(tableName + ".pdf")
            messagebox.showinfo("PDF CREATED", "BILL GENERATED SUCCESSFULLY")
            print("*****************PDF created**************")
            done = 1
        except PermissionError as e:
            done = 0
            messagebox.showwarning("BILL CANNOT BE GENERATED", "PLEASE CHECK IF THE SAME TABLE PDF IS ALREADY OPENED IN ANOTHER TAB")
    except mysql.connector.Error as e:
        print("Issue:", e)
        messagebox.showerror("Database Error", f"Database error: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

    return 0
