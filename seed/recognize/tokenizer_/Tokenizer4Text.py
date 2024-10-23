#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/tokenizer_/Tokenizer4Text.py
    <<==:TODO:e ../../python3_src/seed/recognize/recognizer_LL1_/LMP_LL1.py

[input<Tokenizer4Text> :: str]
    suppose small input, e.g. grammar
    read all input into memory as text
    using py.re

seed.recognize.tokenizer_.Tokenizer4Text
py -m nn_ns.app.debug_cmd   seed.recognize.tokenizer_.Tokenizer4Text -x
py -m nn_ns.app.doctest_cmd seed.recognize.tokenizer_.Tokenizer4Text:__doc__ -ht

>>> wr_hex = WordReader4Text__regex('hex', '0x', '0x[0-9a-fA-F_]+')
>>> read_word_ex(wr_hex, 'aaa')
>>> read_word_ex(wr_hex, '0xffxx', 0, 1)
>>> read_word_ex(wr_hex, '0xffxx', 0, 2)
(Either(False, 'hex'), 2)
>>> read_word_ex(wr_hex, '0xffxx', 0, 3)
(Either(True, Cased('hex', '0xf')), 3)
>>> read_word_ex(wr_hex, '0xffxx', 0, 4)
(Either(True, Cased('hex', '0xff')), 4)
>>> read_word_ex(wr_hex, '0xffxx', 0)
(Either(True, Cased('hex', '0xff')), 4)

>>> wr_bin = WordReader4Text__regex('bin', '0b', '0b[01_]+')

>>> wr_bxx = WordReader4Text__parallel__priority(True, [wr_bin, wr_hex, wr_hex]) #never:[tag==2]
>>> read_word_ex(wr_bxx, '0b11')
(Either(True, Cased(0, Cased('bin', '0b11'))), 4)
>>> read_word_ex(wr_bxx, '0x11')
(Either(True, Cased(1, Cased('hex', '0x11'))), 4)
>>> read_word_ex(wr_bxx, '0o11')
>>> read_word_ex(wr_bxx, '0b21')
(Either(False, Cased(0, 'bin')), 2)
>>> read_word_ex(wr_bxx, '0b112')
(Either(True, Cased(0, Cased('bin', '0b11'))), 4)

>>> wr_bxx = WordReader4Text__parallel__priority(False, [wr_bin, wr_hex, wr_hex])
>>> read_word_ex(wr_bxx, '0b11')
(Either(True, Cased('bin', '0b11')), 4)
>>> read_word_ex(wr_bxx, '0x11')
(Either(True, Cased('hex', '0x11')), 4)
>>> read_word_ex(wr_bxx, '0o11')
>>> read_word_ex(wr_bxx, '0b21')
(Either(False, 'bin'), 2)
>>> read_word_ex(wr_bxx, '0b112')
(Either(True, Cased('bin', '0b11')), 4)


>>> wr_ab = WordReader4Text__constant_words__longest_first(False, "aaa,a,aa,,aab,abb,bbb,bba,ba".split(","))
>>> read_word_ex(wr_ab, 'xx')
(Either(True, Cased('', '')), 0)
>>> read_word_ex(wr_ab, 'axx')
(Either(True, Cased('a', 'a')), 1)
>>> read_word_ex(wr_ab, 'aaxx')
(Either(True, Cased('aa', 'aa')), 2)
>>> read_word_ex(wr_ab, 'aaaxx')
(Either(True, Cased('aaa', 'aaa')), 3)
>>> read_word_ex(wr_ab, 'aaaaxx')
(Either(True, Cased('aaa', 'aaa')), 3)
>>> read_word_ex(wr_ab, 'baaaxx')
(Either(True, Cased('ba', 'ba')), 2)
>>> read_word_ex(wr_ab, 'bbaaxx')
(Either(True, Cased('bba', 'bba')), 3)
>>> read_word_ex(wr_ab, 'bbbaxx')
(Either(True, Cased('bbb', 'bbb')), 3)

>>> wr_ab = WordReader4Text__constant_words__longest_first(True, "aaa,a,aa,,aab,abb,bbb,bba,ba".split(","))
>>> read_word_ex(wr_ab, 'xx')
(Either(True, Cased(3, '')), 0)
>>> read_word_ex(wr_ab, 'axx')
(Either(True, Cased(1, 'a')), 1)
>>> read_word_ex(wr_ab, 'aaxx')
(Either(True, Cased(2, 'aa')), 2)
>>> read_word_ex(wr_ab, 'aaaxx')
(Either(True, Cased(0, 'aaa')), 3)
>>> read_word_ex(wr_ab, 'aaaaxx')
(Either(True, Cased(0, 'aaa')), 3)
>>> read_word_ex(wr_ab, 'baaaxx')
(Either(True, Cased(8, 'ba')), 2)
>>> read_word_ex(wr_ab, 'bbaaxx')
(Either(True, Cased(7, 'bba')), 3)
>>> read_word_ex(wr_ab, 'bbbaxx')
(Either(True, Cased(6, 'bbb')), 3)




>>> wr_bx = WordReader4Text__constant_heads__longest_first(False, [("0b", wr_bin), ("0x", wr_hex)])
>>> read_word_ex(wr_bx, '0b11')
(Either(True, Cased('bin', '0b11')), 4)
>>> read_word_ex(wr_bx, '0x11')
(Either(True, Cased('hex', '0x11')), 4)
>>> read_word_ex(wr_bx, '0o11')
>>> read_word_ex(wr_bx, '0b21')
(Either(False, 'bin'), 2)
>>> read_word_ex(wr_bx, '0b112')
(Either(True, Cased('bin', '0b11')), 4)

>>> wr_bx = WordReader4Text__constant_heads__longest_first(True, [("0b", wr_bin), ("0x", wr_hex)])
>>> read_word_ex(wr_bx, '0b11')
(Either(True, Cased(0, Cased('bin', '0b11'))), 4)
>>> read_word_ex(wr_bx, '0x11')
(Either(True, Cased(1, Cased('hex', '0x11'))), 4)
>>> read_word_ex(wr_bx, '0o11')
>>> read_word_ex(wr_bx, '0b21')
(Either(False, Cased(0, 'bin')), 2)
>>> read_word_ex(wr_bx, '0b112')
(Either(True, Cased(0, Cased('bin', '0b11'))), 4)



>>> wr_uint_hex = WordReader4Text__wrapper__replace_tkey("uint_hex", wr_hex)
>>> read_word_ex(wr_uint_hex, 'aaa')
>>> read_word_ex(wr_uint_hex, '0xffxx', 0, 1)
>>> read_word_ex(wr_uint_hex, '0xffxx', 0, 2) #errmsg free format - unchanged
(Either(False, 'hex'), 2)
>>> read_word_ex(wr_uint_hex, '0xffxx', 0, 3)
(Either(True, Cased('uint_hex', '0xf')), 3)
>>> read_word_ex(wr_uint_hex, '0xffxx', 0, 4)
(Either(True, Cased('uint_hex', '0xff')), 4)
>>> read_word_ex(wr_uint_hex, '0xffxx', 0)
(Either(True, Cased('uint_hex', '0xff')), 4)


>>> wr_eval_hex = WordReader4Text__wrapper__eval_tdat(eval, wr_hex)
>>> read_word_ex(wr_eval_hex, 'aaa')
>>> read_word_ex(wr_eval_hex, '0xffxx', 0, 1)
>>> read_word_ex(wr_eval_hex, '0xffxx', 0, 2)
(Either(False, 'hex'), 2)
>>> read_word_ex(wr_eval_hex, '0xffxx', 0, 3)
(Either(True, Cased('hex', 15)), 3)
>>> read_word_ex(wr_eval_hex, '0xffxx', 0, 4)
(Either(True, Cased('hex', 255)), 4)
>>> read_word_ex(wr_eval_hex, '0xffxx', 0)
(Either(True, Cased('hex', 255)), 4)


#>>> wr_hex
#>>> wr_bxx
#>>> wr_ab
#>>> wr_bx
#>>> wr_uint_hex
#>>> wr_eval_hex

>>> wr_hex
WordReader4Text__regex('hex', '0x', '0x[0-9a-fA-F_]+')
>>> wr_bxx
WordReader4Text__parallel__priority(False, (WordReader4Text__regex('bin', '0b', '0b[01_]+'), WordReader4Text__regex('hex', '0x', '0x[0-9a-fA-F_]+'), WordReader4Text__regex('hex', '0x', '0x[0-9a-fA-F_]+')))
>>> wr_ab
WordReader4Text__constant_words__longest_first(True, ('aaa', 'a', 'aa', '', 'aab', 'abb', 'bbb', 'bba', 'ba'))
>>> wr_bx
WordReader4Text__constant_heads__longest_first(True, (('0b', WordReader4Text__regex('bin', '0b', '0b[01_]+')), ('0x', WordReader4Text__regex('hex', '0x', '0x[0-9a-fA-F_]+'))))
>>> wr_uint_hex
WordReader4Text__wrapper__replace_tkey('uint_hex', WordReader4Text__regex('hex', '0x', '0x[0-9a-fA-F_]+'))
>>> wr_eval_hex
WordReader4Text__wrapper__eval_tdat(<built-in function eval>, WordReader4Text__regex('hex', '0x', '0x[0-9a-fA-F_]+'))

######################
######################
######################
######################
>>> wr_space = WordReader4Text__regex('space', None, r'\s+')
>>> wr_bxs = WordReader4Text__parallel__priority(False, [wr_bin, wr_hex, wr_space])

>>> tknr_bxs = Tokenizer4Text__no_state(wr_bxs, ['space'])
>>> [*iter_tokenize4text_(tknr_bxs, {}, '  0x9a  0b01 0xdd 0xaa 0b0 ')]
[(Cased('hex', '0x9a'), (2, 6)), (Cased('bin', '0b01'), (8, 12)), (Cased('hex', '0xdd'), (13, 17)), (Cased('hex', '0xaa'), (18, 22)), (Cased('bin', '0b0'), (23, 26))]

######################
######################
######################
>>> wr_word = WordReader4Text__regex('word', r'\w', r'\w+')
>>> wr_6 = WordReader4Text__regex('6', None, r'[(]')
>>> wr_9 = WordReader4Text__regex('9', None, r'[)]')
>>> wr_bxs69 = WordReader4Text__parallel__priority(False, [wr_bin, wr_hex, wr_space, wr_6, wr_9])
>>> wr_ws69 = WordReader4Text__parallel__priority(False, [wr_word, wr_space, wr_6, wr_9])

>>> tknr_bxs69 = Tokenizer4Text__with_state_stack(wr_bxs69, ['space'], {'9':RET, '6':mk_cal_('ws69')}, None)
>>> tknr_ws69 = Tokenizer4Text__with_state_stack(wr_ws69, [], {'9':RET, '6':mk_cal_('bxs69'),'space':mk_jmp_('ws69')}, None)
>>> env = tknz_state2tokenizer = {'bxs69':tknr_bxs69, 'ws69':tknr_ws69}
>>> [*iter_tokenize4text_(tknr_ws69, env, ' aaa( 0x9a  0b01 (kkk(0x3) ) 0xdd 0xaa 0b0) bbb cc ')] == (
... [(Cased('space', ' '), (0, 1))
... , (Cased('word', 'aaa'), (1, 4))
... , (Cased('6', '('), (4, 5))
...     , (Cased('hex', '0x9a'), (6, 10))
...     , (Cased('bin', '0b01'), (12, 16))
...     , (Cased('6', '('), (17, 18))
...         , (Cased('word', 'kkk'), (18, 21))
...         , (Cased('6', '('), (21, 22))
...             , (Cased('hex', '0x3'), (22, 25))
...         , (Cased('9', ')'), (25, 26))
...         , (Cased('space', ' '), (26, 27))
...     , (Cased('9', ')'), (27, 28))
...     , (Cased('hex', '0xdd'), (29, 33))
...     , (Cased('hex', '0xaa'), (34, 38))
...     , (Cased('bin', '0b0'), (39, 42))
... , (Cased('9', ')'), (42, 43))
... , (Cased('space', ' '), (43, 44))
... , (Cased('word', 'bbb'), (44, 47))
... , (Cased('space', ' '), (47, 48))
... , (Cased('word', 'cc'), (48, 50))
... , (Cased('space', ' '), (50, 51))
... ])
True



######################
######################
######################

#]]]'''
__all__ = r'''
iter_tokenize4text_
ITokenizer4Text
    Tokenizer4Text__no_state
    Tokenizer4Text__with_state_stack
        TknzStOp
            NOP
            RET
            mk_jmp_
            mk_cal_

read_word_ex
IWordReader4Text
    WordReader4Text__parallel__priority
    WordReader4Text__constant_words__longest_first
    WordReader4Text__constant_heads__longest_first
    WordReader4Text__wrapper__replace_tkey
    IWordReader4Text__wrapper__eval_tdat
        WordReader4Text__wrapper__eval_tdat
    WordReader4Text__regex





















IWordReader4Text
    WordReader4Text__parallel__priority
    WordReader4Text__constant_words__longest_first
    IWordReader4Text__wrapper__postprocess
        WordReader4Text__constant_heads__longest_first
        WordReader4Text__wrapper__replace_tkey
        IWordReader4Text__wrapper__eval_tdat
            WordReader4Text__wrapper__eval_tdat
    WordReader4Text__regex

check_eresult_ex4word_reader
    check_eresult4word_reader
        check_oresult4word_reader





TokenizerError
    TokenizerError__null_word_not_at_eof

TokenizerFail
    TokenizerFail__not_match_head
    TokenizerFail__match_head_but_word

TknzStOp
    NOP
    RET
    mk_jmp_
    mk_cal_

ITokenizer4Text
    ITokenizer4Text__asif_stated
        ITokenizer4Text__no_state
            Tokenizer4Text__no_state
        ITokenizer4Text__with_state_stack
            Tokenizer4Text__with_state_stack


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.types.Either import Cased, Either
from seed.types.Either import mk_Left, mk_Right
from seed.tiny_.containers import mk_frozenset, mk_tuple #, null_frozenset, null_iter

from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len

from seed.seq_tools.mk_prefix_tree import mk_prefix_tree, lookup_longest_prefix4prefix_tree #, update4prefix_tree, lookup4prefix_tree, iter_lookup_prefix4prefix_tree
from seed.seq_tools.mk_prefix_tree import view_seq____not_seq_eq_hash #, view_seq____seq_eq_hash

from seed.iters.duplicate_elements import iter_duplicate_representative_elements

from seed.tiny_.check import check_type_le, check_type_is, check_int_ge, check_int_ge_le, check_subscriptable, check_pair
from seed.tiny_.check import check_non_ABC, check_ABC
from seed.tiny import MapView, fst, ifNone


from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper

from enum import Enum
import re

___end_mark_of_excluded_global_names__0___ = ...

class IWordReader4Text(ABC):
    '[oresult :: Cased tkey tdat][eresult :: Either errmsg oresult]'
    __slots__ = ()
    @abstractmethod
    def peek_may_header_state(sf, txt, begin, end, /):
        'txt/str -> begin/uint -> end/uint -> may header_state'
    @abstractmethod
    def _read_word_(sf, txt, begin, end, header_state, /):
        'txt/str -> begin/uint -> end/uint -> header_state -> eresult_ex/(eresult, end4xxx/(end4head if fail else end4word)/uint)'
    def read_word(sf, txt, begin, end, header_state, /):
        'txt/str -> begin/uint -> end/uint -> header_state -> eresult_ex/(eresult, end4xxx/(end4head if fail else end4word)/uint)'
        eresult_ex = sf._read_word_(txt, begin, end, header_state)
        check_eresult_ex4word_reader(eresult_ex)
        return eresult_ex
def check_eresult_ex4word_reader(eresult_ex, /):
    '[eresult_ex<word_reader> :: (eresult/(Either errmsg oresult/(Cased tkey tdat)), end4xxx)]'
    check_pair(eresult_ex)
    (eresult, end4xxx) = eresult_ex
    check_type_is(int, end4xxx)
    check_eresult4word_reader(eresult)
def check_eresult4word_reader(eresult, /):
    '[eresult<word_reader> :: Either errmsg oresult/(Cased tkey tdat)]'
    check_type_is(Either, eresult)
    if eresult.is_right:
        oresult = eresult.right
        check_oresult4word_reader(oresult)
def check_oresult4word_reader(oresult, /):
    '[oresult<word_reader> :: Cased tkey tdat]'
    check_type_is(Cased, oresult)

def read_word_ex(word_reader, txt, begin=None, end=None, /):
    'word_reader/IWordReader4Text -> txt/str -> begin/(may int) -> end/(may int) -> may eresult_ex/(eresult, end4xxx/(end4head if fail else end4word)/uint){None if peek head fail}'
    check_type_is(str, txt)
    (begin, end) = mk_seq_rng(txt, begin, end)

    may_st = word_reader.peek_may_header_state(txt, begin, end)
    if may_st is None:
        return None
    header_state = may_st
    eresult_ex = word_reader.read_word(txt, begin, end, header_state)
    return eresult_ex


class IWordReader4Text__wrapper__postprocess(IWordReader4Text):
    #see:WordReader4Text__constant_heads__longest_first
    __slots__ = ()

    @property
    @abstractmethod
    def _word_reader_(sf, /):
        '-> IWordReader4Text'
    @abstractmethod
    def postprocess_ex(sf, txt, begin, end, eresult_ex, /):
        'txt/str -> begin/uint -> end/uint -> eresult_ex -> eresult_ex/(eresult, end4xxx)'

    @override
    def peek_may_header_state(sf, txt, begin, end, /):
        'txt/str -> begin/uint -> end/uint -> may header_state'
        return sf._word_reader_.peek_may_header_state(txt, begin, end)
    @override
    def _read_word_(sf, txt, begin, end, header_state, /):
        'txt/str -> begin/uint -> end/uint -> header_state -> eresult_ex/(eresult, end4xxx/(end4head if fail else end4word)/uint)'
        eresult_ex = sf._word_reader_.read_word(txt, begin, end, header_state)
        return sf.postprocess_ex(txt, begin, end, eresult_ex)

class WordReader4Text__wrapper__replace_tkey(IWordReader4Text__wrapper__postprocess):
    ___no_slots_ok___ = True
    def __init__(sf, tkey, word_reader, /):
        check_type_le(IWordReader4Text, word_reader)

        sf._tt = tkey
        sf._wr = word_reader
        sf._args4repr = (tkey, word_reader)
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    def tkey(sf, /):
        '-> tkey'
        return sf._tt

    @property
    @override
    def _word_reader_(sf, /):
        '-> IWordReader4Text'
        return sf._wr
    @override
    def postprocess_ex(sf, txt, begin, end, eresult_ex, /):
        'txt/str -> begin/uint -> end/uint -> eresult_ex -> eresult_ex/(eresult, end4xxx)'
        (eresult, end4xxx) = eresult_ex
        if eresult.is_right:
            oresult = eresult.right
            oresult = oresult.ireplace__case(sf.tkey)
            eresult = eresult.ireplace__payload(oresult)
            eresult_ex = (eresult, end4xxx)
        return eresult_ex



class IWordReader4Text__wrapper__eval_tdat(IWordReader4Text__wrapper__postprocess):
    __slots__ = ()
    @abstractmethod
    def _eval_(sf, tdat, /):
        'tdat -> tdat'
    @override
    def postprocess_ex(sf, txt, begin, end, eresult_ex, /):
        'txt/str -> begin/uint -> end/uint -> eresult_ex -> eresult_ex/(eresult, end4xxx)'
        (eresult, end4xxx) = eresult_ex
        if eresult.is_right:
            oresult = eresult.right
            oresult = oresult.fmap4payload(sf._eval_)
            eresult = eresult.ireplace__payload(oresult)
            eresult_ex = (eresult, end4xxx)
        return eresult_ex

class WordReader4Text__wrapper__eval_tdat(IWordReader4Text__wrapper__eval_tdat):
    ___no_slots_ok___ = True
    def __init__(sf, eval_, word_reader, /):
        check_type_le(IWordReader4Text, word_reader)

        sf._f = eval_
        sf._wr = word_reader
        sf._args4repr = (eval_, word_reader)
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    def _eval_(sf, /):
        '-> (tdat -> tdat)'
        return sf._f

    @property
    @override
    def _word_reader_(sf, /):
        '-> IWordReader4Text'
        return sf._wr




class WordReader4Text__parallel__priority(IWordReader4Text):
    ___no_slots_ok___ = True
    def __init__(sf, to_tag, word_readers, /):
        check_type_is(bool, to_tag)
        word_readers = mk_tuple(word_readers)
        for word_reader in word_readers:
            check_type_le(IWordReader4Text, word_reader)
        sf._tt = to_tag
        sf._ws = word_readers
        sf._args4repr = (to_tag, word_readers)
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    def to_tag(sf, /):
        '-> bool'
        return sf._tt
    @property
    def word_readers(sf, /):
        '-> [IWordReader4Text]'
        return sf._ws
    @override
    def peek_may_header_state(sf, txt, begin, end, /):
        'txt/str -> begin/uint -> end/uint -> may header_state'
        for j, word_reader in enumerate(sf.word_readers):
            may_st = word_reader.peek_may_header_state(txt, begin, end)
            if not may_st is None:
                st = may_st
                break
        else:
            return None
        header_state = (j, st)
        return header_state
    @override
    def _read_word_(sf, txt, begin, end, header_state, /):
        'txt/str -> begin/uint -> end/uint -> header_state -> eresult_ex/(eresult, end4xxx/(end4head if fail else end4word)/uint)'
        (j, st) = header_state
        word_reader = sf.word_readers[j]
        eresult_ex = word_reader.read_word(txt, begin, end, st)
        if not sf.to_tag:
            return eresult_ex
        (eresult, end4word) = eresult_ex
            # no matter ok or fail
        eresult = eresult.itag__payload(j)
            #vs:.untag__payload()
        return (eresult, end4word)
#end-class WordReader4Text__parallel__priority(IWordReader4Text):



class WordReader4Text__constant_words__longest_first(IWordReader4Text):
    ___no_slots_ok___ = True
    def __init__(sf, to_tag, words, /):
        check_type_is(bool, to_tag)
        words = mk_tuple(words)
        for word in words:
            check_type_is(str, word)
        if not len(words) == len(set(words)):raise KeyError([*iter_duplicate_representative_elements(words)])

        prefix_tree = mk_prefix_tree(dict, False, words, to_support_seq_eq=False)
        sf._tt = to_tag
        sf._ws = words
        sf._args4repr = (to_tag, words)
        sf._pt = prefix_tree
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    def to_tag(sf, /):
        '-> bool'
        return sf._tt
    @property
    def words(sf, /):
        '-> [str]'
        return sf._ws
    @override
    def peek_may_header_state(sf, txt, begin, end, /):
        'txt/str -> begin/uint -> end/uint -> may header_state'
        txt_view = view_seq____not_seq_eq_hash(txt)[begin:end]
        prefix_tree = sf._pt
        m = lookup_longest_prefix4prefix_tree(prefix_tree, txt_view)
        if m is None:
            return None
        (len_word, js) = m
        assert js
        if len(js) >= 2:
            raise 000-iter_duplicate_representative_elements
        [j] = js
        assert len_word == len(sf.words[j])
        header_state = j
        return header_state
    @override
    def _read_word_(sf, txt, begin, end, header_state, /):
        'txt/str -> begin/uint -> end/uint -> header_state -> eresult_ex/(eresult, end4xxx/(end4head if fail else end4word)/uint)'
        j = header_state
        word = sf.words[j]
        assert txt.startswith(word, begin, end)
        tkey = j if sf.to_tag else word
            # always ok
            # no matter ok or fail
        oresult = Cased(tkey, tdat:=word)
        eresult = mk_Right(oresult)
        end4word = begin + len(word)
        return (eresult, end4word)
#end-class WordReader4Text__constant_words__longest_first(IWordReader4Text):


class WordReader4Text__constant_heads__longest_first(IWordReader4Text__wrapper__postprocess):
    ___no_slots_ok___ = True
    def __init__(sf, to_tag, headed_word_readers, /):
        check_type_is(bool, to_tag)
        headed_word_readers = mk_tuple(headed_word_readers)

        for x in headed_word_readers:
            check_type_le(tuple, x)
        for (head, word_reader) in headed_word_readers:
            check_type_is(str, head)
            check_type_le(IWordReader4Text, word_reader)

        heads = mk_tuple(map(fst, headed_word_readers))
        head_reader = WordReader4Text__constant_words__longest_first(True, heads)

        sf._tt = to_tag
        sf._ps = headed_word_readers
        sf._args4repr = (to_tag, headed_word_readers)
        sf._hr = head_reader
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    def to_tag(sf, /):
        '-> bool'
        return sf._tt
    @property
    def headed_word_readers(sf, /):
        '-> [str]'
        return sf._ps

    @property
    @override
    def _word_reader_(sf, /):
        '-> IWordReader4Text'
        return sf._hr
    @override
    def postprocess_ex(sf, txt, begin, end, eresult_ex4head, /):
        'txt/str -> begin/uint -> end/uint -> eresult_ex -> eresult_ex/(eresult, end4xxx)'
        (eresult4head, end4head) = eresult_ex4head
        oresult4head = eresult4head.right # MUST BE "right"
        j = oresult4head.case # WordReader4Text__constant_words__longest_first[to_tag:=True]

        (head, word_reader) = sf.headed_word_readers[j]
        assert txt.startswith(head, begin, end)
        assert end4head == begin + len(head)
        may_st = word_reader.peek_may_header_state(txt, begin, end)
        if may_st is None:
            errmsg = head
            eresult = mk_Left(errmsg)
            eresult_ex = (eresult, end4head)
        else:
            st = may_st
            eresult_ex = word_reader.read_word(txt, begin, end, st)
        eresult_ex
        if not sf.to_tag:
            return eresult_ex
        (eresult, end4word) = eresult_ex
            # no matter ok or fail
        eresult = eresult.itag__payload(j)
            #vs:.untag__payload()
        return (eresult, end4word)
#end-class WordReader4Text__constant_heads__longest_first(IWordReader4Text):




class WordReader4Text__regex(IWordReader4Text):
    ___no_slots_ok___ = True
    def __init__(sf, tkey, may_regex4head, regex4word, /):
        if not None is may_regex4head:
            regex4head = may_regex4head
            check_type_is(str, regex4head)
        check_type_is(str, regex4word)

        re4word = re.compile(regex4word)
        may_re4head = re.compile(regex4head) if not None is may_regex4head else None

        sf._tt = tkey
        sf._mre4h = may_re4head
        sf._re4w = re4word
        sf._args4repr = (tkey, may_regex4head, regex4word)
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    ##@property
    ##def may_regex4head(sf, /):
    ##    '-> str'
    ##    return sf._
    ##@property
    ##def regex4word(sf, /):
    ##    '-> str'
    ##    return sf._
    @override
    def peek_may_header_state(sf, txt, begin, end, /):
        'txt/str -> begin/uint -> end/uint -> may header_state'
        may_re4head = sf._mre4h
        re4word = sf._re4w
        re4head = ifNone(may_re4head, re4word)
        m = re4head.match(txt, begin, end)
        if m is None:
            return None
        end4head = m.end()
        assert begin == m.start()
        len_head = end4head -begin
        header_state = end4head
        return header_state
    @override
    def _read_word_(sf, txt, begin, end, header_state, /):
        'txt/str -> begin/uint -> end/uint -> header_state -> eresult_ex/(eresult, end4xxx/(end4head if fail else end4word)/uint)'
        end4head = header_state
        tkey = sf._tt
        may_re4head = sf._mre4h
        re4word = sf._re4w
        if may_re4head is None:
            # !! [re4head == ifNone(may_re4head, re4word) == re4word]
            end4word = end4head
        else:
            m = re4word.match(txt, begin, end)
            if m is None:
                errmsg = tkey
                eresult = mk_Left(errmsg)
                return (eresult, end4head)

            end4word = m.end()
            assert begin == m.start()
        end4word
        word = txt[begin:end4word]
        oresult = Cased(tkey, tdat:=word)
        eresult = mk_Right(oresult)
        return (eresult, end4word)
#end-class WordReader4Text__regex(IWordReader4Text):




class TokenizerError(Exception):pass
class TokenizerError__null_word_not_at_eof(TokenizerError):pass


class TokenizerFail(Exception):pass
class TokenizerFail__not_match_head(TokenizerFail):pass
class TokenizerFail__match_head_but_word(TokenizerFail):pass


class ITokenizer4Text(ABC):
    '["env" used for recur ref other ITokenizer4Text]'
    __slots__ = ()
    @abstractmethod
    def _iter_tokenize4text_(sf, env, txt, begin, end, /):
        'env/mapping -> txt/str -> begin/uint -> end/uint -> Iter (Cased tkey tdat, rng/(begin,end)) | ^TokenizerFail(errmsg, rng)'
    def iter_tokenize4text_(sf, env, txt, begin=None, end=None, /):
        'env/mapping -> txt/str -> begin/(may int) -> end/(may int) -> Iter (Cased tkey tdat, rng/(begin,end)) | ^TokenizerFail(errmsg, rng)'
        check_subscriptable(env)
        check_type_is(str, txt)
        (begin, end) = mk_seq_rng(txt, begin, end)

        check_int_ge(0, begin)
        check_int_ge_le(begin, len(txt), end)
        return sf._iter_tokenize4text_(env, txt, begin, end)
def iter_tokenize4text_(tokenizer, env, txt, begin=None, end=None, /):
    'tokenizer/ITokenizer4Text -> env/mapping -> txt/str -> begin/(may int) -> end/(may int) -> Iter (Cased tkey tdat, rng/(begin,end)) | ^TokenizerFail(errmsg, rng)'
    return tokenizer.iter_tokenize4text_(env, txt, begin, end)

class TknzStOp(Enum):
    r'''[[[
    state_op/(TknzStOp, may tknz_state)
    state_op :=
        | (cal, tknz_state)
        | (ret, None)
        | (jmp, tknz_state)
        | (nop, None)

    #]]]'''#'''
    cal = +1
    ret = -1
    jmp = 0
    nop = None
assert len(TknzStOp) == 4
assert TknzStOp.cal
assert TknzStOp.ret
assert TknzStOp.jmp
assert TknzStOp.nop

assert TknzStOp.cal.value
assert TknzStOp.ret.value
assert not TknzStOp.jmp.value
assert not TknzStOp.nop.value

def __():
    TknzStOp.nop.delta = 0
    TknzStOp.jmp.delta = 0
    TknzStOp.cal.delta = +1
    TknzStOp.ret.delta = -1

    TknzStOp.nop.has_payload = False
    TknzStOp.jmp.has_payload = True
    TknzStOp.cal.has_payload = True
    TknzStOp.ret.has_payload = False
__()
NOP = Cased(TknzStOp.nop, None)
RET = Cased(TknzStOp.ret, None)
def mk_jmp_(tknz_state, /):
    return Cased(TknzStOp.jmp, tknz_state)
def mk_cal_(tknz_state, /):
    return Cased(TknzStOp.cal, tknz_state)



class ITokenizer4Text__asif_stated(ITokenizer4Text):
    __slots__ = ()
    @property
    @abstractmethod
    def word_reader(sf, /):
        '-> IWordReader4Text'
    @abstractmethod
    def is_noise_tkey_(sf, env, tkey, /):
        'env -> tkey -> bool'

class ITokenizer4Text__no_state(ITokenizer4Text__asif_stated):
    __slots__ = ()
    #`def word_reader
    #`def is_noise_tkey_
    @override
    def _iter_tokenize4text_(sf, env, txt, begin, end, /):
        'env/mapping -> txt/str -> begin/uint -> end/uint -> Iter (oresult/(Cased tkey tdat){not sf.is_noise_tkey_(env, tkey)}, rng/(begin,end)) | ^TokenizerFail(errmsg, rng)'
        word_reader = sf.word_reader
        while 1:
            if None is (m := (yield from _iter8loop_body(sf, word_reader, env, txt, begin, end))):
                assert begin == end
                break
            #######next word:
            (tkey, end4word) = m
            begin = end4word
            #assert begin <= end
        assert begin == end
        return
#end-class ITokenizer4Text__no_state(ITokenizer4Text__asif_stated):


class ITokenizer4Text__with_state_stack(ITokenizer4Text__asif_stated):
    __slots__ = ()
    #`def word_reader
    #`def is_noise_tkey_
    @abstractmethod
    def tkey2state_op_(sf, env, tkey, /):
        'env -> tkey -> state_op/(TknzStOp, may tknz_state)'
    @abstractmethod
    def tknz_state2tokenizer_(sf, env, tknz_state, /):
        'env -> tknz_state -> ITokenizer4Text__with_state_stack | ^LookupError'

    @override
    def _iter_tokenize4text_(sf, env, txt, begin, end, /):
        'env/mapping -> txt/str -> begin/uint -> end/uint -> Iter (oresult/(Cased tkey tdat){not sf.is_noise_tkey_(env, tkey)}, rng/(begin,end)) | ^TokenizerFail(errmsg, rng)'
        stack = []
            # [(ITokenizer4Text__with_state_stack, word_reader)]
        word_reader = sf.word_reader
        while 1:
            if None is (m := (yield from _iter8loop_body(sf, word_reader, env, txt, begin, end))):
                assert begin == end
                break
            #######next word:
            (tkey, end4word) = m
            begin = end4word
            #assert begin <= end

            (case, m) = state_op = sf.tkey2state_op_(env, tkey)
            if not case.has_payload:
                if case is TknzStOp.nop:
                    pass
                elif case is TknzStOp.ret:
                    (sf, word_reader) = stack.pop()
                else:
                    check_type_is(TknzStOp, state_op)
                    raise 000
                assert m is None
            else:
                if case is TknzStOp.cal:
                    stack.append((sf, word_reader))
                elif case is TknzStOp.jmp:
                    pass
                else:
                    check_type_is(TknzStOp, state_op)
                    raise 000
                word_reader = ...

                tknz_state = m
                sf = sf.tknz_state2tokenizer_(env, tknz_state)
                check_type_le(__class__, sf) #ITokenizer4Text__with_state_stack
                word_reader = sf.word_reader
                sf, word_reader
            #end-if:case{state_op}
        #end-while
        assert begin == end
        #if stack:raise ... #leave for grammar
        return
#end-class ITokenizer4Text__with_state_stack(ITokenizer4Text__asif_stated):

def _iter8loop_body(sf, word_reader, env, txt, begin, end, /):
    '-> (Iter (oresult, rng)){return:may (tkey, end4word)} #for subclass of ITokenizer4Text__asif_stated'
    may_st = word_reader.peek_may_header_state(txt, begin, end)
    if may_st is None:
        if begin == end:
            return#break
        errmsg = None
        #eresult = mk_Left(errmsg)
        end4xxx = begin
        rng = (begin, end4xxx)
        raise TokenizerFail__not_match_head(errmsg, rng)
    st = may_st
    (eresult, end4xxx) = word_reader.read_word(txt, begin, end, st)
    if eresult.is_left:
        errmsg = eresult.left
        rng = (begin, end4xxx)
        raise TokenizerFail__match_head_but_word(errmsg, rng)
    oresult = eresult.right
    check_type_is(Cased, oresult)
    tkey = oresult.case
    skip = sf.is_noise_tkey_(env, tkey)
    end4word = end4xxx
    rng = (begin, end4word)
    if begin == end4word:
        # null_word
        if begin == end:
            # [null_word@eof ok but at_most_one]
            if not skip:yield (oresult, rng)
            return#break
        # [null_word@non_eof not ok since cause inf iter]
        raise TokenizerError__null_word_not_at_eof(oresult, rng)
    if not skip:yield (oresult, rng)

    #######next word:
    begin = end4word
    return (tkey, end4word)
    return end4word
    return begin
#end-def _iter8loop_body(sf, word_reader, env, txt, begin, end, /):
777;    ITokenizer4Text__asif_stated


class Tokenizer4Text__no_state(ITokenizer4Text__no_state):
    ___no_slots_ok___ = True
    def __init__(sf, word_reader, noise_tkeys, /):
        check_type_le(IWordReader4Text, word_reader)
        noise_tkeys = mk_frozenset(noise_tkeys)

        sf._wr = word_reader
        sf._nks = noise_tkeys
        sf._args4repr = (word_reader, noise_tkeys)

    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    def noise_tkeys(sf, /):
        '-> {tkey}'
        return sf._nks

    @property
    @override
    def word_reader(sf, /):
        '-> IWordReader4Text'
        return sf._wr
    @override
    def is_noise_tkey_(sf, env, tkey, /):
        'env -> tkey -> bool'
        return tkey in sf.noise_tkeys
#end-class Tokenizer4Text__no_state(ITokenizer4Text__no_state):

class Tokenizer4Text__with_state_stack(ITokenizer4Text__with_state_stack):
    ___no_slots_ok___ = True
    def __init__(sf, word_reader, noise_tkeys, tkey2state_op, may__symbol4tknz_state2tokenizer, /):
        check_type_le(IWordReader4Text, word_reader)
        noise_tkeys = mk_frozenset(noise_tkeys)
        hash(may__symbol4tknz_state2tokenizer)


        sf._wr = word_reader
        sf._nks = noise_tkeys
        sf._tk2op = MapView(tkey2state_op)
        sf._msym = may__symbol4tknz_state2tokenizer
        sf._args4repr = (word_reader, noise_tkeys, tkey2state_op, may__symbol4tknz_state2tokenizer)


    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    def noise_tkeys(sf, /):
        '-> {tkey}'
        return sf._nks

    @property
    @override
    def word_reader(sf, /):
        '-> IWordReader4Text'
        return sf._wr
    @override
    def is_noise_tkey_(sf, env, tkey, /):
        'env -> tkey -> bool'
        return tkey in sf.noise_tkeys
    @override
    def tkey2state_op_(sf, env, tkey, /):
        'env -> tkey -> state_op/(TknzStOp, may tknz_state)'
        return sf._tk2op.get(tkey, NOP)
    @override
    def tknz_state2tokenizer_(sf, env, tknz_state, /):
        'env -> tknz_state -> ITokenizer4Text__with_state_stack | ^LookupError'
        if not None is (sym := sf._msym):
            d = env[sym]
        else:
            d = env
        d # tknz_state2tokenizer
        return d[tknz_state]

#end-class Tokenizer4Text__with_state_stack(ITokenizer4Text__with_state_stack):


Tokenizer4Text__no_state(WordReader4Text__constant_words__longest_first(False, []), [])
Tokenizer4Text__with_state_stack(WordReader4Text__constant_words__longest_first(False, []), [], {}, None)
def __():
    for nm in __all__:
        x = globals()[nm]
        if not isinstance(x, type):
            continue
        if nm[0] == 'I':
            check_ABC(x)
        else:
            check_non_ABC(x)
__()
__all__
from seed.recognize.tokenizer_.Tokenizer4Text import \
(ITokenizer4Text
,    Tokenizer4Text__no_state
,    Tokenizer4Text__with_state_stack
,        TknzStOp
,            NOP
,            RET
,            mk_jmp_
,            mk_cal_
#
,IWordReader4Text
,    WordReader4Text__parallel__priority
,    WordReader4Text__constant_words__longest_first
,    WordReader4Text__constant_heads__longest_first
,    WordReader4Text__wrapper__replace_tkey
,    IWordReader4Text__wrapper__eval_tdat
,        WordReader4Text__wrapper__eval_tdat
,    WordReader4Text__regex
)




from seed.recognize.tokenizer_.Tokenizer4Text import *
