

'''
FinalAttrMeta
    to stop casually override class attributes
FinalTypeMeta
    to prevent deriving from the metaclass's instances
FinalT_ABCMeta = FinalAttrMeta + FinalTypeMeta + abc.ABCMeta
'''


__all__ = ('''
    FinalAttrCollisionError final_attr final_method
    FinalAttrMeta FinalTypeMeta FinalT_ABCMeta
''').split()

##
##from sand import fixed__package__
##fixed__package__(globals())
##from sand import top_level_import
##assert top_level_import(__name__, 'import_main.forgot_import', args=('logic error',))
##assert top_level_import(__name__, 'import_main.collect_globals',
##        kwargs=dict(pred=None, include='', exclude='''
##    main'''))

from .. import anonym_class_attr, anonym_readonly_method,\
     frozendict, head_ex, sum_dicts
from itertools import chain
from abc import ABCMeta
from inspect import getattr_static




class FinalAttrCollisionError(NameError):pass
class final_attr(anonym_class_attr):pass
class final_method(anonym_readonly_method, final_attr):pass


class FinalAttrMeta(type):
    '''to stop casually override class attributes at class definition


but cannot prevent: 'Derived.attr = 2'
check only happens at build stage
usage:
    class XX(metaclass=FinalAttrMeta):
        xxx = final_attr(value)
        @final_method
        def meth(self,...):...
        
example:
    >>> class C(metaclass=FinalAttrMeta):
    ...     @final_method
    ...     def f(self):
    ...         'f.doc'
    ...         return 1

    >>> C().f() == 1
    True
    >>> C.f(C()) == 1
    True
    >>> C().f.__doc__ == 'f.doc'
    True

    >>> class D(C):pass
    >>> class D(C):            # doctest: +IGNORE_EXCEPTION_DETAIL
    ...     def f(self):pass
    Traceback (most recent call last):
    ...
    FinalAttrCollisionError: ...


    >>> class B(C):pass
    >>> class E(B,D):pass
    >>> class B:
    ...     def f(self):pass
    >>> class E(D,B):pass
    >>> class E(B,D):pass # B.f override D.f  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    FinalAttrCollisionError: ...
'''
    def __new__(cls, name, bases, namespace, **kwargs):
        self = super(__class__, cls).__new__(cls, name, bases, namespace, **kwargs)
        new_finals = frozendict((attr, obj) for attr, obj in namespace.items()
                                if isinstance(obj, final_attr))
        self.__this_finals = new_finals

        #print(self, list(self.mro()))
        _self, iter_bases = head_ex(base for base in self.mro())
        assert _self is self
        dicts = map(cls.get_this_finals, iter_bases)
        # NOTE: order is important: ([new_finals], dicts)
        dicts = tuple(chain([new_finals], dicts))
        finals = sum_dicts(dicts)
        if len(finals) != sum(map(len, dicts)):
            raise FinalAttrCollisionError('final attrs collision')

        #print(finals)
        #print(self, sorted(vars(self)))
        for attr in finals:
            #print(attr)
            #print(type(getattr_static(self, attr)))
            if getattr(self, attr) is not finals[attr].__get__(None, self) or\
               getattr_static(self, attr) is not finals[attr]:
                raise FinalAttrCollisionError(
                    'override final attr: {!r}'.format(attr))
        return self
        
    
    @classmethod
    def get_this_finals(cls, obj):
        'not include attrs of base classes; attrname2obj'
        if not isinstance(obj, __class__):
            return frozendict()
        return obj.__this_finals

def _test_FinalAttrMeta():
    class C(metaclass=FinalAttrMeta):
        @final_method
        def f(self):
            'f.doc'
            return 1

    assert C().f() == 1
    assert C.f(C()) == 1
    #print('here')
    assert C().f.__doc__ == 'f.doc'
    #print(C.get_this_finals(C))

    # bug: I cannot stop the following assignment:
    # C.f = 3 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # check only happens at build stage

    class D(C):pass
    try:
        class D(C):
            def f(self):pass
        raise logic-error
    except FinalAttrCollisionError:pass

    class B(C):pass
    class E(B,D):pass
    class B:
        def f(self):pass
    class E(D,B):pass
    try:
        class E(B,D):pass
        raise logic-error
    except FinalAttrCollisionError:
        pass
_test_FinalAttrMeta()





    

class FinalTypeMeta(type):
    '''to prevent deriving from the metaclass's instances.

example:
    >>> class C(metaclass=FinalTypeMeta):pass
    >>> class B(C):pass # final?  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    TypeError: ...
'''
##    def __new__(cls, name, bases, namespace, **kwargs):
##        self = super(__class__, cls).__new__(cls, name, bases, namespace, **kwargs)
    def __init__(self, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)
        cls = type(self)
        if any(cls.is_final_class(base) for base in self.__bases__):
            raise TypeError('derive from final class')
        return

    @classmethod
    def is_final_class(cls, obj):
        return isinstance(obj, __class__)
    
def _test_FinalTypeMeta():
    ##class B(metaclass=ABCMeta):pass
    ##class D(B, metaclass=FinalTypeMeta):pass
    class C(metaclass=FinalTypeMeta):pass

    try:
        # final?
        class B(C):pass
        raise logic - error
    except TypeError:
        pass
_test_FinalTypeMeta()


class FinalT_ABCMeta(FinalTypeMeta, FinalAttrMeta, ABCMeta):pass




if __name__ == "__main__":
    import doctest
    doctest.testmod()


