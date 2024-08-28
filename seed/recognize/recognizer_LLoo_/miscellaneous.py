#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/miscellaneous.py

seed.recognize.recognizer_LLoo_.miscellaneous
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.miscellaneous -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.miscellaneous:__doc__ -ht
#]]]'''
__all__ = r'''
Error4IRecognizerLLoo
    ParallelError4IRecognizerLLoo
        Error__not_only_one_match
    LogicError4IRecognizerLLoo
        Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
        Error__inputter_changed
    TypeError4IRecognizerLLoo
        Error__too_few_args
        Error__too_many_args
KindError
LookupError__circle_ref
IScene
    IScene__register
    SceneView
    Scene
        Scene__register
    mk_Scene_ex
IDependentTreeNode
    IDependentTreeNode__no_ref
    IDependentTreeNode__no_children
        IDependentTreeNode__leaf
        IDependentTreeNode__ref
    IDependentTreeNode__wrapper
IWithScene
INamed
IWrapper
    ILazyWrapper

TmpSnapshot4Inputter
BaseReply
    Signal__HeaderCompleted
    Reply4IRecognizerLLoo
BaseHandler4gi4two_phases_recognize
    parse__via_IRecognizerLLoo
    mk_gi4skip_header_signal
    mk_gi4header_signal_at_beginning
    mk_gi4patch_header_signal_if_ok
    mk_gi4validate_two_phases
IMaker4RecognizerLLoo__5args_ex
    IMaker4RecognizerLLoo__5args
IInstruction4flow4LLoo
    Instruction4flow4LLoo__wrapper
    Instruction4flow4LLoo__hdr_sgnl
    Instruction4flow4LLoo__return
    Instruction4flow4LLoo__goto
    Instruction4flow4LLoo__switch
    Instruction4flow4LLoo__exec
    Instruction4flow4LLoo__del_nms6ctx
    Instruction4flow4LLoo__mkr4rgnr7ctx
ICtxUpdater__5oresult
    CtxUpdater__5oresult__assign_nm6ctx
    CtxUpdater__5oresult__assign_nms6ctx
    CtxUpdater__5oresult__no_update
    no_op_updater
WhetherForwardHeaderSignal
    HForwardHeaderSignal
    HNoHeaderSignal
EitherTailWForwardOrEResult
    TailForwardHeaderSignal
    TailNoHeaderSignal
    FinalEResult
    FinalOResult
    FinalErrmsg
IMaker4RecognizerLLoo__5ctx
    rgnr_or2mkr4rgnr7ctx
    Maker4RecognizerLLoo__5ctx__constant
IMaker4RecognizerLLoo__5oresult
    Maker4RecognizerLLoo__5oresult__4switch_branches
    Maker4RecognizerLLoo__5oresult__constant_rgnr
ICallable__using_IDependentTreeNode
    Callable__ref
_IDependentTreeNode__ref__init






ITokenSetQuery
    TokenSetQuery__and
    TokenSetQuery__or
    ITokenSetQuery__leaf
        TokenSetQuery__any_token
            token_set_query__any_token
    ITokenSetQuery__wrapper
        TokenSetQuery__not
        ITokenSetQuery__ref
            TokenSetQuery__ref
    ITokenKeySetQuery
        ITokenKeySetQuery__wrapper
            TokenKeySetQuery__not
        TokenKeySetQuery__and
        TokenKeySetQuery__or
        ICharTokenKeySetQuery
            ICharTokenKeySetQuery__wrapper
            CharTokenKeySetQuery__not
            CharTokenKeySetQuery__and
            CharTokenKeySetQuery__or
            ICharTokenKeySetQuery__using_regex
                CharTokenKeySetQuery__using_regex
            ICharTokenKeySetQuery__using_py_str_method
                CharTokenKeySetQuery__using_py_str_method
CharTokenKeySetQuery__using_regex
    char_set_query__regex__w
    char_set_query__regex__W
    char_set_query__regex__s
    char_set_query__regex__S
    char_set_query__regex__d
    char_set_query__regex__D
CharTokenKeySetQuery__using_py_str_method
    char_set_query__isalnum
    char_set_query__not_isalnum
    char_set_query__isalpha
    char_set_query__not_isalpha
    char_set_query__isascii
    char_set_query__not_isascii
    char_set_query__isdecimal
    char_set_query__not_isdecimal
    char_set_query__isdigit
    char_set_query__not_isdigit
    char_set_query__isidentifier
    char_set_query__not_isidentifier
    char_set_query__islower
    char_set_query__not_islower
    char_set_query__isnumeric
    char_set_query__not_isnumeric
    char_set_query__isprintable
    char_set_query__not_isprintable
    char_set_query__isspace
    char_set_query__not_isspace
    char_set_query__istitle
    char_set_query__not_istitle
    char_set_query__isupper
    char_set_query__not_isupper

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

######################
from seed.recognize.recognizer_LLoo_.IScene import \
(KindError
,LookupError__circle_ref
,IWithScene
,IScene
,    IScene__register
,INamed
,IWrapper
,    ILazyWrapper
,IDependentTreeNode
,    IDependentTreeNode__no_ref
,    IDependentTreeNode__no_children
,        IDependentTreeNode__leaf
,    IDependentTreeNode__wrapper
,    IDependentTreeNode__ref
)

from seed.recognize.recognizer_LLoo_.Scene import SceneView, Scene, Scene__register, mk_Scene_ex


from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import \
(Error4IRecognizerLLoo
,    ParallelError4IRecognizerLLoo
,        Error__not_only_one_match
,    LogicError4IRecognizerLLoo
,        Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
,        Error__inputter_changed
,    TypeError4IRecognizerLLoo
,        Error__too_few_args
,        Error__too_many_args
,KindError
,LookupError__circle_ref
#
,IScene
,    IScene__register
#
,IDependentTreeNode
,    IDependentTreeNode__no_ref
,        IDependentTreeNode__leaf
,    IDependentTreeNode__no_children
,        IDependentTreeNode__leaf
,        IDependentTreeNode__ref
,    IDependentTreeNode__wrapper
#
,IWithScene
,INamed
,IWrapper
,    ILazyWrapper
,        IDependentTreeNode__ref
#
,TmpSnapshot4Inputter
,BaseReply
,    Signal__HeaderCompleted
,    Reply4IRecognizerLLoo
#
,BaseHandler4gi4two_phases_recognize
,    parse__via_IRecognizerLLoo
,    mk_gi4skip_header_signal
,    mk_gi4header_signal_at_beginning
,    mk_gi4patch_header_signal_if_ok
,    mk_gi4validate_two_phases
)
from seed.recognize.recognizer_LLoo_.IMaker4RecognizerLLoo import IMaker4RecognizerLLoo__5args_ex, IMaker4RecognizerLLoo__5args

from seed.recognize.recognizer_LLoo_.combinator_LLoo__flow import \
(IInstruction4flow4LLoo
,    Instruction4flow4LLoo__wrapper
,        Instruction4flow4LLoo__hdr_sgnl
,    Instruction4flow4LLoo__return
,    Instruction4flow4LLoo__goto
,    Instruction4flow4LLoo__switch
#
,    Instruction4flow4LLoo__exec
,    Instruction4flow4LLoo__del_nms6ctx
,    Instruction4flow4LLoo__mkr4rgnr7ctx
,        ICtxUpdater__5oresult
#
,ICtxUpdater__5oresult
,    CtxUpdater__5oresult__assign_nm6ctx
,    CtxUpdater__5oresult__assign_nms6ctx
,    CtxUpdater__5oresult__no_update
,        no_op_updater
)

from seed.recognize.recognizer_LLoo_.combinator_LLoo__gi8flow import \
(WhetherForwardHeaderSignal
,   HForwardHeaderSignal
,   HNoHeaderSignal
,EitherTailWForwardOrEResult
,   TailForwardHeaderSignal
,   TailNoHeaderSignal
,   FinalEResult
,       FinalOResult
,       FinalErrmsg
)


from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import IMaker4RecognizerLLoo__5ctx, rgnr_or2mkr4rgnr7ctx, Maker4RecognizerLLoo__5ctx__constant

from seed.recognize.recognizer_LLoo_.combinator_LLoo__switch import \
(IMaker4RecognizerLLoo__5oresult
,   Maker4RecognizerLLoo__5oresult__4switch_branches
,   Maker4RecognizerLLoo__5oresult__constant_rgnr
)

from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import ICallable__using_IDependentTreeNode, Callable__ref, _IDependentTreeNode__ref__init


######################
from seed.recognize.recognizer_LLoo_.stream.pure_stream import \
(ITokenSetQuery
,   ITokenSetQuery__leaf
,       _ITokenSetQuery__op__init
,           TokenSetQuery__and
,           TokenSetQuery__or
,       TokenSetQuery__not
,       TokenSetQuery__any_token
,           token_set_query__any_token
,   ITokenSetQuery__wrapper
,       ITokenSetQuery__ref
,           TokenSetQuery__ref
,Case4TokenExtraction
)

from seed.recognize.recognizer_LLoo_.stream.token_stream import \
(ITokenKeySetQuery
,   ITokenKeySetQuery__wrapper
,       TokenKeySetQuery__not
,       _ITokenKeySetQuery__op__init
,           TokenKeySetQuery__and
,           TokenKeySetQuery__or
)

from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(ICharTokenKeySetQuery
,   ICharTokenKeySetQuery__wrapper
,       CharTokenKeySetQuery__not
,       CharTokenKeySetQuery__and
,       CharTokenKeySetQuery__or
,   ICharTokenKeySetQuery__using_regex
,       CharTokenKeySetQuery__using_regex
,   ICharTokenKeySetQuery__using_py_str_method
,       CharTokenKeySetQuery__using_py_str_method
)


from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(char_set_query__regex__w
,char_set_query__regex__W
,char_set_query__regex__s
,char_set_query__regex__S
,char_set_query__regex__d
,char_set_query__regex__D
)

from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(char_set_query__isalnum
,char_set_query__not_isalnum
,char_set_query__isalpha
,char_set_query__not_isalpha
,char_set_query__isascii
,char_set_query__not_isascii
,char_set_query__isdecimal
,char_set_query__not_isdecimal
,char_set_query__isdigit
,char_set_query__not_isdigit
,char_set_query__isidentifier
,char_set_query__not_isidentifier
,char_set_query__islower
,char_set_query__not_islower
,char_set_query__isnumeric
,char_set_query__not_isnumeric
,char_set_query__isprintable
,char_set_query__not_isprintable
,char_set_query__isspace
,char_set_query__not_isspace
,char_set_query__istitle
,char_set_query__not_istitle
,char_set_query__isupper
,char_set_query__not_isupper
)


######################
__all__
from seed.recognize.recognizer_LLoo_.miscellaneous import *
