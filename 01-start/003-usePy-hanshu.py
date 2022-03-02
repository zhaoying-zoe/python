# 1. 函数的定义
def sum():
    print('函数的定义', 12344)

# 函数的调用
sum()


# 2.1 必选参数
def fn1(num1, num2):
    print('参数位置传递', num1 + 100 + num2)

# 参数位置传递
fn1(1, 2)


# 2.2 必选参数的使用
def fn2(num1, num2):
    print('参数关键字传递', num1 + num2)

# 参数关键字传递
fn2(num1=2, num2=2)


# 2.3 默认参数
def fn3(num1, num2, num3=100):
    if num3 == 100:
        print('默认参数: num3=100', num1 + num2 + num3)
    else:
        print('调用函数时传递num3', num1 + num2 + num3)

# 不传递第三个参数
fn3(1, 2)
fn3(1, 2, 3)


# 加了星号*的参数会以元组(tuple)的形式导入用来存放所有未命名的参数
# 这个星号*的作用就是把调用时未命名的参数装入到元组中,不要和其他语言中*作用混淆
def fn4(num1, num2, *num):
    print(num1, num2)
    print('<class \'tuple\'> 表示元组', type(num), num)
    result = 0
    for n in num:
        result += n
    print(result)

fn4(1, 2, 3, 4)


#
def fn5(num1, unm2, *num):
    if num:
        print('函数调用时传递元组', num1, unm2, num)
    else:
        print('函数调用时不传递元组', num1, unm2)

l = (3, 4)
# *l 表示将元组扩展开（类似js的...）
fn5(1, 2, *l)
# 如果可变参数不传值, 则是一个空元组
fn5(1, 2)