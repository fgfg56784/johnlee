import os 
# import 
# print('start')
# retval = os.fork()
# if retval:
#     print('父进程')
# else:
#     print('子进程')

# for i in range(4):
#     retval = os.fork()
#     if not retval:
#         print('hello john')

ip = ['192.168.1.%s' % es for es in range(1,255)]
cnt_fname = '/tmp/connection_host'
dsc_fname = '/tmp/disconnection_host'
try:
    os.path.exists(cnt_fname)
except FileNotFoundError:
    print('%s 文件不存在' % cnt_fname)
else:
    os.remove(cnt_fname)
try:
    os.path.exists(dsc_fname)
except FileNotFoundError:
    print('%s 文件不存在' % dsc_fname)
else:
    os.remove(dsc_fname)

for count in ip:
    retval1 = os.fork()
    if not retval1:
        cmd = 'ping -c2 -i0.1 %s &> /dev/null'  % count
        ret6 = os.system(cmd)
        if not ret6:
            with open(cnt_fname, 'a') as fobj:
                fobj.write('%s\t已开启\n' % count)
            exit()
        else:
            with open(dsc_fname, 'a') as fobj:
                fobj.write('%s\t未开启\n' % count)
            exit()