
r'''
e ../../python3_src/seed/tiny_/pprint4container__depth1.py
seed.tiny_.pprint4container__depth1
py -m    seed.tiny_.pprint4container__depth1
py -m nn_ns.app.debug_cmd   seed.tiny_.pprint4container__depth1

from seed.tiny_.pprint4container__depth1 import pprint4container__depth1
from seed.tiny_.pprint4container__depth1 import show5pprint, mk_fshow5pprint, show5pprint__fout

see:
    view ../../python3_src/seed/helper/stable_repr.py
        from seed.helper.stable_repr import stable_repr




#def pprint4container__depth1(xs, /, *, indent='', fout=None, **kwds):
>>> show5pprint__fout(pprint4container__depth1, [2, 1])
'[2\n,1\n]\n'
>>> show5pprint__fout(pprint4container__depth1, (2, 1))
'(2\n,1\n,)\n'
>>> show5pprint__fout(pprint4container__depth1, {2, 1})
'{1\n,2\n}\n'
>>> show5pprint__fout(pprint4container__depth1, {2:3, 1:4})
'{1\n:4\n,2\n:3\n}\n'

>>> show5pprint__fout(pprint4container__depth1, [])
'[]\n'
>>> show5pprint__fout(pprint4container__depth1, ())
'()\n'
>>> show5pprint__fout(pprint4container__depth1, {*[]})
'set()\n'
>>> show5pprint__fout(pprint4container__depth1, {})
'{}\n'


>>> pprint4container__depth1({12:3, 4:5})
{12
:3
,4
:5
}
>>> pprint4container__depth1({12:3, 4:5}, two_lines_per_item=False)
{12:3
,4:5
}
>>> pprint4container__depth1({12:3, 4:5}, two_lines_per_item=False, sort_by_=('keyfunc', None))
{12:3
,4:5
}
>>> pprint4container__depth1({12:3, 4:5}, two_lines_per_item=False, sort_by_=('keyfunc', repr))
{12:3
,4:5
}
>>> pprint4container__depth1({12:3, 4:5}, two_lines_per_item=False, sort_by_=('keyfunc', echo))
{4:5
,12:3
}


######################
######################
######################API ++sort_by_, update ...
######################
######################
$ grep 'pprintT\?4' -r ../../python3_src/ -l
    ./nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py
    ./seed/tiny_/pprint4container__depth1.py
    ./自己的相关数据/on_working.txt

$ grep 'pprintT\?4' -r ../../txt_phone/txt/ -l
    ./script/download_zxcs_novel/collect_links_from_zxcs_sort_pages.py
    ./script/download_zxcs_novel/extract_scores_from_zxcs_novel_page.py
        using pprintT4dict_items__depth1
            fixed



#'''

__all__ = '''
show5pprint
    mk_fshow5pprint
    show5pprint__fout

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

from io import StringIO
from seed.func_tools.dot2 import dot
from seed.tiny_.check import check_callable, check_type_is
from seed.tiny_.funcs import mk_fprint, fst, echo
    #no_op, echo_args_kwargs, echo_kwargs, echo_args, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, with_key, mk_fprint, fprint, py_cmp, int2cmp


def show5pprint(kw_name__or__args_idx___4fout, pprint, /, *args4pprint, **kwargs4pprint):
    fout = StringIO()
    cls = type(kw_name__or__args_idx___4fout)
    if cls is str:
        kw_name4fout = kw_name__or__args_idx___4fout
        pprint(*args4pprint, **kwargs4pprint, **{kw_name4fout:fout})
    elif cls is int:
        args_idx4fout = kw_name__or__args_idx___4fout
        args4pprint = [*args4pprint]
        args4pprint.insert(args_idx4fout, fout)
        pprint(*args4pprint, **kwargs4pprint)
    else:
        raise TypeError(f'kw_name__or__args_idx___4fout is not str/int: {cls!r}')
    txt = fout.getvalue()
    return txt
def mk_fshow5pprint(kw_name__or__args_idx___4fout, /):
    def fshow5pprint(pprint, /, *args4pprint, **kwargs4pprint):
        return show5pprint(kw_name__or__args_idx___4fout, pprint, *args4pprint, **kwargs4pprint)
    return fshow5pprint
show5pprint__fout = mk_fshow5pprint('fout')

def pprintT4iterable__depth1(open_str, close_str, /, *, sep, may_repr4empty, indent, fout, repr4element, to_elememts:'dot[sorted, iter]', sort_by_:"None/('keyfunc', may callable)/('sortfunc4elements', may callable)", default_sort_by_:"('keyfunc', may callable)/('sortfunc4elements', may callable)", default_keyfunc4sort_by_:callable, default_sortfunc4elements4sort_by_:callable):#, default_repr:callable

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

    if sort_by_ is None:
        #sort_by_ = ('keyfunc', None)
        #sort_by_ = ('sortfunc4elements', None)
        sort_by_ = default_sort_by_
    check_type_is(tuple, sort_by_)
    check_callable(default_keyfunc4sort_by_)
    check_callable(default_sortfunc4elements4sort_by_)

    def _4sort_by_():
        case4sort_by_, payload4sort_by_ = sort_by_
        check_type_is(str, case4sort_by_)
        if not case4sort_by_ in ('keyfunc', 'sortfunc4elements'):raise TypeError
        if case4sort_by_ == 'keyfunc':
            may_keyfunc = payload4sort_by_
            if may_keyfunc is None:
                keyfunc = default_keyfunc4sort_by_#repr4element#repr4fst
            else:
                keyfunc = may_keyfunc
            check_callable(keyfunc)
            def sortfunc4elements(xs, /):
                return iter(sorted(xs, key=keyfunc))
        elif case4sort_by_ == 'sortfunc4elements':
            may_sortfunc4elements = payload4sort_by_
            if may_sortfunc4elements is None:
                #??no_sort
                sortfunc4elements = default_sortfunc4elements4sort_by_#iter
            else:
                sortfunc4elements = may_sortfunc4elements
            check_callable(sortfunc4elements)
        else:
            raise logic-err
        return sortfunc4elements
    sortfunc4elements = _4sort_by_()
    to_elememts = dot[sortfunc4elements, to_elememts]

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
                #bug:print(f'{indent!s}{repr4empty!s}', end='')
                #   miss EOL
                print(f'{indent!s}{repr4empty!s}')
            return

        for x in iterable:
            print(f'{indent!s}{sep!s}{repr4element(x)!s}')
        print(f'{indent!s}{close_str!s}')
        return
    return pprint4iterable__depth1

def mk_pprintT4container__depth1(open_str, close_str, /, *, sep, may_repr4empty, default_sort_by_, default_keyfunc4sort_by_, default_sortfunc4elements4sort_by_):
    def pprintT4container__depth1(*, indent, fout, repr4element, to_elememts, sort_by_):
        pprint4container__depth1 = pprintT4iterable__depth1(open_str, close_str, sep=sep, may_repr4empty=may_repr4empty, indent=indent, fout=fout, repr4element=repr4element, to_elememts=to_elememts, sort_by_=sort_by_, default_sort_by_=default_sort_by_, default_keyfunc4sort_by_=default_keyfunc4sort_by_, default_sortfunc4elements4sort_by_=default_sortfunc4elements4sort_by_)
        return pprint4container__depth1
    return pprintT4container__depth1

_kws4no_sort = dict(default_sort_by_=('sortfunc4elements', None), default_keyfunc4sort_by_=repr, default_sortfunc4elements4sort_by_=iter)
_kws4sort4elems = dict(default_sort_by_=('keyfunc', None), default_keyfunc4sort_by_=repr, default_sortfunc4elements4sort_by_=dot[iter, sorted])
pprintT4tuple__depth1 = mk_pprintT4container__depth1('(', ',)', sep=',', may_repr4empty='()', **_kws4no_sort)
pprintT4list__depth1 = mk_pprintT4container__depth1('[', ']', sep=',', may_repr4empty=None, **_kws4no_sort)
#pprintT4nonempty_set__depth1 = mk_pprintT4container__depth1('{', '}', sep=',', may_repr4empty=None)
pprintT4set__depth1 = mk_pprintT4container__depth1('{', '}', sep=',', may_repr4empty='set()', **_kws4sort4elems)


to_items = lambda m:m.items()
def mk_pprintT4mapping__depth1(open_str, close_str, /, *, sep, inner_sep, may_repr4empty, repr4fst, repr4snd, to_pairs:'dot[sorted, to_items]', default_sort_by_, default_keyfunc4sort_by_, default_sortfunc4elements4sort_by_):
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


    if default_sort_by_ is None:
        default_sort_by_ = ('keyfunc', None)
    if default_keyfunc4sort_by_ is None:
        default_keyfunc4sort_by_ = repr4fst
    default_keyfunc4sort_by_ = dot[default_keyfunc4sort_by_, fst]

    if default_sortfunc4elements4sort_by_ is None:
        default_sortfunc4elements4sort_by_ = dot[iter, sorted]


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

    _kws4sort4items = dict(default_sort_by_=default_sort_by_, default_keyfunc4sort_by_=default_keyfunc4sort_by_, default_sortfunc4elements4sort_by_=default_sortfunc4elements4sort_by_)
    _pprintT4mapping__depth1 = mk_pprintT4container__depth1(open_str, close_str, sep=sep, may_repr4empty=may_repr4empty, **_kws4sort4items)
    to_elememts = to_pairs
    def pprintT4mapping__depth1(*, two_lines_per_item, indent, fout, sort_by_):
        repr4element = mk_repr4element(two_lines_per_item, indent)
        if sort_by_ is not None:
            case4sort_by_, payload4sort_by_ = sort_by_
            if payload4sort_by_ is not None and case4sort_by_ == 'keyfunc':
                keyfunc = payload4sort_by_
                keyfunc = dot[keyfunc, fst]
                payload4sort_by_ = keyfunc
                sort_by_ = case4sort_by_, payload4sort_by_
        pprint4mapping__depth1 = _pprintT4mapping__depth1(repr4element=repr4element, to_elememts=to_elememts, indent=indent, fout=fout, sort_by_=sort_by_)
        return pprint4mapping__depth1
    return pprintT4mapping__depth1

_kws4sort4items__None = dict(default_sort_by_=None, default_keyfunc4sort_by_=None, default_sortfunc4elements4sort_by_=None)
pprintT4dict__depth1 = mk_pprintT4mapping__depth1('{', '}', sep=',', inner_sep=':', may_repr4empty=None, repr4fst=None, repr4snd=None, to_pairs=None, **_kws4sort4items__None)
pprintT4dict_items__depth1 = mk_pprintT4mapping__depth1('{', '}', sep=',', inner_sep=':', may_repr4empty=None, repr4fst=None, repr4snd=None, to_pairs=iter, **_kws4sort4items__None)

def pprint4container__depth1(xs, /, *, indent='', fout=None, sort_by_=None, **kwds):
    cls = type(xs)
    basic_kwargs = dict(indent=indent, fout=fout, sort_by_=sort_by_)
    extra_kwargs4elems = dict(repr4element=None, to_elememts=None)
    extra_kwargs4items = dict(two_lines_per_item=True)

    if cls is dict:
        extra_kwargs = extra_kwargs4items
        _pprintT = pprintT4dict__depth1
    elif cls is tuple:
        extra_kwargs = extra_kwargs4elems
        _pprintT = pprintT4tuple__depth1
    elif cls is list:
        extra_kwargs = extra_kwargs4elems
        _pprintT = pprintT4list__depth1
    elif cls is set:
        extra_kwargs = extra_kwargs4elems
        _pprintT = pprintT4set__depth1
    else:
        raise TypeError(cls)
    kwargs = dict(**basic_kwargs, **extra_kwargs)#no overwrite
    kwargs.update(kwds)#allow overwrite
    return _pprintT(**kwargs)(xs)




if __name__ == "__main__":
    import doctest
    doctest.testmod()
