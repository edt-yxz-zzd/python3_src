
'''
see:
    seed.pkg_tools.import_object
'''

__all__ = '''
    import_object
    '''.split()

import builtins, importlib


def import_object(obj_qname):
    module_qname, may_dot, obj_name = obj_qname.rpartition('.')
    assert obj_name.isidentifier()
    if not may_dot:
        module = builtins
    else:
        module = importlib.import_module(module_qname)
    obj = getattr(module, obj_name)
    return obj


