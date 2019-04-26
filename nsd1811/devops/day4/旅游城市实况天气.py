#! /usr/local/bin/python3
import requests
import json
import os

def sk(skurl):
    sktq = requests.get(skurl)
    sktq.encoding =  'utf8'
    info = sktq.json()['weatherinfo']
    for key in info:
        print('%s: %s' % (key, info[key]))

def zs(zsurl):
    kqzs = requests.get(zsurl)
    kqzs.encoding = 'utf8'
    info = kqzs.json()['zs']
    for key in info:
        print(f"{key}: {info[key]}")

if __name__ == "__main__":
    skurl = 'http://www.weather.com.cn/data/sk'
    zsurl = 'http://www.weather.com.cn/data/zs'
    fname = '/var/ftp/nsd_2018/nsd1811/devops/day4/cs.txt'
    cdict = {}
    with open(fname) as fobj:
        for line in fobj:
            clist = line.split('=')
            cdict[clist[1].strip()] = clist[0]
        
    cs = input('查看的城市: ')
    skurl = os.path.join(skurl, cdict[cs]) + '.html'
    zsurl = os.path.join(zsurl, cdict[cs]) + '.html'
    # print(skurl,'\n',zsurl)
    sk(skurl)
    zs(zsurl)