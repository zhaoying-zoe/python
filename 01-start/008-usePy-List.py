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