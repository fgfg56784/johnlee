import random
print('猜拳!!三局两胜!!')
# list = ['石头','剪刀','布']
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# prompt = '''(0) 石头
# (1) 剪刀
# (2) 布
# 请选择 0/1/2: '''
# i = 0
# p = 0
# x = 0
# while x < 2 :
#     computer = random.choice(list)
#     ind = int(input(prompt))
#     player = list[ind]
#     print('你出的是:%s  计算机出的是:%s' % (player, computer))
#     if player == computer:
#         print('平局')
#     elif [player,computer] in win_list:
#         print('你赢了')
#         i += 1
#     else:
#         print('你输了')
#         p += 1
#     x = i if i == 2 else p
# if i >= 2 :
#     print('你赢了两盘,你是胜利者')
# if p >= 2 :
#     print('你输了两盘,你是失败者')

list = ['石头''剪刀','布']
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
xuan = '''(0) 石头
(1) 剪刀
(2) 布
请选择 0/1/2: '''
pwin = 0
cwin = 0
while pwin < 2 and cwin < 2 :
    computer = random.choice(list)
    ind = int(input(xuan))
    player = list[ind]
    print('计算机出的是:%s 你出的是:%s' % (player,computer))
    if player == computer :
        print('\033[32;1m平局\033[0m')
    elif [player,computer] in win_list:
        print('\033[31;1m你赢了\033[0m')
        pwin += 1
    else:
        print('\033[33;1m你输了\033[0m')
        cwin += 1
if pwin == 2:
    print('三局两胜,胜利者为player')
if cwin == 2:
    print('三局两胜,胜利者为computer')