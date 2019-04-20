# import hashlib, os
# from sys import argv
#
# def check_file(fname):
#     m1 = hashlib.md5()
#     with open(fname, 'rb') as fobj:
#         while True:
#             line = fobj.read(4096)
#             if not line:
#                 break
#             m1.update(line)
#     return m1.hexdigest()
#
#
# if __name__ == '__main__':
#     fname = '%s' % argv[0]
#     if not os.path.isfile(fname):
#         print('no such file')
#     else:
#         print(check_file(fname))

# import tarfile
# import os
# tar1 = tarfile.open('/tmp/mytest.tar.gz', 'w:gz')
# tar1.add('/etc/hosts')
# os.chdir('/etc')
# tar1.add('security')
# tar1.close()
#
# os.mkdir('/root/demo3')
# os.chdir('/root/demo3')
# tar2 = tarfile.open('/tmp/mytest.tar.gz', 'r:gz')
# tar2.extractall('./')
# tar2.close()

#生成md5值的函数
import hashlib
import os
import sys
def check_md5():
    fname = '%s' % sys.argv[1]
    h = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            line = fobj.read(4096)
            if not line:
                break
            h.update(line)
    return h.hexdigest()

if __name__ == '__main__':
    print(check_md5())


