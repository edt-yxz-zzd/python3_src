
"""
bucket_sort
L = len(input)
key(e) is in range(N) for e in input
"""

from itertools import accumulate, chain

__all__ = tuple('is_sorted bucket_sort bucket_sorts group_to_list'
                ' split group_unify group'
                ' inner_sort_ints_list inner_sorts_ints_list radix_sort'
                .split())


_id = lambda e: e



def radix_sort(int_tuples, key_f, upper_ls):
    idx_upper_ls = list(enumerate(upper_ls))
    
    for i, upper in reversed(idx_upper_ls):
        int_tuples = bucket_sort(int_tuples, lambda e: key_f(e)[i], upper)

    assert is_sorted(int_tuples, key_f)
    return int_tuples

def is_sorted(iterable, key = _id):
    for pre in iterable:
        break
    else:
        return True # empty list

    key_pre = key(pre)
    for i in iterable:
        key_i = key(i)
        if key_i < key_pre:
            return False
        key_pre = key_i
    return True



def reindex_with_integer_buffer(ints, buffer, key = _id):
    stack = []
    for i in ints:
        i = key(i)
        assert i < len(buffer)
        idx = buffer[i]
        if 0 <= idx < len(stack) and stack[idx] == i:
            pass
        else:
            buffer[i] = len(stack)
            stack.append(i)
    return stack
def bucket_sort_with_integer_buffer(ints, buffer, key = _id):
    raise 'no no'
    #error!!!!!!!!!!!!1
    stack = []
    count = []
    ints = tuple(ints)
    for i in ints:
        i = key(i)
        assert i < len(buffer)
        idx = buffer[i]
        if 0 <= idx < len(stack) and stack[idx] == i:
            count[idx] += 1
        else:
            buffer[i] = len(stack)
            stack.append(i)
            count.append(1)

    where = list(accumulate(chain([0], count)))
    L = where[-1]
    assert L == len(ints)
    # output
    out = [None]*L
    for i in ints:
        idx = buffer[key(i)]
        out[where[idx]] = i
        where[idx] += 1

    return out
    
def bucket_sort(ints, key = None, N = None):
    if key == None: key = _id
    #ints = tuple(ints)
    L = len(ints)
    if N == None: N = L
    
    # count num of i's
    ls = [0]*N
    for i in ints:
        ls[key(i)] += 1

    # where to output i's
    where = 0
    for i in range(N):
        ls[i], where = where, where + ls[i]
    where = ls

    # output
    out = [None]*L
    for i in ints:
        out[where[key(i)]] = i
        where[key(i)] += 1

    return out


def inner_sort_ints_list(N, ints_list, key = _id):
    node_int_ls = tuple((node, i) for node, ints in enumerate(ints_list) for i in ints)
    node_int_ls = bucket_sort(node_int_ls, lambda e:key(e[1]), N)
    ls = tuple([] for _ in range(len(ints_list)))
    for node, i in node_int_ls:
        ls[node].append(i)
    return ls
''' bug
def inner_outer_sort_ints_list(N, ints_list, key = _id):
    node_int_ls = tuple((node, i) for node, ints in enumerate(ints_list) for i in ints)
    node_int_ls = bucket_sort(node_int_ls, lambda e:key(e[1]), N)
    ls = tuple([] for _ in range(len(ints_list)))
    to_new_node = [None]*len(ints_list)
    new_node = 0
    for node, i in node_int_ls:
        if to_new_node[node] == None:
            to_new_node[node] = new_node
            new_node += 1
        ls[to_new_node[node]].append(i)
    return ls
'''


def inner_sorts_ints_list(ints_list, key_with_round, rng, Ns):
    node_int_ls = tuple((node, i) for node, ints in enumerate(ints_list) for i in ints)
    node_int_ls = bucket_sorts(node_int_ls, lambda i,e:key_with_round(i,e[1]), rng, Ns)
    ls = tuple([] for _ in range(len(ints_list)))
    for node, i in node_int_ls:
        ls[node].append(i)
    return ls

''' bug
def inner_outer_sorts_ints_list(ints_list, key_with_round, rng, Ns):
    node_int_ls = tuple((node, i) for node, ints in enumerate(ints_list) for i in ints)
    node_int_ls = bucket_sorts(node_int_ls, lambda i,e:key_with_round(i,e[1]), rng, Ns)
    ls = tuple([] for _ in range(len(ints_list)))
    to_new_node = [None]*len(ints_list)
    new_node = 0
    for node, i in node_int_ls:
        if to_new_node[node] == None:
            to_new_node[node] = new_node
            new_node += 1
        ls[to_new_node[node]].append(i)
    return ls
'''

class __NotEq:
    def __eq__(self, other):
        return False
    def __ne__(self, other):
        return not self == other

__NOT_EQ = __NotEq()
# note: itertools.groupby
def group(iterable, key = None):
    'group so that each element in the same block are equal'
    if key == None: key = _id
    begin = None
    block_key = __NOT_EQ
    block = []
    i = -1 #################### for len(iter) is 0
    for i, n in enumerate(iterable):
        key_n = key(n)
        if key_n != block_key:
            block.append((begin, i))
            begin = i
            block_key = key_n
    block.append((begin, i+1)) # begin may be None, i may be -1
    return block[1:]

def group_unify(seq, key = None):
    block = group(seq, key)
    return tuple(seq[i] for i, j in block)

def split(list_obj, block):
    return [list_obj[i:j] for i,j in block]



def group_to_list(N, seq, key, get_data, container = tuple):
    block = group(seq, key)
    ls = [container() for i in range(N)]
    for i, j in block:
        v = key(seq[i])
        ls[v] = container(get_data(e) for e in seq[i:j])
    return ls

_id_gen = lambda i: _id
def bucket_sorts(ints, key_with_round, rng = None, Ns = None):
    if Ns == None: Ns = [None] * len(rng)
    for r, i in enumerate(rng):
        ints = bucket_sort(ints, key = lambda e:key_with_round(i,e), N=Ns[r])
    return ints







def _t(n=100):
    import random
    fff = list(range(n))
    random.shuffle(fff)
    data = [\
        list(random.randrange(n) for i in range(n)),\
        list(range(n)),\
        fff,\
        [n-1]*n,\
        [0]*n,\
        [1]*n,\
        ]
    buf = [0]*n
    for d in data:
        #print(d)
        
        b = bucket_sort(d)
        s = sorted(d)
        if b != s:
            print(d, b, s)
            break
        continue
        bb = bucket_sort_with_integer_buffer(d, buf)
        if bb != s:
            print(d, bb, s)
            break





        
if __name__ == "__main__":
    _t()
    



