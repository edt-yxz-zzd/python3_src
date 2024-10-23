#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/regex/regex_utilities.py
    view ../../python3_src/seed/recognize/regex/RegexLiteral.py
    view ../../python3_src/seed/recognize/regex/NFA5RegexRepr.py

seed.recognize.regex.regex_utilities
py -m nn_ns.app.debug_cmd   seed.recognize.regex.regex_utilities -x
py -m nn_ns.app.doctest_cmd seed.recognize.regex.regex_utilities:__doc__ -ht



>>> nfa__As = compile8NFA(r' ?!([+,) a ?!(,+])  ')
>>> nfa__As
NFA5RegexRepr(RegexRepr_Colored(RegexRepr_Many1(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))), ''), frozenset({''}))
>>> nfa__As.fullmatch('aaaa', key=ord)
(4, frozenset({''}))
>>> nfa__As.fullmatch('aaaab', key=ord) is None
True
>>> nfa__As.match('aaaab', key=ord)
(4, frozenset({''}), True, False)
>>> nfa__As.match('bbbaaaab', key=ord) is None
True
>>> nfa__As.search('bbbaaaab', key=ord)
(7, {'': (3, 6)}, (3, 6), True, False)
>>> nfa__As.search('bbbb', key=ord) is None
True







>>> dfa__As = compile8DFA(r' ?!([+,) a ?!(,+])  ')
>>> dfa__As
DFA5RegexRepr(NFA5RegexRepr(RegexRepr_Colored(RegexRepr_Many1(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))), ''), frozenset({''})))
>>> dfa__As.fullmatch('aaaa', key=ord)
(4, frozenset({''}))
>>> dfa__As.fullmatch('aaaab', key=ord) is None
True
>>> dfa__As.match('aaaab', key=ord)
(4, frozenset({''}), True, False)
>>> dfa__As.match('bbbaaaab', key=ord) is None
True





#]]]'''
__all__ = r'''
compile_regex_
    compile8NFA
        match4NFA
        fullmatch4NFA
        search4NFA
    compile8DFA
        match4DFA
        fullmatch4DFA
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.regex.RegexLiteral import Parser4RegexLiteral, parser4RegexLiteral__no_builtins, parser4RegexLiteral__with_2x2_builtins, tokenizer4RegexLiteral, tokenizer4RegexLiteral__with_comment
from seed.recognize.regex.NFA5RegexRepr import NFA5RegexRepr, DFA5RegexRepr


from seed.tiny import ifNone
___end_mark_of_excluded_global_names__0___ = ...


######################
from seed.recognize.regex.NFA5RegexRepr import match4NFA, fullmatch4NFA, search4NFA
from seed.recognize.regex.NFA5RegexRepr import match4DFA, fullmatch4DFA

######################
def compile_regex_(text, /, *, NFA_vs_DFA:bool, parser=None, colors4original_stop_pst=None, may_config=None, may_interesting_colors=None, may_whole_set4tkey=None, to_output_regex_repr=False):
    'str -> (NFA5RegexRepr if not NFA_vs_DFA else DFA5RegexRepr, ?to_output_regex_repr=>?regex_repr?)'
    parser = ifNone(parser, parser4RegexLiteral__no_builtins)
    regex_repr = parser.parse__text(text)
    if colors4original_stop_pst is None:
        color4stop = ''
        regex_repr %= color4stop
        colors4original_stop_pst = [color4stop]
    assert not colors4original_stop_pst is None
    nfa = NFA5RegexRepr(regex_repr, colors4original_stop_pst, may_config, may_interesting_colors, may_whole_set4tkey)
    if NFA_vs_DFA:
        xfa = dfa = DFA5RegexRepr(nfa)
    else:
        xfa = nfa
    xfa
    if to_output_regex_repr:
        return (xfa, regex_repr)
    return xfa

######################
def compile8NFA(text, /, *, parser=None, colors4original_stop_pst=None, may_config=None, may_interesting_colors=None, may_whole_set4tkey=None, to_output_regex_repr=False):
    'str -> (NFA5RegexRepr, ?to_output_regex_repr=>?regex_repr?)'
    d = dict(locals())
    del d['text']
    return compile_regex_(text, NFA_vs_DFA=False, **d)

######################
def compile8DFA(text, /, *, parser=None, colors4original_stop_pst=None, may_config=None, may_interesting_colors=None, may_whole_set4tkey=None, to_output_regex_repr=False):
    'str -> (DFA5RegexRepr, ?to_output_regex_repr=>?regex_repr?)'
    d = dict(locals())
    del d['text']
    return compile_regex_(text, NFA_vs_DFA=True, **d)

######################








__all__
from seed.recognize.regex.regex_utilities import compile_regex_, compile8NFA, compile8DFA
from seed.recognize.regex.regex_utilities import compile8NFA, match4NFA, fullmatch4NFA, search4NFA
from seed.recognize.regex.regex_utilities import compile8DFA, match4DFA, fullmatch4DFA
from seed.recognize.regex.regex_utilities import *
