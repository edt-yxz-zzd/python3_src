#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/auto_calc.py

why?
    eg:view ../../python3_src/seed/seq_tools/avoid_substrs.py
    fix some input, auto calc and cache


[[有点关联的思考:
read 需要 类型 作为 向导
  不存在 全局限定标识 #随机命名碰撞
repr 如何覆盖某类型某一构造器的字串化？
静态类型 外挂操作 ==> 动态数据 性质判定/缓存相关计算数据/额外数据
  sort :: Ord a => [a] -> [a]
  f :: is_square x => [@x::a] -> a
    [is_square x =[def]= ?y. [y*y==x]]
      输入等于多出个 x的平方根y
view ../../python3_src/seed/helper/auto_calc.py
]]


seed.helper.auto_calc
py -m nn_ns.app.debug_cmd   seed.helper.auto_calc -x
py -m nn_ns.app.doctest_cmd seed.helper.auto_calc:__doc__ -ff -v
py_adhoc_call   seed.helper.auto_calc   @f
from seed.helper.auto_calc import BaseAutoCalcAndCache, mk_Property4AutoCalcAndCache, Injector4Property4AutoCalcAndCache, calc_all
from seed.helper.auto_calc import mk_onm2inms4dependency_graph_dedges__reversed, collect_src_names, iter_topological_ordering4dependency_graph_, is_DAG4dependency_graph_, mk_reversed_dependency_digraph_, NotDAG_Error, check_DAG4dependency_graph_


def get_signature_of__py3_(f, /, follow_wrapped=True):
    -> (infoss4input/(infos4idx_only, infos4idx_nm_both, tmay_info4varargs, infos4nm_only, tmay_info4varkwds), tmay_return_annotation)

    ===
    infos4xxx :: [info4parameter]
    tmay_info4xxx :: tmay info4parameter
    tmay_return_annotation :: tmay py_obj
    ===
    info4parameter = (name, tmay_annotation, tmay_default)
    ===


>>> from seed.for_libs.for_inspect import get_signature_of__py3_, get_signature_of__py2_
>>> def f(_0,_1:11,_2=222,_3:33=333, /, a=999, b:'bb'=666, c='ccc', d:'dd'='ddd', *args:'`args`', w, x:'xx', y='yyy', z:'zz'='zzz', **kwargs:'`kwargs`'):pass
>>> get_signature_of__py3_(f)
(((('_0', (), ()), ('_1', (11,), ()), ('_2', (), (222,)), ('_3', (33,), (333,))), (('a', (), (999,)), ('b', ('bb',), (666,)), ('c', (), ('ccc',)), ('d', ('dd',), ('ddd',))), (('args', ('`args`',), ()),), (('w', (), ()), ('x', ('xx',), ()), ('y', (), ('yyy',)), ('z', ('zz',), ('zzz',))), (('kwargs', ('`kwargs`',), ()),)), ())



>>> class T(BaseAutoCalcAndCache):
...     @mk_Property4AutoCalcAndCache
...     def c(a, b, /):
...         return a+b

>>> injector = Injector4Property4AutoCalcAndCache(T)
>>> @injector
... def d(c, /):
...     return c+1

>>> t = T(a=2)
>>> t.a
2
>>> t.b
Traceback (most recent call last):
    ...
AttributeError: type object 'T' has no attribute 'b'
>>> t.c
Traceback (most recent call last):
    ...
AttributeError: type object 'T' has no attribute 'b'
>>> t.b = 3
>>> t.b = 4
Traceback (most recent call last):
    ...
AttributeError: b
>>> t
T(a = 2, b = 3)
>>> t.d
6
>>> t
T(a = 2, b = 3, c = 5, d = 6)


>>> t.n
Traceback (most recent call last):
    ...
AttributeError: type object 'T' has no attribute 'n'

>>> @injector
... def mk_n_m(a, b, c, d, /) -> '(n, m)':
...     return (c+d, a-b)
>>> @injector
... def mk_r(n, m, /) -> 'r':
...     return (n, m)
>>> @injector
... def mk_n2_m2(a, b, c, d, /):
...     '-> (n2, m2)'
...     return (c+d, a-b)
>>> @injector
... def mk_r2(n2, m2, /):
...     '-> r2'
...     return (n2, m2)
>>> t.n
11
>>> t.r
(11, -1)
>>> t.m
-1
>>> t.r2
(11, -1)
>>> t
T(a = 2, b = 3, c = 5, d = 6, m = -1, m2 = -1, n = 11, n2 = 11, r = (11, -1), r2 = (11, -1))
>>> t.mk_r2
Traceback (most recent call last):
    ...
AttributeError: type object 'T' has no attribute 'mk_r2'

>>> mk_r2.__doc__ #mk_r2 is func not None
'-> r2'
>>> mk_r2(777, 999) #mk_r2 is func not None
(777, 999)


>>> class TTT(BaseAutoCalcAndCache):
...     @mk_Property4AutoCalcAndCache
...     def c(a, b, /) -> 'd':
...         return a+b
Traceback (most recent call last):
    ...
TypeError: ('d', 'c')
>>> class TTT(BaseAutoCalcAndCache):
...     @mk_Property4AutoCalcAndCache
...     def c(a, b, /) -> '(d,m)':
...         return a+b
Traceback (most recent call last):
    ...
TypeError: (['d', 'm'], 'c')



>>> sorted(T.iter_export_names())
['c', 'd', 'm', 'm2', 'n', 'n2', 'r', 'r2']
>>> t = T()
>>> dir(t)
['c', 'd', 'm', 'm2', 'n', 'n2', 'r', 'r2']
>>> t
T()
>>> calc_all(t)
Traceback (most recent call last):
    ...
AttributeError: type object 'T' has no attribute 'a'
>>> t
T()
>>> t.a = 2
>>> t.b = 3
>>> t
T(a = 2, b = 3)
>>> dir(t)
['a', 'b', 'c', 'd', 'm', 'm2', 'n', 'n2', 'r', 'r2']
>>> calc_all(t) == {'a': 2, 'b': 3, 'c': 5, 'd': 6, 'm': -1, 'm2': -1, 'n': 11, 'n2': 11, 'r': (11, -1), 'r2': (11, -1)}
True
>>> t
T(a = 2, b = 3, c = 5, d = 6, m = -1, m2 = -1, n = 11, n2 = 11, r = (11, -1), r2 = (11, -1))

>>> t = T(a=2,b=3)
>>> t
T(a = 2, b = 3)
>>> dir(t)
['a', 'b', 'c', 'd', 'm', 'm2', 'n', 'n2', 'r', 'r2']
>>> calc_all(t) == {'a': 2, 'b': 3, 'c': 5, 'd': 6, 'm': -1, 'm2': -1, 'n': 11, 'n2': 11, 'r': (11, -1), 'r2': (11, -1)}
True
>>> t
T(a = 2, b = 3, c = 5, d = 6, m = -1, m2 = -1, n = 11, n2 = 11, r = (11, -1), r2 = (11, -1))


>>> mk_onm2inms4dependency_graph_dedges__reversed(T) == {'c': ('a', 'b'), 'd': ('c',), 'm': ('a', 'b', 'c', 'd'), 'm2': ('a', 'b', 'c', 'd'), 'n': ('a', 'b', 'c', 'd'), 'n2': ('a', 'b', 'c', 'd'), 'r': ('n', 'm'), 'r2': ('n2', 'm2')}
True
>>> collect_src_names(T) == {'a', 'b'}
True
>>> [*iter_topological_ordering4dependency_graph_(T, stable=True, u2vtc__vs__dedges=True)]
Traceback (most recent call last):
    ...
NotImplementedError: bug:nonstable-impl:.from_vertex_pairs()
>>> [*iter_topological_ordering4dependency_graph_(T, stable=True, u2vtc__vs__dedges=False)]
['a', 'b', 'c', 'd', 'm', 'm2', 'n', 'n2', 'r', 'r2']
>>> [*iter_topological_ordering4dependency_graph_(T, stable=True)]
['a', 'b', 'c', 'd', 'm', 'm2', 'n', 'n2', 'r', 'r2']
>>> @injector
... def lazy_x_():
...     '-> x'
...     return 333
>>> [*iter_topological_ordering4dependency_graph_(T, stable=True)]
['a', 'b', 'c', 'd', 'm', 'm2', 'n', 'n2', 'r', 'r2', 'x']
>>> mk_onm2inms4dependency_graph_dedges__reversed(T) == {'c': ('a', 'b'), 'd': ('c',), 'm': ('a', 'b', 'c', 'd'), 'm2': ('a', 'b', 'c', 'd'), 'n': ('a', 'b', 'c', 'd'), 'n2': ('a', 'b', 'c', 'd'), 'r': ('n', 'm'), 'r2': ('n2', 'm2'), 'x': ()}
True
>>> collect_src_names(T) == {'a', 'b'}
True


>>> is_DAG4dependency_graph_(T, stable=True, u2vtc__vs__dedges=True)
Traceback (most recent call last):
    ...
NotImplementedError: bug:nonstable-impl:.from_vertex_pairs()
>>> is_DAG4dependency_graph_(T, stable=True, u2vtc__vs__dedges=False)
True
>>> is_DAG4dependency_graph_(T, stable=True)
True
>>> is_DAG4dependency_graph_(T, stable=False, u2vtc__vs__dedges=True)
True
>>> is_DAG4dependency_graph_(T, stable=False, u2vtc__vs__dedges=False)
True
>>> is_DAG4dependency_graph_(T, stable=False)
True
>>> is_DAG4dependency_graph_(T, u2vtc__vs__dedges=True)
Traceback (most recent call last):
    ...
NotImplementedError: bug:nonstable-impl:.from_vertex_pairs()
>>> is_DAG4dependency_graph_(T, u2vtc__vs__dedges=False)
True
>>> is_DAG4dependency_graph_(T)
True



#]]]'''
__all__ = r'''
    BaseAutoCalcAndCache
        calc_all
        mk_onm2inms4dependency_graph_dedges__reversed
        collect_src_names
        iter_topological_ordering4dependency_graph_
        is_DAG4dependency_graph_
        mk_reversed_dependency_digraph_
        NotDAG_Error
        check_DAG4dependency_graph_

    Property4AutoCalcAndCache
        extract_arg_names_and_export_names5func
            extract_arg_names5func
            mk_Property4AutoCalcAndCache
            Injector4Property4AutoCalcAndCache
'''.split()#'''
__all__


from collections import OrderedDict
from seed.graph.U2Vtc_To_DigraphABC import ObjU2Vtc_To_Digraph
from seed.graph.DAG import iter_reversed_topological_ordering, is_DAG, find_one_cycle
from seed.for_libs.for_inspect import get_signature_of__py3_
from seed.helper.repr_input import repr_helper
from seed.tiny import check_type_is, check_type_le, check_callable, mk_tuple
from seed.tiny_.check import check_pseudo_identifier# check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.text.useful_regex_patterns import nm__pattern
import re
export_nms__pattern = f'(?:(?P<nm1>{nm__pattern})|[(](?P<nm2s>{nm__pattern}(?:, *{nm__pattern})+)[)])'
return_export_nms__pattern = f'-> *{export_nms__pattern}'
export_nms__regex = re.compile(export_nms__pattern)
return_export_nms__regex = re.compile(return_export_nms__pattern)

def _vars_(sf, /):
    'to replace vars()'
    return object.__getattribute__(sf, '__dict__')
def extract_arg_names5func(func, /):
    arg_names, export_names = extract_arg_names_and_export_names5func(func)
    return arg_names
def extract_arg_names_and_export_names5func(func, /):
    ((infos4idx_only, infos4idx_nm_both, tmay_info4varargs, infos4nm_only, tmay_info4varkwds), tmay_return_annotation) = get_signature_of__py3_(func)
    infos4idx_only
    if infos4idx_nm_both: raise TypeError
    if tmay_info4varargs: raise TypeError
    if infos4nm_only: raise TypeError
    if tmay_info4varkwds: raise TypeError
    if any(tmay_default for (name, tmay_annotation, tmay_default) in infos4idx_only): raise TypeError

    arg_names = tuple(name for (name, tmay_annotation, tmay_default) in infos4idx_only)

    ########
    tmay_return_annotation
    func.__doc__
    func.__name__
    ########
    if tmay_return_annotation:
        [return_annotation] = tmay_return_annotation
    else:
        return_annotation = ''
    return_annotation
    ########
    if func.__doc__ is None:
        func_doc = ''
    else:
        func_doc = func.__doc__
    func_doc
    ########
    m = export_nms__regex.fullmatch(return_annotation)
    ########
    if not m:
        m = return_export_nms__regex.fullmatch(func_doc.partition('\n')[0])
    ########
    if not m:
        is_multi_exports = False
        nm = func.__name__
        #nm_or_nms = nm
        nms = (nm,)
    else:
        may_nm1 = m.group('nm1')
        may_nm2s = m.group('nm2s')
        assert not bool(may_nm1) is bool(may_nm2s)
        is_multi_exports = bool(may_nm2s)
        if is_multi_exports:
            nm2s = may_nm2s
            #nms = (*nm2s.split(', '),)
            nms = (*nm2s.replace(',', ' ').split(),)
            assert len(nms) >= 2
        else:
            nm = may_nm1
            nms = (nm,)
        nms
    nms
    assert len(nms) >= 1
    ########
    export_names = nms

    return arg_names, export_names
class Property4AutoCalcAndCache:
    def __init__(sf, func, arg_names, export_names, /):
        check_callable(func)
        arg_names = mk_tuple(arg_names)
        export_names = mk_tuple(export_names)
        if not export_names: raise TypeError
        for nm in arg_names: check_pseudo_identifier(nm)
        for nm in export_names: check_pseudo_identifier(nm)
        sf._f = func
        sf._inms = arg_names
        sf._onms = export_names
    def get_func(sf, /):
        return sf._f
    def get_arg_names(sf, /):
        return sf._inms
    def get_export_names(sf, /):
        return sf._onms
    def calc5auto(sf, auto:'BaseAutoCalcAndCache', /):
        f = sf.get_func()
        inms = sf.get_arg_names()
        args = [getattr(auto, nm) for nm in inms]
        x = f(*args)
        return x
    def calc_ex5auto(sf, auto:'BaseAutoCalcAndCache', /):
        x = sf.calc5auto(auto)
        onms = sf.get_export_names()
        if len(onms) == 1:
            xs = (x,)
        else:
            check_type_is(tuple, x)
            xs = x
        xs
        check_type_is(tuple, xs)
        if not len(xs) == len(onms): raise TypeError
        return (*zip(onms, xs),)
def mk_Property4AutoCalcAndCache(func, /, *, multi_exports_ok=False, func_name_exported_only=True):
    r'''[[[
usage:
    class T(BaseAutoCalcAndCache):
        @mk_Property4AutoCalcAndCache
        def f(..., /):...
    #]]]'''#'''
    check_callable(func)
    arg_names, export_names = extract_arg_names_and_export_names5func(func)
    if not multi_exports_ok:
        if not len(export_names) == 1: raise TypeError(([*export_names], func.__name__))
        [export_name] = export_names
        if func_name_exported_only:
            if not export_name == func.__name__: raise TypeError((export_name, func.__name__))

    x = Property4AutoCalcAndCache(func, arg_names, export_names)
    return x
    check_callable(func)
    arg_names = extract_arg_names5func(func)
    x = Property4AutoCalcAndCache(func, arg_names)
    return x
class Injector4Property4AutoCalcAndCache:
    r'''[[[
usage:
    class T(BaseAutoCalcAndCache):
        ...
    injector = Injector4Property4AutoCalcAndCache(T)
    @injector
    def f(..., /):...

    #]]]'''#'''
    def __init__(sf, target_type, /):
        check_type_le(type, target_type)
        sf._T = target_type
    def __call__(sf, func, /):
        #nm = func.__name__
        #check_pseudo_identifier(nm)

        x = mk_Property4AutoCalcAndCache(func, multi_exports_ok=True)
        onms = x.get_export_names()
        for nm in onms:
            setattr(sf._T, nm, x)
        return func # @sf def f(...,/):...

class BaseAutoCalcAndCache:
    def __init__(sf, /, **kwds):
        for nm, x in kwds.items():
            setattr(sf, nm, x)

    def __repr__(sf, /):
        return repr_helper(sf, **_vars_(sf))

    def __setattr__(sf, nm, x, /):
        d = _vars_(sf)
        if nm in d:
            raise AttributeError(nm)
        d[nm] = x
    def __getattribute__(sf, nm, /):
        #cls = type(sf)
        #cls._get_(nm)
    #def _get_(sf, nm, /, *, dry_run):
        d = _vars_(sf)
        while not nm in d:
            cls = type(sf)
            property4AutoCalcAndCache = getattr(cls, nm)
            #check_type_le(Property4AutoCalcAndCache, property4AutoCalcAndCache)
            if 0:
                x = property4AutoCalcAndCache.calc5auto(sf)
                setattr(sf, nm, x)
            else:
                ps = property4AutoCalcAndCache.calc_ex5auto(sf)
                for _nm, _x in ps:
                    setattr(sf, _nm, _x)
                if nm not in d: raise logic-err
        return d[nm]

    @classmethod
    def _mk_onm2inms4dependency_graph_dedges__reversed_(cls, /):
        '-> {onm:[inm]}'
        return dict(cls._iter_onm_inms_pairs_())
    if 0:#bug
      @classmethod
      def _mk_onm2inms4dependency_graph_dedges__reversed_(cls, /):
        #bug: when [inms<onm>==[]]
        '-> {onm:[inm]}'
        onm2inms = {}
        for inm, onm in cls._iter_dependency_graph_dedges_():
            onm2inms.setdefault(onm, []).append(inm)
        return onm2inms
    @classmethod
    def _iter_onm_inms_pairs_(cls, /):
        '-> Iter (onm, [inm])'
        for (onm, inms, onms, property4AutoCalcAndCache) in cls._iter_onm_inms_pairs_ex_():
            yield (onm, inms)
    @classmethod
    def _iter_onm_inms_pairs_ex_(cls, /):
        '-> Iter (onm, inms, onms, property4AutoCalcAndCache)'
        for onm in cls.iter_export_names():
            property4AutoCalcAndCache = getattr(cls, onm)
            #check_type_le(Property4AutoCalcAndCache, property4AutoCalcAndCache)
            inms = property4AutoCalcAndCache.get_arg_names()
            onms = property4AutoCalcAndCache.get_export_names()
            yield (onm, inms, onms, property4AutoCalcAndCache)

    @classmethod
    def _iter_dependency_graph_dedges_(cls, /):
        '-> Iter (inm,onm) # is_DAG?? # nonstable'
        #xxx '-> Iter (xinm,xonm)/Iter ((inm, onm)|(inm, onm_ex)|(onm_ex,onm)) # is_DAG??'
        for (onm, inms, onms, property4AutoCalcAndCache) in cls._iter_onm_inms_pairs_ex_():
            if not onm in onms:raise logic-err
            if 1:
                ########new:
                for inm in inms:
                    yield inm, onm
            elif onm == onms[0]:
                ########old:
                if len(onms) >= 2 and len(inms) >= 2:
                    onm_ex = ','.join(onms)
                    yield onm_ex, onm
                else:
                    onm_ex = onm
                onm_ex

                for inm in inms:
                    yield inm, onm_ex
        return

    @classmethod
    def collect_src_names(cls, /):
        '-> src_names/{inm&&not onm}'
        _onms = set()
        _inms = set()
        for (onm, inms, onms, property4AutoCalcAndCache) in cls._iter_onm_inms_pairs_ex_():
            _inms.update(inms)
            _onms.update(onms)
        src_names = _inms - _onms
        return src_names
    def _calc_all_(sf, /):
        if 0:
            [*iter_topological_ordering4dependency_graph_(type(sf))]
            #raise if not DAG
        return {nm:getattr(sf, nm) for nm in dir(sf)}
    def __dir__(sf, /):
        cls = type(sf)
        return sorted({*cls.iter_export_names(), *_vars_(sf)})
    @classmethod
    def iter_export_names(cls, /):
        '# donot include __init__.kwds and __setattr__ directly  # nonstable'
        return (nm for nm in dir(cls) if isinstance(getattr(cls, nm, None), Property4AutoCalcAndCache))
        #
    if 0:#bug
      @classmethod
      def iter_export_names(cls, /):
          #bug: "__xxx__" is not in __dict__
        nms = set() # only fst occur <<== override by diff type
        for T in cls.__mro__:
            for nm, x in vars(T).items():
                if nm in nms:continue
                nms.add(nm)
                if isinstance(x, Property4AutoCalcAndCache):
                    yield nm
def calc_all(sf, /):
    cls = type(sf)
    return cls._calc_all_(sf)
def mk_onm2inms4dependency_graph_dedges__reversed(cls, /):
    assert issubclass(cls, BaseAutoCalcAndCache)
    return cls._mk_onm2inms4dependency_graph_dedges__reversed_()
def collect_src_names(cls, /):
    assert issubclass(cls, BaseAutoCalcAndCache)
    return cls.collect_src_names()

def iter_topological_ordering4dependency_graph_(cls, /, *, stable=True, u2vtc__vs__dedges=False):
    '-> Iter (inm|onm) #stable-algo-impl #see: collect_src_names()'
    g = mk_reversed_dependency_digraph_(cls, stable=stable, u2vtc__vs__dedges=u2vtc__vs__dedges)
    return iter_reversed_topological_ordering(g)
class NotDAG_Error(Exception):pass
def check_DAG4dependency_graph_(cls, /, *, stable=True, u2vtc__vs__dedges=False):
    '^NotDAG_Error'
    g = mk_reversed_dependency_digraph_(cls, stable=stable, u2vtc__vs__dedges=u2vtc__vs__dedges)
    ls = find_one_cycle(g)
    if ls:
        raise NotDAG_Error(ls)
def is_DAG4dependency_graph_(cls, /, *, stable=True, u2vtc__vs__dedges=False):
    g = mk_reversed_dependency_digraph_(cls, stable=stable, u2vtc__vs__dedges=u2vtc__vs__dedges)
    return is_DAG(g)
def mk_reversed_dependency_digraph_(cls, /, *, stable=True, u2vtc__vs__dedges=False):
    if u2vtc__vs__dedges is False:
        pass
    else:
        if stable:
            raise NotImplementedError('bug:nonstable-impl:.from_vertex_pairs()')

    if u2vtc__vs__dedges is False:
        u2vtc = onm2inms = mk_onm2inms4dependency_graph_dedges__reversed(cls)
        src_names = cls.collect_src_names()
            # to include inm
        for src_name in src_names:
            if src_name in u2vtc:raise logic-err
            u2vtc[src_name] = []
        u2vtc
    else:
        dedges = [(o,i) for i,o in cls._iter_dependency_graph_dedges_()]
            #reversed dedge
        some_vtc = onms = cls.iter_export_names()
            # to include onm without inms, ie. lazy_value
            # ie. for onm s.t. [u2vtc[onm] == []]

    if stable:
        #sorted ==>> stable
        if u2vtc__vs__dedges is False:
            u2vtc = OrderedDict(sorted((u, sorted(vtc)) for u, vtc in u2vtc.items()))
        else:
            raise NotImplementedError('bug:nonstable-impl:.from_vertex_pairs()')
            dedges = sorted(dedges)
            some_vtc = sorted(some_vtc)

    if u2vtc__vs__dedges is False:
        g = ObjU2Vtc_To_Digraph(u2vtc)
    else:
        g = ObjU2Vtc_To_Digraph.from_vertex_pairs(dedges, some_vtc)
            #bug:nonstable-impl:.from_vertex_pairs()

    return g

__all__


from seed.helper.auto_calc import BaseAutoCalcAndCache, mk_Property4AutoCalcAndCache, Injector4Property4AutoCalcAndCache, calc_all
from seed.helper.auto_calc import mk_onm2inms4dependency_graph_dedges__reversed, collect_src_names, iter_topological_ordering4dependency_graph_, is_DAG4dependency_graph_, mk_reversed_dependency_digraph_, NotDAG_Error, check_DAG4dependency_graph_
from seed.helper.auto_calc import *
