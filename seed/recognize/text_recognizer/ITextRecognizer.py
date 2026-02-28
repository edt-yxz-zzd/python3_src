#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer__doctest.py

seed.recognize.text_recognizer.ITextRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.text_recognizer.ITextRecognizer -x # -off_defs
#py -m nn_ns.app.doctest_cmd seed.recognize.text_recognizer.ITextRecognizer:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.recognize.text_recognizer.ITextRecognizer__doctest:__doc__ -ht # -ff -df
#######

[[
用于:解读冫某某某巛文本表达扌#表述冫某某某讠文本表达扌

可能会用于:
view script/对称多项式讠基表达.py
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.recognize.text_recognizer.ITextRecognizer   @f
from seed.recognize.text_recognizer.ITextRecognizer import *
]]]'''#'''
__all__ = r'''
parse_text_
    ParseResult
        OResult
        Errmsg
ITextRecognizer
    ITextRecognizer__postprocess6ok
    ITextRecognizer__fallback
    ITextRecognizer__flow
        ITextRecognizer__flow__cased_oresult7child
            ITextRecognizer__serial
            ITextRecognizer__sep_by
                ITextRecognizer__many
            ITextRecognizer__sep_end_by
                ITextRecognizer__end_by

    TextRecognizer__postprocess6ok
    TextRecognizer__unbox
    TextRecognizer__getitem
    TextRecognizer__box
    TextRecognizer__to_tuple
    TextRecognizer__to_finger_tree_seq

    TextRecognizer__constant_oresult
    TextRecognizer__constant_errmsg
    TextRecognizer__constant_text
    TextRecognizer__regex

    TextRecognizer__trial
    TextRecognizer__fallback
    TextRecognizer__enclosed

    TextRecognizer__serial
    TextRecognizer__sep_end_by
    TextRecognizer__sep_by
    TextRecognizer__end_by
    TextRecognizer__many

    TextRecognizer__serial__cased
    TextRecognizer__sep_end_by__cased
    TextRecognizer__sep_by__cased
    TextRecognizer__end_by__cased
    TextRecognizer__many__cased

    mk_tagged_txt_rgnr_
    mk_tagged_txt_rgnr_fallback_
    mk_ignorable_txt_rgnr_serial_


ITextRecognizer__flow
    ITextRecognizer__flow__cased_oresult7child
IOps4oresult_seq4flow_txt_rgnr
    IOps4oresult_seq4cased_flow_txt_rgnr

IOps4oresult_seq4flow_txt_rgnr
    IOps4oresult_seq4flow_txt_rgnr__wrapper
    Ops4oresult_seq4flow_txt_rgnr__using_list8oresult_seq
        ops4oresult_seq4flow_txt_rgnr__using_list8oresult_seq
    Ops4oresult_seq4flow_txt_rgnr__using_finger_tree_seq8oresult_seq
        ops4oresult_seq4flow_txt_rgnr__using_finger_tree_seq8oresult_seq
    IOps4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq
        Ops4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq__env_is_mapping
            ops4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq__env_is_mapping

IOps4oresult_seq4cased_flow_txt_rgnr
    IOps4oresult_seq4cased_flow_txt_rgnr__wrapper
    IOps4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq
        Ops4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq
            ops4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq
        Ops4oresult_seq4uncased_flow_txt_rgnr__using_list8oresult_seq
            ops4oresult_seq4uncased_flow_txt_rgnr__using_list8oresult_seq
    IOps4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq
        Ops4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq
            ops4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq
        Ops4oresult_seq4uncased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq
            ops4oresult_seq4uncased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq
    IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq
        IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq__env_is_mapping
env4ops4oresult_seq__ftSeq
env4ops4oresult_seq__list



'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.
#.
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
#.with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
#.    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from functools import cached_property
    #.from itertools import islice
    from seed.tiny_.containers import mk_tuple
    from seed.helper.repr_input import repr_helper
    from seed.tiny_.check import check_int_ge_le, check_int_ge, check_type_le, check_type_in, check_type_is, check_all_, check_may_, check_non_ABC, check_ABC, check_callable
    from seed.helper.ifNone import ifNone#ifNonef
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):

    #.from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
    #.#def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
    #.#    def _check6make_(sf, /):

    from seed.iters.flatten_recur import flatten_recur
    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
    from seed.types.Either import mk_Left, mk_Right
    from seed.data_funcs.finger_tree.ft23_7sized_seq import Seq
    from seed.tiny_.types5py import mk_MapView
    from seed.for_libs.for_re import mk_regex5or_pattern_

#.    from seed.debug.print_err import print_err
#.    from seed.func_tools.dot_ import dot_


#.#################################
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0
#.from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
#.lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
#.if 0:from seed.debug.print_err import print_err
#.
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

OResult = mk_namedtuple__check6make_(__name__, 'OResult', 'oresult end')
Errmsg = mk_namedtuple__check6make_(__name__, 'Errmsg', 'errmsg end severe')
OResult.ok = True
Errmsg.ok = False
def _check6make_(sf, /):
    check_int_ge(0, sf.end)
OResult._check6make_ = _check6make_
def _check6make_(sf, /):
    check_int_ge(0, sf.end)
    check_type_is(bool, sf.severe)
Errmsg._check6make_ = _check6make_
del _check6make_
ParseResult = (OResult, Errmsg)

class ITextRecognizer(ABC):
    __slots__ = ()
    @abstractmethod
    def _parse_text_(sf, env, txt, begin, end, /):
        'env -> txt/str -> begin/uint%(1+len(txt)) -> end/uint%(1+len(txt)) -> GI4parse{return-(Either GI4parse (OResult|Errmsg));yield-GI4arbitrary{return-(Either GI4arbitrary arbitrary);yield-GI4arbitrary}}'

def parse_text_(txt_rgnr, env, txt, begin, end, /):
    'ITextRecognizer -> env -> txt/str -> begin/uint%(1+len(txt)) -> end/uint%(1+len(txt)) -> ParseResult/(OResult|Errmsg)'
    check_type_is(str, txt)
    check_int_ge(0, begin)
    check_int_ge_le(begin, len(txt), end)
    eresult = flatten_recur(txt_rgnr._parse_text_(env, txt, begin, end), boxed=True)
    check_type_in(ParseResult, eresult)
    check_int_ge_le(begin, end, eresult.end)
    return eresult




















class ITextRecognizer__fallback(ITextRecognizer):
    'parallel:fallback'
    __slots__ = ()
    @property
    @abstractmethod
    def _txt_rgnr_seq_(sf, /):
        '-> [ITextRecognizer]'
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        es = []
        _end = begin
        for txt_rgnr in sf._txt_rgnr_seq_:
            eresult = yield txt_rgnr._parse_text_(env, txt, begin, end)
            match eresult:
                case OResult():
                    pass
                case Errmsg(severe=_severe):
                    if not _severe:
                        _end = max(_end, eresult.end)
                        es.append(eresult)
                        continue
                    pass
                case _:
                    raise 000
                #case
            return mk_Right(eresult)
        return mk_Right(Errmsg(errmsg=tuple(es), end=_end, severe=False))





















class IOps4oresult_seq4flow_txt_rgnr(ABC):
    'ops{oresult_seq{ITextRecognizer__flow}}'
    __slots__ = ()
    @abstractmethod
    def _mk_init_oresult_seq_(sf, env, /):
        'env -> oresult_seq # eg:list,seed.data_funcs.finger_tree.ft23_7sized_seq.Seq'
    @abstractmethod
    def _mk_oresult5oresult_seq_(sf, oresult_seq, /):
        'oresult_seq -> oresult/(immutable oresult_seq)'
    @abstractmethod
    def _iput4oresult_seq_(sf, oresult_seq, oresult7child, /):
        'oresult_seq -> oresult7child -> oresult_seq'
class IOps4oresult_seq4cased_flow_txt_rgnr(IOps4oresult_seq4flow_txt_rgnr):
    'ops{oresult_seq{ITextRecognizer__flow__cased_oresult7child}}'
    __slots__ = ()
    @property
    @abstractmethod
    def _whether_child_oresult_cased_(sf, /):
        '-> bool # [child_oresult == opaque if not _whether_child_oresult_cased_ else (ignore_vs_echo_vs_unpack/int%3, oresult)] #see:TextRecognizer__tag'
    @abstractmethod
    def _iappend4oresult_seq_(sf, oresult_seq, oresult7child, /):
        'oresult_seq -> oresult7child -> oresult_seq'
    @abstractmethod
    def _iextend4oresult_seq_(sf, oresult_seq, oresults7child, /):
        'oresult_seq -> Iter oresult7child -> oresult_seq'
    @override
    def _iput4oresult_seq_(sf, oresult_seq, oresult7child, /):
        'oresult_seq -> oresult7child -> oresult_seq'
        if not sf._whether_child_oresult_cased_:
            cased_oresult7child = (1, oresult7child)
        else:
            cased_oresult7child = oresult7child
        cased_oresult7child
        del oresult7child
        match cased_oresult7child:
            # (ignore_vs_echo_vs_unpack, ...)
            case (int(1), oresult7child):
                #echo
                oresult_seq = sf._iappend4oresult_seq_(oresult_seq, oresult7child)
            case (int(2), oresults7child):
                #unpack
                oresult_seq = sf._iextend4oresult_seq_(oresult_seq, oresults7child)
            case (int(0), _):
                #ignore
                pass
            case _:
                raise TypeError(cased_oresult7child)
            #case
        return oresult_seq

class IOps4oresult_seq4flow_txt_rgnr__wrapper(IOps4oresult_seq4flow_txt_rgnr):
    __slots__ = ()
    @property
    @abstractmethod
    def _ops4oresult_seq_(sf, /):
        '-> IOps4oresult_seq4flow_txt_rgnr'
    @override
    def _mk_init_oresult_seq_(sf, env, /):
        return sf._ops4oresult_seq_._mk_init_oresult_seq_(env)
    @override
    def _mk_oresult5oresult_seq_(sf, oresult_seq, /):
        return sf._ops4oresult_seq_._mk_oresult5oresult_seq_(oresult_seq)
    @override
    def _iput4oresult_seq_(sf, oresult_seq, oresult7child, /):
        return sf._ops4oresult_seq_._iput4oresult_seq_(oresult_seq, oresult7child)

class IOps4oresult_seq4cased_flow_txt_rgnr__wrapper(IOps4oresult_seq4flow_txt_rgnr__wrapper, IOps4oresult_seq4cased_flow_txt_rgnr):
    __slots__ = ()
    @property
    @abstractmethod
    def _ops4oresult_seq__cased_(sf, /):
        '-> IOps4oresult_seq4cased_flow_txt_rgnr'
    @property
    @override
    def _ops4oresult_seq_(sf, /):
        return sf._ops4oresult_seq__cased_
    @property
    @override
    def _whether_child_oresult_cased_(sf, /):
        return sf._ops4oresult_seq__cased_._whether_child_oresult_cased_
    @override
    def _iappend4oresult_seq_(sf, oresult_seq, oresult7child, /):
        return sf._ops4oresult_seq__cased_._iappend4oresult_seq_(oresult_seq, oresult7child)
    @override
    def _iextend4oresult_seq_(sf, oresult_seq, oresults7child, /):
        return sf._ops4oresult_seq__cased_._iextend4oresult_seq_(oresult_seq, oresults7child)






class Ops4oresult_seq4flow_txt_rgnr__using_list8oresult_seq(IOps4oresult_seq4flow_txt_rgnr):
    'ops{flow_txt_rgnr}:[oresult_seq::list]'
    __slots__ = ()
    @override
    def _mk_init_oresult_seq_(sf, env, /):
        return []
    @override
    def _mk_oresult5oresult_seq_(sf, oresult_seq, /):
        return tuple(oresult_seq)
    @override
    def _iput4oresult_seq_(sf, oresult_seq, oresult7child, /):
        oresult_seq.append(oresult7child)
        return oresult_seq
ops4oresult_seq4flow_txt_rgnr__using_list8oresult_seq = Ops4oresult_seq4flow_txt_rgnr__using_list8oresult_seq()

class Ops4oresult_seq4flow_txt_rgnr__using_finger_tree_seq8oresult_seq(IOps4oresult_seq4flow_txt_rgnr):
    'ops{flow_txt_rgnr}:[oresult_seq::seed.data_funcs.finger_tree.ft23_7sized_seq.Seq]'
    __slots__ = ()
    @override
    def _mk_init_oresult_seq_(sf, env, /):
        return Seq()
    @override
    def _mk_oresult5oresult_seq_(sf, oresult_seq, /):
        return oresult_seq
    @override
    def _iput4oresult_seq_(sf, oresult_seq, oresult7child, /):
        oresult_seq = oresult_seq.ipushR(oresult7child)
        return oresult_seq
ops4oresult_seq4flow_txt_rgnr__using_finger_tree_seq8oresult_seq = Ops4oresult_seq4flow_txt_rgnr__using_finger_tree_seq8oresult_seq()

class IOps4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq(IOps4oresult_seq4flow_txt_rgnr):
    'ops{flow_txt_rgnr}:=env.ops4oresult_seq'
    __slots__ = ()
    @abstractmethod
    def _get_ops4oresult_seq5env_(sf, env, /):
        'env -> ops4oresult_seq/IOps4oresult_seq4flow_txt_rgnr'

    @override
    def _mk_init_oresult_seq_(sf, env, /):
        ops4oresult_seq = sf._get_ops4oresult_seq5env_(env)
        _oresult_seq = ops4oresult_seq._mk_init_oresult_seq_(env)
        oresult_seq = (ops4oresult_seq, _oresult_seq)
        return oresult_seq
    @override
    def _mk_oresult5oresult_seq_(sf, oresult_seq, /):
        (ops4oresult_seq, _oresult_seq) = oresult_seq
        oresult7whole = ops4oresult_seq._mk_oresult5oresult_seq_(_oresult_seq)
        return oresult7whole
    @override
    def _iput4oresult_seq_(sf, oresult_seq, oresult7child, /):
        (ops4oresult_seq, _oresult_seq) = oresult_seq
        _oresult_seq = ops4oresult_seq._iput4oresult_seq_(_oresult_seq, oresult7child)
        oresult_seq = (ops4oresult_seq, _oresult_seq)
        return oresult_seq
class Ops4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq__env_is_mapping(IOps4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq):
    __slots__ = ()
    @override
    def _get_ops4oresult_seq5env_(sf, env, /):
        ops4oresult_seq = env[IOps4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq]
        return ops4oresult_seq
ops4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq__env_is_mapping = Ops4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq__env_is_mapping()








class IOps4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq(Ops4oresult_seq4flow_txt_rgnr__using_list8oresult_seq, IOps4oresult_seq4cased_flow_txt_rgnr):
    'ops{flow_txt_rgnr:cased_oresult7child}:[oresult_seq::list]'
    __slots__ = ()
    _iput4oresult_seq_ = IOps4oresult_seq4cased_flow_txt_rgnr._iput4oresult_seq_
    @override
    def _iappend4oresult_seq_(sf, oresult_seq, oresult7child, /):
        oresult_seq.append(oresult7child)
        return oresult_seq
    @override
    def _iextend4oresult_seq_(sf, oresult_seq, oresults7child, /):
        oresult_seq.extend(oresults7child)
        return oresult_seq
class Ops4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq(IOps4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq):
    __slots__ = ()
    #@override
    _whether_child_oresult_cased_ = True
ops4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq = Ops4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq()

class Ops4oresult_seq4uncased_flow_txt_rgnr__using_list8oresult_seq(IOps4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq):
    __slots__ = ()
    #@override
    _whether_child_oresult_cased_ = False
ops4oresult_seq4uncased_flow_txt_rgnr__using_list8oresult_seq = Ops4oresult_seq4uncased_flow_txt_rgnr__using_list8oresult_seq()

class IOps4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq(Ops4oresult_seq4flow_txt_rgnr__using_finger_tree_seq8oresult_seq, IOps4oresult_seq4cased_flow_txt_rgnr):
    'ops{flow_txt_rgnr:cased_oresult7child}:[oresult_seq::seed.data_funcs.finger_tree.ft23_7sized_seq.Seq]'
    __slots__ = ()
    _iput4oresult_seq_ = IOps4oresult_seq4cased_flow_txt_rgnr._iput4oresult_seq_
    @override
    def _iappend4oresult_seq_(sf, oresult_seq, oresult7child, /):
        oresult_seq = oresult_seq.ipushR(oresult7child)
        return oresult_seq
    @override
    def _iextend4oresult_seq_(sf, oresult_seq, oresults7child, /):
        check_type_is(Seq, oresult_seq)
        #.check_type_is(Seq, oresults7child)
        #.oresult_seq += oresults7child
        oresult_seq += Seq(oresults7child)
        return oresult_seq
class Ops4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq(IOps4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq):
    __slots__ = ()
    #@override
    _whether_child_oresult_cased_ = True
ops4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq = Ops4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq()

class Ops4oresult_seq4uncased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq(IOps4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq):
    __slots__ = ()
    #@override
    _whether_child_oresult_cased_ = False
ops4oresult_seq4uncased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq = Ops4oresult_seq4uncased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq()


class IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq(IOps4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq, IOps4oresult_seq4cased_flow_txt_rgnr):
    'ops{flow_txt_rgnr:cased_oresult7child}:=env.ops4oresult_seq__cased'
    __slots__ = ()
    _iput4oresult_seq_ = IOps4oresult_seq4cased_flow_txt_rgnr._iput4oresult_seq_
    @abstractmethod
    def _get_ops4oresult_seq5env__cased_(sf, env, /):
        'env -> ops4oresult_seq__cased/IOps4oresult_seq4cased_flow_txt_rgnr'
    @override
    def _get_ops4oresult_seq5env_(sf, env, /):
        return sf._get_ops4oresult_seq5env__cased_(env)

    @override
    def _iappend4oresult_seq_(sf, oresult_seq, oresult7child, /):
        (ops4oresult_seq__cased, _oresult_seq) = oresult_seq
        _oresult_seq = ops4oresult_seq__cased._iappend4oresult_seq_(_oresult_seq, oresult7child)
        oresult_seq = (ops4oresult_seq__cased, _oresult_seq)
        return oresult_seq
    @override
    def _iextend4oresult_seq_(sf, oresult_seq, oresults7child, /):
        (ops4oresult_seq__cased, _oresult_seq) = oresult_seq
        #.(_ops4oresult_seq__cased, _oresult_seq7child) = oresults7child
        #.if not ops4oresult_seq__cased is _ops4oresult_seq__cased:raise TypeError
        _oresult_seq7child = oresults7child
        _oresult_seq = ops4oresult_seq__cased._iextend4oresult_seq_(_oresult_seq, _oresult_seq7child)
        oresult_seq = (ops4oresult_seq__cased, _oresult_seq)
        return oresult_seq
class IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq__env_is_mapping(IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq):
    __slots__ = ()
    @override
    def _get_ops4oresult_seq5env__cased_(sf, env, /):
        b = sf._whether_child_oresult_cased_
        ops4oresult_seq__cased = env[(IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq, b)]
        if not b is ops4oresult_seq__cased._whether_child_oresult_cased_:raise TypeError
        return ops4oresult_seq__cased

env4ops4oresult_seq__ftSeq = mk_MapView(
{IOps4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq:ops4oresult_seq4flow_txt_rgnr__using_finger_tree_seq8oresult_seq
,(IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq, True):ops4oresult_seq4cased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq
,(IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq, False):ops4oresult_seq4uncased_flow_txt_rgnr__using_finger_tree_seq8oresult_seq
})
env4ops4oresult_seq__list = mk_MapView(
{IOps4oresult_seq4flow_txt_rgnr__using_env_ops4oresult_seq:ops4oresult_seq4flow_txt_rgnr__using_list8oresult_seq
,(IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq, True):ops4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq
,(IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq, False):ops4oresult_seq4uncased_flow_txt_rgnr__using_list8oresult_seq
})


_default_IOps4oresult_seq4cased_flow_txt_rgnr__using_xxx8oresult_seq = IOps4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq
_default_IOps4oresult_seq4cased_flow_txt_rgnr__using_xxx8oresult_seq = IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq__env_is_mapping





class ITextRecognizer__flow(IOps4oresult_seq4flow_txt_rgnr, ITextRecognizer):
    'flow'
    __slots__ = ()
    @abstractmethod
    def _mk_init_rgnz_state_(sf, env, begin, /):
        'env -> begin -> st'
    @abstractmethod
    def _next_step_info5rgnz_state_and_may_eresult7child_(sf, st, may_eresult7child, /):
        'st -> may eresult/ParseResult/(OResult|Errmsg)-> ((txt_rgnr/ITextRecognizer, st)|ok/bool|(errmsg,)|None{ok:=may_eresult7child is None or eresult7child.ok})'


    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        st = sf._mk_init_rgnz_state_(env, begin)
        rs = sf._mk_init_oresult_seq_(env)
        _begin = begin
        may_eresult7child = None
        while 1:
            match sf._next_step_info5rgnz_state_and_may_eresult7child_(st, may_eresult7child):
                case (txt_rgnr, st):
                    pass
                case bool(ok):
                    break
                case None:
                    ok = may_eresult7child is None or eresult7child.ok
                    break
                case (errmsg,):
                    ok = False
                    if may_eresult7child is None or eresult7child.ok:
                        eresult7child = Errmsg(errmsg=errmsg, end=_begin, severe=False)
                    else:
                        eresult7child = eresult7child._replace(errmsg=errmsg)
                    may_eresult7child = eresult7child
                    break
                case bad:
                    raise TypeError(bad)
                #case
            txt_rgnr
            eresult7child = yield txt_rgnr._parse_text_(env, txt, _begin, end)
            match eresult7child:
                case OResult(oresult=oresult7child, end=_begin):
                    rs = sf._iput4oresult_seq_(rs, oresult7child)
                case Errmsg():
                    pass
                case _:
                    raise TypeError(type(eresult7child))
                #case
            may_eresult7child = eresult7child
        ok
        if not ok:
            if may_eresult7child is None or eresult7child.ok:
                eresult7whole = Errmsg(errmsg=None, end=_begin, severe=not (_begin == begin))
            elif (eresult7child.severe or eresult7child.end == begin):
                eresult7whole = eresult7child
            else:
                eresult7whole = eresult7child._replace(severe=True)
            eresult7whole
        else:
            eresult7whole = OResult(oresult=sf._mk_oresult5oresult_seq_(rs), end=_begin)
        eresult7whole
        return mk_Right(eresult7whole)
class ITextRecognizer__flow__cased_oresult7child(IOps4oresult_seq4cased_flow_txt_rgnr, ITextRecognizer__flow):
    'flow:cased_oresult7child'
    __slots__ = ()


class ITextRecognizer__serial(ITextRecognizer__flow__cased_oresult7child):
    'serial'
    __slots__ = ()
    @property
    @abstractmethod
    def _txt_rgnr_seq_(sf, /):
        '-> [ITextRecognizer]'
    @override
    def _mk_init_rgnz_state_(sf, env, begin, /):
        return iter(sf._txt_rgnr_seq_)
    @override
    def _next_step_info5rgnz_state_and_may_eresult7child_(sf, st, may_eresult7child, /):
        it = st
        if may_eresult7child is None or may_eresult7child.ok:
            for txt_rgnr in it:
                return (txt_rgnr, st)
            return True
        return False

#.class ITextRecognizer__serial(ITextRecognizer):
#.    def _mk_init_oresult_seq_(sf, env, /):
#.        'env -> oresult_seq # eg:list,seed.data_funcs.finger_tree.ft23_7sized_seq.Seq'
#.        return []
#.    def _mk_oresult5oresult_seq_(sf, oresult_seq, /):
#.        'oresult_seq -> oresult/(immutable oresult_seq)'
#.        return tuple(oresult_seq)
#.    def _iappend4oresult_seq_(sf, oresult_seq, oresult7child, /):
#.        'oresult_seq -> oresult7child -> oresult_seq'
#.        oresult_seq.append(oresult7child)
#.        return oresult_seq
#.    def _iextend4oresult_seq_(sf, oresult_seq, oresults7child, /):
#.        'oresult_seq -> Iter oresult7child -> oresult_seq'
#.        oresult_seq.extend(oresults7child)
#.        return oresult_seq
#.    @override
#.    def _parse_text_(sf, env, txt, begin, end, /):
#.        b = sf._whether_child_oresult_cased_
#.        #rs = []
#.        rs = sf._mk_init_oresult_seq_(env)
#.        _begin = begin
#.        for txt_rgnr in sf._txt_rgnr_seq_:
#.            eresult = yield txt_rgnr._parse_text_(env, txt, _begin, end)
#.            match eresult:
#.                case OResult(oresult=_oresult, end=_begin):
#.                    if not b:
#.                        rs = sf._iappend4oresult_seq_(rs, _oresult)
#.                    else:
#.                        match _oresult:
#.                            # (ignore_vs_echo_vs_unpack, ...)
#.                            case (int(1), oresult7child):
#.                                #echo
#.                                rs = sf._iappend4oresult_seq_(rs, oresult7child)
#.                            case (int(2), oresults7child):
#.                                #unpack
#.                                rs = sf._iextend4oresult_seq_(rs, oresults7child)
#.                            case (int(0), _):
#.                                #ignore
#.                                pass
#.                            case _:
#.                                raise TypeError(_oresult)
#.                            #case
#.                        pass
#.                    continue
#.                case Errmsg(end=_end, severe=_severe):
#.                    if not (_severe or _end == begin):
#.                        eresult = eresult._replace(severe=True)
#.                    eresult
#.                    return mk_Right(eresult)
#.                case _:
#.                    raise 000
#.                #case
#.            raise 000
#.        return mk_Right(OResult(oresult=sf._mk_oresult5oresult_seq_(rs), end=_begin))




class ITextRecognizer__sep_by(ITextRecognizer__flow__cased_oresult7child):
    'sep_by'
    __slots__ = ()
    @property
    @abstractmethod
    def _txt_rgnr7item_(sf, /):
        '-> ITextRecognizer'
    @property
    @abstractmethod
    def _txt_rgnr7sep_item_(sf, /):
        '-> ITextRecognizer # eg:TextRecognizer__enclosed(txt_rgnr7sep, txt_rgnr7item, txt_rgnr7null_tuple)'
    @property
    @abstractmethod
    def _min_repeat_(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def _may_max_repeat_(sf, /):
        '-> may uint{>=_min_repeat_}'
    @override
    def _mk_init_rgnz_state_(sf, env, begin, /):
        return 0
    @override
    def _next_step_info5rgnz_state_and_may_eresult7child_(sf, st, may_eresult7child, /):
        sz = st
        if may_eresult7child is None:
            assert sz == 0
            if 0 == sf._may_max_repeat_:
                return True
            return (sf._txt_rgnr7item_, st:=0)
        eresult7child = may_eresult7child
        if eresult7child.ok:
            sz += 1
            if sz == sf._may_max_repeat_:
                return True
            return (sf._txt_rgnr7sep_item_, st:=sz)
        #fail:
        if eresult7child.severe:
            return False
        if sz < sf._min_repeat_:
            return False
        return True

class ITextRecognizer__many(ITextRecognizer__sep_by):
    'many/array'
    __slots__ = ()
    @property
    @override
    def _txt_rgnr7sep_item_(sf, /):
        return sf._txt_rgnr7item_



class ITextRecognizer__sep_end_by(ITextRecognizer__flow__cased_oresult7child):
    'sep_end_by'
    __slots__ = ()
    @property
    @abstractmethod
    def _txt_rgnr7end_(sf, /):
        '-> ITextRecognizer'
    @property
    @abstractmethod
    def _txt_rgnr7item_(sf, /):
        '-> ITextRecognizer'
    @property
    @abstractmethod
    def _txt_rgnr7sep_item_(sf, /):
        '-> ITextRecognizer # eg:TextRecognizer__enclosed(txt_rgnr7sep, txt_rgnr7item, txt_rgnr7null_tuple)'
    @property
    @abstractmethod
    def _min_repeat_(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def _may_max_repeat_(sf, /):
        '-> may uint{>=_min_repeat_}'
    @override
    def _mk_init_rgnz_state_(sf, env, begin, /):
        return (False, 0)
    @override
    def _next_step_info5rgnz_state_and_may_eresult7child_(sf, st, may_eresult7child, /):
        (b_item, sz) = st
        if may_eresult7child is None:
            assert sz == 0
            if sz >= sf._min_repeat_:
                return (sf._txt_rgnr7end_, st:=(False, sz))
            return (sf._txt_rgnr7item_, st:=(True, sz))

        eresult7child = may_eresult7child
        if eresult7child.ok:
            if not b_item:
                # end_by
                return True
            sz += 1
            if sz >= sf._min_repeat_:
                return (sf._txt_rgnr7end_, st:=(False, sz))
            return (sf._txt_rgnr7sep_item_, st:=(True, sz))
        #fail:
        if not b_item:
            # end_by
            if sz == sf._may_max_repeat_:
                return False
            if sz == 0:
                return (sf._txt_rgnr7item_, st:=(True, sz))
            return (sf._txt_rgnr7sep_item_, st:=(True, sz))
        return False


class ITextRecognizer__end_by(ITextRecognizer__sep_end_by):
    'end_by'
    __slots__ = ()
    @property
    @override
    def _txt_rgnr7sep_item_(sf, /):
        return sf._txt_rgnr7item_
























class ITextRecognizer__postprocess6ok(ITextRecognizer):
    __slots__ = ()
    @property
    @abstractmethod
    def _txt_rgnr_(sf, /):
        '-> ITextRecognizer'
    @abstractmethod
    def _postprocess6ok_(sf, oresult, /):
        'oresult -> oresult'
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        txt_rgnr = sf._txt_rgnr_
        eresult = yield txt_rgnr._parse_text_(env, txt, begin, end)
        match eresult:
            case OResult(oresult=oresult):
                _oresult = sf._postprocess6ok_(oresult)
                if not _oresult is oresult:
                    eresult = eresult._replace(oresult=_oresult)
                eresult
            case Errmsg():
                pass
            case _:
                raise 000
            #case
        return mk_Right(eresult)





class _ITextRecognizer__init__wrapped_txt_rgnr_seq(ITextRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnrs, /):
        txt_rgnrs = mk_tuple(txt_rgnrs)
        check_all_([check_type_le, ITextRecognizer], txt_rgnrs)
        sf._rgnrs = txt_rgnrs
    @property
    def _txt_rgnr_seq_(sf, /):
        '-> [ITextRecognizer]'
        return sf._rgnrs
    def __repr__(sf, /):
        return repr_helper(sf, sf._txt_rgnr_seq_)


class _ITextRecognizer__init__wrapped_txt_rgnr(ITextRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnr, /):
        check_type_le(ITextRecognizer, txt_rgnr)
        sf._rgnr = txt_rgnr
    @property
    def _txt_rgnr_(sf, /):
        '-> ITextRecognizer'
        return sf._rgnr
    def __repr__(sf, /):
        return repr_helper(sf, sf._txt_rgnr_)

class TextRecognizer__unbox(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6ok):
    @override
    def _postprocess6ok_(sf, oresult, /):
        [oresult] = oresult
        return oresult
class TextRecognizer__getitem(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6ok):
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnr, key, /):
        _ITextRecognizer__init__wrapped_txt_rgnr.__init__(sf, txt_rgnr)
        sf._k = key
    @override
    def _postprocess6ok_(sf, oresult, /):
        return oresult[sf._k]
    def __repr__(sf, /):
        return repr_helper(sf, sf._txt_rgnr_, sf._k)

class TextRecognizer__box(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6ok):
    @override
    def _postprocess6ok_(sf, oresult, /):
        return (oresult,)

class TextRecognizer__to_tuple(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6ok):
    @override
    def _postprocess6ok_(sf, oresult, /):
        return mk_tuple(oresult)

class TextRecognizer__to_finger_tree_seq(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6ok):
    @override
    def _postprocess6ok_(sf, oresult, /):
        return Seq(oresult)

class TextRecognizer__postprocess6ok(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6ok):
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnr, _postprocess6ok_, /):
        _ITextRecognizer__init__wrapped_txt_rgnr.__init__(sf, txt_rgnr)
        check_callable(_postprocess6ok_)
        sf._pf6ok = _postprocess6ok_
    @override
    def _postprocess6ok_(sf, oresult, /):
        return sf._pf6ok(oresult)
    def __repr__(sf, /):
        return repr_helper(sf, sf._txt_rgnr_, sf._pf6ok)

class TextRecognizer__trial(_ITextRecognizer__init__wrapped_txt_rgnr):
    ___no_slots_ok___ = True
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        txt_rgnr = sf._txt_rgnr_
        eresult = yield txt_rgnr._parse_text_(env, txt, begin, end)
        match eresult:
            case OResult():
                pass
            case Errmsg(severe=_severe):
                if _severe:
                    eresult = eresult._replace(severe=False)
                pass
            case _:
                raise 000
            #case
        return mk_Right(eresult)





class TextRecognizer__constant_oresult(ITextRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, oresult, /):
        sf._ores = oresult
    def __repr__(sf, /):
        return repr_helper(sf, sf._oresult_)
    @property
    def _oresult_(sf, /):
        '-> oresult'
        return sf._ores
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        return mk_Right(OResult(oresult=sf._oresult_, end=begin))
        777;yield


class TextRecognizer__constant_errmsg(ITextRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, errmsg, severe, /):
        check_type_is(bool, severe)
        sf._err = errmsg
        sf._svr = severe
    def __repr__(sf, /):
        return repr_helper(sf, sf._errmsg_, sf._severe_)
    @property
    def _errmsg_(sf, /):
        '-> errmsg'
        return sf._err
    @property
    def _severe_(sf, /):
        '-> severe'
        return sf._svr
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        return mk_Right(Errmsg(errmsg=sf._errmsg_, end=begin, severe=sf._severe_))
        777;yield

class TextRecognizer__constant_text(ITextRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, text, /):
        check_type_is(str, text)
        sf._txt = text
    def __repr__(sf, /):
        return repr_helper(sf, sf._text_)
    @property
    def _text_(sf, /):
        '-> text'
        return sf._txt
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        txt7expected = sf._text_
        if not (_end:=begin + len(txt7expected)) <= end:
            return mk_Right(Errmsg(errmsg=('unmatched:EOF', txt7expected, len(txt7expected), end-begin), end=begin, severe=False))
        txt7actual = txt[begin:_end]
        if not txt7actual == txt7expected:
            return mk_Right(Errmsg(errmsg=('unmatched:NE', txt7expected, txt7actual), end=begin, severe=False))
        return mk_Right(OResult(oresult=txt7expected, end=_end))
        777;yield


class TextRecognizer__regex(ITextRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, regex_or_pattern, /):
        sf._rgx = mk_regex5or_pattern_(regex_or_pattern)
    def __repr__(sf, /):
        return repr_helper(sf, sf._regex_)
    #.    return repr_helper(sf, sf._pattern_)
    #.@property
    #.def _pattern_(sf, /):
    #.    '-> pattern'
    #.    return sf._regex_.pattern
    @property
    def _regex_(sf, /):
        '-> regex'
        return sf._rgx
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        regex = sf._regex_
        m = regex.match(txt, begin, end)
        if not m:
            return mk_Right(Errmsg(errmsg=('unmatched:', regex), end=begin, severe=False))
        _end = m.end()
        #.txt7actual = m.group(0)
        #.oresult = txt7actual
        #.oresult = (txt7actual, m)
        oresult = m
        return mk_Right(OResult(oresult=oresult, end=_end))
        777;yield

























class _I_init__min__may_max:
    def __init__(sf, min_repeat, may_max_repeat, /):
        check_int_ge(0, min_repeat)
        check_may_([check_int_ge, min_repeat], may_max_repeat)
        sf._minsz = min_repeat
        sf._maymaxsz = may_max_repeat
    @property
    @override
    def _min_repeat_(sf, /):
        '-> uint'
        return sf._minsz
    @property
    @override
    def _may_max_repeat_(sf, /):
        '-> may uint{>=_min_repeat_}'
        return sf._maymaxsz


#.class _I_init__min__may_max__rgnr7item(_I_init__min__may_max):
#.    def __init__(sf, min_repeat, may_max_repeat, txt_rgnr7item, /):
#.        _I_init__min__may_max.__init__(sf, min_repeat, may_max_repeat)
#.        check_type_le(ITextRecognizer, txt_rgnr7item)
#.        sf._rgnr7item = txt_rgnr7item
#.    @property
#.    @override
#.    def _txt_rgnr7item_(sf, /):
#.        return sf._rgnr7item

class _I_init__rgnr7sep_item:
    def __init__(sf, txt_rgnr7item, may_txt_rgnr7sep_item, /):
        #txt_rgnr7sep_item = TextRecognizer__enclosed(txt_rgnr7sep, txt_rgnr7item, _lazy_data.txt_rgnr7null_tuple)
        txt_rgnr7sep_item = ifNone(may_txt_rgnr7sep_item, txt_rgnr7item)
        check_type_le(ITextRecognizer, txt_rgnr7item)
        check_type_le(ITextRecognizer, txt_rgnr7sep_item)
        #sf._rgnr7sep = txt_rgnr7sep
        sf._rgnr7item = txt_rgnr7item
        sf._rgnr7sep_item = txt_rgnr7sep_item
    #.@property
    #.def _txt_rgnr7sep_(sf, /):
    #.    return sf._rgnr7sep
    @property
    @override
    def _txt_rgnr7item_(sf, /):
        return sf._rgnr7item
    @property
    @override
    def _txt_rgnr7sep_item_(sf, /):
        return sf._rgnr7sep_item
def _get_may_txt_rgnr7sep_item_(sf, /):
    x = sf._txt_rgnr7sep_item_
    y = sf._txt_rgnr7item_
    may_txt_rgnr7sep_item = None if x is y else x
    return may_txt_rgnr7sep_item
class _I_init__min__may_max__rgnr7sep_item(_I_init__min__may_max, _I_init__rgnr7sep_item):
    def __init__(sf, min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item, /):
        _I_init__min__may_max.__init__(sf, min_repeat, may_max_repeat)
        _I_init__rgnr7sep_item.__init__(sf, txt_rgnr7item, may_txt_rgnr7sep_item)
class _I_init__min__may_max__rgnr7sep_item__rgnr7end(_I_init__min__may_max__rgnr7sep_item):
    def __init__(sf, min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item, txt_rgnr7end, /):
        _I_init__min__may_max__rgnr7sep_item.__init__(sf, min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item)
        check_type_le(ITextRecognizer, txt_rgnr7end)
        sf._rgnr7end = txt_rgnr7end
    @property
    @override
    def _txt_rgnr7end_(sf, /):
        return sf._rgnr7end


class TextRecognizer__sep_end_by(_I_init__min__may_max__rgnr7sep_item__rgnr7end, _default_IOps4oresult_seq4cased_flow_txt_rgnr__using_xxx8oresult_seq, ITextRecognizer__sep_end_by):
    ___no_slots_ok___ = True
    #@override
    _whether_child_oresult_cased_ = False
    def __repr__(sf, /):
        may_txt_rgnr7sep_item = _get_may_txt_rgnr7sep_item_(sf)
        return repr_helper(sf, sf._min_repeat_, sf._may_max_repeat_, sf._txt_rgnr7item_, may_txt_rgnr7sep_item, sf._txt_rgnr7end_)

class TextRecognizer__sep_by(_I_init__min__may_max__rgnr7sep_item, _default_IOps4oresult_seq4cased_flow_txt_rgnr__using_xxx8oresult_seq, ITextRecognizer__sep_by):
    ___no_slots_ok___ = True
    #@override
    _whether_child_oresult_cased_ = False
    def __repr__(sf, /):
        may_txt_rgnr7sep_item = _get_may_txt_rgnr7sep_item_(sf)
        return repr_helper(sf, sf._min_repeat_, sf._may_max_repeat_, sf._txt_rgnr7item_, may_txt_rgnr7sep_item)




class TextRecognizer__end_by(TextRecognizer__sep_end_by):
    ___no_slots_ok___ = True
    def __init__(sf, min_repeat, may_max_repeat, txt_rgnr7item, txt_rgnr7end, /):
        TextRecognizer__sep_end_by.__init__(sf, min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item:=None, txt_rgnr7end)
    def __repr__(sf, /):
        return repr_helper(sf, sf._min_repeat_, sf._may_max_repeat_, sf._txt_rgnr7item_, sf._txt_rgnr7end_)

class TextRecognizer__many(TextRecognizer__sep_by):
    ___no_slots_ok___ = True
    def __init__(sf, min_repeat, may_max_repeat, txt_rgnr7item, /):
        TextRecognizer__sep_by.__init__(sf, min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item:=None)
    def __repr__(sf, /):
        return repr_helper(sf, sf._min_repeat_, sf._may_max_repeat_, sf._txt_rgnr7item_)



class TextRecognizer__sep_end_by__cased(TextRecognizer__sep_end_by):
    ___no_slots_ok___ = True
    #@override
    _whether_child_oresult_cased_ = True
class TextRecognizer__sep_by__cased(TextRecognizer__sep_by):
    ___no_slots_ok___ = True
    #@override
    _whether_child_oresult_cased_ = True

class TextRecognizer__end_by__cased(TextRecognizer__end_by):
    ___no_slots_ok___ = True
    #@override
    _whether_child_oresult_cased_ = True

class TextRecognizer__many__cased(TextRecognizer__many):
    ___no_slots_ok___ = True
    #@override
    _whether_child_oresult_cased_ = True







class TextRecognizer__fallback(_ITextRecognizer__init__wrapped_txt_rgnr_seq, ITextRecognizer__fallback):
    ___no_slots_ok___ = True


class _ITextRecognizer__serial__list__init(_ITextRecognizer__init__wrapped_txt_rgnr_seq, _default_IOps4oresult_seq4cased_flow_txt_rgnr__using_xxx8oresult_seq, ITextRecognizer__serial):
    ___no_slots_ok___ = True
class TextRecognizer__serial(_ITextRecognizer__serial__list__init):
    ___no_slots_ok___ = True
    #@override
    _whether_child_oresult_cased_ = False
check_non_ABC(TextRecognizer__serial)
class TextRecognizer__serial__cased(TextRecognizer__serial):
    ___no_slots_ok___ = True
    #@override
    _whether_child_oresult_cased_ = True

class TextRecognizer__enclosed(TextRecognizer__serial):
    'used for ignore'
    #no:TextRecognizer__enclosed__cased:<<==since echo oresult7content
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnr7open, txt_rgnr7content, txt_rgnr7close, /):
        _ITextRecognizer__init__wrapped_txt_rgnr_seq.__init__(sf, (txt_rgnr7open, txt_rgnr7content, txt_rgnr7close))
    def __repr__(sf, /):
        return repr_helper(sf, *sf._txt_rgnr_seq_)


    #@override
    _whether_child_oresult_cased_ = False
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        eresult = yield super()._parse_text_(env, txt, begin, end)
        match eresult:
            case OResult(oresult=(_, oresult7content, _)):
                eresult = eresult._replace(oresult=oresult7content)
            case Errmsg():
                pass
            case _:
                raise 000
            #case
        return mk_Right(eresult)



#no:TextRecognizer__tag
def mk_tagged_txt_rgnr_(tag, txt_rgnr, /):
    return TextRecognizer__serial([TextRecognizer__constant_oresult(tag), txt_rgnr])
def mk_tagged_txt_rgnr_fallback_(tag__txt_rgnr__pairs, /):
    return TextRecognizer__fallback(mk_tagged_txt_rgnr_(tag, txt_rgnr) for tag, txt_rgnr in tag__txt_rgnr__pairs)


class _LazyData:
    @cached_property
    def txt_rgnr7null_tuple(sf, /):
        return TextRecognizer__constant_oresult(())
    @cached_property
    def regex_010_01_10(sf, /):
        import re
        regex_010 = re.compile(r'0+10+')
        regex_01 = re.compile(r'0+1')
        regex_10 = re.compile(r'10+')
        return (regex_010, regex_01, regex_10)
_lazy_data = _LazyData()

def mk_ignorable_txt_rgnr_serial_(ignore__txt_rgnr__pairs, /):
    ps = mk_tuple(ignore__txt_rgnr__pairs)
    ignores = [ignore for ignore, txt_rgnr in ps]
    txt_rgnrs = [txt_rgnr for ignore, txt_rgnr in ps]
    for ignore in ignores:
        check_type_is(bool, ignore)
    for txt_rgnr in txt_rgnrs:
        check_type_le(ITextRecognizer, txt_rgnr)


    if not any(ignores):
        return TextRecognizer__serial(txt_rgnrs)

    txt_rgnr7null_tuple = _lazy_data.txt_rgnr7null_tuple
    if all(ignores):
        return TextRecognizer__enclosed(TextRecognizer__serial(txt_rgnrs), txt_rgnr7null_tuple, txt_rgnr7null_tuple)

    return TextRecognizer__serial__cased(mk_tagged_txt_rgnr_(int(not ignore), txt_rgnr) for ignore, txt_rgnr in ps)






































def __():
    for nm in sorted(globals()):
        if not nm.startswith('TextRecognizer'):continue
        assert nm.startswith('TextRecognizer__'), nm
        cls = globals()[nm]
        check_type_le(type, cls)
        check_non_ABC(cls)
__()


def __():
    for nm in sorted(globals()):
        if not nm.startswith('ITextRecognizer'):continue
        assert nm.startswith('ITextRecognizer__') or nm == 'ITextRecognizer', nm
        cls = globals()[nm]
        check_type_le(type, cls)
        check_ABC(cls)
__()





__all__
from seed.recognize.text_recognizer.ITextRecognizer import *
