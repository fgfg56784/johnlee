import re
reg1 = re.compile('http\:\/\/.*\.(jpg|png|jpeg|gif)')

with open('/tmp/test.html', 'r') as fobj:
    for line in fobj:
        if reg1.findall(line):
            print(line, end='')
