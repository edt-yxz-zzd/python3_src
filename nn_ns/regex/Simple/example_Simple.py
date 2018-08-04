
r'''
example:
>>> from .SimpleRE import \
... (DeadRE
... ,NullRE
... ,SinglePassRE
... ,SingleNotRE
... ,SingleRE
... ,ConcatenationRE
... ,AlternationRE
... ,CountedRepetitionRE
... ,MoreRepetitionRE
... ,theDeadRE
... ,theNullRE
... ,theSinglePassRE
... ,mkSingleNotRE
... ,mkSingleRE
... ,mkOneOrMoreRE
... ,mkConcatenationRE__from_iterable
... ,mkAlternationRE__from_iterable
... ,mkConcatenationRE
... ,mkAlternationRE
... ,mkZeroOrOneRE
... ,mkZeroOrMoreRE
... ,mkExactRepetitionRE
... ,mkCountedRepetitionRE
... ,mkMoreRepetitionRE
... )

>>> from .mkSimpleNFA import mkSimpleNFA
>>> from .ISimpleNFA import ISimpleNFA
>>> ops = ISimpleNFA.NFA_ops


>>> reB, reS, reA, reX = map(mkSingleRE, 'BSAX')
>>> re_SA_BSAX = (+reS >> +reA) | (+reB >> +reS >> +reA >> +reX)
>>> nfa_SA_BSAX = re_SA_BSAX.toSimpleNFA()
>>> ops.search_leftmost_substring(nfa_SA_BSAX, 'SA', True, False)
(0, 2)
>>> ops.search_leftmost_substring(nfa_SA_BSAX, 'SA', False, True)
(0, 2)
>>> ops.search_leftmost_substring(nfa_SA_BSAX, 'BSA', False, True)
(1, 3)
>>> ops.search_leftmost_substring(nfa_SA_BSAX, 'SSA', False, True)
(1, 3)


>>> str_BSAX = 'BBBSSSAAAXXX'
>>> ops.search_leftmost_substring_ex_ex(nfa_SA_BSAX, 0, zip(str_BSAX, range(1, len(str_BSAX))), False, True)
('LeftMostEnd_NonGreedyBegin', ((5, 5), (7, 7)), (7, 7))



>>> mk = mkSimpleNFA
>>> show = lambda nfa: nfa.show(repr)
>>> show_detail = lambda nfa: nfa.show_detail(repr)
>>> mk_and_show = lambda regex: show(mk(regex))
>>> mk_and_show(theNullRE)
'NullNFA'

>>> re_starE = mkZeroOrMoreRE(SingleRE('E')) # E*
>>> re_plus2E = mkMoreRepetitionRE(SingleRE('E'), 2) # E{2,}
>>> re_starE.does_accept_empty_string()
True
>>> re_plus2E.does_accept_empty_string()
False



>>> nfa_starE = mk(re_starE)
>>> nfa_plus2E = mk(re_plus2E)
>>> show(nfa_starE)
"<SingleNFA('E')+ | NullNFA>"
>>> show(nfa_plus2E)
"[SingleNFA('E') ++ SingleNFA('E')+]"
>>> show_detail(nfa_plus2E)
"{>-0}-> [{>-0}-> SingleNFA('E') ->{1->} ++ {>-1}-> {>-2}-> SingleNFA('E') ->{3->}+ ->{4->}] ->{4->}"

>>> show(re_starE.to_reverse_regex().toSimpleNFA())
"<SingleNFA('E')+ | NullNFA>"
>>> show(re_plus2E.to_reverse_regex().toSimpleNFA())
"[SingleNFA('E') ++ SingleNFA('E')+]"
>>> reE = SingleRE('E')
>>> reNotE = SingleNotRE('E')
>>> r = (reE >> +reE >> -reNotE) | theNullRE | theDeadRE | theSinglePassRE
>>> show(r.toSimpleNFA())
"<<<[[SingleNFA('E') ++ SingleNFA('E')+] ++ <SingleNotNFA('E')+ | NullNFA>] | NullNFA> | DeadNFA> | SinglePassNFA>"
>>> show(r.to_reverse_regex().toSimpleNFA())
"<<<[<SingleNotNFA('E')+ | NullNFA> ++ [SingleNFA('E')+ ++ SingleNFA('E')]] | NullNFA> | DeadNFA> | SinglePassNFA>"
>>> r
AlternationRE([AlternationRE([AlternationRE([ConcatenationRE([ConcatenationRE([SingleRE('E'), MoreRepetitionRE(SingleRE('E'), 1)]), MoreRepetitionRE(SingleNotRE('E'), 0)]), theNullRE]), theDeadRE]), theSinglePassRE])
>>> r.to_reverse_regex()
AlternationRE([AlternationRE([AlternationRE([ConcatenationRE([MoreRepetitionRE(SingleNotRE('E'), 0), ConcatenationRE([MoreRepetitionRE(SingleRE('E'), 1), SingleRE('E')])]), theNullRE]), theDeadRE]), theSinglePassRE])
>>> r.simplify(None, False)
AlternationRE([theNullRE, theSinglePassRE, ConcatenationRE([SingleRE('E'), MoreRepetitionRE(SingleRE('E'), 1), MoreRepetitionRE(SingleNotRE('E'), 0)])])
>>> r.simplify(None, False).to_reverse_regex()
AlternationRE([theNullRE, theSinglePassRE, ConcatenationRE([MoreRepetitionRE(SingleNotRE('E'), 0), MoreRepetitionRE(SingleRE('E'), 1), SingleRE('E')])])
>>> r.to_reverse_regex().simplify(None, False) == r.simplify(None, False).to_reverse_regex()
True



>>> ops = nfa_starE.get_NFA_ops()
>>> ops.does_accept(nfa_starE, '')
True
>>> ops.does_accept(nfa_starE, 'E')
True
>>> ops.does_accept(nfa_starE, 'EE')
True
>>> ops.does_accept(nfa_starE, 'ABC')
False

>>> ops.does_accept(nfa_plus2E, '')
False
>>> ops.does_accept(nfa_plus2E, 'E')
False
>>> ops.does_accept(nfa_plus2E, 'EE')
True
>>> ops.does_accept(nfa_plus2E, 'ABC')
False



>>> ops.does_accept_ex(nfa_starE, None, [])
('SuccessUntilEnd', True, (0, None))
>>> ops.does_accept_ex(nfa_starE, '0', zip('ABC', '123'))
('FailOnGlobalDead', False, (1, '1'))
>>> ops.does_accept_ex(nfa_plus2E, '0', zip('EE', '12'))
('SuccessUntilEnd', True, (2, '2'))



>>> ops.search_prefix(nfa_starE, 'ABC', True)
0
>>> ops.search_prefix(nfa_starE, 'EEEABC', True)
3
>>> ops.search_prefix(nfa_starE, 'EEEABC', False)
0

>>> ops.search_prefix(nfa_plus2E, 'ABC', True) is None
True
>>> ops.search_prefix(nfa_plus2E, 'EEEABC', True)
3
>>> ops.search_prefix(nfa_plus2E, 'EEEABC', False)
2






>>> ops.search_leftmost_substring(nfa_starE, 'ABCEEE', True, False)
(0, 0)
>>> ops.search_leftmost_substring(nfa_starE, 'ABCEEE', True, True)
(0, 0)
>>> ops.search_leftmost_substring(nfa_starE, 'ABCEEE', False, False)
(0, 0)
>>> ops.search_leftmost_substring(nfa_starE, 'ABCEEE', False, True)
(0, 0)



>>> ops.search_leftmost_substring(nfa_plus2E, 'ABCEEE', True, False)
(3, 6)
>>> ops.search_leftmost_substring(nfa_plus2E, 'ABCEEE', True, True)
(3, 5)
>>> ops.search_leftmost_substring(nfa_plus2E, 'ABCEEE', False, False)
(3, 5)
>>> ops.search_leftmost_substring(nfa_plus2E, 'ABCEEE', False, True)
(3, 5)


>>> ops.search_leftmost_substring_ex_ex(nfa_plus2E, 0, zip('ABCEEE', range(1,10)), True, False)
('LeftMostBegin_SuccessUntilEnd', ((3, 3), (6, 6)), (6, 6))


# E?{10}E{10}
>>> reE = SingleRE('E')
>>> re_10_10 = reE[0:1][10] >> reE[10]
>>> nfa_10_10 = re_10_10.toSimpleNFA()
>>> ops.search_leftmost_substring(nfa_10_10, 'ABC' + 'E'*12, True, False)
(3, 15)
>>> ops.search_leftmost_substring(nfa_10_10, 'ABC' + 'E'*12, False, False)
(3, 13)
>>> ops.search_leftmost_substring(nfa_10_10, 'ABC' + 'E'*12, False, True)
(3, 13)
>>> ops.search_leftmost_substring(nfa_10_10, 'ABC' + 'E'*12, True, True)
(3, 13)


search_leftmost_substring:
    # greedy, leftmost_end_first
    are these two cases have same result?:
        greedy=True, leftmost_end_first=True
        greedy=False, leftmost_end_first=False
    NO! see below example:
        search_leftmost_substring (S+A+|B+S+A+X+) in "BBBSSSAAAXXX"
            greedy leftmost_end_first   result
            True        False           (0, 12)
            False       False           (0, 10)
            True        True            (3, 7)
            False       True            (5, 7)

>>> reB, reS, reA, reX = map(mkSingleRE, 'BSAX')
>>> re_SA_BSAX = (+reS >> +reA) | (+reB >> +reS >> +reA >> +reX)
>>> nfa_SA_BSAX = re_SA_BSAX.toSimpleNFA()
>>> ops.search_leftmost_substring(nfa_SA_BSAX, 'SA', True, False)
(0, 2)

>>> str_BSAX = 'BBBSSSAAAXXX'
>>> ops.search_leftmost_substring(nfa_SA_BSAX, str_BSAX, True, False)
(0, 12)
>>> ops.search_leftmost_substring(nfa_SA_BSAX, str_BSAX, False, False)
(0, 10)
>>> ops.search_leftmost_substring(nfa_SA_BSAX, str_BSAX, True, True)
(3, 7)
>>> ops.search_leftmost_substring(nfa_SA_BSAX, str_BSAX, False, True)
(5, 7)
>>> ops.search_leftmost_substring_ex_ex(nfa_SA_BSAX, 0, zip(str_BSAX, range(1, len(str_BSAX))), False, True)
('LeftMostEnd_NonGreedyBegin', ((5, 5), (7, 7)), (7, 7))


'''



def _t():
    from .SimpleRE import \
        (DeadRE
        ,NullRE
        ,SingleRE
        ,ConcatenationRE
        ,AlternationRE
        ,CountedRepetitionRE
        ,MoreRepetitionRE
        ,theDeadRE
        ,theNullRE
        ,mkSingleRE
        ,mkOneOrMoreRE
        ,mkConcatenationRE__from_iterable
        ,mkAlternationRE__from_iterable
        ,mkConcatenationRE
        ,mkAlternationRE
        ,mkZeroOrOneRE
        ,mkZeroOrMoreRE
        ,mkExactRepetitionRE
        ,mkCountedRepetitionRE
        ,mkMoreRepetitionRE
        )

    ops = _ops

    mk = mkSimpleNFA
    show = lambda nfa: nfa.show(repr)

    re_plus2E = mkMoreRepetitionRE(SingleRE('E'), 2) # E{2,}
    nfa_plus2E = mk(re_plus2E)
    r = ops.does_accept_ex(nfa_plus2E, '0', zip('EE', '12'))
    try:
        assert r[0] > 0
    except:
        print(r)
        raise
#_t()




if __name__ == "__main__":
    import doctest
    doctest.testmod()


