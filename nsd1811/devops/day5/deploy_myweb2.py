import wget 
import requests
import os
import hashlib
import tarfile

def has_pass_check(ver_fname, ver_url):
    if not os.path.isfile(ver_fname):
        return True

    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    remote_ver = requests.get(ver_url)
    if local_ver.strip() != remote_ver.text.strip():
        return True
    return False

def has_error(gz_url, deploy_dir,md5_url, gz_file_path):
    wget.download(gz_url, deploy_dir)
    
    m = hashlib.md5()
    with open(gz_file_path, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    r = requests.get(md5_url)
    if m.hexdigest() == r.text.strip():
        return True
    return False

# def deploy_app():




if __name__ == "__main__":
    ver_url = 'http://192.168.1.250/deploy/live_ver'
    ver_fname = '/var/www/download/live_ver'
    if  not has_pass_check(ver_fname, ver_url):
        print('版本一致')
        exit(1)

    r = requests.get(ver_url)
    ver = r.text.strip()
    deploy_dir = '/var/www/download1'
    gz_url = 'http://192.168.4.4/deploy/myweb-%s.tar.gz' % ver
    wget.download(gz_url, deploy_dir)

    md5_url = gz_url + '.md5'
    gz_fname = os.path.split(gz_url)[-1]
    gz_file_path = os.path.join(deploy_dir, gz_fname)

    if not has_error(gz_url, deploy_dir, md5_url, gz_file_path):
        print('文件已损坏,请重试')
        os.remove(gz_file_path)
        exit(2)
    print('OK')