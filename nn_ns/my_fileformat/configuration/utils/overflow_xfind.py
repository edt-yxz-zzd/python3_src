'''
diff with str.find!!
    str.find return -1 when fail
    but this module return begin-1 or end when fail
'''

__all__ = '''
    overflow_xfind
    overflow_rfind
    overflow_find
    '''.split()

def _overflow_find_common(pred, s, begin, end):
    assert 0 <= begin <= end <= len(s)
    if callable(pred):
        pass
    elif hasattr(pred, '__contains__'):
        c = pred
        pred = lambda x: x in c
    else:
        raise TypeError('pred should be callable or container')
    return pred


def overflow_xfind(pred, s, begin, end, *, reverse:bool):
    # fail: begin-1 or end
    pred = _overflow_find_common(pred, s, begin, end)
    reverse = bool(reverse)

    it = range(begin, end)
    if reverse:
        it = reversed(it)

    default = begin-1 if reverse else end
    for i in it:
        if pred(s[i]):
            break
    else:
        i = default
    return i
def overflow_rfind(pred, s, begin, end):
    # fail: begin-1
    return overflow_xfind(pred, s, begin, end, reverse=True)
def overflow_find(pred, s, begin, end):
    # fail: end
    return overflow_xfind(pred, s, begin, end, reverse=False)


