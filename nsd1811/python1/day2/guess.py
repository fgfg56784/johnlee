import random
ran = random.randint(1,100)

guess_times = 0

if guess_times >= 3 :
    exit()
else:
    num = int(input('guess a number(1~100): '))
if num > ran :
    print('你猜大了')
elif num < ran :
    print('你猜小了')
else:
    print('你猜对了')
guess_times += 1

import random
ran = random.randint(1,100)

guess_times = 0
while guess_times < 3 :
    num = int(input('guess a number(1~100): '))
    if num > ran :
        print('你猜大了')
    elif num < ran :
        print('你猜小了')
    else:
        print('你猜对了')
        exit(0)
    guess_times += 1
