


'''
usage source:
    def sympy_fraction2py_fraction(fr):
        N, D = map(int, sympy.fraction(fr))
        return Fraction(N, D)
    def sympy_mx2lsls(mx):
        R = mx.rows
        C = mx.cols
        lsls = [list(mx[r, :]) for r in range(R)]
        return lsls


    def lsls_of_sympy_fraction2py_fraction(lsls):
        return deep_map(2, sympy_fraction2py_fraction, lsls)
    def sympy_mx2lsls_with_fraction_convert(mx):
        return lsls_of_sympy_fraction2py_fraction(sympy_mx2lsls(mx))
        
'''

from ..types.pair_based_leftward_list import to_leftward_list
def deep_map_funcs(funcs, ls):
    'deep_map_funcs((tuple, None, set), [[[1]]]) == ([{1}],)'
    funcs = to_leftward_list(funcs)
    
def __deep_map_funcs_impl(funcs, x):
    if not funcs:
        return x
    ls = x
    f, funcs = funcs
    if f is None:
        f = type(x)
    return f(__deep_map_funcs_impl(funcs, x) for x in ls)

assert deep_map_funcs((tuple, None, set), [[[1]]]) == ([{1}],)


if 0:
    # reserve for old code query
    def deep_map(n, f, ls):
        funcs = [f,]*n
        funcs.append(type(ls))
        return deep_map_funcs(funcs, ls)

    # deprecated
    def deep_map(n, f, ls):
        T = type(ls)
        if n > 1:
            return T(deep_map(n-1, f, sub_ls) for sub_ls in ls)
        if n == 0:
            return T(ls)
        if n == 1:
            return T(map(f, ls))

        if not isinstance(n, int):
            raise TypeError('not isinstance(n, int)')
        if n < 0:
            raise ValueError('n < 0')

        raise ValueError('unkown')
