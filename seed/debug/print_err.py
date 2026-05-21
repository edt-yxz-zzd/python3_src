
'''
see:
    no_op

usage:
    _debug_ = True
    if _debug_:
        from seed.debug.print_err import print_err, print_ferr
    else:
        from seed.tiny_.funcs import no_op as print_err

    print_ferr(lambda: f'{i}')

'''
__all__ = '''
    print_err
    print_ferr
    '''.split()
import sys

def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
def print_ferr(*fargs, **kwargs):
    args = (f() for f in fargs)
    print(*args, file=sys.stderr, **kwargs)


from seed.debug.print_err import print_err, print_ferr
