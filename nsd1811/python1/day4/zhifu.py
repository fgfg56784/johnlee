alist = ['john','bob','lucy','lala']
# for i in [1,  2,  3,  4] :
#     print('%s:%s' % (i, alist[i]))

# for i in range(4):
#     print('%s:%s' % (i, alist[i]))

# for i in range(len(alist)):
#     print('%s:%s' % (i, alist[i]))

# for item in enumerate(alist):
#     print('%s,%s' % item)

# for ind, name in enumerate(alist):
#     print('%s:%s' % (ind,name))

print(list(reversed(alist)))
alist.reverse()
print(alist)
print(list(sorted(alist)))
alist.sort()
print(alist)
max(1,2,3,4)
min(1,2,3,4)
sum(1,2,3,4)

