from  urllib  import  request, error
import re
import os
# import sys
# import ex1_down_webcontent

def cut(fname, patt, encoding='utf8'):
    cpatt = re.compile(patt)
    result = []
    with open(fname, encoding=encoding) as obj:
        for i in obj:
            data = cpatt.search(i)
            if data:                
                result.append(data.group())
    return result

def download(url, fname):
    r = request.urlopen(url)
    with open(fname, 'wb') as pic:
        while True:
            data = r.read(4096)
            if not data:
                break
            pic.write(data)

if __name__ == "__main__":
    patt = 'http://[\w/.-]+\.(jpg|bng|jpeg|gif)'

    fname = '/tmp/123.html'
    url163 = 'https://www.163.com/'
    download(url163, fname)
    url = cut(fname, patt, 'gbk')
    imgdir = '/tmp/1631'
    if not os.path.exists(imgdir):
        os.mkdir(imgdir) 

    for i in url:
        picname = i.split('/')[-1]
        dst_name = os.path.join(imgdir, picname)
        try:
            download(i, dst_name)
        except error.HTTPError:
            pass
    