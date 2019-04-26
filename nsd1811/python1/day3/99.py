# for i in range(1,10):
#     for j in range(1,10):
#         if i <= j:
#             # print(str(i)+'X'+str(j)+'='+str(i*j), end='\t')
#             print('%sx%s=%s' % (i,j,i * j), end='\t')
#     print()
# for c in range(3):
#     for d in range(c+1):
#         print('hello john', end=' ')
#     print()
# n = input('请输入运算的范围,例如:1,9: ')
# for i in range(int(n[0]) + 1,int(n[2]) + 1):
#     for j in range(int(n[0]) + 1,int(n[2]) + 1):
#         if i <= j:
#             # print(str(i)+'X'+str(j)+'='+str(i*j), end='\t')
#             print('%sx%s=%s' % (i,j,i * j), end='\t')
#     print()
# print([10 + 5 for i in range(5)])
# print([15 for i in range(5)])
# print([15, 15, 15, 15, 15])
# print([10, 11, 12, 13, 14, 15, 16, 17, 18])
# print([10 + i for i in range(6)])
# print([10, 11, 12, 13, 14, 15])
# print([0 + i for i in range(1,6) if i % 2 == True])
# print([10 + i for i in range(1,6) if i % 2 == False])
# print('192.168.1.%s' % i for i in rage(1,255)]
# result = 0
# for i in range(0,101):
#     result += i
# print(result)
# result = 0
# for i in range(1,101, 2):
#     result += i
# print(result)
# result = 0
# for i in range(2,101, 2):
#     result += i
# print(result)
# f = open('/tmp/passwd')
# data = f.read()
# print(data)
# print('(^$^)' * 20)
# data = f.read()
# print(data)
# f.close()
# f = open('/tmp/passwd')
# print(f.read(4))
# print(f.read(10))
# print(f.readline())
# print(f.readlines(), end='\n')
# f.close()
# print('(^-^)' * 20)
# d = open('/root/.ssh/id_rsa.pub')
# key = d.read()
# print(key)
# d.close()
# f = open('/tmp/passwd')
# for line in f:
#     print(line)
# f.close()
# f = open('/tmp/passwd')
# for line in f:
#     print(line, end='')
# f.close()
# p = open('/tmp/timg.jpg', 'rb')
# print(p.read(4))
# print(p.read(4096))
# print(p.read(4096))
# p.close()
# f = open('/tmp/passwd', 'rb')
# print(f.read(4))
# print(f.readline())
# print(f.readlines())
# f.close()
# f = open('/tmp/hi.txt', 'w')
# f.write('hello john!!!\n')
# f.write('hello world!!!\n')
# f.writelines(['2nd line   ', '3rd line\n'])
# f.writelines(['2nd line\n', '3rd line\n'])
# f.flush()
# f.close()
# f = open('/tmp/hi.txt')
# print(f.read())
# f.close()
# with open('/tmp/passwd') as f :
#     print(f.readline())
# lond = int(input('please enter the range: '))
# for i in range(1,lond+1):
#     for j in range(1,lond+1):
#         if i >= j:
#             print('%sx%s=%s' % (j , i , i * j), end='\t')
#     print()
# print([10 + 5 for i in range(5)])
# print([10 + i for i in range(5)])
# print([0 + i for i in range(1, 10, 2)])
# print([0 + i for i in range(10, 0, -1)])
# print([0 + i for i in range(20) if i % 2 == True])
# print([0 + i for i in range(20) if i % 3 == False])
# print(['192.168.1.%s' % i for i in range(30)])
# result = 0
# for i in range(10):
#     print(result+i)
# for i in range(10):
#     result += i
# print(result)
# for i in range(1, 101, 2):
#     result += i
# print(result)
# f = open('/tmp/passwd')
# print(f.read(3))
# print(f.read(5))
# print(f.readline(), end='')
# print(f.readlines(), end='')
# f.close()
# with open('/tmp/passwd') as f:
#     print(f.read(4))
#     print(f.readline(), end='')
#     print(f.readlines(), end='')
# with open('/tmp/passwd', 'rb') as f:
#     print(f.read(5))
#     print(f.tell())
#     f.seek(0, 0)
#     print(f.tell())
#     print(f.readline())
#     print(f.tell())
#     f.seek(10, 1)
#     print(f.tell())
#     f.seek(-20,2)
#     print(f.tell())
# src_fname = input('please enter the source file:')
# dst_fname = input('please enter the destination file:')
# src_fobj = open(src_fname, 'rb')
# dst_fobj = open(dst_fname, 'wb')
# while True:
#     data = src_fobj.read(4096)
#     if not data:
#     # if data == 0:
#     # if data == False:
#     # if data == b'':
#         break
#     dst_fobj.write(data)
# src_fobj.close()
# dst_fobj.close()
# import sys
def copy(src_fname, dst_fname):
    src_fobj = open(src_fname, 'rb')
    dst_fobj = open(dst_fname, 'wb')
    while True:
        data = src_fobj.read(4096)
        if not data:
            break
        dst_fobj.write(data)
    src_fobj.close()
    dst_fobj.close()
copy(sys.argv[1],sys.argv[2])
