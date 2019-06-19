"""
    1. Install XAMPP / WAMPP
        DB -> MySQL Setup | RDBMS -> Relational Data Base Management System


    2. Create a DataBase in XAMPP
        Database -> Collection of Tables

    3. Create a Table in DataBase
        Table -> Collection of Rows and Columns just like excel sheet

    ORM : Object Relational Mapping
        Table Name : Customer
        Columns : name, phone, email

        In every table we can have 1 additional column
        We call that column as a primary key and auto increment

    SQL -> Structured Query Language in MySQL DataBase

    Python Syntax:
    class Customer:

        def __init__(self, name, phone, email):
            self.name = name
            self.phone = phone
            self.email = email

    SQL Syntax:
    create table Customer(
        cid int primary key auto_increment,
        name varchar(256),
        phone varchar(256),
        email varchar(256)
    )

    4. Insert Data in Table

    Python Syntax:
    cRef = Customer('John', '+91 99999 88888', 'john@example.com')

    SQL Syntax:
    insert into Customer values(null, 'John', '+91 99999 88888', 'john@example.com')

    5. Configure Python Driver in Your Pycharm Project

    6. Write Python Program to Save Data in Table

    7. Update Row in Table
    update Customer set name = 'John Watson', email = 'john.w@example.com', phone = '+91 99999 88888' where cid = 1

"""

import mysql.connector

# DAO : Data Access Object
# So that we can perform DB operations using the below class DBHelper
class DBHelper:

    def saveCustomerInDB(self, customer):
        # 1. Create SQL Statement
        sql =  "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)
        print(sql)

        # 2. Create Connection with DataBase
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="aurigw")

        # 3. Create Cursor over connection to execute SQL Statements

        cursor = con.cursor()
        cursor.execute(sql)

        con.commit() # Execute as Transaction

        print(">> ", customer.name, "Saved !!")

    def upatedCustomerInDB(self, customer):
        # 1. Create SQL Statement
        sql =  "update Customer set name = '{}', email = '{}', phone = '{}' where cid = {}".format(customer.name, customer.email, customer.phone, customer.cid)

        print(sql)

        # 2. Create Connection with DataBase
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="aurigw")

        # 3. Create Cursor over connection to execute SQL Statements

        cursor = con.cursor()
        cursor.execute(sql)

        con.commit() # Execute as Transaction

        print(">> ", customer.name, "Updated !!")

    def deleteCustomerFromDB(self, cid):
        # 1. Create SQL Statement
        sql =  "delete from Customer where cid = {}".format(cid)

        print(sql)

        # 2. Create Connection with DataBase
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="aurigw")

        # 3. Create Cursor over connection to execute SQL Statements

        cursor = con.cursor()
        cursor.execute(sql)

        con.commit() # Execute as Transaction

        print(">> ", cid, "Deleted !!")

    def fetchAllCustomersFromDB(self):
        # 1. Create SQL Statement
        sql =  "select * from Customer"

        print(sql)

        # 2. Create Connection with DataBase
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="aurigw")

        # 3. Create Cursor over connection to execute SQL Statements

        cursor = con.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        # print(rows)

        for row in rows:
            print(row)


    def fetchSingleCustomerFromDB(self, cid):
        # 1. Create SQL Statement
        sql =  "select * from Customer where cid = {}".format(cid)

        print(sql)

        # 2. Create Connection with DataBase
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="aurigw")

        # 3. Create Cursor over connection to execute SQL Statements

        cursor = con.cursor()
        cursor.execute(sql)

        row = cursor.fetchone()
        print(row)



class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print("Name: {} | Phone: {} | Email:{}".format(self.name, self.phone, self.email))


"""
print("==Welcome==")
print("1. Add New Customer")
print("2. Update Customer")
print("3. Delete Customer")
print("4. View Customers")
choice = int(input("Enter Your Choice: "))

if choice == 1:
    cRef = Customer(None, None, None)
    cRef.name = input("Enter Customer Name: ")
    cRef.phone = input("Enter Customer Phone: ")
    cRef.email = input("Enter Customer Email: ")

    cRef.showCustomerDetails()

    save = input("Do you wish to Save Customer(yes/no): ")

    if save == "yes":
        db = DBHelper()
        db.saveCustomerInDB(cRef)

elif choice == 2:
    cRef = Customer(None, None, None)
    cRef.cid = int(input("Enter Customer ID: "))
    cRef.name = input("Enter Customer Name: ")
    cRef.phone = input("Enter Customer Phone: ")
    cRef.email = input("Enter Customer Email: ")

    cRef.showCustomerDetails()

    update = input("Do you wish to Update Customer(yes/no): ")

    if update == "yes":
        db = DBHelper()
        db.upatedCustomerInDB(cRef)

elif choice == 3:

    db = DBHelper()

    cid = int(input("Enter Customer ID: "))

    db.fetchSingleCustomerFromDB(cid)

    delete = input("Do you wish to Delete Customer(yes/no): ")

    if delete == "yes":

        db.deleteCustomerFromDB(cid)

elif choice == 4:
    db = DBHelper()
    db.fetchAllCustomersFromDB()
"""