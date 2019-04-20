from string import ascii_letters, digits
from sys import argv
# all_chs = 'qwertyuiopasdfghjklzxcvbnm1234567890'
all_chs = ascii_letters + digits
def gen_pass(n = 8):
    from random import choice
    ch = ''
    for i in range(n):
        word = choice(all_chs)
        ch += word
    return ch
if __name__ == "__main__":
    print(gen_pass())
    print(gen_pass(4))