"""
    Exception is Parent to All the Errors
        IndexError(Exception)
        ZeroDivisionError(Exception)
        NameError(Exception)
        .
        ..
        ...

    try:
        ...
    except:
        ....
    finally:
        ....

    try:
        try:
        ...
        except:
            ....
        finally:
            ....

    except:
        try:
        ...
        except:
            ....
        finally:
            ....

    finally:
        try:
        ...
        except:
            ....
        finally:
            ....

"""

# BankingException IS-AN Exception | Inheritance | IS-A
# User Defined Exception
class BankingException(Exception):
    pass


class BankAccount:

    def __init__(self):
        self.balance = 10000
        self.attempts = 0

    def withdraw(self, amount):
        self.balance -= amount

        if self.balance <= 0:
            self.balance += amount
            self.attempts += 1
            print("Withdraw Failed !! Balance is Low:",self.balance)
        else:
            print("Withdraw Done! New Balance is:",self.balance)

        if self.attempts == 3:
            # iRef = IndexError("Illegal Attempts !!")
            # raise iRef # We are explicitly now crashing our program

            # bRef = BankingException("Illegal Attempts !!")
            # raise bRef

            raise BankingException("Illegal Attempts !!")


print(">> Banking Started")
bRef = BankAccount()

try:
    for _ in range(5000):
        bRef.withdraw(3000)
except Exception as e:
    print(">> Sorry !! We cannot Process More requests !!")

print(">> Banking Finished")





