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


class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print("Name: {} | Phone: {} | Email:{}".format(self.name, self.phone, self.email))

print("==Welcome==")
print("1. Add New Customer")
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
