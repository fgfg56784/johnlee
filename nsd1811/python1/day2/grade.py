# score = int(input('请输入你的成绩: '))
# if score >= 90 :
#     print('优秀')
# elif score >= 80 :
#     print('好')
# elif score >= 70 :
#     print('良')
# elif score >= 60 :
#     print('及格')
# elif score > 100 :
#     print('请输入0~100的成绩!')
#     print('*' * 40)
#     python3 grade.py
# else:
#     print('你要努力了')

score = int(input('请输入你的成绩(0~100): '))
if 60 <= score < 70:
    print('及格')
elif 70 <= score < 80:
    print('良')
elif 80 <= score < 90:
    print('好')
elif 90 <= score < 100:
    print('优秀')
elif score == 100:
    print('满分')
else:
    print('请输入100以内的成绩')
    print('*' * 40)