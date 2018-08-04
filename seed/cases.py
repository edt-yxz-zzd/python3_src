
__all__ = '''
    ECHO
    ENUM
    CLASS
'''.split()


from seed.types.VirtualModule import register_virtual_module_from_name2attr, \
     CachedName2Attr

def echo(name):
    return name

class _Enum:
    # CachedName2Attr(_Enum())
    def __init__(self, begin=0):
        assert type(begin) is int
        self.new = begin
    def __call__(self, name):
        case = self.new
        self.new += 1
        return case

class ClassCaseBase:pass
def name2class(name):
    # CachedName2Attr(name2class)
    return type(name, (ClassCaseBase,), {})


    
func_module_pairs = [
    (echo, 'ECHO'),
    (CachedName2Attr(_Enum()), 'ENUM'),
    (CachedName2Attr(name2class), 'CLASS')]
for name2attr, module_name in func_module_pairs:
    register_virtual_module_from_name2attr(name2attr, module_name, __name__, True)

