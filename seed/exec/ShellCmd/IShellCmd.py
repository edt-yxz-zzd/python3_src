

__all__ = '''
    IShellCmd
    ExePathTypeEx
    '''.split()


from ._HasAttr_overwrite import _HasAttr_overwrite
from .IShellCmdHelper import IShellCmdHelper
from .is_instance_of import is_instance_of
from .common import (
    IReprImmutableHelper
    , MappingProxyType
    , abstractmethod


    , ExePathType
    , ArgType
    , ArgsType
    , ListArgsType
    , TupleArgsType

    , PayloadType

    , FlagType
    , OptionsType
    , DictOptionsType

    #, KeywordType
    , DictKwargsType
    )
from typing import Iterator, Tuple, Union


########################################

class IShellCmd(_HasAttr_overwrite, IReprImmutableHelper):
    '''

properties:
* overwrite : bool
    is old_options of this shell_cmd can be overwritten?
    given old_shell_cmd::IShellCmd
        when construct new shell_cmd:
            IShellCmd(overwrite=[True|False], old_shell_cmd, args, __old_options, **_new_kwargs)
        old_shell_cmd.overwrite will take effect
        if old_shell_cmd.overwrite:
            then __old_options and _new_kwargs may contains key in old_shell_cmd.old_options
        else:
            cannot
* executable_path : str # not ExePathTypeEx
* args : ArgsType
* old_options : OptionsType
    can be overwritten by new_options?? <<== overwrite
'''
    __slots__ = ()

    def ___get_args_kwargs___(self
        ) -> Tuple[bool, ExePathType, ListArgsType, DictOptionsType]:
        args = (self.overwrite, self.executable_path, list(self.args), dict(self.old_options))
        return (args, {})

    @property
    def executable_path(self) -> ExePathType: # not ExePathTypeEx
        return self.__executable_path
    @property
    def args(self) -> ArgsType:
        return self.__args
    @property
    def old_options(self) -> OptionsType:
        return self.__old_options


    def __init__(self
        , __overwrite:bool
        , __executable_path_ex:'ExePathTypeEx'
        , __args:ArgsType
        , __old_options:OptionsType
        , **_new_kwargs:PayloadType
        ) -> None:
        #assert isinstance(__executable_path_ex, (ExePathType, IShellCmd))
        #assert is_instance_of(__args, ArgsType)
        #assert is_instance_of(__old_options, OptionsType)
        #assert is_instance_of(_new_kwargs, DictKwargsType)

        # affect later use, not current
        _HasAttr_overwrite.__init__(self, overwrite=__overwrite)
        del __overwrite

        (__executable_path, __args, __old_options
        ) = type(self).__mk_init_args(
            __executable_path_ex, __args, __old_options, _new_kwargs)
        del __executable_path_ex, _new_kwargs

        assert type(__executable_path) is str
        assert type(__args) is tuple
        assert type(__old_options) is dict # fresh

        # str
        self.__executable_path = str(__executable_path)
        # tuple<str>
        self.__args = tuple(__args)
        # MappingProxyType<DictOptionsType>
        self.__old_options = MappingProxyType(__old_options)
        return

    def iextend(self
        , __overwrite:bool
        #, __executable_path_ex:'ExePathTypeEx'
        , __args:ArgsType
        , __old_options:OptionsType
        , **_new_kwargs:PayloadType
        ):
        __executable_path_ex = self
        return type(self).from_IShellCmd_init_args(
                    __overwrite, __executable_path_ex
                    , __args, __old_options, **_new_kwargs)

    @classmethod
    def from_IShellCmd_init_args(cls
        , __overwrite:bool
        , __executable_path_ex:'ExePathTypeEx'
        , __args:ArgsType
        , __old_options:OptionsType
        , **_new_kwargs:PayloadType
        ):
        return cls(__overwrite, __executable_path_ex
                    , __args, __old_options, **_new_kwargs)
    @classmethod
    def __mk_init_args(cls
        , __executable_path_ex:'ExePathTypeEx'
        , __args:ArgsType
        , __old_options:OptionsType
        , _new_kwargs:DictKwargsType
        ) -> Tuple[ExePathType, TupleArgsType, DictOptionsType]:

        if not isinstance(__executable_path_ex, (ExePathType, IShellCmd)): raise TypeError
        # seq except str
        if isinstance(__args, str): raise TypeError
        if not is_instance_of(__args, ArgsType): raise TypeError
        if not is_instance_of(__old_options, OptionsType): raise TypeError
        if not is_instance_of(_new_kwargs, DictKwargsType): raise TypeError



        maker = cls.make_IShellCmdHelper(overwrite=False)
        __old_options = maker.make_options(__old_options, **_new_kwargs)
        del maker

        if isinstance(__executable_path_ex, ExePathType):
            __executable_path = __executable_path_ex
            del __executable_path_ex

            __executable_path = str(__executable_path)
            __args = tuple(__args)
            __old_options = __old_options
        elif isinstance(__executable_path_ex, IShellCmd):
            old_shell_cmd = __executable_path_ex
            del __executable_path_ex

            __executable_path = old_shell_cmd.__executable_path
            __args = (*old_shell_cmd.__args, *__args)

            oldold_options = old_shell_cmd.__old_options
            maker = cls.make_IShellCmdHelper(
                                overwrite=old_shell_cmd.overwrite)
            __old_options = maker.union_options(
                    old_options=oldold_options, new_options=__old_options)
            del maker
        else:
            raise TypeError('__executable_path_ex is not str or IShellCmd: {!r}'.format(__executable_path_ex))


        # str                       # ExePathType
        assert type(__executable_path) is str
        # tuple<str>                # TupleArgsType
        assert type(__args) is tuple
        # dict<str, (str|bool)>     # DictOptionsType
        assert type(__old_options) is dict # fresh

        return __executable_path, __args, __old_options

    def to_run_args(self) -> ArgsType:
        # subprocess.run(args, ...)
        # subprocess.run(shell_cmd.to_run_args, ...)
        return [*self.to_iter_run_args()]

    @classmethod
    @abstractmethod
    def make_IShellCmdHelper(cls, *, overwrite:bool) -> IShellCmdHelper:
        raise NotImplementedError
    @abstractmethod
    def iter_seperators_of_options_and_args(self) -> Iterator[ArgType]:
        # gnu only??
        yield '--' # to seperate options and positional_arguments
        return
    @abstractmethod
    def iter_option_args(self, flag:FlagType, payload:ArgType) -> Iterator[ArgType]:
        yield flag
        yield payload
        return

        raise NotImplementedError
        if space:
            yield flag
            yield payload
        elif eq:
            yield flag
            yield '='
            yield payload
        elif eq_join:
            assert '=' not in flag
            yield f'{flag}={payload}'
        else:
            ...
    @abstractmethod
    def to_iter_run_args(self) -> Iterator[ArgType]:
        yield self.__executable_path
        for flag, payload in self.__old_options.items():
            if isinstance(payload, str):
                yield from self.iter_option_args(flag, payload)
            elif isinstance(payload, bool):
                switch = flag
                if payload:
                    yield switch
            else:
                raise TypeError(f'payload in options should be (str|bool): {payload!r}')

        if self.__args:
            yield from self.iter_seperators_of_options_and_args()
            yield from self.__args
        return



ExePathTypeEx = Union[ExePathType, IShellCmd]


