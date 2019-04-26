# import random

# nums = (random.randint(1,1000) for i in range(100))
# result =filter(lambda x: x%2, nums)
# print(list(result))

# num = (random.randint(1,1000) for i in range(100))
# result2 = map(lambda x: x+2, num)
# print(list(result2))

import os
# import random
import subprocess

# print('start')
# retval = os.fork()
# if retval:
#     print('父进程')
def ping(host):
    # print('start')
    # retval = os.fork()
    if not retval:
        rt = subprocess.run('ping -c2 %s &> /dev/null' % host, shell=True)
        # os.system(ping -c2 host &> /dev/null)
        if rt.returncode == 0:
            print("%s is up" % host)
            # exit()
        else:
            print("%s is down" % host)
            # exit()

if __name__ == "__main__":
    ip_list = ["192.168.1.%s" % i for i in range(1, 255)]
    print()
    for ip1 in ip_list:
        retval = os.fork()
        if not retval:
            ping(ip1)
            exit()