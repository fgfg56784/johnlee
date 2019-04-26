#需要用到的模块
import tarfile
from time import strftime
import os
import hashlib
# from check_file import check_file
# from sys import argv
# from hashlib import md5
import pickle
# from check_file import check_file
#定义生成md5值函数
def check_file(fname):
    m1 = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            line = fobj.read(4096)
            if not line:
                break
            m1.update(line)
    return m1.hexdigest()
#定义完全备份函数
def full_backup(src, dst, md5file):
    #生成压缩包的绝对路径
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)
    #对文件进行压缩
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()
    md5dict = {}
    #生成md5值字典
    for path, folders, files in os.walk(src):
        for file in files:
            file_path = os.path.join(path, file)
            md5dict[file_path] = check_file(file_path) #调用MD5校验函数对字典进行赋值
    #把md5值字典保存到文件中
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)
#定义增量备份函数
def incr_backup():
    #生成压缩包的绝对路径
    fname = os.path.basename(src)
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)
    md5dict = {}
    #生成新的md5值
    for path, folders, files in os.walk(src):  #得到格式为[("","",""),("","",""),("","","").....]的列表,每个元组中的三个值按顺序依次赋值给 path, folders, files
        for file in files: #再把flies中的代表文件的值,依次赋值给file
            key = os.path.join(path, file)  #拼接文件路径
            md5dict[key] = check_file(key) #调用MD5校验函数对字典进行赋值
    #提取上一次备份的md5值字典
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)
    #更新md5文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)
    #将新md5与旧md5值,与旧md5对比,把md5值不相同的文件重新打包
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if md5dict[key] != old_md5.get(key):
            tar.add(key)
    #结束关闭文件
    tar.close()

if __name__ == '__main__':
    # fname = '%s' % argv[1]
    #定义源地址,tar文件存放地址,md5文件存放地址
    src = '/tmp/mydemo/security'
    dst = '/tmp/demo/'
    md5file = '/tmp/mydemo/check.data'
    #定义脚本执行周期
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup()