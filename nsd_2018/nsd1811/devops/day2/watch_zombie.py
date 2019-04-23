# import os
# import time 

# print('start...')
# retval = os.fork()
# if retval:
#     print('父进程')
#     time.sleep(60)
# else:
#     print('子进程')
#     time.sleep(15)
#     exit() #完全退出子进程

# print('Done')

import os
import time

class ZbWatch:
    def watch_zb(self):
        print('start')
        retval = os.fork()
        if retval:
            print('父进程')
            time.sleep(60)
        else:
            print('子进程')
            time.sleep(5)
            exit()
        print('done')

if __name__ == "__main__":
    f1 = ZbWatch()
    f1.watch_zb()