import wget 
import requests
import os
import hashlib

def has_pass_check(ver_fname, ver_url):
    with open(ver_fname) as fobj:
        local_ver = fobj.read()
    remote_ver = requests.get(ver_url)
    if local_ver.strip() != remote_ver.text.strip():
        return True
    return False

def has_error(gz_url):
    wget.download(gz_url)
    tar

if __name__ == "__main__":
    ver_url = 'http://192.168.4.4/deploy/live_ver'
    ver_fname = '/var/www/download/live_ver'
    if  not has_pass_check(ver_fname, ver_url):
        print('版本一致')
        exit(1)
    r = requests.get(ver_url)
    ver = r.text.strip()
    gz_url = 'http://192.168.4.4/deploy/myweb-%s.tar.gz' % ver

    if not has_error(gz_url):
        print()
        exit(2)