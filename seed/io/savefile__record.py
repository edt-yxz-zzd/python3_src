#__all__:goto
r'''[[[
e ../../python3_src/seed/io/savefile__record.py
view ../../python3_src/seed/io/savefile__str_tuple.py
view ../../python3_src/seed/io/savefile/unbuffered_growonly_dict_in_file.py

seed.io.savefile__record
py -m nn_ns.app.debug_cmd   seed.io.savefile__record -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.savefile__record:__doc__ -ht # -ff -df
#######

[[
[记录 == 多个不同类型的条目 :: 元组{条目...}]
[配置{条目} == (_repr_/_to_bytes_, _eval_/_from_bytes_, _locals_, _eq_, 前导符纟条目, 欤不含换行符)]
[配置{记录} == (各种行首耂前导符, 各个条目耂配置)]
[配置{文件} == ({前导符纟记录:配置{记录}}, 欤允许空行, ?encoding?)]
    特殊记录: 前导符纟注释, 前导符纟指令
    指令:『?』
    注释:『#』
    单行:『[,:]=』
    多行:『[,:]> /换行非末行 %换行且末行 +续行非末行 -续行且末行』

newline='\n'
    二进制模式:非空文件=>确保:末字符必是换行符
        确保 换行符 编码后 是 b'\n'

前导符: preceding_word? preface?

自动换行/自动断行???:++num_chars4wrap vs num_bytess4wrap

]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.io.savefile__record   @f


]]]'''#'''
__all__ = r'''
write_cased_records2binary_file_
iter_records5binary_file_
    IConfig4RecordFile
    IConfig4Record
    IConfig4Field6Record
        Config4RecordFile
        Config4Record
        Config4Field6Record


iter_records5binary_file_
    std_iter_records5binary_file_
        iter_records5iter_line_exs_

iter_line_exs5binary_file_
    iter_records5iter_line_exs_
    read_record_field5iter_line_exs_
    read_multiline5iter_line_exs_

write_cased_records2binary_file_
    bytes5cased_record_
        iter_bytess5cased_record_
            iter_strs5cased_record_
                iter_strs5record_
                    iter_strs5field6record_

str5cased_record_
    iter_strs5cased_record_



BaseError
    Error__readline6ibfile
    Error__encode_newline
    FormatError


check_preceding_word_
check_smay_preceding_word_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.from abc import update_abstractmethods
#.#################################
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
#.with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
#.    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
#.from seed.helper.lazy_import__func import force_lazy_imported_func_ # lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
with mk_ctx4lazy_import4funcs_(__name__):
    from bisect import bisect_right
    from codecs import lookup
    #.from functools import cached_property
    from itertools import pairwise #islice
    from operator import is_


    from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_int_ge_lt, check_may_, check_callable

    from seed.tiny_.containers import mk_tuple
    from seed.tiny_.funcs import echo,fst,snd
    from seed.iters.PeekableIterator import echo_or_mk_PeekableIterator
    from seed.helper.repr_input import repr_helper
#.    from seed.tiny_.map_ import map_, cmap_, call_, prepare4call_, dots_
#.    from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
#.    from seed.debug.print_err import print_err
#.    from seed.debug.expectError import expectError
#.    from seed.helper.ifNone import ifNone,ifNonef
#.    from seed.types.Either import mk_Left,mk_Right #Either,Cased
#.    from seed.iters.flatten_recur import flatten_recur
#.    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#.    from seed.func_tools.dot_ import dot_
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#.    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#.    #    def _check6make_(sf, /):
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import collect_tuple_subclasses_with_cached_property
#.    #assert not (__:=collect_tuple_subclasses_with_cached_property(globals(), to_print_err=True)), __
#.#################################
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0



#.#################################
#.from seed.types.LazyList import ToConcatLazyList, decorator4protocol4ToConcatLazyList_
#.from seed.types.LazyList import LazyList, LazyListError
#.from seed.types.LazyList import to_LazyList, to_LazyListIter
#.
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__


def check_preceding_word_(preceding_word, /):
    check_smay_preceding_word_(preceding_word)
    if not preceding_word:raise TypeError
def check_smay_preceding_word_(smay_preceding_word, /):
    check_type_is(str, smay_preceding_word)
    if '\n' in smay_preceding_word:raise TypeError('contain newline', smay_preceding_word)




class BaseError(Exception):pass
class Error__readline6ibfile(BaseError):pass
class Error__encode_newline(BaseError):pass
class FormatError(BaseError):pass


class IConfig4Field6Record(ABC):
    'cfg4field6record'
    __slots__ = ()
    @abstractmethod
    def _repr_(sf, field6record, /):
        'field6record -> str'
    @abstractmethod
    def _eval_(sf, txt, _locals_, /):
        'str -> _locals_ -> field6record'
    @property
    @abstractmethod
    def _locals_(sf, /):
        '-> _locals_'
    @abstractmethod
    def _eq_(sf, lhs_field6record, rhs_field6record, /):
        'field6record -> field6record -> bool'
    @property
    @abstractmethod
    def _smay_preceding_word4field6record_(sf, /):
        '-> (smay preceding_word4field6record)/str'
    @property
    @abstractmethod
    def _whether_no_newlines_(sf, /):
        '-> bool'
    def repr_(sf, field6record, /, *, validate=True):
        'field6record -> str'
        txt = sf._repr_(field6record)
        if validate:
            if not sf._eq_(field6record, (_field6record:=sf.eval_(txt))):raise Exception(sf, field6record, _field6record, txt)
        return txt
    def eval_(sf, txt, /, *, validate=True):
        'str -> field6record'
        if sf._whether_no_newlines_ and '\n' in txt: raise FormatError(sf, txt)
        field6record = sf._eval_(txt, sf._locals_)
        if validate:
            if not txt == (_txt:=sf._repr_(field6record)):raise Exception(sf, txt, _txt, field6record)
        return field6record
    def validate(sf, /):
        sf._locals_.items()
        check_type_is(bool, sf._whether_no_newlines_)
        check_smay_preceding_word_(sf._smay_preceding_word4field6record_)

class IConfig4Record(ABC):
    'cfg4record'
    __slots__ = ()
    @property
    @abstractmethod
    def _may_preceding_word_seq4multiline_(sf, /):
        '-> may [preceding_word4multiline/str{nonempty}]{len==6} # (preceding_word4solo_line, preceding_word4head_line, preceding_word4new_line, preceding_word4new_line_eof, preceding_word4old_line, preceding_word4old_line_eof)'
    @property
    @abstractmethod
    def _seq4cfg4field6record_(sf, /):
        '-> [IConfig4Field6Record]'
    @abstractmethod
    def _mk_record5fields_(sf, fields, /):
        'Iter field6record -> record'
    @abstractmethod
    def _iter_fields5record_(sf, record, /):
        'record -> Iter field6record'
    def record2fields_(sf, record, /):
        'record -> tuple<field6record>'
        fields = mk_tuple(sf._iter_fields5record_(record))
        sf.record5fields_(fields)
        return fields
    def record5fields_(sf, fields, /):
        'Iter field6record -> record'
        fields = mk_tuple(fields)
        if not len(fields) == len(sf._seq4cfg4field6record_):raise TypeError
        record = sf._mk_record5fields_(fields)
        _fields = mk_tuple(sf._iter_fields5record_(record))
        if not len(_fields) == len(sf._seq4cfg4field6record_):raise TypeError
        if not all(map(is_, fields, _fields)):raise TypeError #cfg4field6record._eq_
        return record
    def validate(sf, /):
        ################
        if not None is (preceding_word_seq4multiline:=sf._may_preceding_word_seq4multiline_):
            if not len(preceding_word_seq4multiline) == 6:raise TypeError(preceding_word_seq4multiline)
            for preceding_word in preceding_word_seq4multiline:
                check_preceding_word_(preceding_word)
            for a, b in pairwise(sorted(preceding_word_seq4multiline)):
                if b.startswith(a):raise TypeError(preceding_word_seq4multiline, a, b)
        ################
        if 0 == len(sf._seq4cfg4field6record_):raise TypeError
        sf._seq4cfg4field6record_[:0]
        for cfg4field6record in sf._seq4cfg4field6record_:
            check_type_le(IConfig4Field6Record, cfg4field6record)
            cfg4field6record.validate()
        ################
        if None is sf._may_preceding_word_seq4multiline_:
            for cfg4field6record in sf._seq4cfg4field6record_:
                if not cfg4field6record._whether_no_newlines_:raise TypeError(sf, cfg4field6record)
        ################


class IConfig4RecordFile(ABC):
    'cfg4record_file'
    __slots__ = ()
    @property
    @abstractmethod
    def _cfg4empty_line_(sf, /):
        '-> uint%3 # {0:ignore, 1:data_line/fallback, 2:error}'
    @property
    @abstractmethod
    def _encoding_(sf, /):
        '-> encoding/str'
    @property
    @abstractmethod
    def _sorted_items4preceding_word2cfg4record_(sf, /):
        '-> strict-sorted [(preceding_word4record, cfg4record)] #for:bisect'
    @property
    @abstractmethod
    def _may_fallback_cfg4record_(sf, /):
        '-> may cfg4record'
    def iter_records5binary_file_(sf, ibfile, /):
        'ibfile -> Iter record'
        return std_iter_records5binary_file_(sf, ibfile)
    def validate(sf, /):
        ################
        check_int_ge_lt(0, 3, sf._cfg4empty_line_)
        check_type_is(str, sf._encoding_)
        ################
        x = lookup(sf._encoding_)
        777;x.decode
        777;x.encode
        if not '\n' == b'\n'.decode(sf._encoding_):raise TypeError(sf._encoding_)
        if not b'\n' == '\n'.encode(sf._encoding_):raise TypeError(sf._encoding_)
        ################
        if 0 == len(sf._sorted_items4preceding_word2cfg4record_):raise TypeError
        sf._sorted_items4preceding_word2cfg4record_[0]
        sf._sorted_items4preceding_word2cfg4record_[:1]
        for (preceding_word4record, cfg4record) in sf._sorted_items4preceding_word2cfg4record_:
            check_preceding_word_(preceding_word4record)
            check_type_le(IConfig4Record, cfg4record)
            cfg4record.validate()
        for (a, _), (b, _) in pairwise(sf._sorted_items4preceding_word2cfg4record_):
            if not a < b:raise TypeError(sf._sorted_items4preceding_word2cfg4record_, a, b)
        ################
        check_may_([check_type_le, IConfig4Record], sf._may_fallback_cfg4record_)
        if sf._cfg4empty_line_ == 1 and None is sf._may_fallback_cfg4record_:raise TypeError(sf)
        ################




class Config4Field6Record(IConfig4Field6Record):
    ___no_slots_ok___ = True
    def __init__(sf, _repr_, _eval_, _locals_, _smay_preceding_word4field6record_, _whether_no_newlines_, /):
        check_callable(_repr_)
        check_callable(_eval_)
        sf._rp = _repr_
        sf._vl = _eval_
        sf._d = _locals_
        sf._smw = _smay_preceding_word4field6record_
        sf._noNL = _whether_no_newlines_
        sf.validate()
    def __repr__(sf, /):
        return repr_helper(sf, sf._rp, sf._vl, sf._d, sf._smw, sf._noNL)
    @abstractmethod
    def _repr_(sf, field6record, /):
        return sf._rp(field6record)
    @abstractmethod
    def _eval_(sf, txt, _locals_, /):
        return sf._vl(txt, _locals_)
    @property
    @abstractmethod
    def _locals_(sf, /):
        return sf._d
    @abstractmethod
    def _eq_(sf, lhs_field6record, rhs_field6record, /):
        return lhs_field6record == rhs_field6record
    @property
    @abstractmethod
    def _smay_preceding_word4field6record_(sf, /):
        return sf._smw
    @property
    @abstractmethod
    def _whether_no_newlines_(sf, /):
        return sf._noNL

class Config4Record(IConfig4Record):
    ___no_slots_ok___ = True
    def __init__(sf, record_type, _may_preceding_word_seq4multiline_, _seq4cfg4field6record_, /):
        check_callable(record_type)
        sf._Rcd = record_type
        sf._may_ws = None if None is _may_preceding_word_seq4multiline_ else mk_tuple(_may_preceding_word_seq4multiline_)
        sf._cfgs = mk_tuple(_seq4cfg4field6record_)
        sf.validate()
    def __repr__(sf, /):
        return repr_helper(sf, sf._Rcd, sf._may_ws, sf._cfgs)
    @property
    @override
    def _may_preceding_word_seq4multiline_(sf, /):
        return sf._may_ws
    @property
    @override
    def _seq4cfg4field6record_(sf, /):
        return sf._cfgs
    @override
    def _mk_record5fields_(sf, fields, /):
        return sf._Rcd(*fields)
    @override
    def _iter_fields5record_(sf, record, /):
        return iter(record)

class Config4RecordFile(IConfig4RecordFile):
    ___no_slots_ok___ = True
    def __init__(sf, _cfg4empty_line_, _encoding_, _sorted_items4preceding_word2cfg4record_, _may_fallback_cfg4record_, /):
        sf._caseNUL = _cfg4empty_line_
        sf._enc = _encoding_
        sf._ps = _sorted_items4preceding_word2cfg4record_
        sf._mc = _may_fallback_cfg4record_
        sf.validate()
    def __repr__(sf, /):
        return repr_helper(sf, sf._caseNUL, sf._enc, sf._ps, sf._mc)
    @property
    @override
    def _cfg4empty_line_(sf, /):
        return sf._caseNUL
    @property
    @override
    def _encoding_(sf, /):
        return sf._enc
    @property
    @override
    def _sorted_items4preceding_word2cfg4record_(sf, /):
        return sf._ps
    @property
    @override
    def _may_fallback_cfg4record_(sf, /):
        return sf._mc


#.def read_may_line_ex_(decode_, ibfile, /):
#.    bs8line = ibfile.readline()
#.    if not bs8line:
#.        may_line = None
#.    else:
#.        if not bs8line[-1:] == b'\n':raise TypeError
#.        bs = bs8line[:-1]
#.        if b'\n' in bs:raise TypeError
#.        s = decode_(bs)
#.        if '\n' in s:raise TypeError
#.        may_line = s
#.    return (bs8line, may_line)
def iter_line_exs5binary_file_(encoding, ibfile, /):
    'encoding -> ibfile -> Iter (bs8line, line_content)'
    #encode_ex_ = lookup(encoding).encode
    decode_ex_ = lookup(encoding).decode
    def decode_(bs, /):
        (s, sz7byte) = decode_ex_(bs)
        return s
    for bs8line in ibfile:
        if not bs8line[-1:] == b'\n':raise FormatError(r'file not endswith b"\n"')
        bs = bs8line[:-1]
        if b'\n' in bs:raise Error__readline6ibfile(ibfile)
        s = decode_(bs)
        if '\n' in s:raise Error__encode_newline(encoding)
        yield (bs8line, s)
def iter_records5binary_file_(cfg4record_file, ibfile, /):
    'IConfig4RecordFile -> ibfile -> Iter record'
    return cfg4record_file.iter_records5binary_file_(ibfile)
def std_iter_records5binary_file_(cfg4record_file, ibfile, /):
    'IConfig4RecordFile -> ibfile -> Iter record'
    iter_line_exs = iter_line_exs5binary_file_(cfg4record_file._encoding_, ibfile)
    return iter_records5iter_line_exs_(cfg4record_file, iter_line_exs)
def iter_records5iter_line_exs_(cfg4record_file, iter_line_exs, /):
    'IConfig4RecordFile -> Iter (bs8line, line_content) -> Iter record'
    ps = cfg4record_file._sorted_items4preceding_word2cfg4record_
    it = echo_or_mk_PeekableIterator(iter_line_exs)
    #.while not it.is_empty():
    #.    (bs8line, s) = it.head
    for (bs8line, s) in it:
        #if not bs:
        if not s:
            #empty line
            match cfg4record_file._cfg4empty_line_:
                case 0:
                    #ignore
                    continue
                case 1:
                    #data_line
                    pass
                case 2:
                    #error
                    raise FormatError('empty line')
                case bad:
                    raise TypeError('not in [0,1,2]:', bad)
                #case
            #match
        #

        s
        j = bisect_right(ps, s, key=fst)
        if j and s.startswith(fst(item:=ps[j-1])):
            (preceding_word4record, cfg4record) = item
            _s = s.removeprefix(preceding_word4record)
        elif not None is (fallback_cfg4record:=cfg4record_file._may_fallback_cfg4record_):
            cfg4record = fallback_cfg4record
            _s = s
        else:
            raise Exception('no matched preceding_word4record for:', s, bs8line)
        cfg4record, _s
        it.append_left((bs8line, _s))

        may_preceding_word_seq4multiline = cfg4record._may_preceding_word_seq4multiline_
        cfgs = cfg4record._seq4cfg4field6record_
        fields = []
        for cfg4field6record in cfgs:
            field6record = read_record_field5iter_line_exs_(cfg4field6record, may_preceding_word_seq4multiline, it)
            fields.append(field6record)
        fields
        record = cfg4record.record5fields_(fields)
        yield record

def read_record_field5iter_line_exs_(cfg4field6record, may_preceding_word_seq4multiline, iter_line_exs, /):
    'IConfig4Field6Record -> may [preceding_word4multiline/str{nonempty}]{len==6} -> Iter (bs8line, line_content) -> field6record|^EOFError'
    it = iter(iter_line_exs)
    it = echo_or_mk_PeekableIterator(it)
    for (bs8line, s) in it:
        break
    else:
        raise EOFError
    smay_prw = cfg4field6record._smay_preceding_word4field6record_
    if not s.startswith(smay_prw):raise FormatError(smay_prw, s)
    _s = s.removeprefix(smay_prw)
    if cfg4field6record._whether_no_newlines_:
        txt = _s
    else:
        it.append_left((bs8line, _s))
        txt = read_multiline5iter_line_exs_(may_preceding_word_seq4multiline, it)
    txt
    #.no_NL = cfg4field6record._whether_no_newlines_
    #.if no_NL and '\n' in txt:raise FormatError(cfg4field6record, txt)
    field6record = cfg4field6record.eval_(txt)
    return field6record

def read_multiline5iter_line_exs_(may_preceding_word_seq4multiline, iter_line_exs, /):
    'may [preceding_word4multiline/str{nonempty}]{len==6} -> Iter (bs8line, line_content) -> str|^EOFError'
    it = iter(iter_line_exs)
    it = echo_or_mk_PeekableIterator(it)
    for (bs8line, s) in it:
        break
    else:
        raise EOFError
    if None is may_preceding_word_seq4multiline:
        return s
    (preceding_word4solo_line, preceding_word4head_line, preceding_word4new_line, preceding_word4new_line_eof, preceding_word4old_line, preceding_word4old_line_eof) = preceding_word_seq4multiline = may_preceding_word_seq4multiline
    ss = []
    if not (_put(bs8line, s, preceding_word4solo_line, ss) or _put(bs8line, s, preceding_word4head_line, ss)):raise FormatError(preceding_word_seq4multiline[:2], s, bs8line)

    for (bs8line, s) in it:
        if _put(bs8line, s, preceding_word4old_line, ss):
            continue
        if _put(bs8line, s, preceding_word4old_line_eof, ss):
            break
        ss.append('\n')
        if _put(bs8line, s, preceding_word4new_line, ss):
            continue
        if _put(bs8line, s, preceding_word4new_line_eof, ss):
            break
        raise FormatError(preceding_word_seq4multiline[2:], s, bs8line)
    else:
        raise EOFError
    s = ''.join(ss)
    return s

def _put(bs8line, s, preceding_word, ss, /):
    if (ok:=s.startswith(preceding_word)):
        _s = s.removeprefix(preceding_word)
        ss.append(_s)
    return ok

def write_cased_records2binary_file_(cfg4record_file, obfile, cased_records, /):
    'IConfig4RecordFile -> obfile -> Iter cased_record/(preceding_word4record, record) -> None'
    for cased_record in cased_records:
        bs = bytes5cased_record_(cfg4record_file, cased_record)
        obfile.write(bs)
def bytes5cased_record_(cfg4record_file, cased_record, /):
    'IConfig4RecordFile -> cased_record/(preceding_word4record, record) -> bytes'
    return b''.join(iter_bytess5cased_record_(cfg4record_file, cased_record))
def iter_bytess5cased_record_(cfg4record_file, cased_record, /):
    'IConfig4RecordFile -> cased_record/(preceding_word4record, record) -> Iter bytes'
    encode_ex_ = lookup(cfg4record_file._encoding_).encode
    def encode_(s, /):
        (bs, sz7char) = encode_ex_(s)
        return bs
    return map(encode_, iter_strs5cased_record_(cfg4record_file, cased_record))
def str5cased_record_(cfg4record_file, cased_record, /):
    'IConfig4RecordFile -> cased_record/(preceding_word4record, record) -> str'
    return ''.join(iter_strs5cased_record_(cfg4record_file, cased_record))
def iter_strs5cased_record_(cfg4record_file, cased_record, /):
    'IConfig4RecordFile -> cased_record/(preceding_word4record, record) -> Iter str'
    (preceding_word4record, record) = cased_record
    ps = cfg4record_file._sorted_items4preceding_word2cfg4record_
    j = bisect_right(ps, preceding_word4record, key=fst)
    if j and preceding_word4record == fst(item:=ps[j-1]):
        (_, cfg4record) = item
    elif preceding_word4record == '' and not None is (fallback_cfg4record:=cfg4record_file._may_fallback_cfg4record_):
        cfg4record = fallback_cfg4record
    else:
        raise Exception('no matched preceding_word4record for:', preceding_word4record)
    cfg4record
    yield preceding_word4record
    yield from iter_strs5record_(cfg4record, record)

def iter_strs5record_(cfg4record, record, /):
    'IConfig4Record -> record -> Iter str'
    may_preceding_word_seq4multiline = cfg4record._may_preceding_word_seq4multiline_
    fields = cfg4record.record2fields_(record)
    if not len(cfg4record._seq4cfg4field6record_) ==len(fields):raise TypeError
    for cfg4field6record, field6record in zip(cfg4record._seq4cfg4field6record_, fields):
        yield from iter_strs5field6record_(cfg4field6record, may_preceding_word_seq4multiline, field6record)
def iter_strs5field6record_(cfg4field6record, may_preceding_word_seq4multiline, field6record, /):
    'IConfig4Field6Record -> may [preceding_word4multiline/str{nonempty}]{len==6} -> field6record -> Iter str'
    txt = cfg4field6record.repr_(field6record)
    yield cfg4field6record._smay_preceding_word4field6record_
    if cfg4field6record._whether_no_newlines_:
        if '\n' in txt: raise FormatError(cfg4field6record, field6record, txt)
        yield from ('', txt, '\n')
    elif None is may_preceding_word_seq4multiline:raise TypeError
    else:
        (preceding_word4solo_line, preceding_word4head_line, preceding_word4new_line, preceding_word4new_line_eof, preceding_word4old_line, preceding_word4old_line_eof) = preceding_word_seq4multiline = may_preceding_word_seq4multiline
        ss = txt.split('\n')
        assert ss
        if len(ss) == 1:
            [s] = ss
            yield from (preceding_word4solo_line, s, '\n')
        else:
            if 1:
                yield from (preceding_word4head_line, ss[0], '\n')
            for s in ss[1:-1]:
                yield from (preceding_word4new_line, s, '\n')
            if 1:
                yield from (preceding_word4new_line_eof, ss[-1], '\n')
    return

__all__
from seed.io.savefile__record import IConfig4RecordFile, IConfig4Record, IConfig4Field6Record
from seed.io.savefile__record import Config4RecordFile, Config4Record, Config4Field6Record
from seed.io.savefile__record import iter_records5binary_file_, write_cased_records2binary_file_
from seed.io.savefile__record import *
