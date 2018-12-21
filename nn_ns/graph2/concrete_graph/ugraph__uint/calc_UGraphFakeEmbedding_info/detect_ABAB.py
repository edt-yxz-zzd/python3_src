
__all__ = '''
    detect_ABAB
    '''.split()


from seed.tiny import echo
import operator

def detect_ABAB(obj_seq, buffer__key2max_idx, *, key=None, __eq__=None):
    '''
input:
    obj_seq :: Iter obj
    buffer__key2max_idx :: Map key UInt
        # e.g. seed.types.OneTime.OneTimeMap
    key :: obj -> key
    __eq__ :: key -> key -> Bool
output:
    ()|(idx, idx, idx, idx)
        if ():
            no ABAB
        else:
            ABAB


example:
    >>> key_map = {}
    >>> detect_ABAB('', key_map)
    ()
    >>> detect_ABAB('112A23443', key_map)
    ()
    >>> detect_ABAB('00110221', key_map)
    (1, 3, 4, 7)
'''
    obj2key = key if key is not None else echo
    if __eq__ is None:
        __eq__ = operator.__eq__

    buffer__key2max_idx.clear()
    inner_idx2may_min_range_snd_idx = []
    range_snd_idx2may_range_fst_idx = []
    stack = []
    for i, key in enumerate(map(obj2key, obj_seq)):
        range_snd_idx2may_range_fst_idx.append(None)
        inner_idx2may_min_range_snd_idx.append(None)

        may_max_idx = buffer__key2max_idx.setdefault(key, i)
        if may_max_idx < i:
            # key in old buffer__key2max_idx
            buffer__key2max_idx[key] = i

            i_ = max_idx = may_max_idx
            range_snd_idx2may_range_fst_idx[i] = i_
            may_pair_snd_idx = inner_idx2may_min_range_snd_idx[i_]
            if may_pair_snd_idx is not None:
                # done!
                pair_snd_idx = may_pair_snd_idx
                pair_fst_idx = range_snd_idx2may_range_fst_idx[pair_snd_idx]
                assert pair_fst_idx is not None
                assert pair_fst_idx < i_ < pair_snd_idx < i
                return (pair_fst_idx, i_, pair_snd_idx, i)

            while True:
                i_ = stack.pop()
                if i_ == max_idx:
                    break
                else:
                    inner_idx2may_min_range_snd_idx[i_] = i
        stack.append(i)

    return ()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


