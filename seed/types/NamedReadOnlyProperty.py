
r'''
e ../../python3_src/seed/types/NamedReadOnlyProperty.py

used in ImmutableNamespaceBase



''' r"""
usage:
from seed.types.NamedReadOnlyProperty import NamedReadOnlyProperty, set_NamedReadOnlyProperty4cls_, set_NamedReadOnlyProperty4sf_
_attr_nms = r'''
    aaa
    '''.split()#'''
class ZZZ:
    def __init__(sf, aaa, /):
        ########init sf:
        set_NamedReadOnlyProperty4sf_(sf, _attr_nms, locals())
if 1:
    set_NamedReadOnlyProperty4cls_(ZZZ, _attr_nms)
#end-class ZZZ:
=====or:
from seed.helper.repr_input import repr_helper
class ZZZ:
    _attr_nms = r'''
    aaa
    '''.split()#'''

    def get_args(sf, /):
        return tuple(getattr(sf, nm) for nm in __class__._attr_nms)
    def __repr__(sf, /):
        args = sf.get_args()
        return repr_helper(sf, *args)
    def __init__(sf, aaa, /):
        ########init sf:
        set_NamedReadOnlyProperty4sf_(sf, __class__._attr_nms, locals())
if 1:
    set_NamedReadOnlyProperty4cls_(ZZZ, ZZZ._attr_nms)
#end-class ZZZ:


"""#"""


__all__ = '''
    NamedReadOnlyProperty
    set_NamedReadOnlyProperty4cls_
    set_NamedReadOnlyProperty4sf_
    '''.split()

from seed.helper.repr_input import repr_helper

class NamedReadOnlyProperty:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return vars(instance)[self.name]
        return instance.__dict__[self.name]

    # MUST define "__set__" to make self a data_descriptor
    #   otherwise, instance override self
    def __set__(self, instance, value):
        raise AttributeError(self.name)
    def __delete__(self, instance):
        raise AttributeError(self.name)
    def __repr__(self):
        return repr_helper(self, self.name)



def set_NamedReadOnlyProperty4cls_(cls, attr_nms, /):
    assert isinstance(cls, type)
    for nm in attr_nms:
        setattr(cls, nm, NamedReadOnlyProperty(nm))
def set_NamedReadOnlyProperty4sf_(sf, attr_nms, locals, /):
    d = vars(sf)
    for nm in attr_nms:
        d[nm] = locals[nm]


from seed.types.NamedReadOnlyProperty import NamedReadOnlyProperty, set_NamedReadOnlyProperty4cls_, set_NamedReadOnlyProperty4sf_
from seed.types.NamedReadOnlyProperty import *
