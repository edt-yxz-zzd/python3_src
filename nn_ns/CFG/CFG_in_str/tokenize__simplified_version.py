

__all__ = '''
    tokenizer__simplified_version
    tokenize__simplified_version
    iter_tokenize__simplified_version
    '''.split()

from seed.ECHO import INITIAL
from nn_ns.Tokenizer.biregex.BiPatternABC__directly import \
    (BiPatternABC__directly
    ,BiPatternABC__directly__same
    )
from nn_ns.Tokenizer.with_state.RecognizerABC__using_biregex import \
    RecognizerABC__using_biregex__directly
from nn_ns.Tokenizer.with_state.Tokenizer_with_state import \
    Tokenizer_with_state
from ..class_property import class_property
from .Token import Token

biregex_dict = {}
class BiPatternHereSame(BiPatternABC__directly__same):
    biregex_dict = globals()['biregex_dict']

class ignore(BiPatternHereSame):
    pattern_fmt = r'\s+'

class comment(BiPatternHereSame):
    pattern_fmt = r'(?<!\S)[#][^\n]*'
class filter(BiPatternHereSame):
    pattern_fmt = r'\b(?!\d)\w+[$](?![$])'
class filter_ex(BiPatternHereSame):
    pattern_fmt = r'\b\w+[$][$](?![$])'
class decorator(BiPatternHereSame):
    pattern_fmt = r'~@|(?<!@)\b\w+@'
class name(BiPatternHereSame):
    pattern_fmt = r'\b(?!\d)\w+\b(?![$@])'

    # r'@\w+@'
class kw_terminal_set(BiPatternHereSame):
    pattern_fmt = '@terminal_set@'
class kw_start_nonterminal(BiPatternHereSame):
    pattern_fmt = '@start_nonterminal@'
class kw_ambiguous_nonterminal(BiPatternHereSame):
    pattern_fmt = '@ambiguous_nonterminal@'
class kw_maybedead_nonterminal(BiPatternHereSame):
    pattern_fmt = '@maybedead_nonterminal@'
class kw_pass(BiPatternHereSame):
    pattern_fmt = '@pass@'
class kw_any(BiPatternHereSame):
    pattern_fmt = '@any@'
class kw_none(BiPatternHereSame):
    pattern_fmt = '@none@'
    # '@none@?'
    # '@noise@+'

class op_semicolon(BiPatternHereSame):
    pattern_fmt = r'(?<!\S);(?!\S)'
class op_colon(BiPatternHereSame):
    pattern_fmt = r'(?<!\S):(?!\S)'
class op_eq(BiPatternHereSame):
    pattern_fmt = r'(?<!\S)=(?!\S)'
    # (((
class op_discard(BiPatternHereSame):
    pattern_fmt = r'(?<!\S)[-](?=\S)(?![,)])'
class op_selected(BiPatternHereSame):
    pattern_fmt = r'(?<!\S)[+](?=\S)(?![,)])'
class op_unpack(BiPatternHereSame):
    pattern_fmt = r'(?<!\S)[*](?=\S)(?![,)])'

    # (({[
class op_multi(BiPatternHereSame):
    pattern_fmt = r'(?<=[\w)>\]}}@])[?*+](?:(?!\S)|(?=[,)]))'

#print(op_multi.__abstractmethods__)
assert biregex_dict



###############################################################
recognizer_dict = {}
class _R(RecognizerABC__using_biregex__directly):
    recognizer_dict = globals()['recognizer_dict']
    #require: biregex
    @class_property
    def biregex(cls):
        if cls is __class__: return None
        return biregex_dict[cls.name]

    #allow_empty = False
    #   set below;
    #   why? to make _R abstract
    #   it is easier to merge _R and BiPatternHereSame together
    precondition_states = {INITIAL}
    to_state = None
    @classmethod
    def iter_tokens(cls, regex_match_result):
        m = regex_match_result
        yield Token(cls.name, m.string, m.start(), m.end())

#print(_R.__abstractmethods__)
def fill_recognizer_dict():
    for name in biregex_dict:
        T = type(name, (_R,), {'allow_empty':False})
        #print(T.__abstractmethods__)
fill_recognizer_dict()
assert recognizer_dict

###############################################################
def _remove_tokens():
    @classmethod
    def iter_tokens(cls, regex_match_result):
        return; yield
    for name in 'ignore comment'.split():
        recognizer_dict[name].iter_tokens = iter_tokens
_remove_tokens()
del _remove_tokens
###############################################################


tokenizer__simplified_version \
    = Tokenizer_with_state(INITIAL, recognizer_dict.values())
def tokenize__simplified_version(source):
    return list(iter_tokenize__simplified_version(source))
def iter_tokenize__simplified_version(source):
    return tokenizer__simplified_version.iter_tokens(source, 0, len(source))



if __name__ == "__main__":
    from .concrete_CFG_syntax import simplified_concrete_CFG_syntax
    tokens = tokenize__simplified_version(simplified_concrete_CFG_syntax)
    print(tokens)
    from pprint import pprint
    pprint(tokens)



