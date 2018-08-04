
'''
LeftwardList a = () | (a, LeftwardList a)
'''

__all__ = '''
    leftward
    to_leftward_list
    to_reversed_leftward_list
        reversable2leftward_list
            seq2leftward_list
    

    iter_leftward_list
    leftward_list2list

    leftward_list2last
    leftward_list2default_last
    leftward_list2head
    leftward_list2default_head

'''.split()


############### constructors ###############

def leftward(x, leftward_list):
    return x, leftward_list
def to_reversed_leftward_list(iterable):
    ls = ()
    for x in iterable:
        ls = leftward(x, ls)
    return ls

def reversable2leftward_list(reversable):
    return to_reversed_leftward_list(reversed(reversable))
seq2leftward_list = reversable2leftward_list


def to_leftward_list(iterable):
    maybe_seq = iterable
    try:
        r = reversed(maybe_seq)
    except TypeError:
        seq = tuple(iterable)
        r = reversed(seq)
    else:
        #print('here')
        pass
    return to_reversed_leftward_list(r)

if 1:
    # try reversed
    assert reversed(range(3))
    try:
        reversed(iter([0,1,2]))
    except TypeError:
        pass
    else:
        raise logic - error


assert to_leftward_list(range(3)) == (0, (1, (2, ())))
assert to_leftward_list(iter([0,1,2])) == (0, (1, (2, ())))







############### output ###############

def iter_leftward_list(leftward_list):
    while leftward_list:
        x, leftward_list = leftward_list
        yield x
def leftward_list2list(leftward_list, list=list):
    return list(iter_leftward_list(leftward_list))














############### elem ###############

def leftward_list2last(leftward_list):
    if not leftward_list:
        raise IndexError('last(empty_leftward_list)')
    return leftward_list2default_last(leftward_list)

def leftward_list2default_last(leftward_list, default=None):
    for default in iter_leftward_list(leftward_list):
        pass
    return default

def leftward_list2head(leftward_list):
    if not leftward_list:
        raise IndexError('head(empty_leftward_list)')
    return leftward_list2default_head(leftward_list)
def leftward_list2default_head(leftward_list, default=None):
    for default in iter_leftward_list(leftward_list):
        break
    return default




    
