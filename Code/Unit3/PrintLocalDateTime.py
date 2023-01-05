from datetime import datetime
now = datetime.now() # 获得当前日期和时间信息
print(now)
now.strftime("%x") # 输出其中的日期部分
now.strftime("%X") # 输出其中的时间部分