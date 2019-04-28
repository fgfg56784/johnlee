#!/usr/local/bin/python3
import requests
import os 
import wget
import hashlib
import tarfile

def has_new_ver(ver_fname, ver_url):
    if not os.path.isfile(ver_fname):
        return True

    with open(ver_fname) as fobj:
        local_file = fobj.read()
    r = requests.get(ver_url)
    remote_file = r.text
    if local_file != remote_file:
        return True
    return False

def has_error(fname, md5_url):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    r = requests.get(md5_url)
    if m.hexdigest()  == r.text.strip():
        return True

    return False

def deploy(fname):
    deploy_dir = '/var/www/deploy'

    tar = tarfile.open(fname, 'r:gz')
    tar.extractall(deploy_dir)
    tar.close()
    
    fname = os.path.basename(fname)
    fname = fname.replace('.tar.gz', '')
    file_path = os.path.join(deploy_dir, fname)

    link_path = '/var/www/html/nsd1811'
    if os.path.islink(link_path):
        os.remove(link_path)

    os.symlink(file_path, link_path)

if __name__ == "__main__":
    #检查是否有新版本
    app_dir = '/var/www/download'
    ver_fname = '/var/www/download/live_ver'
    ver_url = 'http://192.168.4.4/deploy/live_ver'
    
    if not has_new_ver(ver_fname, ver_url):
        print('没有发现新版本')
        exit(1)
    # print('OK')

    r = requests.get(ver_url)
    ver = r.text.strip()
    app_url = 'http://192.168.4.4/deploy/packages/myweb-%s.tar.gz' % ver
    wget.download(app_url, app_dir)
    app_fname = app_url.split('/')[-1]
    fname = os.path.join(app_dir, app_fname)

    md5_url  = app_url + '.md5'
    # print(has_error(fname, md5_url))
    if not has_error(fname, md5_url):
        print('文件损坏,请重试')
        os.remove(app_fname)
        exit(2)
    print('\nOK')
    
    deploy(fname)
    with open(ver_fname, 'w') as fobj:
        fobj.write(r.text)
    





    

    
    

    
