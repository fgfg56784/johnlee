import os
import time

print("start")
retval = os.fork()
if retval:
    print('父进程')
    result = os.waitpid(-1, 0)
    print(result)

else:
    print('子进程')
    time.sleep(10)
    exit()

time.sleep(15)
print('Done')

