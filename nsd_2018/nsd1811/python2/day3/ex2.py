from random import randint
def my_gen():
    yield 'hello john'
    num = [randint(1,100) for i in range(2)]
    yield  num
    yield 100

if __name__ == '__main__':
    r = my_gen()
    print(r.__next__())
    print(r.__next__())
    print(r.__next__())

    mg = my_gen()
    for item in mg:
        print(item)