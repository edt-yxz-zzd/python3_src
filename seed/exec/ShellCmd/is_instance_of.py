
'''
for types in typing module
incomplete yet
'''

__all__ = '''
    is_instance_of
    '''.split()

import typing
import collections.abc

def _try():
    CommandType = typing.Sequence[str]
    assert CommandType.__class__ is typing.GenericMeta
    assert CommandType.__args__ == (str,)
    assert CommandType.__extra__ is collections.abc.Sequence
    assert CommandType.__name__ == 'Sequence'
    assert CommandType.__qualname__ == 'Sequence'
    assert CommandType.__module__ == 'typing'

    '''
    from pprint import pprint
    pprint(dir(CommandType))
    pprint(list(CommandType.__dict__.keys()))
    for attr in '__args__ __orig_bases__ __origin__ __parameters__ count index'.split():
        obj = getattr(CommandType, attr)
        #rint(f'{attr}={obj!r}')
    '''
_try()

# assert isinstance([''], Sequence[str])
#   TypeError: Parameterized generics cannot be used with class or instance checks

def is_instance_of(
    obj:object
    , Type:typing.Union[None, tuple
                        , typing.GenericMeta, typing.TypingMeta, type
                        ]
    )->bool:
    def this_func__top(obj, Type)->bool:
        if isinstance(Type, tuple):
            types = Type
            return any(this_func__top(obj, tp) for tp in types)
        else:
            return this_func__bottom(obj, Type)
    def this_func__bottom(obj, Type)->bool:
        #rint('is_instance_of')
        #rint(Type, type(Type))
        if Type is None:
            return obj is None
        elif isinstance(Type, typing.GenericMeta):
            TypeConstructor = Type.__origin__
            if TypeConstructor is None:
                raise NotImplementedError

            types = Type.__args__
            tp = Type.__extra__ # collections.abc.Sequence/dict/...
            #rint(TypeConstructor, types, tp)
            if tp is None:
                raise NotImplementedError

            if not isinstance(obj, tp):
                return False
            if TypeConstructor is typing.Sequence or TypeConstructor is typing.List:
                assert tp is collections.abc.Sequence or tp is list
                seq = obj
                [Elem] = types
                return all(this_func__bottom(elem, Elem) for elem in seq)
            elif TypeConstructor is typing.Mapping or TypeConstructor is typing.Dict:
                assert tp is collections.abc.Mapping or tp is dict
                mapping = obj

                [Key, Value] = types
                return all(this_func__bottom(k, Key)
                            and this_func__bottom(v, Value)
                            for k, v in mapping.items())
            elif TypeConstructor is typing.Union:
                raise NotImplementedError

        elif isinstance(Type, typing.TypingMeta):
            raise NotImplementedError

        #elif isinstance(Type, typing.Union): # raise error!
        elif type(Type) is _typeof_Union:
            TypeConstructor = Type.__origin__
            if TypeConstructor is None:
                raise NotImplementedError

            types = Type.__args__
            #rint(TypeConstructor, types)
            return any(this_func__bottom(obj, tp) for tp in types)

        elif isinstance(Type, type):
            return isinstance(obj, Type)
        else:
            raise NotImplementedError
    return this_func__top(obj, Type)

_typeof_Union = type(typing.Union[None, int])

