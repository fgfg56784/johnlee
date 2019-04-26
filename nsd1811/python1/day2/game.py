# import random
# machine = random.choice(['包','剪','揼'])
# human = input('请输入你想出的手势包,剪,揼： ')
# if machine == '包' and human == '揼' :
#     print('计算机出的是包,你输了')
# elif machine == '包' and human == '剪' :
#     print('计算机出的是包,你赢了')
# elif machine == '剪' and human == '包' :
#     print('计算机出的是剪,你输了')
# elif machine == '剪' and human == '揼' :
#     print('计算机出的是剪,你赢了')
# elif machine == '揼' and human == '剪' :
#     print('计算机出的是揼,你输了')
# elif machine == '揼' and human == '包' :
#     print('计算机出的是揼,你赢了')
# else:
#     print('计算机出的是'+machine+',平手')

# print('你的选择是:%s,计算机的选择是:%s' % (human,machine))
# if machine == human :
#     print('平手')
# elif machine == '包' and human == '揼' :
#     print('你输了')
# elif machine == '剪' and human == '包' :
#     print('你输了')
# elif machine == '揼' and human == '剪' :
#     print('你输了')
# else:
#     print('你赢了')
# win_list = [['剪','包'],['包','揼'],['揼','剪']]
# print('你的选择是:%s   计算机的选择是:%s' % (human,machine))
# if [human,machine] in win_list:
#     print('\033[31;1mYou Win!\033[0m')
# elif human == machine:
#     print('\033[32;1m平手\033[0m')
# else:
#     print('\033[33;1mYou Lose!\033[0m')

# import random
# all_choice = ['石头','剪刀','布']
# win_list = [['布','石头'],['石头','剪刀'],['剪刀','布']]
# computer = random.choice(all_choice)
# player = input('请出拳(石头/剪刀/布): ')
# print('你出的是:%s  计算机出的是:%s' % (player,computer))
# if player == computer:
#     print('\033[32;1m平局\033[0m')
# elif [player,computer] in win_list:
#     print('\033[31;1m你赢了\033[0m')
# else:
#     print('\033[33;1m你输了\033[0m')

# import random
# list = ['石头','剪刀','布']
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# prompt = '''(0) 石头
# (1) 剪刀
# (2) 布
# 请选择 0/1/2: '''
# computer = random.choice(list)
# ind = int(input(prompt))
# player = list[ind]
# print('你出的是:%s  计算机出的是:%s' % (player,computer))
# if player == computer:
#     print('平局')
# elif [player,computer] in win_list:
#     print('你赢了')
# else:
#     print('你输了')


import random
print('猜拳!!三局两胜!!')
list = ['石头','剪刀','布']
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择 0/1/2: '''
i = 0
p = 0
x = 0
while x < 2 :
    computer = random.choice(list)
    ind = int(input(prompt))
    player = list[ind]
    print('你出的是:%s  计算机出的是:%s' % (player, computer))
    if player == computer:
        print('平局')
    elif [player,computer] in win_list:
        print('你赢了')
        i += 1
    else:
        print('你输了')
        p += 1
    x = i if i == 2 else p
if i >= 2 :
    print('你赢了两盘,你是胜利者')
if p >= 2 :
    print('你输了两盘,你是失败者')















