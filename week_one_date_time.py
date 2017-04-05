import datetime as dt
import time as tm

# Time return the current time in seconds since Epoch
print(tm.time())
print("---------------")

dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)
print("---------------")

print(dtnow.year) 
print(dtnow.month) 
print(dtnow.day) 
print(dtnow.hour) 
print(dtnow.minute) 
print(dtnow.second)
print("---------------")

# timedelta is a duration expressing the difference between two dates
delta = dt.timedelta(days = 100)
print(delta)
print("---------------")

today = dt.date.today()
print(today)
print("---------------")

today - delta # The date 100 days ago
print(today - delta)
print("---------------")

today > today - delta
print(today > today - delta)
print("---------------")
