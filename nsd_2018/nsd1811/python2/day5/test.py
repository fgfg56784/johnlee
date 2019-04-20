import pickle
a = input('内容: ')
fname = '/tmp/neirong.txt'
with open(fname, 'wb') as fobj:
    pickle.dump(a, fobj)
with open(fname, 'rb') as fobj:
    ne = pickle.load(fobj)
print(ne)