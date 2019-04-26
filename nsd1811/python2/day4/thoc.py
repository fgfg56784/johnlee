from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    x = 0
    nums = [randint(1,1000) for i in range(2)]
    nums.sort(reverse=True)
    adic = {'+':add, '-':sub}
    cho = choice('+-')
    go = adic[cho](x=nums[0],y=nums[1])
    while x < 3:
        mu = int(input('%s%s%s= ' % (nums[0], cho, nums[1])))
        if mu == go:
            print('答案正确')
            break
        else:
            print('答案错误')
            x += 1
    else:
        print('错误3次,正确答案为: %s' % go)


def get_info():
    while True:
        exam()
        yn = input('continue(y/n): ')
        if yn in 'nN':
            break

if __name__ == '__main__':
    get_info()
