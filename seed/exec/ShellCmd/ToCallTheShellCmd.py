
__all__ = '''
    ToCallTheShellCmd
    '''.split()


from .CallSetting import CallSetting
from .IShellCmd import IShellCmd
from .CallTheShellCmd import CallTheShellCmd
from .common import IReprImmutableHelper

from typing import Tuple, Dict, Type

class ToCallTheShellCmd(IReprImmutableHelper):
    def ___get_args_kwargs___(self
        ) -> Tuple[Tuple[CallSetting, IShellCmd], Dict[None,None]]:
        return (_get_args(self), {})

    def __init__(self
        , __shell_cmd_cls:Type[IShellCmd]
        , __caller:CallSetting
        )->None:
        #from pprint import pprint; pprint(dir(self)); raise Exception
        assert issubclass(__shell_cmd_cls, IShellCmd)
        assert isinstance(__caller, CallSetting)
        self.__shell_cmd_cls = __shell_cmd_cls
        self.__caller = __caller
    def __getattribute__(self, __attr:str) -> CallTheShellCmd:
        __shell_cmd_cls, __caller = _get_args(self)

        __shell_cmd = __shell_cmd_cls.from_IShellCmd_init_args(
            False, __attr, (), {})
        return CallTheShellCmd(__shell_cmd, __caller)

#ToCallTheShellCmd(int,1)

def _get_args(__to_cmd:ToCallTheShellCmd
    ) -> Tuple[CallSetting, IShellCmd]:
    #
    __shell_cmd_cls = object.__getattribute__(__to_cmd
        , '_ToCallTheShellCmd__shell_cmd_cls')
    #
    __caller = object.__getattribute__(__to_cmd
        , '_ToCallTheShellCmd__caller')
    #
    return __shell_cmd_cls, __caller


