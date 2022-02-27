r'''
seed.lang.basic_descriptors
py -m seed.lang.basic_descriptors
py -m nn_ns.app.debug_cmd   seed.lang.basic_descriptors

seed.lang.basic_descriptors
seed.lang.apply_descriptor_protocol
seed.abc.IDescriptor
e ../../python3_src/seed/lang/basic_descriptors.py
e ../../python3_src/seed/lang/apply_descriptor_protocol.py
e ../../python3_src/seed/abc/IDescriptor.py


from seed.lang.basic_descriptors import BasicNonDataDescriptor4InstanceMethod as NonDataDescriptor4InstanceMethod
from seed.lang.basic_descriptors import NonDataDescriptor4InstanceMethod
from seed.lang.basic_descriptors import NonDataDescriptor4InstanceMethod, NonDataDescriptor4ClassMethod, NonDataDescriptor4StaticMethod, NonDataDescriptor4Echo
from seed.lang.basic_descriptors import descriptor4instance_method, descriptor4class_method, descriptor4static_method, descriptor4echo




from seed.abc.IDescriptor import NonDataDescriptor4InstanceMethod
from seed.abc.IDescriptor import NonDataDescriptor4InstanceMethod, NonDataDescriptor4ClassMethod, NonDataDescriptor4StaticMethod, NonDataDescriptor4Echo
from seed.abc.IDescriptor import descriptor4instance_method, descriptor4class_method, descriptor4static_method, descriptor4echo

>>> def g():pass
>>> is_descriptor(g)
True
>>> is_non_data_descriptor(g)
True
>>> is_data_descriptor(g)
False

>>> is_descriptor(BasicNonDataDescriptor4InstanceMethod(id))
True
>>> is_non_data_descriptor(BasicNonDataDescriptor4InstanceMethod(id))
True
>>> is_data_descriptor(BasicNonDataDescriptor4InstanceMethod(id))
False

>>> class B:
...     @BasicNonDataDescriptor4InstanceMethod
...     def echo(*args):return args
>>> B_echo = B.__dict__['echo']
>>> b = B()
>>> type(B_echo) is BasicNonDataDescriptor4InstanceMethod
True
>>> B.echo is B_echo.__func__
True
>>> B.echo()
()
>>> b.echo() == (b,)
True

#'''

__all__ = '''
    BasicNonDataDescriptor4InstanceMethod

    NonDataDescriptor4InstanceMethod
    NonDataDescriptor4ClassMethod
    NonDataDescriptor4StaticMethod
        descriptor4instance_method
        descriptor4class_method
        descriptor4static_method


    '''.split()


from types import MethodType
#from seed.debug.expectError import expectError
from seed.lang.apply_descriptor_protocol import is_descriptor, is_data_descriptor, is_non_data_descriptor


class BasicNonDataDescriptor4InstanceMethod:
    'basic cmp to seed.abc.IDescriptor.NonDataDescriptor4InstanceMethod'
    #__slots__ = ()
    #@property __func__

    def __init__(sf, __func__, /):
        sf.__func__ = __func__
        super().__init__()

    def __get__(sf, may_instance, may_owner=None, /):
        if may_instance is None:
            return sf.__func__
        else:
            instance = may_instance
            return MethodType(sf.__func__, instance)

NonDataDescriptor4InstanceMethod = BasicNonDataDescriptor4InstanceMethod
NonDataDescriptor4ClassMethod = classmethod
NonDataDescriptor4StaticMethod = staticmethod

descriptor4instance_method = NonDataDescriptor4InstanceMethod
descriptor4class_method = NonDataDescriptor4ClassMethod
descriptor4static_method = NonDataDescriptor4StaticMethod


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):



