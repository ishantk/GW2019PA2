# hierarchy Inheritance
class Cab:

    def bookCab(self, source, destination):
        print(">> Cab Booked from {} to {}".format(source, destination))

class UberPool(Cab):

    def bookCab(self, source, destination):
        print(">> UberPool Cab Booked from {} to {}".format(source, destination))

class UberGo(Cab):

    def bookCab(self, source, destination):
        print(">> UberGo Cab Booked from {} to {}".format(source, destination))

class UberX(Cab):

    def bookCab(self, source, destination):
        print(">> UberX Cab Booked from {} to {}".format(source, destination))

# cRef = Cab()
# cRef.bookCab("Silver Arc", "MBD")

cRef = UberPool()
cRef.bookCab("Silver Arc", "MBD")

print()

cRef = UberGo()
cRef.bookCab("Silver Arc", "MBD")

print()

cRef = UberX()
cRef.bookCab("Silver Arc", "MBD")

# Run Time Polymorphism - RTP
# Same Reference Variable can point to any Child Object
# Same function bookCab with similar inputs is booking different cabs