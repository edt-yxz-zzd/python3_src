
__all__ = '''
    CallTheShellCmd
    '''.split()


from .CallSetting import CallSetting
from .IShellCmd import IShellCmd
from .common import (
    IReprImmutableHelper
    ,SubprocessRun_KwargsValueType
    ,ArgsType
    ,OptionsType
    ,PayloadType
    )

from subprocess import CompletedProcess
from typing import Tuple, Dict, Optional


class CallTheShellCmd(IReprImmutableHelper):
    def ___get_args_kwargs___(self
        ) -> Tuple[Tuple[CallSetting, IShellCmd], Dict[None,None]]:
        return ((self.__shell_cmd, self.__caller), {})

    def __init__(self, __shell_cmd:IShellCmd, __caller:CallSetting)->None:
        assert isinstance(__shell_cmd, IShellCmd)
        assert isinstance(__caller, CallSetting)
        self.__shell_cmd = __shell_cmd
        self.__caller = __caller

    def ireplace(self
        , __may_shell_cmd:Optional[IShellCmd] = None
        , __may_caller:Optional[CallSetting] = None
        , **__subprocess_run_kwargs:SubprocessRun_KwargsValueType):

        __shell_cmd = (self.__shell_cmd if __may_shell_cmd is None
                    else __may_shell_cmd)

        __caller = (self.__caller if __may_caller is None
                    else __may_caller)
        __caller = __caller.ireplace(**__subprocess_run_kwargs)

        return type(self)(__shell_cmd, __caller)


    def call_the_shell_cmd(self) -> CompletedProcess:
        return self.__caller.call_shell_cmd(self.__shell_cmd)
    def call_the_shell_cmd_ex(self
        , __args:ArgsType
        , __old_options:OptionsType
        , **_new_kwargs:PayloadType
        ) -> CompletedProcess:
        return self.__caller.call_shell_cmd_ex(
            self.__shell_cmd, __args, __old_options, **_new_kwargs)

    def __call__(self
        , __args:ArgsType = ()
        , __old_options:OptionsType = {}
        , **_new_kwargs:PayloadType
        ) -> CompletedProcess:
        return self.call_the_shell_cmd_ex(
            __args, __old_options, **_new_kwargs)


