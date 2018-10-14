
__all__ = '''
    ExePathType

    ArgType
    ArgsType
    ListArgsType
    TupleArgsType

    SwitchPayloadType
    PayloadType

    FlagType
    OptionsType
    DictOptionsType

    KeywordType
    KwargsType
    DictKwargsType

    SubprocessRun_KeywordType
    SubprocessRun_KwargsValueType
    SubprocessRun_KwargsType
    SubprocessRun_DictKwargsType


    IReprImmutableHelper
    MappingProxyType

    ABC
    abstractmethod
    not_implemented
    override
    '''.split()

from seed.abc import ABC, abstractmethod, not_implemented, override
from seed.abc.IReprImmutableHelper import IReprImmutableHelper
from types import MappingProxyType
#from subprocess import run, CalledProcessError, CompletedProcess, PIPE, STDOUT
#   subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, encoding=None, errors=None)

#import typing
#import collections.abc
from typing import (
    Sequence, Tuple, List
    , Mapping, Dict
    , Union #, Optional
    , IO, AnyStr
    #, Iterator
    )
#from types import MappingProxyType
from numbers import Real
#from subprocess import run, CalledProcessError, CompletedProcess, PIPE, STDOUT



if True:
    # below for IShellCmd:
    #   ExePathType
    #   ArgsType, PayloadType, FlagType, KeywordType, OptionsType, DictKwargsType
    # FlagType vs KeywordType
    #   see IShellCmd.keyword2flag
    #
    # typeof "args" in IShellCmd.args
    ExePathType = str

    ArgType = str
    ArgsType = Sequence[ArgType]
    ListArgsType = List[ArgType]
    TupleArgsType = Tuple[ArgType]

    SwitchPayloadType = bool
    PayloadType = Union[ArgType, SwitchPayloadType]

    FlagType = str
    OptionsType = Mapping[FlagType, PayloadType]
    DictOptionsType = Dict[FlagType, PayloadType]

    KeywordType = str
    KwargsType = Mapping[KeywordType, PayloadType]
    DictKwargsType = Dict[KeywordType, PayloadType]


if True:
    #below for CallSetting
    StreamType = Union[IO[AnyStr], int]
        # py3.6::17.5.1.1. Frequently Used Arguments::stdin, stdout and stderr
        # Valid values are PIPE, DEVNULL, an existing file descriptor (a positive integer), an existing file object, and None.
        # Additionally, stderr can be STDOUT
    # typeof "kwargs" (all keyword arguments) in subprocess.run(..., *, kwargs...)
    SubprocessRun_KeywordType = str # finite set
    SubprocessRun_KwargsValueType = Union[None, bool, str, Real, StreamType]
    SubprocessRun_KwargsType = Mapping[SubprocessRun_KeywordType, SubprocessRun_KwargsValueType]
    SubprocessRun_DictKwargsType = Dict[SubprocessRun_KeywordType, SubprocessRun_KwargsValueType]

    # typeof "args" in subprocess.run(args, *, ...)
    #SubprocessRun_ArgsType = ArgsType
    #SubprocessRun_ListArgsType = ListArgsType
        #CommandType = Sequence[str]


