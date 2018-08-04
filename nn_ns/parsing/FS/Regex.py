

'''
RegexAbstractSyntax a = ReConcat [RegexAbstractSyntax a]
                      | ReAlter  (Set (RegexAbstractSyntax a))
                      | ReStar (RegexAbstractSyntax a)
                      | ReComplement (RegexAbstractSyntax a)
                      | ReSymbol a
'''


__all__ = '''
    ReConcat
    ReAlter
    ReStar
    ReComplement
    ReSymbol
    
    HandedStar
    HandedNot
    handed2re
    re2ndfa
    re2dfa
'''.split()


from itertools import repeat
from .Maybe import just, unjust, nothing
from .FA_construct import transition_rules2ndfa
from .FA_transform import ndfa2dfa, clean_dfa
from .FA_FSM import SimpleDFA2FSM

from sand.types.Newtype import Newtype
class RegexAbstractSyntax(Newtype):pass


is_re_obj = lambda e: isinstance(e, all_re_types)
is_re_objs = lambda ls: all(map(is_re_obj, ls))
class ReConcat(RegexAbstractSyntax):
    def __init__(self, exprs):
        super().__init__(tuple(exprs))
        assert is_re_objs(self.seq)

    @property
    def seq(self):
        return self.unbox()

class ReAlter(RegexAbstractSyntax):
    def __init__(self, exprs):
        super().__init__(frozenset(exprs))
        assert is_re_objs(self.alts)

    @property
    def alts(self):
        return self.unbox()

class ReSymbol(RegexAbstractSyntax):
    def __init__(self, x):
        super().__init__(x)

    @property
    def symbol(self):
        return self.unbox()


class _ReRefOne(RegexAbstractSyntax):
    def __init__(self, re):
        super().__init__(re)
        assert is_re_obj(self.ref)

    @property
    def ref(self):
        return self.unbox()
class ReStar(_ReRefOne): pass
class ReComplement(_ReRefOne): pass

all_re_types = (ReConcat, ReAlter, ReSymbol, ReStar, ReComplement)

class HandedStar(Newtype):
    def __init__(self, x):
        super().__init__(x)
class HandedNot(Newtype):
    def __init__(self, x):
        super().__init__(x)



def handed2re(handed):
    ''':: Handed a => RegexAbstractSyntax b ????????

class Handed a
instance Handed a => Handed (tuple a)
instance Handed a => Handed (frozenset a)
instance Handed a => Handed (HandedStar a)
instance Handed a => Handed (HandedNot a)
instance Handed (RegexAbstractSyntax a)
instance Immutable a => Handed a
'''
    T = type(handed)
    if T == tuple:
        return ReConcat(map(handed2re, handed))
    elif T == frozenset:
        return ReAlter(map(handed2re, handed))
    elif T == HandedStar:
        return ReStar(handed2re(handed.unbox()))
    elif T == HandedNot:
        return ReComplement(handed2re(handed.unbox()))
    elif is_re_obj(handed):
        return handed
    else:
        return ReSymbol(handed)


def make_re__Star_ab_b_abN(n, dot=None):
    'regex = "[ab]*b[ab]{n}"'

    if dot is None:
        dot = 'ab'

    ab = frozenset(dot)
    handed = HandedStar(ab), 'b', (ab,)*n
    re = handed2re(handed)
    return re

def test__make_re__Star_ab_b_abN(rng, *, dot=None):
    return list(map(make_re__Star_ab_b_abN, rng, repeat(dot)))

    for n in rng:
        re = make_re__Star_ab_b_abN(n, dot=dot)
        print(n, re)

assert test__make_re__Star_ab_b_abN(range(4)) == [ReConcat((ReStar(ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')}))), ReSymbol('b'), ReConcat(()))), ReConcat((ReStar(ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')}))), ReSymbol('b'), ReConcat((ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')})),)))), ReConcat((ReStar(ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')}))), ReSymbol('b'), ReConcat((ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')})), ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')})))))), ReConcat((ReStar(ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')}))), ReSymbol('b'), ReConcat((ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')})), ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')})), ReAlter(frozenset({ReSymbol('a'), ReSymbol('b')}))))))]
#print(test__make_re__Star_ab_b_abN(range(2), dot='abc'))


def re2ndfa(re, begin = 0):
    return transition_rules2ndfa(re2rules(re, begin), [begin])
def re2dfa(re):
    dfa = ndfa2dfa(re2ndfa(re))
    return clean_dfa(dfa)


def re2rules(re, begin):
    ''':: Re x -> Iter Rule where Rule = (Integer, Maybe (Maybe x, Integer))
begin - the only start symbol
'''
    rules, end = re2rules_end(re, begin)
    yield (end, nothing)
    for q0, maybe_symbol, qt in rules:
        yield q0, just((maybe_symbol, qt))
def re2rules_end(re, begin):
    ''':: Re x -> Integer -> ([Rule], Integer) where Rule = (Integer, Maybe x, Integer)
begin - the only start symbol
end - the only final symbol # so, no rules "A = ;"
'''
    T = type(re)

    # bug: if begin0 == begin, goto: (ref[0].end, nothing)-> begin -> begin0!!
    # ==>> begin0 < begin <= end < end0
    begin0 = begin
    begin = end0 = begin0 + 1
    ls = []
    if T == ReConcat:
        ls.append((begin0, nothing, begin))
        for e in re.seq:
            assert begin == end0
            rules, end = re2rules_end(e, begin)
            ls.extend(rules)
            
            begin = end0 = end + 1
            ls.append((end, nothing, end0))
        return ls, end0
    elif T == ReAlter:
        ends = []
        begins = []
        
        for e in re.alts:
            assert begin == end0
            rules, end = re2rules_end(e, begin)
            ls.extend(rules)

            begins.append(begin)
            ends.append(end)
            begin = end0 = end + 1
            # bug: ls.append((end, nothing, end0))

        ls.extend((begin0, nothing, begin) for begin in begins)
        ls.extend((end, nothing, end0) for end in ends)

        # NOTE: if no alts, then ls = [] i.e. no rules connect begin0 and end0
        return ls, end0
    elif T == ReStar:
        assert begin == end0
        e = re.ref
        rules, end = re2rules_end(e, begin)
        end0 = end + 1
        rules.append((begin0, nothing, begin))
        rules.append((end, nothing, end0))
        
        rules.append((begin0, nothing, end0)) # for null
        rules.append((end, nothing, begin))   # for recur
        return rules, end0
    elif T == ReComplement:
        raise NotImplementedError
    elif T == ReSymbol:
        rule = begin0, just(re.symbol), end0
        return [rule], end0
    
    else:
        print(T)
        raise logic-error
    pass

    

    
def test__re2ndfa(rng, *, dot=None):
    re_ls = test__make_re__Star_ab_b_abN(rng, dot=dot)
    for e in re_ls:
        yield re2ndfa(e)
def test__re2dfa(rng, *, dot=None):
    re_ls = test__make_re__Star_ab_b_abN(rng, dot=dot)
    for e in re_ls:
        yield re2dfa(e)



def test__ndfa2dfa(rng, *, dot=None):
    for ndfa in test__re2ndfa(rng, dot=dot):
        yield ndfa2dfa(ndfa)

if 0:

    from pprint import pprint
    e = make_re__Star_ab_b_abN(1, 'ab')
    assert e == ReConcat((
        ReStar(
            ReAlter(frozenset({
                ReSymbol('a'),
                ReSymbol('b')})
                    )
            ),
        ReSymbol('b'),
        ReConcat((
            ReAlter(frozenset({
                ReSymbol('a'),
                ReSymbol('b')})),
            ))
        )) 
    dfa = re2dfa(e)
    pprint(e)
    pprint(re2ndfa(e).transition)
    pprint(dfa)
    fsm = SimpleDFA2FSM(dfa)
    assert not fsm.accepted('bab')



def __show(n, dots, show=True):
    rng = list(range(n))
    for dot in dots:
        dfas = list(test__re2dfa(rng, dot=dot)) # bug: forgot clean_dfa; now clean in re2dfa
        #print(r)
        if show:
            #print(list(dfa.calc_num_states() for dfa in dfas))
            #print(dfas)
            ls = (list(dfa.calc_num_states() for dfa in dfas))
            assert ls == [2**(i+1) for i in rng]
__show(3, 'ab abc'.split(), show=True)
'''
__show(6, 'ab abc abcd abcde abcdef'.split(), show=True)

[2, 4, 8, 15, 27, 48]
[2, 5, 11, 23, 46, 90]
[2, 6, 14, 30, 61, 122]
[2, 7, 17, 37, 76, 153]
[2, 8, 20, 44, 91, 184]
#'''



    
