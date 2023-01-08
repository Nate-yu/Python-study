from datetime import datetime
# today = datetime.now()
""" today = datetime.utcnow()
print(today) """

""" someday = datetime(2023,1,8,22,22,32,7)
print(someday)
print(someday.min, someday.max, someday.year, someday.month, someday.day, someday.hour, someday.minute)
print(someday.isoformat(), someday.isoweekday(), someday.strftime("%Y-%m-%d %H:%M:%S")) """

now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%A, %d. %B %Y %I: %M%p"))
print("今天是{0:%Y}年{0:%m}月{0:%d}日".format(now))