# import os
# print(os.getcwd())
# print(os.listdir('/etc'))
# os.mkdir('/root/omak1')
# os.chdir('/root/omak1')
# os.mknod('test.txt')
# print(os.getcwd())
# os.makedirs('ha/xi/ho/he')
# os.symlink('/etc/hosts', './hosts')
# print(os.listdir('/root/omak1/'))
# os.unlink('./hosts')
# os.remove('test.txt')
# print(os.listdir('/root/omak1'))
import os
# print(os.path.isfile('/etc/hosts'))
# print(os.path.isdir('/etc'))
# print(os.path.islink('/iso'))
# print(os.path.exists('/haha'))
# print(os.path.exists('/root'))
# print(os.path.getsize('/root/.ssh'))
# print(os.path.ismount('/var'))
# print(os.path.split('/etc/sysconfig/network-scripts'))
# print(os.path.join('/etc/sysconfig','network'))

# import pickle, subprocess
# adict = dict(['ab',('name','john'),('age',23)])
# print(adict)
# fname = '/root/adict'
# with open(fname, 'wb') as f:
#     pickle.dump(adict, f)
#
# n = subprocess.run('cat /root/adict', shell=True)
# print(n)
#
# with open(fname, 'rb') as c:
#     d = pickle.load(c)
# print(d)

# def func1(*args):
#     print(args)
#
# if __name__ == '__main__':
#     func1('ha','xi')

# def add(**args):
#     print(args)
#
# if __name__ == '__main__':
#     add(ab='ha', name='jj')
#
# import random
# def add(x):
#     return x % 2
#
# if __name__ == '__main__':
#     nums = [random.randint(1,100) for i in range(10)]
#     r = filter(add, nums)
#     print(list(r))

# if __name__ == '__main__':
#     nums = [random.randint(1,100) for i in range(10)]
#     r = filter(lambda x:x % 2, nums)
#     print(list(r))
#     c = map(lambda x:x+2, nums)
#     print(list(c))
# def foo(x):
#     return x+2
#
# if __name__ == '__main__':
#     nums = [random.randint(1,100) for i in range(2)]
#     c = map(foo, nums)
#     print(list(c))

