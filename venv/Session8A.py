class Counter:
    # Attribute: Property of Class
    ccount = 1

    # Constructor Function
    def __init__(self):
        self.count = 1
        Counter.ccount = 1
    # Business Function : Logic
    def increment(self):
        self.count = self.count + 1
        Counter.ccount = Counter.ccount + 1
    # Read Function : Displaying/Reading the container
    def show(self):
        print("count is: {} and ccount is: {}".format(self.count, Counter.ccount))

c1 = Counter()  # Object Construction
c2 = Counter()  # Object Construction
c3 = c1         # Reference Copy

c1.increment()
c2.increment()
c3.increment()

c1.increment()
c2.increment()
c3.increment()

c4 = Counter()

c1.show() # count is: 5 and ccount is: 7 1 7
c2.show() # count is: 3 and ccount is: 7 1 7
c3.show() # count is: 5 and ccount is: 7 1 7
c4.show() # count is: 1 and ccount is: 1 1 7