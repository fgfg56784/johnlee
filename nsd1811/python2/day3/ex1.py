# from functools import partial
# from operrator import add
# 5! = 5*4!
# 5! = 5*4*3!
# 5! = 5*4*3*2!
# 5! = 5*4*3*2*1!
# from sys import argv
# def func(num):
#     if num == 1:
#         return 1
#
#     return num * func(num - 1)
#
# if __name__ == '__main__':
#     r = func(int(argv[1]))
#     print(r)

# from random import randint
# def qsort(seq):
#     if len(seq) < 2:
#         return seq
#     middle = seq[0]
#     smaller = []
#     larger = []
#
#     for item in seq[1:]:
#         if item < middle:
#             smaller.append(item)
#         else:
#             larger.append(item)
#
#     return qsort(smaller) + [middle] + qsort(larger)
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(10)]
#     print(nums)
#     print(qsort(nums))

# 5!=5*4!
# 5!=5*4*3!......

#递归函数
# def func1(num):
#     if num == 1:
#         return 1
#     return num * func1(num-1)
#
# if __name__ == '__main__':
#     print(func1(3))

#用递归函数对数值,实现快速排序
# from random import randint
#
# def fun2(x):
#     if len(x) < 2:
#         return x
#     else:
#         middle = x[0]
#         smaller = []
#         larger = []
#         for i in x[1:]:
#             if i < middle:
#                 smaller.append(i)
#             else:
#                 larger.append(i)
#         return fun2(smaller) + [middle] + fun2(larger)
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(10)]
#     print(fun2(nums))

#利用生成器返回函数中间值
# import random
# import os
# import time
# import datetime
# file_des = []
# def gen_say():
#     nums = [random.randint(1,100) for i in range(3)]
#     yield nums
#     walk = os.walk('/etc/security')
#     for path, folders, files in walk:
#         for file in files:
#             file_des.append(os.path.join(path, file))
#     yield file_des
#     nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
#     yield nowtime
#     date = datetime.datetime.now()
#     yield date
#     date1 = datetime.timedelta
#     yield date1
#
#     # yield 'hello'
#     # yield 'yahello'
#     # yield 'None'
#
# if __name__ == '__main__':
#     m = gen_say()
#     print(tuple(m))

#内部函数>>>>闭包
import sys
# def fun3(co,say):
#     def cors():
#         return '\033[%s;1m%s\033[0m' % (co, say())
#     return cors()
#
# def hello():
#     return 'say hello'
#
# def hi():
#     return 'yahello!'
#
# if __name__ == '__main__':
#     cmds = {'red':31, 'golden':32, 'yellow':33, 'blue':34, 'purple':35, 'lbule':36, 'white':37, 'green':38}
#     try:
#         choice = cmds[sys.argv[1]]
#     except  (KeyError):
#         print('无此颜色')
#         exit()
#     except (IndexError):
#         print('无输入')
#         exit()
#     else:
#         print(fun3(co=choice, say=hello))

# import getpass
# getpass.getpass('mima: ')

#通用计算器
# def counter(start=0):
#     count = start
#     def incr():
#         nonlocal count
#         count += 1
#         return count
#     return incr()
#
# if __name__ == '__main__':
#     print(counter())
#     print(counter(20))

#查看函数运行时长
# import time
# import random
# def addef(nums):
#     global t1
#     t1 = time.time()
#     if len(nums) < 2:
#         return nums
#     else:
#         middle = nums[0]
#         smaller = []
#         larger = []
#         for i in nums[1:]:
#             if i < middle:
#                 smaller.append(i)
#             else:
#                 larger.append(i)
#         return addef(smaller) + [middle] + addef(larger)
#         # t2 = time.time()
#         # return  t2 - t1
#     # return alist, tc
#
#
# if __name__ == '__main__':
#     n = [random.randint(1, 10000) for i in range(100)]
#     print(addef(n))
#     t2 = time.time()
#     print(t2-t1)
