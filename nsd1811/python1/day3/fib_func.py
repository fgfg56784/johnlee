# def gen_list():
#     fib = [0,1]
#     n = int(input('请输入:'))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     # print(fib)
#     return fib  #函数的结果应该通过return进行返回,否则返回NONE
# mylist = gen_list()
# print(mylist)
# new_list = [ 10 + i for i in mylist]
# print(new_list)
# def gen_list(n=10):
#     fib = [0, 1]
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     return fib
# mylist = gen_list()
# print(mylist)
# num = int(input('长度:'))
# print(gen_list(num))
# print('哈哈')
# def gen_list():
#     fib = [0,1]
#     for i in range(2,10):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# my_list = gen_list()
# print(my_list)
# def gen_list():
#     fib = [0,1]
#     num = int(input('please enter the langth: '))
#     for i in range(0,num-2):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# my_list = gen_list()
# print(my_list)
import sys
def gen_list(num):
    fib = [0,1]
    for i in range(0,num-2):
        fib.append(fib[-1]+fib[-2])
    return fib
my_list = gen_list(int(sys.argv[1]))
print(my_list)

# def gen_list():
#     fib = [0,1]
#     n = int(input('请输入:'))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     # print(fib)
#     return fib  #函数的结果应该通过return进行返回,否则返回NONE
# mylist = gen_list()
# print(mylist)
# new_list = [ 10 + i for i in mylist]
# print(new_list)
# def gen_list(n=10):
#     fib = [0, 1]
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     return fib
# mylist = gen_list()
# print(mylist)
# num = int(input('长度:'))
# print(gen_list(num))
# print('哈哈')
# def gen_list():
#     fib = [0,1]
#     for i in range(2,10):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# my_list = gen_list()
# print(my_list)
# def gen_list():
#     fib = [0,1]
#     num = int(input('please enter the langth: '))
#     for i in range(0,num-2):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# my_list = gen_list()
# print(my_list)
import sys
def gen_list(num):
    fib = [0,1]
    for i in range(0,num-2):
        fib.append(fib[-1]+fib[-2])
    return fib
my_list = gen_list(int(sys.argv[1]))
print(my_list)
