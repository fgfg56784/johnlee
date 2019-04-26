# print('%s is %s years old' % ('john',29))
# print('%10s%8s' % ('john',29))
# print('%10s%8s' % ('tom',10))
# print('%-10s%-8s' % ('john',29))
# print('%-10s%-8s' % ('tom',10))
# %c
# %o
# %d
# %x
# %e
# %f
print('\033[31;1m{} is {} years old\033[0m'.format('john',20))
print('\033[32;1m{} is {} years old\033[0m'.format(20,'john'))
print('\033[33;1m{1} is {0} years old\033[0m'.format(20,'john'))

