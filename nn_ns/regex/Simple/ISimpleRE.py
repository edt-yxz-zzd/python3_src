
__all__ = '''
    ISimpleRE
    '''.split()

from .abc import ABC, abstractmethod, not_implemented, override


class ISimpleRE(ABC):
    '''
simple regex
simple regular expression

terminal_set
    .__contains__
    but not require .__bool__
    why?
        terminal_set may be implement by a predicator
        we donot know whether it contains any value

SimpleRegex terminal_set
    = DeadRE
    | NullRE
    | SingleRE terminal_set
    | ConcatenationRE
            [(SimpleRegex terminal_set)]
    | AlternationRE
            [(SimpleRegex terminal_set)]
    | CountedRepetitionRE
            (SimpleRegex terminal_set) (min::UInt) (max::UInt)
    | MoreRepetitionRE
            (SimpleRegex terminal_set) (min::UInt)

SimpleNFA terminal_set
    # Thompson's construction
    = DeadNFA initial_astate final_astate
    | NullNFA initial_astate final_astate
    | SinglePassNFA initial_astate final_astate
    | SingleNotNFA initial_astate final_astate
            terminal_set
    | SingleNFA initial_astate final_astate
            terminal_set
    | ConcatenationNFA initial_astate final_astate
            (SingleNFA terminal_set) (SingleNFA terminal_set)
    | AlternationNFA initial_astate final_astate
            (SingleNFA terminal_set) (SingleNFA terminal_set)
    | OneOrMoreNFA initial_astate final_astate
            (SingleNFA terminal_set)
'''
    __slots__ = ()

    def toSimpleNFA(self):
        return mkSimpleNFA(self)

    @not_implemented
    def does_accept_empty_string(self):
        # -> bool
        ...
    @not_implemented
    def to_reverse_regex(self):
        # -> ISimpleRE
        ...
    @not_implemented
    def __repr__(self):
        ...
    @not_implemented
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        return not (self == other)
    @not_implemented
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        # -> ISimpleRE
        # if terminal_set_cmp is None:
        #   if is_terminal_block_set: then use block_set_cmp
        #   else: not sort them, using an O(n^2) unique by eq algo
        #
        ...
    @classmethod
    @not_implemented
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        ...
    @classmethod
    @not_implemented
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        ...



    @not_implemented
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        '''
called by SimpleNFA.mkSimpleNFA only
    user should not call it

output:
    nfa :: ISimpleNFA
input:
  make_new_astate :: MakeNewAState
  may_initial_astate, may_final_astate :: None | UInt
  NFAs :: namespace
    namespace NFAs has below attrs:
        (DeadNFA
        ,NullNFA
        ,SinglePassNFA
        ,SingleNotNFA
        ,SingleNFA
        ,ConcatenationNFA
        ,AlternationNFA
        ,OneOrMoreNFA
        )
    example:
    import SimpleNFA as NFAs
        '''
        ...
    def __getitem__(self, idx_or_slice):
        if isinstance(idx_or_slice, slice):
            sl = idx_or_slice
            if sl.step is not None: raise TypeError('supper None step only')
            return mkCountedRepetitionRE(self, sl.start, sl.stop)
        elif isinstance(idx_or_slice, int):
            idx = idx_or_slice
            return mkExactRepetitionRE(self, idx)
        else:
            raise TypeError
    '''
    to_reverse_regex or reverse the final astate?
    def __inv__(self):
        return self.to_reverse_regex()
    '''
    def __pos__(self):
        return mkOneOrMoreRE(self)
    def __neg__(self):
        return mkZeroOrMoreRE(self)
    def __rshift__(self, other):
        return mkConcatenationRE(self, other)
    def __or__(self, other):
        return mkAlternationRE(self, other)
    pass

    def before__le(self, other, terminal_set_cmp):
        return self.simple_re_cmp(other, terminal_set_cmp) <= 0
    def before__lt(self, other, terminal_set_cmp):
        return self.simple_re_cmp(other, terminal_set_cmp) < 0
    def simple_regex_cmp(self, other, terminal_set_cmp):
        # -> -1/0/+1
        # terminal_set_cmp :: terminal_set -> terminal_set -> (-1|0|+1)
        assert isinstance(other, __class__)
        sT = type(self)
        oT = type(other)
        if sT is oT:
            return type(self).__re_cmp__(self, other, terminal_set_cmp)
        d = sT.order_of_SimpleRE() - oT.order_of_SimpleRE()
        if not d: raise TypeError(f'{sT} and {oT} has same order_of_SimpleRE')
        return -1 if d < 0 else +1


from .mkSimpleNFA import mkSimpleNFA
from .SimpleRE import \
    (mkAlternationRE
    ,mkConcatenationRE
    ,mkZeroOrMoreRE
    ,mkOneOrMoreRE
    ,mkCountedRepetitionRE
    ,mkExactRepetitionRE
    )


