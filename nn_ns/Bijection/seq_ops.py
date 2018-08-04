
__all__ = '''
    left_rotate_seq__strict
    reverse_seq_prefix__strict
    left_rotate_seq
    reverse_seq_prefix
    may_seq_len2len
'''.split()


def left_rotate_seq__strict(L, ls):
    # ls -> ls[L:] ++ ls[:L]
    assert 0 <= L <= len(ls)
    return ls[L:] + ls[:L]
    # left_rotate_seq L <==>
        # reverse_seq_prefix L
        # reverse_seq_prefix len(ls)
        # reverse_seq_prefix len(ls)-L
    pass

def reverse_seq_prefix__strict(L, ls):
    # ls -> reverse(ls[:L]) ++ ls[L:]
    assert 0 <= L <= len(ls)
    r = ls[L-1::-1] + ls[L:]
    assert len(r) == len(ls)
    assert L == 0 or (r[0] is ls[L-1] and r[L-1] is ls[0])
    return r
def reverse_seq_prefix(may_prefix_len, ls):
    L = may_seq_len2len(may_prefix_len, len(ls))
    return reverse_seq_prefix__strict(L, ls)
def left_rotate_seq(may_prefix_len, ls):
    L = may_seq_len2len(may_prefix_len, len(ls))
    return left_rotate_seq__strict(L, ls)
def may_seq_len2len(may_len, max_len):
    assert may_len is None or type(may_len) is int
    assert type(max_len) is int and max_len >= 0
    L = max_len
    if may_len is None:
        return max_len
    X = may_len
    if X >= 0:
        if X <= L: return X
        raise ValueError('{} == may_len > max_len == {}'.format(X, L))
    else:
        if -L <= X: return X + L
        raise ValueError('{} == may_len < -max_len == {}'.format(X, -L))
    pass


