

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
'''

__all__ = '''
    symtable2forgots
    fname2forgots
    '''.split()

from seed.mapping_tools.dict_op import intersect_keys__immutable
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

def symtable2forgots(table, not_forgots):
    'fname2forgots(__file__, {names from star import})'
    forgot2linenos = table2forgots(table)
    forgots = set(forgot2linenos)
    forgots -= set(not_forgots)
    forgots -= builtin_names
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
    if namespace.has_children():
        for child in namespace.get_children():
            collect_forgots(child, output_dict)
def table2forgots(table):
    forgot2linenos = defaultdict(list)
    _table2forgots__impl(table, forgot2linenos)
    forgots = set(forgot2linenos)
    forgots -= set(keyword.kwlist)
    forgots = set(name for name in forgots
                  if not (name.startswith('__') and name.endswith('__')))
    forgot2linenos = intersect_keys__immutable(forgot2linenos, forgots)

    for name, ls in forgot2linenos.items():
        forgot2linenos[name] = sorted(set(ls))
    return forgot2linenos

def _table2forgots__impl(table, output_dict):
    forgot2linenos = defaultdict(list)
    defined = set()
    frees = set()
    globals_ = set()
    others = set()
    for symbol in table.get_symbols():
        name = symbol.get_name()
        #if symbol.is_free(): frees.add(name)
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
        for namespace in symbol.get_namespaces():
            collect_forgots(namespace, forgot2linenos)

    #pprint(list(map(sorted, (frees, globals_, others, defined))))
    #forgots -= set(get_builtin_names())
    forgots = set(forgot2linenos)
    forgots -= defined
    forgots -= others
    forgot2linenos = intersect_keys__immutable(forgot2linenos, forgots)
    for name, ls in forgot2linenos.items():
        output_dict[name].extend(ls)
    return
    return forgots








