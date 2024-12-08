#__all__:goto
#TODO:always tkd_/tkey2rgnr4tkd_  # cooperate with subscript_ .@(idx/0/1)
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/tokenize_utils.py

seed.recognize.recognizer_LLoo__ver2_.tokenize_utils
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo__ver2_.tokenize_utils -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.tokenize_utils:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo__ver2_.tokenize_utils   @f
#]]]'''
__all__ = r'''
mk_rgnr4words_
    mk_rgnr4operators_
    mk_rgnr4enum_type_

tokenize__core_
    tokenize__args8chars_
        tokenize__chars_
        tokenize__file_
        tokenize__path_

mk_null_env4main_rgnr_









ns4common_rgnr4tknz
    all_name_set4common_rgnr4tknz
    xqset2rgnr4tdat_
    xqset2rgnr4tkey_
    tkey2rgnr4tdat_
    tkey2rgnr4tkey_

    xqset2both_rgnrs4tdat_
    xqset2both_rgnrs4tkey_
    tkey2both_rgnrs4tdat_
    tkey2both_rgnrs4tkey_

    xqset2rgnr4tkd_
    tkey2rgnr4tkd_

IHelper4Tokenization
    BaseHelper4Tokenization
    whether_default
        whether_default_
        remove_default_methods_
    extract_info5hlpr4tknz_
    prepare4tokenize_

isinstance
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.types.IToken import mk_high_lvl_rawstream5low_high_low_triples_
#def mk_high_lvl_rawstream5low_high_low_triples_(high_lvl_offset, low_lvl_tgbegin, low_high_low_triples, /, *, to_flatten:bool):

#from seed.types.IToken import mk_chr_rawstream5args8chars_
    # -> chr_rawstream
from seed.types.stream.IRecoverableInputStream import mk_istream5rawstream_, mk_chr_istream5args8chars_, mk_chr_istream5path_, mk_chr_istream5file_, mk_chr_istream5chars_
    # -> chr_istream
    # -> istream
#def mk_chr_istream5args8chars_(args8chars, max_num_tokens6backward=0, /):
#def mk_istream5rawstream_(rawstream, max_num_tokens6backward=0, /):
#def mk_chr_istream5path_(ipath, /, *, encoding, may_pseudo_fname=None, max_num_tokens6backward=0):
#def mk_chr_istream5chars_(chr_tgbegin, chars, /, *, max_num_tokens6backward=0):
from seed.types.IToken import (
mk_chr_rawstream5args8chars_
,   mk_chr_rawstream5path_
,       mk_chr_tgbegin5fname_
,   mk_chr_rawstream5file_
,   mk_chr_rawstream5chars_
,       mk_chr_rawstream5text_
,   mk_args8chars5path_
,   mk_args8chars5file_
,   mk_args8chars5chars_
#       args8chars = mk_args8chars5chars_(chr_tgbegin, chars)
#       args8chars = mk_args8chars5file_(chr_tgbegin, ifile, to_close=to_close)
#       args8chars = mk_args8chars5path_(ipath, encoding=encoding, may_pseudo_fname=may_pseudo_fname)
)

from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import recognize_, mk_Environment, IRecognizerLLoo
from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import Makers4IRecognizerLLoo

from seed.types.Either import Cased, Either
from seed.types.Either import mk_Left, mk_Right

from seed.helper.getset_external_cache4func import getset_external_cache4func# getset_external_cache4method
#def getset_external_cache4func(get_vs_set_vs_set_ex, f, /, *weakable_args, __depth=0):

from seed.tiny_.check import check_type_is, check_type_le, check_int_ge
from seed.tiny import ifNone, echo, fst, curry1# print_err

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
___end_mark_of_excluded_global_names__0___ = ...

__all__

def isinstance(v, T, /):
    #to avoid py.bug
    return issubclass(type(v), T)
def mk_rgnr4words_(words, /, *, word2oresult_=echo):
    '{word}/{[tkey]} -> (kw:word2oresult_::word->oresult) -> IRecognizerLLoo<oresult> # [word :: [tkey]] # [[tkey==char] -> [word==keyword==operator::str]]'
    mkrs = Makers4IRecognizerLLoo
    #rgnr = mkrs.tkey_prefix_tree_(tuple(Cased(word2oresult_(w),w) for w in words))
    rgnr = mkrs.tkey_prefix_tree_(tuple((word2oresult_(w),w) for w in words))
        # Cased-->Pair
    return rgnr
def mk_rgnr4operators_(operators, /):
    '{operator}/{[tkey]} -> IRecognizerLLoo<oresult:=Cased(operator,None)>'
    #._rgnr4op = mk_rgnr4words_(operators)
    #.rgnr4op = mkrs.spostprocess_(_rgnr4op, None, lambda tkey8op:Cased(tkey8op, None), _force_postprocess_when_ignore_:=True)
    return mk_rgnr4words_(operators, word2oresult_=_word2cased_word_None)
        # !! tkey_prefix_tree_#no matter whether ignore
def _word2cased_word_None(word, /):
    'word/[tkey] -> Cased(word, None)'
    return Cased(word, None)
def mk_rgnr4enum_type_(enum_type_name, enum_value_names, /):
    'enum_type_name -> {enum_value_name}/{[tkey]} -> IRecognizerLLoo<oresult:=Cased(enum_type_name,enum_value_name)>'
    _val2cased_typ_val = curry1(Cased, enum_type_name)
    return mk_rgnr4words_(enum_value_names, word2oresult_=_val2cased_typ_val)
        # !! tkey_prefix_tree_#no matter whether ignore

def _mk_null_env():
    _null_env = mk_Environment(param2setting:={}, name2rgnr:={}, name2may_gpreprocess:={}, name2may_gpostprocess6err:={}, name2may_gpostprocess6ok:={}, name2force_postprocess_when_ignore:={})
    return _null_env
#bug:_null_env = _mk_null_env()
#   since cache... eg:required_num_tokens6backward6cenv_()

def mk_null_env4main_rgnr_(main_rgnr, /):
    check_type_le(IRecognizerLLoo, main_rgnr)
    return getset_external_cache4func(get_vs_set_vs_set_ex:=1, _mk_null_env4main_rgnr, main_rgnr)
def _mk_null_env4main_rgnr(main_rgnr, /):
    return _mk_null_env()


def tokenize__chars_(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, chr_tgbegin, chars, /, *, to_flatten:bool, max_num_tokens6backward4low_lvl:'deprecated'=0, max_num_tokens6backward4high_lvl=0, may_env4tknz=None):
    'may_tkey2tdat2tdat__7high_lvl_tkd/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> PositionInfo4Gap__text_file -> Iter char -> high_lvl_istream'
    args8chars = mk_args8chars5chars_(chr_tgbegin, chars)
    return tokenize__args8chars_(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, args8chars, to_flatten=to_flatten, max_num_tokens6backward4low_lvl=max_num_tokens6backward4low_lvl, max_num_tokens6backward4high_lvl=max_num_tokens6backward4high_lvl, may_env4tknz=may_env4tknz)
def tokenize__file_(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, chr_tgbegin, ifile, /, *, to_close:bool, to_flatten:bool, max_num_tokens6backward4low_lvl:'deprecated'=0, max_num_tokens6backward4high_lvl=0, may_env4tknz=None):
    'may_tkey2tdat2tdat__7high_lvl_tkd/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> PositionInfo4Gap__text_file -> input_text_file -> high_lvl_istream'
    args8chars = mk_args8chars5file_(chr_tgbegin, ifile, to_close=to_close)
    return tokenize__args8chars_(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, args8chars, to_flatten=to_flatten, max_num_tokens6backward4low_lvl=max_num_tokens6backward4low_lvl, max_num_tokens6backward4high_lvl=max_num_tokens6backward4high_lvl, may_env4tknz=may_env4tknz)
def tokenize__path_(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, ipath, /, *, to_flatten:bool, encoding, may_pseudo_fname=None, max_num_tokens6backward4low_lvl:'deprecated'=0, max_num_tokens6backward4high_lvl=0, may_env4tknz=None):
    'may_tkey2tdat2tdat__7high_lvl_tkd/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> path<text_file> -> high_lvl_istream'
    args8chars = mk_args8chars5path_(ipath, encoding=encoding, may_pseudo_fname=may_pseudo_fname)
    return tokenize__args8chars_(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, args8chars, to_flatten=to_flatten, max_num_tokens6backward4low_lvl=max_num_tokens6backward4low_lvl, max_num_tokens6backward4high_lvl=max_num_tokens6backward4high_lvl, may_env4tknz=may_env4tknz)

def tokenize__args8chars_(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, args8chars, /, *, to_flatten:bool, max_num_tokens6backward4low_lvl:'deprecated'=0, max_num_tokens6backward4high_lvl=0, may_env4tknz=None):
    'may_tkey2tdat2tdat__7high_lvl_tkd/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> args8chars -> high_lvl_istream # [#args8chars:see:seed.types.IToken#]'
    if not max_num_tokens6backward4low_lvl == 0: raise DeprecationWarning('deprecated:max_num_tokens6backward4low_lvl')
    env = mk_null_env4main_rgnr_(rgnr4tknz) if may_env4tknz is None else may_env4tknz
    may_env4tknz = env
    cenv = env.core_env
    max_num_tokens6backward4tknz = rgnr4tknz.required_num_tokens6backward6cenv_(cenv)
    max_num_tokens6backward4low_lvl = max(max_num_tokens6backward4low_lvl, max_num_tokens6backward4tknz)

    chr_istream = mk_chr_istream5args8chars_(args8chars, max_num_tokens6backward4low_lvl)
    high_lvl_rawstream = tokenize__core_(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, chr_istream, to_flatten=to_flatten, high_lvl_offset=0, may_env4tknz=may_env4tknz)
    high_lvl_istream = mk_istream5rawstream_(high_lvl_rawstream, max_num_tokens6backward4high_lvl)
    return high_lvl_istream

def tokenize__core_(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, chr_istream, /, *, to_flatten:bool, high_lvl_offset=0, may_env4tknz=None):
    'may_tkey2tdat2tdat__7high_lvl_tkd/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> chr_istream{tkey::Char} -> high_lvl_rawstream'
    low_lvl_tgbegin = chr_istream.tell_gap_info()
    low_high_low_triples = _iter_LHLs(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, chr_istream, may_env4tknz)
    high_lvl_rawstream = mk_high_lvl_rawstream5low_high_low_triples_(high_lvl_offset, low_lvl_tgbegin, low_high_low_triples, to_flatten=to_flatten)
    return high_lvl_rawstream

def _iter_LHLs(may_tkey2tdat2tdat__7high_lvl_tkd, may_tkeys8noise4tknz, rgnr4tknz, chr_istream, may_env4tknz, /):
    '-> Iter (ext_info8begin, ext_info8end, tkd)'
    #(rgnr4tknz, env:=mk_null_env4main_rgnr_(rgnr4tknz), gctx:={}, istream:=chr_istream)
    tkey2tdat2tdat__7high_lvl_tkd = {} if may_tkey2tdat2tdat__7high_lvl_tkd is None else may_tkey2tdat2tdat__7high_lvl_tkd
    tkeys8noise4tknz = () if may_tkeys8noise4tknz is None else may_tkeys8noise4tknz
    #bug:env = _null_env if may_env4tknz is None else may_env4tknz
    #   since cache... eg:required_num_tokens6backward6cenv_()
    env = mk_null_env4main_rgnr_(rgnr4tknz) if may_env4tknz is None else may_env4tknz
    while not chr_istream.eof:
        ext_info8begin = chr_istream.tell_ext_info()
        reply = recognize_(rgnr4tknz, env, gctx:={}, chr_istream)
        ext_info8end = reply.ext_info8end
        assert ext_info8end == chr_istream.tell_ext_info()
        if not reply.ok:raise SyntaxError(ext_info8begin, ext_info8end, reply.errmsg)
        if ext_info8begin == ext_info8end:raise Exception('nullable token')
        oresult = reply.oresult
        check_type_is(Cased, oresult)
        may_tdat2tdat__7high_lvl_tkd = tkey2tdat2tdat__7high_lvl_tkd.get(oresult.case)
        oresult = oresult.fmap4payload(may_tdat2tdat__7high_lvl_tkd)

        low_lvl_tgbegin4tokens = ext_info8begin.gap_info
        high_lvl_tkd = oresult
        low_lvl_tgend4tokens = ext_info8end.gap_info
        if not high_lvl_tkd.case in tkeys8noise4tknz:
            yield (low_lvl_tgbegin4tokens, high_lvl_tkd, low_lvl_tgend4tokens)


######################
######################
def _spost4xquot(oresult, /):
    'oresult/(char, [(meta_vs_char, char)], char) -> oresult/str'
    #rgnr8squot_str
    #rgnr8dquot_str
    def f():
        check_type_is(tuple, oresult)
        q0, body, q1 = oresult
        check_char(q0)
        check_char(q1)
        assert q0 == q1
        check_type_is(tuple, body)
        yield q0
        for (meta_vs_char, char) in body:
            if not meta_vs_char:
                #meta
                yield "\\"
            yield char
        yield q1
    return ''.join(f(oresult))
def _spost4xint(oresult, /):
    'oresult/recur_tuple<str> -> oresult/str'
    #rgnr8uint
    #rgnr8int
    def f(x):
        if type(x) is str:
            yield x
            return
        check_type_is(tuple, x)
        for it in map(f, x):
            yield from it
    return ''.join(f(oresult))
def _mk_common_rgnr4tknz():
    '-> (ns4common_rgnr4tknz, (xqset2rgnr4tdat_, xqset2rgnr4tkey_, tkey2rgnr4tdat_, tkey2rgnr4tkey_), (xqset2both_rgnrs4tdat_, xqset2both_rgnrs4tkey_, tkey2both_rgnrs4tdat_, tkey2both_rgnrs4tkey_), (xqset2rgnr4tkd_, tkey2rgnr4tkd_))'
    ######################
    from seed.tiny import MapView
    from seed.types.Namespace import NamespaceForbidModify
    ######################

    from seed.types.IToken import TokenKeyQuerySet5xqset
    from seed.types.IToken import char_qset__isdecimal, char_qset__isspace, char_qset__py_regex__w, char_qset__py_regex__hexdigit_underscore, char_qset__py_regex__digit_underscore, char_qset__py_regex__bit_underscore, char_qset__py_regex__octal_digit_underscore
        #, char_qset__py_regex__hexdigit, char_qset__py_regex__digit, char_qset__py_regex__bit, char_qset__py_regex__octal_digit
    from seed.types.Tester import Tester__eq_obj, Tester__in_obj
    ######################
    tkn_qset5xqset_ = TokenKeyQuerySet5xqset
    mkrs = Makers4IRecognizerLLoo
    ######################
    ######################
    xqset2rgnr4tdat_ = lambda xqset:mkrs.spost__tkn2tdat_(mkrs.token_(tkn_qset5xqset_(xqset)))
        # xqset<tkey> -> rgnr{tkn -> tdat}
    xqset2rgnr4tkey_ = lambda xqset:mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(xqset)))
        # xqset<tkey> -> rgnr{tkn -> ttkey}
    ######################
    tkey2rgnr4tdat_ = lambda tkey:xqset2rgnr4tdat_(Tester__eq_obj(tkey))
        # tkey -> rgnr{tkn -> tdat}
    tkey2rgnr4tkey_ = lambda tkey:xqset2rgnr4tkey_(Tester__eq_obj(tkey))
        # tkey -> rgnr{tkn -> ttkey}
    ######################
    xqset2both_rgnrs4tdat_ = lambda xqset:(xqset2rgnr4tdat_(xqset), xqset2rgnr4tdat_(~xqset))
    xqset2both_rgnrs4tkey_ = lambda xqset:(xqset2rgnr4tkey_(xqset), xqset2rgnr4tkey_(~xqset))
    ######################
    tkey2both_rgnrs4tdat_ = lambda tkey:xqset2both_rgnrs4tdat_(Tester__eq_obj(tkey))
    tkey2both_rgnrs4tkey_ = lambda tkey:xqset2both_rgnrs4tkey_(Tester__eq_obj(tkey))
    ######################
    xqset2rgnr4tkd_ = lambda xqset:mkrs.spost__tkn2tkd_(mkrs.token_(tkn_qset5xqset_(xqset)))
        # xqset<tkey> -> rgnr{tkn -> tkd}
    tkey2rgnr4tkd_ = lambda tkey:xqset2rgnr4tkd_(Tester__eq_obj(tkey))
        # tkey -> rgnr{tkn -> tkd}
    ######################
    (xqset2rgnr4tdat_, xqset2rgnr4tkey_, tkey2rgnr4tdat_, tkey2rgnr4tkey_)
    (xqset2both_rgnrs4tdat_, xqset2both_rgnrs4tkey_, tkey2both_rgnrs4tdat_, tkey2both_rgnrs4tkey_)
    (xqset2rgnr4tkd_, tkey2rgnr4tkd_)
    ######################
    ig_ = lambda x:(x, 0)
    ######################
    rgnr8digit_underscore = xqset2rgnr4tkey_(char_qset__py_regex__digit_underscore)
    rgnr8hexdigit_underscore = xqset2rgnr4tkey_(char_qset__py_regex__hexdigit_underscore)
    rgnr8bit_underscore = xqset2rgnr4tkey_(char_qset__py_regex__bit_underscore)
    rgnr8octal_digit_underscore = xqset2rgnr4tkey_(char_qset__py_regex__octal_digit_underscore)

    rgnr8digit = xqset2rgnr4tkey_(char_qset__isdecimal)
    rgnr8space = xqset2rgnr4tkey_(char_qset__isspace)
    rgnr8word_body_char = xqset2rgnr4tkey_(char_qset__py_regex__w)
    rgnr8sign = xqset2rgnr4tkey_(Tester__in_obj(tuple('+-')))
    rgnr8zero = tkey2rgnr4tkey_('0')
    rgnr8Bb = xqset2rgnr4tkey_(Tester__in_obj(tuple('Bb')))
    rgnr8Oo = xqset2rgnr4tkey_(Tester__in_obj(tuple('Oo')))
    rgnr8Xx = xqset2rgnr4tkey_(Tester__in_obj(tuple('Xx')))
    rgnr8uint_hdr_0B_0b = mkrs.serial_([rgnr8zero, rgnr8Bb, False])
    rgnr8uint_hdr_0O_0o = mkrs.serial_([rgnr8zero, rgnr8Oo, False])
    rgnr8uint_hdr_0X_0x = mkrs.serial_([rgnr8zero, rgnr8Xx, False])
    rgnr8both_quot = xqset2rgnr4tkey_(Tester__in_obj(tuple('"' "'")))
    rgnr8sharp = tkey2rgnr4tkey_('#')
    (rgnr8underscore, rgnr8not_underscore) = tkey2both_rgnrs4tkey_('_')
    (rgnr8eol, rgnr8not_eol) = tkey2both_rgnrs4tkey_('\n')
    rgnr8eof = mkrs.rgnr__eof
    rgnr8eol_eof = mkrs.priority_parallel_([rgnr8eol, rgnr8eof])
    (rgnr8reverse_slash, rgnr8not_reverse_slash) = tkey2both_rgnrs4tkey_('\\')
        # reverse solidus
        # reverse slash
    rgnr8any_char = mkrs.spost__tkn2tkey_(mkrs.rgnr__any_token)
    rgnr8xchar = mkrs.priority_parallel_([mkrs.tag_(rgnr8not_reverse_slash, True), mkrs.tag_(mkrs.unbox_tuple_(1, 0, True, [rgnr8reverse_slash, rgnr8any_char]), False)])
        # cased meta_vs_char
    ######################
    def xquot2rgnr8xquot_str_(xquot, /):
        'xquot/char -> rgnr8xquot_str'
        (rgnr8xquot, rgnr8not_xquot) = tkey2both_rgnrs4tkey_(xquot)
        rgnr8xquot_str_item = mkrs.unbox_tuple_(1, 1, True, [mkrs.not_followed_by_(rgnr8xquot), rgnr8xchar])
        rgnr8xquot_str_body = mkrs.many_(rgnr8xquot_str_item)
        _rgnr8xquot_str = mkrs.serial_([rgnr8xquot, rgnr8xquot_str_body, rgnr8xquot]) #not between_
        rgnr8xquot_str = mkrs.spostprocess_(_rgnr8xquot_str, None, _spost4xquot)
        return rgnr8xquot_str
    ######################
    def mk_uint8prefix__xxx_body_(rgnr8xxx_digit_underscore, /):
        rgnr8uint8prefix__xxx_body = mkrs.unbox_tuple_(1, 3, False, [mkrs.not_followed_by_(rgnr8underscore), mkrs.many_(rgnr8xxx_digit_underscore, 1), mkrs.not_followed_by_(rgnr8word_body_char)])
        return rgnr8uint8prefix__xxx_body
    ######################
    rgnr8spaces0 = mkrs.many_(rgnr8space)
    rgnr8spaces1 = mkrs.many_(rgnr8space, 1)
    rgnr8digits1 = mkrs.many_(rgnr8digit, 1)
    rgnr8word_body_chars1 = mkrs.many_(rgnr8word_body_char, 1)
    ######################
    rgnr8identifier8prefix = mkrs.unbox_tuple_(1, 1, True, [mkrs.not_followed_by_(rgnr8digit), rgnr8word_body_chars1])
    rgnr8identifier7nontouch_xquot = mkrs.unbox_tuple_(0, 2, False, [rgnr8identifier8prefix, mkrs.not_followed_by_(rgnr8both_quot)])
    rgnr8identifier = rgnr8identifier8prefix
        # xxx: rgnr8identifier7nontouch_xquot
        #       <<== identifier inside quot

    #####
    #xxx:rgnr8digits1
    rgnr8uint8prefix__decimal_body = mk_uint8prefix__xxx_body_(rgnr8digit_underscore)
    rgnr8uint8prefix__hexadecimal_body = mk_uint8prefix__xxx_body_(rgnr8hexdigit_underscore)
    rgnr8uint8prefix__binary_body = mk_uint8prefix__xxx_body_(rgnr8bit_underscore)
    rgnr8uint8prefix__octal_body = mk_uint8prefix__xxx_body_(rgnr8octal_digit_underscore)
    #####
    rgnr8uint8prefix__decimal = mkrs.serial_([ig_(mkrs.not_followed_by_(rgnr8zero)), mkrs.constant_loader_(mk_Right(())), True, rgnr8uint8prefix__decimal_body])
    rgnr8uint8prefix__hexadecimal = mkrs.serial_([rgnr8uint_hdr_0X_0x, False, rgnr8uint8prefix__hexadecimal_body])
    rgnr8uint8prefix__octal = mkrs.serial_([rgnr8uint_hdr_0O_0o, False, rgnr8uint8prefix__octal_body])
    rgnr8uint8prefix__binary = mkrs.serial_([rgnr8uint_hdr_0B_0b, False, rgnr8uint8prefix__binary_body])
    #####
    rgnr8uint8prefix__dec_hex_bin_oct = mkrs.priority_parallel_([rgnr8uint8prefix__decimal, rgnr8uint8prefix__hexadecimal, rgnr8uint8prefix__binary, rgnr8uint8prefix__octal])
    #xxx:rgnr8digits1
    rgnr8uint__dec_hex_bin_oct = mkrs.unbox_tuple_(0, 2, False, [rgnr8uint8prefix__dec_hex_bin_oct, mkrs.not_followed_by_(rgnr8word_body_char)])
        # xxx: , mkrs.not_followed_by_(rgnr8both_quot)
        #       <<== uint inside quot
    ######################
    rgnr8uint = mkrs.spostprocess_(rgnr8uint__dec_hex_bin_oct, None, _spost4xint)
    _rgnr8int = mkrs.serial_([rgnr8sign, (echo or ig_)(rgnr8spaces0), True, rgnr8uint])
    rgnr8int = mkrs.spostprocess_(_rgnr8int, None, _spost4xint)
    del _rgnr8int
    rgnr8comment = mkrs.between_(rgnr8sharp, rgnr8eol_eof, mkrs.many_(rgnr8not_eol))
    rgnr8squot_str = xquot2rgnr8xquot_str_("'")
    rgnr8dquot_str = xquot2rgnr8xquot_str_('"')
    ######################
    nm2rgnr = dict(locals())
    nm2rgnr = {nm:v for nm, v in nm2rgnr.items() if isinstance(v, IRecognizerLLoo)}
    ns4common_rgnr4tknz = NamespaceForbidModify(nm2rgnr)
        #ns-namespace
    return (ns4common_rgnr4tknz
    ,(xqset2rgnr4tdat_, xqset2rgnr4tkey_, tkey2rgnr4tdat_, tkey2rgnr4tkey_)
    ,(xqset2both_rgnrs4tdat_, xqset2both_rgnrs4tkey_, tkey2both_rgnrs4tdat_, tkey2both_rgnrs4tkey_)
    ,(xqset2rgnr4tkd_, tkey2rgnr4tkd_)
    )
#end-def _mk_common_rgnr4tknz():
(ns4common_rgnr4tknz
,(xqset2rgnr4tdat_, xqset2rgnr4tkey_, tkey2rgnr4tdat_, tkey2rgnr4tkey_)
,(xqset2both_rgnrs4tdat_, xqset2both_rgnrs4tkey_, tkey2both_rgnrs4tdat_, tkey2both_rgnrs4tkey_)
,(xqset2rgnr4tkd_, tkey2rgnr4tkd_)
) = _mk_common_rgnr4tknz()

#if 0b0000:print_err(sorted(ns4common_rgnr4tknz))
all_name_set4common_rgnr4tknz = frozenset(ns4common_rgnr4tknz)
assert all_name_set4common_rgnr4tknz == (
__:=frozenset(r'''
rgnr8uint
rgnr8underscore
rgnr8uint8prefix__binary
rgnr8Xx
rgnr8identifier
rgnr8xchar
rgnr8space
rgnr8reverse_slash
rgnr8uint__dec_hex_bin_oct
rgnr8Oo
rgnr8identifier8prefix
rgnr8zero
rgnr8sign
rgnr8uint8prefix__octal
rgnr8uint8prefix__hexadecimal
rgnr8not_eol
rgnr8uint_hdr_0X_0x
rgnr8eol_eof
rgnr8uint8prefix__dec_hex_bin_oct
rgnr8uint_hdr_0O_0o
rgnr8any_char
rgnr8uint8prefix__decimal_body
rgnr8uint_hdr_0B_0b
rgnr8digit_underscore
rgnr8word_body_chars1
rgnr8uint8prefix__hexadecimal_body
rgnr8uint8prefix__octal_body
rgnr8both_quot
rgnr8squot_str
rgnr8dquot_str
rgnr8bit_underscore
rgnr8not_underscore
rgnr8int
rgnr8octal_digit_underscore
rgnr8uint8prefix__binary_body
rgnr8hexdigit_underscore
rgnr8uint8prefix__decimal
rgnr8digit
rgnr8word_body_char
rgnr8identifier7nontouch_xquot
rgnr8eol
rgnr8not_reverse_slash
rgnr8spaces1
rgnr8eof
rgnr8spaces0
rgnr8digits1
rgnr8sharp
rgnr8Bb
rgnr8comment
'''.split()#'''
)), (' '.join(all_name_set4common_rgnr4tknz), __-all_name_set4common_rgnr4tknz, all_name_set4common_rgnr4tknz-__)

######################
class IHelper4Tokenization(ABC):
    r'''[[[
    ._keyword_tkeys_ = ... # {tkey}/{str}
    ._noise_tkeys_ = ... # {tkey}/{str}
    #xxx: ._goal_name4rgnr4tknz_ = ... # str

    #rgnr<tkey>
    .{_prefix4attr4rgnr_}tkey{_suffix4attr4rgnr_} = ...

    #mk4tkd<tkey>
    @+whether_default
    @-whether_default
    def {_prefix4attr4mk4tkd_}tkey{_suffix4attr4mk4tkd_}(sf, tkey, oresult, /):
        'tkey -> oresult -> tkd'

    #spost<tkey>
    @+whether_default
    @-whether_default
    def {_prefix4attr4spost_}tkey{_suffix4attr4spost_}(sf, tdat, /):
        'tdat -> tdat'

    <<==:
    (keyword_tkeys, tkey2rgnr_mmk4tkd_mspost, noise_tkeys)

    <<==:
    keyword/operator:
        [tkey == keyword :: constant_string]
        [tdat == None]
        # xxx:[tdat == tkey]
        => keyword_tkeys
    rgnr/regex:
        {tkey:(rgnr, may_tkd_mkr, may_spostprocess)}
        => tkey2rgnr_mmk4tkd_mspost
        [mk4tkd/tkd_mkr :: tkey -> oresult -> tkd]
            # allow alter tkey, eg: [tkd := oresult]
            # default=Cased
        [spost/spostprocess :: tdat -> tdat]
            # after tkd_mkr
            # fmap<tkd>
            # default=echo
    noise:
        {tkey}
        => noise_tkeys

    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def _keyword_tkeys_(sf, /):
        '-> {tkey}/{str}'
    @property
    @abstractmethod
    def _noise_tkeys_(sf, /):
        '-> {tkey}/{str}'

    @property
    @abstractmethod
    def _prefix4attr4rgnr_(sf, /):
        '-> str'
    @property
    @abstractmethod
    def _prefix4attr4mk4tkd_(sf, /):
        '-> str'
    @property
    @abstractmethod
    def _prefix4attr4spost_(sf, /):
        '-> str'

    @property
    @abstractmethod
    def _suffix4attr4rgnr_(sf, /):
        '-> str'
    @property
    @abstractmethod
    def _suffix4attr4mk4tkd_(sf, /):
        '-> str'
    @property
    @abstractmethod
    def _suffix4attr4spost_(sf, /):
        '-> str'
#end-class IHelper4Tokenization(ABC):
class whether_default:
    r'''[[[
    usage:
    @remove_default_methods_
    class C:
        @+whether_default
        def f(sf, ...):
            ...
        @-whether_default
        def g(sf, ...):
            ...
    # C.f: be deleted
    # C.g: remain

    #]]]'''#'''
    def __pos__(sf, /):
        return _is_default
    def __neg__(sf, /):
        return _not_default
def whether_default_(f, /, *tmay_default):
    '-> bool'
    assert len(tmay_default) < 2
    b = getattr(f, '_is_default_', *tmay_default)
    check_type_is(bool, b)
    return b
def _not_default(f, /):
    f._is_default_ = False
    return f
def _is_default(f, /):
    f._is_default_ = True
    return f
def remove_default_methods_(cls, /):
    'remove 『@whether_default<newline>def xxx(...):...』'
    nms = [nm for nm in dir(cls) if whether_default_(getattr(cls, nm), False)]
    for nm in nms:
        delattr(cls, nm)
    return cls
whether_default = whether_default()
#end-class whether_default:

@remove_default_methods_
class BaseHelper4Tokenization(IHelper4Tokenization):
    ___no_slots_ok___ = True
    #a possible config
    #@override
    _keyword_tkeys_ = frozenset()
    _noise_tkeys_ = frozenset()

    #@override
    _prefix4attr4rgnr_ = ''
    _prefix4attr4mk4tkd_ = '_tkd5'
    _prefix4attr4spost_ = '_spost4'

    #@override
    _suffix4attr4rgnr_ = ''
    _suffix4attr4mk4tkd_ = ''
    _suffix4attr4spost_ = ''

    @+whether_default
    def f(sf, /):
        'default'
BaseHelper4Tokenization()
assert not hasattr(BaseHelper4Tokenization(), 'f')

def extract_info5hlpr4tknz_(hlpr4tknz, /, *, extra=False):
    'IHelper4Tokenization -> (keyword_tkeys, tkey2rgnr_mmk4tkd_mspost, noise_tkeys) if not extra else ((keyword_tkeys, tkey2rgnr_mmk4tkd_mspost, noise_tkeys),  (num_nonkeyword_rgnrs, num_mk4tkds, num_sposts))'
    ######################
    check_type_le(IHelper4Tokenization, hlpr4tknz)
    check_type_is(bool, extra)
    ######################
    def f(nms8all, prefix, suffix, /):
        L0, L1 = len(prefix), len(suffix)
        L = L0 + L1
        for nm in nms8all:
            if L <= len(nm) and nm.startswith(prefix) and nm.endswith(suffix):
                v = getattr(hlpr4tknz, nm)
                _nm_ = nm[L0:len(nm)-L1]
                    #removeprefix, removesuffix
                yield (_nm_, v)
    ######################
    def g(nms4rgnr, prefix, suffix, /):
        for _nm_ in nms4rgnr:
            nm = f'{prefix}{_nm_}{suffix}'
            m = getattr(hlpr4tknz, nm, None)
            if m is None:
                continue
            f = m
            if not whether_default_(f):
                assert callable(f), (hlpr4tknz, _nm_, nm, f)
                yield (_nm_, f)
        return
    ######################
    nms8all = dir(hlpr4tknz)
    ps4nm_rgnr = [(_nm_, v) for (_nm_, v) in f(nms8all, hlpr4tknz._prefix4attr4rgnr_, hlpr4tknz._suffix4attr4rgnr_) if isinstance(v, IRecognizerLLoo)]

    ######################
    nms4rgnr = tuple(map(fst, ps4nm_rgnr))
    ps4nm_mk4tkd = [*g(nms4rgnr, hlpr4tknz._prefix4attr4mk4tkd_, hlpr4tknz._suffix4attr4mk4tkd_)]
    ps4nm_spost = [*g(nms4rgnr, hlpr4tknz._prefix4attr4spost_, hlpr4tknz._suffix4attr4spost_)]

    ######################
    nm2rgnr = dict(ps4nm_rgnr)
    nm2mk4tkd = dict(ps4nm_mk4tkd)
    nm2spost = dict(ps4nm_spost)
    ######################
    keyword_tkeys = hlpr4tknz._keyword_tkeys_
    noise_tkeys = hlpr4tknz._noise_tkeys_
    tkey2rgnr_mmk4tkd_mspost = {_nm_:(rgnr, nm2mk4tkd.get(_nm_), nm2spost.get(_nm_)) for (_nm_, rgnr) in nm2rgnr.items()}
    ######################
    #num_keywords = len(keyword_tkeys)
    #num_noises = len(noise_tkeys)
    num_nonkeyword_rgnrs = len(tkey2rgnr_mmk4tkd_mspost)
    num_mk4tkds = sum(may_mk4tkd is not None for (rgnr, may_mk4tkd, may_spost) in tkey2rgnr_mmk4tkd_mspost.values())
    num_sposts = sum(may_spost is not None for (rgnr, may_mk4tkd, may_spost) in tkey2rgnr_mmk4tkd_mspost.values())
    if extra:
        return ((keyword_tkeys, tkey2rgnr_mmk4tkd_mspost, noise_tkeys),  (num_nonkeyword_rgnrs, num_mk4tkds, num_sposts))
    return (keyword_tkeys, tkey2rgnr_mmk4tkd_mspost, noise_tkeys)
#end-def extract_info5hlpr4tknz_(hlpr4tknz, /):


######################

def prepare4tokenize_(keyword_tkeys, tkey2rgnr_mmk4tkd_mspost, /):
    r'''[[[
    -> rgnr4tknz

    * preprocess:
        extract_info5hlpr4tknz_+IHelper4Tokenization

    * further-processs:
        * ++noise_tkeys as may_tkeys8noise4tknz
        #* deprecated:[max_num_tokens6backward4tknz := rgnr4tknz.required_num_tokens6backward6cenv_(cenv)]
        ==>>:
        #deprecated:(may_tkeys8noise4tknz, max_num_tokens6backward4tknz) are used in:
        may_tkeys8noise4tknz is used in:
            tokenize__chars_
            tokenize__file_
            tokenize__path_

    #]]]'''#'''
    ######################
    mkrs = Makers4IRecognizerLLoo
    ######################
    #._rgnr4op = mk_rgnr4words_(keyword_tkeys)
    #.rgnr4op = mkrs.spostprocess_(_rgnr4op, None, lambda tkey8op:Cased(tkey8op, None), _force_postprocess_when_ignore_:=True)
    rgnr4op = mk_rgnr4operators_(keyword_tkeys)
        # !! tkey_prefix_tree_#no matter whether ignore
    ######################
    def _iter_tagged_rgnr():
        yield rgnr4op #tagged
        for tkey, (rgnr, may_mk4tkd, may_spost) in tkey2rgnr_mmk4tkd_mspost.items():
            # tag_
            rgnr = mkrs.tag_(rgnr, tkey)
                #_force_postprocess_when_ignore_=True
            mk4tkd = ifNone(may_mk4tkd, Cased)
            if not mk4tkd is Cased:
                rgnr = mkrs.spostprocess_(rgnr, None, _mk_spost6outer__5mk4tkd(mk4tkd), _force_postprocess_when_ignore_=True)

            spost6inner = ifNone(may_spost, echo)
            if not spost6inner is echo:
                rgnr = mkrs.spostprocess_(rgnr, None, _mk_spost6outer__5spost6inner(spost6inner), _force_postprocess_when_ignore_=False)
            yield rgnr
    #end-def _iter_tagged_rgnr():

    rgnr4tknz = mkrs.priority_parallel_(_iter_tagged_rgnr())
    return rgnr4tknz
    #tkeys8noise4tknz = frozenset(noise_tkeys)
    #max_num_tokens6backward4tknz = rgnr4tknz.required_num_tokens6backward6cenv_(cenv)
    #may_env4tknz = None
def _mk_spost6outer__5mk4tkd(mk4tkd, /):
    def spost6outer(tkd, /):
        tkey, oresult = tkd
        tkd = mk4tkd(tkey, oresult)
        check_type_le(Cased, tkd)
        return tkd
    return spost6outer


def _mk_spost6outer__5spost6inner(spost6inner, /):
    def spost6outer(tkd, /):
        tkd = tkd.fmap4payload(spost6inner)
        check_type_le(Cased, tkd)
        return tkd
    return spost6outer
#end-def prepare4tokenize_():
__all__
from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import tokenize__core_, tokenize__args8chars_
from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import tokenize__chars_, tokenize__file_, tokenize__path_
from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import mk_rgnr4words_, mk_rgnr4operators_, mk_rgnr4enum_type_



from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import (
ns4common_rgnr4tknz
,   all_name_set4common_rgnr4tknz
,   xqset2rgnr4tdat_
,   xqset2rgnr4tkey_
,   tkey2rgnr4tdat_
,   tkey2rgnr4tkey_
#
,   xqset2both_rgnrs4tdat_
,   xqset2both_rgnrs4tkey_
,   tkey2both_rgnrs4tdat_
,   tkey2both_rgnrs4tkey_
#
,   xqset2rgnr4tkd_
,   tkey2rgnr4tkd_
#
,IHelper4Tokenization
,   BaseHelper4Tokenization
,   whether_default
,       whether_default_
,       remove_default_methods_
,   extract_info5hlpr4tknz_
,   prepare4tokenize_
)

from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import *
