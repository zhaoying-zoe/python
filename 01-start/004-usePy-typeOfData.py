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

# 字符串的用法
# 1.
var1 = 'abc'
var2 = "hello"
var3 = "I\'am ok, I said \"ok\""
print(var1)
print(var2)
print('如果要同时包含单引号\'和双引号\"\",用转义字符\\来标识', var3)
# str(x),将x转换为字符串
str1 = 'i am amy'
print('str(x),将x转换为字符串', str(str1))

nonea = None
print(nonea, None)

# 列表
language = ['python', 'javascript', 'java', 'css']
print('language', language)
print('正数访问元素language[1]', language[1])
print('倒数访问元素language[-2]', language[-2])
# 获取列表的长度len()
print('获取列表的长度len()', len(language))
# 如果为空列表,则length为0
length0 = []
print('如果为空列表,则length为0', len(length0))

# 截取列表,列表[起始索引:结束索引],包含起始索引元素,但是不包含结束索引元素
print('截取数组: 列表[起始索引:结束索引]', language[0:1])

# 列表尾部追加元素 列表.append()
language.append('go')
print('列表尾部追加元素 列表.append()', language)

# 列表指定位置追加元素 列表.insert(索引, 添加的元素)
language.insert(0, 'html')
print('列表指定位置追加元素 列表.insert(索引, 添加的元素)', language)

# 修改列表 列表[index]
language[0] = 'php'
print('修改列表的某一项', language)

# 删除列表 pop(index)
language.pop()
print('删除列表 pop() 删除末尾的元素', language)
language.pop(0)
print('删除列表 pop(index) 删除指定索引的元素', language)
# 删除列表自身 del
del language
if language:
    print(language)  # name 'language' is not defined
else:
    print('删除language列表成功')