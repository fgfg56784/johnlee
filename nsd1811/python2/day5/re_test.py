import re
import pickle

src = '/var/ftp/nsd_2018/nsd1811/devops/snacks.data'
with open(src, 'r') as src_fobj:
    for line in src_fobj:
         m = re.split("[，\ 、。\.\s]", line)
# print(m)
m2 = []
de = re.compile('')
print(len(m))
for i in range(len(m)):
    # print(m[i])
    mde = m[i]
    if not de.fullmatch(mde):
        # print(m[i])
        m2.append(m[i])
for i in m2:
    print(i)

# dst = '/var/ftp/nsd_2018/nsd1811/devops/snacks.data1'
# with open(dst, 'wb')  as dst_fobj:
#     pickle.dump(m, dst_fobj)
