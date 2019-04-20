# range(0,10)
# for i in range(0,10):
#     print(i)
# print(list(range(10)))
# print(list(range(1, 10, 2)))
# print(list(range(10, 0, -1)))

#z = x + y
#x = y
#y = z
# list = [0,1]
# num = int(input('请输入长度(数字！): '))
# x = 0
# y = 1
# z = 0
# langth = 0
# while langth <= num :
#     z = x + y
#     langth += 1
#     x = y
#     y = z
#     list.append(z)
# print(list)

fip = [0,1]
large = int(input('请输入长度： '))
for i in range(large - 2):
    fip.append(fip[-2]+fip[-1])
print(fip)