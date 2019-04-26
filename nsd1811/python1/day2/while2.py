import random  # 猜数字游戏
computer = random.randint(1, 100)
x = 1
while x <= 5 :
    player = int(input('请输入1~100中的数字: '))
    if player == computer:
        print('\033[31;1m你猜对你!\033[0m')
        exit(10)
    elif 100 >= player > computer:
        print('\033[32;1m你猜大了\033[0m')
        x += 1
        continue
    elif player < computer:
        print('\033[33;1m你猜小了\033[0m')
        x += 1
        continue
    else:
        print('\033[34;1m请输入1~100中的数字\033[0m')
        continue
print('数字为'+computer)
