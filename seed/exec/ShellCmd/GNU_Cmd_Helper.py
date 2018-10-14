


__all__ = '''
    GNU_Cmd_Helper
    '''.split()


from .IShellCmdHelper import IShellCmdHelper
from .common import (
    FlagType
    , KeywordType
    )

class GNU_Cmd_Helper(IShellCmdHelper):
    def __keyword2flag__(self, __kw:KeywordType) -> FlagType:
        cls = type(self)
        return super(__class__, cls).__keyword2flag__(self, __kw)
    def is_flag(self, __flag:FlagType) -> bool:
        return super().is_flag(__flag)


