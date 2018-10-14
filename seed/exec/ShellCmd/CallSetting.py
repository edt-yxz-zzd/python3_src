


__all__ = '''
    CallSetting
    '''.split()

from .IShellCmd import IShellCmd
from .common import (
    IReprImmutableHelper
    , MappingProxyType

    , ArgsType
    , OptionsType
    , PayloadType

    , SubprocessRun_KwargsValueType
    , SubprocessRun_KwargsType
    , SubprocessRun_DictKwargsType
    )



#from subprocess import run, CalledProcessError, CompletedProcess, PIPE, STDOUT, DEVNULL
#   subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, encoding=None, errors=None)
import subprocess # run
from subprocess import CompletedProcess
from typing import Tuple, List

class CallSetting(IReprImmutableHelper):
    '''

======================================
see:
    subprocess module
usage:
    * to ignore output
        * echo to user:
            CallSetting(stdout=None, stderr=None, ...).call_shell_cmd(...)
        * shut up/be quiet:
            CallSetting(stdout=DEVNULL, stderr=DEVNULL, ...).call_shell_cmd(...)
    to capture output and be quiet:
        CallSetting(stdout=PIPE, stderr=(PIPE|STDOUT), ...).call_shell_cmd(...)

result:
    #CompletedProcess
    result.args/returncode/stdout/stderr

    #if check=True & error
    #CalledProcessError
    exception.cmd/returncode/stdout/stderr
        where returncode != 0

    ###### .stdout/.stderr :: None | bytes | str
    ######      <<== PIPE, "encoding", ...
======================================

'''
    @property
    def subprocess_run_kwargs(self) -> SubprocessRun_KwargsType:
        return self.__subprocess_run_kwargs
    def ___get_args_kwargs___(self
        ) -> Tuple[List[None], SubprocessRun_DictKwargsType]:
        return ([], dict(self.__subprocess_run_kwargs))
    def __init__(self
        , **__subprocess_run_kwargs:SubprocessRun_KwargsValueType
        ) -> None:
        # keyword arguments of subprocess.run
        self.__subprocess_run_kwargs=MappingProxyType(__subprocess_run_kwargs)

    def ireplace(self, **__subprocess_run_kwargs:SubprocessRun_KwargsValueType):
        #bug: return type(self)(**self.__subprocess_run_kwargs, **__subprocess_run_kwargs)
        return type(self)(**{**self.__subprocess_run_kwargs, **__subprocess_run_kwargs})

    def call_shell_cmd(self, __shell_cmd:IShellCmd) -> CompletedProcess:
        # -> CompletedProcess | raise CalledProcessError
        assert isinstance(__shell_cmd, IShellCmd)
        cmd = __shell_cmd.to_run_args()
        return subprocess.run(cmd, **self.__subprocess_run_kwargs)
    def call_shell_cmd_ex(self
        , __shell_cmd:IShellCmd # not IShellCmdType
        , __args:ArgsType
        , __old_options:OptionsType
        , **_new_kwargs:PayloadType
        ) -> CompletedProcess:
        # -> CompletedProcess | raise CalledProcessError
        assert type(__shell_cmd) is not str
            # since I donot known how to covert _new_kwargs to options
        assert isinstance(__shell_cmd, IShellCmd)

        overwrite = False
            # "overwrite" is not used
            #   since the cmd is discard as sooner as possible
        __shell_cmd = __shell_cmd.iextend(overwrite
                , __args, __old_options , **_new_kwargs)
        return self.call_shell_cmd(__shell_cmd)



