#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.types.attr.IValueAppendDecorator
py -m    seed.types.attr.IValueAppendDecorator
py -m nn_ns.app.debug_cmd   seed.types.attr.IValueAppendDecorator

used in:
    seed.func_tools.fmapT.TypeBasedDispatcher::on_type/on_basetype
        view ../../python3_src/seed/func_tools/fmapT/TypeBasedDispatcher.py
        #related toview ../../python3_src/seed/types/view/RecurView.py

from seed.types.attr.IValueAppendDecorator import IValueAppendDecorator, IValueAppendDecorator__fix3, IValueAppendDecorator__fixN_lt3, IValueAppendDecorator__fix2, IValueAppendDecorator__fix1, ValueAppendDecorator__fix0, iter_attr_case_args4group_by__IValueAppendDecorator, group_by_attr_then_case__IValueAppendDecorator, group_by_case_then_attr__IValueAppendDecorator


#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''
    IValueAppendDecorator
        IValueAppendDecorator__fix3
        IValueAppendDecorator__fixN_lt3
            IValueAppendDecorator__fix2
            IValueAppendDecorator__fix1
            ValueAppendDecorator__fix0

    iter_attr_case_args4group_by__IValueAppendDecorator
    group_by_attr_then_case__IValueAppendDecorator
    group_by_case_then_attr__IValueAppendDecorator

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver0 import ABC, abstractmethod, override
from seed.tiny import check_type_is

___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#IValueAppendDecorator:goto
#IValueAppendDecorator__fixN:goto
#helper_utils___group_by:goto
#zzzwww:goto

#[[[IValueAppendDecorator:begin

#同一函数 可能 同时使用 这两个 修饰词:on_basetype, on_type
#   同一个修饰词 也能 作用于 同一函数 多次？？
class IValueAppendDecorator(ABC):
    ___main_attr___ = '___private4ValueAppendDecorator'
        # f.<.___main_attr___> :: {symbol8lord: [(case4option, args4case)]}

    def __call__(sf, f, /):
        cls = type(sf)
        ___main_attr___ = cls.___main_attr___
        if not hasattr(f, ___main_attr___):
            setattr(f, ___main_attr___, {})
        lord2arged_opts = getattr(f, ___main_attr___)
        lord = sf.get_symbol8lord()
        arged_opts = lord2arged_opts.setdefault(lord, [])

        case4option = sf.get_case4option()
        args4case = sf.get_args4case()
        arged_opt = case4option, args4case

        check_type_is(tuple, args4case)
        sf.check_args4case(*args4case)
        arged_opts.append(arged_opt)
        return f
    @abstractmethod
    def get_symbol8lord(sf, /):
        '-> symbol8lord'
    @abstractmethod
    def get_case4option(sf, /):
        '-> case4option'
    @abstractmethod
    def get_args4case(sf, /):
        '-> args4case/tuple'
    def check_args4case(sf, /, *args4case):
        pass
#]]]IValueAppendDecorator:end

#[[[IValueAppendDecorator__fixN:begin

class IValueAppendDecorator__fix3(IValueAppendDecorator):
    def __init__(sf, /):
        super().__init__()
    @abstractmethod
    class ___symbol8lord___:pass
    @abstractmethod
    class ___case4option___:pass
    @abstractmethod
    class ___args4case___:pass

    @override
    def get_symbol8lord(sf, /):
        '-> symbol8lord'
        return type(sf).___symbol8lord___
    @override
    def get_case4option(sf, /):
        '-> case4option'
        return type(sf).___case4option___
    @override
    def get_args4case(sf, /):
        '-> args4case/tuple'
        return type(sf).___args4case___
class IValueAppendDecorator__fixN_lt3(IValueAppendDecorator):
    def __init__(sf, /, *args4case):
        sf._args4case = sf.standardize_args4case(*args4case)
        sf.check_args4case(*sf._args4case)
        super().__init__()
    def standardize_args4case(sf, /, *args4case):
        '-> args4case/tuple'
        return args4case
class IValueAppendDecorator__fix2(IValueAppendDecorator__fixN_lt3):
    def __init__(sf, /, *args4case):
        super().__init__(*args4case)
    @abstractmethod
    class ___symbol8lord___:pass
    @abstractmethod
    class ___case4option___:pass
    @override
    def get_symbol8lord(sf, /):
        '-> symbol8lord'
        return type(sf).___symbol8lord___
    @override
    def get_case4option(sf, /):
        '-> case4option'
        return type(sf).___case4option___
    @override
    def get_args4case(sf, /):
        '-> args4case/tuple'
        return sf._args4case
class IValueAppendDecorator__fix1(IValueAppendDecorator__fixN_lt3):
    def __init__(sf, case4option, /, *args4case):
        sf._case4option = case4option
        super().__init__(*args4case)
    @abstractmethod
    class ___symbol8lord___:pass
    @override
    def get_symbol8lord(sf, /):
        '-> symbol8lord'
        return type(sf).___symbol8lord___
    @override
    def get_case4option(sf, /):
        '-> case4option'
        return sf._case4option
    @override
    def get_args4case(sf, /):
        '-> args4case/tuple'
        return sf._args4case
class ValueAppendDecorator__fix0(IValueAppendDecorator__fixN_lt3):
    def __init__(sf, symbol8lord, case4option, /, *args4case):
        sf._symbol8lord = symbol8lord
        sf._case4option = case4option
        super().__init__(*args4case)
    @override
    def get_symbol8lord(sf, /):
        '-> symbol8lord'
        return sf._symbol8lord
    @override
    def get_case4option(sf, /):
        '-> case4option'
        return sf._case4option
    @override
    def get_args4case(sf, /):
        '-> args4case/tuple'
        return sf._args4case
#]]]IValueAppendDecorator__fixN:end

#[[[helper_utils___group_by:begin

def iter_attr_case_args4group_by__IValueAppendDecorator(BaseValueAppendDecorator, lord, cls, /):
    '-> Iter<(attr, case4option, args4case)>'
    ___main_attr___ = BaseValueAppendDecorator.___main_attr___
    for attr, xxx in cls.__dict__.items():
        if not (type(attr) is str and attr.isidentifier()): continue
        lord2arged_opts = getattr(xxx, ___main_attr___, {})
        arged_opts = lord2arged_opts.get(lord, [])
        if not arged_opts: continue

        for case4option, args4case in arged_opts:
            yield attr, case4option, args4case




def group_by_attr_then_case__IValueAppendDecorator(BaseValueAppendDecorator, lord, cls, /):
    '-> {attr:{case4option:[args4case]}}'
    attr2case2argss = {}
    it = iter_attr_case_args4group_by__IValueAppendDecorator(BaseValueAppendDecorator, lord, cls)
    for attr, case4option, args4case in it:
        case2argss = attr2case2argss.setdefault(attr, {})
        argss = case2argss.setdefault(case4option, [])
        argss.append(args4case)
    return attr2case2argss

def group_by_case_then_attr__IValueAppendDecorator(BaseValueAppendDecorator, lord, cls, /):
    '-> {case4option:{attr:[args4case]}}'
    case2attr2argss = {}
    it = iter_attr_case_args4group_by__IValueAppendDecorator(BaseValueAppendDecorator, lord, cls)
    for attr, case4option, args4case in it:
        attr2argss = case2attr2argss.setdefault(case4option, {})
        argss = attr2argss.setdefault(attr, [])
        argss.append(args4case)
    return case2attr2argss
#]]]helper_utils___group_by:end


#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    from seed.types.attr.IValueAppendDecorator import *
    from seed.types.attr.IValueAppendDecorator import IValueAppendDecorator, IValueAppendDecorator__fix3, IValueAppendDecorator__fixN_lt3, IValueAppendDecorator__fix2, IValueAppendDecorator__fix1, ValueAppendDecorator__fix0, iter_attr_case_args4group_by__IValueAppendDecorator, group_by_attr_then_case__IValueAppendDecorator, group_by_case_then_attr__IValueAppendDecorator
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


