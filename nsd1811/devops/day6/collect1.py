from collections import namedtuple

Point = namedtuple('point', ['a', 'b', 'c'])
a = Point('haha', 'lala', 'dada')
print(a.a)
print(a.b)
print(a.c)
