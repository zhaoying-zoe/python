# 1. 集合Set
# 2. 定义集合
# 2.1 使用 变量 = {} 的方法
set1 = {1, 2, 3, 4, 5}
print('变量 = {}                                                 ', set1)
# 2.2 使用 变量.set() 方法
# 2.2.1 set中传入 字符串
set2 = set('hello world')
print('set中传入 字符串 \'hello world\'                           ', set2)
# 2.2.2 set中传入 元组   元组中的每一项 为集合的键
set2 = set(('html', 'python', 'javascript'))
print('set中传入 元组(\'html\', \'python\', \'javascript\')       ', set2)
# 2.2.3 set中传入 列表   列表中的每一项 为集合的键
set2 = set(['html', 'python', 'javascript'])
print('set中传入 列表[\'html\', \'python\', \'javascript\']       ', set2)
# 2.2.4 定义空集合,因为{}用来定义空字典,所以空集合用set()来创建
set3 = set()
print('set3 = set()', set3)
print('查看set类型', type(set3))
# 定义集合的注意点

# 由于集合的键不重复,所以在定义时,如果有重复的键将会被去除
s = {'Tom', 'Amy', 'Tom'}
print(s)  # {'Amy', 'Tom'}

# 和定义字典一样,集合的键必须不可变
s = {'Tom', 3.14, (1, 2)}
print(s)

# 集合添加键
s.add('to mmmm')
print('s.add(\'to mmmm\')               ', s)

# 集合删除键
s.remove('to mmmm')
print('s.remove(\'to mmmm\')            ', s)

# 使用in先判断集合中是否有相应的键
print('tom' in s)
print('Tom' in s)
