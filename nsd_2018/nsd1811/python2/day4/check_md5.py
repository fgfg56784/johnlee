import hashlib
import os
# import time
from sys import argv
def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            line = fobj.read(4096)
            if not line:
                break
            m.update(line)
    return m.hexdigest()
        
if __name__ == "__main__":
    if not os.path.isfile(argv[0]):
        print('no such file or it\'s not a file')
        exit()
    else:
        fname = argv[0]
        print(check_md5(fname))
