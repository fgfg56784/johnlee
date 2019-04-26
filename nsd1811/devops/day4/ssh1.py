#! /usr/local/bin/python3

import paramiko
from getpass import getpass
import sys
import os
import threading

def ssh(host=None, user='root', passwd=None, port=22, command=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=pwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    error = stderr.read()
    
    if out:
        print('[%s] \033[33;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if error:
        print('[%s] \033[31;1mERROR\033[0m]:\n%s' % (host, error.decode()))

    ssh.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s ipfile 'command'" % sys.argv[0])
        exit(1)
    ipfile = sys.argv[1]
    if not os.path.isfile(ipfile):
        print('No such file: ', ipfile)
        exit(2)
    pwd = getpass('密码: ')
    cmd = sys.argv[2]
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
    # host = input('主机名: ')
    # user = input('登录用户: ')
   
    # cmd = input('操作命令: ')
            # ssh(host=ip,user='root' ,pwd='a', cmd=sys.argv[2])
            r = threading.Thread(target=ssh, args=(ip,), kwargs={'user': 'root', 'passwd': pwd, 'command': cmd})
            r.start()