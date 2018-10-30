
'''
usage:
    see: .LexPostprocess
    see: nn_ns.my_fileformat.configuration.MyConfiguration2_lex
'''

__all__ = '''
    make_pseudo_lex_module_obj
    show_pseudo_lex_module_obj
    make_pseudo_yacc_module_obj
    show_pseudo_yacc_module_obj
    '''.split()


from types import SimpleNamespace, FunctionType
from collections.abc import Collection, Mapping

lex_required_names = 'tokens states __file__'.split()
    #   ply.lex.lex requires __file__
yacc_required_names = 'tokens start __file__'.split()
    #   ply.yacc.yacc requires __file__

lex_kwargs = dict(required_names=lex_required_names, prefixes={'t_',})
yacc_kwargs = dict(required_names=yacc_required_names, prefixes={'p_',})

def make_pseudo_lex_module_obj(module_or_class_or_dict):
    return make_pseudo_X_module_obj('lex', module_or_class_or_dict, **lex_kwargs)
def make_pseudo_yacc_module_obj(module_or_class_or_dict):
    return make_pseudo_X_module_obj('yacc', module_or_class_or_dict, **yacc_kwargs)

def check_type(x, T):
    if not isinstance(x, T): raise TypeError
def check_strs(ss):
    if isinstance(ss, str): raise TypeError
    if not isinstance(ss, Collection): raise TypeError
    if not all(type(s) is str for s in ss): raise TypeError

def make_pseudo_X_module_obj__from_dict(
    module_classX, module_dict, *, required_names, prefixes
    ):
    assert isinstance(module_dict, Mapping)
    check_strs(required_names)
    check_strs(prefixes)

    g = module_dict # globals; del globals

    d = {}
    for name in required_names:
        d[name] = g[name]

    for prefix in set(prefixes):
        d.update((name, value)
                for name, value in g.items()
                if name.startswith(prefix)
                )

    return SimpleNamespace(**d)

    x = SimpleNamespace()
    #fail:x.__dict__ = d
    x.__dict__.clear()
    x.__dict__.update(d)
    return x

def make_pseudo_X_module_obj(
    module_classX, module_or_class_or_dict, *, required_names, prefixes
    ):
    # module_classX = X = 'lex' or 'yacc'
    assert module_classX in ('lex', 'yacc')
        # why?
        #   when module_or_class_or_dict is a class obj
        #       it pass by the test of required_names!
        #

    x = module_or_class_or_dict
    if isinstance(x, dict):
        if not all(n in x for n in required_names):
            missing = set(required_names) - set(x)
            raise Exception(f'not a {module_classX!r} module dict: missing {missing!r}')
        module_dict = x
        pseudo_X_module = make_pseudo_X_module_obj__from_dict(
            module_classX
            , module_dict
            , required_names=required_names
            , prefixes=prefixes
            )
    elif isinstance(x, str):
        raise NotImplementedError('??should be module name or script file path??')
    elif isinstance(x, type):
        pseudo_X_module = cls = x
        # cls neednot '__file__'!!!!
    elif all(hasattr(x, n) for n in required_names):
        pseudo_X_module = module = x
    else:
        missing = {n for n in required_names if not hasattr(x, n)}
        raise Exception(f'not a {module_classX!r} module: missing {missing!r}')
        raise Exception(f'not a {module_classX!r} module')
    return pseudo_X_module



def show_pseudo_lex_module_obj(pseudo_lex_module):
    return show_pseudo_X_module_obj('lex', pseudo_lex_module, **lex_kwargs)
def show_pseudo_yacc_module_obj(pseudo_yacc_module):
    return show_pseudo_X_module_obj('yacc', pseudo_yacc_module, **yacc_kwargs)
def show_pseudo_X_module_obj(
    module_classX, pseudo_X_module, *, required_names, prefixes
    ):
    assert module_classX in ('lex', 'yacc')
    assert type(pseudo_X_module) is SimpleNamespace
    check_strs(required_names)
    check_strs(prefixes)

    d = pseudo_X_module.__dict__
    required_names = set(required_names)
    for name, f in d.items():
        print(name)
        if any(name.startswith(prefix) for prefix in prefixes):
            tp = type(f)
            if tp is FunctionType:
                print(f'\t{f.__doc__}')
            elif tp is str:
                print(f'\t{f!r}')
            else:
                raise logic-error
        elif name in required_names:
            print(f'\t{f!r}')
        else:
            raise TypeError(f'not the SimpleNamespace pseudo_X_module: pseudo_{module_classX}_module')
        print()


