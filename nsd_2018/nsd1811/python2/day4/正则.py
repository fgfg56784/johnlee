# import re
# import random
#
# m = [random.randint ]
# f = 'seafood'
# print(re.match('f..', 'food'))
# print(re.match('f..', f))
# print(re.search('f..', f))
# m = re.search('f..', f)
# print(m.group())
# str1 = 'rfsdfseefsqwfs'
# print(str1)
# m1 = re.match('f.', str1)
# # print(m1.group())
# m2 = re.search('f.', str1)
# print(m2.group())
# m3 = re.findall('f.', str1)
# print(m3)
# re.fullmatch('f..', 'foo')
# re.fullmatch('f..', 'food')
# patt = re.compile('f..')
# m4 = patt.search(str1)
# print(m4.group())
#
# re.sub('x', 'john', 'hi x, haw are you x')
#
# re.search('.+', '')


import re
print(re.match('f..', 'food'))
print(re.match('f..', 'seafood'))
print(re.search('f..', 'search'))
print(re.findall('f..', 'ffosuwekjflsdfiewfkdsajfkdlfiwaefasdf'))
print(re.fullmatch('f..', 'foo fee fww faa'))
m = re.compile('f..')
m1 = m.search('food seefood')
print(m1.group())
