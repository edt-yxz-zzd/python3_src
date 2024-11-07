#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/tokenize_utils.py

seed.recognize.recognizer_LLoo__ver2_.tokenize_utils
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo__ver2_.tokenize_utils -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.tokenize_utils:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo__ver2_.tokenize_utils   @f
#]]]'''
__all__ = r'''
mk_rgnr4words_
tokenize__core_
    tokenize__args8chars_
        tokenize__chars_
        tokenize__file_
        tokenize__path_
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
,       mk_gap_position_info_at_ifile_begin
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

from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import recognize_, Environment
from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import Makers4IRecognizerLLoo

from seed.types.Either import Cased, Either
from seed.types.Either import mk_Left, mk_Right

from seed.tiny_.check import check_type_is, check_int_ge

___end_mark_of_excluded_global_names__0___ = ...

def mk_rgnr4words_(words, /):
    '[[tkey]] -> IRecognizerLLoo'
    mkrs = Makers4IRecognizerLLoo
    rgnr = mkrs.tkey_prefix_tree_(tuple((w,w) for w in words))
    return rgnr
def _mk_null_env():
    _null_env = Environment(param2setting:={}, name2rgnr:={}, name2may_gpreprocess:={}, name2may_gpostprocess6err:={}, name2may_gpostprocess6ok:={})
    return _null_env
_null_env = _mk_null_env()


def tokenize__chars_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, chr_tgbegin, chars, /, *, to_flatten:bool, max_num_tokens6backward4low_lvl=0, max_num_tokens6backward4high_lvl=0, may_env4tknz=None):
    'may_tkey2tdat2tdat/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> PositionInfo4Gap__text_file -> Iter char -> high_lvl_istream'
    args8chars = mk_args8chars5chars_(chr_tgbegin, chars)
    return tokenize__args8chars_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, args8chars, to_flatten=to_flatten, max_num_tokens6backward4low_lvl=max_num_tokens6backward4low_lvl, max_num_tokens6backward4high_lvl=max_num_tokens6backward4high_lvl, may_env4tknz=may_env4tknz)
def tokenize__file_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, chr_tgbegin, ifile, /, *, to_close:bool, to_flatten:bool, max_num_tokens6backward4low_lvl=0, max_num_tokens6backward4high_lvl=0, may_env4tknz=None):
    'may_tkey2tdat2tdat/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> PositionInfo4Gap__text_file -> input_text_file -> high_lvl_istream'
    args8chars = mk_args8chars5file_(chr_tgbegin, ifile, to_close=to_close)
    return tokenize__args8chars_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, args8chars, to_flatten=to_flatten, max_num_tokens6backward4low_lvl=max_num_tokens6backward4low_lvl, max_num_tokens6backward4high_lvl=max_num_tokens6backward4high_lvl, may_env4tknz=may_env4tknz)
def tokenize__path_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, ipath, /, *, to_flatten:bool, encoding, may_pseudo_fname=None, max_num_tokens6backward4low_lvl=0, max_num_tokens6backward4high_lvl=0, may_env4tknz=None):
    'may_tkey2tdat2tdat/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> path<text_file> -> high_lvl_istream'
    args8chars = mk_args8chars5path_(ipath, encoding=encoding, may_pseudo_fname=may_pseudo_fname)
    return tokenize__args8chars_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, args8chars, to_flatten=to_flatten, max_num_tokens6backward4low_lvl=max_num_tokens6backward4low_lvl, max_num_tokens6backward4high_lvl=max_num_tokens6backward4high_lvl, may_env4tknz=may_env4tknz)

def tokenize__args8chars_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, args8chars, /, *, to_flatten:bool, max_num_tokens6backward4low_lvl=0, max_num_tokens6backward4high_lvl=0, may_env4tknz=None):
    'may_tkey2tdat2tdat/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> args8chars -> high_lvl_istream # [#args8chars:see:seed.types.IToken#]'
    chr_istream = mk_chr_istream5args8chars_(args8chars, max_num_tokens6backward4low_lvl)
    high_lvl_rawstream = tokenize__core_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, chr_istream, to_flatten=to_flatten, high_lvl_offset=0, may_env4tknz=may_env4tknz)
    high_lvl_istream = mk_istream5rawstream_(high_lvl_rawstream, max_num_tokens6backward4high_lvl)
    return high_lvl_istream

def tokenize__core_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, chr_istream, /, *, to_flatten:bool, high_lvl_offset=0, may_env4tknz=None):
    'may_tkey2tdat2tdat/may {tkey:(tdat->tdat)} -> may_tkeys8noise4tknz/{tkey} -> rgnr4tknz{oresult::Cased}{no:ref} -> chr_istream{tkey::Char} -> high_lvl_rawstream'
    low_lvl_tgbegin = chr_istream.tell_gap_info()
    low_high_low_triples = _iter_LHLs(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, chr_istream, may_env4tknz)
    high_lvl_rawstream = mk_high_lvl_rawstream5low_high_low_triples_(high_lvl_offset, low_lvl_tgbegin, low_high_low_triples, to_flatten=to_flatten)
    return high_lvl_rawstream

def _iter_LHLs(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, chr_istream, may_env4tknz, /):
    '-> Iter (ext_info8begin, ext_info8end, tkd)'
    #(rgnr4tknz, env:=_null_env, gctx:={}, istream:=chr_istream)
    tkey2tdat2tdat = {} if may_tkey2tdat2tdat is None else may_tkey2tdat2tdat
    tkeys8noise4tknz = () if may_tkeys8noise4tknz is None else may_tkeys8noise4tknz
    env = _null_env if may_env4tknz is None else may_env4tknz
    while not chr_istream.eof:
        ext_info8begin = chr_istream.tell_ext_info()
        reply = recognize_(rgnr4tknz, env, gctx:={}, chr_istream)
        ext_info8end = reply.ext_info8end
        assert ext_info8end == chr_istream.tell_ext_info()
        if not reply.ok:raise SyntaxError(ext_info8begin, ext_info8end, reply.errmsg)
        if ext_info8begin == ext_info8end:raise Exception('nullable token')
        oresult = reply.oresult
        check_type_is(Cased, oresult)
        may_tdat2tdat = tkey2tdat2tdat.get(oresult.case)
        oresult = oresult.fmap4payload(may_tdat2tdat)

        low_lvl_tgbegin4tokens = ext_info8begin.gap_info
        high_lvl_tkd = oresult
        low_lvl_tgend4tokens = ext_info8end.gap_info
        if not high_lvl_tkd.case in tkeys8noise4tknz:
            yield (low_lvl_tgbegin4tokens, high_lvl_tkd, low_lvl_tgend4tokens)



__all__
from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import tokenize__core_, tokenize__args8chars_
from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import tokenize__chars_, tokenize__file_, tokenize__path_
from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import mk_rgnr4words_
from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import *
