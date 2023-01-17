fname = input("请输入要写入的文件：")
fo = open(fname,"w+")
ls = ["abc","def","ghi"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()
