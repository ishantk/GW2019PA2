"""
    Python and Firebase
    Firebase : Product of Google
             : Serverless Computing Platform

    1. Go to Google Firebase
    2. Click on Go To Console and Login
    3. Create a New Project
    4. Create a DataBase -> Cloud Firestore
                            and NOT Realtime Database
                            Locked Mode
                            Test Mode (SELECT This)
       Collection -> Folder or Table
       Document   -> File containing data as dictionary or Row

    5. Open the Link for Python and Firebase Integration
       and follow steps
       https://firebase.google.com/docs/firestore/quickstart
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Reference to Firebase Firestore DataBase
db = firestore.client()

class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print("Name: {} | Phone: {} | Email:{}".format(self.name, self.phone, self.email))


cRef = Customer("John", "+91 99999 88888", "john@example.com")
data = cRef.__dict__
print(data)

# Insert Data in Cloud Firebase Firestore :)
# db.collection("Customer").document().set(data)

# print(">> Done")

docs = db.collection("Customer").get()

for doc in docs:
    print(doc.id, doc.to_dict())

# 1. Update Operation
# 2. Delete Operation