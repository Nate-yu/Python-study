# 月球上物体的重量是在地球上的16.5%，假如你在地球上每年增长0.5kg，编写程序输出未来10年你这地球和月球上的体重情况
earthWeight = eval(input("输入在地球上的初始体重：")) # 利用eval()函数将输入的字符串转换为数字
moonWeight = earthWeight * 0.165
for i in range(10):
    earthWeight = earthWeight + 0.5
    moonWeight = earthWeight * 0.165
    print("第{0}年你的地球体重为：{1:.2f}kg，你的月球体重为：{2:.2f}kg".format(i+1,earthWeight,moonWeight)) # 利用format()方法将输出的数据格式化
    
