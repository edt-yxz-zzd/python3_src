#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/cmdline/txt_process.py
see:
    view ../../python3_src/seed/recognize/cmdline/adhoc_argparser.py

处理模式:
    +行预处理
        行过滤
        行处理
        行过滤囗行处理
    块读入囗块写出
    块读入囗集合输出
换行模式:
    flush:
        print.flush
        file.flush
    print.end:
        '', '\n', ...
    file.write:
        写:
            None, '\r', '\r\n'
                '\n' --> ???
            '', '\n'
                os.linesep
    file.read/readline:
        读:
            None
                ('\r', '\n', '\r\n') --> '\n'
            '', '\r', '\n', '\r\n'
                不变



seed.recognize.cmdline.txt_process
py -m nn_ns.app.debug_cmd   seed.recognize.cmdline.txt_process -x
py -m nn_ns.app.doctest_cmd seed.recognize.cmdline.txt_process:__doc__ -ff -v

from seed.recognize.cmdline.txt_process import main, line_filter
from seed.recognize.cmdline.txt_process import open_ioFiles_, mk_may_Path4file_, mk_may_ioPaths4file_
from seed.recognize.cmdline.txt_process import *


echo $'\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None --cased_func_or_args4islice__eithers:

echo $'\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None --cased_func_or_args4islice__eithers: --may_fmt4out:':{0!s}{1!r}:'
:'\n'::abc'\n'::123'\n'::'\n':
    echo ~ println --- append '\n'

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None --cased_func_or_args4islice__eithers: --may_fmt4out:':{0!s}{1!r}:'
:'\n'::abc'\n'::123'\n':

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None --cased_func_or_args4islice__eithers: --may_fmt4out:':{0!s}{1!r}:' -without_last_line_if_empty
:'\n'::abc'\n'::123'\n'::'':

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None --cased_func_or_args4islice__eithers: --may_fmt4out:':{0!s}{1!r}:' --end4println:+
:'\n':+:abc'\n':+:123'\n':+

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None --cased_func_or_args4islice__eithers: --may_fmt4out:':{0!s}{1!r}:' --may_smay_newline4in:$'\r'
    if not smay_newline: raise ValueError(newlines, smay_newline, line) #expect eof
ValueError: (('\r',), '', 'abc\n')
    <<== stdin.newline='\n' instead of '\r'


printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None --cased_func_or_args4islice__eithers: --may_fmt4out:':{0!s}{1!r}:' =2
:'\n'::abc'\n':


printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None --may_fmt4out:':{0!s}{1!r}:' ++cased_func_or_args4islice__eithers='(0,len)'
:'\n':

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None --may_fmt4out:':{0!s}{1!r}:' ++cased_func_or_args4islice__eithers='(1,len)'
:abc'\n'::123'\n':

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None %seed.tiny:chains  %seed.func_tools.dot2:dot  ++cased_func_or_args4islice__eithers='(2,dot["".join, chains])'
<BLANK>
abc
123

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None %seed.tiny:fst  %seed.func_tools.dot2:dot  ++cased_func_or_args4islice__eithers='(2,dot["/".join, [map,fst]])'
/abc/123

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None  ++cased_func_or_args4islice__eithers='(3,lambda st_ln:repr("/".join(st_ln)))'
'/\n''abc/\n''123/\n'

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None  ++cased_func_or_args4islice__eithers='(3,lambda st_ln:repr("/".join(st_ln)))'  --end4println:$'\n'
'/\n'
'abc/\n'
'123/\n'

printf '\nabc\n123\n' | py_adhoc_call   seed.recognize.cmdline.txt_process   @main :line_filter   --encoding:u8  --may_ipath=None  ++cased_func_or_args4islice__eithers='(3,lambda st_ln:repr("/".join(st_ln)))'  --end4println:$'\n'   ++cased_func_or_args4islice__eithers=1,2
'abc/\n'


def line_filter(*args4islice4out, cased_func_or_args4islice__eithers, ifile, ofile, may_smay_newline4in, end4println='', flush4println=True, without_last_line_if_empty=True, may_fmt4out=None):






#]]]'''
__all__ = r'''
main
    line_filter

open_ioFiles_
    mk_may_Path4file_
    mk_may_ioPaths4file_

mk_predicator_on_channel_idc

'''.split()#'''
__all__


#from seed.str_tools.iter_split_ex_by_ import iter_split_ex_by_
from seed.seq_tools.find_all import find_all_, iter_all_
from seed.iters.isplit_if import iter_split_if_starts_, iter_split_if_ends_, iter_split_with_sep_if_, iter_split_without_sep_if_
from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__path__human, iter_line_contents__path
#def iter_line_contents__path(ipath, /, *, encoding, newline=default_may_smay_newline, kwargs4open=None, may_newlines=default_may_newlines, without_last_line_if_empty=False):
#from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__file__human, iter_line_contents__file
from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__path_, iter_line_contents_ex__file_
#def iter_line_contents_ex__file_(ifile, /, *, newlines__or__may_smay_newline, without_last_line_if_empty):
#    -> Iter (line_content, smay_newline)

from seed.tiny import mk_fprint, ifNone
from seed.io.savefile__str_tuple import SaveStrTupleAsMultiLine, std_saver4str_tuple
    #def iter_read_str_tuple_from_ifile_(sf, ifile, /):

#from seed.tiny import fst, snd, at
from seed.tiny_.check import check_callable, check_type_is, check_uint_lt
from seed.io.may_open import open4wt, open4wt_err, open4rt
#def open4wt(may_opath, /, *, force, encoding):
#def open4rt(may_opath, /, *, encoding):
from seed.helper.with_many import with_many
from seed.func_tools.detect_depth4fail import decorator4show_py_help
from itertools import islice, filterfalse
from functools import partial
from pathlib import Path


def main(nm4subcmd_or_subcmd, /, *args, may_ipath, encoding, may_opath=None, oencoding=..., force=False, may_smay_newline4in='', may_smay_newline4out='', **kw):
    #if not encoding: raise TypeError
    #if not oencoding: raise TypeError
    if callable(nm4subcmd_or_subcmd):
        subcmd = nm4subcmd_or_subcmd
    else:
        nm4subcmd = nm4subcmd_or_subcmd
        subcmd = _nm2subcmd[nm4subcmd]
    check_callable(subcmd)
    subcmd = decorator4show_py_help(subcmd)

    if oencoding is ...:
        oencoding = encoding
    iencoding = encoding
    del encoding

    with open_ioFiles_(may_ipath=may_ipath, may_opath=may_opath, iencoding=iencoding, oencoding=oencoding, force=force, may_smay_newline4in=may_smay_newline4in, may_smay_newline4out=may_smay_newline4out) as (ifile, ofile):
        return subcmd(*args, ifile=ifile, ofile=ofile, may_smay_newline4in=may_smay_newline4in, **kw)


def mk_may_Path4file_(may_path, /):
    if not may_path is None:
        path = may_path
        if not path:raise TypeError(repr(path))
        path = Path(path)
        if path.exists() and not path.is_file(): raise IsADirectoryError(path)
        may_path = path
    return may_path
def mk_may_ioPaths4file_(may_ipath, may_opath, force, /):
    '-> (may_ipath, may_opath)'
    check_type_is(bool, force)
    may_ipath = mk_may_Path4file_(may_ipath)
    may_opath = mk_may_Path4file_(may_opath)
    if not (may_ipath is None or may_opath is None):
        ipath = may_ipath
        opath = may_opath
        if not ipath.exists(): raise FileNotFoundError(ipath)
        if opath.exists() and opath.samefile(ipath): raise PermissionError(f'I=O: {ipath!r} === {opath!r}')
    if not (may_opath is None or force):
        assert not force
        opath = may_opath
        if opath.exists() and not force: raise FileExistsError(opath)
    return (may_ipath, may_opath)


def open_ioFiles_(*, may_ipath, may_opath, iencoding, oencoding, force, may_smay_newline4in, may_smay_newline4out):
    '-> with ... as (ifile, ofile):'
    (may_ipath, may_opath) = mk_may_ioPaths4file_(may_ipath, may_opath, force)
    #with open4rt(may_ipath, encoding=iencoding) as ifile, open4wt(may_opath, encoding=oencoding, force=force) as ofile:
    return with_many([lambda:open4rt(may_ipath, encoding=iencoding, may_smay_newline=may_smay_newline4in)], [lambda:open4wt(may_opath, encoding=oencoding, force=force, may_smay_newline=may_smay_newline4out)])


def mk_predicator_on_channel_idc(predicator, channel_idc, /):
    channel_idc[:0]
    def predicator_on_channel_idc(row, /):
        args = (row[i] for i in channel_idc)
        return predicator(*args)
    return predicator_on_channel_idc

def line_filter(*args4islice4out, cased_func_or_args4islice__eithers, ifile, ofile, may_smay_newline4in, end4println='', flush4println=True, without_last_line_if_empty=True, may_fmt4out=None):
    r'''

    initially:
        ipath -> Iter (line_content, smay_newline)
        # pair ==>> channel_idx can be 0,1
    assume curr_rows :: Iter row
        row :: tuple(data)
    assume finally be (Iter (str|tuple))

    cased_func_or_args4islice__eithers :: [((case,func,*channel_idc)|(*args4islice,))]

    if not channel_idc:
        channel_idc = [0]
    if len(channel_idc)==1:
        ...
    args = (row[i] for i in channel_idc)

    * [case==0]:
        [func==not.predicator]
        [predicator(*args)]
    * [case==1]:
        [func==predicator]
        [predicator(*args)]
    * [case==2]:
        [func==rows_processor]
        [rows_processor(rows)]
    * [case==3]:
        [func==row_processor]
        [row_processor(row)]
    '''#'''

    #fprint = mk_fprint(ofile)
    fprint = partial(print, file=ofile, end=end4println, flush=flush4println)
    if not may_fmt4out is None:
        fmt4out = may_fmt4out
        check_type_is(str, fmt4out)

    #it = iter(ifile)
    it = iter_line_contents_ex__file_(ifile, newlines__or__may_smay_newline=may_smay_newline4in, without_last_line_if_empty=without_last_line_if_empty)
    for ls in cased_func_or_args4islice__eithers:
        if len(ls) == 2 and callable(ls[1]):
            case, func, *channel_idc = ls

            check_uint_lt(4, case)
            if case == 3:
                row_processor = func
                [] = channel_idc
                it = map(row_processor, it)
                    #e.g. output formattor
            elif case == 2:
                [] = channel_idc
                rows_processor = func
                it = rows_processor(it)
                    #e.g. merge multilines
            elif 0 <= case < 2:
                predicator = func
                if not channel_idc:
                    channel_idc = b'\0'
                filterX = filter if case else filterfalse
                predicator_on_channel_idc = mk_predicator_on_channel_idc(predicator, channel_idc)
                it = filterX(predicator_on_channel_idc, it)
            else:
                raise 000
        else:
            args4islice = ls
            if args4islice:
                it = islice(it, *args4islice)
    it

    ###output
    if args4islice4out:
        it = islice(it, *args4islice4out)

    for str_or_row in it:
        if not type(str_or_row) in (str, tuple): raise TypeError
        if type(str_or_row) is str:
            s = str_or_row
            row = (s,)
        else:
            row = str_or_row
        row

        if not may_fmt4out is None:
            fmt4out
            s = fmt4out.format(*row)
            row = (s,)
        row

        for s in row:
            fprint(s)

#for t in std_saver4str_tuple.iter_read_str_tuple_from_ifile_(ifile):


_nms4subcmd = r'''
line_filter
'''.split()#'''
def __(_nms4subcmd, /):
    gd = globals()
    _nm2subcmd = {nm:gd[nm] for nm in _nms4subcmd}
    return _nm2subcmd
_nm2subcmd = __(_nms4subcmd)



from seed.recognize.cmdline.txt_process import main, line_filter
from seed.recognize.cmdline.txt_process import open_ioFiles_, mk_may_Path4file_, mk_may_ioPaths4file_

from seed.recognize.cmdline.txt_process import *
