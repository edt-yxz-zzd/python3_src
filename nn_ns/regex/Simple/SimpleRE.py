
'''
assume all classes defined here are immutable
user should not modify them

'''



__all__ = '''
    DeadRE
    NullRE
    SinglePassRE
    SingleNotRE
    SingleRE
    ConcatenationRE
    AlternationRE
    CountedRepetitionRE
    MoreRepetitionRE

    theDeadRE
    theNullRE
    theSinglePassRE
    mkSingleNotRE
    mkSingleRE
    mkOneOrMoreRE

    mkConcatenationRE__from_iterable
    mkAlternationRE__from_iterable
    mkConcatenationRE
    mkAlternationRE

    mkZeroOrOneRE
    mkZeroOrMoreRE
    mkExactRepetitionRE
    mkCountedRepetitionRE
    mkMoreRepetitionRE
    '''.split()

from itertools import repeat
from .abc import override
from seed.helper.repr_input import repr_helper
from seed.iters.iter_unique_by_eq import iter_unique_by_eq
from seed.tiny import int2cmp
from seed.for_libs.sort_then_unique import sort_then_unique
from seed.for_libs.sorted_ex import sorted_ex
#from functools import cmp_to_key
from seed.seq_tools.seq_index_if import seq_find_if

'''
    namespace NFAs has below attrs:
        (DeadNFA
        ,NullNFA
        ,SingleNFA
        ,ConcatenationNFA
        ,AlternationNFA
        ,OneOrMoreNFA
        )
    example:
    import SimpleNFA as NFAs

'''


'''
since ISimpleRE will import following free function
    so, put them at front
'''
def mkSingleNotRE(terminal_set):
    return SingleNotRE(terminal_set)
def mkSingleRE(terminal_set):
    return SingleRE(terminal_set)
def mkConcatenationRE(*regex_ls):
    return ConcatenationRE(regex_ls)
def mkAlternationRE(*regex_ls):
    return AlternationRE(regex_ls)
def mkMoreRepetitionRE(regex, min):
    return MoreRepetitionRE(regex, min)
def mkZeroOrOneRE(regex):
    return mkCountedRepetitionRE(regex, 0, 1)
def mkZeroOrMoreRE(regex):
    return mkMoreRepetitionRE(regex, 0)
def mkOneOrMoreRE(regex):
    return mkMoreRepetitionRE(regex, 1)
def mkExactRepetitionRE(regex, n):
    return mkCountedRepetitionRE(regex, n, n)
def mkCountedRepetitionRE(regex, may_min, may_max):
    if may_min is None:
        may_min = 0
    if may_max is None:
        m = may_min
        if not 0 <= m: raise ValueError
        return mkMoreRepetitionRE(regex, m)
    else:
        m = may_min
        M = may_max
        if not 0 <= m <= M: raise ValueError
        return CountedRepetitionRE(regex, m, M)
    pass


########## before ISimpleRE

from .ISimpleRE import ISimpleRE



def int2cmp(i):
    if not i:
        return 0
    return -1 if i < 0 else +1
def len_cmp(lhs, rhs):
    d = len(lhs) - len(rhs)
    return int2cmp(d)
def regexes_cmp(lhs_regexes, rhs_regexes, terminal_set_cmp):
    # -> (-1|0|+1)
    # not dictionary order
    r = len_cmp(lhs_regexes, rhs_regexes)
    if r: return r
    for lhs, rhs in zip(lhs_regexes, rhs_regexes):
        r = lhs.simple_regex_cmp(rhs, terminal_set_cmp)
        if not r: continue
        return r
    return 0


class DeadRE(ISimpleRE):
    __slots__ = ()

    @classmethod
    @override
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        return 0
    @classmethod
    @override
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        return 0

    @override
    def does_accept_empty_string(self):
        return False
    @override
    def __eq__(self, other):
        return isinstance(other, __class__)
    @override
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        return theDeadRE
    @override
    def __repr__(self):
        return 'theDeadRE'
    @override
    def to_reverse_regex(self):
        # -> ISimpleRE
        return self
    @override
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        return NFAs.DeadNFA(make_new_astate, may_initial_astate, may_final_astate)
    pass
class NullRE(ISimpleRE):
    __slots__ = ()

    @classmethod
    @override
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        return 1
    @classmethod
    @override
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        return 0

    @override
    def does_accept_empty_string(self):
        return True
    @override
    def __eq__(self, other):
        return isinstance(other, __class__)
    @override
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        return theNullRE
    @override
    def __repr__(self):
        return 'theNullRE'
    @override
    def to_reverse_regex(self):
        # -> ISimpleRE
        return self
    @override
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        return NFAs.NullNFA(make_new_astate, may_initial_astate, may_final_astate)
    pass

class SinglePassRE(ISimpleRE):
    "the '.'; for [^.] see DeadRE"
    __slots__ = ()

    @classmethod
    @override
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        return 2
    @classmethod
    @override
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        return 0

    @override
    def does_accept_empty_string(self):
        return False
    @override
    def __eq__(self, other):
        return isinstance(other, __class__)
    @override
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        return theSinglePassRE
    @override
    def __repr__(self):
        return 'theSinglePassRE'
    @override
    def to_reverse_regex(self):
        # -> ISimpleRE
        return self
    @override
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        return NFAs.SinglePassNFA(make_new_astate, may_initial_astate, may_final_astate)
    pass
class SingleNotRE(ISimpleRE):
    '[^...]'
    __slots__ = 'terminal_set'.split()

    def __init__(self, terminal_set):
        if not hasattr(terminal_set, '__contains__'): raise TypeError
        self.terminal_set = terminal_set


    @classmethod
    @override
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        return 3
    @classmethod
    @override
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        return terminal_set_cmp(self.terminal_set, other.terminal_set)
    @override
    def does_accept_empty_string(self):
        return False
    @override
    def __eq__(self, other):
        return (isinstance(other, __class__)
            and self.terminal_set == other.terminal_set)
    @override
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        if is_terminal_block_set:
            if not self.terminal_set:
                return theSinglePassRE
            elif self.terminal_set.is_whole_set():
                return theDeadRE
        return self
        return __class__(self.terminal_set)
    @override
    def __repr__(self):
        return repr_helper(self, self.terminal_set)
    @override
    def to_reverse_regex(self):
        # -> ISimpleRE
        return self
        return __class__(self.terminal_set)
    @override
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        return NFAs.SingleNotNFA(make_new_astate
                    , may_initial_astate, may_final_astate
                    , self.terminal_set)
    pass

class SingleRE(ISimpleRE):
    '[[:digit:]...]'
    __slots__ = 'terminal_set'.split()

    def __init__(self, terminal_set):
        if not hasattr(terminal_set, '__contains__'): raise TypeError
        self.terminal_set = terminal_set


    @classmethod
    @override
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        return 4
    @classmethod
    @override
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        return terminal_set_cmp(self.terminal_set, other.terminal_set)
    @override
    def does_accept_empty_string(self):
        return False
    @override
    def __eq__(self, other):
        return (isinstance(other, __class__)
            and self.terminal_set == other.terminal_set)
    @override
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        if is_terminal_block_set:
            if not self.terminal_set:
                return theDeadRE
            elif self.terminal_set.is_whole_set():
                return theSinglePassRE
        return self
        return __class__(self.terminal_set)
    @override
    def __repr__(self):
        return repr_helper(self, self.terminal_set)
    @override
    def to_reverse_regex(self):
        # -> ISimpleRE
        return self
        return __class__(self.terminal_set)
    @override
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        return NFAs.SingleNFA(make_new_astate
                    , may_initial_astate, may_final_astate
                    , self.terminal_set)
    pass
class ConcatenationRE(ISimpleRE):
    __slots__ = 'regexes'.split()

    def __init__(self, regexes):
        self.regexes = tuple(regexes)


    @classmethod
    @override
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        return 5
    @classmethod
    @override
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        return regexes_cmp(self.regexes, other.regexes, terminal_set_cmp)

    @override
    def does_accept_empty_string(self):
        return all(r.does_accept_empty_string() for r in self.regexes)
    @override
    def __eq__(self, other):
        return (isinstance(other, __class__)
            and self.regexes == other.regexes)
    @override
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        is_terminal_block_set = bool(is_terminal_block_set)
        regexes = []
        stack = list(reversed(self.regexes))
        while stack:
            regex = stack.pop()
            if isinstance(regex, __class__):
                stack.extend(reversed(regex.regexes))
            else:
                regexes.append(regex)
        regexes = (regex.simplify(terminal_set_cmp, is_terminal_block_set) for regex in regexes)
        regexes = (r for r in regexes if not isinstance(r, NullRE))
        other = __class__(regexes)

        regexes = other.regexes
        if not regexes:
            return theNullRE
        elif len(regexes) == 1:
            [regex] = regexes
            return regex
        elif any(isinstance(r, DeadRE) for r in regexes):
            return theDeadRE
        return other



    @override
    def __repr__(self):
        return repr_helper(self, list(self.regexes))
    @override
    def to_reverse_regex(self):
        # -> ISimpleRE
        return __class__(r.to_reverse_regex() for r in reversed(self.regexes))
    @override
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        regexes = self.regexes
        L = len(regexes)
        if not L:
            return NFAs.NullNFA(make_new_astate, may_initial_astate, may_final_astate)
        elif L == 1:
            [regex] = regexes
            return regex._mkSimpleNFA_(
                NFAs, make_new_astate, may_initial_astate, may_final_astate)
        headRE = regexes[0]
        headNFA = headRE._mkSimpleNFA_(
                NFAs, make_new_astate, may_initial_astate, None)
        lNFA = headNFA
        for regexR in regexes[1:-1]:
            lNFA = NFAs.ConcatenationNFA(NFAs, make_new_astate, None, lNFA, regexR)
        regexR = regexes[-1]
        lNFA = NFAs.ConcatenationNFA(NFAs, make_new_astate
                , may_final_astate, lNFA, regexR)
        return lNFA
    pass
class AlternationRE(ISimpleRE):
    __slots__ = 'regexes'.split()
    def __init__(self, regexes):
        self.regexes = tuple(regexes)


    @classmethod
    @override
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        return 6
    @classmethod
    @override
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        return regexes_cmp(self.regexes, other.regexes, terminal_set_cmp)
    @override
    def does_accept_empty_string(self):
        return any(r.does_accept_empty_string() for r in self.regexes)
    @override
    def __eq__(self, other):
        # donot consider unorder
        return (isinstance(other, __class__)
            and self.regexes == other.regexes)

    @override
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        is_terminal_block_set = bool(is_terminal_block_set)
        if is_terminal_block_set and terminal_set_cmp is None:
            def terminal_set_cmp(a, b):
                # terminal_set is block_set
                return a.block_set_cmp(b)

        regexes = []
        stack = list(reversed(self.regexes))
        while stack:
            regex = stack.pop()
            if isinstance(regex, __class__):
                stack.extend(reversed(regex.regexes))
            else:
                regexes.append(regex)
        regexes = (regex.simplify(terminal_set_cmp, is_terminal_block_set)
                    for regex in regexes)
        regexes = [r for r in regexes if not isinstance(r, DeadRE)]

        exist_pass = theSinglePassRE in regexes
        if exist_pass:
            regexes = [r for r in regexes if not isinstance(r, AllSingleREs)]
            regexes.append(theSinglePassRE)

        if terminal_set_cmp is None:
            # O(n*n)
            #regexes = sorted(regexes, key=lambda r: type(r).order_of_SimpleRE())
            def null_terminal_set_cmp(a, b):
                # terminal_set is block_set
                return 0 # always eq
            def cmp(a, b):
                # regex
                return a.simple_regex_cmp(b, null_terminal_set_cmp)
            regexes = sorted_ex(regexes, cmp=cmp)
            regexes = iter_unique_by_eq(regexes)
        else:
            # O(n*log(n))
            def cmp(a, b):
                return a.simple_regex_cmp(b, terminal_set_cmp)
            regexes = sort_then_unique(regexes, cmp=cmp)
        while not exist_pass and is_terminal_block_set:
            # union all pos terminal_sets - neg terminal_sets
            # ???block set???
            regexes = [*regexes]
            pred = lambda r: isinstance(r, AllSingleREs)
            npred = lambda r: not isinstance(r, AllSingleREs)
            begin, may_regex = seq_find_if(regexes, pred)
            if begin < 0: break
            first_regex = may_regex
            out_terminal_set = first_regex.terminal_set.self_make_empty_block_set()

            end, may_regex = seq_find_if(regexes, npred, begin+1)
            if end < 0:
                end = len(regexes)

            out_terminal_set
            for regex in regexes[begin:end]:
                if isinstance(regex, SingleRE):
                    out_terminal_set |= regex.terminal_set
                elif isinstance(regex, SingleNotRE):
                    out_terminal_set -= regex.terminal_set
                else:
                    raise logic-error
            regex = SingleRE(out_terminal_set)
            regexes[begin:end] = [regex]
            break

        other = __class__(regexes)

        regexes = other.regexes
        if not regexes:
            return theDeadRE
        elif len(regexes) == 1:
            [regex] = regexes
            return regex
        return other

    @override
    def __repr__(self):
        return repr_helper(self, list(self.regexes))
    @override
    def to_reverse_regex(self):
        # -> ISimpleRE
        return __class__(r.to_reverse_regex() for r in self.regexes)
    @override
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        regexes = self.regexes
        L = len(regexes)
        if not L:
            return NFAs.DeadNFA(make_new_astate, may_initial_astate, may_final_astate)
        elif L == 1:
            [regex] = regexes
            return regex._mkSimpleNFA_(
                NFAs, make_new_astate, may_initial_astate, may_final_astate)
        headRE = regexes[0]
        headNFA = headRE._mkSimpleNFA_(
                NFAs, make_new_astate, may_initial_astate, may_final_astate)
        uNFA = headNFA
        for regexD in regexes[1:]:
            uNFA = NFAs.AlternationNFA(NFAs, make_new_astate, uNFA, regexD)
        return uNFA
    pass

class CountedRepetitionRE(ISimpleRE):
    __slots__ = 'regex min max'.split()
    def __init__(self, regex, min, max):
        if max is None or min is None: raise TypeError
        if not (0 <= min <= max): raise ValueError
        assert isinstance(max, int)

        self.regex = regex
        self.min = min
        self.max = max


    @classmethod
    @override
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        return 7
    @classmethod
    @override
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        if self.min != other.min:
            return int2cmp(self.min, other.min)
        if self.max != other.max:
            return int2cmp(self.max, other.max)
        return self.regex.simple_regex_cmp(other.regex, terminal_set_cmp)
    @override
    def does_accept_empty_string(self):
        return self.min == 0 or self.regex.does_accept_empty_string()
    @override
    def __eq__(self, other):
        return (isinstance(other, __class__)
            and self.min == other.min
            and self.max == other.max
            and self.regex == other.regex
            )
    @override
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        regex = self.regex.simplify(terminal_set_cmp, is_terminal_block_set)
        if isinstance(regex, DeadRE):
            if min == 0:
                return theNullRE
            return theDeadRE
        elif isinstance(regex, NullRE):
            return theNullRE
        return __class__(regex, self.min, self.max)
    @override
    def __repr__(self):
        return repr_helper(self, self.regex, self.min, self.max)
    @override
    def to_reverse_regex(self):
        # -> ISimpleRE
        return __class__(self.regex.to_reverse_regex(), self.min, self.max)
    @override
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        # e{m,M} == e{m} e?{M-m}
        regex = self.regex
        m = self.min
        M = self.max

        assert m >= 0
        regexes = (regex,)*m
        if m < M:
            regex_optional = mkAlternationRE(regex, theNullRE) # (regex?)
            regexes += (regex_optional,)*(M-m)
        return ConcatenationRE(regexes)._mkSimpleNFA_(
            NFAs, make_new_astate, may_initial_astate, may_final_astate)

    pass
class MoreRepetitionRE(ISimpleRE):
    __slots__ = 'regex min'.split()

    def __init__(self, regex, min):
        if not (0 <= min): raise ValueError
        self.regex = regex
        self.min = min


    @classmethod
    @override
    def order_of_SimpleRE(cls):
        # -> UInt, should diff with other cls
        return 8
    @classmethod
    @override
    def __re_cmp__(cls, self, other, terminal_set_cmp):
        # -> (-1|0|+1)
        assert type(self) is cls is type(other)
        if self.min != other.min:
            return int2cmp(self.min, other.min)
        return self.regex.simple_regex_cmp(other.regex, terminal_set_cmp)
    @override
    def does_accept_empty_string(self):
        return self.min == 0 or self.regex.does_accept_empty_string()
    @override
    def __eq__(self, other):
        return (isinstance(other, __class__)
            and self.min == other.min
            and self.regex == other.regex
            )
    @override
    def simplify(self, terminal_set_cmp:[None, 'cmp'], is_terminal_block_set:bool):
        regex = self.regex.simplify(terminal_set_cmp, is_terminal_block_set)
        if isinstance(regex, DeadRE):
            if min == 0:
                return theNullRE
            return theDeadRE
        elif isinstance(regex, NullRE):
            return theNullRE
        return __class__(regex, self.min)
    @override
    def __repr__(self):
        return repr_helper(self, self.regex, self.min)
    @override
    def to_reverse_regex(self):
        # -> ISimpleRE
        return __class__(self.regex.to_reverse_regex(), self.min)
    @override
    def _mkSimpleNFA_(self, NFAs, make_new_astate, may_initial_astate, may_final_astate):
        # e{m,M} == e{m} e?{M-m}
        regex = self.regex
        m = self.min

        assert m >= 0

        if m == 1:
            return NFAs.OneOrMoreNFA(NFAs, make_new_astate
                    , may_initial_astate, may_final_astate, regex)
        elif m == 0:
            # e* = (e+)?
            re_star = mkAlternationRE(mkOneOrMoreRE(regex), theNullRE)
            return re_star._mkSimpleNFA_(
                NFAs, make_new_astate, may_initial_astate, may_final_astate)

        elif m >= 2:
            prefixRE = mkExactRepetitionRE(regex, m-1)
            suffixRE = mkOneOrMoreRE(regex)
            r = mkConcatenationRE(prefixRE, suffixRE)
            return r._mkSimpleNFA_(
                NFAs, make_new_astate, may_initial_astate, may_final_astate)

    pass


AllSingleREs = (SingleNotRE, SingleRE, SinglePassRE)
theDeadRE = DeadRE()
theNullRE = NullRE()
theSinglePassRE = SinglePassRE()

mkConcatenationRE__from_iterable = ConcatenationRE
mkAlternationRE__from_iterable = AlternationRE

mkAlternationRE.from_iterable = mkAlternationRE__from_iterable
mkConcatenationRE.from_iterable = mkConcatenationRE__from_iterable


'''
from . import ISimpleRE as out
out.mkAlternationRE = mkAlternationRE
out.mkConcatenationRE = mkConcatenationRE
out.mkZeroOrMoreRE = mkZeroOrMoreRE
out.mkOneOrMoreRE = mkOneOrMoreRE
out.mkCountedRepetitionRE = mkCountedRepetitionRE
out.mkExactRepetitionRE = mkExactRepetitionRE
del out
'''








################################






