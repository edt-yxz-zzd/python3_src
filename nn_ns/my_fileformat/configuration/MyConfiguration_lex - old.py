
r'''
#################################################################
WholeFileText
    = IgnoreTailMultiLines0 Repr_TheMainObject IgnoreTailMultiLines0
Repr_TheMainObject
    = Repr_Object<''>
    | '>>> {}:' IgnoreTailMultiLines0 '\n'
        MultiLineRepr_DictBody<''>
    | '>>> ():' IgnoreTailMultiLines0 '\n'
        MultiLineRepr_ListBody<''>
    | '>>> []:' IgnoreTailMultiLines0 '\n'
        MultiLineRepr_ListBody<''>
    | ">>> '':" IgnoreTailMultiLines0 '\n'
        MultiLineRepr_CharStringBody<''>
    | ">>> b'':" IgnoreTailMultiLines0 '\n'
        MultiLineRepr_ByteStringBody<''>



#################################################################
#################################################################
#################################################################
Object = Dict | ObjectArray | ObjectTuple | CharString | ByteString | Fraction | Bool | None
    Dict = Map CharString Object
    ObjectArray = [Object]
    Bool = False | True
    None = None

    CharString
    ByteString
    Fraction


INDENT
DEDENT
'''

from ast import literal_eval
import re


r'''
to distinguish:
    * seperater ',' inside container
    * char/byte-string continuer ', ...'
I introduce two states:
    * inside
    * first
        \A or NEWLINE -> first=True,inside=False
        first + IndentSpaces1 -> first=True
        first + token<ANY|first> -> first=False,inside=True

    inside_OP_ [COMMA/COLON/ASSIGN/DIV]
    first_ [CharStringLine/ByteStringLine]
    first_ IndentSpaces1
    ANY_ NEWLINE/NAME/Integer/RawDictKey
    ANY_OP_ [SMALL_/MIDDLE_/BIG_][OPEN/CLOSE]

    ANY_
        Inline_ByteString
        Inline_CharString
        [OP_/OP_UNINDENT_][CharStringHead/ByteStringHead/ObjectTupleHead/ObjectArrayHead/DictHead]
    first_
        IgnoreLine
    inside_
        Ignores1
        #IgnoreTail1
            merge to NEWLINE=IgnoreTail1? ('[\n\r]+' IgnoreTail1?)+
'''

###################






























t_NEWLINE = r'[\r\n]'
t_OP_COMMA = r','

t_OP_ASSIGN = r'='
t_OP_COLON = r':'

t_OP_DIV = r'/'
t_OP_SMALL_OPEN     = r'(?:\((?!\):))' # (
t_OP_SMALL_CLOSE    = r'\)'
t_OP_MIDDLE_OPEN    = r'(?:\[(?!\]:))' # [
t_OP_MIDDLE_CLOSE   = r'\]'
t_OP_BIG_OPEN       = r'(?:\{(?!\}:))' # {
t_OP_BIG_CLOSE      = r'\}'


    #t_OP_SEMICOLON = r';'
    #t_OP_ESCAPE = r'\\'
    #t_OP_BAR = r'\|'


if False:
    t_OP_ObjectTupleHead    = r'\(\):'
    t_OP_ObjectArrayHead    = r'\[\]:'
    t_OP_DictHead           = r'\{\}:'
    t_OP_CharStringHead     = r"'':"
    t_OP_ByteStringHead     = r"b'':"

    _UNINDENT_HEAD = \
        {">>> {}:": "OP_UNINDENT_DictHead"
        ,">>> []:": "OP_UNINDENT_ObjectArrayHead"
        ,">>> ():": "OP_UNINDENT_ObjectTupleHead"
        ,">>> '':": "OP_UNINDENT_CharStringHead"
        ,">>> b'':": "OP_UNINDENT_ByteStringHead"
        }
    def _insert__UNINDENT_HEAD():
        d = globals()
        for value, name in _UNINDENT_HEAD.items():
            name = f't_{name}'
            d[name] = re.escape(value)
    _insert__UNINDENT_HEAD(); del _insert__UNINDENT_HEAD

#_RESERVED =

_CONSTANTS = \
    {"None": None
    ,"True": True
    ,"False": False
    }

########################################################
#NAME/constants/CONSTANTS
########################################################
def t_NAME(t):
    r'(?ai)(?!\d)\w+(?!\s*=)'
    Nothing = object()
    s = t.value
    may_result = _CONSTANTS.get(s, Nothing)
    if may_result is Nothing:
        raise SyntaxError(f'unknown symbol: line={t.lineno}: {s!r}')

    result = may_result
    t.value = result
    if result is None:
        t.type = 'None'
    elif type(result) is bool:
        t.type = 'Bool'
    else:
        raise logic-error
    return t


########################################################
#Inline_ByteString/Inline_CharString
########################################################
digit = r'[0-9]' # not include [a-f]
xdigit = r'[0-9A-F]' # not include [a-f]
inline_text_byte = r'(?:(?=[\x00-\x7F])[\x20\S])'
    # text_byte = inline_text_byte|'\n'
string_byte = fr'(?:(?![\'\"\\]){inline_text_byte})'
escaped_byte_sequence = fr'(?:\\\\|\\\"|\\\'|\\n|\\r|\\t|\\x{xdigit}{{2}})'
        # exclude '\0'
inline_text_char = r'(?:[\x20\u3000\S])'
    # text_char = inline_text_char|'\n'
string_char = fr'(?:(?![\'\"\\]){inline_text_char})'
escaped_char_sequence = fr'(?:\\\\|\\\"|\\\'|\\n|\\r|\\t|\\x{xdigit}{{2}}|\\u&{xdigit}{{4}};|\\U&{xdigit}{{4}}_{xdigit}{{4}};)'
        # exclude '\0'


def t_Inline_ByteString(t):
    t.value = literal_eval(t.value)
    return t
t_Inline_ByteString.__doc__ = (
    fr"""r?b'(\"|{string_byte}|{escaped_byte_sequence})*'(?!:)"""
    '|'
    fr'''r?b"(\'|{string_byte}|{escaped_byte_sequence})*"(?!:)'''
    )
assert t_Inline_ByteString.__doc__ is not None

def t_Inline_CharString(t):
    t.value = parse_Inline_CharString(t.value)
    return t
t_Inline_CharString.__doc__ = (
    fr"""r?b'(\"|{string_char}|{escaped_char_sequence})*'(?!:)"""
    '|'
    fr'''r?b"(\'|{string_char}|{escaped_char_sequence})*"(?!:)'''
    )
assert t_Inline_CharString.__doc__ is not None


#rex_escaped_char_sequence = re.compile(escaped_char_sequence)
partial_escaped_char_sequence = fr'\\u&{xdigit}{{4}};|\\U&{xdigit}{{4}}_{xdigit}{{4}};'
rex_partial_escaped_char_sequence = re.compile(partial_escaped_char_sequence)
_parse_Inline_CharString__rex_char_to_del = re.compile(r'[&_;]')
def parse_Inline_CharString(s):
    if s[0] == 'r':
        return literal_eval(s)
    ss = s.split(r'\\'); del s

    replace = rex_partial_escaped_char_sequence.sub
    rex_dels = _parse_Inline_CharString__rex_char_to_del.sub
    def repl(m):
        w = m.group(0)
        case = w[1]
        assert case in 'uU'
        # del &_;
        return rex_dels('', w)

    for i in range(len(ss)):
        ss[i] = replace(repl, ss[i])

    s = r'\\'.join(ss)
    return literal_eval(s)

assert parse_Inline_CharString(r"""'\\\n\r\xAAab,"\'\"\x00 \u&11FF;\U&0000_EEFF;'""") == '\\\n\r\xAAab,"\'\"\x00 \u11FF\U0000EEFF'
assert parse_Inline_CharString(r"""r'\\\n\r\xAAab,"\'\"\x00 \u&11FF;\U&0000_EEFF;'""") == r'\\\n\r\xAAab,"\'\"\x00 \u&11FF;\U&0000_EEFF;'

########################################################
###p_ Inline_Fraction
#t_ ignore_IgnoreLine
#t_ Ignores1
#t_ IndentSpaces1
#t_ Integer
########################################################

ignore_char = r'[ ]'
tail_comment = fr"(?:[#][ ]{inline_text_char}*$)" # \# \x23??

# ignore single line
#Ignores0 = fr'{ignore_char}*' = Ignores1?
Ignores1 = fr'(?:{ignore_char}+)'
#IgnoreTail1 = fr'(?:{ignore_char}*{tail_comment}?$)'
IgnoreTail1 = (
    fr'(?:{ignore_char}+{tail_comment}?$)'
    '|'
    fr'(?:{ignore_char}*{tail_comment}$)'
    )
IgnoreLine = fr'(?:^{IgnoreTail1}$)'
t_ignore_IgnoreLine = IgnoreLine
t_Ignores1 = Ignores1

def t_IndentSpaces1(t):
    #'^((?![\r\n])\s)*(?=\S)(?![#])'
    '^(?:(?![\r\n])\s)+(?=\S)(?![#])'


    '^[ ]{4}(?=\S)'
    s = t.value
    if len(s)%4 == 0 and s == ' '*len(s):
        # IndentSpaces1
        return t
    return IndentationError('bad indent: line={t.lineno}: {s!r}')
assert '+' in t_IndentSpaces1.__doc__
assert '*' not in t_IndentSpaces1.__doc__


HexRepr_PInt = fr"(?:0x[_0]*(?![_0])[_{xdigit[1:-1]}]+)" # not "0X"
BinRepr_PInt = fr"(?:0b[_0]*1[_01]*)" # not "0B"
DecRepr_PInt = fr"(?:(?![_0])[0-9]+)"
Repr_PInt = '(?:{})'.format('|'.join(
    [HexRepr_PInt
    ,BinRepr_PInt
    ,DecRepr_PInt
    ]))

Repr_NonZeroInteger = fr"(?:[+-]?{Repr_PInt})" # "-3" not "- 3"
Repr_Zero = "0" # not "-0" "0x0"...
Repr_Integer = fr"(?:{Repr_Zero}|{Repr_NonZeroInteger})"
rex_Repr_Integer = re.compile(Repr_Integer)


def t_Integer(t):
    r'[+-]?[0-9]\w+(?!\s*=)'
    may_i = parse_mayInteger(t.value)
    if may_i is None:
        raise SyntaxError(f'unknown number: line={t.lineno}: {s!r}')

    t.value = may_i
    return t
def parse_mayInteger(s):
    # -> None|int
    m = rex_Repr_Integer.fullmatch(s)
    if m is None:
        return None
    i = literal_eval(s.replace('_', ''))

    #i==0 ==>> s=='0'
    assert i != 0 or s == '0'
    return i

assert parse_mayInteger('0') == 0
assert parse_mayInteger('-1') == -1
assert parse_mayInteger('-0x__1_1') == -0x11
assert parse_mayInteger('+0b__1_1') == 0b11
assert parse_mayInteger('323') == 323
assert parse_mayInteger('0x0') is None

########################################################
###p_ Inline_ObjectArray Inline_ObjectTuple Inline_Dict
#t_OP_*OPEN/t_OP_*CLOSE
#t_OP_COMMA/t_OP_COLON/t_OP_ASSIGN
#t_ RawDictKey
########################################################

# t_RawDictKey vs t_NAME/t_Integer
t_RawDictKey = fr"(?:(?:(?![\'\",:=#(){{}}\[\]\s]){inline_text_char})+(?=\s*=))"


########################################################
###p_ MultiLineRepr_CharStringBody/MultiLineRepr_ByteStringBody
#t_OP_COMMA/t_OP_SEMICOLON/t_OP_ESCAPE/t_OP_BAR
#t_OP_*Head
########################################################
Repr_IndentedEscapedCharString = \
    fr"(?:([\'\"]|{string_char}|{escaped_char_sequence})*$)"
Repr_IndentedEscapedByteString = \
    fr"(?:([\'\"]|{string_byte}|{escaped_byte_sequence})*$)"
CharStringLine = (
    '(?:'
    fr'[;,][ ]{{3}}{inline_text_char}*$'
    '|'
    fr'[|\\][ ]{{3}}{Repr_IndentedEscapedCharString}$'
    '|'
    fr'[|\\;,]$'
    ')'
    )
ByteStringLine = (
    '(?:'
    fr'[;,][ ]{{3}}{inline_text_byte}*$'
    '|'
    fr'[|\\][ ]{{3}}{Repr_IndentedEscapedByteString}$'
    '|'
    fr'[|\\;,]$'
    ')'
    )
rex_CharStringLine = re.compile(CharStringLine)
rex_ByteStringLine = re.compile(ByteStringLine)

# AfterIndent

def t_InCharStringBody_CharStringLine(t):
    r'[|\\;,].*$'
    return _t_InXStringBody_XStringLine(t, is_byte_string=False)
def t_InByteStringBody_ByteStringLine(t):
    r'[|\\;,].*$'
    return _t_InXStringBody_XStringLine(t, is_byte_string=True)

def _t_InXStringBody_XStringLine(t, *, is_byte_string):
    i = is_byte_string = bool(is_byte_string)
    rex_XStringLine = (rex_CharStringLine, rex_ByteStringLine)[i]
    parse_Inline_XString = (parse_Inline_CharString, parse_Inline_ByteString)[i]
    string_type = ('', 'b')[i]
    tp = ('char', 'byte')[i]
    del i

    s = t.value
    may_pair = parse_XStringLine_to_may_xstring_pair(s
        ,rex_XStringLine = rex_XStringLine
        ,parse_Inline_XString=parse_Inline_XString
        ,string_type=string_type
        )

    if may_pair is None:
        raise SyntaxError(f'unknown {tp}-string line format: line={t.lineno}: {s!r}')
    t.value = may_pair
    return t


if 'parse_Inline_ByteString' not in globals():
    parse_Inline_ByteString = literal_eval
def parse_XStringLine_to_may_xstring_pair(s, *
    , rex_XStringLine
        # == rex_CharStringLine | rex_ByteStringLine
    , parse_Inline_XString
        # == parse_Inline_CharString | parse_Inline_ByteString
    , string_type
        # == '' or 'b'
    ):
    # -> None|(str, str)
    # -> None|(bytes, bytes)
    m = rex_XStringLine.fullmatch(s)
    if m is None:
        return None

    case = s[0]
    fst = '\n' if case in '|;' else ''
        # if this is first line
        #   then discard fst
        #   else fst+snd

    t = s[4:]
    if case in ';,':
        # unescaped
        t = 'r{string_type!s}"{t!s}"'
    elif case in '|\\':
        # escaped

        # escape r'"' to r'\"'
        def repl(m):
            s = m.group(0)
            return '\\'+s if len(s) == 1 else s
        t = re.sub(r'\\.|"', repl, t)
        t = '{string_type!s}"{t!s}"'
    else:
        raise logic-error

    snd = parse_Inline_XString(t)
    return fst, snd


#t_OP_*Head

def t_OP_CharStringHead(t):
    r"'':"
    t.lexer.push_state('IntoCharStringBody')
    return t
def t_OP_UNINDENT_CharStringHead(t):
    ">>> '':"
    #t.lexer.push_state('IntoCharStringBody')
    return t
def t_OP_ByteStringHead(t):
    r"b'':"
    t.lexer.push_state('IntoByteStringBody')
    return t
def t_OP_UNINDENT_ByteStringHead(t):
    ">>> b'':"
    #t.lexer.push_state('IntoByteStringBody')
    return t



########################################################
###p_ MultiLineRepr_ListBody/MultiLineRepr_DictBody
#t_OP_*Head
########################################################
def t_OP_ObjectTupleHead(t):
    r'\(\):'
    t.lexer.push_state('IntoListBody')
    return t
def t_OP_UNINDENT_ObjectTupleHead(t):
    r">>> \(\):"
    #t.lexer.push_state('IntoListBody')
    return t
def t_OP_ObjectArrayHead(t):
    r'\[\]:'
    t.lexer.push_state('IntoListBody')
    return t
def t_OP_UNINDENT_ObjectArrayHead(t):
    r">>> \[\]:"
    #t.lexer.push_state('IntoListBody')
    return t


def t_OP_DictHead(t):
    r'\{\}:'
    t.lexer.push_state('IntoDictBody')
    return t
def t_OP_UNINDENT_DictHead(t):
    r">>> \{\}:"
    #t.lexer.push_state('IntoDictBody')
    return t



















########################################################
def _show_t():
    # show t_*
    for name, value in globals().items():
        if name.startswith('t_'):
            print(name)
_show_t()

exclusive = 'exclusive'
inclusive = 'inclusive'
states = dict(
    AfterIndent=inclusive

    # Into* - requires an INDENT!
    ,IntoListBody=inclusive
    ,IntoDictBody=inclusive


    ,IntoByteStringBody=exclusive
    ,IntoCharStringBody=exclusive
    # In* - exclusive
    ,InByteStringBody=exclusive
    ,InCharStringBody=exclusive
    )
states = list(states.items())
tokens = '''
    INDENT
    DEDENT
    NEWLINE

    None
    Bool
    '''.split()
