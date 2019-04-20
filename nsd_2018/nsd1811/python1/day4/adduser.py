import sys, subprocess
from randpass2 import gen_pass

def user(name, password, fname):
    info = '''用户信息:
用户名:%s
密码:%s''' % (name, password)
    
    subprocess.run('useradd %s' % name, shell=True)
    subprocess.run('echo %s |passwd --stdin %s'  % (password, name), shell=True)
    with open(fname, 'a')  as f:
        f.writelines(info)
if __name__ == "__main__":
    username = sys.argv[1]
    fname = '/tmp/usr.txt'
    psw = gen_pass()
    user(username, psw, fname)
