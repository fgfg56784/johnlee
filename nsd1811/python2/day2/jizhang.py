import time, pickle, os
fname = r'C:\ha\sc'

if not os.path.exists(fname):
        date = time.strftime('%Y/%m/%d')
        data = [
            [date, 0, 0, 10000, 'init data'],
        ]
        with open(fname, 'wb') as init:
            pickle.dump(data, init)

def save(fname):
    date = time.strftime('%Y/%m/%d')
    sh = int(input('请输入收入金额： '))
    de = input('说明： ')
    
    with open(fname, 'rb') as fobj:
        fil = pickle.load(fobj)
        balance = fil[-1][-2] + sh

    line = [date, sh, 0, balance, de]
    fil.append(line)
    
    with open(fname, 'wb') as save_fobj:
        pickle.dump(fil, save_fobj)
        
def cost(fname):
    date = time.strftime('%Y/%m/%d')
    co = int(input('请输入支出金额: '))
    de = input('支出原因:')
    
    with open(fname, 'rb') as fobj:
        fil = pickle.load(fobj)
        balance = fil[-1][-2] - co

    line = [date, 0, co, balance, de]
    fil.append(line)

    with open(fname, 'wb') as cost_fobj:
        pickle.dump(fil, cost_fobj)

def quary(fname):
    with open(fname, 'rb') as f:
        cafi = pickle.load(f)

    print('%-15s%-8s%-8s%-10s%-15s' % ('date', 'save', 'cost', 'balance', 'comment'))
    for line in cafi:
        print('%-15s%-8s%-8s%-10s%-15s'% tuple(line))

def manu():
    info = '''    (0)  收入
    (1)  支出
    (2)  查询明细
    (3)  退出
    请选择(0/1/2/3)： '''

    cmds = {'0':save, '1':cost, '2':quary}
    while True:
        choice = input(info)
        if choice not in ['0', '1', '2', '3']:
            print('输入无效请重试')
            continue

        if choice == '3':
            print('    Bye-bye!')
            break

        cmds[choice](fname)

if __name__ == "__main__":
    manu()