#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/LazyErrmsg.py
[[
!!wrong guess!!
<<==:
??? "slow"/inefficiency maybe caused by f-string/strig-formatting to generate errmsg @20240911
    TODO:++class LazyErrmsg(fmtr,*kwds4fmt)
        # see: py::string.Formatter.get_field(self, field_name, args, kwargs)[#fast check field_name be identifier instead of expr#](check_unused_args?useless)
            #or: use re directly
            #or: static-parsed-fmt...
grep "\\.format(" -i -r ../../python3_src/seed/recognize/recognizer_LLoo_/
#)
grep $"\br\\?fr\\?['\"]" -i -r ../../python3_src/seed/recognize/recognizer_LLoo_/  -l
grep $"mk_Left(" -i -r ../../python3_src/seed/recognize/recognizer_LLoo_/  -l
#)
==>> not found:mk_Left(f'...')
==>> inefficiency not caused by strig-formatting to generate errmsg
!!wrong guess!!
]]


seed.recognize.recognizer_LLoo_.LazyErrmsg
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.LazyErrmsg -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.LazyErrmsg:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.LazyErrmsg   @f
#]]]'''
__all__ = r'''
LazyErrmsg
SimpleFormatter
    FormatError
    FormattingError
    parse_simple_fmt

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import re
from seed.tiny_.check import check_type_is, check_int_ge
from seed.tiny import ifNone
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

class FormatError(Exception):pass
class FormattingError(Exception):pass
_re4fmt = re.compile(r'(?P<literal>[^{}]+)|(?P<escaped>\{\{|\}\})|\{(?P<nm>(?!\d)\w+)(?:!(?P<conversion>[rsa]))?\}')
def parse_simple_fmt(fmt, /):
    check_type_is(str, fmt)
    ls = []
        # ls[0::2] :: literal
        # ls[1::2] :: (nm, smay_conversion)
    literal_parts = []
    def put_literal5parts():
        ls.append(''.join(literal_parts))
        literal_parts.clear()
    def put_nm(nm, smay_conversion, /):
        assert 0 == len(ls)&1
            # [not ls]or[ls[-1] is (nm, smay_conversion)]
        put_literal5parts()
        assert 1 == len(ls)&1
            # [ls[-1] is literal]
        assert not literal_parts
        ls.append((nm, smay_conversion))
        assert 0 == len(ls)&1
            # [ls[-1] is (nm, smay_conversion)]

    #prev_end = 0
    #for m in _re4fmt.finditer(fmt):
        #begin, end = m.span
    j = 0
    L = len(fmt)
    while not L == (i:=j)==L:
        m = _re4fmt.match(fmt, i)
        if m is None:
            raise FormatError(fmt, i, fmt[i:i+10])
        j = m.end()
        assert i < j
        m = m.groupdict()
        if not None is (s:=m['literal']):
            literal_parts.append(s)
        elif not None is (xx:=m['escaped']):
            literal_parts.append(xx[0])
        elif not None is (nm:=m['nm']):
            smay_conversion = ifNone(m['conversion'], '')
            put_nm(nm, smay_conversion)
        else:
            raise 000

    put_literal5parts()
    assert 1 == len(ls)&1
        # [ls[-1] is literal]
    assert not literal_parts
    return ls

class SimpleFormatter:
    def __repr__(sf, /):
        return repr_helper(sf, sf._fmt)
    def __init__(sf, fmt, /):
        ls = parse_simple_fmt(fmt)
        assert 1 == len(ls)&1
        nms = frozenset(nm for nm, smay_conversion in ls[1::2])
        sf._ls = ls
        sf._nms = nms
        sf._fmt = fmt
    @property
    def names(sf, /):
        return sf._nms
    def check_names(sf, nms, /):
        if not (s:=set(nms)) == sf.names:raise FormattingError(sf.names, s)#KeyError#NameError
    def format(sf, /, **kwds):
        return sf.vformat(kwds)
    def vformat(sf, kwds, /):
        sf.check_names(kwds.keys())
        return ''.join(_iter4vformat(sf._ls, kwds))

_smay_conversion2f = {'':str,'r':repr,'s':str,'a':ascii}
def _iter4vformat(ls, kwds, /):
    is_nm = False
    for x in ls:
        if is_nm:
            check_type_is(tuple, x)
            (nm, smay_conversion) = x
            f = _smay_conversion2f[smay_conversion]
            val = kwds[nm]
            s = f(val)
        else:
            literal = x
            s = literal
        yield s
        is_nm = not is_nm

def __():
    fmt = '{vvv}{vvv!r}{{}}abc{vvv!s}{vvv!a}'
    assert ((x0:=r"我'我'{}abc我'\u6211'") == (x1:=SimpleFormatter(fmt).format(vvv='我'))), (x0,x1)
    assert (x0 == (x2:=fmt.format(vvv='我'))), (x0,x1,x2)
__()
#end-class SimpleFormatter:


class LazyErrmsg:
    def __init__(sf, may_fmtr, may_errmsg=None, /, **kwds):
        if may_fmtr is None is may_errmsg: raise TypeError
        if not may_errmsg is None:
            check_type_is(str, may_errmsg)
        if not may_fmtr is None:
            check_type_is(SimpleFormatter, may_fmtr)
        else:
            if kwds:raise TypeError

        sf._fmtr = may_fmtr
        sf._kwds = kwds
        sf._s = may_errmsg
        sf._m = None
    def unlazy(sf, /):
        if sf._m is None:
            if sf._s is None:
                s = sf._fmtr.vformat(sf._kwds)
            else:
                s = sf._s
            sf._m = f'[<LazyErrmsg:{s!r}>]'
        return sf._m
    def __str__(sf, /):
        return sf.unlazy()
    def __repr__(sf, /):
        if sf._s is None:
            return repr_helper(sf, sf._fmtr, **sf._kwds)
        return repr_helper(sf, sf._fmtr, sf._s, **sf._kwds)
def __():
    fmt = '{vvv}{vvv!r}{{}}abc{vvv!s}{vvv!a}'
    lazy_errmsg = LazyErrmsg(SimpleFormatter(fmt), vvv='我')

    assert (r:=repr(lazy_errmsg)) == "LazyErrmsg(SimpleFormatter('{vvv}{vvv!r}{{}}abc{vvv!s}{vvv!a}'), vvv = '我')", r
    assert (r:=str(lazy_errmsg)) == r'''[<LazyErrmsg:"我'我'{}abc我'\\u6211'">]''', r

    lazy_errmsg = LazyErrmsg(None, 'uuu')
    assert (r:=repr(lazy_errmsg)) == "LazyErrmsg(None, 'uuu')", r
    assert (r:=str(lazy_errmsg)) == r'''[<LazyErrmsg:'uuu'>]''', r

__()
#end-class LazyErrmsg:





__all__
from seed.recognize.recognizer_LLoo_.LazyErrmsg import LazyErrmsg, SimpleFormatter
from seed.recognize.recognizer_LLoo_.LazyErrmsg import *
