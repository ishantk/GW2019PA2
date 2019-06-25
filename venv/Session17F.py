# In Python Every Source File is called as Python Module

"""
import Session17E

print(Session17E.companyName)
Session17E.hello("John")
Session17E.bye("Fionna")
sRef = Session17E.Student(101, "Leo")
sRef.show()
"""

"""
import Session17E as ss

print(ss.companyName)
ss.hello("John")
ss.bye("Fionna")
sRef = ss.Student(101, "Leo")
sRef.show()
"""

"""
# from Session17E import hello
# from Session17E import bye

from Session17E import *

hello("Harry")
bye("George")

"""

"""
import db.DBHelper
db.DBHelper.saveCustomer("John","+91 99999 88888", "john@example.com")
"""

"""
import db.DBHelper as db
db.saveCustomer("John","+91 99999 88888", "john@example.com")
"""

# from db import DBHelper
# from db import * # error
# DBHelper.saveCustomer("John","+91 99999 88888", "john@example.com")