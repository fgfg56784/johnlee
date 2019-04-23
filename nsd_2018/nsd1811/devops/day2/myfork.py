import os
# print('start')
# os.fork()
# print('hello')
# print('salaba')

# print('BEGIN')
# retval = os.fork()
# if retval:
#     print('yahello')
# else:
#     print('你好')
# print('both')

# retval = os.fork()
# for i in range(3):
#     retval = os.fork()
#     if not retval:
#         print('hello john')
        # exit()

ip  = [ '192.168.1.%s' % i for i in range(1,255)]
# retval = os.fork()
# cmd = 'ping -c2 -i0.1 192.168.1.1 &> /dev/null'
# ret1 = os.system(cmd)
# print(ret1)
for count in ip:
    retval = os.fork()
    if not retval:
        cmd = 'ping -c2 -i0.1 %s &>/dev/null' % count
        ret1 = os.system(cmd)
        if not ret1:
            print('%s 已开启' % count)
            exit()
        else:
            print('%s 未开启' % count)
            exit()