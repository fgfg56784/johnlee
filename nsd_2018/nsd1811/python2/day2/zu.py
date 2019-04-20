# def func1(*args):
#     print(args)
#
# if __name__ == '__main__':
#     func1()
#     func1('ha')
#     func1('ha', 'xi')
#
# def func2(**kwargs):
#     print(kwargs)
#
# if __name__ == '__main__':
#     func2(name='xi', say='ha')
#     func2(name='john', age=12)
#     func2()

# def info(name, age):
#     print('%s:%s' % (name, age))
#
# if __name__ == '__main__':
#     info(**{'name':'tom', 'age':23})
#     info(name='tom', age=23)

# def pstat(n):
#     print('*' * n)
#
# if __name__ == '__main__':
#     pstat(30)

# def add(x, y):
#     return x + y
#
# if __name__ == '__main__':
#     print(add(15, 5))
#     myadd = lambda x, y: x+y
#     print(myadd(10, 5))

from random import randint
from time import sleep
def func1(x):
    return x % 2

if __name__ == '__main__':
    nums1 = [randint(1, 100) for i in range(10)]
    print(nums1)
    result1 = filter(func1, nums1)
    print(list(result1))

    result2 = filter(lambda x: x % 2, nums1)
    print(list(result2))

from random import randint

def func2(x):
    return x + 2

if __name__ == '__main__':
    nums2 = [randint(1,100) for i in range(10)]
    result3 = map(func2, nums2)
    print(list(result3))

    result4 = map(lambda x: x+2, nums2)
    print(list(result4))