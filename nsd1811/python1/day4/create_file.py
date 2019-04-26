import os
def get_fname():
    while True:
        dst_fname = input('文件名: ')
        if os.path.exists(dst_fname):
            print('文件已存在,请重试')
        else:
            break
    return dst_fname

def get_content():
    ch = []
    print('请输入数据,在单独一行输入end结束')
    while True:
        content = input('>')
        if content == 'end':
            break
        ch.append(content)
    return ch

def ifile(name,cnt):
    # file_name = name
    # file_content = cnt
    # f = open(file_name, 'w')
    # f.writelines(file_content)
    # f.close()
    with open('name', 'w') as f:
        f.writelines(cnt)        

if __name__ == "__main__":
    fname = get_fname()
    fcontent = get_content()
    fcontent = [line + '\n' for line in fcontent ]
    ifile(fname,fcontent)
