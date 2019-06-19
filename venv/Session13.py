from tkinter import *

# from Session12 import Customer
# from Session12 import DBHelper

from Session12 import *

def onClick():

    cRef = Customer(None, None, None)

    cRef.name = entryName.get()
    cRef.phone = entryPhone.get()
    cRef.email = entryEmail.get()

    # print(">> Button Clicked")
    # print(">> Data: ",name, phone, email)

    cRef.showCustomerDetails()

    db = DBHelper()
    db.saveCustomerInDB(cRef)

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