# class A:
#     def func1(self):
#         print('a func')
#     def func(self):
#         print('aaaaa')
#
# class B:
#     def func2(self):
#         print('b func')
#
#     def func(self):
#         print('bbbbbb')
#
#         # 左  右
# class C(B, A):   #父类可以有多个
#     def func3(self):
#         print('c func')
#
#     def func(self):
#         print('ccccc')
#
# if __name__ == "__main__":
#     c1 = C()
#     c1.func1()
#     c1.func2()
#     c1.func3()
#     c1.func()   # 同名函数先找自身,若无在从定义的 父类左边开始找,都是匹配则停止

class A:
    def an(self):
        print('你有看见我的小熊吗?')

    def fz(self):
        print('梅贾的窃魂卷')

class B:
    def ll(self):
        print('誓言,禁固在身上,带上你的画卷,一起流浪!')

    def fz(self):
        print('死亡之帽')

class C(B, A):
    def yj(self):
        print('我好像95%的时候都在说谎。')

    def fz(self):
        print('大天使之杖')

if __name__ == '__main__':
    c1 = C()
    c1.an()
    c1.ll()
    c1.yj()
    c1.fz()
