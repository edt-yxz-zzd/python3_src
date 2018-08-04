

__all__ = '''
is_reiterable
to_reiterable
iter_adj2
seq_adj2


is_hashable_type
is_immutable_type
is_reiterable_type
is_collection_type
is_sequence_type
is_container_type
is_immutable_sequence_type
is_immutable_container_type

is_hashable
is_immutable
is_reiterable
is_collection
is_sequence
is_container
is_immutable_sequence
is_immutable_container


to_reiterable
to_collection
to_container
to_sequence
to_any_immutable_sequence
to_known_immutable_sequence
to_subtuple
to_tuple


'''.split()

'''
not export:
    call_if

    ToKnownImmutableContainers
    to_str
    to_bytes
    to_substr
    to_subbytes

    IsTypeXXX
    NotIsTypeXXX
    IsObjXXX
'''

from collections.abc import (Sequence, Container, Iterable, Iterator,
     MutableSequence, Hashable, Collection)

null_iterable = iter(())
_seq_types = (tuple, str, bytes)







def is_hashable_type(cls):
    return issubclass(cls, Hashable)
def is_immutable_type(cls):
    return is_hashable_type(cls)
def is_sequence_type(cls):
    return issubclass(cls, Sequence)
def is_reiterable_type(cls):
    return issubclass(cls, Iterable) and \
           not issubclass(cls, Iterator)
def is_container_type(cls):
    return issubclass(cls, Container) and \
           issubclass(cls, Iterable) and \
           not issubclass(cls, Iterator)
def is_collection_type(cls):
    return issubclass(cls, Collection) and \
           not issubclass(cls, Iterator)

def is_immutable_sequence_type(cls):
    return is_sequence_type(cls) and is_immutable_type(cls) \
            and not issubclass(cls, MutableSequence)
def is_immutable_container_type(cls):
    return is_container_type(cls) and is_immutable_type(cls)






def is_hashable(obj):
    return is_hashable_type(type(obj))
def is_immutable(obj):
    return is_immutable_type(type(obj))

def is_reiterable(obj):
    return is_reiterable_type(type(obj))
def is_collection(obj):
    return is_collection_type(type(obj))
def is_sequence(obj):
    return is_sequence_type(type(obj))
def is_container(obj):
    return is_container_type(type(obj))
def is_immutable_sequence(obj):
    return is_immutable_sequence_type(type(obj))
def is_immutable_container(obj):
    return is_immutable_container_type(type(obj))













def call_if(obj, pred, f):
    return obj if pred(obj) else f(obj)
def to_reiterable(obj, type=tuple):
    'so we can iter many times'
    return call_if(iterable, is_reiterable, type)
def to_container(iterable, type=tuple):
    'so we can iter many times; and "x in c"'
    return call_if(iterable, is_container, type)
def to_collection(iterable, type=tuple):
    'so we can iter many times; and "x in c"; and len(c)'
    return call_if(iterable, is_collection, type)
def to_sequence(iterable, type=tuple):
    '''so we can iter many times;

but not safe if use in generator, since seq may be modified
'''
    return call_if(iterable, is_sequence, type)
def to_any_immutable_sequence(iterable, type=tuple):
    return call_if(iterable, is_immutable_sequence_type, type)
def to_known_immutable_sequence(iterable, types=_seq_types, type=tuple):
    if isinstance(iterable, types):
        return iterable
    return type(iterable)

def to_subtuple(iterable):
    'may use to_any_immutable_seq instead'
    if isinstance(iterable, tuple):
        return iterable
    return tuple(iterable)
def to_tuple(iterable):
    'if want to compare two seq...'
    return to_type(iterable, tuple)
    if type(iterable) is tuple:
        return iterable
    return tuple(iterable)


def to_type(x, T):
    if type(x) is T:
        return x
    return T(x)




def iter_adj2(iterable):
    '''iter_adj2(iterable) =[def]= zip(seq, seq[1:])'''
    it = iter(iterable)
    for fst in it: break
    for snd in it:
        yield fst, snd
        fst = snd
    pass
def seq_adj2(stable_reiterable):
    '''seq_adj2(seq) =[def]= zip(seq, seq[1:])'''
    it = iter(seq)
    next(it)
    return zip(seq, it)















class ToKnownImmutableContainers:
    '''

usage:
    to_tuple = ToKnownImmutableContainers((tuple,))
    to_subtuple = ToKnownImmutableContainers((tuple,), allow_subtype=True)
    to_sympy_Tuple = ToKnownImmutableContainers((Tuple,), from_iterable=lambda it: Tuple(*it))
'''
    def __init__(self, types, from_iterable=None, allow_subtype=False):
        types = tuple(types)
        if not types:
            raise ValueError('not types')
        if not all(map(is_immutable_container_type, types)):
            raise TypeError('not all immutable_container_types')

        if from_iterable is None:
            # assume types[0] has __init__(iterable)
            from_iterable = types[0]

        self.types = types
        self.type_set = frozenset(types)
        self.from_iterable = from_iterable
        self.allow_subtype = bool(allow_subtype)

        default = from_iterable(null_iterable)
    def __call__(self, iterable=()):
        'to known types; cls.from_iterable'
        if type(iterable) in self.type_set:
            return iterable
        if self.allow_subtype and isinstance(iterable, self.types):
            return iterable

        return self.from_iterable(iterable)



#to_tuple = ToKnownImmutableContainers((tuple,))
to_str = ToKnownImmutableContainers((str,))
to_bytes = ToKnownImmutableContainers((bytes,))
#to_subtuple = ToKnownImmutableContainers((tuple,), allow_subtype=True)
to_substr = ToKnownImmutableContainers((str,), allow_subtype=True)
to_subbytes = ToKnownImmutableContainers((bytes,), allow_subtype=True)












class IsTypeXXX:
    def __init__(self, type2bool):
        self.type2bool = type2bool
    def __contains__(self, type):
        return self.type2bool(type)
class NotIsTypeXXX:
    def __init__(self, type2bool):
        self.type2bool = type2bool
    def __contains__(self, type):
        return not self.type2bool(type)


class IsObjXXX:
    def __init__(self, type2bool):
        self.type2bool = type2bool
    def __contains__(self, obj):
        return self.type2bool(type(obj))

def make_IsTypeXXX_IsObjXXX(type2bool):
    return IsTypeXXX(type2bool), IsObjXXX(type2bool)




