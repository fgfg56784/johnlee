from random import choice
class FguessingGame:
    def __init__(self, cname):
        self.cname = cname
    def caiquan(self):
        cmds = {'1':'剪刀', '2':'石头', '3':'布'}
        win_list = ['剪刀布', '布石头', '石头剪刀']
#         info = '''(1)  剪刀
# (2)  石头
# (3)  布
# 请选择(1/2/3):  '''
        x = 0 
        y = 0 
        z = 0
        while z < 2:
            pcc = choice('123')
            pcco = cmds[pcc]
            hm = self.cname.strip()
            hmco = cmds[hm]
            print('你出的是%s, 计算机出的是%s' % (hmco, pcco))
            if hmco+pcco in win_list:
                print('你赢了')
                x += 1
            elif hmco == pcco:
                print('平局')
            else:
                print('你输了')
                y += 1

            if x == 2:
                print('三局两胜,你赢了')
            if y == 2:
                print('三局两胜,电脑赢了')
            z = x if x >= 2 else y

    if __name__ == "__main__":
        caiquan()