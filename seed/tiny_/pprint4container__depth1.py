
r'''
e ../../python3_src/seed/tiny_/pprint4container__depth1.py
seed.tiny_.pprint4container__depth1
py -m    seed.tiny_.pprint4container__depth1
py -m nn_ns.app.debug_cmd   seed.tiny_.pprint4container__depth1

from seed.tiny_.pprint4container__depth1 import pprintT4tuple__depth1, pprint4container__depth1


#'''

__all__ = '''
pprint4container__depth1
pprintT4iterable__depth1
    mk_pprintT4container__depth1
        pprintT4tuple__depth1
        pprintT4list__depth1
        pprintT4set__depth1
    mk_pprintT4mapping__depth1
        to_items
        pprintT4dict__depth1
        pprintT4dict_items__depth1

    '''.split()

from seed.tiny_.check import check_callable, check_type_is
from seed.tiny_.funcs import mk_fprint
    #no_op, echo_args_kwargs, echo_kwargs, echo_args, echo, fst, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, with_key, mk_fprint, fprint, py_cmp, int2cmp

def pprintT4iterable__depth1(open_str, close_str, /, *, sep, may_repr4empty, indent, fout, repr4element, to_elememts):

    if repr4element is None:
        repr4element = repr
    if to_elememts is None:
        to_elememts = iter
    if indent is None:
        indent = ''
    check_callable(repr4element)
    check_callable(to_elememts)
    check_type_is(str, indent)
    check_type_is(str, open_str)
    check_type_is(str, close_str)
    check_type_is(str, sep)
    print = mk_fprint(fout)
    if not may_repr4empty is None:
        repr4empty = may_repr4empty
        check_type_is(str, repr4empty)

    def pprint4iterable__depth1(iterable, /):
        iterable = iter(to_elememts(iterable)) #check iterable
        for x in iterable:
            #head ==>> first row
            print(f'{indent!s}{open_str!s}', end='')
            print(repr4element(x))
            break
        else:
            #iterable is empty ==>> one line
            if may_repr4empty is None:
                print(f'{indent!s}{open_str!s}', end='')
                print(close_str)
            else:
                print(f'{indent!s}{repr4empty!s}', end='')
            return

        for x in iterable:
            print(f'{indent!s}{sep!s}{repr4element(x)!s}')
        print(f'{indent!s}{close_str!s}')
        return
    return pprint4iterable__depth1

def mk_pprintT4container__depth1(open_str, close_str, /, *, sep, may_repr4empty):
    def pprintT4container__depth1(*, indent, fout, repr4element, to_elememts):
        pprint4container__depth1 = pprintT4iterable__depth1(open_str, close_str, sep=sep, may_repr4empty=may_repr4empty, indent=indent, fout=fout, repr4element=repr4element, to_elememts=to_elememts)
        return pprint4container__depth1
    return pprintT4container__depth1

pprintT4tuple__depth1 = mk_pprintT4container__depth1('(', ',)', sep=',', may_repr4empty='()')
pprintT4list__depth1 = mk_pprintT4container__depth1('[', ']', sep=',', may_repr4empty=None)
#pprintT4nonempty_set__depth1 = mk_pprintT4container__depth1('{', '}', sep=',', may_repr4empty=None)
pprintT4set__depth1 = mk_pprintT4container__depth1('{', '}', sep=',', may_repr4empty='set()')

to_items = lambda m:m.items()
def mk_pprintT4mapping__depth1(open_str, close_str, /, *, sep, inner_sep, may_repr4empty, repr4fst, repr4snd, to_pairs):
    if repr4fst is None:
        repr4fst = repr
    if repr4snd is None:
        repr4snd = repr
    if to_pairs is None:
        to_pairs = to_items
    if inner_sep is None:
        inner_sep = ''

    check_callable(repr4fst)
    check_callable(repr4snd)
    check_callable(to_pairs)
    check_type_is(str, inner_sep)

    def repr4element__one_line(kv, /):
        k, v = kv
        return f'{repr4fst(k)!s}{inner_sep!s}{repr4snd(v)!s}'
    def mk_repr4element(two_lines_per_item, indent, /):
        if not two_lines_per_item:
            repr4element = repr4element__one_line
        else:
            def repr4element__two_lines(kv, /):
                k, v = kv
                return f'{repr4fst(k)!s}\n{indent!s}{inner_sep!s}{repr4snd(v)!s}'
            repr4element = repr4element__two_lines
        del two_lines_per_item
        return repr4element
    to_elememts = to_pairs
    _pprintT4mapping__depth1 = mk_pprintT4container__depth1(open_str, close_str, sep=sep, may_repr4empty=may_repr4empty)
    def pprintT4mapping__depth1(*, two_lines_per_item, indent, fout):
        repr4element = mk_repr4element(two_lines_per_item, indent)
        pprint4mapping__depth1 = _pprintT4mapping__depth1(repr4element=repr4element, to_elememts=to_elememts, indent=indent, fout=fout)
        return pprint4mapping__depth1
    return pprintT4mapping__depth1
pprintT4dict__depth1 = mk_pprintT4mapping__depth1('{', '}', sep=',', inner_sep=':', may_repr4empty=None, repr4fst=None, repr4snd=None, to_pairs=None)
pprintT4dict_items__depth1 = mk_pprintT4mapping__depth1('{', '}', sep=',', inner_sep=':', may_repr4empty=None, repr4fst=None, repr4snd=None, to_pairs=iter)

def pprint4container__depth1(xs, /, *, indent='', fout=None, **kwds):
    cls = type(xs)
    kwargs = dict(indent=indent, fout=fout, repr4element=None, to_elememts=None)
    if cls is dict:
        kwargs = dict(indent=indent, fout=fout, two_lines_per_item=True)
        _pprintT = pprintT4dict__depth1
    elif cls is tuple:
        _pprintT = pprintT4tuple__depth1
    elif cls is list:
        _pprintT = pprintT4list__depth1
    elif cls is set:
        _pprintT = pprintT4set__depth1
    else:
        raise TypeError(cls)
    kwargs.update(kwds)
    return _pprintT(**kwargs)(xs)

