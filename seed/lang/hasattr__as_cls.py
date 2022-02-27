#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.lang.hasattr__as_cls
py -m    seed.lang.hasattr__as_cls
py -m nn_ns.app.debug_cmd   seed.lang.hasattr__as_cls
e ../../python3_src/seed/lang/hasattr__as_cls.py


why?
    #################################
    any("__iter__" in B.__dict__ for B in C.__mro__)
        not hasattr(cls, "__iter__")
    #################################
    class Iterable(ABC):
        __slots__ = ()
        @classmethod
        @override
        def __subclasshook__(cls, C, /):
            # ABCMeta::__subclasshook__
            if cls is __class__:
                #assert isinstance(C, type)
                if any("__iter__" in B.__dict__ for B in C.__mro__):
                    return True
            return NotImplemented
    #################################


from seed.lang.hasattr__as_cls import hasattr__as_cls, hasattr__via_cls, relay_hasattr__as_cls

from seed.lang.hasattr__as_cls import getattr_ex__as_cls__not_apply_descriptor_protocol, getattr_tmay__as_cls__apply_descriptor_protocol, getattr_tmay__via_cls__apply_descriptor_protocol

from seed.lang.hasattr__as_cls import hasattr_if__as_cls__apply_descriptor_protocol, hasattr_if__via_cls__apply_descriptor_protocol, flip_predicator, is_None, is_not_None, not_callable #callable

from seed.lang.hasattr__as_cls import hasattr_not_None__as_cls__apply_descriptor_protocol, hasattr_not_None__via_cls__apply_descriptor_protocol, hasattr_callable__as_cls__apply_descriptor_protocol, hasattr_callable__via_cls__apply_descriptor_protocol


from seed.lang.hasattr__as_cls import relay_hasattr__as_cls, relay_getattr_ex__as_cls__not_apply_descriptor_protocol,  relay_getattr_tmay__as_cls__apply_descriptor_protocol,  relay_hasattr_if__as_cls__apply_descriptor_protocol


from seed.lang.hasattr__as_cls import iter_relay_getattr_ex__as_cls__not_apply_descriptor_protocol, iter_relay_getattr_ex__as_cls__apply_descriptor_protocol





#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>> class Meta(type):
...     def fff(sf_as_cls, /):pass
>>> class C(metaclass=Meta):pass
>>> c = C()
>>> c.fff = id
>>> hasattr(c, 'fff')
True
>>> hasattr(type(c), 'fff')
True
>>> hasattr(type(type(c)), 'fff')
True
>>> hasattr(type(type(type(c))), 'fff')
False

>>> hasattr__via_cls(c, 'fff')
False
>>> hasattr__via_cls(type(c), 'fff')
True
>>> hasattr__via_cls(type(type(c)), 'fff')
False

>>> hasattr__as_cls(type(c), 'fff')
False
>>> hasattr__as_cls(type(type(c)), 'fff')
True
>>> hasattr__as_cls(type(type(type(c))), 'fff')
False




#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''
    getattr_ex__as_cls__not_apply_descriptor_protocol
        hasattr__as_cls
        hasattr__via_cls
        relay_hasattr__as_cls
        iter_relay_getattr_ex__as_cls__not_apply_descriptor_protocol
            relay_getattr_ex__as_cls__not_apply_descriptor_protocol

    getattr_tmay__as_cls__apply_descriptor_protocol
        relay_getattr_tmay__as_cls__apply_descriptor_protocol
        iter_relay_getattr_ex__as_cls__apply_descriptor_protocol
        getattr_tmay__via_cls__apply_descriptor_protocol

        hasattr_if__as_cls__apply_descriptor_protocol
            relay_hasattr_if__as_cls__apply_descriptor_protocol
            hasattr_if__via_cls__apply_descriptor_protocol
            flip_predicator
            is_None
            is_not_None
                hasattr_not_None__as_cls__apply_descriptor_protocol
                    hasattr_not_None__via_cls__apply_descriptor_protocol
            not_callable
                hasattr_callable__as_cls__apply_descriptor_protocol
                    hasattr_callable__via_cls__apply_descriptor_protocol
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny import check_type_is
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

#[[[zzzwww:begin
def getattr_ex__as_cls__not_apply_descriptor_protocol(cls, key, /):
    '-> may (initial_cls4mro, new_mro_idx4middle_relay_cls, new_middle_relay_cls, key, value)  #to avoid instance.__dict__ and meta.attr'
    Nothing = object()
    for i, B in enumerate(cls.__mro__):
        m = B.__dict__.get(key, Nothing)
        if m is not Nothing:
            value = m
            break
    else:
        return None
    return (cls, i, B, key, value)
def hasattr__as_cls(cls, key, /):
    return any(key in B.__dict__ for B in cls.__mro__)
    return not None is getattr_ex__as_cls__not_apply_descriptor_protocol(cls, key)
def hasattr__via_cls(obj, key, /):
    cls = type(obj)
    may_instance = obj
    return hasattr__as_cls(type(obj), key)





def relay_hasattr__as_cls(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, /, *, offset4restart_from_middle:int):
    (mro_idx4middle_relay_cls, middle_relay_cls, restart_idx4mro) = _initial_of_relay(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, offset4restart_from_middle)

    mro = initial_cls4mro.__mro__
    return any(key in mro[i].__dict__ for i in range(restart_idx4mro, len(mro)))
def relay_getattr_ex__as_cls__not_apply_descriptor_protocol(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, /, *, offset4restart_from_middle:int):
    '-> may (initial_cls4mro, new_mro_idx4middle_relay_cls, new_middle_relay_cls, key, value)   #to mimic  super()'
    it = iter_relay_getattr_ex__as_cls__not_apply_descriptor_protocol(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, offset4restart_from_middle=offset4restart_from_middle)
    for (initial_cls4mro, new_mro_idx4middle_relay_cls, new_middle_relay_cls, key, value) in it:
        return (initial_cls4mro, new_mro_idx4middle_relay_cls, new_middle_relay_cls, key, value)
    return None
def iter_relay_getattr_ex__as_cls__not_apply_descriptor_protocol(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, /, *, offset4restart_from_middle:int):
    '-> Iter (initial_cls4mro, new_mro_idx4middle_relay_cls, new_middle_relay_cls, key, value)   #to support delta-member: delta-check, delta-constraint-specification, dispatch-init-sink, listener-callback, monotonic-data-description-neighbor-check'
    (mro_idx4middle_relay_cls, middle_relay_cls, restart_idx4mro) = _initial_of_relay(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, offset4restart_from_middle)

    mro = initial_cls4mro.__mro__
    Nothing = object()
    for i in range(restart_idx4mro, len(mro)):
        B = mro[i]
        m = B.__dict__.get(key, Nothing)
        if m is not Nothing:
            value = m
            new_middle_relay_cls = B
            new_mro_idx4middle_relay_cls = i
            yield (initial_cls4mro, new_mro_idx4middle_relay_cls, new_middle_relay_cls, key, value)
    return
def _initial_of_relay(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, offset4restart_from_middle:int, /):
    check_type_is(int, offset4restart_from_middle)
    mro = initial_cls4mro.__mro__
    check_type_is(tuple, mro)
    assert mro

    if may_mro_idx4middle_relay_cls is None is may_middle_relay_cls:
        mro_idx4middle_relay_cls = 0
        middle_relay_cls = mro[0]
    else:
        if may_middle_relay_cls is None:
            mro_idx4middle_relay_cls = may_mro_idx4middle_relay_cls
            check_type_is(int, mro_idx4middle_relay_cls)
            middle_relay_cls = mro[mro_idx4middle_relay_cls]
        else:
            middle_relay_cls = may_middle_relay_cls

            if may_mro_idx4middle_relay_cls is None:
                mro_idx4middle_relay_cls = mro.index(middle_relay_cls)
            else:
                mro_idx4middle_relay_cls = may_mro_idx4middle_relay_cls
        mro_idx4middle_relay_cls
        middle_relay_cls
        check_type_is(int, mro_idx4middle_relay_cls)
        if not 0 <= mro_idx4middle_relay_cls < len(mro): raise TypeError
            # <
        if not mro[mro_idx4middle_relay_cls] is middle_relay_cls: raise TypeError

    ######################################
    ######################################
    restart_idx4mro = mro_idx4middle_relay_cls + offset4restart_from_middle
    if not 0 <= restart_idx4mro <= len(mro): raise TypeError
        # <=
    return mro_idx4middle_relay_cls, middle_relay_cls, restart_idx4mro







def getattr_tmay__as_cls__apply_descriptor_protocol(cls, key, may_instance, /):
    m = getattr_ex__as_cls__not_apply_descriptor_protocol(cls, key)
    return _may2tmay__convert_result_of_getattr_ex(m, may_instance)
def relay_getattr_tmay__as_cls__apply_descriptor_protocol(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, may_instance, /, *, offset4restart_from_middle:int):
    m = relay_getattr_ex__as_cls__not_apply_descriptor_protocol(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, offset4restart_from_middle=offset4restart_from_middle)
    return _may2tmay__convert_result_of_getattr_ex(m, may_instance)
def _may2tmay__convert_result_of_getattr_ex(result_of_getattr_ex, may_instance):
    m = result_of_getattr_ex
    if m is None:
        return ()
    (_cls, _i, _B, _key, _value) = m
    value = _apply_descriptor_protocol(_cls, _i, _B, _key, _value, may_instance)
    return (value,)

def iter_relay_getattr_ex__as_cls__apply_descriptor_protocol(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, may_instance, /, *, offset4restart_from_middle:int):
    '-> ((initial_cls4mro, new_mro_idx4middle_relay_cls, new_middle_relay_cls, key, value__pre_protocol), may_instance, value__post_protocol)'
    it = iter_relay_getattr_ex__as_cls__not_apply_descriptor_protocol(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, offset4restart_from_middle=offset4restart_from_middle)
    #for (initial_cls4mro, new_mro_idx4middle_relay_cls, new_middle_relay_cls, key, value) in it:
    for tpl in it:
        (_cls, _i, _B, _key, _value) = tpl
        value = _apply_descriptor_protocol(_cls, _i, _B, _key, _value, may_instance)
        yield (tpl, may_instance, value)
        #yield value
    return
def _apply_descriptor_protocol(initial_cls4mro, mro_idx4middle_relay_cls, middle_relay_cls, key, _value, may_instance, /):
    #if hasattr(_value, '__get__') and hasattr(type(_value), '__get__'):
    if hasattr__as_cls(type(_value), '__get__'):
        descriptor = _value
        #may_instance = None
        value = type(descriptor).__get__(descriptor, may_instance, initial_cls4mro)
    else:
        value = _value #echo
    return value

def getattr_tmay__via_cls__apply_descriptor_protocol(obj, key, /):
    cls = type(obj)
    may_instance = obj
    return getattr_tmay__as_cls__apply_descriptor_protocol(cls, key, may_instance)






def hasattr_if__as_cls__apply_descriptor_protocol(predicator, cls, key, may_instance, /, *, flip:bool):
    flip = bool(flip)
    tmay_value = getattr_tmay__as_cls__apply_descriptor_protocol(cls, key, may_instance)
    return _tail_of_hasattr_if(predicator, tmay_value, flip)
def relay_hasattr_if__as_cls__apply_descriptor_protocol(predicator, initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, may_instance, /, *, offset4restart_from_middle:int, flip:bool):
    flip = bool(flip)
    tmay_value = relay_getattr_tmay__as_cls__apply_descriptor_protocol(initial_cls4mro, may_mro_idx4middle_relay_cls, may_middle_relay_cls, key, may_instance, offset4restart_from_middle=offset4restart_from_middle)
    return _tail_of_hasattr_if(predicator, tmay_value, flip)
def _tail_of_hasattr_if(predicator, tmay_value, flip:bool):
    if tmay_value:
        [value] = tmay_value
        return bool(flip) is not bool(predicator(value))
        return bool(flip) ^ bool(predicator(value))
    return False
def hasattr_if__via_cls__apply_descriptor_protocol(predicator, obj, key, /, *, flip:bool):
    cls = type(obj)
    may_instance = obj
    return hasattr_if__as_cls__apply_descriptor_protocol(predicator, cls, key, may_instance, flip=flip)


def is_None(x, /):
    return x is None
def is_not_None(x, /):
    return x is not None
callable
def not_callable(x, /):
    return not callable(x)
def flip_predicator(f, /):
    return lambda x, /: not f(x)

def hasattr_not_None__as_cls__apply_descriptor_protocol(cls, key, may_instance, /):
    return hasattr_if__as_cls__apply_descriptor_protocol(is_not_None, cls, key, may_instance, flip=False)
def hasattr_not_None__via_cls__apply_descriptor_protocol(obj, key, /):
    cls = type(obj)
    may_instance = obj
    return hasattr_not_None__as_cls__apply_descriptor_protocol(cls, key, may_instance)


def hasattr_callable__as_cls__apply_descriptor_protocol(cls, key, may_instance, /):
    return hasattr_if__as_cls__apply_descriptor_protocol(callable, cls, key, may_instance, flip=False)
def hasattr_callable__via_cls__apply_descriptor_protocol(obj, key, /):
    cls = type(obj)
    may_instance = obj
    return hasattr_callable__as_cls__apply_descriptor_protocol(cls, key, may_instance)

assert bool(object())
#assert callable(object.__bool__)
    #AttributeError: type object 'object' has no attribute '__bool__'
assert not hasattr(object, '__bool__')
assert hash(object())
assert hasattr(object, '__hash__')
assert callable(object.__hash__)
assert hasattr_callable__as_cls__apply_descriptor_protocol(object, '__hash__', None)
assert not hasattr_callable__as_cls__apply_descriptor_protocol(object, '__bool__', None)
assert not hasattr_callable__as_cls__apply_descriptor_protocol(object, '__iter__', None)
assert hasattr_callable__via_cls__apply_descriptor_protocol({}, '__len__')

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


