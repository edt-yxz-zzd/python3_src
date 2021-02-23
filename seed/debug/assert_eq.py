
from seed.debug.print_err import print_err
def assert_eq(__lhs, __rhs, *, _fmt='lhs={};\nrhs={};\nvars={vars}', **vars):
    try:
        assert __lhs == __rhs
    except:
        print_err(_fmt.format(__lhs, __rhs, vars=vars))
        raise

