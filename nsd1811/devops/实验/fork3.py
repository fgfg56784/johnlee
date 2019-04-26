#! /usr/local/bin/python3

import os
import subprocess

def ping(host):
    for i in host:
        retval = os.fork()
        if not retval:
            ipret = subprocess.run('ping -c2 %s &>/dev/null' % i, shell=True)
            if ipret.returncode == 0:
                print('%s is up' % i)
                exit()
            else:
                # print('%s is down' % i)
                exit()

if __name__ == "__main__":
    host = ['176.121.202.%s' % i for i in range(1,255)]
    ping(host)