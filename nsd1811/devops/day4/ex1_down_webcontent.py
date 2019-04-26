#! /usr/local/bin/python3
#this script for download the Web Content

from  urllib import request
from sys import argv

def down(url, fname):
    r = request.urlopen(url, fname)
    with open(fname, 'wb') as pic:
        while True:
            data = r.read(4096)
            if not data:
                break
            pic.write(data)
    return fname

if __name__ == '__main__':
    down(argv[1], argv[2])