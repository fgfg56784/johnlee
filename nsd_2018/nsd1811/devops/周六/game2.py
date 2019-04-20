
class Score:
    def __init__(self, nfen):
        self.nfen = nfen
    def fenshu(self):
        # score = int(input('分数: '))
        score = self.nfen
        if score >= 90:
            print('优秀')
        elif score >= 80:
            print('好')
        elif score >= 70:
            print('良')
        elif score >= 60:
            print('及格')
        else:
            print('你要努力了')
