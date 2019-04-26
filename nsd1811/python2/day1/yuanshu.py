# aset = set('abc')
# bset = set('bcd')
# aset  |  bset
# aset & bset
# aset  - bset
# aset.add('abc')
# aset.update(['aa', 'bb', 'cc'])
# aset.remove('aa')

import time
print(time.time())
print(time.ctime())
print(time.localtime())
t = time.localtime()
print(t.tm_yday)
print(t.tm_year)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(t.tm_mon)
print(t.tm_hour, t.tm_min,  t.tm_sec)
print(time.strftime('%a, %A'))

import datetime
print(datetime.datetime.now())
print(datetime.timedelta())




