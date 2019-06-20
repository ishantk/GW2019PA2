from tkinter import *

# from Session12 import Customer
# from Session12 import DBHelper

from Session12 import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Reference to Firebase Firestore DataBase
db = firestore.client()


def onClick():

    cRef = Customer(None, None, None)

    cRef.name = entryName.get()
    cRef.phone = entryPhone.get()
    cRef.email = entryEmail.get()

    # print(">> Button Clicked")
    # print(">> Data: ",name, phone, email)

    cRef.showCustomerDetails()

    # db = DBHelper()
    # db.saveCustomerInDB(cRef)

    data = cRef.__dict__
    # Insert Data in Cloud Firebase Firestore :)
    db.collection("Customer").document().set(data)
    print(">> Document Saved :)")

window = Tk()

lblTitle = Label(window, text="Enter Customer Details")
lblTitle.pack()

lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Customer Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer = Button(window, text="Add Customer", command=onClick)
btnAddCustomer.pack()

window.mainloop()