
__all__ = '''
    parse_Inline_CharString
    parse_Inline_ByteString
    parse_ByteStringBodyLine
    parse_CharStringBodyLine
    '''.split()

import re
from ast import literal_eval
xdigit = '[0-9A-F]'
partial_escaped_char_sequence = fr'\\u&{xdigit}{{4}};|\\U&{xdigit}{{4}}_{xdigit}{{4}};'
rex_partial_escaped_char_sequence = re.compile(partial_escaped_char_sequence)
_parse_Inline_CharString__rex_char_to_del = re.compile(r'[&_;]')
def parse_raw_Inline_XString(s):
    # -> str|bytes
    if s[0] != 'r': raise ValueError
    # old_version: return literal_eval(s)

    assert s[-1] in "\"'"
    if s[-2] != '\\':
        return literal_eval(s)
    A, B = s[:-1], s[-1:]
    r0 = literal_eval(f'{A}0{B}')
    return r0[:-1]

def parse_Inline_CharString(s):
    if s[0] == 'r':
        return parse_raw_Inline_XString(s)
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
    try:
        return literal_eval(s)
    except:
        print(s)
        print(repr(s))
        raise

assert parse_Inline_CharString(r"""'\\\n\r\xAAab,"\'\"\x00 \u&11FF;\U&0000_EEFF;'""") == '\\\n\r\xAAab,"\'\"\x00 \u11FF\U0000EEFF'
assert parse_Inline_CharString(r"""r'\\\n\r\xAAab,"\'\"\x00 \u&11FF;\U&0000_EEFF;'""") == r'\\\n\r\xAAab,"\'\"\x00 \u&11FF;\U&0000_EEFF;'

#old_version: parse_Inline_ByteString = literal_eval
def parse_Inline_ByteString(s):
    if s[0] == 'r':
        return parse_raw_Inline_XString(s)
    return literal_eval(s)
def parse_ByteStringBodyLine(s):
    return _parse_XStringBodyLine_to_xstring_pair(s, is_byte_string=True)
def parse_CharStringBodyLine(s):
    return _parse_XStringBodyLine_to_xstring_pair(s, is_byte_string=False)
def _parse_XStringBodyLine_to_xstring_pair(s, *, is_byte_string:bool):
    i = is_byte_string = bool(is_byte_string)
    parse_Inline_XString = (parse_Inline_CharString, parse_Inline_ByteString)[i]
    string_type = ('', 'b')[i]
    del i

    fst, snd = __parse_XStringBodyLine_to_xstring_pair(s
        ,parse_Inline_XString=parse_Inline_XString
        ,string_type=string_type
        )
    return fst, snd

def __parse_XStringBodyLine_to_xstring_pair(s, *
    , parse_Inline_XString
        # == parse_Inline_CharString | parse_Inline_ByteString
    , string_type
        # == '' or 'b'
    ):
    # -> (str, str) | (bytes, bytes)
    assert string_type in 'b'

    case = s[0]
    assert case in r'|\;,'
    fst = '\n' if case in '|;' else ''
        # if this is first line
        #   then discard fst
        #   else fst+snd

    t = s[4:]
    if case in ';,':
        # unescaped
        if string_type == '':
            snd = t
        else:
            snd = t.encode('ascii')
    elif case in r'\|':
        # escaped

        # escape r'"' to r'\"'
        #   "'" may or may not escaped
        #   '\\' is escaped
        #   we only take care of '"'
        def repl(m):
            s = m.group(0)
            return '\\'+s if len(s) == 1 else s
        t = re.sub(r'\\.|"', repl, t)
        t = f'{string_type!s}"{t!s}"'
        snd = parse_Inline_XString(t)
    else:
        raise logic-error
    return fst, snd

