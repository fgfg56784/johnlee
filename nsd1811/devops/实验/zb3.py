#! /usr/local/bin/python3

import os

def wt_child():
    result = os.waitpid(-1,1) 
    print('child pid is %s' % result[0])

if __name__ == "__main__":
    do = ['%s' % i  for i in range(1,101)]
    for i in do:
        pid = os.fork()
        if pid:
            print('haha')
        else:
            print('xixi')
            exit()
