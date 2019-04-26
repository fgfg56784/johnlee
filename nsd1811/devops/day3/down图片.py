from geturl import get_url
from download_all  import download
import re
from urllib import request
from sys import argv 

# def downpic(result):
#         for i in result:
                # url = 'http://' + re.split('//', i)[-1]  
                # dst = '/tmp/' + re.split('/', i)[-1]               
                

# if __name__ == "__main__":    
fn = download(argv[1], argv[2])
fn = '/tmp/tedu.html'
reg1 = r'http://[.\w/-]+\.(jpg|png|jpeg|gif)'
result = get_url(reg1, fn)
# downpic(result)
for i in result:
        # url = 'http://' + re.split('//', i)[-1]  
        dst = '/tmp/' + re.split('/', i)[-1]
        download(i , dst)
                