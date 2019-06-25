# import datetime
import datetime as dt

today = dt.datetime.today()
print("Today:",today)

tomorrow = dt.datetime(2019, 6, 26, 18, 12, 12, 100)
print("Tomorrow:",tomorrow)

difference = tomorrow - today
print("Difference:",difference)