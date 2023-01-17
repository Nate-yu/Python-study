textFile = open("7.1.txt","rt",encoding='utf-8') # 只读文本文件模式
print(textFile.readline())
textFile.close()

textFile = open("7.1.txt","rb") # 只读二进制文件模式
print(textFile.readline())
textFile.close()