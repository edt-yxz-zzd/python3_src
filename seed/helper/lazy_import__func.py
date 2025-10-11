#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import__func.py

seed.helper.lazy_import__func
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import__func -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func:__doc__ -ht # -ff -df

[[
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7ast import mk_decorator4lazy_import__funcs_, decorator4lazy_import__funcs_

===
usage:
from seed.helper.lazy_import__func import lazy_import4func_
lazy_import4func_('seed.tiny', 'echo', __name__)
    ##if toplevel then almost eqv:
echo = lazy_import4func_('seed.tiny', 'echo')
    ##not overwrite global.echo
best:
echo = lazy_import4func_('seed.tiny', 'echo', __name__)

lazy_import4func_('seed.tiny', 'ifNone', __name__, '_ifNone_')
    ##if toplevel then almost eqv:
_ifNone_ = lazy_import4func_('seed.tiny', 'ifNone')
    ##not overwrite global._ifNone_
best:
_ifNone_ = lazy_import4func_('seed.tiny', 'ifNone', __name__, '_ifNone_')

===
usage:
from seed.helper.lazy_import__func import lazy_import4funcs_
lazy_import4funcs_('seed.tiny', 'fst,snd:_snd_', __name__)
    ##if toplevel then almost eqv:
[fst,_snd_] = lazy_import4funcs_('seed.tiny', 'fst,snd')
    ##not overwrite global.fst/_snd_
best:
[fst,_snd_] = lazy_import4funcs_('seed.tiny', 'fst,snd:_snd_', __name__)

===
usage:
from seed.helper.lazy_import__func7ast import mk_decorator4lazy_import__funcs_, decorator4lazy_import__funcs_
@decorator4lazy_import__funcs_
def __():
    from seed.tiny import fst, snd as _snd_
    ##if toplevel then eqv:
@mk_decorator4lazy_import__funcs_(__name__)
def __():
    from seed.tiny import fst, snd as _snd_


]]
[[
force_lazy_imported_func_:
old:
    (echo(0) or echo)
now:
    force_lazy_imported_func_(echo)
]]



######################
>>> import seed.helper.lazy_import__func as this_mdl
>>> this_mdl.check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'check_int_ge'
>>> this_mdl._check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_check_int_ge'
>>> x = lazy_import4func_('seed.tiny_.check', 'check_int_ge')
>>> this_mdl.check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'check_int_ge'
>>> this_mdl._check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_check_int_ge'
>>> x = lazy_import4func_('seed.tiny_.check', 'check_int_ge', __name__, '_check_int_ge')
>>> this_mdl.check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'check_int_ge'
>>> this_mdl._check_int_ge # yes:sf
_LazyImport4Func('seed.tiny_.check', 'check_int_ge', 'seed.helper.lazy_import__func', '_check_int_ge')
>>> this_mdl._check_int_ge(0, 1)
>>> this_mdl._check_int_ge # yes:f #doctest: +ELLIPSIS
<function check_int_ge at 0x...>
>>> x = lazy_import4func_('seed.tiny_.check', 'check_int_ge', __name__)
>>> this_mdl.check_int_ge # yes:sf
_LazyImport4Func('seed.tiny_.check', 'check_int_ge', 'seed.helper.lazy_import__func', '')
>>> this_mdl.check_int_ge(0, 1)
>>> this_mdl.check_int_ge # yes:f #doctest: +ELLIPSIS
<function check_int_ge at 0x...>




######################
>>> import seed.helper.lazy_import__func as this_mdl
>>> this_mdl.echo # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'echo'
>>> this_mdl._echo_ # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_echo_'
>>> x = lazy_import4func_('seed.tiny', 'echo', __name__)
>>> y = lazy_import4func_('seed.tiny', 'echo', __name__, '_echo_')
>>> this_mdl.echo # yes:sf
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '')
>>> this_mdl._echo_ # yes:sf
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '_echo_')
>>> this_mdl.echo(666)
666
>>> this_mdl._echo_(999)
999
>>> this_mdl.echo # yes:f #doctest: +ELLIPSIS
<function <lambda> at 0x...>
>>> this_mdl._echo_ # yes:f #doctest: +ELLIPSIS
<function <lambda> at 0x...>
>>> x
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '')
>>> y
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '_echo_')


######################
>>> import seed.helper.lazy_import__func as this_mdl
>>> this_mdl.fst # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'fst'
>>> this_mdl._snd_ # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_snd_'
>>> xs = lazy_import4funcs_('seed.tiny', 'fst,snd:_snd_', __name__)
>>> this_mdl.fst # yes:sf
_LazyImport4Func('seed.tiny', 'fst', 'seed.helper.lazy_import__func', '')
>>> this_mdl._snd_ # yes:sf
_LazyImport4Func('seed.tiny', 'snd', 'seed.helper.lazy_import__func', '_snd_')
>>> this_mdl.fst([666,999])
666
>>> this_mdl._snd_([666,999])
999
>>> this_mdl.fst # yes:f #doctest: +ELLIPSIS
<function fst at 0x...>
>>> this_mdl._snd_ # yes:f #doctest: +ELLIPSIS
<function snd at 0x...>
>>> xs
[_LazyImport4Func('seed.tiny', 'fst', 'seed.helper.lazy_import__func', ''), _LazyImport4Func('seed.tiny', 'snd', 'seed.helper.lazy_import__func', '_snd_')]

######################



[[
py_adhoc_call   seed.helper.lazy_import__func   ,str.filter_FromImportStmt6seed_tiny :'mk_tuple,echo'
===
from seed.helper.Echo import echo, theEcho
from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple, mk_Just, mk_Left, mk_Right
from seed.tiny_.funcs import no_op, echo_args_kwargs, echo_kwargs, echo_args, echo, unbox_, unbox, fst, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, not_, with_key, mk_fprint, fprint, py_cmp, int2cmp, set_doc_

]]
[[
py_adhoc_call   seed.helper.lazy_import__func   ,str.filter_FromImportStmt6seed_tiny :'mk_tuple,echo' | py -m seed.helper.lazy_import__func
===
lazy_import4funcs_('seed.helper.Echo', 'echo,theEcho', __name__)
if 0:from seed.helper.Echo import echo, theEcho

lazy_import4funcs_('seed.tiny_.containers', 'null_str,null_bytes,null_int,null_tuple,null_frozenset,null_mapping_view,null_iter,mk_frozenset,mk_tuple,mk_Just,mk_Left,mk_Right', __name__)
if 0:from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple, mk_Just, mk_Left, mk_Right

lazy_import4funcs_('seed.tiny_.funcs', 'no_op,echo_args_kwargs,echo_kwargs,echo_args,echo,unbox_,unbox,fst,snd,const,lazy,lazy_raise_v,lazy_raise_f,eq,not_eq,is_,not_is,in_,not_in,flip,neg_flip,xor,xnor,not_,with_key,mk_fprint,fprint,py_cmp,int2cmp,set_doc_', __name__)
if 0:from seed.tiny_.funcs import no_op, echo_args_kwargs, echo_kwargs, echo_args, echo, unbox_, unbox, fst, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, not_, with_key, mk_fprint, fprint, py_cmp, int2cmp, set_doc_
]]


]]]'''#'''
__all__ = r'''
lazy_import4func_
    lazy_import4funcs_
force_lazy_imported_func_

filter_FromImportStmt6seed_tiny
    main4convert_FromImportStmt
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import cached_property

from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name
from seed.tiny_.check import check_callable
from seed.pkg_tools.import_object import import_object, import4qobject
#def import4qobject(may_qname4module, may_qname4obj, /):


#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

def _inject_(sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst, /):
    if 0b0000:
        from seed.tiny import print_err
        print_err((sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst))
    f = sf if may_func8dst is None else may_func8dst
    if smay_qnm4mdl8dst:
        #inject...
        qnm4mdl8dst = smay_qnm4mdl8dst
        nm4func8dst = smay_nm4func8dst
        mdl8dst = import4qobject(qnm4mdl8dst, None)
        ########
        try:
            #x = import4qobject(mdl8dst, nm4func8dst)
            x = getattr(mdl8dst, nm4func8dst)
        except AttributeError:
            #ok
            pass
        else:
            if not x is sf:
                raise Exception('dst exist:', (mdl8dst, nm4func8dst), (sf, x), (id(sf), id(x)))
        ########
        setattr(mdl8dst, nm4func8dst, f)
        x = getattr(mdl8dst, nm4func8dst)
        if not x is f:raise Exception('setattr fail?:', (mdl8dst, nm4func8dst), x, f)
        ########

class _LazyImport4Func:
    @cached_property
    def _func_(sf, /):
        (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst) = sf._args
        f = import4qobject(qnm4mdl8src, qnm4func8src)
        check_callable(f)
        _inject_(sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst:=f)
        return f
    def __init__(sf, qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst, /):
        sf._args4repr = (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst)
        check_pseudo_qual_name(qnm4mdl8src)
        check_pseudo_qual_name(qnm4func8src)
        check_smay_pseudo_qual_name(smay_qnm4mdl8dst)
        check_smay_pseudo_identifier(smay_nm4func8dst)
        if smay_nm4func8dst and not smay_qnm4mdl8dst:raise TypeError
        if smay_qnm4mdl8dst and not smay_nm4func8dst:
            check_pseudo_identifier(smay_nm4func8dst:=qnm4func8src)
        assert bool(smay_qnm4mdl8dst) is bool(smay_nm4func8dst)
        sf._args = (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst)

    def __call__(sf, /, *args, **kwds):
        return sf._func_(*args, **kwds)
    def __repr__(sf, /):
        from seed.helper.repr_input import repr_helper
        return repr_helper(sf, *sf._args4repr)
def lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst='', smay_nm4func8dst='', /):
    sf = _LazyImport4Func(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst)
    (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst) = sf._args
        # updated:smay_nm4func8dst
    _inject_(sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst:=None)
    return sf
def lazy_import4funcs_(qnm4mdl8src, xqnms4func8src, smay_qnm4mdl8dst='', /):
    r'''[[[
    [xqnms4func8src :: (Iter xqnm4func8src) | xqnms4func8src__str]
    [xqnms4func8src__str <- regex"{xqnm4func8src}(,{xqnm4func8src})*"]
    [xqnm4func8src <- regex"{qnm4func8src}(:{nm4func8dst})?"]
    #]]]'''#'''
    if type(xqnms4func8src) is str:
        xqnms4func8src = xqnms4func8src.split(',')
    xs = []
    for xqnm4func8src in xqnms4func8src:
        qnm4func8src, _, smay_nm4func8dst = xqnm4func8src.partition(':')
        x = lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst)
        xs.append(x)
    return xs

def force_lazy_imported_func_(f, /):
    if type(f) is _LazyImport4Func:
        f = f._func_
    return f

class _LazyData:
    @cached_property
    def regex4FromImportStmt(sf, /):
        import re
        regex4FromImportStmt = re.compile(r'^(\s*)from\s+(\S+)\s+import\s+([^()#]+|[(][^()#]+[)]\s+)((?:#.*)?)$')
        return regex4FromImportStmt
    def parse4regex4FromImportStmt(sf, match_obj, /):
        (indent, qnm4mdl, import_list, smay_comment) = match_obj.groups()
        import_list = import_list.replace('(', ' ').replace(')', ' ').strip()
        import_list = ' '.join(import_list.split())
        _import_list = import_list.replace(' as ', ':').replace(' ', '')
        line = match_obj.group(0)
        content = line.strip()
        s = f"{indent}lazy_import4funcs_('{qnm4mdl}', '{_import_list}', __name__)\n{indent}if 0:{content}"
        return (s, (indent, qnm4mdl, _import_list, smay_comment, content))
_lazy_data = _LazyData()

#.def main4convert_FromImportStmt6seed_tiny(nms4funcs, /):
#.    'deeper and lazy version of "from seed.tiny import ..."'
def filter_FromImportStmt6seed_tiny(nms4funcs, /):
    'deeper version of "from seed.tiny import ..."'
    import re
    from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
    from seed.tiny_.containers import mk_tuple__split_first_if_str
    from seed.tiny_.check import check_pseudo_identifier, check_all_

    nms4funcs = mk_tuple__split_first_if_str(nms4funcs, ',')
    check_all_(check_pseudo_identifier, nms4funcs)
    s = '|'.join(nms4funcs)
    s = fr'\b(?:{s})\b'
    regex8nms = re.compile(s)
    txt = read_under_pkg_('seed', 'tiny.py', xencoding='u8')
    for line in txt.split('\n'):
        if not line.startswith('from '):
            continue
        if line.startswith('from seed.tiny import '):
            continue
        j = line.find(mid:=' import ')
        if j == -1:
            continue
        m = regex8nms.search(line[j+len(mid):])
        if not m:
            continue
        yield line

def main4convert_FromImportStmt(args=None, /):
    regex4FromImportStmt = _lazy_data.regex4FromImportStmt
    parse4regex4FromImportStmt = _lazy_data.parse4regex4FromImportStmt
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description=r'''convert "from xxx.yyy import aaa, bbb as ccc" to "lazy_import4funcs_('xxx.yyy', 'aaa,bbb:ccc', __name__);\nif 0:from xxx.yyy import aaa, bbb as ccc"'''
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    force = args.force
    omode = 'wt' if args.force else 'xt'
    iencoding = args.iencoding
    oencoding = args.oencoding
    iencoding = 'utf8' if not iencoding else iencoding
    oencoding = 'utf8' if not oencoding else oencoding

    may_ifname = args.input
    may_ofname = args.output
    with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin, may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        for line in fin:
            m = regex4FromImportStmt.fullmatch(line)
            if m:
                (s, _) = parse4regex4FromImportStmt(m)
                print(s, end='\n\n', file=fout)

if __name__ == "__main__":
    main4convert_FromImportStmt()

__all__
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
if 1:from seed.helper.lazy_import__func import filter_FromImportStmt6seed_tiny, main4convert_FromImportStmt
from seed.helper.lazy_import__func import *
