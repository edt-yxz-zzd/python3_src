


__all__ = '''
    neg_inf
    check_depth
    verify_depth
    '''.split()

neg_inf = float('-inf')

def check_depth(depth):
    if not verify_depth(depth): raise TypeError
    return True
def verify_depth(depth):
    return depth >= 0 or depth == neg_inf


