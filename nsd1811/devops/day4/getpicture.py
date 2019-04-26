#!/usr/local/bin/python3
from urllib import request
import os
import re

# class PictureDown:
    # def __init__(self):
def geturl(url, url_file):
    web_urls = request.urlopen(url)
    with open(url_file, 'wb') as fobj:
        fobj.write(web_urls.read())

def getcontent(patt, url_file, headers, dir, encoding = 'utf8' ):
    pics = []
    
    if not os.path.exists(f'/tmp/{dir}'):
            os.mkdir(f'/tmp/{dir}')
    with open(url_file, encoding = encoding) as robj:
        for line in robj:
            m = re.search(patt, line)
            if m:
                pic_url = m.group().split('//')[1]
                full_url = 'http://' + pic_url
                pics.append(full_url)
    # print(pics)
    # for i in pics:
    #     picname = i.split('/')[-1]
    #     # obj = request.Request(i, headers=headers)
    #     # content = request.urlopen(obj)
    #     content = request.urlopen(i)

    #     stor = os.path.join(f'/tmp/{dir}', picname)
    #     with open(stor, 'wb') as cobj:
    #         cobj.write(content.read())
    return pics

if __name__ == "__main__":
    headers = {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    patt = '(http:)?//[\w/.-]+\.(jpg|jpeg|gif|png)'
    url = input('地址: ').strip()
    dir = url.split('.')[1]
    url_file = input('存放路径: ')
    if os.path.exists(url_file):
        print('文件已存在')
        exit(2)
    geturl(url = url, url_file = url_file)
    pic = getcontent(patt = patt, url_file = url_file, headers = headers, dir = dir)

    for i in pic:
        picname = i.split('/')[-1]
        stor = os.path.join(f'/tmp/{dir}', picname)
        geturl(url = pic, url_file = stor)
        # stor = os.path.join(f'/tmp/{dir}', picname)
        # with open(stor, 'wb') as cobj:
        #     cobj.write(content.read())
        
    

