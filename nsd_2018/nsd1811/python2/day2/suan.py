import random

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def gen_int():
    x = 0
    cmds = {'+': lambda x, y: x+y, '-': lambda x, y: x-y}
    nums = [random.randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    biao = random.choice('+-')
    result = cmds[biao](*nums)
    prompt = '%s%s%s 结果为:' % (nums[0], biao, nums[1])

    # if biao == '+':
        # go = num[0] + num[1]
    # else:
        # go = num[0] - num[1]
        # result = sub(*num)
    # try:
    while x < 3:
        ch = int(input(prompt))
    # except (ValueError, ZeroDivisionError):
    #     print('无效的数字')
    #     continue
    # except (KeyboardInterrupt, EOFError):
    #     print('\nBye-bye')
    #     exit()
        if ch == result:
            print('答案正确')
            break
        print('答案错误')
        x += 1
    else:
            print('正确答案为: %s' % result)
def main():
    while True:
        gen_int()
        # try:
        yn = input('continue(y/n)??').strip()
        # except (ValueError, ZeroDivisionError):
        #     print('无效的数字')
        #     continue
        # except (KeyboardInterrupt, EOFError):
        # yn = 'n'
        if yn in 'nN':
            print('Bye-bye')
            break

if __name__ == '__main__':
    main()
