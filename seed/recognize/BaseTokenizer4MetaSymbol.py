#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/BaseTokenizer4MetaSymbol.py
view ../../python3_src/seed/recognize/Fail.py

seed.recognize.BaseTokenizer4MetaSymbol
py -m nn_ns.app.debug_cmd   seed.recognize.BaseTokenizer4MetaSymbol -x
py -m nn_ns.app.doctest_cmd seed.recognize.BaseTokenizer4MetaSymbol:__doc__ -ht

[[[[[[[
{{{{{{{

>>> def tokenize__str(s, /):
...     return [*base_tokenizer4meta_symbol.tokenize__str(s)]


#>>> tokenize__str(' \t\r\n')
#
#>>> tokenize__str('?!.')
#>>> tokenize__str('?!-')
#>>> tokenize__str('?!,')
#>>> tokenize__str('?!:')
#>>> tokenize__str('?!;')
#
#>>> tokenize__str('?![#...comment...#]')
#>>> tokenize__str('?![]')
#>>> tokenize__str('?![@solidus+41+3000@space]')
#>>> tokenize__str('?![.-,:;]')
#
#>>> tokenize__str('?!')
#>>> tokenize__str('?!()')
#>>> tokenize__str('?!(...)')
#>>> tokenize__str('?!(?!(|))')
#
#>>> tokenize__str(r"""abc 012 -+*!? ~@#$%^&*/-_+=<>|\:;,.  "'` ()[]{}""")
#
#>>> tokenize__str('?!([|)')
#>>> tokenize__str('?!(|)')
#>>> tokenize__str('?!(|])')

#
#
#
#




>>> tokenize__str(' \t\r\n')
[]
>>> tokenize__str('?!.')
[(2, ('char', {'char': '?'}), 3), (3, ('char', {'char': '!'}), 3)]
>>> tokenize__str('?!-')
[(2, ('char', {'char': ' '}), 3)]
>>> tokenize__str('?!,')
[(2, ('char', {'char': '\t'}), 3)]
>>> tokenize__str('?!:')
[(2, ('char', {'char': '\r'}), 3)]
>>> tokenize__str('?!;')
[(2, ('char', {'char': '\n'}), 3)]
>>> tokenize__str('?![#...comment...#]')
[]
>>> tokenize__str('?![]')
[]
>>> tokenize__str('?![.-,:;]')
[(3, ('char', {'char': '?'}), 4), (4, ('char', {'char': '!'}), 4), (4, ('char', {'char': ' '}), 5), (5, ('char', {'char': '\t'}), 6), (6, ('char', {'char': '\r'}), 7), (7, ('char', {'char': '\n'}), 8)]
>>> tokenize__str('?![@solidus+41+3000@space]')
[(3, ('char', {'char': '/'}), 11), (11, ('char', {'char': 'A'}), 14), (14, ('char', {'char': '\u3000'}), 19), (19, ('char', {'char': ' '}), 25)]
>>> tokenize__str('?!')
Traceback (most recent call last):
    ...
seed.recognize.BaseTokenizer4MetaSymbol.BadFormat__eof: 2
>>> tokenize__str('?!()')
[(2, ('meta_char', {'xchars': [_RawChar(2, '(', 3), _RawChar(3, ')', 4)], 'chars': '()'}), 4)]
>>> tokenize__str('?!(...)')
[(2, ('meta_char', {'xchars': [_RawChar(2, '(', 3), _RawChar(3, '.', 4), _RawChar(4, '.', 5), _RawChar(5, '.', 6), _RawChar(6, ')', 7)], 'chars': '(...)'}), 7)]
>>> tokenize__str('?!(?!(|))')
Traceback (most recent call last):
    ...
seed.recognize.BaseTokenizer4MetaSymbol.BadFormat__unexpected_esc: (3, 5)
>>> tokenize__str('?!([|)')
[(2, ('meta_char', {'xchars': [_RawChar(2, '(', 3), _RawChar(3, '[', 4), _RawChar(4, '|', 5), _RawChar(5, ')', 6)], 'chars': '([|)'}), 6)]
>>> tokenize__str('?!(|)')
[(2, ('meta_char', {'xchars': [_RawChar(2, '(', 3), _RawChar(3, '|', 4), _RawChar(4, ')', 5)], 'chars': '(|)'}), 5)]
>>> tokenize__str('?!(|])')
[(2, ('meta_char', {'xchars': [_RawChar(2, '(', 3), _RawChar(3, '|', 4), _RawChar(4, ']', 5), _RawChar(5, ')', 6)], 'chars': '(|])'}), 6)]



>>> tokenize__str(r"""abc 012 -+*!? ~@#$%^&*/-_+=<>|\:;,.  "'` ()[]{}""") == (
... [(0, ('char', {'char': 'a'}), 1)
... , (1, ('char', {'char': 'b'}), 2)
... , (2, ('char', {'char': 'c'}), 3)
... , (3, ('char', {'char': '0'}), 5)
... , (5, ('char', {'char': '1'}), 6)
... , (6, ('char', {'char': '2'}), 7)
... , (7, ('char', {'char': '-'}), 9)
... , (9, ('char', {'char': '+'}), 10)
... , (10, ('char', {'char': '*'}), 11)
... , (11, ('char', {'char': '!'}), 12)
... , (12, ('char', {'char': '?'}), 13)
... , (13, ('char', {'char': '~'}), 15)
... , (15, ('char', {'char': '@'}), 16)
... , (16, ('char', {'char': '#'}), 17)
... , (17, ('char', {'char': '$'}), 18)
... , (18, ('char', {'char': '%'}), 19)
... , (19, ('char', {'char': '^'}), 20)
... , (20, ('char', {'char': '&'}), 21)
... , (21, ('char', {'char': '*'}), 22)
... , (22, ('char', {'char': '/'}), 23)
... , (23, ('char', {'char': '-'}), 24)
... , (24, ('char', {'char': '_'}), 25)
... , (25, ('char', {'char': '+'}), 26)
... , (26, ('char', {'char': '='}), 27)
... , (27, ('char', {'char': '<'}), 28)
... , (28, ('char', {'char': '>'}), 29)
... , (29, ('char', {'char': '|'}), 30)
... , (30, ('char', {'char': '\\'}), 31)
... , (31, ('char', {'char': ':'}), 32)
... , (32, ('char', {'char': ';'}), 33)
... , (33, ('char', {'char': ','}), 34)
... , (34, ('char', {'char': '.'}), 35)
... , (35, ('char', {'char': '"'}), 38)
... , (38, ('char', {'char': "'"}), 39)
... , (39, ('char', {'char': '`'}), 40)
... , (40, ('char', {'char': '('}), 42)
... , (42, ('char', {'char': ')'}), 43)
... , (43, ('char', {'char': '['}), 44)
... , (44, ('char', {'char': ']'}), 45)
... , (45, ('char', {'char': '{'}), 46)
... , (46, ('char', {'char': '}'}), 47)])
True


######################
######################
######################
# recur comment:
#
>>> [*base_tokenizer4meta_symbol.tokenize__str('?![#?!-?![-,:;.+41]666?![#777?![#abc#]888#]999#]')]
[]
>>> [*base_tokenizer4meta_symbol__with_comment.tokenize__str('?![#?!-?![-,:;.+41]666?![#777?![#abc#]888#]999#]')]
[(4, ('comment', {'comment': '?![#  \t\r\n?!.A666?![#777?![#abc#]888#]999#]'}), 48)]

>>> [*base_tokenizer4meta_symbol.tokenize__str('?!(|)')]
[(2, ('meta_char', {'xchars': [_RawChar(2, '(', 3), _RawChar(3, '|', 4), _RawChar(4, ')', 5)], 'chars': '(|)'}), 5)]
>>> [*base_tokenizer4meta_symbol.tokenize__str('?![#?!(|)#]')]
Traceback (most recent call last):
    ...
seed.recognize.BaseTokenizer4MetaSymbol.BadFormat__forbid_mata_char: (4, 6)
>>> [*base_tokenizer4meta_symbol__with_comment.tokenize__str('?![#?!(|)#]')]
Traceback (most recent call last):
    ...
seed.recognize.BaseTokenizer4MetaSymbol.BadFormat__forbid_mata_char: (4, 6)

######################
# recur parenthesis@meta_char:
>>> tokenize__str('?!(())')
[(2, ('meta_char', {'xchars': [_RawChar(2, '(', 3), _RawChar(3, '(', 4), _RawChar(4, ')', 5), _RawChar(5, ')', 6)], 'chars': '(())'}), 6)]
>>> tokenize__str('?!(a(b(c)()(())))')
[(2, ('meta_char', {'xchars': [_RawChar(2, '(', 3), _RawChar(3, 'a', 4), _RawChar(4, '(', 5), _RawChar(5, 'b', 6), _RawChar(6, '(', 7), _RawChar(7, 'c', 8), _RawChar(8, ')', 9), _RawChar(9, '(', 10), _RawChar(10, ')', 11), _RawChar(11, '(', 12), _RawChar(12, '(', 13), _RawChar(13, ')', 14), _RawChar(14, ')', 15), _RawChar(15, ')', 16), _RawChar(16, ')', 17)], 'chars': '(a(b(c)()(())))'}), 17)]

}}}}}}}
#]]]]]]]
#]]]]]
]]]]]]]
#]]]'''
__all__ = r'''

Fail
    ParseFail
    TokenizeFail
        BadFormat

BadFormat
    BadFormat__eof
    BadFormat__char_esc_fmt
    BadFormat__esc_esc
    BadFormat__unknown_meta_char_payload
    BadFormat__forbid_mata_char
    BadFormat__forbid_esc_inside_escaped_chars
    BadFormat__unexpected_esc
    BadFormat__unknown_char_esc_fmt
    BadFormat__unknown_single_char_payload
    BadFormat__unknown_single_char_payload4meta_char

BaseTokenizer4MetaSymbol
    base_tokenizer4meta_symbol
    mk_positioned_chars5text
    mk_positioned_chars5str
    _PosIter
    _RawChar
    _TrueChar
BaseTokenizer4MetaSymbol__with_comment
    base_tokenizer4meta_symbol__with_comment
IterUntilEndMarker
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import pairwise
from unicodedata import lookup as _nm2ch
from seed.iters.PeekableIterator import PeekableIterator, echo_or_mk_PeekableIterator
from seed.tiny_.check import check_type_is, check_pair# check_type_le, check_int_ge
from seed.tiny import fst, snd, ifNone, echo# MapView

from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

######################
from seed.recognize.Fail import Fail, ParseFail, TokenizeFail, BadFormat

######################
BadFormat
class BadFormat__eof(BadFormat):pass
class BadFormat__char_esc_fmt(BadFormat):pass
class BadFormat__esc_esc(BadFormat):pass
class BadFormat__unknown_meta_char_payload(BadFormat):pass
class BadFormat__forbid_mata_char(BadFormat):pass
class BadFormat__forbid_esc_inside_escaped_chars(BadFormat):pass
class BadFormat__unexpected_esc(BadFormat):pass
class BadFormat__unknown_char_esc_fmt(BadFormat):pass
class BadFormat__unknown_single_char_payload(BadFormat):pass
class BadFormat__unknown_single_char_payload4meta_char(BadFormat):pass
######################



def mk_positioned_chars5text(position_info, text, /):
    '(lineno, columno) -> Iter char -> positioned_chars'
    check_pair(position_info)
    (lineno, columno) = position_info
    check_type_is(int, lineno)
    check_type_is(int, columno)
    it = echo_or_mk_PeekableIterator(text)
    #_4newline
    for ch in it:
        if ch == '\r':
            if not it.is_empty() and it.head == '\n':
                next(it)
            ch = '\n'
        #####
        if ch == '\n':
            lineno += 1
            columno = 0 #<<==newline.end_position_info
        else:
            columno += 1
        yield ch, (lineno, columno)
def mk_positioned_chars5str(position_info, s, /):
    'idx -> Iter char -> positioned_chars'
    check_type_is(int, position_info)
    j = position_info
    it = ((c,j) for j,c in enumerate(s, 1+j))
    return it

class _RawChar:
    raw_vs_true = False
    @property
    def char(sf, /):
        return sf._ch
    @property
    def xchar(sf, /):
        '-> (raw_vs_true, char)'
        return (False, sf._ch)

    def __repr__(sf, /):
        ch = sf._ch
        (prev_p, p) = sf._span
        return repr_helper(sf, prev_p, ch, p)
    def __init__(sf, prev_p, ch, p, /):
        sf._ch = ch
        sf._span = (prev_p, p)
    @property
    def span(sf, /):
        return sf._span
class _TrueChar:
    raw_vs_true = True
    @property
    def char(sf, /):
        return sf._ch
    @property
    def xchar(sf, /):
        '-> (raw_vs_true, char)'
        return (True, sf._ch)

    def __repr__(sf, /):
        return repr_helper(sf, sf._ch_tkn)
    def __init__(sf, ch_tkn, /):
        sf._ch_tkn = ch_tkn
        (prev_p, (tkey, tdat), p) = ch_tkn
        assert tkey == 'char'
        sf._ch = tdat['char']
    @property
    def char_token(sf, /):
        return sf._ch_tkn

class _PosIter:
    def __init__(sf, position_info, positioned_xs, /, *, key):
        'positioned_xs -> Iter (x, position_info) -> None'
        sf._p = position_info
        sf._it = iter(positioned_xs)
        sf._f = key
        sf._tm = []
        sf._eof = False
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        tm = sf._tm
        if tm:
            item = tm.pop()
            [] = tm
        else:
            item = next(sf._it)
        sf._p = sf._f(item)
        return item
    @property
    def eof(sf, /):
        if sf._eof:
            return True
        if sf._tm:
            return False
        try:
            sf.head
        except StopIteration:
            sf._eof = True
        return sf.eof
    @property
    def head(sf, /):
        tm = sf._tm
        if not tm:
            item = next(sf._it)
            tm.append(item)
        [item] = tm
        return item
    @property
    def position_info(sf, /):
        return sf._p
_4single = (
{'.':'?!'
,'-':' '
,':':'\r'
,';':'\n'
,',':'\t'
})
class BaseTokenizer4MetaSymbol:
    r'''[[[
LL1
[[
format:
    ignore spaces
    the only spec_char:『?!』
    text_substitute:
        『?!.』 --> 『?!』
        『?!-』 --> 『 』
        『?!,』 --> 『\t』
        『?!:』 --> 『\r』
        『?!;』 --> 『\n』
        『?![』item4substitute* 『]』 --> unescaped_chars
            item4substitute:
                『+』\x+ --> chr(...)
                『@』\w+ --> unicodedata.lookup(...)
                [-,:;.] --> same as above
    recursive_comment:
        『?![#』item4comment* 『#]』 --> comment
            [comment :: str{『?!.』,『?![#...#]』,no other spec_chars,spaces are not ignorable}]
                ==>> escape 『?!』-->『?!.』
            item4comment:
                recursive_comment
                substituted_char
                raw_char but not form 『#]』
    usrdefined-meta_char:
        『?!(』item4meta_char* 『)』 --> meta_char
            item4meta_char:
                recursive_comment
                recursive:『(』item4meta_char* 『)』
                substituted_char
                raw_char but not form 『)』
]]
[[
datatype:
    [positioned_chars :: Iter (char, position_info)]
    [token :: (position_info, (tkey/str, tdat/dict), position_info)]
        [char_tkn :: (position_info, (tkey:='char', tdat:={'char':char}), position_info)]
        [comment_tkn :: (position_info, (tkey:='comment', tdat:={'comment':comment}), position_info)]
            [comment :: str{『?!.』,『?![#...#]』,no other spec_chars,spaces are not ignorable}]
        [usrdefined-meta_char_tkn :: ???]
            to be overrided:[meta_char_tkn :: (position_info, (tkey:='meta_char', tdat:={'xchars':xchars/[(_RawChar|_TrueChar)], 'chars':chars/str}), position_info)]
]]

    #]]]'''#'''
    _to_output_comment_ = False
    def tokenize__text(sf, text, position_info=(1,1), /):
        positioned_chars = mk_positioned_chars5text(position_info, text)
        return sf.tokenize(position_info, positioned_chars)
    def tokenize__str(sf, s, position_info=0, /):
        positioned_chars = mk_positioned_chars5str(position_info, s)
        return sf.tokenize(position_info, positioned_chars)
    def tokenize(sf, position_info, positioned_chars, /):
        'position_info -> Iter (char, position_info) -> Iter token/(position_info, (tkey/str, tdat/dict), position_info)/(usrdefined-meta_char_tkn|char_tkn|comment_tkn)'
        positioned_maychars = sf.preprocess(positioned_chars)
        pr_positioned_maychars = _PosIter(position_info, positioned_maychars, key=snd)
        positioned_emay_may_rawXtrue_chars = sf.substitute_true_chars(pr_positioned_maychars)
        pr_positioned_emay_may_rawXtrue_chars = _PosIter(position_info, positioned_emay_may_rawXtrue_chars, key=snd)
        positioned_may_rawXtrue_charXcomments = sf.recognize_comment(pr_positioned_emay_may_rawXtrue_chars, may_outs=None)
        pr_positioned_may_rawXtrue_charXcomments = _PosIter(position_info, positioned_may_rawXtrue_charXcomments, key=snd)
        iter_metaXcharXcomments = sf.recognize_meta_char(pr_positioned_may_rawXtrue_charXcomments)
        return iter_metaXcharXcomments
    ######################
    ######################
    ######################
    def preprocess(sf, positioned_chars, /):
        'Iter (char, position_info) -> Iter (may char, position_info)'
        positioned_chars = sf.denoise(positioned_chars)
        positioned_maychars = sf.cut(positioned_chars)
        return positioned_maychars
    def cut(sf, positioned_chars, /):
        'Iter (char, position_info) -> Iter (may char, position_info)'
        it = iter(positioned_chars)
        f = _4prefix.iter_until_end_marker
        while 1:
            may_prefix = yield from f(it, key=fst, eof_ok=True)
            if may_prefix:
                # '?!' --> (None, p)
                prefix = may_prefix
                match prefix:
                    case [('?', _), ('!', p)]:
                        pass
                    case _:
                        raise 000
                yield None, p
            else:
                # None @eof
                assert may_prefix is None
                break
        return
        ######################
    def denoise(sf, positioned_chars, /):
        'Iter (char, position_info) -> Iter (char, position_info)'
        for (ch, p) in positioned_chars:
            if not ch.isspace():
                yield (ch, p)




    ######################
    ######################
    ######################
    def substitute_true_chars(sf, pr_positioned_maychars, /):
        '_PosIter (may char, position_info) -> Iter (emay may (raw_char|true_char), position_info) | ^BadFormat__... | ^BadFormat__eof'
        #raw_char == _RawChar(char)
        #true_char == _TrueChar(char_token)
        it = pr_positioned_maychars
        prev_p = it.position_info
        for m, p in it:
            if m is None:
                yield from sf.on_substitute_true_chars(it)
            else:
                ch = m
                yield (_RawChar(prev_p, ch, p), p)
            prev_p = it.position_info
        return
    def on_substitute_true_chars(sf, pr_positioned_maychars, /):
        '_PosIter (may char, position_info) -> Iter (emay may (raw_char|true_char), position_info) | ^BadFormat__... | ^BadFormat__eof'
        it = pr_positioned_maychars
        prev_p = it.position_info
        (m, p) = sf._read1(it)
            # ^BadFormat__eof
        if m is None:
            raise BadFormat__esc_esc(p)
        ch = m
        if not ch == '[':
            if ch in _4single:
                for char_tkn in sf.iter_escaped_char_tokens5single_char_payload(prev_p, ch, p):
                    yield (_TrueChar(char_tkn), char_tkn[-1])
                return
            yield (None, prev_p)
            yield (_RawChar(prev_p, ch, p), p)
            return
        else:
            (m, _p) = sf._peek1(it)
                # ^BadFormat__eof
            if m == '#':
                sf._read1(it)
                yield (..., _p) #comment_header
                return
        for ch_tkn in sf.iter_escaped_char_tokens5long_payload(it):
            #(prev_p, (tkey, tdat), p) = ch_tkn
            yield (_TrueChar(ch_tkn), ch_tkn[-1])
        return
    def _read1(sf, it, /):
        for x in it:
            return x
        raise BadFormat__eof(it.position_info)
    def _peek1(sf, it, /):
        if it.eof:
            raise BadFormat__eof(it.position_info)
        return it.head

    def iter_escaped_char_tokens5long_payload(sf, it, /):
        prev_p = it.position_info
        (m, p) = sf._read1(it)
            # ^BadFormat__eof
        if m == '#':
            raise 000
        while 1:
            prev_p, (m, p), it
            if m is None:
                raise BadFormat__forbid_esc_inside_escaped_chars(prev_p, p)
            ch = m
            if ch == ']':
                prev_p = p
                break
            if ch in _4single:
                yield from sf.iter_escaped_char_tokens5single_char_payload(prev_p, ch, p)
                prev_p = p
                (m, p) = item = sf._read1(it)
                prev_p, (m, p), it
                continue
            if not ch in '+@':
                raise BadFormat__unknown_char_esc_fmt(prev_p, ch, p)
            s = sf._greedy_reads_ex(lambda c:c=='_' or c.isalnum(), it)
                #str.isidentifier
                #str.isalnum
                # ^BadFormat__eof...
            if not s:
                raise BadFormat__char_esc_fmt(prev_p, ch, p, s)
            _prev_p = it.position_info
            try:
                if ch == '+':
                    _ch = chr(int(s, 16))
                elif ch == '@':
                    _ch = _nm2ch(s)
                else:
                    raise 000
            except Exception:
                raise BadFormat__char_esc_fmt(prev_p, ch, p, s, _prev_p)
            _ch
            # ((ch, p), s) --> _ch
            # (prev_p, (ch, p), s, it)
            # --> (prev_p, _ch, it)
            yield sf.mk_token4char(prev_p, _ch, _prev_p)
            prev_p = _prev_p
            (m, p) = item = sf._read1(it)
            prev_p, (m, p), it
        return
    def _greedy_reads_ex(sf, char2ok_, it, /):
        '-> str'
        cs = []
        while 1:
            (m, p) = x = sf._peek1(it)
                # ^BadFormat__eof
            if m is None:
                raise BadFormat__unexpected_esc(it.position_info, p)
            ch = m
            if not char2ok_(ch):
                cs = ''.join(cs)
                return cs
            sf._read1(it)
            cs.append(ch)
    def iter_escaped_char_tokens5single_char_payload(sf, prev_p, ch, p, /):
        try:
            txt = _4single[ch]
        except KeyError:
            raise BadFormat__unknown_single_char_payload(prev_p, ch, p)
        for _ch in txt:
            yield sf.mk_token4char(prev_p, _ch, p)
            prev_p = p
        return

    def mk_token4comment(sf, begin_position_info, comment, end_position_info, /):
        return sf.mk_token(begin_position_info, 'comment', end_position_info, comment=comment)
    def mk_token4char(sf, begin_position_info, char, end_position_info, /):
        return sf.mk_token(begin_position_info, 'char', end_position_info, char=char)
    def mk_token(sf, begin_position_info, tkey, end_position_info, /, **tdat):
        '-> token/(position_info, (tkey/str, tdat/dict), position_info)'
        check_type_is(str, tkey)
        return (begin_position_info, (tkey, tdat), end_position_info)




    ######################
    ######################
    ######################
    def recognize_comment(sf, pr_positioned_emay_may_rawXtrue_chars, /, *, may_outs):
        '_PosIter (emay may (raw_char|true_char), position_info) -> Iter (may (raw_char|true_char|comment_tkn), position_info) | ^BadFormat__... | ^BadFormat__eof'
        it = pr_positioned_emay_may_rawXtrue_chars
        for x in it:
            m, p = x
            if m is ...:
                for comment_tkn in sf.iter_comment_tokens5long_payload(it, may_outs=may_outs):
                    yield comment_tkn, comment_tkn[-1]
                continue
            yield x
        return
    def iter_comment_tokens5long_payload(sf, pr_positioned_emay_may_rawXtrue_chars, /, *, may_outs):
        '-> (Iter comment_tkn){len<2}'
        it = pr_positioned_emay_may_rawXtrue_chars
        p0 = it.position_info
        p = p0
        b = sf._to_output_comment_
        ss = ifNone(may_outs, []) if b else None
        assert b is (ss is not None)
        toplvl = ss is not None is may_outs
        #if b and not toplvl:
        if b:
            ss.append('?![#')
        ch_ = '' # '' or raw-'#'
        positioned_may_rawXtrue_charXcomments = sf.recognize_comment(pr_positioned_emay_may_rawXtrue_chars, may_outs=ss)
        for item in positioned_may_rawXtrue_charXcomments:
            prev_p = p
            x, p = item
            if x is None:
                raise BadFormat__forbid_mata_char(prev_p, p)
            if type(x) is tuple:
                comment_tkn = x
                assert x[1][0] == 'comment'
                raise 000#exported-via-ss/may_outs

            assert type(x) in (_RawChar, _TrueChar)
            is_raw = not x.raw_vs_true
            ch = x.char
            if is_raw:
                if ch == '#':
                    ch_ = '#' # save
                elif ch == ']':
                    if ch_ == '#':
                        break
                else:
                    ch_ = ''
            else:
                ch_ = ''

            if b:
                ss.append(ch)
        else:
            raise BadFormat__eof(p)
        assert is_raw
        assert ch == ']'
        assert ch_ == '#'
        if b:
            assert ss
            assert ss[-1] == '#'
            ss.pop()
        #if b and not toplvl:
        if b:
            ss.append('#]')
        if b and toplvl:
            def __(ss, /):
                if ss:
                    yield ss[0]
                for a, b in pairwise(ss):
                    yield b
                    if a == '?' and b == '!':
                        yield '.'
            comment = ''.join(__(ss))
            comment_tkn = sf.mk_token4comment(p0, comment, p)
            yield comment_tkn
        return


    ######################
    ######################
    ######################
    def recognize_meta_char(sf, pr_positioned_may_rawXtrue_charXcomments, /):
        '_PosIter (may (raw_char|true_char|comment_tkn), position_info) -> Iter (usrdefined-meta_char_tkn|char_tkn|comment_tkn) | ^BadFormat__... | ^BadFormat__eof'
        #-> iter_metaXcharXcomments
        it = pr_positioned_may_rawXtrue_charXcomments
        p = it.position_info
        for item in it:
            p_ = p
            m, p = item
            if m is None:
                yield from sf.iter_meta_char_tokens5payload(it)
                    #usrdefined-meta_char_tkn
                continue
            x = m
            T = type(x)
            if T is tuple:
                comment_tkn = x
                assert x[1][0] == 'comment'
                yield comment_tkn
                continue
            assert T in (_RawChar, _TrueChar)
            if not x.raw_vs_true:
                #raw_char
                ch = x.char
                (p_, p) = x.span
                char_tkn = sf.mk_token4char(p_, ch, p)
            else:
                #true_char
                char_tkn = x.char_token
            yield char_tkn

        return
    def iter_meta_char_tokens5single_char_payload(sf, prev_p, ch, p, /):
        '-> Iter (usrdefined-meta_char_tkn) | ^BadFormat__...'
        raise BadFormat__unknown_single_char_payload4meta_char(prev_p, ch, p)
    def iter_meta_char_tokens5payload(sf, it, /):
        '_PosIter (may (raw_char|true_char|comment_tkn), position_info) -> Iter (usrdefined-meta_char_tkn) | ^BadFormat__... | ^BadFormat__eof'
        p0 = prev_p = it.position_info
        (m, p) = x = sf._read1(it)
            # ^BadFormat__eof
        p1 = p
        check_type_is(_RawChar, m)
        xch = m
        if not xch.xchar == (False, '('):
            yield from sf.iter_meta_char_tokens5single_char_payload(prev_p, ch, p)
            return

        #_greedy_reads_ex
        xs = [xch]
            # include: 『()』
        num_lparenthesis = 0
            # recur parenthesis@meta_char:
        while 1:
            prev_p = p
            (m, p) = item = sf._read1(it)
                # ^BadFormat__eof
            if m is None:
                raise BadFormat__unexpected_esc(prev_p, p)
            x = m
            T = type(x)
            if T is tuple:
                comment_tkn = x
                assert x[1][0] == 'comment'
                #raise BadFormat__forbid_comment_inside_meta_char
                #discard: #yield comment_tkn
                continue
            assert T in (_RawChar, _TrueChar)
            ch = x.char
            xs.append(x)
                # include: 『()』
            if not x.raw_vs_true:
                #raw_char
                if ch == ')':
                    if num_lparenthesis == 0:
                        pz = prev_p
                        break
                    num_lparenthesis -= 1
                    #bug:continue
                elif ch == '(':
                    #raise BadFormat__unexpected_left_parenthesis_inside_meta_char
                    num_lparenthesis += 1
                    #bug:continue
                else:
                    pass
            else:
                #true_char
                pass
            #xs.append(x)
        cs = ''.join(x.char for x in xs)
        meta_char_tkns = sf._iter_customize_meta_char_tokens_(p0, xs, cs, p)
            # include: 『()』
        #meta_char_tkns = sf._iter_customize_meta_char_tokens_(p1, xs, cs, pz)
            # exclude: 『()』
        yield from meta_char_tkns
        return
    def _iter_customize_meta_char_tokens_(sf, begin_position_info, xchars, chars, end_position_info, /):
        'position_info -> xchars/[(_RawChar|_TrueChar){.raw_vs_true,.char,(.span|.char_token)}] -> chars/str{len=len(xchars)} -> position_info -> Iter usrdefined-meta_char_tkn #to be overrided'
        assert xchars
        assert len(xchars) == len(chars)
        assert chars[0] == '('
        assert chars[-1] == ')'
        yield sf.mk_token(begin_position_info, 'meta_char', end_position_info, xchars=xchars, chars=chars)

    ######################
    ######################
    ######################
#end-class BaseTokenizer4MetaSymbol:
class BaseTokenizer4MetaSymbol__with_comment(BaseTokenizer4MetaSymbol):
    #@override
    _to_output_comment_ = True
base_tokenizer4meta_symbol = BaseTokenizer4MetaSymbol()
base_tokenizer4meta_symbol__with_comment = BaseTokenizer4MetaSymbol__with_comment()

class IterUntilEndMarker:
    def __init__(sf, end_marker, /):
        if not end_marker:raise ValueError
        if end_marker[0] in end_marker[1:]:raise ValueError
        sf._ls = end_marker
    def iter_until_end_marker(sf, iterable, /, *, key=None, eof_ok=False):
        'Iter x -> (Iter x){return-may [x]~=~end_marker}'
        key = ifNone(key, echo)
        ls = sf._ls
        sz = len(ls)
        prevs = []
        assert sz
        for x in iterable:
            #assert sz
            #assert sz + len(prevs) == len(ls)
            k = key(x)
            if k == ls[len(prevs)]:
                prevs.append(x)
                sz -= 1
                if not sz:
                    #assert len(prevs) == len(ls)
                    return prevs
                continue
            if prevs:
                #flush
                yield from prevs
                prevs.clear()
                sz = len(ls)
            #assert not prevs
            yield x
        else:
            #eof
            #assert sz
            if prevs:
                #flush
                yield from prevs
                prevs.clear()
            #assert not prevs
        #assert not prevs
        #assert sz
        if not eof_ok:
            raise BadFormat__eof
        return None
#end-class IterUntilEndMarker:
_4newline = IterUntilEndMarker('\r\n')
_4prefix = IterUntilEndMarker('?!')
__all__




__all__
from seed.recognize.BaseTokenizer4MetaSymbol import BaseTokenizer4MetaSymbol, BaseTokenizer4MetaSymbol__with_comment
from seed.recognize.BaseTokenizer4MetaSymbol import *
