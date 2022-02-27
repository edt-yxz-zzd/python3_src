#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
why?
    1.
        logic-err!!!:
            super().__init__(*args, **kwargs)
            super(__class__, sf).__init__(*args, **kwargs)
        should be:
            super(__class__, type(sf)).__init__(sf, *args, **kwargs)
            Super4BypassInstance(__class__, sf).__init__(*args, **kwargs)
    2.
        super().__self__/__self_class__/__thisclass__
            donot reflect/proxy/forward the_wrapped_obj!!!

seed.lang.super4bypass_instance
py -m    seed.lang.super4bypass_instance
py -m nn_ns.app.debug_cmd   seed.lang.super4bypass_instance

from seed.lang.super4bypass_instance import ...

e ../../python3_src/seed/lang/super4bypass_instance.py

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
import ...
from seed.tiny import str2__all__
__all__ = str2__all__(r'''#)
    #(''')
from seed.abc.abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from seed.helper.repr_input import repr_helper
from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f
from seed.helper.check.checkers import check_pair, check_type_is
  #from seed.helper.check.checkers import checks, checkers, check_funcs
  #view ../../python3_src/seed/helper/check/checkers.py
if 0b00:#[01_to_turn_off]
    #0b01
    print(fr'x={x}')
    from seed.tiny import print_err
    print_err(fr'x={x}')
    from pprint import pprint
    pprint(x)
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#super4bypass_instance:goto
#super4subclass:goto
#zzzwww:goto

#[[[super4bypass_instance:begin
print(super(type, type))
print(super(object, type))
print(super(type, object))
print(super(object, object))
assert super(type, type).__self__ is type
assert super(type, type).__self_class__ is type
assert super(type, type).__thisclass__ is type

assert super(object, type).__self__ is type
assert super(object, type).__self_class__ is type
assert super(object, type).__thisclass__ is object

assert super(type, object).__self__ is object
assert super(type, object).__self_class__ is type
assert super(type, object).__thisclass__ is type

assert super(object, object).__self__ is object
assert super(object, object).__self_class__ is None
assert super(object, object).__thisclass__ is object


super(type, type).__self__ is type
super(type, type).__self_class__ is type
super(type, type).__thisclass__ is type

super(object, type).__self__ is type
super(object, type).__self_class__ is type
super(object, type).__thisclass__ is object

super(type, object).__self__ is object
super(type, object).__self_class__ is type
super(type, object).__thisclass__ is type

super(object, object).__self__ is object
super(object, object).__self_class__ is None
super(object, object).__thisclass__ is object




class Super4BypassInstance:
    #__slots__ = ('_super',)
    __slots__ = ('__the_self__', '__may_the_self_middle_class__', '__imay_idx4the_self_middle_class__')
    r'''
    help(super)
    |  __self__
    |      the instance invoking super(); may be None
    |  __self_class__
    |      the type of the instance invoking super(); may be None
    |  __thisclass__
    |      the class invoking super()
    #'''
    def __init__(sf, may__class__, instance, /):
        if may__class__ is not None:
            __class__ = may__class__
            if not isinstance(instance, __class__): raise TypeError
            mro = type(instance).__mro__
            try:
                i = mro.index(__class__)
            except ValueError:
                #eg. __class__ :: ABCMeta
                raise TypeError
            imay_idx = i
        else:
            imay_idx = -1
        object.__setattr__(sf, '__the_self__', instance)
        object.__setattr__(sf, '__may_the_self_middle_class__', may__class__)
        object.__setattr__(sf, '__imay_idx4the_self_middle_class__', imay_idx)
        #_super = super(__class__, type(instance))
        #object.__setattr__(sf, '_super', _super)
    def __getattribute__(sf, attr, /):
        imay_idx = object.__getattribute__(sf, '__imay_idx4the_self_middle_class__')
        may__class__ = object.__getattribute__(sf, '__may_the_self_middle_class__')
        instance = object.__getattribute__(sf, '__the_self__')

        mro = type(instance).__mro__

        if may__class__ is not None:
            __class__ = may__class__
            assert imay_idx >= 0
            i = imay_idx
            if not __class__ is mro[i]: raise TypeError
        else:
            assert imay_idx == -1
        for j in range(imay_idx+1, len(mro)):
            cls = mro[j]
            if attr in cls.__dict__:
                value_or_descriptor = cls.__dict__[attr]
                break
        else:
            raise AttributeError(f'{attr!r} not in Super4BypassInstance({may__class__!r}, {type(instance)!r})')
        may_get = getattr(type(value_or_descriptor), '__get__', None)
        if may_get is not None:
            descriptor = value_or_descriptor
            __get__ = may_get
            value = __get__(descriptor, instance, None)
        else:
            value = value_or_descriptor
        return value

        #
        _super = object.__getattribute__(sf, '_super')
        f = getattr(_super, attr)
        #return types.MethodType(f, sf.....)
    def __setattr__(sf, attr, value, /):
        raise AttributeError
    def __delattr__(sf, attr, /):
        raise AttributeError

#]]]super4bypass_instance:end

#[[[super4subclass:begin
class Super4Subclass:
    __slots__ = ('__the_self_class__', '__may_the_self_middle_class__', '__imay_idx4the_self_middle_class__')
    def __init__(sf, may__class__, cls4instance, /):
        if may__class__ is not None:
            __class__ = may__class__
            if not issubclass(cls4instance, __class__): raise TypeError
            mro = cls4instance.__mro__
            try:
                i = mro.index(__class__)
            except ValueError:
                #eg. __class__ :: ABCMeta
                raise TypeError
            imay_idx = i
        else:
            imay_idx = -1
        object.__setattr__(sf, '__the_self_class__', cls4instance)
        object.__setattr__(sf, '__may_the_self_middle_class__', may__class__)
        object.__setattr__(sf, '__imay_idx4the_self_middle_class__', imay_idx)
    def __getattribute__(sf, attr, /):
        imay_idx = object.__getattribute__(sf, '__imay_idx4the_self_middle_class__')
        may__class__ = object.__getattribute__(sf, '__may_the_self_middle_class__')
        cls4instance = object.__getattribute__(sf, '__the_self_class__')

        mro = cls4instance.__mro__

        if may__class__ is not None:
            __class__ = may__class__
            assert imay_idx >= 0
            i = imay_idx
            if not __class__ is mro[i]: raise TypeError
        else:
            assert imay_idx == -1
        for j in range(imay_idx+1, len(mro)):
            cls = mro[j]
            if attr in cls.__dict__:
                value_or_descriptor = cls.__dict__[attr]
                break
        else:
            raise AttributeError(f'{attr!r} not in Super4Subclass({may__class__!r}, {cls4instance!r})')
        may_get = getattr(type(value_or_descriptor), '__get__', None)
        if may_get is not None:
            descriptor = value_or_descriptor
            __get__ = may_get
            value = __get__(descriptor, None, cls4instance)
        else:
            value = value_or_descriptor
        return value

    def __setattr__(sf, attr, value, /):
        raise AttributeError
    def __delattr__(sf, attr, /):
        raise AttributeError


#]]]super4subclass:end

#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):



