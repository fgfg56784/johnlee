from urllib import request

# https://www.baidu.com/s?ie=UTF-8&wd=%E6%B5%B7%E5%86%9B

url = 'https://www.baidu.com/s?ie=UTF-8&wd=' + request.quote('西游记')
print(url)

r = request.urlopen(url)

