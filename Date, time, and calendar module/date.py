from datetime import datetime,date,time

today = date.today()
print("today is:",today)
now = datetime.now()
print("Now:",now)
Currenttime = time(now.hour,now.minute,now.second)
print("Current time is:", Currenttime)
print("Today year:",now.year)
print("Today month:",now.month)
print("Today day:",now.day)