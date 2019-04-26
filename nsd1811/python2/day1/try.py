# try:
#     num = int(input('number: '))
#     re = 100 / num
#     print(re)
# except ValueError:
#     print('无效的数字')
# except  ZeroDivisionError:
#     print('无效的数字')
# except KeyboardInterrupt:
#     print('\nBye-bye')
#     exit()
# except EOFError:
#     print('\nBye-bye')
#     exit()

try:
    num = int(input('number: '))
    re = 100 / num
    # print(re)
except (ValueError, ZeroDivisionError):
    print('无效的数字')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit()
else:
    print(re)
finally:
    print('Done')