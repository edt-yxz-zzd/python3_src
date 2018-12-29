
__all__ = '''
    make_compact_uint2group_idx
    '''.split()

from itertools import groupby

def make_compact_uint2group_idx(num_uints, unique_uints, *, key):
    '''Eq k => unique[UInt] -> (UInt->k) -> ([UInt], [k], [PInt])
Eq k => unique_uints -> (UInt->k) -> (uint2group_idx, group_idx2key, group_idx2size)

#num_groups = len(group_idx2key)
'''
    uint2group_idx = [None]*num_uints
    group_idx2key = []
    group_idx2size = []
    for k, g in groupby(unique_uints, key=key):
        uint_block = tuple(g)
        assert uint_block

        group_idx = len(group_idx2key)
        group_idx2key.append(k)
        group_idx2size.append(len(uint_block))
        for uint in uint_block:
            if uint2group_idx[uint] is not None:
                raise ValueError('duplicate uint in unique_uints: len(set(unique_uints)) != len(list(unique_uints))')
            uint2group_idx[uint] = group_idx
    if any(i is None for i in uint2group_idx):
        raise ValueError('len(unique_uints) < num_uints')
    return uint2group_idx, group_idx2key, group_idx2size





