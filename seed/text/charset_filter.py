#HHHHH
r"""
basic_charset_filter
    = charset
    | encoding
    | ord -> bool
    | is_normalized, form
    | (regex | str->bool), (
        | name, default
        | normalize, form
        | category
        | bidirectional
        | decomposition
        )
form = NFC | NFKC | NFD | NFKD
    #unicodedata
charset = char_ord_rngs
    see: seed.data_funcs.rngs

charset_filter
    = charset_filter
    | not charset_filter
    | charset_filter op charset_filter
op = or | and | xor | exclude




see:
    view ../../python3_src/seed/text/charset_filter.py
    view ../../python3_src/seed/text/mk_char_pt_ranges5predicator.py


usage:
    printable_ascii_gb2312_char_pt_ranges = ((EncodingCharFilter('ascii') | EncodingCharFilter('gb2312')) & the_printable_char_filter).to_NonTouchRanges()


py -m nn_ns.app.debug_cmd   seed.text.charset_filter
py -m seed.text.charset_filter -i U

from seed.text.charset_filter import (
    ICharFilter
        ,ICharPredicatorCharFilter
        ,IBinOpCharFilter
)
from seed.text.charset_filter import (
        EncodingCharFilter
        ,CharsetCharFilter
        ,CharNameRegexCharFilter
        ,CharPredicatorCharFilter
)
from seed.text.charset_filter import (
    the_space_char_filter
    ,the_printable_char_filter
        ,the_identifier_char_filter
            ,the_alpha_numeric_char_filter
                ,the_alpha_char_filter
                    ,the_lower_char_filter
                    ,the_upper_char_filter
                ,the_numeric_char_filter
                    ,the_digit_char_filter
                        ,the_decimal_char_filter
)


#"""

#################################
#HHHHH
__all__ = '''
    unicode_begin
    unicode_end
    unicode_rngs

    ICharFilter
        EncodingCharFilter
        CharsetCharFilter
        CharNameRegexCharFilter
        CharPredicatorCharFilter
        ICharPredicatorCharFilter
            PrintableCharFilter
                the_printable_char_filter
            SpaceCharFilter
                the_space_char_filter
            IdentifierCharFilter
                the_identifier_char_filter
            AlphaNumericCharFilter
                the_alpha_numeric_char_filter
            AlphaCharFilter
                the_alpha_char_filter
            LowerCharFilter
                the_lower_char_filter
            UpperCharFilter
                the_upper_char_filter
            NumericCharFilter
                the_numeric_char_filter
            DigitCharFilter
                the_digit_char_filter
            DecimalCharFilter
                the_decimal_char_filter

    encoding2char_key_func4sort
    sort_chars_by_encoding

        IBinOpCharFilter
            OrCharFilter
            AndCharFilter
            XorCharFilter
            ExcludeCharFilter
    E
    R
    N
    U
    main
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
import codecs
import re
import unicodedata
from abc import ABC, abstractmethod
from seed.data_funcs.rngs import (
    make_Ranges
    ,sorted_unique_ints_to_iter_nontouch_ranges
    )
from seed.data_funcs.rngs import NonTouchRanges
from seed.helper.repr_input import repr_helper
from seed.helper.safe_eval import safe_eval
___end_mark_of_excluded_global_names__0___ = ...




#################################
#HHHHH
unicode_begin = 0
unicode_end = 0x11_0000
unicode_rngs = make_Ranges([(0, 0x11_0000)])
class ICharFilter(ABC):
    @abstractmethod
    def _get_init_args(self, /):
        raise NotImplementedError
    @abstractmethod
    def _is_good_char_ord(self, char_ord, /):
        raise NotImplementedError
    def is_good_char_ord(self, char_ord, /):
        return self._is_good_char_ord(char_ord)
    def iter_sorted_good_char_ords(self, /):
        return filter(self.is_good_char_ord, unicode_rngs.iter_ints())
    def iter_nontouch_ranges(self, /):
        return sorted_unique_ints_to_iter_nontouch_ranges(self.iter_sorted_good_char_ords())
    def iter_sorted_good_chars(self, /):
        return map(chr, self.iter_sorted_good_char_ords())
    def sort_all_good_chars_by_encoding(self, encoding, /):
        return sort_chars_by_encoding(encoding, self.iter_sorted_good_chars())
    def to_NonTouchRanges(self, /):
        rngs = self.iter_nontouch_ranges()
        nontouch_ranges = make_Ranges(rngs)
        assert type(nontouch_ranges) is NonTouchRanges
        return nontouch_ranges
    def to_CharsetCharFilter(self, /):
        rngs = self.iter_nontouch_ranges()
        return CharsetCharFilter(rngs)
    def __repr__(self, /):
        args = self._get_init_args()
        return repr_helper(self, *args)

    def __or__(self, other, /):
        return OrCharFilter(self, other)
    def __and__(self, other, /):
        return AndCharFilter(self, other)
    def __xor__(self, other, /):
        return XorCharFilter(self, other)
    def __sub__(self, other, /):
        return ExcludeCharFilter(self, other)

class EncodingCharFilter(ICharFilter):
    def __init__(self, encoding, /):
        self.__codec_info = codecs.lookup(encoding)
    @property
    def encoding(self, /):
        return self.__codec_info.name
    def _get_init_args(self, /):
        return (self.encoding,)
    def _is_good_char_ord(self, char_ord, /):
        try:
            self.__codec_info.encode(chr(char_ord))
        except UnicodeEncodeError:
            return False
        else:
            return True
    def sort_all_good_chars_by_encoding(self, encoding=None, /):
        if encoding is None:
            encoding = self.encoding
        return super().sort_all_good_chars_by_encoding(encoding)

class CharsetCharFilter(ICharFilter):
    def __init__(self, xtouch_ranges, /):
        self.__rngs = make_Ranges(xtouch_ranges)
    @property
    def ranges(self, /):
        return self.__rngs.ranges
    def len(self, /):
        return self.__rngs.len_ints()
    def _get_init_args(self, /):
        return (self.ranges,)
    def _is_good_char_ord(self, char_ord, /):
        return char_ord in self.__rngs

class CharNameRegexCharFilter(ICharFilter):
    def __init__(self, pattern_or_regex, /):
        if isinstance(pattern_or_regex, str):
            pattern = pattern_or_regex
            regex = re.compile(pattern)
        else:
            regex = pattern_or_regex
        self.__rex = regex
    @property
    def pattern(self, /):
        return self.__rex.pattern
    def _get_init_args(self, /):
        return (self.pattern,)
    def _is_good_char_ord(self, char_ord, /):
        char = chr(char_ord)
        may_char_name = unicodedata.name(char, '')
        m = self.__rex.search(may_char_name)
        return m is not None

class CharPredicatorCharFilter(ICharFilter):
    'bad: repr()'
    def __init__(self, char_predicator, /):
        if not callable(char_predicator): raise TypeError(char_predicator)
        self.__pred = char_predicator
    @property
    def char_predicator(self, /):
        return self.__pred
    def _get_init_args(self, /):
        return (self.char_predicator,)
    def _is_good_char_ord(self, char_ord, /):
        char = chr(char_ord)
        b = self.__pred(char)
        if not type(b) is bool: raise TypeError(b)
        return b



class ICharPredicatorCharFilter(ICharFilter):
    'ICharPredicatorCharFilter vs CharPredicatorCharFilter: better look repr()'
    @staticmethod
    @abstractmethod
    def ___char_predicator___(char, /):
        'char -> bool'
        raise NotImplementedError

    def __new__(cls, /):
        while not hasattr(cls, '___the_self___'):
            cls.___the_self___ = super(__class__, cls).__new__(cls)
        sf = cls.___the_self___
        if type(sf) is not cls: raise TypeError
        return sf
    def __init__(self, /):
        return
    def _get_init_args(self, /):
        return ()
    def _is_good_char_ord(self, char_ord, /):
        char = chr(char_ord)
        b = type(self).___char_predicator___(char)
        if not type(b) is bool: raise TypeError(b)
        return b


# %s/class \(\w\+\)CharFilter(ICharPredicatorCharFilter):/\0\rthe_\1_char_filter = \1CharFilter()
class PrintableCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = str.isprintable
the_printable_char_filter = PrintableCharFilter()
class SpaceCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = str.isspace
the_space_char_filter = SpaceCharFilter()

class IdentifierCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = lambda ch,/:str.isidentifier('_'+ch)
the_identifier_char_filter = IdentifierCharFilter()
class AlphaNumericCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = str.isalnum
the_alpha_numeric_char_filter = AlphaNumericCharFilter()

class AlphaCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = str.isalpha
the_alpha_char_filter = AlphaCharFilter()
class LowerCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = str.islower
the_lower_char_filter = LowerCharFilter()
class UpperCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = str.isupper
the_upper_char_filter = UpperCharFilter()

class NumericCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = str.isnumeric
the_numeric_char_filter = NumericCharFilter()
class DigitCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = str.isdigit
the_digit_char_filter = DigitCharFilter()
class DecimalCharFilter(ICharPredicatorCharFilter):
    ___char_predicator___ = str.isdecimal
the_decimal_char_filter = DecimalCharFilter()



assert the_printable_char_filter is PrintableCharFilter()



#################################
#HHHHH
def encoding2char_key_func4sort(encoding, /):
    encode = codecs.lookup(encoding).encode
    def char_key_func(char, /):
        assert len(char) == 1
        bs = encode(char)
        return len(bs), bs
    return char_key_func

def sort_chars_by_encoding(encoding, chars, /):
    key = encoding2char_key_func4sort(encoding)
    return ''.join(sorted(chars, key=key))








#################################
#HHHHH
class IBinOpCharFilter(ICharFilter):
    @abstractmethod
    def _bool_bin_op(self, fa, fb, /):
        raise NotImplementedError
    @abstractmethod
    def _get_op_str(self, /):
        raise NotImplementedError
    def __repr__(self, /):
        lhs, rhs = self._get_init_args()
        op = self._get_op_str()
        return f"({lhs!r} {op!s} {rhs!r})"
    def __init__(self, lhs_char_filter, rhs_char_filter, /):
        self.__lhs = lhs_char_filter
        self.__rhs = rhs_char_filter
    def _get_init_args(self, /):
        return (self.__lhs, self.__rhs)
    def _is_good_char_ord(self, char_ord, /):
        fa = lambda:bool(self.__lhs.is_good_char_ord(char_ord))
        fb = lambda:bool(self.__rhs.is_good_char_ord(char_ord))
        return bool(self._bool_bin_op(fa, fb))
class OrCharFilter(IBinOpCharFilter):
    def _bool_bin_op(self, fa, fb, /):
        return bool(fa()) or bool(fb())
    def _get_op_str(self, /):
        return '|'
class AndCharFilter(IBinOpCharFilter):
    def _bool_bin_op(self, fa, fb, /):
        return bool(fa()) and bool(fb())
    def _get_op_str(self, /):
        return '&'
class XorCharFilter(IBinOpCharFilter):
    def _bool_bin_op(self, fa, fb, /):
        return bool(fa()) ^ bool(fb())
    def _get_op_str(self, /):
        return '^'
class ExcludeCharFilter(IBinOpCharFilter):
    def _bool_bin_op(self, fa, fb, /):
        return bool(fa()) and not bool(fb())
    def _get_op_str(self, /):
        return '-'

#################################
#HHHHH
r"""
E(s) = EncodingCharFilter(s)
R({1:2,3:4}) = CharsetCharFilter([(1,2),(3,4)])
N(s) = CharNameRegexCharFilter(s)
U = E('utf8').to_CharsetCharFilter()
U = CharsetCharFilter([(0, 0xD800), (0xE000, 0x11_0000)])
| & ^ -
#"""


def E(s, /):
    return EncodingCharFilter(s)
def R(begin2end, /):
    rngs = sorted(begin2end.items())
    return CharsetCharFilter(rngs)
def N(s, /):
    return CharNameRegexCharFilter(s)
#_U = E('utf8').to_CharsetCharFilter()
U = CharsetCharFilter([(0, 0xD800), (0xE000, 0x11_0000)])

def _t():
    ccf = (E('gb2312') & N('CJK')).to_CharsetCharFilter()
    rngs = make_Ranges(ccf.ranges)
    print(rngs.len_ints())
    assert rngs.len_ints() == 6763 == 3755+3008
    cs = sort_chars_by_encoding('gb2312', ccf.iter_sorted_good_chars())
    cs1 = cs[:3755]
    cs2 = cs[3755:]
    print(cs1)
    print(cs2)
    cs1.startswith('啊阿埃挨哎唉哀皑癌蔼矮艾')
    cs1.endswith('罪尊遵昨左佐柞做作坐座')
    cs2.startswith('亍丌兀丐廿卅丕亘丞鬲孬噩')
    cs2.endswith('黜黝黠黟黢黩黧黥黪黯鼢鼬鼯鼹鼷鼽鼾齄')
def _u():
    _U = E('utf8').to_CharsetCharFilter()
    ccf = _U.to_CharsetCharFilter()
    rngs = make_Ranges(ccf.ranges)
    print(rngs.len_ints())
    print(rngs.ranges)
    assert rngs.len_ints() == 1112064
    assert rngs.ranges == ((0, 55296), (57344, 1114112)) == ((0, 0xD800), (0xE000, 0x11_0000)) == U.ranges

if 0 and __name__ == '__main__':
    _t()
    _u()

#################################
#HHHHH
def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description="charset_filter"
        , epilog=r"""
exprs that usr can use:
    E :: encoding -> ICharFilter
    R :: Map begin end -> ICharFilter
    N :: py_regex_pattern -> ICharFilter
        #unicodedata.name()
    U :: ICharFilter
    (|), (&), (^), (-) :: ICharFilter -> ICharFilter -> ICharFilter
    where
        E(s) = EncodingCharFilter(s)
        R({1:2,3:4}) = CharsetCharFilter([(1,2),(3,4)])
        N(s) = CharNameRegexCharFilter(s)
        U = E('utf8').to_CharsetCharFilter()
        U = CharsetCharFilter([(0, 0xD800), (0xE000, 0x11_0000)])
        | & ^ -
            union, intersection, symmetric_difference, difference

==================================
py -m seed.text.charset_filter -i U
CharsetCharFilter(((0, 55296), (57344, 1114112)))
py -m seed.text.charset_filter -i 'E("utf8").to_CharsetCharFilter()'
CharsetCharFilter(((0, 55296), (57344, 1114112)))

py -m seed.text.charset_filter -i '(E("gb2312") & N("CJK")).to_CharsetCharFilter()'

py -m seed.text.charset_filter -o ~/tmp/cjk_d.txt > ~/tmp/cjk_pr.txt
py -m seed.text.charset_filter -o ~/tmp/cjk_d.txt -f > ~/tmp/cjk_pr2.txt

=========
py -m seed.text.charset_filter -i '(E("gb2312") & N("CJK")).sort_all_good_chars_by_encoding("gb2312")' > ~/tmp/gb2312.txt


py -m seed.text.charset_filter -i '(E("gbk") & N("CJK")).sort_all_good_chars_by_encoding("gbk")' > ~/tmp/gbk.txt

py -m seed.text.charset_filter -i '(E("big5") & N("CJK")).sort_all_good_chars_by_encoding("big5")' > ~/tmp/big5.txt


py -m seed.text.charset_filter -i '(E("hz") & N("CJK")).sort_all_good_chars_by_encoding("hz")' > ~/tmp/hz.txt

gb2312
gbk
hz
big5
big5hkscs
cp950
iso2022_jp_2
gb18030
utf8

gb18030-2000
python 没有 *与 ISO 10646 相应的国家标准 GB 13000 中的其它 CJK 汉字
#"""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input python expr str; without this arg, handle all cjk_encodings')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    #may_ifname = args.input
    #with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
    locals = dict(
            E=E
            ,R=R
            ,N=N
            ,U=U
            )
    may_s = args.input
    if may_s is None:
        r = d = _cjk()
    else:
        s = may_s
        r = safe_eval(s, locals=locals)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        print(repr(r), file=fout)

def _cjk_encodings():
    #Chinese Japanese Korean Vietnamese
    encodings = r"""
gb2312
gbk
hz
big5
big5hkscs
cp950
iso2022_jp_2
gb18030
utf8

cp932
euc_jp
euc_jis_2004
euc_jisx0213
iso2022_jp
iso2022_jp_1
iso2022_jp_2
iso2022_jp_2004
iso2022_jp_3
iso2022_jp_ext
shift_jis
shift_jis_2004
shift_jisx0213

cp949
euc_kr
iso2022_jp_2
iso2022_kr
johab

cp1258

#"""
    encodings = encodings.split()[:-1]
    assert len(encodings) == 9+13+5+1
    encodings = set(encodings)
    assert len(encodings) == 9+13+5+1-2
    return encodings
def _cjk_encodings_to_rngss(cjk_encodings, /):
    encodings = sorted(set(cjk_encodings))
    utf8 = 'utf8'
    #(E("gb2312") & N("CJK")).to_CharsetCharFilter()
    CJK = (U & N("CJK")).to_CharsetCharFilter()
    d = {}
    for encoding in encodings:
        print(f"#{encoding!s}")
        if encoding == utf8:
            r = CJK
        else:
            r = (CJK & E(encoding)).to_CharsetCharFilter()
        d[encoding] = r
        n = r.len()
        print(f"{encoding!s} = {r!r} #{encoding!s}")
        print(f"{encoding!s}_sz = {n!r}")
    return d

def _cjk():
    cjk_encodings = _cjk_encodings()
    print(f"cjk_encodings = {sorted(cjk_encodings)}")
    d = _cjk_encodings_to_rngss(cjk_encodings)
    return d


if __name__ == "__main__":
    main()

r"""

#"""

