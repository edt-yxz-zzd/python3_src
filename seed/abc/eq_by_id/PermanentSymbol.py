#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.abc.eq_by_id.PermanentSymbol
py -m    seed.abc.eq_by_id.PermanentSymbol
py -m nn_ns.app.debug_cmd   seed.abc.eq_by_id.PermanentSymbol

from seed.abc.eq_by_id.PermanentSymbol import get_PermanentSymbol, fill_module_with_registered_permanent_symbols, lookup_may_PermanentSymbol, lookup_PermanentSymbol, register_new_PermanentSymbol, get_extensional_path__PermanentSymbol, get_intensional_description, PermanentSymbol

intent:
    to repr module.cls.method.kwarg
        to support cooperative methods eg. __init__ to distinguish target/dispatch/consume

usage:
    1. register_new_PermanentSymbol
    2. lookup_PermanentSymbol
    3. create holder/namespace in module toplevel
    4. call fill_module_with_registered_permanent_symbols after all holders created
    5. get_PermanentSymbol

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
    get_PermanentSymbol
        fill_module_with_registered_permanent_symbols
    lookup_may_PermanentSymbol
        lookup_PermanentSymbol
    register_new_PermanentSymbol
        get_extensional_path__PermanentSymbol
        get_intensional_description
        PermanentSymbol
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.eq_by_id.AddrAsHash import BaseAddrAsHash, le_AddrAsHash, AddrAsHash as EqById

from seed.debug.expectError import expectError
from seed.tiny import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name
from seed.tiny import check_type_is
from seed.tiny import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter
from seed.helper.repr_input import repr_helper__str
import weakref
import importlib
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin


_module2smay_holder2qname2symbol = {}
def _register_new_PermanentSymbol(symbol, /):
    check_type_is(PermanentSymbol, symbol)
    (module_qname, smay_holder, symbol_qname) = extensional_path = get_extensional_path__PermanentSymbol(symbol)
    check_pseudo_qual_name(module_qname)
    check_smay_pseudo_qual_name(smay_holder)
    check_pseudo_qual_name(symbol_qname)
    may_symbol = lookup_may_PermanentSymbol(module_qname, smay_holder, symbol_qname)
    if not may_symbol is None: raise Exception('registered')
    _symbol = (
        _module2smay_holder2qname2symbol
        .setdefault(module_qname, {})
        .setdefault(smay_holder, {})
        .setdefault(symbol_qname, symbol)
        )
    ...
    if not _symbol is symbol: raise logic-err
    may_symbol = lookup_may_PermanentSymbol(module_qname, smay_holder, symbol_qname)
    if not may_symbol is symbol: raise logic-err
    return

assert ''.split() == []
assert ''.split('.') == ['']
def _get_attrs__ex(obj, /, *smay_qnames):
    objss = [[obj]]
    for smay_qname in smay_qnames:
        ls = []
        objss.append(ls)
        if smay_qname:
            qname = smay_qname
            for attr in qname.split('.'):
                obj = getattr(obj, attr)
                ls.append(obj)
    #bug:assert objss[-1][-1] is obj
    #   should skip tail empty lists first
    return objss, obj
def _get_either_holder_vs_symbol(module_qname4extensional_path, smay_holder_object_qname4extensional_path, smay_symbol_qname4extensional_path, /):
    '-> holder|PermanentSymbol|raise ImportError/AttributeError'
    check_pseudo_qual_name(module_qname4extensional_path)
    check_smay_pseudo_qual_name(smay_holder_object_qname4extensional_path)
    check_smay_pseudo_qual_name(smay_symbol_qname4extensional_path)

    module_obj = importlib.import_module(module_qname4extensional_path)
    if (type(module_obj) is PermanentSymbol): raise TypeError

    xss, x = _get_attrs__ex(module_obj, smay_holder_object_qname4extensional_path, smay_symbol_qname4extensional_path)
    [[_module_obj], holders, symbols] = xss
    assert _module_obj is module_obj
    if any(type(holder) is PermanentSymbol for holder in holders): raise TypeError
    if not all(type(symbol) is PermanentSymbol for symbol in symbols): raise TypeError
    if not (type(x) is PermanentSymbol) is bool(smay_symbol_qname4extensional_path): raise TypeError
    holder_vs_symbol = x
    return holder_vs_symbol
def get_PermanentSymbol(module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path, /):
    '-> PermanentSymbol|raise ImportError/AttributeError'
    holder_vs_symbol = _get_either_holder_vs_symbol(module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path)
    if not symbol_qname4extensional_path: raise TypeError
    symbol = holder_vs_symbol
    check_type_is(PermanentSymbol, symbol)
    return symbol

def fill_module_with_registered_permanent_symbols(module_qname4extensional_path, /):
    smay_holder2qname2symbol = _module2smay_holder2qname2symbol.get(module_qname4extensional_path, null_mapping_view)
    for smay_holder, qname2symbol in smay_holder2qname2symbol.items():
        holder_obj = _get_either_holder_vs_symbol(module_qname4extensional_path, smay_holder, '')
        assert type(holder_obj) is not PermanentSymbol
        for symbol_qname, symbol in sorted(qname2symbol.items()):
            check_type_is(PermanentSymbol, symbol)
            [attr, *attrs] = symbol_qname.split('.')
            if not attrs:
                setattr(holder_obj, attr, symbol)
            [[_holder_obj], _symbols], _symbol = _get_attrs__ex(holder_obj, symbol_qname)
            if not _symbol is symbol: raise logic-err
            for _symbol in _symbols:
                check_type_is(PermanentSymbol, _symbol)


ImportError
NameError
LookupError
KeyError
AttributeError
def lookup_PermanentSymbol(module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path, Error=LookupError, /):
    may_symbol = lookup_may_PermanentSymbol(module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path)
    if may_symbol is None: raise Error
    symbol = may_symbol
    check_type_is(PermanentSymbol, symbol)
    return symbol
def lookup_may_PermanentSymbol(module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path, /):
    may_symbol = (
            _module2smay_holder2qname2symbol
            .get(module_qname4extensional_path, null_mapping_view)
            .get(smay_holder_object_qname4extensional_path, null_mapping_view)
            .get(symbol_qname4extensional_path, None)
            )
    if may_symbol is not None:
        symbol = may_symbol
        check_type_is(PermanentSymbol, symbol)
    return may_symbol

def _init_storage4PermanentSymbol(symbol, /):
    check_type_is(PermanentSymbol, symbol)
    __PermanentSymbol_d.__set__(symbol, {})
    return
def _get_storage4PermanentSymbol(symbol, /):
    check_type_is(PermanentSymbol, symbol)
    #d = object.__getattribute__(symbol, '__dict__')
    d = __PermanentSymbol_d.__get__(symbol)
    return d

r'''
def _get_properties__PermanentSymbol(symbol, /):
    d = _get_storage4PermanentSymbol(symbol)
    properties = d['$properties']
    return properties
def get_child_symbol_names__PermanentSymbol(symbol, /):
    (module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path, intensional_description, child_symbol_names) = _get_properties__PermanentSymbol(symbol)
    return child_symbol_names
#'''
def _get_member__PermanentSymbol(symbol, private_attr, /):
    d = _get_storage4PermanentSymbol(symbol)
    member = d[private_attr]
    return member
def get_extensional_path__PermanentSymbol(symbol, /):
    return _get_member__PermanentSymbol(symbol, '$extensional_path')
def get_intensional_description(symbol, /):
    return _get_member__PermanentSymbol(symbol, '$intensional_description')


def register_new_PermanentSymbol(module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path, intensional_description, /):
    extensional_path = (module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path)
    may_symbol = lookup_may_PermanentSymbol(*extensional_path)
    if may_symbol is None:
        symbol = new_symbol_as_sf = object.__new__(PermanentSymbol)
        _init_storage4PermanentSymbol(symbol)
        d = _get_storage4PermanentSymbol(symbol)
        d['$extensional_path'] = extensional_path
        d['$intensional_description'] = intensional_description
        d['$$attr2child_symbol'] = {}
        _register_new_PermanentSymbol(symbol)
        may_symbol = lookup_may_PermanentSymbol(*extensional_path)
        if may_symbol is None: raise logic-err
    else:
        symbol = old_symbol_as_sf = may_symbol
        d = _get_storage4PermanentSymbol(symbol)
        if not d['$extensional_path'] == extensional_path: raise logic-err
        if not d['$intensional_description'] == intensional_description: raise Exception('register_new_PermanentSymbol: same extensional_path with diff intensional_description')
        raise Exception('register_new_PermanentSymbol: registered')
    if may_symbol is None: raise logic-err
    sf = may_symbol
    return None
    _ = PermanentSymbol(module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path, intensional_description)
    assert _ is None
    return None
class PermanentSymbol(EqById):
    __slots__ = ('_d', '__weakref__')
    #__slots__ = ('__dict__', '__weakref__')
    #Weakable
    def __new__(cls, module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path, intensional_description, /):#(, child_symbol_names, /):
        #see: register_new_PermanentSymbol
        if not cls is __class__: raise TypeError
        raise TypeError
        #child_symbol_names = frozenset(child_symbol_names)
        #properties = (module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path, intensional_description, child_symbol_names)
    def __repr__(sf):
        (module_qname, smay_holder, symbol_qname) = extensional_path = get_extensional_path__PermanentSymbol(sf)
        return repr_helper__str('lookup_PermanentSymbol', module_qname, smay_holder, symbol_qname)
    def __dir__(sf, /):
        d = _get_storage4PermanentSymbol(sf)
        attr2child_symbol = d['$$attr2child_symbol']
        return sorted(attr2child_symbol)
        #child_symbol_names = get_child_symbol_names__PermanentSymbol(sf)
        #return sorted(child_symbol_names)
    def __getattribute__(sf, attr, /):
        d = _get_storage4PermanentSymbol(sf)
        attr2child_symbol = d['$$attr2child_symbol']
        may_child_symbol = attr2child_symbol.get(attr)
        if may_child_symbol is None:
            (module_qname, smay_holder, symbol_qname) = extensional_path = get_extensional_path__PermanentSymbol(sf)
            child_symbol_qname = f'{symbol_qname!s}.{attr!s}'
            may_child_symbol = lookup_may_PermanentSymbol(module_qname, smay_holder, child_symbol_qname)
            if may_child_symbol is None: raise AttributeError(attr)
            child_symbol = may_child_symbol
            attr2child_symbol[attr] = child_symbol
        else:
            child_symbol = may_child_symbol
        check_type_is(__class__, child_symbol)
        return child_symbol
    def __setattr__(sf, attr, child_symbol, /):
        raise AttributeError(attr)
        r'''
    def __setattr__(sf, attr, child_symbol, /):
        d = _get_storage4PermanentSymbol(symbol)
        attr2child_symbol = d['$$attr2child_symbol']
        may_child_symbol = attr2child_symbol.get(attr)
        if not may_child_symbol is None: raise AttributeError(attr)
        attr2child_symbol[attr] = child_symbol
        #'''
    r'''
    def __init__(sf, module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path, intensional_description, child_symbol_names, /):
        check...
        #sf.__extensional_path = (module_qname4extensional_path, smay_holder_object_qname4extensional_path, symbol_qname4extensional_path)
        sf.__module_qname = module_qname4extensional_path
        sf.__smay_holder = smay_holder_object_qname4extensional_path
        sf.__symbol_qname = symbol_qname4extensional_path)
        sf.__intensional_description = intensional_description
        sf.__child_symbol_names = frozenset(child_symbol_names)
    @property
    def module_qname(sf, /):
        return sf.__module_qname
    @property
    def smay_holder(sf, /):
        return sf.__smay_holder
    @property
    def symbol_qname(sf, /):
        return sf.__symbol_qname
    @property
    def intensional_description(sf, /):
        return sf.__intensional_description
    @property
    def child_symbol_names(sf, /):
        return sf.__child_symbol_names
    #'''
__PermanentSymbol_d = PermanentSymbol._d
del PermanentSymbol._d




assert None is lookup_may_PermanentSymbol(__name__, '_T', 'PermanentSymbol')
register_new_PermanentSymbol(__name__, '_T', 'PermanentSymbol', 'PermanentSymbol class')
register_new_PermanentSymbol(__name__, '_T', 'PermanentSymbol.__dir__', 'PermanentSymbol class::__dir__')
register_new_PermanentSymbol(__name__, '_T', 'PermanentSymbol.uuuuu', 'PermanentSymbol class::uuuuu-nonexist')
assert not None is lookup_may_PermanentSymbol(__name__, '_T', 'PermanentSymbol')
assert PermanentSymbol is type(lookup_may_PermanentSymbol(__name__, '_T', 'PermanentSymbol'))
assert PermanentSymbol is type(lookup_PermanentSymbol(__name__, '_T', 'PermanentSymbol'))


assert expectError(AttributeError, lambda:fill_module_with_registered_permanent_symbols(__name__))
class _T:pass
assert expectError(AttributeError, lambda:get_PermanentSymbol(__name__, '_T', 'PermanentSymbol'))
fill_module_with_registered_permanent_symbols(__name__)
assert _T.PermanentSymbol is get_PermanentSymbol(__name__, '_T', 'PermanentSymbol') is lookup_PermanentSymbol(__name__, '_T', 'PermanentSymbol')
assert _T.PermanentSymbol is eval(repr(_T.PermanentSymbol))
weakref.ref(_T.PermanentSymbol)
assert expectError(AttributeError, lambda:_T.PermanentSymbol.__init__)
assert not expectError(AttributeError, lambda:_T.PermanentSymbol.__dir__)
assert not expectError(AttributeError, lambda:_T.PermanentSymbol.uuuuu)
assert dir(_T.PermanentSymbol) == '__dir__ uuuuu'.split()
del _module2smay_holder2qname2symbol[__name__]
del _T



#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


