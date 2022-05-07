r'''
py -m nn_ns.app.debug_cmd   seed.seq_tools.seq_as_mapping


from seed.seq_tools.seq_as_mapping import SeqAsMapping
from seed.seq_tools.seq_as_mapping import pseudo_seq2idc, pseudo_seq2iter_idc, pseudo_seq2iter_values, pseudo_seq2iter_items, pseudo_seq__enumerate
from seed.seq_tools.seq_as_mapping import pseudo_seq2idc_, pseudo_seq2iter_idc_, pseudo_seq2iter_values_, pseudo_seq2iter_items_, pseudo_seq__enumerate_
from seed.seq_tools.seq_as_mapping import pseudo_seq__get, mk_subseq5slice_range__tuple

from seed.mapping_tools.mapping_as_seq import MappingAsSeq


#'''

__all__ = '''
    SeqAsMapping

    pseudo_seq2idc_
    pseudo_seq2iter_idc_
    pseudo_seq2iter_values_
    pseudo_seq2iter_items_
    pseudo_seq__enumerate_

        pseudo_seq2idc
        pseudo_seq2iter_idc
        pseudo_seq2iter_values
        pseudo_seq2iter_items
        pseudo_seq__enumerate

    pseudo_seq__get
        mk_subseq5slice_range__tuple



    MappingAsSeq
    '''.split()


from collections.abc import Sequence, MutableSequence, Mapping, MutableMapping
from seed.tiny_.slice2triple import fix_slice_by_len_of, slice2triple_



def pseudo_seq2idc_(lookupable, /, *, reverse):
    L = len(lookupable)
    if reverse:
        return range(L-1, -1, -1)
    else:
        return range(L)
def pseudo_seq2iter_idc_(lookupable, /, *, reverse):
    return iter(pseudo_seq2idc_(lookupable, reverse=reverse))
def pseudo_seq2iter_values_(lookupable, /, *, reverse):
    return (lookupable[i] for i in pseudo_seq2idc_(lookupable, reverse=reverse))
def pseudo_seq2iter_items_(lookupable, /, *, reverse):
    return ((i, lookupable[i]) for i in pseudo_seq2idc_(lookupable, reverse=reverse))
def pseudo_seq__enumerate_(lookupable, /, *, reverse):
    return enumerate(pseudo_seq2iter_values_(lookupable, reverse=reverse))


def pseudo_seq2idc(lookupable, /):
    return pseudo_seq2idc_(lookupable, reverse=False)
def pseudo_seq2iter_idc(lookupable, /):
    return pseudo_seq2iter_idc_(lookupable, reverse=False)
def pseudo_seq2iter_values(lookupable, /):
    return pseudo_seq2iter_values_(lookupable, reverse=False)
def pseudo_seq2iter_items(lookupable, /):
    return pseudo_seq2iter_items_(lookupable, reverse=False)
def pseudo_seq__enumerate(lookupable, /):
    return pseudo_seq__enumerate_(lookupable, reverse=False)


def mk_subseq5slice_range__tuple(lookupable, slice_, idc, /):
    return tuple(lookupable[i] for i in idc)

def pseudo_seq__get(lookupable, idx_or_slice, mk_subseq5slice_range, /):
    if mk_subseq5slice_range is None:
        mk_subseq5slice_range = mk_subseq5slice_range__tuple

    if type(idx_or_slice) is slice:
        slice_ = idx_or_slice
        slice_fixed = fix_slice_by_len_of(lookupable, slice_)
        idc = slice2triple_(range, slice_fixed)
        return mk_subseq5slice_range(lookupable, slice_, idc)


    if not isinstance(idx_or_slice, int): raise IndexError(i)
    i = idx_or_slice

    L = len(lookupable)
    if not -L <= i < L: raise IndexError(i)
    try:
        return lookupable[i]
    except KeyError:
        raise IndexError(i)

class SeqAsMapping(Mapping):
    def __init__(sf, pseudo_seq, /):
        sf._pseudo_seq = pseudo_seq
    def __len__(sf, /):
        return len(sf._pseudo_seq)
    def __iter__(sf, /):
        return pseudo_seq2iter_idc(sf._pseudo_seq)
    def __contains__(sf, k, /):
        return k in pseudo_seq2idc(sf._pseudo_seq)
    def __getitem__(sf, k, /):
        if not isinstance(k, int): raise KeyError(k)
        if not (0 <= k < len(sf)): raise KeyError(k)
        try:
            return sf._pseudo_seq[k]
        except IndexError:
            raise KeyError(k)
class MappingAsSeq(Sequence):
    def __init__(sf, pseudo_seq, /, *, mk_subseq5slice_range=None):
        sf._pseudo_seq = pseudo_seq
        sf._mk_subseq5slice_range = mk_subseq5slice_range
    def __len__(sf, /):
        return len(sf._pseudo_seq)
    def __getitem__(sf, idx_or_slice, /):
        return pseudo_seq__get(sf._pseudo_seq, idx_or_slice, sf._mk_subseq5slice_range)


    r'''
    __reversed__, index...
    def __iter__(sf, /):
        return pseudo_seq2iter_values(sf._pseudo_seq)
    def __contains__(sf, k, /):
        return k in pseudo_seq2iter_values(sf._pseudo_seq)
    #'''
































from seed.seq_tools.seq_as_mapping import SeqAsMapping
from seed.seq_tools.seq_as_mapping import pseudo_seq2iter_idc, pseudo_seq2idc, pseudo_seq2iter_values, pseudo_seq2iter_items
from seed.seq_tools.seq_as_mapping import pseudo_seq2iter_idc_, pseudo_seq2idc_, pseudo_seq2iter_values_, pseudo_seq2iter_items_
from seed.seq_tools.seq_as_mapping import pseudo_seq__get, mk_subseq5slice_range__tuple


