

'''
Auto-detect whether the global names are all imported.
So, we donot worry if forgot import some names.
We need not import anything when writing code.
When imported, raise_when_forgot will show all names.
And then we can use ALL start imports for fast debugging.
At the end, we comment out all imports to get the names used
and replace the '*' with proper names.
I donot know why python's std lib doesnot offer such thing.
# fail case: "import importlib.util" writes as "import importlib"

usage:
# at top to make detecting first to save time
# since some modules like sympy are time-consuming.
# put the following code at top:
from ??? import raise_when_forgot
assert not raise_when_forgot(__file__, 'error logic')


[[
bug4class_namespace:here
patch4class_namespace:goto
===
found bug@nn_ns.app.debug_cmd
    from:seed.types.PruneableArray
bug:cannot found unbound_name:『begin』
    -->from seed.pkg_tools.detect_all_unbound_names import DetectAllUnboundNames
    -->from ._forgot_import import symtable2forgots
    -->def _collect_forgots(table, may_context, /):
        patch...
class PruneableArray:
    @property
    def begin(sf, /):
        return sf._begin
    def __contains__(sf, v, /):
        j = sf.index(v, begin, end)
        ...
]]
'''

__all__ = '''
    symtable2forgots
    fname2forgots
    '''.split()

from seed.mapping_tools.dict_op import intersect_keys__immutable
from seed.tiny_.check import check_type_is
from .read_python_source import read_python_source
import symtable
import inspect #.getsource(object)
from pprint import pprint
import keyword
from collections import defaultdict
import importlib #.import_module


def _imported_main_(importer, notforgots_str, **kwargs):
    #print(_imported_main_)
    if not __debug__:
        return
    not_forgots = notforgots_str.split()
    args = Args_For_RaiseWhenForgot(not_forgots, **kwargs)
    args.test__module(importer)



############## xxx2symtable ################

def module2symtable(module):
    src = inspect.getsource(module)
    table = symtable.symtable(src, module.__file__, "exec")
    return table
def module_name2symtable(module_name):
    module = importlib.import_module(module_name)
    return module2symtable(module)
def fname2symtable(fname):
    'fname2symtable(__file__)'
    src = read_python_source(fname)
    table = symtable.symtable(src, fname, "exec")
    return table






##########################################
def _collect_if__simple(predicator, table, /, *, recursive=False, with_table=False, identifier_vs_symbol=False):
    return _collect_if(predicator, table, recursive=recursive, with_table=with_table, identifier_vs_symbol=identifier_vs_symbol)

def _collect_if(predicator, table, /, *, recursive, with_table, identifier_vs_symbol):
    if identifier_vs_symbol:
        def fx(symbol, /):
            return symbol
    else:
        def fx(symbol, /):
            return symbol.get_name()

    if with_table:
        output_dict = defaultdict(set)
        def fy(table, symbol, /):
            output_dict[table] = fx(symbol)
    else:
        output_set = set()
        def fy(table, symbol, /):
            output_set.add(fx(symbol))

    __collect_if(predicator, table, fy, recursive=recursive)

    if with_table:
        return dict(output_dict)
    else:
        return frozenset(output_set)

def __collect_if(predicator, table, output, /, *, recursive):
  def recur(table, /):
    #print(table.get_type())
    # <- {'module', 'class', 'function'}
    assert table.get_type() in {'module', 'class', 'function'}
    if 0:
        _i = 2
        types = ['module', 'class', 'function']
        typ = table.get_type()
        if _i == types.index(typ):
            print(typ, dir(table)); raise SystemExit
            #module ['get_children', 'get_id', 'get_identifiers', 'get_lineno', 'get_name', 'get_symbols', 'get_type', 'has_children', 'has_exec', 'is_nested', 'is_optimized', 'lookup']
            #class ['get_children', 'get_id', 'get_identifiers', 'get_lineno', 'get_methods', 'get_name', 'get_symbols', 'get_type', 'has_children', 'has_exec', 'is_nested', 'is_optimized', 'lookup']
                #+:get_methods
            #function ['get_children', 'get_frees', 'get_globals', 'get_id', 'get_identifiers', 'get_lineno', 'get_locals', 'get_name', 'get_nonlocals', 'get_parameters', 'get_symbols', 'get_type', 'has_children', 'has_exec', 'is_nested', 'is_optimized', 'lookup']
                #+:get_frees, get_globals, get_locals, get_nonlocals, get_parameters

    #print(table.get_symbols()); raise SystemExit
    #print(table.get_identifiers()); raise SystemExit
    assert set(table.get_identifiers()) == set(symbol.get_name() for symbol in table.get_symbols())
    for symbol in table.get_symbols():
        #print(dir(symbol)); raise SystemExit
        #['get_name', 'get_namespace', 'get_namespaces', 'is_annotated', 'is_assigned', 'is_declared_global', 'is_free', 'is_global', 'is_imported', 'is_local', 'is_namespace', 'is_nonlocal', 'is_parameter', 'is_referenced']
        #name = symbol.get_name()
        if predicator(symbol):
            output(table, symbol)

    if recursive:
        for child in table.get_children():
            recur(child)
  #end-def recur(table, /):
  def main():
      recur(table)
  return main()

def _collect_defined_globals(table, /):
    if not table.get_type() == 'module': raise TypeError
    if table.is_nested(): raise TypeError
    #bug: defined_globals = _collect_all_locals(table)
    #       cannot found: del local_forgot__deleted_but_not_defined
    defined_globals = _collect_defined_locals(table)
    return defined_globals
def _collect_defined_locals(table, /):
    defined_locals = _collect_if__simple(is_symbol_local_defined, table)
    return defined_locals

def is_symbol_local_undefined(symbol, /):
    #fail!!
    #eg: "del local_forgot__deleted_but_not_defined"
    return symbol.is_local() and not _is_symbol_defined(symbol)
def is_symbol_local_defined(symbol, /):
    #       cannot found: del local_forgot__deleted_but_not_defined
    return symbol.is_local() and _is_symbol_defined(symbol)
def _is_symbol_defined(symbol, /):
    return (not symbol.is_free()) and (symbol.is_parameter() or symbol.is_imported() or symbol.is_assigned() or symbol.is_namespace())
r'''
def _collect_all_locals(table, /):
    all_locals = _collect_if__simple(symtable.Symbol.is_local, table)
    return all_locals
    all_locals = set()
    for symbol in table.get_symbols():
        if symbol.is_local():
            all_locals.add(symbol.get_name())
    return all_locals
#'''

def _collect_forgots(table, may_context, /):
    '-> forgot2linenos'
    table2forgots = {}
    def recur(table, context, /):
        all_nonlocals = _collect_if__simple(symtable.Symbol.is_nonlocal, table)
        all_globals = _collect_if__simple(symtable.Symbol.is_global, table)
        all_frees = _collect_if__simple(symtable.Symbol.is_free, table)
        all_but_locals = all_frees|all_globals|all_nonlocals
        all_locals = _collect_if__simple(symtable.Symbol.is_local, table)

        if 0:
            forgots = all_but_locals - context
            #cannot found: del local_forgot__deleted_but_not_defined
        if 1:
            #found defined_locals
            defined_locals = _collect_defined_locals(table)

        forgots1 = all_but_locals - context
        forgots2 = all_locals - defined_locals
        forgots = forgots1 | forgots2
        assert table not in table2forgots
        table2forgots[table] = forgots

        check_type_is(frozenset, context)
        typ = table.get_type()
        if 0:
            context |= all_locals
        else:
            #patch4class_namespace:here
            #   20240129:see:seed.types.PruneableArray
            #bug4class_namespace:goto
            #
            #if 0x0001:print()
            if not typ == 'class':
                context |= all_locals
        if typ == 'class':
            context4method = context | {'__class__'}
        else:
            context4method = context
        for child in table.get_children():
            recur(child, context4method if child.get_type() == 'function' else context)
    #end-def recur(table, context, /):
    def main():
        if may_context is None:
            context = _collect_defined_globals(table)
        else:
            context = may_context
        #d = dict.fromkeys(context)
        #from collections import ChainMap
        context = frozenset(context)
        recur(table, context)
        table2forgots
        forgot2linenos = defaultdict(list)
        for _table, forgots in table2forgots.items():
            lineno = _table.get_lineno()
            for forgot in forgots:
                forgot2linenos[forgot].append(lineno)
        forgot2linenos = {**forgot2linenos}
        for linenos in forgot2linenos.values():
            linenos.sort()
        return forgot2linenos
    return main()




def symtable2forgots(table, not_forgots, may_context=None, /):
    'fname2forgots(__file__, {names from star import})'

    if 0:
        fs = ['is_annotated', 'is_assigned', 'is_declared_global', 'is_free', 'is_global', 'is_imported', 'is_local', 'is_namespace', 'is_nonlocal', 'is_parameter', 'is_referenced']
        for fn in fs:
            print(fn)
            predicator = getattr(symtable.Symbol, fn)
            ns = _collect_if(predicator, table, recursive=True)
            print('   ', ns)
        raise SystemExit
    #defined_globals = _collect_if(symtable.Symbol.is_local, table, recursive=False)
    #all_globals = _collect_if(symtable.Symbol.is_global, table, recursive=True)
    #all_frees = _collect_if(symtable.Symbol.is_free, table, recursive=True)
    #print(defined_globals); raise SystemExit
    #print(all_frees); raise SystemExit

    #forgot2linenos = table2forgots(table)
    forgot2linenos = _collect_forgots(table, may_context)
    forgots = set(forgot2linenos)
    forgots -= set(not_forgots)
    forgots -= set(keyword.kwlist)
    forgots -= builtin_names
    forgots -= module_global_special_attr_frozenset

    forgot2linenos = intersect_keys__immutable(forgot2linenos, forgots)
    return forgot2linenos

def fname2forgots(fname, not_forgots):
    table = fname2symtable(fname)
    forgots = symtable2forgots(table, not_forgots)
    return forgots



















########################## worker ######################



def get_builtin_names():
    return tuple(sorted(_get_builtin_names()))
def _get_builtin_names():
    #builtins = globals.get('__builtins__', __builtins__)
    import builtins
    if inspect.ismodule(builtins):
        return dir(builtins)
    return builtins.keys()
builtin_names = frozenset(get_builtin_names())
del get_builtin_names


def collect_forgots(namespace, output_dict):
    if namespace.get_type() == 'class':
        'where is @xxxx???; once, not found @final_method'
##        print(dir(namespace))
##        #help(namespace)
##        print(namespace.get_identifiers())
##        print(namespace.get_symbols())
##        raise
    elif namespace.get_type() == 'function':
        lineno = namespace.get_lineno()
        for name in namespace.get_globals():
            output_dict[name].append(lineno)
        #output_set.update(namespace.get_globals())
        #output_set.update(namespace.get_frees())
##        if 'x' in output_set:
##            n = namespace
##            #print(dir(n))
##            print(collect_forgots, n.get_name(), sep='\n')
##            print('line:', n.get_lineno())
##            if 'x' in n.get_frees():
##                print('get_frees()')
##            if 'x' in n.get_globals():
##                print('get_globals()')
##            output_set.remove('x')
    _table2forgots__impl(namespace, output_dict)
    for child in namespace.get_children():
        collect_forgots(child, output_dict)

module_global_special_attr_frozenset = frozenset(name for name in importlib.__dict__ if (name.startswith('__') and name.endswith('__')))

def table2forgots(table):
    forgot2linenos = defaultdict(list)
    _table2forgots__impl(table, forgot2linenos)
    forgots = set(forgot2linenos)
    if 0:
        forgots -= set(keyword.kwlist)
    if 0:
        forgots = set(name for name in forgots if not (name.startswith('__') and name.endswith('__')))
        forgots -= module_global_special_attr_frozenset
    forgot2linenos = intersect_keys__immutable(forgot2linenos, forgots)

    for name, ls in forgot2linenos.items():
        forgot2linenos[name] = sorted(set(ls))
    return forgot2linenos

def is_symbol_defined(symbol, /):
    return _is_symbol_defined(symbol)
    return not symbol.is_free()
    return not symbol.is_free() and (symbol.is_parameter() or symbol.is_imported() or symbol.is_assigned() or symbol.is_namespace())
def _table2forgots__impl(table, output_dict):
    forgot2linenos = defaultdict(list)
    defined = set()
    frees = set()
    globals_ = set()
    others = set()
    for symbol in table.get_symbols():
        name = symbol.get_name()
        #if symbol.is_free(): frees.add(name)
        if 0:
            if symbol.is_global(): globals_.add(name)
            #if not(symbol.is_free() or symbol.is_global()): others.add(name)
            if not symbol.is_global(): others.add(name)

            #if symbol.is_free() or symbol.is_global():
            if symbol.is_global():
                if symbol.is_namespace():
                    defined.add(name)
                elif not symbol.is_imported():
                    #forgots.add(name)
                    # ???????? but symbol no get_lineno
                    forgot2linenos[name].append(table.get_lineno())
        is_forgot = False
        if symbol.is_local() or symbol.is_nonlocal():
            if not is_symbol_defined(symbol):
                is_forgot = True
        if symbol.is_global():
                is_forgot = True
        if is_forgot:
            forgot2linenos[name].append(table.get_lineno())
        for namespace in symbol.get_namespaces():
            collect_forgots(namespace, forgot2linenos)

    #pprint(list(map(sorted, (frees, globals_, others, defined))))
    #forgots -= set(get_builtin_names())
    forgots = set(forgot2linenos)
    forgots -= defined
    if 0:forgots -= others
    forgot2linenos = intersect_keys__immutable(forgot2linenos, forgots)
    for name, ls in forgot2linenos.items():
        output_dict[name].extend(ls)
    return
    return forgots








from seed.pkg_tools._forgot_import import symtable2forgots, fname2forgots
from seed.pkg_tools._forgot_import import *
