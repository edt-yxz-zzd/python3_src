#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/IMaker4RecognizerLLoo.py

seed.recognize.recognizer_LLoo_.IMaker4RecognizerLLoo
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.IMaker4RecognizerLLoo -x
#]]]'''
__all__ = r'''
IMaker4RecognizerLLoo__5args_ex
    IMaker4RecognizerLLoo__5args
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.recognizer_LLoo_._common import (IForkable__stamp
,check_type_is, check_type_le, check_int_ge
,abstractmethod, override, ABC
)
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, IDependentTreeNode

___end_mark_of_excluded_global_names__0___ = ...

class IMaker4RecognizerLLoo__5args_ex(IDependentTreeNode):
    '#assume[inputter contains global runtime info...]'
    __slots__ = ()
    @property
    @abstractmethod
    def num_args4mkr4LLoo(sf, /):
        '-> uint'

    @abstractmethod
    def _mk_recognizer_LLoo5args_ex_(sf, inputter, /, *args):
        'inputter.fork() -> (*args){len=.num_args4mkr4LLoo} -> IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
    def mk_recognizer_LLoo5args_ex(sf, inputter, /, *args):
        'inputter.fork() -> (*args){len=.num_args4mkr4LLoo} -> IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
        check_type_le(IForkable__stamp, inputter)
        rgnr = sf._mk_recognizer_LLoo5args_ex_(inputter.fork(), *args)
        check_type_le(IRecognizerLLoo, rgnr)
        return rgnr

class IMaker4RecognizerLLoo__5args(IMaker4RecognizerLLoo__5args_ex):
    __slots__ = ()
    @abstractmethod
    def _mk_recognizer_LLoo5args_(sf, /, *args):
        '(*args){len=.num_args4mkr4LLoo} -> IRecognizerLLoo'

    def mk_recognizer_LLoo5args(sf, /, *args):
        '(*args){len=.num_args4mkr4LLoo} -> IRecognizerLLoo'
        rgnr = sf._mk_recognizer_LLoo5args_(*args)
        check_type_le(IRecognizerLLoo, rgnr)
        return rgnr

    @override
    def _mk_recognizer_LLoo5args_ex_(sf, inputter, /, *args):
        'inputter.fork() -> (*args){len=.num_args4mkr4LLoo} -> IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
        rgnr = sf._mk_recognizer_LLoo5args_(*args)
        return rgnr
    @override
    def mk_recognizer_LLoo5args_ex(sf, inputter, /, *args):
        'inputter.fork() -> (*args){len=.num_args4mkr4LLoo} -> IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
        rgnr = sf.mk_recognizer_LLoo5args(*args)
        return rgnr



__all__
from seed.recognize.recognizer_LLoo_.IMaker4RecognizerLLoo import IMaker4RecognizerLLoo__5args_ex, IMaker4RecognizerLLoo__5args
from seed.recognize.recognizer_LLoo_.IMaker4RecognizerLLoo import *
