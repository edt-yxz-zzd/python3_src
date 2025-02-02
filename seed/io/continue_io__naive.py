#__all__:goto
r'''[[[
e ../../python3_src/seed/io/continue_io__naive.py
used in:
    view script/搜索冫伪素数牜临近幂方.py

seed.io.continue_io__naive
py -m nn_ns.app.debug_cmd   seed.io.continue_io__naive -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.continue_io__naive:__doc__ -ht # -ff -df

[[
]]

>>> from seed.for_libs.for_tempfile import Path, mk_temp_dir_ctx_
>>> with mk_temp_dir_ctx_() as tmp_dir:
...     tmp_dir = Path(tmp_dir)
...     #LineContinueIO__offset_args0(offset4lineno, path, encoding, qnm4worker, args4worker, kwds4worker)
...     fpath = tmp_dir/'tmp_out'
...     #######startup
...     sz = 3
...     with LineContinueIO__offset_args0(0, fpath, encoding:='u8', f'{__name__}._0worker_', [999,666], {}) as x:#startup
...         x.run_(extra_kwds4worker=dict(sz=sz))
...     ##
...     with open(fpath, 'rt', encoding='u8') as ifile:
...         print(ifile.read(), end='=#=#=\n')
...     #######resume
...     sz = 2
...     with LineContinueIO__offset_args0(0, fpath, encoding:='u8', f'{__name__}._0worker_', [999,666], {}) as x:#resume
...         x.run_(extra_kwds4worker=dict(sz=sz))
...     ##
...     with open(fpath, 'rt', encoding='u8') as ifile:
...         print(ifile.read(), end='=#=#=\n')
...     #######
('seed.io.continue_io__naive._0worker_', [999, 666], {})
(0, 999, 666)
(1, 999, 666)
(2, 999, 666)
=#=#=
('seed.io.continue_io__naive._0worker_', [999, 666], {})
(0, 999, 666)
(1, 999, 666)
(2, 999, 666)
(3, 999, 666)
(4, 999, 666)
=#=#=
>>> with open(fpath, 'rt', encoding='u8') as ifile: pass  #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
FileNotFoundError: ...




py_adhoc_call   seed.io.continue_io__naive   @f
]]]'''#'''
__all__ = r'''
ILineContinueIO
    ILineContinueIO__mixins__init
        LineContinueIO__offset_args0
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from itertools import count as count_ #islice
from pathlib import Path
from functools import cached_property
from io import SEEK_END

from seed.for_libs.for_time import timer__print_err__thread_wide as timer
#   with postpone, timer(prefix=f'{n}', _to_show_=_to_show_, _show_hint_on_enter_=True):
from seed.for_libs.for_time import PeriodicToilLeisureTime, mkr4try_resting_
#def mkr4try_resting_(*, may_prompt_string6resting, may_args4PeriodicToilLeisureTime:[None,(float,float)]):
#    '-> try_resting_/(()->None) # [may sleep_if_work_too_long_enough_]'



from seed.pkg_tools.import_object import import_object, import4qobject
from seed.tiny_.check import check_callable, check_type_is, check_int_ge, check_non_ABC
from seed.tiny import print_err

from seed.helper.stable_repr import stable_repr
from seed.helper.safe_eval import safe_eval
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#from seed.helper.repr_input import repr_helper
from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...


def _mk_postpone_(to_postpone_KeyboardInterrupt_until_yield=False, prompt_string4postpone_KeyboardInterrupt_until_yield=None):
    from seed.for_libs.for_signal import PostponeKeyboardInterrupt
        # ++kw:to_postpone_KeyboardInterrupt_until_yield => flush4print
    check_type_is(bool, to_postpone_KeyboardInterrupt_until_yield)
    if None is prompt_string4postpone_KeyboardInterrupt_until_yield:
        prompt_string4postpone_KeyboardInterrupt_until_yield = '\n\n... postpone_KeyboardInterrupt_until_yield ...\n\n'
    else:
        to_postpone_KeyboardInterrupt_until_yield = True
    check_type_is(str, prompt_string4postpone_KeyboardInterrupt_until_yield)
    # ++kw:prompt_string4postpone_KeyboardInterrupt_until_yield => to_postpone_KeyboardInterrupt_until_yield
    ######################
    postpone = PostponeKeyboardInterrupt(whether_turnoff:=not to_postpone_KeyboardInterrupt_until_yield, may_prompt_string=prompt_string4postpone_KeyboardInterrupt_until_yield)
    return postpone
    #######

class ILineContinueIO(ABC):
    '[worker :: ((*updated_args4worker, **updated_kwds4worker, **extra_kwds4worker) -> Iterator record)]'
    __slots__ = ()
    #@property
    #@abstractmethod
    #def to_postpone_KeyboardInterrupt_until_yield(sf, /):
    #    '-> bool'
    #@property
    #@abstractmethod
    #def may_prompt_string4postpone_KeyboardInterrupt_until_yield(sf, /):
    #    '-> may str'
    @property
    @abstractmethod
    def _path4io_(sf, /):
        '-> Path'
    @property
    @abstractmethod
    def _encoding4io_(sf, /):
        '-> encoding/str'
    @property
    @abstractmethod
    def _header_(sf, /):
        '-> header/(qnm4worker/str, args4worker, kwds4worker)'
    #.@property
    #.@abstractmethod
    #.def _extra_kwds4worker_(sf, /):
    #.    '-> extra_kwds4worker'
    @abstractmethod
    def _update_settings_(sf, last_lineno, tmay_last_record, args4worker, kwds4worker, /):
        'last_lineno -> tmay_last_record -> args4worker -> kwds4worker -> updated_settings/(updated_args4worker, updated_kwds4worker)'
    def _eval4header_(sf, s, /):
        'str -> header/(qnm4worker/str, args4worker, kwds4worker)'
        return safe_eval(s)
    def _eval4record_(sf, s, /):
        'str -> record'
        return safe_eval(s)
    def __enter__(sf, /):
        file4io = sf._file4io_
        type(file4io).__enter__(file4io)
        return sf
    def __exit__(sf, /, *args4worker):
        file4io = sf._file4io_
        type(file4io).__exit__(file4io, *args4worker)
        file4io.close()
        return
    def run_(sf, /, *, also_to_stderr=False, to_postpone_KeyboardInterrupt_until_yield=False, prompt_string4postpone_KeyboardInterrupt_until_yield=None, extra_kwds4worker=None, may_prompt_string6resting=None, may_args4PeriodicToilLeisureTime:[None,(float,float)]=None, to_show_timedelta=False):
        d = dict(locals())
        del d['sf']
        for _ in sf.iter_run_(**d):pass
        return
    def iter_run_(sf, /, *, also_to_stderr=False, to_postpone_KeyboardInterrupt_until_yield=False, prompt_string4postpone_KeyboardInterrupt_until_yield=None, extra_kwds4worker=None, may_prompt_string6resting=None, may_args4PeriodicToilLeisureTime:[None,(float,float)]=None, to_show_timedelta=False):
        ######################
        try_resting_ = mkr4try_resting_(may_prompt_string6resting=may_prompt_string6resting, may_args4PeriodicToilLeisureTime=may_args4PeriodicToilLeisureTime)
        check_type_is(bool, to_show_timedelta)
        ######################
        #extra_kwds4worker = sf._extra_kwds4worker_
        if extra_kwds4worker is None:
            extra_kwds4worker = {}
        postpone = _mk_postpone_(to_postpone_KeyboardInterrupt_until_yield, prompt_string4postpone_KeyboardInterrupt_until_yield)
        with sf:
            #######
            header = sf._header_
            worker = sf._worker_
            (updated_args4worker, updated_kwds4worker) = sf._updated_settings_
            extra_kwds4worker
            #######
            file4io_ex = sf._file4io_ex_
            (file4io, last_lineno, tmay_last_record, addr4continue) = file4io_ex
            #######
            if not addr4continue == file4io.tell():raise 000
            file4io.seek(0, SEEK_END)
            if not addr4continue == file4io.tell():raise 000
            #######
            records = worker(*updated_args4worker, **updated_kwds4worker, **extra_kwds4worker)
            if not iter(records) is records: raise TypeError(type(records))
            records = iter(records)
            #for lineno, record in enumerate(records, last_lineno+1):
            Nothing = object()
            lineno = last_lineno
            while 1:
                lineno += 1
                try_resting_()
                with postpone, timer(prefix=f'{lineno}', _to_show_=to_show_timedelta, _show_hint_on_enter_=True):
                    record = next(records, Nothing)
                    if record is Nothing:break
                    if also_to_stderr:print_err(lineno, record, sep=':')
                    s = stable_repr(record)
                    sf._print_(file4io, s)
                    yield record
                    postpone.exit_then_enter()
                        # ^KeyboardInterrupt@__exit__ if any && not whether_turnoff
                #end-with postpone:
        #######
        #end-with sf:
        return


    @cached_property
    def _file4io_(sf, /):
        '-> file4io'
        file4io_ex = sf._file4io_ex_
        (file4io, last_lineno, tmay_last_record, addr4continue) = file4io_ex
        return file4io
    @cached_property
    def _file4io_ex_(sf, /):
        '-> file4io_ex/(file4io, last_lineno, tmay_last_record, addr4continue)'
        header = sf._header_
        ok = False
        #file4io = open(sf._path4io_, 'r+', encoding=sf._encoding4io_)
            #^FileNotFoundError@startup
        file4io = open(sf._path4io_, 'a+', encoding=sf._encoding4io_)
        try:
            777; addr8end = file4io.tell()
            777; file4io.seek(0)
                # since 'a+'
            lineno = -1
            for lineno, line in enumerate(file4io, lineno+1):
                assert lineno == 0
                # old_file
                _header = sf._eval4header_(line)
                if not _header == header:raise TypeError(header, _header, sf._path4io_)
                break
            else:
                # new_file
                assert lineno == -1
                assert 0 == addr8end == file4io.tell()
                s = stable_repr(header)
                sf._print_(file4io, s)
                lineno += 1
            assert lineno == 0
            #assert not 0 == file4io.tell()
                #OSError: telling position disabled by next() call
            for lineno, line in enumerate(file4io, lineno+1):
                record = sf._eval4record_(line)
                sf._on_reading_record_(lineno, record)
            last_lineno = lineno
            if last_lineno == 0:
                tmay_last_record = ()
            else:
                tmay_last_record = (record,)
            addr4continue = file4io.tell()
            file4io_ex = (file4io, last_lineno, tmay_last_record, addr4continue)
            ...
            ok = True
            return file4io_ex
        finally:
            if not ok:file4io.close()
        raise 000
    def _on_reading_record_(sf, lineno, record, /):
        '-> None'
    def _print_(sf, file4io, s, /):
        #[sf._file4io_ is not set yet]
        check_type_is(str, s)
        if '\n' in s:raise TypeError(s)
        print(s, file=file4io, flush=True)
    @cached_property
    def _qnm4worker_(sf, /):
        '-> qnm4worker/str'
        header = sf._header_
        (qnm4worker, args4worker, kwds4worker) = header
        return qnm4worker
    @cached_property
    def _worker_(sf, /):
        '-> worker/((*updated_args4worker, **updated_kwds4worker, **extra_kwds4worker) -> Iterator record)'
        qnm4worker = sf._qnm4worker_
        smay_qnm4mdl, _, nm4worker = qnm4worker.rpartition('.')
        worker = import4qobject(smay_qnm4mdl, nm4worker)
        return worker
    @cached_property
    def _settings_(sf, /):
        '-> settings/(args4worker, kwds4worker)'
        header = sf._header_
        (qnm4worker, args4worker, kwds4worker) = header
        settings = (args4worker, kwds4worker)
        return settings
    @cached_property
    def _updated_settings_(sf, /):
        '-> updated_settings/(updated_args4worker, updated_kwds4worker)'
        settings = sf._settings_
        (args4worker, kwds4worker) = settings
        file4io_ex = sf._file4io_ex_
        (file4io, last_lineno, tmay_last_record, addr4continue) = file4io_ex
        (updated_args4worker, updated_kwds4worker) = sf._update_settings_(last_lineno, tmay_last_record, args4worker, kwds4worker)
        updated_settings = (updated_args4worker, updated_kwds4worker)
        return updated_settings
class ILineContinueIO__mixins__init(ILineContinueIO, _Base4repr):
    '[worker :: ((*updated_args4worker, **updated_kwds4worker, **extra_kwds4worker) -> Iterator record)]'
    ___no_slots_ok___ = True
    if 0:
        @abstractmethod
        def _update_settings_(sf, last_lineno, tmay_last_record, args4worker, kwds4worker, /):
            'last_lineno -> tmay_last_record -> args4worker -> kwds4worker -> updated_settings/(updated_args4worker, updated_kwds4worker)'
    def __init__(sf, /, path, encoding, qnm4worker, args4worker, kwds4worker):
        check_type_is(str, encoding)
        Path(path)
        sf.__args = (path, encoding, qnm4worker, args4worker, kwds4worker)
        #sf._init4repr(path, encoding, qnm4worker, args4worker, kwds4worker)
        sf._reset4repr(sf.__args, None)
        check_callable(sf._worker_)
    #.def __repr__(sf, /):
    #.    return repr_helper(sf, *args4worker, **kwds4worker)
    @property
    @override
    def _path4io_(sf, /):
        '-> Path'
        return sf.__args[0]
    @property
    @override
    def _encoding4io_(sf, /):
        '-> encoding/str'
        return sf.__args[1]
    @property
    @override
    def _header_(sf, /):
        '-> header/(qnm4worker/str, args4worker, kwds4worker)'
        return sf.__args[2:]

class LineContinueIO__offset_args0(ILineContinueIO__mixins__init):
    '[updated_args4worker := (begin:=last_lineno+sf.offset4lineno, *args4worker)][updated_kwds4worker := kwds4worker]' \
        '# [worker :: ((*updated_args4worker, **updated_kwds4worker, **extra_kwds4worker) -> Iterator record)]'
    #LineContinueIO__offset_args0(offset4lineno, path, encoding, qnm4worker, args4worker, kwds4worker)
    def __init__(sf, /, offset4lineno, path, encoding, qnm4worker, args4worker, kwds4worker):
        check_type_is(int, offset4lineno)
        super().__init__(path, encoding, qnm4worker, args4worker, kwds4worker)
        sf._offset = offset4lineno
        sf._init4repr(offset4lineno, path, encoding, qnm4worker, args4worker, kwds4worker)

    @property
    def offset4lineno(sf, /):
        '-> offset4lineno/int'
        return sf._offset
    @override
    def _update_settings_(sf, last_lineno, tmay_last_record, args4worker, kwds4worker, /):
        'last_lineno -> tmay_last_record -> args4worker -> kwds4worker -> updated_settings/(updated_args4worker, updated_kwds4worker)'
        updated_args4worker = (begin:=last_lineno+sf.offset4lineno, *args4worker)
        begin
        updated_kwds4worker = kwds4worker
        updated_settings = (updated_args4worker, updated_kwds4worker)
        return updated_settings
check_non_ABC(LineContinueIO__offset_args0)



def _0worker_(begin=0, /, *_args, sz):
    '# [worker :: ((*updated_args4worker, **updated_kwds4worker, **extra_kwds4worker) -> Iterator record)]'
    #for i in count_(begin):
    for i in range(begin, begin+sz):
        yield (i, *_args)
        #sleep(1.0)






__all__
from seed.io.continue_io__naive import ILineContinueIO, ILineContinueIO__mixins__init, LineContinueIO__offset_args0
    #LineContinueIO__offset_args0(offset4lineno, path, encoding, qnm4worker, args4worker, kwds4worker)
from seed.io.continue_io__naive import *
