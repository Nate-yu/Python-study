PM = eval(input("请输入PM2.5数值："))
""" if 0 <= PM < 35:
    print("空气质量优，建议户外运动")
if 35 <= PM <75:
    print("空气质量良，建议适度户外运动")
if PM >=75:
    print("空气污染警告") """

""" if PM >= 75:
    print("空气污染警告")
else:
    print("空气没有污染") """

# print("空气{}污染！".format("存在" if PM>=75 else "没有"))

if 0 <= PM < 35:
    print("空气质量优，建议户外运动")
elif 35 <= PM <75:
    print("空气质量良，建议适度户外运动")
else:
    print("空气污染警告")
