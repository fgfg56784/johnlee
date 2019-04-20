# class Weapon:
#     def __init__(self, name, strength):
#         self.name = name
#         self.strength = strength
#
#
# class Warrior:
#     # def __init__(self, name, weapon):
#     def __init__(self, name,  wname, wstrength):
#         self.name  = name
#         # self.weapon = weapon
#         self.weapon = Weapon(wname, wstrength)
#
#     def speak(self, content):
#         print('我是%s, %s' % (self.name, content))
#
# class MaleWarrior(Warrior):  #括号中制定父类
#     def attack(self):
#         print('放马过来吧，哈哈哈')
#
# if __name__ == "__main__":
#     # lb = MaleWarrior('吕布', '方天画戟')
#     fthj = Weapon('方天画戟', 100)
#     qlyyd = Weapon('青龙偃月刀','98')
#     zbsm = Weapon('丈八蛇矛', '98')
#     # lb = Warrior('吕布', fthj)  #自动调用__init__
#     # gy = Warrior('关羽', qlyyd)
#     # zf = Warrior('张飞', zbsm)
#     # print('我是%s, 使用的武器是%s, 攻击强度是%s' % (lb.name, lb.weapon.name, lb.weapon.strength))
#     # print('我是%s, 使用的武器是%s, 攻击强度是%s' % (gy.name, gy.weapon.name, gy.weapon.strength))
#     lb = Warrior('吕布', '方天画戟', 100)
#     gy = Warrior('关羽', '青龙偃月刀', 98)
#     zf = Warrior('张飞', '丈八蛇矛', 98)
#     print('我是%s, 我的武器是%s, 攻击强度为: %s' % (lb.name, lb.weapon.name, lb.weapon.strength))
#     print('我是%s, 我的武器是%s, 攻击强度为: %s' % (gy.name, gy.weapon.name, gy.weapon.strength))
#     print('我是%s, 我的武器是%s, 攻击强度为: %s' % (zf.name, zf.weapon.name, zf.weapon.strength))
#     lb.speak('从此刻开始，战场由我一人主宰!')
#     # lb.attack()
#     gy.speak('给人信仰,为梦前行永不放弃!')
#     zf.speak('百万军中，取人首级如探囊取物!')
#
#
# #__init__ 是构造方法, 当实例化时自动调用
# #方法就是类中的函数
# #实例化时,实例自动作为第一个参数传递给__init__
# #self只是一个变量名,也可以改为其他,只是在python中习惯起名为self
# #拥有self(绑定到实例上的属性), 在类中任何位置均可使用
# #
# #
# class Wand:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
# class Magester:
#     # def __init__(self, name, wand):
#     def __init__(self, name, fname,fpower):
#         self.name = name
#         # self.wand = wand
#         self.wand = Wand(fname, fpower)
#
#     def speak(self, content):
#         print('我是%s, %s' % (self.name, content))
#
#         # class Wand:
#     #     def __init__(self, name, power):
#     #         self.name = name
#     #         self.power = power
#
# class FemaleMagester(Magester):
#     pass
#
# if __name__ == "__main__":
#     sy = Wand('深渊权杖', 70)
#     dts = Wand('大天使之杖', 100)
#     an = Magester('安妮', '深渊权杖', 70)
#     ll = Magester('流浪法师', '大天使之杖', 100)
#     # an = FemaleMagester('安妮', '深渊权杖')
#     print('我是%s, 我的法杖是%s, 法术强度: %s' % (an.name, an.wand.name, an.wand.power))
#     print('我是%s, 我的法杖是%s, 法术强度: %s' % (ll.name, ll.wand.name, ll.wand.power))
#     an.speak('你有看见我的小熊吗?')
#     ll.speak('誓言,禁固在身上,带上你的画卷,一起流浪!')


class Weapon:
    # def __init__(self, name, strength):
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class Warrior:
    # def __init__(self, name, weapon):
    def __init__(self, name, wname, wstrength):
        self.name = name
        # self.weapon = weapon
        self.weapon = Weapon(wname, wstrength)

    def speak(self, content):
        print('我是%s,%s'% (self.name, content))


if __name__ == '__main__':
    # fthj = Weapon('方天画戟', 100)
    # qlyyd = Weapon('青龙偃月刀', 98)
    # zbsm = Weapon('丈八蛇矛', 98)

    # lb = Warrior('吕布', fthj)
    # gy = Warrior('关羽', qlyyd)
    # zf = Warrior('张飞', zbsm)
    lb = Warrior('吕布', '方天画戟', 100)
    gy = Warrior('关羽', '青龙偃月刀', 98)
    zf = Warrior('张飞', '丈八蛇矛', 98)

    # print('我是%s, 武器是%s, 攻击强度为: %s' % (lb.name, lb.weapon.name, lb.weapon.strength))
    # print('我是%s, 武器是%s, 攻击强度为: %s' % (gy.name, gy.weapon.name, gy.weapon.strength))
    # print('我是%s, 武器是%s, 攻击强度为: %s' % (zf.name, zf.weapon.name, zf.weapon.strength))
    print('我是%s, 武器是%s, 攻击强度为: %s' % (lb.name, lb.weapon.name, lb.weapon.strength))
    print('我是%s, 武器是%s, 攻击强度为: %s' % (gy.name, gy.weapon.name, gy.weapon.strength))
    print('我是%s, 武器是%s, 攻击强度为: %s' % (zf.name, zf.weapon.name, zf.weapon.strength))

    lb.speak('从此刻开始,战场由我一人主宰')
    gy.speak('给人信仰,为梦前行永不放弃!')
    zf.speak('谁来与我决一死战!')