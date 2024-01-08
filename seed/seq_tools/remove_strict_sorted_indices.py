r'''[[[
e ../../python3_src/seed/seq_tools/remove_strict_sorted_indices.py



py -m nn_ns.app.debug_cmd -x   seed.seq_tools.remove_strict_sorted_indices


#]]]'''#'''

__all__ = r'''
    iter_rngs__via_idc_
    iter_values__via_idc_
    iter_ints_in_gaps_
    iter_idc4reserve_
        iter_complement_idc_

    list_rngs__via_idc_
    list_values__via_idc_
    list_idc4reserve_
        list_complement_idc_

    ls2ls_pair__via_idc_
    lsls2lsls_pair__via_idc_
    remove_strict_sorted_indices__emplace_
'''.split()#'''
__all__


from seed.tiny_.mk_reiterable import mk_reiterable
#from seed.iters.difference_of_two_sorted_iterables import difference_of_two_sorted_iterables
from seed.data_funcs.rngs import sorted_unique_ints_to_iter_nontouch_ranges, rngs_to_iter_ints, rngs_op__iter_gaps # difference__xtouch_ranges
#def sorted_unique_ints_to_iter_nontouch_ranges(sorted_unique_ints, /):


def iter_rngs__via_idc_(strict_sorted_idc, /):
    return sorted_unique_ints_to_iter_nontouch_ranges(strict_sorted_idc)
def iter_values__via_idc_(idc, seq, /):
    for i in idc:
        yield seq[i]

#def iter_idc4gaps_(idc4remove, /):
def iter_ints_in_gaps_(strict_sorted_ints, /):
    'strict_sorted Iter int -> strict_sorted Iter int # without whole (begin,end)'
    strict_sorted_ints = iter(strict_sorted_ints)
    for end_j in strict_sorted_ints:
        next_j = end_j + 1
        break
    for end_j in strict_sorted_ints:
        if not next_j == end_j:
            if not next_j < end_j: raise ValueError('not strict_sorted')
            yield from range(next_j, end_j)
        next_j = end_j +1 #skip ==>> gaps
    return

def __():
  def iter_idc4reserve_(length, idc4remove, /):
    'whole length -> strict_sorted idc4remove -> strict_sorted idc4reserve'
    next_j = 0
    for end_j in idc4remove:
        if not next_j <= end_j: raise ValueError('not strict_sorted')
        yield from range(next_j, end_j)
        next_j = end_j +1 #skip idx4remove
    else:
        end_j = length
        if not next_j <= end_j: raise ValueError('not whole length')
        yield from range(next_j, end_j)
def iter_idc4reserve_(length, idc4remove, /):
    'whole length -> strict_sorted idc4remove -> strict_sorted idc4reserve'
    rngs4remove = iter_rngs__via_idc_(idc4remove)
    #rngs4reserve = difference__xtouch_ranges([(0, length)], rngs4remove)
    rngs4reserve = rngs_op__iter_gaps(rngs4remove, whole_rng=(0, length))
    idc4reserve = rngs_to_iter_ints(rngs4reserve)
    return idc4reserve
iter_complement_idc_ = iter_idc4reserve_

iter_rngs__via_idc_
iter_values__via_idc_
iter_idc4reserve_
iter_complement_idc_
def list_rngs__via_idc_(strict_sorted_idc, /):
    return [*iter_rngs__via_idc_(strict_sorted_idc)]
def list_values__via_idc_(idc, seq, /):
    return [*iter_values__via_idc_(idc, seq)]
def list_idc4reserve_(length, idc4remove, /):
    return [*iter_idc4reserve_(length, idc4remove)]
list_complement_idc_ = list_idc4reserve_

#def ls2lsls__via_idcs_(idcs, ls, /):
#    '[[idx]] -> [v] -> [[v]]'
def lsls2lsls_pair__via_idc_(idc, lsls, /):
    '[idx]{len=K} -> [[v]{len=L}]{len=N} -> (selected_vss, unselected_vss)/([[v]{len=K}]{len=N}, [[v]{len=L-K}]{len=N})'
    lsls = mk_reiterable(lsls)
    idc = mk_reiterable(idc)
    if not lsls:
        assert not idc
        idcX = []
    else:
        L = len(lsls[0])
        if not all(len(ls) == L for ls in lsls): raise ValueError

        idcX = iter_complement_idc_(L, idc)
        if len(lsls) > 1:
            idcX = [*idcX]

    selected_vss = [[*iter_values__via_idc_(idc, ls)] for ls in lsls]
    unselected_vss = [[*iter_values__via_idc_(idcX, ls)] for ls in lsls]
    return (selected_vss, unselected_vss)
def ls2ls_pair__via_idc_(idc, ls, /):
    '[idx] -> [v] -> (selected_vs, unselected_vs)/([v], [v])'
    ([selected_vs], [unselected_vs]) = lsls2lsls_pair__via_idc_(idc, [ls])
    return (selected_vs, unselected_vs)





def __():
  def remove_strict_sorted_indices__emplace_(idc4remove, seq, /):
    idc4remove = iter(idc4remove)
    for i in idc4remove:
        break
    else:
        return
    begin, end = i, i+1
        #gap/spaces
    for j in idc4remove:
        if j == end:
            end += 1
        else:
            assert end < j
            for begin, end in enumerate(range(end, j), begin):
                seq[begin] = seq[end]
            begin += 1
            end = j+1
    else:
        assert begin < end
        j = len(seq)
        if end < j:
            for begin, end in enumerate(range(end, j), begin):
                seq[begin] = seq[end]
            begin += 1
            end += 1
        assert begin < end == len(seq)
        del seq[begin:]
    return

def __():
  def remove_strict_sorted_indices__emplace_(idc4remove, seq, /):
    ls = []
    for i in reversed(idc4remove):
        while seq:
            ls.append(seq.pop())
            if len(seq) == i:
                ls.pop()
                break
        else:
            raise ValueError((idc4remove, i))
    seq.extend(reversed(ls))
    return
def remove_strict_sorted_indices__emplace_(idc4remove, seq, /):
    idc4reserve = iter_idc4reserve_(len(seq), idc4remove)
    i = -1
    for i, j in enumerate(idc4reserve):
        if not i == j:
            seq[i] = seq[j]
    else:
        i += 1
        del seq[i:]
    return











from seed.seq_tools.remove_strict_sorted_indices import iter_ints_in_gaps_

from seed.seq_tools.remove_strict_sorted_indices import remove_strict_sorted_indices__emplace_
from seed.seq_tools.remove_strict_sorted_indices import iter_rngs__via_idc_, iter_values__via_idc_, iter_idc4reserve_, iter_complement_idc_
from seed.seq_tools.remove_strict_sorted_indices import list_rngs__via_idc_, list_values__via_idc_, list_idc4reserve_, list_complement_idc_

from seed.seq_tools.remove_strict_sorted_indices import ls2ls_pair__via_idc_, lsls2lsls_pair__via_idc_
from seed.seq_tools.remove_strict_sorted_indices import *

