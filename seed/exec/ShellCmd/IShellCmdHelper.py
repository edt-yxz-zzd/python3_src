


__all__ = '''
    IShellCmdHelper
    keyword2flag__GNU
    '''.split()


from seed.str_tools.contains_space import contains_space
from ._HasAttr_overwrite import _HasAttr_overwrite
from .common import (
    ABC
    , abstractmethod

    , PayloadType

    , FlagType
    , OptionsType
    , DictOptionsType

    , KeywordType
    )
from collections import defaultdict



class IShellCmdHelper(_HasAttr_overwrite, ABC):
    '''

why IShellCmdHelper is not baseclass of IShellCmd?
    * to force always select a "overwrite" value
    * let IShellCmd more simpler
'''
    @abstractmethod
    def __keyword2flag__(self, __kw:KeywordType) -> FlagType:
        return keyword2flag__GNU(__kw)
    @abstractmethod
    def is_flag(self, __flag:FlagType) -> bool:
        return not contains_space(__flag)


    ###############
    def keyword2flag(self, __kw:KeywordType) -> FlagType:
        flag = type(self).__keyword2flag__(self, __kw)
        self.check_flag(flag)
        return flag
    def check_flag(self, __flag:FlagType) -> None:
        if not self.is_flag(__flag):
            raise ValueError(f'invalid flag: {flag!r}')


    ##############################
    '''
    @classmethod
    def from_overwrite(cls, overwrite:bool) -> IShellCmdHelper:
        return cls(overwrite)
    '''

    def detect_duplicated_flags(self, *
        , old_options:OptionsType, new_options:OptionsType
        )->None:
        if not self.overwrite:
            common = set(old_options) & set(new_options)
            if common:
                raise ValueError(f'duplicated flags: {common}')
    def union_options(self, *
        , old_options:OptionsType, new_options:OptionsType
        ) ->DictOptionsType:
        # -> dict
        self.detect_duplicated_flags(old_options=old_options, new_options=new_options)

        L = len(old_options) + len(new_options)
        options = {**old_options, **new_options} # new overwrite old

        if __debug__:
            if self.overwrite:
                assert len(options) <= L
            else:
                assert len(options) == L

        assert type(options) is dict
        return options


    def make_options(self
        , __old_options:OptionsType
        , **_new_kwargs:PayloadType
        ) -> DictOptionsType:
        for _ in map(self.check_flag, __old_options):pass

        #new_options = {self.keyword2flag(kw):payload
        #                for kw, payload in _new_kwargs.items()}
        new_options = {self.keyword2flag(kw):payload
                        for kw, payload in _new_kwargs.items()}
        if len(new_options) != len(_new_kwargs):
            flag2kws = defaultdict(set)
            for kw, payload in _new_kwargs.items():
                flag = self.keyword2flag(kw)
                flag2kws[flag].add(kw)
            flag2kws = {flag: kws for flag, kws in flag2kws.items() if len(kws) > 1}
            assert flag2kws
            raise ValueError(f'many keyword to same flag: {flag2kws}')
        del _new_kwargs

        options = self.union_options(
            old_options=__old_options, new_options=new_options)
        assert options is not new_options
        assert options is not __old_options
        assert type(options) is dict
        return options


def keyword2flag__GNU(__kw:KeywordType) -> FlagType:
    '''

example:
>>> keyword2flag = keyword2flag__GNU
>>> keyword2flag('_h')
'-h'
>>> keyword2flag('help')
'--help'
>>> keyword2flag('help_xxx')
'--help-xxx'
'''
    if not __kw.isidentifier(): raise ValueError
    if not __kw: raise ValueError
    #if __kw[:2] == '__': raise ValueError
    if '__' in __kw: raise ValueError # to avoid '_MyClass__param'
    flag = __kw.replace('_', '-')
    if flag[0] != '-':
        flag = '--' + flag
    return flag



