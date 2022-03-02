
# 1 数据类型
# 数据类型的用处：区分在内存中的储存空间
import sys
# 2 使用type()查看数据类型
# 3 使用sys.getsizeof() 来计算变量在内存中的字节数

a = 1
b = '1'
print('a的数据类型', type(a))  # <class 'int'> 28
print('b的数据类型', type(a))  # <class 'int'> 28
print('a在内存中的字节数', sys.getsizeof(a))  # <class 'int'> 28
print('b在内存中的字节数', sys.getsizeof(b))  # <class 'str'> 50

print(1 + 1)  # 数字加减
print('1' + '1')  # 字符串拼接

print('----------------------------')

# 数字Number
# 十进制
num1 = 3333
print('十进制', num1)
# 十六进制 0x前缀和0-9，a-f表示
num2 = 0xa
print('十六进制', num2)
# 浮点型
num3 = 1.1
print('浮点型', num3)
# 科学计数法表示
num4 = 3e10
print('学计数法表示', num4)
# 复数
num5 = 1+2j
print('复数', num5)

# 数值类型的转换
# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

x = '4444'
y = '4444.4'
print('将x转换为整数', int(x))  # x只能为整数字符串
print('将y装换为浮点数', float(y))  # y可以为整数字符串或浮点字符串
z = 3
o = 2
print('将z转为复数', complex(z))
print('将z和o转为复数', complex(z, o))
