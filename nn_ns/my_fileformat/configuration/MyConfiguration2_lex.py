
r'''
problem:
    * rough/precise regex pattern
        rough to fast-trap-read
        precise to dectect error
    * distinguish: RawDictKey vs Name vs Integer
        vs inline cb-string vs multiline cb-string
        vs body-headers

        RawDictKey.rough follows by "(?=\s*=)"
        Name/Integer.rough follows by "(?!\s*=)"
            bug:not enough!!!!
            SHOULD add (?!RawDictKey) at front!!

        Name begins by '(?![+-\d])'
        Integer begins by '[+-]?(?=\d)'

        inline cb-string contains ['"]
        RawDictKey/Name/Integer donot

        multiline cb-string contains [,;|\\]
        Name/Integer donot
        multiline cb-string after indents1?
        RawDictKey does not

        body-headers contains [{}\[\]()]
        RawDictKey/Name/Integer donot
    * distinguish: seperater-comma vs multiline cb-string(continuer-comma)
        multiline cb-string after indents1?
        seperater-comma donot
    * distinguish: OPEN and Head
        {...} vs {}:
        [...] vs []:
        (...) vs ():
        '...' vs '':
        b'...' vs b'':
    * cannot distinguish CharStringBodyLine and ByteStringBodyLine!
        byte_string is just encode char_string by 'ascii'!
        merge CharStringBodyLine and ByteStringBodyLine into XStringBodyLine

3-states:
    #no INITIAL, so jump to AfterNoIndents at the beginning
    ANY
    AfterNoIndents                  # AfterNoIndents
    AfterNoIndents_AfterIndents1    # AfterIndents0
    inside                          # NotAfterIndents0

    start from ANY|AfterNoIndents
        ANY_ BigNewlineNoIndents
            = ignore_tail0 newline (ignore_tail0 newline)* (?![#\s])
            | ignore_tail1 (\Z)
            state: -> AfterNoIndents
        ANY_ BigNewlineIndents1
            = ignore_tail0 newline (ignore_tail0 newline)* indents1 (?![#\s])
            state: -> AfterIndents1

        ANY_ * # except belows:
        AfterNoIndents_OP_UNINDENT_ [CharStringHead/ByteStringHead/ObjectTupleHead/ObjectArrayHead/DictHead]
            state: -> inside
            # they if any should be the first non-ignore-token
            #   'first'/'at-most-one' is promise by CFG-product-rule, not by tokenizer
        AfterNoIndents_AfterIndents1_ [CharStringBodyLine/ByteStringBodyLine]
            state: -> inside
        inside_OP_ [COMMA/COLON/ASSIGN/DIV]
            state: --
        inside_ Ignores1 # Ignores0 = Ignores1?
            state: --

        ANY_
            Name/Integer/RawDictKey
            Inline_ByteString/Inline_CharString
            state: -> inside
        ANY_OP_
            [SMALL_/MIDDLE_/BIG_][OPEN/CLOSE]
            [CharStringHead/ByteStringHead/ObjectTupleHead/ObjectArrayHead/DictHead]
            state: -> inside

################
name convention
    noncapital - regex ; allow match ''
        ignore_tail0
        ignore_tail1
    captial - token regex ; not allow match ''
        BigNewlineNoIndents


################
usage:
    tokens = parse_source_string(src)
    iter_tokens = iter_parse_source_string(src)

################
__usage:
    import nn_ns.my_fileformat.configuration.MyConfiguration2_lex \
        as THIS_MODULE
    import ply.lex
    lexer = ply.lex.lex(module = MyConfiguration2_lex)
    lexer.input(source_string)
    lexer.begin(THIS_MODULE.START_STATE)#NOTE!!!!
    tokens = list(iter(lexer))




################ parts of this file:
0 define 'tokens' 'states'
1 utils:
    make_Pattern... # which has been moved out
2 define patterns
3 define token actions
4 define token value parsers
    parse_Inline_CharString... # which has been moved out
5 tokens filter
    extract indents from big_newlines
'''

# tokens - lex
#   indeed raw_tokens
# terminals - yacc
#   lex_postprocess_filter :: raw_tokens -> terminals
__all__ = '''
    tokens
    terminals

    states
    __file__
    lex_postprocess_filter
    lex_postprocessor

    count_newlines
    '''.split()

# outdated by LexPostprocessor
'''
    iter_parse_source_string
    parse_source_string

    lex_postprocess_filter
    iter_raw_parse_source_string
    raw_parse_source_string

    START_STATE
    pseudo_this_module
    regex_flags
    lexers


    '''.split()

'''
utils:
    Flippable
    PatternBase

    StateTo
    make_token_action
    make_token_action_and_inject_to
    LexError
    overflow_xfind
    overflow_rfind
    overflow_find
    token_error_handle
    extract_token_info
    lex_error_handle
    make_pseudo_lex_module_obj


using:
    StateTo
    make_Pattern
    make_token_action_and_inject_to
    token_error_handle
    lex_error_handle
    make_pseudo_lex_module_obj


'''
# LexError, SyntaxError, IndentationError
from .utils.StateTo import StateTo
from .utils.PatternBase import make_Pattern, PatternBase
from .utils.make_token_action import make_token_action_and_inject_to
from .utils.lex_error_handle import lex_error_handle, token_error_handle
from .utils.make_pseudo_lex_module_obj import make_pseudo_lex_module_obj, show_pseudo_lex_module_obj
from .utils.LexPostprocessors.LexPostprocessor import LexPostprocessor

from .parse_Inline_CharString import (
    parse_Inline_CharString
    ,parse_Inline_ByteString
    ,parse_ByteStringBodyLine
    ,parse_CharStringBodyLine
    )


import ply.lex
from ast import literal_eval
#from re import compile as ___re_compile
#import re as _re

if True or weird:
    import re
    assert re.compile(r'fs\Z').match('afsx', 1,3)
    assert not re.compile(r'\Afs\Z').match('afsx', 1,3)
    del re


#START_STATE = 'INITIAL'
START_STATE = 'AfterNoIndents'


Pattern = make_Pattern(globals())

##########################################
#ANY
#AfterNoIndents
#AfterNoIndents_AfterIndents1
#inside
##########################################
exclusive = 'exclusive'
inclusive = 'inclusive'
states = dict(
    AfterNoIndents=exclusive
    ,AfterIndents1=exclusive
    ,inside=exclusive
    )
states = list(states.items())
terminals_only = (
    #EOF
    '''
    NullIndent
    Indent
    Dedent
    '''.split()
    )
raw_tokens_only = '''
    BigNewlineNoIndents
    BigNewlineIndents1
    '''.split()
common_of_terminals_and_raw_tokens = (
    #CharStringBodyLine
    #ByteStringBodyLine
    '''
    XStringBodyLine
    Ignores1

    Name
    Integer
    RawDictKey
    Inline_ByteString
    Inline_CharString

    OP_UNINDENT_CharStringHead
    OP_UNINDENT_ByteStringHead
    OP_UNINDENT_ObjectTupleHead
    OP_UNINDENT_ObjectArrayHead
    OP_UNINDENT_DictHead

    OP_COMMA
    OP_COLON
    OP_ASSIGN
    OP_DIV
    OP_CharStringHead
    OP_ByteStringHead
    OP_ObjectTupleHead
    OP_ObjectArrayHead
    OP_DictHead

    OP_SMALL_OPEN
    OP_SMALL_CLOSE
    OP_MIDDLE_OPEN
    OP_MIDDLE_CLOSE
    OP_BIG_OPEN
    OP_BIG_CLOSE
    '''.split()
    )

tokens = raw_tokens = \
    raw_tokens_only + common_of_terminals_and_raw_tokens
terminals = terminals_only + common_of_terminals_and_raw_tokens



state_to = StateTo(states)
##########################################
raw_newline_chars = r'\n\r'
raw_inline_text_chars = r'\x20\u3000\S'
raw_the_space = r'\x20'
raw_the_comment_char = r'\#'

# is OK: f?r?''
#   avoid f'
#   fr' ...{raw_...}, {{not_raw_name}}, {{{{1232\d+}}}}'
#   r' ...{not_raw_name}... {{1234\d+}}...'
#   r'...(?!{not_raw_name.flip}...' # '?!' ==>> ".flip"
#   fr'...(?!{{not_raw_name.flip}}...' # '?!' ==>> ".flip"
class whole_sourcefile_char(Pattern):
    no_wrap = True
    rough_pattern = r'[\D\d]'
    precise_pattern = fr'[{raw_newline_chars}{raw_inline_text_chars}]'
class inline_text_char(Pattern):
    # text_char = inline_text_char|'\n'
    no_wrap = True
    rough_pattern = fr'[^{raw_newline_chars}]'
    precise_pattern = fr'[{raw_inline_text_chars}]'
class the_space(Pattern):
    no_wrap = True
    rough_pattern = precise_pattern = fr'{raw_the_space}'
class comment_char(Pattern):
    no_wrap = True
    rough_pattern = precise_pattern = fr'{raw_the_comment_char}'
class newline(Pattern):
    no_wrap = True
    rough_pattern = precise_pattern = fr'[{raw_newline_chars}]'
class tail_comment(Pattern):
    rough_pattern_fmt = r"{comment_char}{inline_text_char}*$"
    precise_pattern_fmt = r"{comment_char}(?:{the_space}{inline_text_char}*)?$"

class ignore_char(Pattern):
    ####xxx: no_wrap = True
    rough_pattern_fmt = r'(?!{newline.flip})\s'
    precise_pattern_fmt = r'{the_space}'
class ignores0(Pattern):
    pattern_fmt = r'{ignore_char}*'
class Ignores1(Pattern):
    pattern_fmt = r'{ignore_char}+'
class ignore_tail0(Pattern):
    pattern_fmt = r'{ignore_char}*{tail_comment}?$'
class ignore_tail1(Pattern):
    pattern_fmt = r'(?={ignore_char}|{comment_char}){ignore_tail0}$'

class indents1(Pattern):
    pattern_fmt = r'^{ignore_char}+(?!{ignore_char.flip})'

###############################BigNewlineNoIndents/BigNewlineIndents1
class BigNewlineNoIndents(Pattern):
    pattern_fmt = r'(?:{ignore_tail0}{newline})*{ignore_tail1}\Z|(?:{ignore_tail0}{newline})+(?!{comment_char.flip}|\s)'
class BigNewlineIndents1(Pattern):
    pattern_fmt = r'(?:{ignore_tail0}{newline})+(?P<indents1>{indents1})(?!{comment_char.flip}|\s)'

###############################XStringBodyLine/CharStringBodyLine/ByteStringBodyLine

raw_xdigits = r'0-9A-F' # not include [a-f]
class xdigit(Pattern):
    no_wrap = True
    rough_pattern = precise_pattern = fr'[{raw_xdigits}]'
        # not include [a-f]
class inline_text_byte(Pattern):
    # text_byte = inline_text_byte|'\n'
    no_wrap = True
    rough_pattern = inline_text_char.rough_pattern
    precise_pattern = r'(?:(?=[\x00-\x7F])[\x20\S])'
class string_byte(Pattern):
    pattern_fmt = r'(?![\'\"\\]){inline_text_byte}'
class escaped_byte_sequence(Pattern):
    pattern_fmt = r'\\\\|\\\"|\\\'|\\n|\\r|\\t|\\x{xdigit}{{2}}'
        # exclude '\0'
class string_char(Pattern):
    pattern_fmt = r'(?![\'\"\\]){inline_text_char}'
class escaped_char_sequence(Pattern):
    pattern_fmt = r'\\\\|\\\"|\\\'|\\n|\\r|\\t|\\x{xdigit}{{2}}|\\u&{xdigit}{{4}};|\\U&{xdigit}{{4}}_{xdigit}{{4}};'
        # exclude '\0'
class escaped_char_in_body(Pattern):
    pattern_fmt = r"[\'\"]|{string_char}|{escaped_char_sequence}"
class escaped_byte_in_body(Pattern):
    pattern_fmt = r"[\'\"]|{string_byte}|{escaped_byte_sequence}"
class CharStringBodyLine(Pattern):
    pattern_fmt = (
        r'[;,][ ]{{3}}{inline_text_char}*$'
        '|'
        r'[|\\][ ]{{3}}{escaped_char_in_body}*$'
        '|'
        r'[|\\;,]$'
        )
class XStringBodyLine(Pattern):
    pattern_fmt = CharStringBodyLine.pattern_fmt
class ByteStringBodyLine(Pattern):
    pattern_fmt = (
        r'[;,][ ]{{3}}{inline_text_byte}*$'
        '|'
        r'[|\\][ ]{{3}}{escaped_char_in_body}$'
        '|'
        r'[|\\;,]$'
        )




###############################Name/Integer/RawDictKey
class RawDictKey(Pattern):
    pattern_fmt = r"(?:(?![\'\",:=#(){{}}\[\]\s]){inline_text_char})+(?=\s*=)"

class Name(Pattern):
    ALL_CONSTANT_NAMES = 'True False None'.split()

    rough_pattern = fr'''(?!{RawDictKey.rough_pattern})\b(?!\d)\w+\b(?!\s*=)(?!['"])'''
    #precise_pattern_fmt = r'(?!\d)(?:(?={inline_text_char})\w)+(?!\s*=)'
    precise_pattern = '|'.join(ALL_CONSTANT_NAMES)
    precise_pattern = fr'''\b(?:{precise_pattern})\b(?!\s*=)(?!['"])'''

class Integer(Pattern):
    rough_pattern = fr'(?!{RawDictKey.rough_pattern})[+-]?\b(?=\d)\w+\b(?!\s*=)'

    hex_pint = fr"(?:0x[_0]*(?![_0])[_{raw_xdigits}]+)" # not "0X"
    bin_pint = r"(?:0b[_0]*1[_01]*)" # not "0B"
    dec_pint = r"(?:(?![_0])[0-9]+)"
    pint = fr'(?:{hex_pint}|{dec_pint}|{bin_pint})'

    nonzero_int = fr"(?:[+-]?\b{pint}\b)" # "-3" not "- 3"
    zero_int = r"\b0\b" # not "-0" "0x0"...
    sint = fr"(?:{zero_int}|{nonzero_int})"

    precise_pattern = fr'{sint}(?!\s*=)'

###############################Inline_ByteString/Inline_CharString
class Inline_CharString(Pattern):
    # old version: r'\'' is complete!
    # new version: r'\' is complete!
    pattern_fmt = (
        r"""'(?:(?!'){escaped_char_in_body})*'"""
        '|'
        #old version:
        #r"""r'(?:(?!['\\]){inline_text_char}|\\{inline_text_char})*'"""
        r"""r'(?:(?![']){inline_text_char})*?'"""

        '|'
        r'''"(?:(?!"){escaped_char_in_body})*"'''
        '|'
        #old version:
        #r'''r"(?:(?!["\\]){inline_text_char}|\\{inline_text_char})*"'''
        r'''r"(?:(?!["]){inline_text_char})*?"'''
        )
    #pattern_fmt = f'(?:{pattern_fmt})(?!:)'
    pattern_fmt = f"""(?!'':)(?:{pattern_fmt})"""
        # avoid '':
class Inline_ByteString(Pattern):
    pattern_fmt = (
        r"""b'(?:(?!'){escaped_byte_in_body})*'"""
        '|'
        #old version:
        #r"""rb'(?:(?!['\\]){inline_text_byte}|\\{inline_text_byte})*'"""
        r"""rb'(?:(?![']){inline_text_byte})*?'"""

        '|'
        r'''b"(?:(?!"){escaped_byte_in_body})*"'''
        '|'
        #old version:
        #r'''rb"(?:(?!["\\]){inline_text_byte}|\\{inline_text_byte})*"'''
        r'''rb"(?:(?!["]){inline_text_byte})*?"'''
        )
    #pattern_fmt = f'(?:{pattern_fmt})(?!:)'
    pattern_fmt = f"""(?!b'':)(?:{pattern_fmt})"""
        # avoid b'':






###############################

####################### t_XXX
def count_newlines(s):
    i = 0
    for i, _ in enumerate(newline.precise_regex.finditer(s), 1):pass
    return i
@state_to('-> AfterNoIndents', BigNewlineNoIndents)
def t_ANY_BigNewlineNoIndents(t):
    #= (ignore_tail0 newline)+ (?![#\s])
    #| ignore_tail1 (\Z)
    t.num_newlines = count_newlines(t.value)
    t.lexer.lineno += t.num_newlines
    t.indent_level = 0
    return t
@state_to('-> AfterIndents1', BigNewlineIndents1)
def t_ANY_BigNewlineIndents1(t):
    #= (ignore_tail0 newline)+ indents1 (?![#\s])
    t.num_newlines = count_newlines(t.value)
    t.lexer.lineno += t.num_newlines

    indents1 = t.lexer.lexmatch.group('indents1')
    if len(indents1)%4 != 0 or indents1 != ' '*len(indents1):
        err_msg = f'indents must be " "*4*x: {t.lineno}: {indents1}'
        raise token_error_handle(__token, IndentationError, err_msg)
        raise IndentationError(err_msg)

    indent_level = len(indents1)//4
    assert indent_level*4 == len(indents1)
    t.indent_level = indent_level
    return t

############ inside_OP_/inside_
#inside_OP_ [COMMA/COLON/ASSIGN/DIV]
#   state: --
#inside_ Ignores1 # Ignores0 = Ignores1?
#   state: --
##
t_inside_OP_COMMA   = r','
t_inside_OP_COLON   = r':'
t_inside_OP_ASSIGN  = r'='
t_inside_OP_DIV     = r'/'

@state_to('--', Ignores1)
def t_inside_Ignores1(t):
    assert '\n' not in t.value
    assert '\r' not in t.value
    return t


################ AfterNoIndents_OP_UNINDENT_/AfterNoIndents_AfterIndents1_
#AfterNoIndents_OP_UNINDENT_ [CharStringHead/ByteStringHead/ObjectTupleHead/ObjectArrayHead/DictHead]
#   state: -> inside
#   # they if any should be the first non-ignore-token
#   #   'first' is promise by CFG-product-rule, not by tokenizer
#AfterNoIndents_AfterIndents1_ [XStringBodyLine/CharStringBodyLine/ByteStringBodyLine]
#   state: -> inside
###############
def make_token_action_and_inject_globals(
    from_states, to_state, token_name, string
    , *, escaped:bool):
    make_token_action_and_inject_to(
        from_states, to_state, token_name, string
        , escaped=escaped, globals=globals())


OP_UNINDENT_XXXHead2constant = dict(
    CharString = ">>> '':"
    ,ByteString = ">>> b'':"
    ,ObjectTuple = ">>> ():"
    ,ObjectArray = ">>> []:"
    ,Dict = ">>> {}:"
    )
def make_all__t_AfterNoIndents_OP_UNINDENT_XXXHead():
    # t_AfterNoIndents_OP_UNINDENT_ CharStringHead(t):
    from_states = 'AfterNoIndents'
    to_state = 'inside'
    for base_name, constant_string in OP_UNINDENT_XXXHead2constant.items():
        token_name = f'OP_UNINDENT_{base_name}Head'
        make_token_action_and_inject_globals(
            from_states, to_state, token_name, constant_string
            , escaped=False
            )
    return
make_all__t_AfterNoIndents_OP_UNINDENT_XXXHead()
del make_all__t_AfterNoIndents_OP_UNINDENT_XXXHead


@state_to('-> inside', XStringBodyLine)
def t_AfterNoIndents_AfterIndents1_XStringBodyLine(t):
    # treat byte_string as char_string
    t.value = parse_CharStringBodyLine(t.value)
    return t
'''
@state_to('-> inside', CharStringBodyLine)
def t_AfterNoIndents_AfterIndents1_CharStringBodyLine(t):
    t.value = parse_CharStringBodyLine(t.value)
    return t
@state_to('-> inside', ByteStringBodyLine)
def t_AfterNoIndents_AfterIndents1_ByteStringBodyLine(t):
    t.value = parse_ByteStringBodyLine(t.value)
    return t
'''


###############
#ANY_OP_
#   [SMALL_/MIDDLE_/BIG_][OPEN/CLOSE]
#   [CharStringHead/ByteStringHead/ObjectTupleHead/ObjectArrayHead/DictHead]
#   state: -> inside
###############

OP_XXXHead2constant = dict(
    CharString = "'':"
    ,ByteString = "b'':"
    ,ObjectTuple = "():"
    ,ObjectArray = "[]:"
    ,Dict = "{}:"
    )
def make_all__t_ANY_OP_XXXHead():
    # t_ANY_OP_ CharStringHead(t):
    from_states = 'ANY'
    to_state = 'inside'
    for base_name, constant_string in OP_XXXHead2constant.items():
        token_name = f'OP_{base_name}Head'
        make_token_action_and_inject_globals(
            from_states, to_state, token_name, constant_string
            , escaped=False
            )
    return
make_all__t_ANY_OP_XXXHead()
del make_all__t_ANY_OP_XXXHead



#[SMALL_/MIDDLE_/BIG_][OPEN/CLOSE]
OP_XXX_YYY2pattern = dict(
    SMALL_OPEN     = r'(?:\((?!\):))' # (
    ,SMALL_CLOSE    = r'\)'
    ,MIDDLE_OPEN    = r'(?:\[(?!\]:))' # [
    ,MIDDLE_CLOSE   = r'\]'
    ,BIG_OPEN       = r'(?:\{(?!\}:))' # {
    ,BIG_CLOSE      = r'\}'
    )
def make_all__t_ANY_OP_XXX_YYY():
    # t_ANY_OP_ SMALL_OPEN(t):
    from_states = 'ANY'
    to_state = 'inside'
    for base_name, constant_string in OP_XXX_YYY2pattern.items():
        token_name = f'OP_{base_name}'
        make_token_action_and_inject_globals(
            from_states, to_state, token_name, constant_string
            , escaped=True ##not False
            )
    return
make_all__t_ANY_OP_XXX_YYY()
del make_all__t_ANY_OP_XXX_YYY




###############
#ANY_
#   Name/Integer/RawDictKey
#   Inline_ByteString/Inline_CharString
#   state: -> inside
###############
@state_to('-> inside', Name)
def t_ANY_Name(t):
    t.value = literal_eval(t.value)
    return t
@state_to('-> inside', Integer)
def t_ANY_Integer(t):
    t.value = literal_eval(t.value.replace('_', ''))
    return t
@state_to('-> inside', RawDictKey)
def t_ANY_RawDictKey(t):
    pass
    return t
@state_to('-> inside', Inline_ByteString)
def t_ANY_Inline_ByteString(t):
    t.value = parse_Inline_ByteString(t.value)
    return t
@state_to('-> inside', Inline_CharString)
def t_ANY_Inline_CharString(t):
    t.value = parse_Inline_CharString(t.value)
    return t



######################## error handle
#   AfterNoIndents                  # AfterNoIndents
#   AfterNoIndents_AfterIndents1    # AfterIndents0
#   inside                          # NotAfterIndents0
########################
def t_error(t):
    raise logic-error
def t_AfterNoIndents_error(t):
    return lex_error_handle(t, 'AfterNoIndents')
def t_AfterIndents1_error(t):
    return lex_error_handle(t, 'AfterIndents1')
def t_inside_error(t):
    return lex_error_handle(t, 'inside')





























##################################
# tokens filter
#   token.type
#   token.value
#   token.lexpos
#   token.lineno
#   token.lexer
def make_lex_token(*, type, value, lexpos, lineno, lexer):
    d = dict(locals())
    t = ply.lex.LexToken()
    t.__dict__.update(d)
    return t

_newline_cases = ('BigNewlineIndents1', 'BigNewlineNoIndents')
def _is_OP_UNINDENT_XXXHead_token(t):
    tp = t.type
    return tp.startswith('OP_UNINDENT_') and tp.endswith('Head')
def lex_postprocess_filter(tokens):
    # lex_postprocess_filter :: raw_tokens -> terminals
    def iter_maybe_new_NullIndentToken(token):
        end = token.lexpos + len(token.value)
        if end == len(token.lexer.lexdata):
            # last big_newlines
            # donot yet NullIndent
            pass
        else:
            yield make_NullIndentToken(token)
        return


    indent_level = 0
    #prev_is_OP_UNINDENT = False
    #_is_OP_UNINDENT = _is_OP_UNINDENT_XXXHead_token
    for token in tokens:
        if token.type not in _newline_cases:
            yield token
            #prev_is_OP_UNINDENT = _is_OP_UNINDENT(token)
            continue

        # will discard this newline token

        next_indent_level = token.indent_level
        if False and prev_is_OP_UNINDENT:
            # prev token is OP_UNINDENT_XXXHead
            yield from iter_maybe_new_NullIndentToken(token)
            if next_indent_level > indent_level:
                err_msg = 'too much indents!'
                raise token_error_handle(token, IndentationError, err_msg)
        #prev_is_OP_UNINDENT = False

        if next_indent_level == indent_level:
            #bug: yield make_NullIndentToken(token)
            yield from iter_maybe_new_NullIndentToken(token)
            # NullIndent is newline??
        elif next_indent_level > indent_level:
            if next_indent_level == indent_level+1:
                yield make_IndentToken(token)
            else:
                err_msg = 'too much indents!'
                raise token_error_handle(token, IndentationError, err_msg)
        else:
            assert 0 <= next_indent_level < indent_level
            n = indent_level-next_indent_level
            yield from make_DedentTokens(token, n)
            # Dedent many1-to-1 NullIndent
            yield from iter_maybe_new_NullIndentToken(token)
        indent_level = next_indent_level

    #end-of-file
    #   pad dedents
    yield from make_DedentTokens(token, indent_level)
    #yield make_EOF_Token(token) # useless
    return

def make_EOF_Token(big_newline_token):
    return make_XXdentToken(big_newline_token, type='EOF')
def make_NullIndentToken(big_newline_token):
    return make_XXdentToken(big_newline_token, type='NullIndent')
def make_IndentToken(big_newline_token):
    return make_XXdentToken(big_newline_token, type='Indent')
def make_DedentTokens(big_newline_token, num):
    return [make_XXdentToken(big_newline_token, type='Dedent')]*num
def make_XXdentToken(big_newline_token, *, type):
    #BigNewlineIndents1/BigNewlineNoIndents
    t = big_newline_token
    assert t.type in _newline_cases
    assert type in ('Indent', 'Dedent', 'NullIndent', 'EOF')

    L = t.indent_level*4
    end = t.lexpos + len(t.value)
        # big_newline_token's value donot change
        #   so its len is useful
    begin = end - L
    return make_lex_token(
        type = type
        ,value = t.indent_level
        ,lexpos = begin
        ,lineno = t.lineno + t.num_newlines
        ,lexer = t.lexer
        )




##################################


lex_postprocessor = LexPostprocessor(
            globals()
            , regex_flags=PatternBase.regex_flags
            , START_STATE=START_STATE
            , lex_postprocess_filter=lex_postprocess_filter
            )


if 0 and old and by and LexPostprocessor:
    pseudo_this_module = make_pseudo_lex_module_obj(globals())
    del make_pseudo_lex_module_obj

    def iter_lexers():
        # -> Iter lexer
        #import importlib
        #module = importlib.import_module(__name__)
        module = pseudo_this_module
        lexer = ply.lex.lex(module = module, reflags = PatternBase.regex_flags)
            # I add re.MULTILINE
        lexer.begin(START_STATE)#NOTE!!!!
        while True:
            yield lexer.clone()
    lexers = iter_lexers()
    del iter_lexers

    def iter_parse_source_string(source_string:str):
        it = iter_raw_parse_source_string(source_string)
        return lex_postprocess_filter(it)
    def iter_raw_parse_source_string(source_string:str):
        # str -> Iter Token
        lexer = next(lexers, None)
        lexer.input(source_string)
        lexer.lineno = 1
        yield from lexer
        # why not return iter(lexer)??
        #   since "lexer is iter(lexer)"
        #   output too many information

    def raw_parse_source_string(source_string:str):
        # str -> [Token]
        return list(iter_raw_parse_source_string(source_string))
    def parse_source_string(source_string:str):
        # str -> [Token]
        return list(iter_parse_source_string(source_string))



def main():
    from pprint import pprint
    pseudo_this_module = lex_postprocessor.XXX_pseudo_lex_module
    show_pseudo_lex_module_obj(pseudo_this_module)
if __name__ == "__main__":
    main()
