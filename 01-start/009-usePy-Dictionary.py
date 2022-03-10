# 字典Dictionary
# 1. 特点
#   查询快、可以存任何类型数据
#   键必须不可变,所以可以用数字,字符串或元组充当,值可以是任意数据类型
# 2. 定义
d = {'name': 'tom', 'age': 19}
d = {'Tom': 18, 3.14: 'pi', (1,): [1, 2, 3]}
print('键必须不可变,所以可以用数字,字符串或元组充当', d)

# 3. 访问字典
print('字典名[键]---d[\'Tom\']                  ', d['Tom'])
print('字典名.get(键)--d.get(\'Tom\')           ', d.get('Tom'))
print('通过 in 来判断键是否存在                   ', 'Tom' in d)
print('通过 in 来判断键是否存在                   ', 'tom' in d)
print('用get()方法访问,如果不存在返回None          ', d.get('class'))
print('items()方法可以返回可遍历的(键, 值) 元组列表  ', d.items())

# 4. 修改字典
# 使用字典名[键] = 值的形式添加或修改字典
d['class'] = 'javascript'
print('如果字典中没有对应的键则是添加                ', d)
d['class'] = 'python'
print('如果字典中有对应的键则是修改                  ', d)

# 5. 删除字典
# 5.1 用del 字典名[键]删除单一元素
del d['class']
print('', d)

# 5.2 用del 字典名删除整个字典
# del d # NameError: name 'd' is not defined
# print('NameError: name 'd' is not defined', d) #NameError: name 'd' is not defined

# 5.3 用字典名.clear()清空字典
d.clear()
print('用clear()方法清空字典', d)
