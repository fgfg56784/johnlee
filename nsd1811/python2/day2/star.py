# hi = 'hello world'  #全局;变量
# x = 10
#
# def pstar():
#     print('*' * 20)
#
# def foo():  # 如果局部变量有与全局变量的一样, 它会将全局变量暂时遮盖
#     x = 2323
#     print(x)
#
# def bar():
#     global x  #声明使用的是全局变量
#     x = 100   #修改全局变量
#     print(x)
#
# if __name__ == '__main__':
#     pstar()
#     foo()
#     # bar()
#
# print(x)
from sys import argv
from functools import partial
def add(a, b, c, d, e):
    return a+b+c+d+e

myadd = partial(add, 10, 20, 30, 40)

if __name__ == '__main__':
    print(myadd(int(argv[1])))