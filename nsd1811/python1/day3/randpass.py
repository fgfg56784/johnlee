# import random
# list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=_+?/.,<>!@#$%^&*()[]{}~`;:'
# yi = random.choice(list)
# er = random.choice(list)
# san = random.choice(list)
# si = random.choice(list)
# wu = random.choice(list)
# liu = random.choice(list)
# qi = random.choice(list)
# ba = random.choice(list)
# password = yi + er + san + si + wu + liu + qi + ba
# print(password)

import random
list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=_+?/.,<>!@#$%^&*()[]{}~`;:'
password = ''
for i in range(8):
    shu = random.choice(list)
    password += shu
print(password)

from random import choice
all_chs = 'qwertyuiopasdfghjklzxcvbnm1234567890'
ch = ''
for i in range(8):
    word = choice(all_chs)
    ch += word
print(ch)