from tkinter import *
from tkinter import messagebox
import mysql.connector

def establish_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Redranger@123",
        database="Kishore"
    )

from tkinter import *
from tkinter import messagebox
import mysql.connector

# Function to establish a database connection
def establish_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Redranger@123",
        database="Kishore"
    )
import mysql.connector

def create_tables():
    try:
        # Establish connection to MySQL
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Redranger@123",
            database="Kishore"
        )
        cursor = con.cursor()

        for i in range(1, 7):  # Assuming you have 6 tables
            table_name = f"table{i}"
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    itemNo INT PRIMARY KEY,
                    dishName VARCHAR(50),
                    rate FLOAT,
                    quantity INT,
                    itemAmount FLOAT
                )
            """)
        
        con.commit()
        print("Tables created successfully!")
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

        try:
            # Establish connection to MySQL again for creating 'menu' table
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Redranger@123",
                database="Kishore"
            )
            cursor = conn.cursor()

            cursor.execute("""
                 CREATE TABLE IF NOT EXISTS menu (
                    dish VARCHAR(255) PRIMARY KEY,
                    rate INT NOT NULL
                )
            """)

            conn.commit()
            print("Menu table created successfully!")
        except mysql.connector.Error as e:
            conn.rollback()
            print("Error creating menu table:", e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

# Check if tables exist, if not, create them
create_tables()




def InsertIntoListBox(tableName, listBox):
    conn = establish_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT itemNo, dish, rate, quantity, itemamount FROM " + tableName + " ORDER BY itemNo")
        data = cursor.fetchall()
        for d in data:
            mdata = "            " + str(d[0]) + "                   " + d[1] + "              " + str(d[2]) + \
                    "                " + str(d[3]) + "             " + str(d[4]) + "\n"
            listBox.insert(END, mdata)
    except mysql.connector.Error as e:
        print("issue", e)
    finally:
        cursor.close()
        conn.close()


def InsertIntoTable(tableName, itemNo, dish, itemAmount, quantity, amount):
    conn = establish_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO " + tableName + " VALUES (%s, %s, %s, %s, %s)"
        args = (itemNo, dish, itemAmount, quantity, amount)
        cursor.execute(sql, args)
        conn.commit()
    except mysql.connector.Error as e:
        conn.rollback()
        print("error -->", e)
    finally:
        cursor.close()
        conn.close()


def deleteFromTable(tableName):
    conn = establish_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM " + tableName
        cursor.execute(sql)
        conn.commit()
    except mysql.connector.Error as e:
        conn.rollback()
        print("error is ", e)
    finally:
        cursor.close()
        conn.close()

def addIntoMenu(dish_name, rate, entDish, entRate):
    if dish_name == '' or rate == '':
        messagebox.showerror("Error ", "Please fill all the fields")
    elif len(dish_name) < 2 or len(dish_name) > 20:
        messagebox.showerror("Error ", "DISH name should contain at least 2 and maximum 20 letters")
        entDish.delete(0, END)
        entDish.focus()
    elif rate.isdigit():
        rate = int(rate)
        if rate < 10:
            messagebox.showerror("Error ", "Rate cannot be less than 10 Rupees")
            entRate.delete(0, END)
            entRate.focus()
        else:
            import mysql.connector
            conn = None
            cursor = None
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Redranger@123",
                    database="Kishore"
                )
                cursor = conn.cursor()
                sql = "INSERT INTO menu (dish, rate) VALUES (%s, %s)"
                args = (dish_name, rate)
                cursor.execute(sql, args)
                conn.commit()
                msg = str(cursor.rowcount) + " records inserted"
                messagebox.showinfo("Success ", msg)
                entDish.delete(0, END)
                entRate.delete(0, END)
            except mysql.connector.Error as e:
                conn.rollback()
                print("error -->", e)
                messagebox.showerror("Error", "An error occurred while inserting data")
            finally:
                if cursor is not None:
                    cursor.close()
                if conn is not None:
                    conn.close()
    else:
        messagebox.showerror("Error ", "RATE SHOULD CONTAIN ONLY DIGITS")
        entRate.delete(0, END)
        entRate.focus()


def InsertMenuIntoLB(LB):
    import mysql.connector
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Redranger@123",
            database="Kishore"
        )
        cursor = conn.cursor()
        sql = "SELECT * FROM menu"
        cursor.execute(sql)
        for d in cursor.fetchall():
            dish = d[0]
            rate = d[1]
            mdata = f"{dish:<25}{rate}\n"
            LB.insert(END, mdata)
    except mysql.connector.Error as e:
        print("Error:", e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def addIntoEmp(employee_id, name, salary):
    cursor = None  # Initialize cursor variable
    con = None     # Initialize connection variable

    if not employee_id or not name or not salary:
        messagebox.showerror("Error", "Please fill all the fields")
        return

    if not employee_id.isdigit():
        messagebox.showerror("Error", "ID should contain only digits")
        return

    if not name.isalpha():
        messagebox.showerror("Error", "Name cannot contain numbers or special characters")
        return

    if not salary.isdigit():
        messagebox.showerror("Error", "Salary should contain only digits")
        return

    employee_id = int(employee_id)
    salary = int(salary)

    if len(name) < 2 or len(name) > 20:
        messagebox.showerror("Error", "Employee name should contain at least 2 and at most 20 letters")
        return

    if salary < 8000:
        messagebox.showerror("Error", "Salary cannot be less than 8000")
        return

    try:
        # Establishing a connection to the MySQL database
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Redranger@123",
            database="Kishore"
        )
        cursor = con.cursor()

        # SQL to create the table if it doesn't exist
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS hotel_employee (
            ID INT PRIMARY KEY,
            name VARCHAR(20),
            salary INT
        )
        """
        cursor.execute(create_table_sql)

        # SQL query to insert or update data in the table
        sql = """
            INSERT INTO hotel_employee (ID, name, salary)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            salary = VALUES(salary)
        """
        values = (employee_id, name, salary)

        cursor.execute(sql, values)
        con.commit()

        if cursor.rowcount == 1:
            msg = "1 record inserted"
        else:
            msg = "1 record updated"
        messagebox.showinfo("Success", msg)
    except Error as e:
        print("Error:", e)
        messagebox.showerror("Error", f"Database error: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()


def InsertEmpIntoLB(LB):
    import mysql.connector
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Redranger@123",
            database="Kishore"
        )
        cursor = conn.cursor()
        sql = "SELECT * FROM hotel_employee ORDER BY ID"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            mdata = "            {}            {}                                 {}\n".format(d[0], d[1], d[2])
            LB.insert(END, mdata)
    except mysql.connector.Error as e:
        print("Issue:", e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def deleteFromEmployee(ID, entID):
    if ID == '':
        messagebox.showerror("error", "ID CANNOT BE BLANK")
    elif ID.isdigit():
        import mysql.connector
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Redranger@123",
                database="Kishore"
            )
            cursor = conn.cursor()
            sql = "DELETE FROM hotel_employee WHERE ID = %s"
            cursor.execute(sql, (ID,))
            conn.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("error", "EMP ID = " + ID + " DOESN'T EXIST")
            else:
                msg = str(cursor.rowcount) + " Employee with ID =" + str(ID) + " Deleted"
                messagebox.showinfo("Success", msg)
        except mysql.connector.Error as e:
            print("Issue:", e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
    else:
        messagebox.showerror("error", "ID cannot contain letters and special characters")


def deleteFromMenu(dish, entDish):
    if dish == '':
        messagebox.showerror("Error", "DISH NAME CANNOT BE BLANK")
    else:
        import mysql.connector
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Redranger@123",
                database="Kishore"
            )
            cursor = conn.cursor()
            sql = "DELETE FROM menu WHERE dish = %s"
            cursor.execute(sql, (dish,))
            conn.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("Error", "DISH NAME = " + dish + " DOESN'T EXIST")
            else:
                msg = str(cursor.rowcount) + " dish with name = " + dish + " Deleted"
                messagebox.showinfo("Success", msg)
        except mysql.connector.Error as e:
            print("Issue:", e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
