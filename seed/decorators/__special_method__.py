
'''
why?
    to prevent:
        self.__special_method__
        super().__special_method__
    to force:
        cls.__special_method__


'''




__all__ = '''
    __instance_method__
    __class_method__
    __static_method__

    __special_method__
    SpecialMethodAccessError
    '''.split()



class SpecialMethodAccessError(Exception):pass
class __special_method__:
    #__slots__ = ['name']
    #def __init__(self): self.name = None
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, instance, owner):
        if instance is None:
            cls = type(self)
            return super(__class__, self).__get__(None, owner)
        raise SpecialMethodAccessError(f'should access via class: cls.__static_method__: cls.{self.name}')
    def __set__(self, instance, value):
        raise AttributeError
    def __delete__(self, instance):
        raise AttributeError

class __static_method__(__special_method__, staticmethod):
    __slots__ = ()
class __class_method__(__special_method__, classmethod):
    __slots__ = ()
#class __instance_method__(__special_method__, instancemethod):
class __instance_method__(__special_method__, staticmethod):
    __slots__ = ()



def _t():
    from seed.tiny import expectError
    class B:
        @__static_method__
        def __s__():
            return 1
        @__class_method__
        def __c__(cls):
            return cls
        @__instance_method__
        def __i__(self):
            return 2

    class C(B):
        @__static_method__
        def __s__():
            return super(__class__, __class__).__s__()
        @__class_method__
        def __c__(cls):
            return super().__c__()
        @__instance_method__
        def __i__(self):
            return super().__i__()

    B.__s__
    B.__c__
    B.__i__
    C.__s__
    C.__c__
    C.__i__

    assert B.__s__() == 1
    assert B.__c__() is B
    assert C.__s__() == 1
    assert C.__c__() is C

    b = B()
    assert expectError(SpecialMethodAccessError, lambda:b.__s__)
    assert expectError(SpecialMethodAccessError, lambda:b.__c__)
    assert expectError(SpecialMethodAccessError, lambda:b.__i__)
    assert B.__i__(b) == 2

    c = C()
    assert expectError(SpecialMethodAccessError, lambda:c.__s__)
    assert expectError(SpecialMethodAccessError, lambda:c.__c__)
    assert expectError(SpecialMethodAccessError, lambda:c.__i__)
    assert expectError(SpecialMethodAccessError, lambda:C.__i__(c))


    """
    # to find instancemethod??

    from inspect import getattr_static
    class D:
        def f(self):pass
    f = getattr_static(D, 'f')
    print(type(f))
    """

if __name__ == "__main__":
    _t()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


