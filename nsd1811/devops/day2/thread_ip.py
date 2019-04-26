# import threading
# # import time
# import subprocess
# class Ping:    #把普通函数改为oop的形式 
#     def __init__(self, host):    #把ip绑定到实例中
#         self.host = host

#     def __call__(self):   #添加oop 调用函数  把ping_th(ip)  ---->  __call__(self)
#         jg = subprocess.run('ping -c2 %s &> /dev/null' % self.host, shell = True)
#         if jg.returncode == 0:
#             print('%s is up' % self.host)
#         else:
#             print('%s is down' % self.host)

# if __name__ == '__main__':  
#     iplist = ['176.121.202.%s' % i for i in range(1, 255)]
#     for ip in iplist:
#         r1 = Ping(ip)
#         r1 = threading.Thread(target=Ping(ip))    #把   target=ping_th, args=ip 改为了现在这样
#     # for ip in iplist:
#         r1.start()

# from random import randint
# def  sub(x):
#     # rc = x % 2
#     # if rc:
#     return x % 2

# if __name__ == "__main__":
#     nums = [randint(1,100) for i in range(10)]
#     for i in nums:
#         if sub(i):
#             print(i)
#     t1 = filter(sub, nums)
#     print(list(t1))

# import threading
# # import time
# import subprocess
# class Ping:    #把普通函数改为oop的形式 
#     def __init__(self, host):    #把ip绑定到实例中
#         self.host = host

#     def __call__(self):   #添加oop 调用函数  把ping_th(ip)  ---->  __call__(self)
#         jg = subprocess.run('ping -c2 %s &> /dev/null' % self.host, shell = True)
#         if jg.returncode == 0:
#             print('%s is up' % self.host)
#         else:
#             print('%s is down' % self.host)

# if __name__ == '__main__':  
#     iplist = ['176.121.202.%s' % i for i in range(1, 255)]
#     for ip in iplist:
#         r1 = Ping(ip)
#         r1 = threading.Thread(target=Ping(ip))    #把   target=ping_th, args=ip 改为了现在这样
#     # for ip in iplist:
#         r1.start()

# from random import randint
# def  sub(x):
#     # rc = x % 2
#     # if rc:
#     return x % 2

# if __name__ == "__main__":
#     nums = [randint(1,100) for i in range(10)]
#     for i in nums:
#         if sub(i):
#             print(i)
#     t1 = filter(sub, nums)
#     print(list(t1))

import subprocess
import threading

class PingIp:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        multithread = subprocess.run('ping -c2 %s &> /dev/null' % self.host, shell = True)
        if multithread.returncode == 0:
            print('%s is up' % self.host)
        else:
            print('%s is down' % self.host)

if __name__ == "__main__":
    iplist = ['176.121.202.%s' % i for i in range(1,255)]
    for ip in iplist:
        r1 = PingIp(ip)
        r1 = threading.Thread(target=PingIp(ip))
    # for ip in iplist:   
        r1.start()
