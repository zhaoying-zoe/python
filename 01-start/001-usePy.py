# 1. 标识符：可以理解为变量名
#   大小写英文、数字、_的组合；
#   不能用数字开头
#   区分大小写

# 2. 关键字
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 3. 注释
# 单行注释用一个 #
# 多行注释用三个 ''' 或 三个 """
'''
    这里是注释
'''
"""
    这里是注释
"""

# 4. 行与缩进
#   Python用缩进来表示代码块
#   缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
#   代码块内的缩进不一致会导致报错
if True:
    print('ok1')
    print('ok2')
else:
        print('ng1')
        print('ng2')

# 5. 多行语句
#   Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠\来实现多行语句
var1 = 1 + \
       2 + \
       3
print(1+
      1+
      1, var1)
#   在 [], {}, 或 () 中的多行语句，不需要使用反斜杠\
items = ['item1', 'item2',
         'item3', 'item4']
print(items)

# 6. 检查数据类型 type() 用sys.getsizeof来计算变量在内存中的字节数
import sys
print(type(items), sys.getsizeof(items))

# 7. 数据类型
#   None
a = None
print(a)

print(not False)

for item in items:
    print('item', item)
else:
    print('end')

# from PyQt5 import QtWidgets,QtGui,QtCore
# print(QtWidgets)

# https://www.bilibili.com/bangumi/play/ss28006/?from=search&seid=752620588334199542&spm_id_from=333.337.0.0