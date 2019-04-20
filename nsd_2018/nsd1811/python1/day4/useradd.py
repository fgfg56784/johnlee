import sys, random, subprocess
from string import ascii_letters, digits
first_list = ascii_letters + '_'
all_list = first_list + digits

def gen_pass():
    word = ''
    for i in range(8):
        word += random.choice(all_list)
    return word

def adduser(user, passwd, fname):
    info = '''用户信息:
用户名: %s
密码: %s
''' % (user, passwd)

    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run('echo %s |passwd --stdin %s' % (passwd, user), shell=True)
    with open(fname, 'a') as f:
        f.write(info)

if __name__ == "__main__":
    username = sys.argv[1]
    psw = gen_pass()
    file_name = '/tmp/users.txt'
    adduser(username, psw, file_name)