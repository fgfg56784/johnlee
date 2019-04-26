import re
from sys import argv
# from urllib import request

# def geturl(url, fname):
#     result = []
#     with open(fname) as fobj:
#         for line in fobj:
#             picurl =  url.search(line)
#             if picurl:
#                 result.append(line.group())
#     # for i in result:
#     #     dst = re.split('/', i)[-1]
#     #     obj = request.Request(i, headers = head)
#     #     data = request.urlopen(obj)
#     #     with open('/tmp/%s' % dst, 'wb') as dobj:
#     #         dobj.write(data)
#     return result

# if __name__ == "__main__":
#     reg1 = r'http://[\w\./-]+\.(jpg|png|jpeg|gif)'
#     # reg1 = re.compile('http://[\w\./-]+\.(jpg|png|jpeg|gif)')
#     # head = {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
#     print(down_pic(reg1, argv[1]))
    
def get_url(patt, fname, encoding = 'utf8'):        #patt可匹配图片网址正则表达式，
                                #fname为1）中爬取到内容的文件
    cpatt = re.compile(patt, encoding = encoding)    #将正则表达式字符串形式编译为cpatt实例
    result = []                #存放匹配正则表达式的图片网址
    with open(fname) as fobj:        #打开爬取到网站（www.tedu.cn）内容的文件
        for line in fobj:            #遍历fname文件
            m = cpatt.search(line)        #使用cpatt实例查找匹配规则的网址
            if m:
                result.append(m.group())        #将匹配到的图片网址最加到result列表
    return result                            #函数最终返回result列表

if __name__ == '__main__':
    url = r'(http://|//)[.\w/-]+\.(jpg|png|jpeg|gif)'    #符合图片网址规则的正则表达式
    print(get_url(url, argv[1]))    
