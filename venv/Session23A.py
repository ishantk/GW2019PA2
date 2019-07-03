import threading
import time

# print(">> App Started")

lock = threading.Lock()

class Printer:
    def printDocument(self, docName, copies):

        lock.acquire()

        for i in range(1, copies+1):
            time.sleep(1) # 1 second
            print(">> Printing {} Copy #{}".format(docName, i))

        lock.release()

class Desktop(threading.Thread):

    def attachPrinter(self, printer):
        self.printer = printer

    def run(self):
        self.printer.printDocument(" ** LearningPython.pdf ** ", 10)

class Laptop(threading.Thread):

    def attachPrinter(self, printer):
        self.printer = printer

    def run(self):
        self.printer.printDocument(" ## LearningJava.pdf ##", 10)


printer = Printer()
# printer.printDocument("LearningPython.pdf", 10)

desktop = Desktop()
desktop.attachPrinter(printer)

laptop = Laptop()
laptop.attachPrinter(printer)

desktop.start()
laptop.start()


# print(">> App Finished")