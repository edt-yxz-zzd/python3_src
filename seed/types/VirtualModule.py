

__all__ = '''
    register_virtual_module_from_name2attr
    VirtualModule
    
    SpecialMemberAccess
    register_virtual_module
    echo
'''.split()

from importlib import import_module
import sys

def vars(obj):
    return object.__getattribute__(obj, '__dict__')



class SpecialMemberAccess:
    # obj_attr_name maynot be a valid identifier; but should be hashable
    
    def __init__(self, cls_attr_name_for_obj_attr_name):
        self.cls_attr_name = cls_attr_name_for_obj_attr_name
    def get_obj_attr_name(self, obj):
        return getattr(type(obj), self.cls_attr_name)

    def get_obj_attr(self, obj):
        return vars(obj)[self.get_obj_attr_name(obj)]
    def set_obj_attr(self, obj, value):
        vars(obj)[self.get_obj_attr_name(obj)] = value

name2attr_accessor = SpecialMemberAccess('__name2attr_name__')

virtual_module_pkg = __name__

def split_qual_name(qual_name):
    names = qual_name.split('.')
    return '.'.join(names[:-1]), names[-1]

def register_virtual_module(virtual_module,
                            module_name,
                            pkg=virtual_module_pkg,
                            assign=False):
    assert module_name.isidentifier()

    qual_name = '.'.join([pkg, module_name]) if pkg else module_name

    pkg, basic = split_qual_name(qual_name)
    if qual_name in sys.modules:
        if sys.modules[qual_name] is not virtual_module:
            raise ValueError('other same name module exists')
    else:
        if pkg:
            import_module(pkg)
        
        sys.modules[qual_name] = virtual_module
        import_module(qual_name)

    if assign and pkg:
        pkg_obj = import_module(pkg)
        if hasattr(pkg_obj, basic):
            raise ValueError('other same name pkg attr exists')
        setattr(pkg_obj, basic, virtual_module)
    return qual_name


def register_virtual_module_from_name2attr(name2attr,
                                           module_name,
                                           pkg=virtual_module_pkg,
                                           assign=False):
    vm = VirtualModule(name2attr)
    return register_virtual_module(vm, module_name, pkg, assign=assign)


class VirtualModule:
    __name2attr_name__ = '--name2attr--'
    def __init__(self, name2attr):
        name2attr_accessor.set_obj_attr(self, name2attr)
    def __getattribute__(self, name):
        return name2attr_accessor.get_obj_attr(self)(name)

    __call__ = __getitem__ = __getattribute__


class CachedName2Attr:
    'not boring underly name2attr with same names'
    def __init__(self, name2attr):
        self.name2attr = name2attr
        self.name2case = {}
    def __call__(self, name):
        try:
            return self.name2case[name]
        except KeyError:pass
        except Exception as e:
            print(repr(e))
            raise

        case = self.name2case[name] = self.name2attr(name)
        return case
    


def echo_attr(name):
    if name == '__all__':
        raise AttributeError('echo module has no attr "__all__"')
    attr = name
    return attr

echo = VirtualModule(echo_attr)

assert echo.aaa == 'aaa'
assert echo.__aaa__ == '__aaa__'

register_virtual_module(echo, 'echo')


##from sand.types.VirtualModule import echo
##assert echo.b == 'b'
##from sand.types.VirtualModule.echo import aaa
##assert aaa == 'aaa'

def _test():
    src = '''
from {VirtualModulePath} import echo
assert echo.b == 'b'
from {VirtualModulePath}.echo import aaa
assert aaa == 'aaa'
'''.format(VirtualModulePath = __name__)
    exec(src)


_test()




    









