

'''
semigroup mul table
    (a * b) * c === a * (b * c)
    may no 1
    may not: a * b == b * a
'''
import itertools as I
class IterAllTables:
    def __iter__(self):
        L = self.L
        while True:
            n = self.getNext()
            if n is None: return

def mul(table, i, j):
    return table[i][j]
def verify1(table, i, j, k):
    ij = mul(table, i, j)
    ij_k = mul(table, ij, k)
    jk = mul(table, j, k)
    i_jk = mul(table, i, jk)
    return ij_k == ij_k
def verify_table(L, table):
    # row_i * col_j == table[i][j]
    assert len(table) == L
    for i, line in enumerate(table):
        assert len(line) == L
    return all(verify1(table, i, j, k) for i, j, k in product(range(L), 3))

def product(iterable, n):
    return I.product(iterable, repeat=n)


def ls2table(L, ls):
    return [ls[i:i+L] for i in range(0, len(ls), L)]
def iterAllTables(L):
    for ls in product(range(L), L*L):
        yield ls2table(L, ls)

def table2immutable(table):
    return tuple(map(tuple, table))

def new2old_to_old2new(new2old):
    ls = [None]*len(new2old)
    for new, old in enumerate(new2old):
        ls[old] = new
    return ls

def app_permutation_table(permutation, table):
    table = app_permutation_table_value(permutation, table)
    return app_permutation_rowcol(permutation, table)
def app_permutation_table_value(permutation, table):
    new2old = permutation
    old2new = new2old_to_old2new(new2old)
    t = [[old2new[v] for v in ls] for ls in table]
    return t
def app_permutation_rowcol(permutation, table):
    # (old2new, new2old) = permutation
    new2old = permutation
    table = app_permutation_list(new2old, table)
    table = list(map(lambda row: app_permutation_list(new2old, row), table))
    return table
def app_permutation_list(new2old, ls):
    # permutation = (old2new, new2old)
    return [ls[old] for old in new2old]
def std_table(table):
    L = len(table)
    min_table = list(map(list, table))
    for permutation in I.permutations(range(L)):
        t = app_permutation_table(permutation, table)
        if t < min_table:
            min_table = t
    return table2immutable(min_table)

def iterValidAllTables(L):
    return filter(lambda table: verify_table(L, table), iterAllTables(L))

def _t(n=2):
    tables = iterValidAllTables(n)
    s = set()
    for table in tables:
        #rint(table)
        t = std_table(table)
        if t not in s:
            s.add(t)
            print(t)
    print(len(s))
_t(3)


'''
L = 2
[(0, 0), (0, 0)] all 0s
[(1, 1), (1, 1)] all 1s
[(0, 0), (1, 1)] const
[(1, 1), (0, 0)] const . not
[(0, 1), (0, 1)] const id
[(1, 0), (1, 0)] const not
[(0, 1), (1, 0)] a xor b
[(1, 0), (0, 1)] a nxor b

[(1, 1), (1, 0)] not (a and b)
[(0, 0), (0, 1)] a and b
[(0, 0), (1, 0)] a and not b
[(0, 1), (0, 0)] not a and b
[(0, 1), (1, 1)] a or b
[(1, 0), (0, 0)] not (a or b)
[(1, 0), (1, 1)] a or not b
[(1, 1), (0, 1)] not a or b



((0, 0), (0, 0))
((0, 0), (0, 1))
((0, 0), (1, 0))
((0, 0), (1, 1))
((0, 1), (0, 0))
((0, 1), (0, 1))
((0, 1), (1, 0))
((1, 0), (0, 0))
((1, 0), (1, 0))
((1, 1), (0, 0))
'''

