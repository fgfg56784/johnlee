import paramiko
import sys
import os
import threading
from getpass import getpass

def ssh_agent(host = None, user = None, passwd = None, port = 22, command = None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy
    ssh.connect(host, username = user, password = passwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    error = stderr.read()
    if stdout:
        print(f'OUT:\n{out}')
    if stderr:
        print(f"ERROR:\n{error}")
    
    ssh.close()

if __name__ == "__main__":
    if sys.argv != 3:
        print(f"Usage: {sys.argv[0]} IPfile 'command'")
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print(f'No such file: {sys.argv[1]}')
        exit(2)
    cmd = sys.argv[2]
    with open(sys.argv[1]) as fobj:
        

    user = 'root'
    pwd = getpass('密码: ')
    ssh_agent()