
__all__ = '''
    GNU_Cmd
    '''.split()


from .IShellCmd import IShellCmd
from .GNU_Cmd_Helper import GNU_Cmd_Helper
from .common import (
    ArgType
    , FlagType
    )
from typing import Iterator

class GNU_Cmd(IShellCmd):
    @classmethod
    def make_IShellCmdHelper(cls, *, overwrite:bool) -> GNU_Cmd_Helper:
        return GNU_Cmd_Helper(overwrite=overwrite)
    def iter_seperators_of_options_and_args(self) -> Iterator[ArgType]:
        return super().iter_seperators_of_options_and_args()
    def iter_option_args(self, flag:FlagType, payload:ArgType) -> Iterator[ArgType]:
        return super().iter_option_args(flag, payload)
    def to_iter_run_args(self) -> Iterator[ArgType]:
        return super().to_iter_run_args()
GNU_Cmd(True, 'ls', ['.'], {'-A':True}, _1=True)


