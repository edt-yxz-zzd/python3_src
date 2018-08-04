



def char_range(a, z):
    return map(chr, range(ord(a), ord(z)+1))

__prefix_chars = frozenset(char_range(*'az')) | frozenset(char_range(*'AZ'))
def get_unused_prefix(prefix, names, alphabet=__prefix_chars):
    '''when we want to make a new id, we make a unused prefix first

pre = get_unused_prefix(prefix, names, alphabet)
assert pre.startswith(prefix)
assert not any(name.startswith(pre) for name in names)
assert set(pre[len(prefix):]) <= alphabet
alphabet is a set<char>

NOTE: pre may be empty
'''
    names = list(names)
    pre = _get_unused_prefix(prefix, names, alphabet)
    assert pre.startswith(prefix)
    assert not any(name.startswith(pre) for name in names)
    assert set(pre[len(prefix):]) <= alphabet
    return pre
    
def _get_unused_prefix(prefix, names, alphabet):
    min_ = min(alphabet)
    while True:
        names = set(name for name in names if name.startswith(prefix))
        if not names:
            return prefix
        
        i = len(prefix)
        not_next_chars = set(name[i] for name in names if len(name) > i)
        next_chars = alphabet - not_next_chars
        if not next_chars:
            next_char = min_
        else:
            next_char = min(next_chars)
        prefix += next_char

    
