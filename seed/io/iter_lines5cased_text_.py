#__all__:goto
r'''[[[
e ../../python3_src/seed/io/iter_lines5cased_text_.py

seed.io.iter_lines5cased_text_
py -m nn_ns.app.debug_cmd   seed.io.iter_lines5cased_text_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.iter_lines5cased_text_:__doc__ -ht # -ff -df

[[
源起:用于读取文档中的数据
    view script/枚举冫双幂方和型素数.py
    view ../../python3_src/seed/str_tools/cut_text_by_marker_seq.py
===
++MultiFiles
    to read from tar_lzma_file
        view script/枚举冫加一偶幂型素数.py
            注水解包冫输出文件扌():kw:whether_tar_lzma
]]

py_adhoc_call   seed.io.iter_lines5cased_text_   @f
]]]'''#'''
__all__ = r'''
simplify_cased_text_
    psopen_
        NoCloseFile
        MultiFiles
    text5cased_text_
        slice_
    iter_lines5cased_text_
        iter_lines5text_

iter_eval_lines5cased_text__slice_by_marker_lines_
    iter_lines5cased_text_
        simplify_cased_text_
            psopen_
    iter_slice_lines5cased_text__by_marker_lines_
        iter_slice_lines_by_marker_lines_
            mk_eval_
    iter_eval_lines_
        filter_lines4eval_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from ast import literal_eval
from itertools import islice, takewhile, dropwhile
from seed.tiny_.check import check_type_is, check_int_ge
from seed.tiny_.funcs import echo
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

def simplify_cased_text_(cased_text, /, *, will_use_WITH_AS=False):
    r'''[[[
    :: cased_text -> simplified_cased_text

    [simplified_cased_text <: cased_text]

    cased_text ::=
        | ('text', txt, *args)
        | ('file', ifile, to_close, *args)
        | ('path', path, encoding_or_kwds4open, *args)
        | ('stdin', *args)
        | ('tar_lzma_path', path, encoding, *args)

    simplified_cased_text ::=
        | ('text', txt, *args)
        | ('file', ifile, to_close, *args)

    [txt :: str]
    [to_close :: bool]
    [encoding_or_kwds4open :: (str|Mapping|args4dict)]

    usage:
    match simplify_cased_text_(cased_text):
        case ('text', txt, *args):
            (txt, *args)
        case ('file', ifile, to_close, *args):
            #bug:with psopen_(ifile, to_close=to_close):
            #   !! NoCloseFile,MultiFiles
            with psopen_(ifile, to_close=to_close) as ifile:
                (ifile, *args)
        case _:
            raise Exception(cased_text)

    #]]]'''#'''
    #match simplify_cased_text_(cased_text):
    match cased_text:
        case ('text', txt, *args):
            check_type_is(str, txt)
            simplified_cased_text = cased_text
        case ('file', ifile, to_close, *args):
            check_type_is(bool, to_close)
            simplified_cased_text = cased_text
        case ('path', path, encoding_or_kwds4open, *args):
            #with open(path, 'rt', encoding=encoding) as ifile:
            if type(encoding_or_kwds4open) is str:
                encoding = encoding_or_kwds4open
                kwds4open = dict(encoding=encoding)
            else:
                kwds4open = encoding_or_kwds4open
                kwds4open = dict(kwds4open)
            kwds4open
            ifile = open(path, 'rt', **kwds4open)
            simplified_cased_text = ('file', ifile, to_close:=True, *args)
        case ('stdin', *args):
            from sys import stdin as ifile
            simplified_cased_text = ('file', ifile, to_close:=False, *args)
        case ('tar_lzma_path', path, encoding, *args):
            #from seed.for_libs.for_tarfile import iter_read_solo_tarfile_
            #def iter_read_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}):
            #    '-> Iter line/(bytes if not xencoding4data else str)|^Error__not_solo_tarfile'
            from seed.for_libs.for_tarfile import double_open_solo_tarfile_# group_open_solo_tarfile_, read_solo_tarfile_, iter_read_solo_tarfile_
            #def double_open_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}, group=False):
            #    '-> ((ifile4tar, (ifile4data|ifile4text))|grp_ctx_mngr{(ifile4tar, ifile4data_or_ifile4text)})/(TarFile, (BufferedReader if not xencoding4data else TextIOWrapper) if not group else GroupContextManager)|^Error__not_solo_tarfile'
            check_type_is(str, encoding)
            (ifile4tar, ifile4text) = double_open_solo_tarfile_(path, xencoding4data=encoding)
            if 0:
                del ifile4tar
                simplified_cased_text = ('file', ifile:=ifile4text, to_close:=True, *args)
            ifile = MultiFiles([ifile4tar], ifile4text)
            simplified_cased_text = ('file', ifile, to_close:=True, *args)
        case _:
            raise Exception(cased_text)
    simplified_cased_text
    if will_use_WITH_AS:
        match simplified_cased_text:
            case ('file', ifile, False, *args):
                ifile = psopen_(ifile)
                simplified_cased_text = ('file', ifile, to_close:=True, *args)
        simplified_cased_text
    simplified_cased_text
    return simplified_cased_text

class MultiFiles:
    def __init__(sf, other_fileobjs, fileobj, /):
        sf.other_fileobjs = tuple(other_fileobjs)
        sf.fileobj = fileobj
    def __enter__(sf, /):
        fl = sf.fileobj
        return type(fl).__enter__(fl)
    def __exit__(sf, /, *args):
        for fl in sf.other_fileobjs:
            type(fl).__exit__(fl, *args)
        fl = sf.fileobj
        return type(fl).__exit__(fl, *args)


class NoCloseFile:
    def __init__(sf, fileobj, /):
        sf.fileobj = fileobj
    def __enter__(sf, /):
        #return sf.fileobj
        fl = sf.fileobj
        return type(fl).__enter__(fl)
    def __exit__(sf, /, *args):
        return
        fl = sf.fileobj
        return type(fl).__exit__(fl, *args)
def psopen_(fileobj, /, *, to_close):
    if to_close:
        return fileobj
    return NoCloseFile(fileobj)
def text5cased_text_(cased_text, /):
    match simplify_cased_text_(cased_text):
        case ('text', txt, *args):#args=(begin=None, end=None)
            txt = slice_(txt, *args)
        case ('file', ifile, to_close):#no args
            with psopen_(ifile, to_close=to_close) as ifile:
                txt = ifile.read()
        case _:
            raise Exception(cased_text)
    return txt
def iter_lines5cased_text_(cased_text, /):
    match simplify_cased_text_(cased_text):
        case ('text', txt, *args):#args=(begin=None, end=None)
            yield from iter_lines5text_(txt, *args)
        case ('file', ifile, to_close):#no args
            with psopen_(ifile, to_close=to_close) as ifile:
                yield from ifile
        case _:
            raise Exception(cased_text)
    return

def slice_(array, begin=None, end=None, /):
    (begin, end, _1) = slice(begin, end).indices(len(array))
    return array if begin == 0 and end == len(array) else array[begin:end]
def iter_lines5text_(txt, begin=None, end=None, /):
    check_type_is(str, txt)
    #range(len(txt))[begin:end]
    (begin, end, _1) = slice(begin, end).indices(len(txt))
    i = begin
    while i < end:
        # [i < end]
        smay_jmm = txt.find('\n', i, end)
        # [smay_jmm == -1]or[i <= smay_jmm < end]
        if smay_jmm < 0:
            # [smay_jmm == -1]
            j = end
            # [j == end]
            # !! [i < end]
            # [i < j == end]
            # [i < j <= end]
        else:
            # [i <= smay_jmm < end]
            jmm = smay_jmm
            # [i <= jmm < end]
            j = 1+jmm
            # [i < j <= end]
        # [i < j <= end]
        line = txt[i:j]
        assert line
        yield line
        777;    i = j
        # [i == j <= end]
    return
def iter_slice_lines_by_marker_lines_(lines, may_line_prefix4begin_marker, may_line_prefix4end_marker, /):
    iter_lines = lines = iter(lines)
    if not may_line_prefix4begin_marker is None:
        line_prefix4begin_marker = may_line_prefix4begin_marker
        # seek to begin
        iter_lines = dropwhile(lambda line:not line.startswith(line_prefix4begin_marker), iter_lines)
        iter_lines = islice(iter_lines, 1, None)
    iter_lines
    if not may_line_prefix4end_marker is None:
        line_prefix4end_marker = may_line_prefix4end_marker
        iter_lines = takewhile(lambda line:not line.startswith(line_prefix4end_marker), iter_lines)
    iter_lines
    return iter_lines

def mk_eval_(may_eval_or_name, /):
    eval_ = None
    if not may_eval_or_name:
        eval_ = literal_eval
    elif type(may_eval_or_name) is str:
        nm4eval = may_eval_or_name
        match nm4eval:
            case 'literal_eval':
                eval_ = literal_eval
            case 'eval':
                eval_ = eval
            case 'echo':
                eval_ = echo
    eval_
    if eval_ is None:
        raise Exception(f'unknown eval_:{may_eval_or_name!r}')
    eval_
    assert callable(eval_)
    return eval_

def filter_lines4eval_(lines, /):
    return filter(lambda line:not line[:1] in ' #>.\t', lines)
def iter_eval_lines_(may_eval_or_name, may_filter_lines4eval_, lines, /):
    f = filter_lines4eval_ if may_filter_lines4eval_ is None else may_filter_lines4eval_
    eval_ = mk_eval_(may_eval_or_name)
    return map(eval_, f(lines))
    return map(eval_, filter_lines4eval_(lines))

def iter_slice_lines5cased_text__by_marker_lines_(cased_text, may_line_prefix4begin_marker, may_line_prefix4end_marker, /):
    iter_lines = iter_lines5cased_text_(cased_text)
    iter_lines = iter_slice_lines_by_marker_lines_(iter_lines, may_line_prefix4begin_marker, may_line_prefix4end_marker)
    return iter_lines
def iter_eval_lines5cased_text__slice_by_marker_lines_(cased_text, may_line_prefix4begin_marker, may_line_prefix4end_marker, /, *, may_eval_or_name='literal_eval', may_filter_lines4eval_=filter_lines4eval_):
    iter_lines = iter_slice_lines5cased_text__by_marker_lines_(cased_text, may_line_prefix4begin_marker, may_line_prefix4end_marker)
    return iter_eval_lines_(may_eval_or_name, may_filter_lines4eval_, iter_lines)










__all__
from seed.io.iter_lines5cased_text_ import iter_eval_lines5cased_text__slice_by_marker_lines_, iter_slice_lines5cased_text__by_marker_lines_
from seed.io.iter_lines5cased_text_ import text5cased_text_, iter_lines5cased_text_
from seed.io.iter_lines5cased_text_ import simplify_cased_text_#++kw:will_use_WITH_AS
from seed.io.iter_lines5cased_text_ import simplify_cased_text_, psopen_, slice_, iter_lines5text_, iter_slice_lines_by_marker_lines_, mk_eval_, filter_lines4eval_, iter_eval_lines_
from seed.io.iter_lines5cased_text_ import *
