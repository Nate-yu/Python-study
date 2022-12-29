## 开始

`> python`进入python环境开始写程序

`>>> exit()`退出环境

`> python xxx.py`命令行执行python源文件

### pip命令

`pip list` 列出匹配管理的包

`pip install 包名` 安装

`pip uninstall 包名` 卸载

`pip -V`或`pip -version` 查看版本

### 初始笔记

1. `print()`函数中，参数end代表换行符，可以改变，如：`print(a, end=',')`，表示不换行，且用逗号替换
2. `print("{:.2f}".format(area))`表示area保留两位小数输出，`{}`为占位符，`format()`函数中的参数为需要格式化的对象
3. 数组相关：

```python
print("{}同学".format(name)) # 按格式输出完整名字
print("{}哥哥".format(name[0])) # 输出第一个字符
print("{}弟弟".format(name[1:])) # 从第二个字符开始输出直至末尾
```

4. 日期相关：

```python
from datetime import datetime
now = datetime.now() # 获得当前日期和时间信息
print(now)
now.strftime("%x") # 输出其中的日期部分
now.strftime("%X") # 输出其中的时间部分
```
