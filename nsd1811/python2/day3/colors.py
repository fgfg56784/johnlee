import sys, random
cmds = {'red':31, 'green':32, 'yellow':33, 'blue':34, 'purple':35, 'lblue':36, 'white':37, 'dgreen':38}
def desc(cho,color):
    def cor():
        return '\033[%s;1m%s\033[0m' % (cho, color())
    return cor

def hello():
    return 'hello john'

# @desc
def hi():
    return 'yahello'

# if __name__ == '__main__':
# print(hello())
# print(hi())
# ch = cmds[sys.argv[1]]
rh = random.choice()
a = desc(ch, hello)
# print(a())
# print(hi())

import sys
import random
import functools
import operator
import os
import shutil
import pickle as p

