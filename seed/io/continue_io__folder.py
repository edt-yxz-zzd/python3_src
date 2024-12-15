#__all__:goto
r'''[[[
e ../../python3_src/seed/io/continue_io__folder.py

seed.io.continue_io__folder
py -m nn_ns.app.debug_cmd   seed.io.continue_io__folder -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.continue_io__folder:__doc__ -ht # -ff -df


++kw:to_postpone_KeyboardInterrupt_until_subtask_switchover
++kw:may_prompt_string4postpone_KeyboardInterrupt_until_subtask_switchover


[[
append_eof --> continue_io__folder
===
view ../../python3_src/nn_ns/app/append_eof.py
view ../../python3_src/seed/io/continue_io.py
view ../../python3_src/seed/io/continue_io__folder.py
===
源起:
py_adhoc_call   script.搜索冫某进制表达数乊多种进制解 读皆为素数   ,str.搜索冫某进制表达数乊多种进制解读皆为素数扌 ="[17,19,23,29,31]" =16     ="0x00*16**6"  ="0x01*16**6" --imay_radix4beyond=-1 +int_vs_str +str_with_int +to_swap_fmt4str_with_int | lineno  | append_eof  >  /sdcard/0my_files/tmp/out多种进制解读皆为素数/16_56_00tmp
一共分割为256行命令(5分钟以内/命令)
append_eof 用于确认命令正常结束
===
append_eof --> continue_io__folder
===
job shop scheduling
车间作业进度表
job step
工作步骤
作业步
作业步骤
作业段
加工步骤
job step task
作业步任务
serializer-deserializer
串行器-解串器
===
odir
job_mkr(*args4job, **kwds4job)
iter_tasks5job_ :: job -> Iter task
id5job_task_ :: job -> task -> id4task
    id4task:repr,eval
    id4task <-> subpath4task
subpath5job_ :: job -> subpath4job
subpath4logbook5job_ :: job -> subpath4logbook
tmp_subpath5job_task_ :: job -> task -> tmp_subpath4task
subpath5job_task_ :: job -> task -> subpath4task
exec_job_task_ :: job -> task -> result4task
open_tmp_ofile4task_ :: job -> task -> tmp_opath4task -> tmp_ofile4task
serializer5job_task_ :: job -> task -> serializer4result4task/(tmp_ofile4task -> result4task -> None)


[odir4job =[def]= odir/subpath4job]
[opath4logbook =[def]= odir4job/subpath4logbook]
    :: [id4task]
[opath4task =[def]= odir4job/subpath4task]
    opath5task_
[tmp_opath4task =[def]= odir4job/tmp_subpath4task]
    tmp_opath5task_
    tmp_opath4task will be rename to opath4task iff task completed
==>>:
py_adhoc_call   script.搜索冫某进制表达数乊多种进制解读皆为素数   @_八位十六进制数囗后续五种素进制解读皆为素数囗断点重启冫拆分成两百五十六个串行子任务 +to_postpone_KeyboardInterrupt_until_subtask_switchover --may_prompt_string4postpone_KeyboardInterrupt_until_subtask_switchover:$'\n\n... postpone_KeyboardInterrupt_until_subtask_switchover ...\n\n'
===
]]


py_adhoc_call   seed.io.continue_io__folder   @f

]]]'''#'''
__all__ = r'''
IFolderBasedContinueJob
    IFolderBasedContinueJob__using_py_repr_eval
    IFolderBasedContinueJob__mk_task5idx
    IFolderBasedContinueJob__using_standalone_task
        IFolderBasedContinueJob__mk_result5idx4task
IStandaloneTask4IFolderBasedContinueJob
    serializer4result4task__repr
    serializer4result4task__repr_iter
    open_tmp_ofile4task__xencoding_

    IStandaloneTask4IFolderBasedContinueJob__using_xencoding4ofile4task
        StandaloneTask4IFolderBasedContinueJob__params
            StandaloneTask4IFolderBasedContinueJob__mk_task5idx

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.for_libs.for_signal import PostponeKeyboardInterrupt
    # ++kw:to_postpone_KeyboardInterrupt_until_subtask_switchover

from pathlib import Path
from seed.io.may_open import open4w, open4w_err, open4r
#def open4w(may_opath, /, *, force, xencoding, **kwargs):
from seed.io.make_mode_ex4open import xencoding2may_encoding

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny_.check import check_type_is, check_pair, check_callable, check_non_ABC, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

class IFolderBasedContinueJob(ABC):
    'job'
    __slots__ = ()
    @classmethod
    @abstractmethod
    def job_mkr(cls, /, *args4job, **kwds4job):
        '-> sf/job'

    @abstractmethod
    def eval_record4log_file_(sf, repr4record, /):
        'repr4record/str -> record/(id4task, subpath4task)'

    @abstractmethod
    def repr_record4log_file_(sf, record, /):
        'record/(id4task, subpath4task) -> repr4record/str'

    @abstractmethod
    def iter_tasks5job_(sf, /):
        '-> Iter task'

    #.@abstractmethod
    #.def subpath5job_(sf, /):
    #.    '-> subpath4job'

    #.@abstractmethod
    #.def subpath4logbook5job_(sf, /):
    #.    '-> subpath4logbook'

    @property
    @abstractmethod
    def subpath4job(sf, /):
        '-> subpath4job'

    @property
    @abstractmethod
    def subpath4logbook(sf, /):
        '-> subpath4logbook'

    @property
    @abstractmethod
    def to_postpone_KeyboardInterrupt_until_subtask_switchover(sf, /):
        '-> bool'

    @property
    @abstractmethod
    def may_prompt_string4postpone_KeyboardInterrupt_until_subtask_switchover(sf, /):
        '-> may prompt_string/str #see:to_postpone_KeyboardInterrupt_until_subtask_switchover'

    @abstractmethod
    def tmp_subpath5job_task_(sf, task, /):
        'task -> tmp_subpath4task'

    @abstractmethod
    def subpath5job_task_(sf, task, /):
        'task -> subpath4task'

    @abstractmethod
    def id5job_task_(sf, task, /):
        'task -> id4task'

    @abstractmethod
    def exec_job_task_(sf, task, /):
        'task -> result4task'

    @abstractmethod
    def open_tmp_ofile4task_(sf, task, tmp_opath4task, /, *, force:bool):
        'task -> tmp_opath4task -> tmp_ofile4task'

    @abstractmethod
    def serializer5job_task_(sf, task, /):
        'task -> serializer4result4task/(tmp_ofile4task -> result4task -> None)'


    @classmethod
    def run_or_resume_(cls, odir, args4job, kwds4job, /, *, force4ofile:bool, force4tmp_ofile:bool, verbose:bool):
        check_type_is(bool, force4ofile)
        check_type_is(bool, force4tmp_ofile)
        check_type_is(bool, verbose)
        job = sf = cls.job_mkr(*args4job, **kwds4job)
        job._run_or_resume_(verbose, force4ofile, force4tmp_ofile, odir)

    def _run_or_resume_(sf, verbose, force4ofile, force4tmp_ofile, odir, /):
        ######################
        if verbose:
            from seed.tiny import print_err
        ######################
        job = sf
        odir = Path(odir)
        #.subpath4job = sf.subpath5job_()
        #.subpath4logbook = sf.subpath4logbook5job_()
        subpath4job = sf.subpath4job
        subpath4logbook = sf.subpath4logbook
        [odir4job := odir/subpath4job]
        [opath4logbook := odir4job/subpath4logbook]
        postpone = PostponeKeyboardInterrupt(whether_turnoff:=not sf.to_postpone_KeyboardInterrupt_until_subtask_switchover, may_prompt_string=sf.may_prompt_string4postpone_KeyboardInterrupt_until_subtask_switchover)
        with open(opath4logbook, 'at+', encoding='utf8') as log_file:
            log_file.seek(0)
            ######################
            id2subpath4task = {}
            id5subpath4task = {}
            for line in log_file:
                repr4record = line.strip()
                assert repr4record
                #assert repr4record[0] == '('
                #assert repr4record[-1] == ')'
                record = sf.eval_record4log_file_(repr4record)
                check_pair(record)
                (id4task, subpath4task) = record
                if id4task in id2subpath4task:raise Exception(id4task, id2subpath4task[id4task], subpath4task)
                if subpath4task in id5subpath4task:raise Exception(subpath4task, id5subpath4task[subpath4task], id4task)
                id2subpath4task[id4task] = subpath4task
                id5subpath4task[subpath4task] = id4task
            assert len(id2subpath4task) == len(id5subpath4task)
            ######################
            ######################
            for task in sf.iter_tasks5job_():
                id4task = sf.id5job_task_(task)
                subpath4task = sf.subpath5job_task_(task)
                tmp_subpath4task = sf.tmp_subpath5job_task_(task)
                [opath4task := odir4job/subpath4task]
                [tmp_opath4task := odir4job/tmp_subpath4task]
                    # tmp_opath4task will be rename to opath4task iff task completed
                record = (id4task, subpath4task)
                ######################
                if id4task in id2subpath4task:
                    if not subpath4task == id2subpath4task[id4task]:raise Exception(id4task, id2subpath4task[id4task], subpath4task)
                    ###########
                    if verbose: print_err('skip done:', record)
                    ###########
                    continue#done
                #
                if subpath4task in id5subpath4task:raise Exception(subpath4task, id5subpath4task[subpath4task], id4task)
                id2subpath4task[id4task] = subpath4task
                id5subpath4task[subpath4task] = id4task
                assert len(id2subpath4task) == len(id5subpath4task)
                ######################
                if verbose: print_err('to do:', record)
                ######################
                repr4record = sf.repr_record4log_file_(record)
                check_type_is(str, repr4record)
                if not sf.eval_record4log_file_(repr4record) == record:raise Exception(record)
                if any(newline in repr4record for newline in '\r\n'):raise Exception(record)
                ######################
                with postpone:
                    _run_or_resume4task(force4ofile, force4tmp_ofile, job, task, opath4task, tmp_opath4task)
                    assert opath4task.is_file()
                    #############
                    print(repr4record, file=log_file, flush=True)
                    #############
                    if verbose: print_err('done:', record)
                    #############
                #end-with postpone:
                    # ^KeyboardInterrupt@__exit__ if any && not whether_turnoff
            #end-for task in sf.iter_tasks5job_():


def _run_or_resume4task(force4ofile, force4tmp_ofile, job, task, opath4task, tmp_opath4task, /):
    ######################
    if not force4ofile:
        if opath4task.exists():raise FileExistsError(opath4task)
    else:
        #force4ofile==True
        if opath4task.exists() and not opath4task.is_file():raise FileExistsError(opath4task)
    ######################

    serializer4result4task = job.serializer5job_task_(task)
    if 1:#with postpone:
        result4task = job.exec_job_task_(task)
        tmp_ofile4task = job.open_tmp_ofile4task_(task, tmp_opath4task, force=force4tmp_ofile)
        try:
            with tmp_ofile4task as tmp_ofile4task:
                serializer4result4task(tmp_ofile4task, result4task)
            ######################
            if opath4task.exists():
                if not force4ofile and opath4task.exists():raise FileExistsError(opath4task)
                if opath4task.exists() and not opath4task.is_file():raise FileExistsError(opath4task)
                opath4task.unlink()
            ######################
            #move/mv
            tmp_opath4task.rename(opath4task)
            #tmp_opath4task.replace(opath4task)
            ######################
        except: #of try:
            #remove/rm
            tmp_opath4task.unlink()
            raise
    #end-with postpone:
        # ^KeyboardInterrupt@__exit__ if any && not whether_turnoff

    return
#end-def _run_or_resume4task(force4ofile, force4tmp_ofile, job, task, opath4task, tmp_opath4task, /):
#end-class IFolderBasedContinueJob(ABC):

class IFolderBasedContinueJob__using_py_repr_eval(IFolderBasedContinueJob):
    __slots__ = ()

    @override
    def eval_record4log_file_(sf, repr4record, /):
        'repr4record/str -> record/(id4task, subpath4task)'
        return eval(repr4record)

    @override
    def repr_record4log_file_(sf, record, /):
        'record/(id4task, subpath4task) -> repr4record/str'
        return repr(record)


class IFolderBasedContinueJob__mk_task5idx(IFolderBasedContinueJob):
    '[id4task == idx4task]'
    __slots__ = ()

    @property
    @abstractmethod
    def num_tasks(sf, /):
        '-> uint'

    @abstractmethod
    def mk_task5idx_(sf, idx4task, /):
        'idx4task/uint%.num_tasks -> task # [id4task == idx4task]'

    @override
    def iter_tasks5job_(sf, /):
        '-> Iter task'
        #for idx4task in range(sf.num_tasks):
        return map(sf.mk_task5idx_, range(sf.num_tasks))




class IFolderBasedContinueJob__using_standalone_task(IFolderBasedContinueJob):
    '[task/standalone_task :: IStandaloneTask4IFolderBasedContinueJob]'
    __slots__ = ()

    @override
    def tmp_subpath5job_task_(sf, task, /):
        'task -> tmp_subpath4task'
        return task.tmp_subpath4task

    @override
    def subpath5job_task_(sf, task, /):
        'task -> subpath4task'
        return task.subpath4task

    @override
    def id5job_task_(sf, task, /):
        'task -> id4task'
        return task.id4task

    @override
    def exec_job_task_(sf, task, /):
        'task -> result4task'
        return task.exec_task_()

    @override
    def open_tmp_ofile4task_(sf, task, tmp_opath4task, /, *, force:bool):
        'task -> tmp_opath4task -> tmp_ofile4task'
        return task.open_tmp_ofile4task_(tmp_opath4task, force=force)

    @override
    def serializer5job_task_(sf, task, /):
        'task -> serializer4result4task/(tmp_ofile4task -> result4task -> None)'
        return task.serializer4result4task

class IFolderBasedContinueJob__mk_result5idx4task(IFolderBasedContinueJob__using_py_repr_eval, IFolderBasedContinueJob__using_standalone_task, IFolderBasedContinueJob__mk_task5idx):
    __slots__ = ()
    # subpath4job, subpath4logbook, to_postpone_KeyboardInterrupt_until_subtask_switchover, may_prompt_string4postpone_KeyboardInterrupt_until_subtask_switchover
    @property
    @abstractmethod
    def fmt4tmp_subpath4task(sf, /):
        '-> str'
    @property
    @abstractmethod
    def fmt4subpath4task(sf, /):
        '-> str'
    @property
    @abstractmethod
    def xencoding4ofile4task(sf, /):
        '-> xencoding'
    @property
    @abstractmethod
    def whether_result4task_is_iterator(sf, /):
        '-> bool/[is_iterator(result4task)]'
    @abstractmethod
    def mk_result5idx4task_(sf, idx4task, /):
        'idx4task -> result4task'
    def idx2lazy_result4task_(sf, idx4task, /):
        'idx4task -> lazy_result4task/(() -> result4task)'
        return lambda:sf.mk_result5idx4task_(idx4task)
    @override
    def mk_task5idx_(sf, idx4task, /):
        'idx4task/uint%.num_tasks -> task # [id4task == idx4task]'
        task = StandaloneTask4IFolderBasedContinueJob__mk_task5idx(sf.fmt4tmp_subpath4task, sf.fmt4subpath4task, sf.xencoding4ofile4task, sf.whether_result4task_is_iterator, sf.idx2lazy_result4task_, idx4task)
        return task
assert (__:=','.join(sorted(IFolderBasedContinueJob__mk_result5idx4task.__abstractmethods__))) == 'fmt4subpath4task,fmt4tmp_subpath4task,job_mkr,may_prompt_string4postpone_KeyboardInterrupt_until_subtask_switchover,mk_result5idx4task_,num_tasks,subpath4job,subpath4logbook,to_postpone_KeyboardInterrupt_until_subtask_switchover,whether_result4task_is_iterator,xencoding4ofile4task', __



class IStandaloneTask4IFolderBasedContinueJob(ABC):
    'standalone_task'
    __slots__ = ()
    @property
    @abstractmethod
    def tmp_subpath4task(sf, /):
        '-> tmp_subpath4task'

    @property
    @abstractmethod
    def subpath4task(sf, /):
        '-> subpath4task'

    @property
    @abstractmethod
    def id4task(sf, /):
        '-> id4task'

    @abstractmethod
    def exec_task_(sf, /):
        '-> result4task'

    @abstractmethod
    def open_tmp_ofile4task_(sf, tmp_opath4task, /, *, force:bool):
        'tmp_opath4task -> tmp_ofile4task'
        open_tmp_ofile4task__xencoding_

    @property
    @abstractmethod
    def serializer4result4task(sf, /):
        '-> serializer4result4task/(tmp_ofile4task -> result4task -> None)'
        serializer4result4task__repr
        serializer4result4task__repr_iter


def serializer4result4task__repr(ofile, reprable, /, *, to_str=repr):
    s = to_str(reprable)
    #print(s, file=ofile)
    ofile.write(s)
def serializer4result4task__repr_iter(ofile, iter_reprable, /, *, to_str=repr):
    for s in map(to_str, iter_reprable):
        print(s, file=ofile)
def open_tmp_ofile4task__xencoding_(xencoding, tmp_opath4task, /, *, force:bool, **kwargs):
    'xencoding -> tmp_opath4task -> tmp_ofile4task # [xencoding = nonencoding | encoding] [nonencoding = '' | None | False] [encoding :: nonempty_str]'
    return open4w(tmp_opath4task, force=force, xencoding=xencoding, **kwargs)
#end-class IStandaloneTask4IFolderBasedContinueJob(ABC):


class IStandaloneTask4IFolderBasedContinueJob__using_xencoding4ofile4task(IStandaloneTask4IFolderBasedContinueJob):
    '# [xencoding = nonencoding | encoding] [nonencoding = '' | None | False] [encoding :: nonempty_str]'
    __slots__ = ()
    @property
    @abstractmethod
    def xencoding4ofile4task(sf, /):
        '-> xencoding # [xencoding = nonencoding | encoding] [nonencoding = '' | None | False] [encoding :: nonempty_str]'

    @override
    def open_tmp_ofile4task_(sf, tmp_opath4task, /, *, force:bool):
        'tmp_opath4task -> tmp_ofile4task'
        tmp_ofile4task = open_tmp_ofile4task__xencoding_(sf.xencoding4ofile4task, tmp_opath4task, force=force)
        return tmp_ofile4task





class StandaloneTask4IFolderBasedContinueJob__params(IStandaloneTask4IFolderBasedContinueJob__using_xencoding4ofile4task):
    ___no_slots_ok___ = True
    def __init__(sf, /, tmp_subpath4task, subpath4task, id4task, xencoding4ofile4task, serializer4result4task, lazy_result4task):
        Path(tmp_subpath4task)
        Path(subpath4task)
        hash(id4task)
        #assert eval(repr(id4task)) == id4task
        xencoding4ofile4task = xencoding2may_encoding(xencoding4ofile4task)
        check_callable(serializer4result4task)
        check_callable(lazy_result4task)

        vars(sf).update((f'_{nm}', v) for nm, v in locals().items() if not nm == 'sf')
        #del vars(sf)['sf']
    @property
    @override
    def tmp_subpath4task(sf, /):
        '-> tmp_subpath4task'
        return sf._tmp_subpath4task

    @property
    @override
    def subpath4task(sf, /):
        '-> subpath4task'
        return sf._subpath4task

    @property
    @override
    def id4task(sf, /):
        '-> id4task'
        return sf._id4task


    @property
    @override
    def xencoding4ofile4task(sf, /):
        return sf._xencoding4ofile4task

    @property
    @override
    def serializer4result4task(sf, /):
        '-> serializer4result4task/(tmp_ofile4task -> result4task -> None)'
        return sf._serializer4result4task
    @override
    def exec_task_(sf, /):
        '-> result4task'
        return sf._lazy_result4task()

check_non_ABC(StandaloneTask4IFolderBasedContinueJob__params)
class StandaloneTask4IFolderBasedContinueJob__mk_task5idx(StandaloneTask4IFolderBasedContinueJob__params):
    ___no_slots_ok___ = True
    def __init__(sf, /, fmt4tmp_subpath4task, fmt4subpath4task, xencoding4ofile4task, whether_result4task_is_iterator, idx2lazy_result4task_, idx4task):
        check_type_is(str, fmt4tmp_subpath4task)
        check_type_is(str, fmt4subpath4task)
        check_type_is(bool, whether_result4task_is_iterator)
        check_int_ge(0, idx4task)

        tmp_subpath4task = fmt4tmp_subpath4task.format(idx4task)
        subpath4task = fmt4subpath4task.format(idx4task)
        id4task = idx4task
        xencoding4ofile4task = xencoding2may_encoding(xencoding4ofile4task)
        serializer4result4task = serializer4result4task__repr_iter if whether_result4task_is_iterator else serializer4result4task__repr
        lazy_result4task = idx2lazy_result4task_(idx4task)
        check_callable(lazy_result4task)
        super().__init__(tmp_subpath4task, subpath4task, id4task, xencoding4ofile4task, serializer4result4task, lazy_result4task)

check_non_ABC(StandaloneTask4IFolderBasedContinueJob__mk_task5idx)

__all__
from seed.io.continue_io__folder import IFolderBasedContinueJob__mk_result5idx4task
from seed.io.continue_io__folder import *
