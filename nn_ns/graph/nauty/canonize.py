
import itertools, bisect
import math
import random
import timeit


def inc_permutation(permutation):
    n = len(permutation)
    i1 = n - 1
    while i1:
        i = i1 - 1
        if permutation[i] < permutation[i1]:
            break
        i1 = i
    else:
        return 0

    permutation[i1:] = permutation[:i1-1:-1]
    assert len(permutation) == n
    
    x = permutation[i]
    j = bisect.bisect_right(permutation, x, i+1)
    y = permutation[j]
    assert permutation[j-1] <= x < y
    permutation[i], permutation[j] = y, x
    return n - i # how many items moved


# label = new_v2old_v
def cmplabel(n, g, hasedge, L, R, cmpeq_len = 0):
    for new in range(n):
        if L[new] != R[new]:
            break
##    for new, (v, u) in enumerate(zip(L, R)):
##        if v != u:
##            break
    else:
        raise ValueError('same label')

    if new < cmpeq_len:
        new = cmpeq_len
        
    has = lambda label: bool(hasedge(g, label[row], label[col]))
    for row in range(new, n):
        for col in range(row+1):
            l = has(L)
            r = has(R)
            if l != r:
                return l - r, row
    return 0, new # automorphism

def canonize_graph(n, g, hasedge):
    minlabel = list(range(n))
    label = minlabel.copy()
    cmpeq_len = n
    while True:
        num_moved = inc_permutation(label)
        if not num_moved: break

        cmpeq_len = min(cmpeq_len, n-num_moved)
        assert cmpeq_len >= 0
        r, row = cmplabel(n, g, hasedge, minlabel, label, cmpeq_len=cmpeq_len)
        if not r:
            # automorphism
            if label[0] == minlabel[0]:
                cmpeq_len = n
                continue
            else:
                r = -1
                row = 0
                #discard all
                #  not continue
        
        if r > 0:
            minlabel = label.copy()
            cmpeq_len = n
            continue

        # discard from row
        # next round, label[row] will be changes
        tail = label[row+1:]
        tail.sort(reverse = True)
        if row:
            cmpeq_len = row - 1 # since num_moved will be >= n - row
        else:
            cmpeq_len = 0
    return minlabel



def make_simple(g):
    edges = frozenset(tuple(sorted([v, u])) for v, ns in enumerate(g) for u in ns)
    return edges


def hasedge(g_edges, i, j):
    e = tuple(sorted([i,j]))
    return e in g_edges
class HasEdge:
    __slots__ = ('count',)
    def __init__(self):
        self.count = 0
    def __call__(self, g_edges, i, j):
        self.count += 1
        e = tuple(sorted([i,j]))
        return e in g_edges
    
def str_relabelled_graph(n, g, hasedge, label):
    ls = [''.join('1' if hasedge(g, label[row], label[col]) else '0'
                  for col in range(row+1))
          for row in range(n)]
    r = '\n'.join(ls)
    return r

def calcNshowLabel(g):
    
    edges = make_simple(g)
    n = len(g)
    hasedge = HasEdge()
    label = canonize_graph(n, edges, hasedge) # query hasedge 894 for n = 5
    print('label', label)
    print('hasedge.count', hasedge.count)
    print('math.factorial({})'.format(n), math.factorial(n))

    print(str_relabelled_graph(n, edges, hasedge, label))


def gen_graph(n, p):
    assert 0 <= p <= 1
    assert n >= 0
    ls = [[] for _ in range(n)]
    for row in ls:
        m = random.gauss(n*p, sigma = 1)
        row.extend(random.randrange(n) for _ in range(int(m)))
    return ls

def show_perms(n):
    p = list(range(n))
    while inc_permutation(p): print(p)


g = [[1,2], [2], [1], [1,2], []]
calcNshowLabel(g)
f = lambda:calcNshowLabel(gen_graph(n, .5))
for n in range(4, 10):
    dt = timeit.timeit(f, number=1)
    print('dt', dt)
    
'''
label [4, 0, 3, 1, 2]
hasedge.count 894
math.factorial(5) 120
0
00
000
0110
01110
label [0, 2, 1, 3]
hasedge.count 126
math.factorial(4) 24
0
00
110
1110
dt 0.026980268424494247
label [3, 0, 4, 1, 2]
hasedge.count 638
math.factorial(5) 120
0
00
010
1110
11110
dt 0.03192366977785727
label [1, 3, 4, 0, 5, 2]
hasedge.count 3398
math.factorial(6) 720
0
00
010
1110
11100
111011
dt 0.061559641905186396
label [2, 1, 3, 0, 4, 6, 5]
hasedge.count 15398
math.factorial(7) 5040
0
00
001
0110
01111
101001
1111000
dt 0.1668298990988983
label [1, 7, 4, 6, 0, 5, 2, 3]
hasedge.count 125984
math.factorial(8) 40320
0
00
011
1011
11001
110011
1101011
11110110
dt 1.0781458164114084
label [0, 3, 6, 7, 1, 8, 5, 4, 2]
hasedge.count 1605520
math.factorial(9) 362880
0
00
000
0010
01010
011011
1011111
11001101
111101110
dt 11.507302940822868
'''






