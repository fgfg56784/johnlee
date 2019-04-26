from urllib import request

# headers = {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
headers = {'User-Agent':"curl/7.29.0"}
# headers = {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

obj = request.Request('http://127.0.0.1/', headers = headers)

r = request.urlopen(obj)
list(r)
