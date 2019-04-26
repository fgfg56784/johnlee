from urllib import request
from sys import argv

def download(url, fname):
    r = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = r.read(4096)
            if not data:
                break
            fobj.write(data)
    return fname
    
if __name__ == "__main__":
    # fname = '/tmp/163.html'
    # url = 'https://www.163.com/
    download(argv[1], argv[2])