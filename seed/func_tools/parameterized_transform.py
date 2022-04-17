r'''
e ../../python3_src/seed/func_tools/parameterized_transform.py

f<g, h>(a) -> b
f(g, h) :: a -> b

scenarios:
    fmap4dict(echo, fmap4list(int))
        :: may env4recur -> {k:[a]} -> {k:[int]}
    repr4dict(...)

#'''


from abc import ABC, abstractmethod
from seed.types.FrozenDict import FrozenDict
from seed.helper.repr_input import repr_helper

class IPureParameterized(ABC, tuple):
    __slots__ = ()
    @classmethod
    @abstractmethod
    def check_args4inlt(cls, /, *args4init, **kwargs4init):
        pass
    @classmethod
    def transform_args4human_to_args4init(cls, /, *args4human, **kwargs4human):
        '-> (args4init, kwargs4init)'
        (args4init, kwargs4init) = (args4human, kwargs4human)
        return (args4init, kwargs4init)
    @classmethod
    def mk(cls, /, *args4human, **kwargs4human):
        (args4init, kwargs4init) = cls.transform_args4human_to_args4init(*args4human, **kwargs4human)
        return __class__.__new__(args4init, kwargs4init)
    def __new__(cls, /, *args4init, **kwargs4init):
        'final_method #SHOULD NOT BE overrided'
        cls.check_args4inlt(*args4init, **kwargs4init)
        return tuple.__new__(cls, [args4init, FrozenDict(kwargs4init)])

    def __repr__(sf, /):
        args4init, kwargs4init = tuple.__iter__(sf)
        return repr_helper(sf, *args4init, **kwargs4init)
    __str__ = __repr__
    __bool__ = None
    __len__ = None
    __iter__ = None
    __getitem__ = None
    def __ne__(sf, ot, /):
        return not sf == ot
    def __eq__(sf, ot, /):
        if sf is ot: return True
        if not type(sf) is type(ot): return False
        len = tuple.__len__
        if not len(sf) == len(ot): return False
        eq = tuple.__eq__
        return eq(sf, ot)
    def __hash__(sf, /):
        cls = type(sf)
        L = tuple.__len__(sf)
        h = tuple.__hash__(sf)
        return hash((cls, L, h))


class IParameterizedTransform(IPureParameterized):
    __slots__ = ()
    @classmethod
    @abstractmethod
    def ___calc_type_description_of_IO___(cls, /, *args4init, **kwargs4init):
        '-> (scheme_parameter_list, type_description<input>, type_description<output>) # eg: [forall a, b. Either a b -> Maybe b]'
    @abstractmethod
    def ___call___(sf, x, /):
        'x -> y'

    def __call__(sf, x, /):
        'x -> y'
        return type(sf).___call___(sf, x)






