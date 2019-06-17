"""
class CA():
    pass

a = 10
a = "John"
a = 2.2
a = CA()
"""

# class CA:
# class CA():
class CA(object):
    pass

class CB:
    pass

# class list(object):
#     pass

cRef = CA()
print("CA Object Dictionary:",cRef.__dict__)
print("CA Class Dictionary:",CA.__dict__)
print("CB Class Dictionary:",CB.__dict__)


# RULE : Parent's Reference Can Point to Any Child Object
# In Python we have object class as parent to all
