import os
import time
import pickle

ip  = [ '192.168.1.%s' % i for i in range(1,255)]
# retval = os.fork()
# cmd = 'ping -c2 -i0.1 192.168.1.1 &> /dev/null'
# ret1 = os.system(cmd)
# print(ret1)
up_list = []
down_list= []
for count in ip:
    retval = os.fork()
    cmd = 'ping -c2  %s &>/dev/null' % count
    # print('haha')
    if not retval:
        ret1 = os.system(cmd)
        if not ret1:
            up_list.append(count)
            # print('%s 已开启' % count)
            # exit()
            exit()
        else:
            # print('%s 未开启' % count)
            down_list.append(count)
            exit()
print('开启的机器: %s' % up_list)
print('未开启的机器: %s'% down_list)