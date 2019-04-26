# import random  # 猜数字游戏
# computer = random.randint(1, 10)
# x = 1
# while x <= 5 :
#     player = int(input('请输入1~10中的数字: '))
#     x += 1
#     if player == computer:
#         print('\033[31;1m你猜对了!\033[0m')
#         break
#     elif 100 >= player > computer:
#         print('\033[32;1m你猜大了\033[0m')
#     elif player < computer:
#         print('\033[33;1m你猜小了\033[0m')
#     else:
#         print('\033[34;1m请输入1~100中的数字\033[0m')
# else:    #如果循环执行了break,则不再执行lese语句
#     print('数字为',computer)

# import random
# ran = random.randint(1,10)
# x = 1
# while x <= 5 :
#     guess = int(input('请输入1~10的数字: '))
#     x += 1
#     if guess == ran:
#         print('\033[31;1m你猜对了!\033[0m')
#         break
#     elif guess > ran:
#         print('\033[32;1m你猜大了\033[0m')
#     else:
#         print('\033[33;1m你猜小了!\033[0m')
# else:
#     print('\033[34;1m正确答案是: %s\033[0m' % ran )
import random
computer = random.randint(1,10)
guess_times = 0
while guess_times < 5:
    player_guess = int(input('please enter your guession number which in 1~10: '))
    guess_times += 1
    if player_guess == computer:
        print('\033[31;1mcurrect!!\033[0m')
        break
    elif player_guess > computer:
        print('\033[32;1mit could be smaller\033[0m')
    else:
        print('\033[33;1mit could be larger\033[0m')
else:
    print('\033[34;1mthis number is: %s ' % computer)