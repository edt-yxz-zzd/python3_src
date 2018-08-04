import call_cnauty as m
import sys


from array import array
from cnauty import *

g = [[1,2,], [2,], [], [1,2], []]
n = len(g)
try:
    nauty_packed(g, directed=True, userautomproc=lambda : 3)
    raise "should not come here"
except TypeError:
    pass

def err(*args, **kw):
    try:
        nauty_packed(*args, **kw)
        raise "should not come here"
    except TypeError:
        pass

def prt(g, *args, **kw):
    canon_vtx2old_vtx, leveled_partition, orbits = nauty_packed(
        g, *args, userautomproc=print, **kw)

    print('graph', g)
    print('canon_vtx2old_vtx', canon_vtx2old_vtx)
    print('partition', leveled_partition)
    print('orbits', orbits)


    canon_vtx2old_vtx, leveled_partition, orbits = nauty_sparse(
        g, *args, userautomproc=print, **kw)

    print('graph', g)
    print('canon_vtx2old_vtx', canon_vtx2old_vtx)
    print('partition', leveled_partition)
    print('orbits', orbits)

g = [[1,2,], [2,], [], [1,2], []]
err(g, directed=True, userautomproc=lambda : 3)
prt(g, directed=True)

g = [[1,2,], [2,], [1], [1,2], []]
prt(g, directed=True)
g = [[1,2,], [2,0,3], [1,3,0], [1,2], []]
prt(g, directed=False)
g = [[2,], [], [0]]
prt(g, directed=False)
print(graph2cgraph(g, False))
cg = array.array('I', [1<<2, 0, 1])
r = cnauty_packed(3, cg)
print(r, cg)

