

__all__ = '''
    print_lines
    print_odict_keys_after
    odict_split
    list_map
    handle_seq_begin_end
    list_find__by_is
    list_find__by_eq
    list_find
    list_split__by_is
    list_split__by_eq
    list_split
    list_join
    sum_lists
    id_map
    mkErr
    drop_prefix
    are_disjoint_sets
    find_out_nondisjoint_sets
    are_elements_all_unique
    find_duplicate_elements
    catch
    will_raise
    iterFrom
    betweenFromTo
    iterFromTo
    end_of
    even_lines_of_paired_words_to_odict
    fst
    snd
    cached
    group_to_pairs
    '''.split()

from collections import OrderedDict, Counter
from itertools import chain, groupby
from operator import is_, __eq__


#############################
__begin = ...
#############################

def fst(ls):
    return ls[0]
def snd(ls):
    return ls[1]

def id_map(x):
    return x
def end_of(XXX):
    '''\
example:
    class XXX:
        ...
    end_of(XXX)
'''
    pass



def drop_prefix(s, prefix):
    # (str, prefix) -> (None | suffix)
    if s.startswith(prefix):
        return s[len(prefix):]
    return None





def cached(dict, key, f):
    if key not in dict:
        dict[key] = f()
    return dict[key]




######## prints

def print_lines(iter_strs):
    '''\
e.g. print_lines(globals())
__all__ = \'''
    xxx
    yyy
\'''.split()
'''
    print('\n'.join(iter_strs))

def print_odict_keys_after(odict, key):
    _, after = odict_split(odict, key)
    print_lines(after)
def print_odict_keys_between(odict, begin_key, after_key):
    _, after = odict_split(odict, begin_key)
    between, _ = odict_split(after, after_key)
    print_lines(between)






######## iter/range

def repeat(x=None):
    while True:
        yield x
def iterFrom(i):
    while True:
        yield i
        i += 1

def betweenFromTo(i, x, j):
    return i <= x and (j is None or x <= j)
def iterFromTo(i, j):
    # [i..j]
    # len([i..j]) == j-i+1 >= 0
    assert j is None or i <= j+1
    if j is None:
        return iterFrom(i)
    return range(i, j+1)

'''
def iterMax(M):
    if M is None:
        return iterFrom(0)
    return range(M-1)
'''
def handle_seq_begin_end(seq, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(seq)
    if not 0 <= begin <= end <= len(seq):
        raise ValueError("0 <= begin <= end <= len(seq)")
    return seq, begin, end


'''
def fix_range(s, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(s)
    assert 0 <= begin <= end <= len(s)
    return s, begin, end
'''





###### list ops
def list_map(f, iterable):
    return list(map(f, iterable))


def list_find__by_is(ls, elem, begin=None, end=None):
    return list_find(ls, elem, begin, end, eq = is_)
def list_find__by_eq(ls, elem, begin=None, end=None):
    return list_find(ls, elem, begin, end, eq = __eq__)
def list_find(ls, elem, begin=None, end=None, *, eq=None):
    if eq is None: eq = __eq__
    ls, begin, end = handle_seq_begin_end(ls, begin, end)
    for i in range(begin, end):
        if ls[i] == elem:
            return i
    return -1
def list_split__by_is(ls, elem):
    return list_split(ls, elem, eq=is_)
def list_split__by_eq(ls, elem):
    return list_split(ls, elem, eq=__eq__)
def list_split(ls, elem, *, eq=None):
    indices = []
    begin = 0
    rngs = []
    L = len(ls)
    while True:
        i = list_find(ls, elem, begin, eq=eq)
        if i == -1:
            rngs.append((begin, len(ls)))
            break
        indices.append(i)
        rngs.append((begin, i))
        begin = i+1
    rs = [ls[i:j] for i, j in rngs]
    return rs
assert list_split([], ...) == [[]]


def list_join(seps, lists):
    it = iter(lists)
    seps = list(seps)
    ls = []
    for head in it:
        break
    else:
        return ls
    ls.extend(head)
    for x in it:
        ls.extend(seps)
        ls.extend(x)
    return ls



def sum_lists(lists):
    ls = []
    for s in lists:
        ls.extend(s)
    return ls





######### unique/disjoint/set
''' bug:
def are_disjoint_sets(sets):
    it = iter(sets)
    for s0 in it: break
    else: return True
    L0 = len(s0)
    for s in it:
        L = len(s)
        s0 |= s
        L0_ = len(s0)
        if L0_ != L0 + L:
            return False
        L0 = L0_
    return True
'''
def are_disjoint_sets(sets):
    it = iter(sets)
    s0 = set()
    L0 = len(s0)
    for s in it:
        L = len(s)
        s0 |= s
        L0_ = len(s0)
        if L0_ != L0 + L:
            return False
        L0 = L0_
    return True

def find_out_nondisjoint_sets(name2set):
    # -> {name_pair:instersection} where name_pair is set of len 2
    tested = set()
    pair2common = {}
    for name1, s1 in name2set.items():
        for name2, s2 in name2set.items():
            if name1 == name2: continue
            pair = frozenset([name1, name2])
            if pair in tested:
                continue
            tested.add(pair)
            common = s1 & s2
            if common:
                pair2common[pair] = common
    return pair2common




def are_elements_all_unique(ls):
    L = len(ls)
    s = set(ls)
    return L == len(s)
def find_duplicate_elements(iterable):
    c = Counter(iterable)
    return {k for k,v in c.items() if v > 1}
assert find_duplicate_elements([1,2,2]) == {2}






##### err

def mkErr(Error, *args, **kwargs):
    return Error(*args, **kwargs)
'''
def mkErr(Error, *args, with_traceback=None, **kwargs):
    e = Error(*args, **kwargs)
    if with_traceback is not None:
        e.with_traceback(with_traceback)
    return e
'''
def catch(Error, f, handler, otherwise=None):
    try:
        r = f()
    except Error as e:
        return handler(e)
    return otherwise(r) if otherwise is not None else r
def will_raise(e):
    def raise_():
        raise e
    return raise_
def will_return(r):
    def return_():
        return r
    return return_






############ odict ops

def group_to_pairs(iterable, key=None):
    '([a], a->k) -> [(k,[a])]'
    return [(k, list(g)) for k, g in groupby(iterable, key)]
#rint(group_to_pairs([1]))
assert group_to_pairs([1,1,2,1]) == [(1,[1,1]), (2,[2]), (1,[1])]

def odict_split(odict, key):
    '''\
input: odict::OrderedDict, key
assume key in odict
output: odict before key, odict after key
'''
    if key not in odict:
        raise ValueError('key not in odict')
    before = OrderedDict()
    after = OrderedDict()
    d = before
    for k, v in odict.items():
        if k == key:
            d = after
            continue
        d[k] = v
    return before, after

assert odict_split({1:3}, 1) == ({}, {})
assert odict_split({0:-1, 1:3, 2:4}, 1) == ({0:-1}, {2:4})


def even_lines_of_paired_words_to_odict(s):
    '''\
Main = TwoLines/newline*
TwoLines = KeyLine newline ValueLine
KeyLine = Words
ValueLine = Words
Words = Word/Space1s*

example:
    >>> even_lines_of_paired_words_to_odict(\'''\\
k1 k2
v1 v2
k3
v3\\
\'''
    {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
'''
    lines = s.split('\n')
    if len(lines) % 2 != 0:
        raise ValueError('not even lines')
    key_lines = lines[0::2]
    val_lines = lines[1::2]
    assert len(key_lines) == len(val_lines)
    key_val_pairs = []
    for key_line, val_line in zip(key_lines, val_lines):
        keys = key_line.split()
        vals = val_line.split()
        if len(keys) != len(vals):
            raise ValueError('len(keys) != len(vals)')
        key_val_pairs.extend(zip(keys, vals))
    key2val = OrderedDict(key_val_pairs)
    if len(key2val) != len(key_val_pairs):
        raise ValueError('keys not unique: {!r}'
            .format(find_duplicate_elements(map(fst, key_val_pairs))))
    return key2val
end_of(even_lines_of_paired_words_to_odict)


#############################
__end = ...
#############################
def _test_even_lines_of_paired_words_to_odict():
    try:
        even_lines_of_paired_words_to_odict('x x\ny y')
    except ValueError as e:
        assert e.args == ("keys not unique: {'x'}",)
    else: raise logic-error

    assert even_lines_of_paired_words_to_odict(' x \n y ') == {'x':'y'}
    try:
        even_lines_of_paired_words_to_odict(' x \n y \n')
    except ValueError as e:
        assert e.args == ('not even lines',)
    else: raise logic-error

    try:
        even_lines_of_paired_words_to_odict(' x z\n y ')
    except ValueError as e:
        assert e.args == ('len(keys) != len(vals)',)
    else: raise logic-error
    try:
        even_lines_of_paired_words_to_odict(' x \nz y ')
    except ValueError as e:
        assert e.args == ('len(keys) != len(vals)',)
    else: raise logic-error

_test_even_lines_of_paired_words_to_odict()

#############################

def _test1__list_split(string, char=' '):
    r1 = list(map(list, string.split(char)))
    r2 = list_split(list(string), char)
    try:
        assert r1 == r2
    except:
        print('{!r} {!r}'.format(string, char))
        print('{!r} {!r}'.format(r1, r2))
        raise
def _test__list_split():
    assert list_split([], ...) == [[]]
    _test = _test1__list_split
    _test('')
    _test('a')
    _test(' ')
    _test(' a')
    _test('a ')
    _test(' a ')
    _test(' a b')
    _test('c a b')
    _test('c a ')
    _test(' c a b')
    _test('c a b ')
    _test(' c a b ')
_test__list_split()


if __name__ == '__main__':
    print_odict_keys_between(globals(), '__begin', '__end')
    #rint_lines(__all__)

