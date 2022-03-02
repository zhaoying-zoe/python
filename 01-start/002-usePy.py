import logging
# 创建日志文件,将打印的信息存入到日志文件
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.info('+++++++++++++++++++++++')
logging.warning('+++++++++++++++++++++++')
logging.debug('+++++++++++++++++++++++')
# print(logging)

def sum():
    num1 = 1+1+1+1+1+1
    # num2 = input(1+1)
    logging.info(num1)
    print(num1)
    # print(num2)
    # return num1 + num2
sum()