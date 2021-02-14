
r'''
scene:
    try:
        assert ans == result
    except:
        i = diff_str(ans, result)
        print(ans[:i])
        print(ans[i:])
        print(result[i:])
        raise
#'''

__all__ = '''
    fst_diff_idx_of__seq
    diff_str
    assert_seq_eq
    '''.split()

from seed.tiny import print_err



def fst_diff_idx_of__seq(lhs, rhs):
    i = -1
    for i, (x, y) in enumerate(zip(lhs, rhs)):
        try:
            b = x==y
        except:
            b = False
        if not b:
            return i
    return i+1

diff_str = fst_diff_idx_of__seq
assert 4 == diff_str('0123', '0123')
assert 2 == diff_str('0123', '01x3')

assert 0 == diff_str('y123', '01x3')
assert 3 == diff_str('012', '0123')

def assert_seq_eq(lhs, rhs):
    try:
        assert lhs == rhs
    except AssertionError:
        i = fst_diff_idx_of__seq(lhs, rhs)
        s = '='*20
        t = '\n'*6

        print_err(t)
        print_err(f'{s}common prefix:len={i}{s}')
        print_err(lhs[:i])

        print_err(t)
        print_err(s + 'lhs' + s)
        print_err(lhs[i:])

        print_err(t)
        print_err(s + 'rhs' + s)
        print_err(rhs[i:])
        raise

