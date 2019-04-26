import random

def caishu():
    gen = random.randint(1,100)
    x = 0

    while x < 5:
        try:
            gu = int(input('电脑生成了一个在1~100的数字,猜一下是多少: '))
        except ValueError:
            print('请输入数字')
            continue
        else:
            gu = int(gu)

        if gu > 100:
            print('都说在100以内了,你是不是傻')
            continue

        if gu == gen:
            print('你猜对了')
        elif abs(gu - gen) < 5:
            print('答案已经很近了')
        elif gu > gen:
            print('猜大了')
            x += 1
        else:
            print('猜小了')
            x += 1

    else:
        print('正确数字为: %s' % gen)

if __name__ == "__main__":
    caishu()