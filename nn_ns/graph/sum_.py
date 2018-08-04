
'''
count_c3m3_4to23 = [1, 1, 2, 5, 14, 50, 233, 1249, 7595, 49566, 339722, 2406841, 17490241, 129664753, 977526957, 7475907149, 57896349553, 453382272049, 3585853662949, 28615703421545, ]
count_c3m3d_4to42 = count_c3m3_4to23
assert len(count_c3m3_4to23) == 23-3

#4 to 36 .. [0:17]
s = sum(count_c3m3d_4to42[:17])
print(s)
print(bin(s))
print('{} bit'.format(len(bin(s)) - 2))
a = 0
n = 2
for c in count_c3m3d_4to42:
    a += c
    n += 2
    print('n = {}, total = {}, {} bit'.format(n, a, len(bin(a)) - 2))

'''


from .graph_format_ascii_embedding import str2embedding as _str2embedding
from simple_undirected_graph import graph as _graph
from bucket_sort import bucket_sorts, group_to_list, bucket_sort, group, split
file = 'txt/ac3m3_from4to18d.txt'

gs = []
with open(file) as f:
    for s in f:
        e = _str2embedding(s[:-1])
        g = _graph(e)
        ds = [g.degree(v) for v in g.vertices()]
        ds.sort()
        gs.append((ds, e))

gs.sort()
pre = ()
n = 0
flag = False
rs = []
sp= [[3, 3, 3, 3, 6, 6, 6, 6, 6, 6], \
     [3, 3, 3, 5, 5, 5, 6, 6, 6]]

for ds, e in gs:
    if ds == pre:
        n += 1
        if ds in sp:print(ds)
        if not flag:
            rs.append(pre)
            flag = True
    else:
        pre = ds
        flag = False
    
print('m = {}'.format(len(rs)))
print('n = {}'.format(n))
#print(rs)
ls = []
for r in rs:
    block = group(r)
    x = split(r, block)
    if not sum(len(e) == 2 or len(e) == 1 for e in x):
        print(r)
