#! /usr/local/bin/python3

import threading
import os
import subprocess

class PingIp:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        ret = subprocess.run('ping -c2  %s &> /dev/null' % self.host, shell=True )
        if ret.returncode == 0:
            print("%s is up" % self.host)

if __name__ == "__main__":
    iplist = ['176.121.202.%s' % i for i in range(1,255)]
    for ip in iplist:
        r1 = PingIp(ip)
        r1 = threading.Thread(target=PingIp(ip))
        r1.start()