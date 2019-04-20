#完全备份与增量备份
import time 
import os 
import tarfile


def full_backup(src, dst, md5file):
    src_fname = os.path.split(src)
    tar_fname = '%s_full_%s.tar.gz' % (src_fname[0], time.strftime('%Y%m%d'))
    dst_fname = op.path.join(dst, tar_fname)
    tar1 = tarfile.open(dst_fname, 'w:gz')
    os.chdir(src_fname[0])
    tar1.add(src_fname[1])


def incr_backup():


if __name__ == "__main__":
    src = input('需要备份的文件: ')
        if not os.path.exists(src):
            print('no such file or directory')
            exit(10)
    dst = input('存放备份的目录: ')
        if not os.path.isdir(dst):
            print('no such directory')
            exit(10)
    md5file = '/tmp/md5_check.data'
    if time.strftime('%a') == 'Mon':
        full_backup()
    else:
        incr_backup()

