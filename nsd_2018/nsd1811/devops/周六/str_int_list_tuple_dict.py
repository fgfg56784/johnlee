astr = 'yahellojohn'
aint = 1234567890
alist = ['ni', 'ge', 'sha', 'gua', 1]
atuple = ('you', 'bing', 'a', 'ni')
adict = {'name':'john', 'age':12}

>>> aset = {'a', 'b', 'c'}
>>> aset.update('ah')
>>> aset
{'a', 'b', 'c', 'h'}
>>> agroup
{'b', 'a', 'c', 'z', 'e', 'w'}
>>> aset - agroup
{'h'}
>>> agroup - aset
{'z', 'e', 'w'}
>>> agroup
{'b', 'a', 'c', 'z', 'e', 'w'}
>>> aset.difference(agroup)
{'h'}
>>> aset.difference_update(agroup)
>>> aset
{'h'}
