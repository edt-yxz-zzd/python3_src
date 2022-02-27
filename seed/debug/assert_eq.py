r"""
    assert_eq           # :: lhs -> rhs -> (_fmt=...) -> **vars -> ()
    assert_eq_f         # :: ans -> f -> *args -> (_fmt=...) -> **vars -> ()
    mk_assert_eq_f      # :: (_fmt=...) -> **vars -> (ans -> f -> *args -> **kwargs -> ())

from seed.tiny import assert_eq, assert_eq_f, mk_assert_eq_f
from seed.debug.assert_eq import assert_eq, assert_eq_f, mk_assert_eq_f
#"""

__all__ = '''
    assert_eq
    assert_eq_f
    mk_assert_eq_f
    '''.split()

from seed.debug.print_err import print_err
def assert_eq(__lhs, __rhs, /, *, _fmt='lhs={!r};\nrhs={!r};\nvars={vars!r}', **vars):
    try:
        assert __lhs == __rhs
    except:
        print_err(_fmt.format(__lhs, __rhs, vars=vars))
        raise
def assert_eq_f(ans, f, /, *args, _fmt='ans={!r};\nresult={!r}={!s}{!r};\nvars={vars!r}', **vars):
    try:
        r = f(*args)
    except:
        print_err(_fmt.format(ans, "??err:exception??", f.__name__, args, vars=vars))
        raise
    try:
        assert ans == r
    except:
        print_err(_fmt.format(ans, r, f.__name__, args, vars=vars))
        raise
def mk_assert_eq_f(_fmt='ans={!r};\nresult={!r}={!s}(*{!r}, **{!r});\nvars={vars!r}', /, **vars):
    def assert_eq_f(ans, f, /, *args, **kwargs):
        try:
            r = f(*args, **kwargs)
        except:
            print_err(_fmt.format(ans, "??err:exception??", f.__name__, args, kwargs, vars=vars))
            raise
        try:
            assert ans == r
        except:
            print_err(_fmt.format(ans, r, f.__name__, args, kwargs, vars=vars))
            raise
    return assert_eq_f

