# class book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return '《%s》' % self.title
#
#     def __call__(self):
#         print('《%s》 is written by %s' % (self.title, self.author))
#
# if __name__ == "__main__":
#     stupidpy = book('笨方法学python3', 'Zed A. Shaw')
#     corepy = book('python核心编程', 'Wesley')
#     print(stupidpy)
#     stupidpy()
#     print(corepy) #自动调用__str__方法中的代码
#     corepy()  #自动调用__call__方法中的代码


class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '《%s》 is written by %s' % (self.title, self.author)

    def __call__(self):
        print('《%s》is written by %s' % (self.title, self.author))

if __name__ == '__main__':
    corepy = book('python核心编程', 'Welesy')
    stupidpy = book('笨方法学python', 'Zed A.Shaw')
    print(corepy)
    print(stupidpy)
    corepy()
    stupidpy()

