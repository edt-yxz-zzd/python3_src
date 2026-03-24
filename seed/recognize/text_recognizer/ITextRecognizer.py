#__all__:goto
#TODO:test&update__all__:
    #repr_as_,TextRecognizer__repr
r'''[[[
e ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer__doctest.py

py -m seed.recognize.text_recognizer.ITextRecognizer
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
BaseError
    ParseFail
parse_text_
    parse_text7full_
    parse_text7raise_
    parse_text7exact_
    check_parse_result__between_
        check_parse_result_
    ParseResult
        OResult
        Errmsg
ITextRecognizer
    ITextRecognizer__postprocess
    ITextRecognizer__postprocess6ok
        ITextRecognizer__postprocess6oresult
    ITextRecognizer__postprocess6ko
        ITextRecognizer__postprocess6errmsg
    ITextRecognizer__fallback
    ITextRecognizer__flow
        ITextRecognizer__flow__cased_oresult7child
            ITextRecognizer__serial
            ITextRecognizer__sep_by
                ITextRecognizer__many
            ITextRecognizer__sep_end_by
                ITextRecognizer__end_by

    TextRecognizer__inside
    TextRecognizer__span
    TextRecognizer__span6regex
    TextRecognizer__repr

    ITextRecognizer__postprocess
        TextRecognizer__fullmatched
    TextRecognizer__postprocess6ok
        TextRecognizer__postprocess6oresult
        TextRecognizer__tag
    TextRecognizer__postprocess6ko
        TextRecognizer__postprocess6errmsg
        TextRecognizer__named
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







mk_txt_rgnr__span_
mk_txt_rgnr__span6regex_
mk_txt_rgnr__regex_
mk_txt_rgnr__text_
mk_txt_rgnr__oresult_
mk_txt_rgnr__errmsg_


mk_txt_rgnr__serial_
mk_txt_rgnr__sep_end_by_
mk_txt_rgnr__sep_by_
mk_txt_rgnr__end_by_
mk_txt_rgnr__many_

txt_rgnr5or_regex_
txt_rgnr5or_txt_





mk_txt_rgnr7sep_item_

check_may_group_or_groups_
xget_groups5re_match_





BaseError
ParseFail
check_parse_result_
check_parse_result__between_
parse_text7full_
parse_text7raise_
parse_text7exact_
ITextRecognizer__postprocess
TextRecognizer__fullmatched
TextRecognizer__inside
TextRecognizer__span
TextRecognizer__span6regex
mk_txt_rgnr__span_
mk_txt_rgnr__span6regex_
span5re_matchT_
check_xgroup_


TextRecognizer__repr
    name5or_named_obj_
'''.split()#'''
    # ++@20260313:_BaseTextRecognizer__ops4mkr
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
    from seed.helper.repr_input import repr_helper, repr_helper__str
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

    from seed.tiny_.mk_fdefault import mk_default

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

class BaseError(Exception):pass
class ParseFail(BaseError):pass

OResult = mk_namedtuple__check6make_(__name__, 'OResult', 'oresult end')
Errmsg = mk_namedtuple__check6make_(__name__, 'Errmsg', 'errmsg end severe')
OResult.ok = True
Errmsg.ko = True
OResult.ko = False
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



class _BaseTextRecognizer__ops4mkr:
    # ++@20260313

    ##################
    def on_ok_(txt_rgnr, _postprocess6oresult_, _imay_num_args4postprocess6oresult_=1, /):
        'ITextRecognizer -> imay uint%2 -> (case _imay_num_args4postprocess6oresult_ of {-1:oresult; 0:(() -> oresult); 1:(oresult -> oresult);}) -> ITextRecognizer'
        if _imay_num_args4postprocess6oresult_ == 1:
            oresult2oresult_ = _postprocess6oresult_
            return TextRecognizer__postprocess6ok(txt_rgnr, oresult2oresult_)
        return TextRecognizer__postprocess6oresult(txt_rgnr, _imay_num_args4postprocess6oresult_, _postprocess6oresult_)
        #.def on_ok_(txt_rgnr, oresult2oresult_, /):
        #.    return TextRecognizer__postprocess6ok(txt_rgnr, oresult2oresult_)
    def on_ko_(txt_rgnr, errmsg_severe2errmsg_severe_pair__or__postprocess6errmsg_, _may_imay_num_args4postprocess6errmsg_=None, /):
        if _may_imay_num_args4postprocess6errmsg_ is None:
            errmsg_severe2errmsg_severe_pair_ = errmsg_severe2errmsg_severe_pair__or__postprocess6errmsg_
            return TextRecognizer__postprocess6ko(txt_rgnr, errmsg_severe2errmsg_severe_pair_)
        _imay_num_args4postprocess6errmsg_ = _may_imay_num_args4postprocess6errmsg_
        _postprocess6errmsg_ = errmsg_severe2errmsg_severe_pair__or__postprocess6errmsg_

        return TextRecognizer__postprocess6errmsg(txt_rgnr, _imay_num_args4postprocess6errmsg_, _postprocess6errmsg_)
        #.def on_ko_(txt_rgnr, errmsg_severe2errmsg_severe_pair_, /):
        #.    #def on_fail_(txt_rgnr, errmsg2errmsg_, /):
        #.    '[errmsg_severe2errmsg_severe_pair_ :: errmsg -> severe -> (errmsg, severe)]'
        #.    return TextRecognizer__postprocess6ko(txt_rgnr, errmsg_severe2errmsg_severe_pair_)
    def on_errmsg6ko_(txt_rgnr, _imay_num_args4postprocess6errmsg_, _postprocess6errmsg_, /):
        return TextRecognizer__postprocess6errmsg(txt_rgnr, _imay_num_args4postprocess6errmsg_, _postprocess6errmsg_)
    def named_(txt_rgnr, name, /, *, global_vs_local=False, to_tag=False):
        if to_tag:
            txt_rgnr = txt_rgnr.then_tag_(name)
        return TextRecognizer__named(global_vs_local, name, txt_rgnr)
    #__mod__ = named_
    def tagnamed_(txt_rgnr, name, /, *, global_vs_local=False, to_tag=True):
        return txt_rgnr.named_(name, global_vs_local=global_vs_local, to_tag=to_tag)
    ##################
    def fullmatched_(txt_rgnr, /):
        return TextRecognizer__fullmatched(txt_rgnr) if not type(txt_rgnr) is TextRecognizer__fullmatched else txt_rgnr
    def inside_(txt_rgnr, txt_rgnr7span, /, *, no_seekback=False):
        return TextRecognizer__inside(txt_rgnr7span, txt_rgnr, no_seekback)
    def insideR_(txt_rgnr, regex_or_pattern, xgroup, /, *, no_seekback=False):
        txt_rgnr7span = mk_txt_rgnr__span6regex_(regex_or_pattern, xgroup)
        return txt_rgnr.inside_(txt_rgnr7span, no_seekback=no_seekback)
    def insideV_(txt_rgnr, may_txt_rgnr7begin, may_txt_rgnr7end, /, *, backward=False, no_seekback=False):
        txt_rgnr7span = mk_txt_rgnr__span_(may_txt_rgnr7begin, may_txt_rgnr7end, backward=backward)
        return txt_rgnr.inside_(txt_rgnr7span, no_seekback=no_seekback)
    def span_(txt_rgnr, may_txt_rgnr7end, /, *, backward=False):
        return mk_txt_rgnr__span_(may_txt_rgnr7begin:=txt_rgnr, may_txt_rgnr7end, backward=backward)
    def spanB_(txt_rgnr, may_txt_rgnr7begin, /, *, backward=True):
        return mk_txt_rgnr__span_(may_txt_rgnr7begin, may_txt_rgnr7end:=txt_rgnr, backward=backward)
    ##################
    def repr_as_(txt_rgnr, name_or_named_obj, /, *args4repr, **kwds4repr):
        return TextRecognizer__repr(txt_rgnr, name_or_named_obj, *args4repr, **kwds4repr)
    ##################
    def then_unbox_(txt_rgnr, /):
        'see:enclosed_by_'
        return TextRecognizer__unbox(txt_rgnr)
    def then_getitem_(txt_rgnr, k, /):
        return TextRecognizer__getitem(txt_rgnr, k)
    def then_box_(txt_rgnr, /):
        'see:then_.kw:cased'
        return TextRecognizer__box(txt_rgnr)
    def then_to_tuple_(txt_rgnr, /):
        return TextRecognizer__to_tuple(txt_rgnr) if not type(txt_rgnr) is TextRecognizer__to_tuple else txt_rgnr
    def then_to_finger_tree_seq_(txt_rgnr, /):
        return TextRecognizer__to_finger_tree_seq(txt_rgnr) if not type(txt_rgnr) is TextRecognizer__to_finger_tree_seq else txt_rgnr
    def then_tag_(txt_rgnr, tag, /):
        #++TextRecognizer__tag
        return mk_tagged_txt_rgnr_(tag, txt_rgnr)
    def then_(txt_rgnr, /, *txt_rgnr_seq, cased=False):
        return mk_txt_rgnr__serial_((txt_rgnr, *txt_rgnr_seq), cased=cased)
    ##################
    def else_trial_(txt_rgnr, /):
        return TextRecognizer__trial(txt_rgnr) if not type(txt_rgnr) is TextRecognizer__trial else txt_rgnr
    def else_(txt_rgnr, /, *txt_rgnr_seq):
        return TextRecognizer__fallback((txt_rgnr, *txt_rgnr_seq))
    ##################
    def enclosed_by_(txt_rgnr, txt_or_txt_rgnr7open, txt_or_txt_rgnr7close, /, *, as_regex=False):
        # -->at[1] #unbox
        return TextRecognizer__enclosed(txt_rgnr5or_txt_(txt_or_txt_rgnr7open, as_regex=as_regex), txt_rgnr7content:=txt_rgnr, txt_rgnr5or_txt_(txt_or_txt_rgnr7close, as_regex=as_regex))
    def sep_end_by_(txt_rgnr, txt_rgnr7sep, txt_rgnr7end, min_repeat=0, may_max_repeat=None, /, *, cased=False):
        txt_rgnr7item = txt_rgnr
        #bug:may_txt_rgnr7sep_item = txt_rgnr7sep_item = mk_txt_rgnr__serial_([txt_rgnr7sep, txt_rgnr7item], cased=cased)
        may_txt_rgnr7sep_item = txt_rgnr7sep_item = mk_txt_rgnr7sep_item_(cased, txt_rgnr7sep, txt_rgnr7item)
        return mk_txt_rgnr__sep_end_by_(min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item, txt_rgnr7end, cased=cased)
    def sep_by_(txt_rgnr, txt_rgnr7sep, min_repeat=0, may_max_repeat=None, /, *, cased=False):
        txt_rgnr7item = txt_rgnr
        may_txt_rgnr7sep_item = txt_rgnr7sep_item = mk_txt_rgnr7sep_item_(cased, txt_rgnr7sep, txt_rgnr7item)
        return mk_txt_rgnr__sep_by_(min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item, cased=cased)
    def end_by_(txt_rgnr, txt_rgnr7end, min_repeat=0, may_max_repeat=None, /, *, cased=False):
        txt_rgnr7item = txt_rgnr
        return mk_txt_rgnr__end_by_(min_repeat, may_max_repeat, txt_rgnr7item, txt_rgnr7end, cased=cased)
    def many_(txt_rgnr, min_repeat=0, may_max_repeat=None, /, *, cased=False):
        txt_rgnr7item = txt_rgnr
        return mk_txt_rgnr__many_(min_repeat, may_max_repeat, txt_rgnr7item, cased=cased)
    def many0_(txt_rgnr, may_max_repeat=None, /, *, cased=False):
        return txt_rgnr.many_(0, may_max_repeat, cased=cased)
    def many1_(txt_rgnr, may_max_repeat=None, /, *, cased=False):
        return txt_rgnr.many_(1, may_max_repeat, cased=cased)
    def optional_(txt_rgnr, /, *, cased=False):
        #def mk_txt_rgnr__optional_(txt_rgnr, /):
        #def mk_txt_rgnr__tmay_(txt_rgnr, /):
        return txt_rgnr.many_(0, 1, cased=cased)
    ##################
    #for:kw:cased:suboresult_is_cased
    #   [tag:=ignore_vs_echo_vs_unpack :: uint%3]
    def tag7ignore_(txt_rgnr, /):
        return txt_rgnr.then_tag_(0)
    def tag7echo_(txt_rgnr, /):
        return txt_rgnr.then_tag_(1)
    def tag7unpack_(txt_rgnr, /):
        return txt_rgnr.then_tag_(2)
    __neg__ = tag7ignore_
    __pos__ = tag7echo_
    __invert__ = tag7unpack_
    __matmul__ = then_tag_
    ##################
#
#
    r'''[[[
    other_mkrs:
,   mk_tagged_txt_rgnr_fallback_
,   mk_ignorable_txt_rgnr_serial_
#
,   TextRecognizer__constant_oresult
,   TextRecognizer__constant_errmsg
,   TextRecognizer__constant_text
,   TextRecognizer__regex

    ]]]'''#'''
class span5re_matchT_:
    def __init__(sf, xgroup, method=None, /):
        check_type_in((int, str), xgroup)
        case4method = _case5method4span6regex_(method)
        sf._xg = xgroup
        sf._cm = case4method
    def __repr__(sf, /):
        case4method = sf._cm
        if not case4method == 2:
            return repr_helper(sf, sf._xg, case4method)
        return repr_helper(sf, sf._xg)
    def __call__(sf, m, /):
        xgroup = sf._xg
        case4method = sf._cm
        match case4method:
            case 2:
                return m.span(xgroup)
            case 1:
                return m.end(xgroup)
            case 0:
                return m.start(xgroup)
        raise 000
def mk_txt_rgnr__span_(may_txt_rgnr7begin, may_txt_rgnr7end, /, *, backward=False):
    txt_rgnr7span = TextRecognizer__span(may_txt_rgnr7begin, may_txt_rgnr7end, backward)
    return txt_rgnr7span
def mk_txt_rgnr__span6regex_(regex_or_pattern, xgroup, /, *, method=None):
    return TextRecognizer__span6regex(regex_or_pattern, xgroup, method)
def _case5method4span6regex_(method, /):
    match method:
        case None | 2 | 'span':
            case4method = 2
        case 1 | 'end':
            case4method = 1
        case 0 | 'start':
            case4method = 0
        case _:
            raise TypeError(method)
        #case
    return case4method
def _ex_mk_txt_rgnr__span6regex_(regex_or_pattern, xgroup, method=None, /):
    '#method:(2/span|0/start|1/end)'
    rgx = mk_regex5or_pattern_(regex_or_pattern)
    check_xgroup_(rgx, xgroup)
    case4method = _case5method4span6regex_(method)
    txt_rgnr = mk_txt_rgnr__regex_(rgx, None).on_ok_(span5re_matchT_(xgroup, case4method))
    return (rgx, case4method, txt_rgnr)

def mk_txt_rgnr__regex_(regex, may_group_or_groups, /, *, as_regex=True):
    #.return TextRecognizer__regex(regex)
    return mk_txt_rgnr__text_(regex, may_group_or_groups, as_regex=as_regex)
def mk_txt_rgnr__text_(text, may_group_or_groups=None, /, *, as_regex=False):
    if as_regex:
        regex = text
        return TextRecognizer__regex(regex, may_group_or_groups)
    if not None is may_group_or_groups: raise TypeError
    return TextRecognizer__constant_text(text)
def mk_txt_rgnr__oresult_(oresult, /):
    return TextRecognizer__constant_oresult(oresult)
def mk_txt_rgnr__errmsg_(errmsg, severe=False, /):
    return TextRecognizer__constant_errmsg(errmsg, severe)
def mk_txt_rgnr__serial_(txt_rgnrs, /, *, cased=False):
    'cased:suboresult_is_cased'
    return (TextRecognizer__serial__cased if cased else TextRecognizer__serial)(txt_rgnrs)
def mk_txt_rgnr__sep_end_by_(min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item, txt_rgnr7end, /, *, cased=False):
    'cased:suboresult_is_cased'
    return (TextRecognizer__sep_end_by__cased if cased else TextRecognizer__sep_end_by)(min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item, txt_rgnr7end)
def mk_txt_rgnr__sep_by_(min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item, /, *, cased=False):
    'cased:suboresult_is_cased'
    return (TextRecognizer__sep_by__cased if cased else TextRecognizer__sep_by)(min_repeat, may_max_repeat, txt_rgnr7item, may_txt_rgnr7sep_item)
def mk_txt_rgnr__end_by_(min_repeat, may_max_repeat, txt_rgnr7item, txt_rgnr7end, /, *, cased=False):
    'cased:suboresult_is_cased'
    return (TextRecognizer__end_by__cased if cased else TextRecognizer__end_by)(min_repeat, may_max_repeat, txt_rgnr7item, txt_rgnr7end)
def mk_txt_rgnr__many_(min_repeat, may_max_repeat, txt_rgnr7item, /, *, cased=False):
    'cased:suboresult_is_cased'
    return (TextRecognizer__many__cased if cased else TextRecognizer__many)(min_repeat, may_max_repeat, txt_rgnr7item)


def txt_rgnr5or_regex_(regex_or_txt_rgnr, /):
    global txt_rgnr5or_regex_
    import re
    assert 'Pattern' in re.__all__
    from re import Pattern
    def txt_rgnr5or_regex_(regex_or_txt_rgnr, /):
        match regex_or_txt_rgnr:
            case str(regex) | Pattern(regex):
                txt_rgnr = TextRecognizer__regex(regex, None)
            #.case ITextRecognizer(txt_rgnr):
            #.    txt_rgnr
            case ITextRecognizer():
                txt_rgnr = regex_or_txt_rgnr
            case _:
                raise TypeError(type(regex_or_txt_rgnr))
            #
        return txt_rgnr
    return txt_rgnr5or_regex_(regex_or_txt_rgnr)

def txt_rgnr5or_txt_(txt_or_txt_rgnr, /, *, as_regex=False):
    if as_regex:
        regex_or_txt_rgnr = txt_or_txt_rgnr
        return txt_rgnr5or_regex_(regex_or_txt_rgnr)
    match txt_or_txt_rgnr:
        case str(txt):
            txt_rgnr = TextRecognizer__constant_text(txt)
        #.case ITextRecognizer(txt_rgnr):
        #.    txt_rgnr
        case ITextRecognizer():
            txt_rgnr = txt_or_txt_rgnr
        case _:
            raise TypeError(type(txt_or_txt_rgnr))
        #
    return txt_rgnr
def mk_txt_rgnr7sep_item_(cased, txt_rgnr7sep, txt_rgnr7item, /):
    txt_rgnr7sep_item = mk_txt_rgnr__serial_([txt_rgnr7sep, txt_rgnr7item], cased=cased)
    if cased:
        txt_rgnr7sep_item = txt_rgnr7sep_item.tag7unpack_()
    return txt_rgnr7sep_item
#end-class _BaseTextRecognizer__ops4mkr:
class ITextRecognizer(_BaseTextRecognizer__ops4mkr, ABC):
    __slots__ = ()
    @abstractmethod
    def _parse_text_(sf, env, txt, begin, end, /):
        'env -> txt/str -> begin/uint%(1+len(txt)) -> end/uint%(1+len(txt)) -> GI4parse{return-(Either GI4parse (OResult|Errmsg));yield-GI4arbitrary{return-(Either GI4arbitrary arbitrary);yield-GI4arbitrary}}'

def check_parse_result_(eresult, /):
    check_type_in(ParseResult, eresult)
def check_parse_result__between_(begin, end, eresult, /):
    check_parse_result_(eresult)
    check_int_ge_le(begin, end, eresult.end)
def parse_text_(txt_rgnr, env, txt, begin, end, /, *, fullmatched=False, to_raise_if_fail=False):
    'ITextRecognizer -> env -> txt/str -> begin/uint%(1+len(txt)) -> end/uint%(1+len(txt)) -> (eresult/ParseResult/(OResult|Errmsg) if not to_raise_if_fail else (((oresult, end) if not fullmatched else oresult)) if eresult.ok else ^ParseFail(eresult, prefix4remain_txt))'
    check_type_is(bool, to_raise_if_fail)
    check_type_is(bool, fullmatched)
    check_type_is(str, txt)
    check_int_ge(0, begin)
    check_int_ge_le(begin, len(txt), end)
    if fullmatched:
        txt_rgnr = txt_rgnr.fullmatched_()
    eresult = flatten_recur(txt_rgnr._parse_text_(env, txt, begin, end), boxed=True)
    check_parse_result__between_(begin, end, eresult)
    if to_raise_if_fail:
        match eresult:
            case OResult(oresult=oresult, end=end):
                pass
            case Errmsg():
                prefix4remain_txt = txt[eresult.end:min(eresult.end+200, end)]
                raise ParseFail(eresult, prefix4remain_txt)
            case _:
                raise 000
            #case
        return (oresult, end) if not fullmatched else oresult
    return eresult
def parse_text7full_(txt_rgnr, env, txt, begin, end, /, *, fullmatched=True, to_raise_if_fail=False):
    return parse_text_(txt_rgnr, env, txt, begin, end, fullmatched=fullmatched, to_raise_if_fail=to_raise_if_fail)
def parse_text7raise_(txt_rgnr, env, txt, begin, end, /, *, fullmatched=False, to_raise_if_fail=True):
    return parse_text_(txt_rgnr, env, txt, begin, end, fullmatched=fullmatched, to_raise_if_fail=to_raise_if_fail)
def parse_text7exact_(txt_rgnr, env, txt, begin, end, /, *, fullmatched=True, to_raise_if_fail=True):
    return parse_text_(txt_rgnr, env, txt, begin, end, fullmatched=fullmatched, to_raise_if_fail=to_raise_if_fail)
if 0:
    'from:view ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare.py'
    def _parse7full_(parse_text_, s, /):
        parse_result = parse_text_(s, 0, len(s))
        #match parse_result:
        if not parse_result.ok:
            raise Exception(parse_result, s[parse_result.end:])
        if not parse_result.end == len(s):
            raise Exception(parse_result, len(s)-parse_result.end, s[parse_result.end:])
        return parse_result.oresult




















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
                raise TypeError(sf, cased_oresult7child)
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
        if not b is ops4oresult_seq__cased._whether_child_oresult_cased_:raise TypeError(env, sf)
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
                case bad_next_step_info:
                    raise TypeError(bad_next_step_info, sf)
                #case
            txt_rgnr
            eresult7child = yield txt_rgnr._parse_text_(env, txt, _begin, end)
            match eresult7child:
                case OResult(oresult=oresult7child, end=_begin):
                    rs = sf._iput4oresult_seq_(rs, oresult7child)
                case Errmsg():
                    pass
                case _:
                    raise TypeError(type(eresult7child), txt_rgnr)
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























class ITextRecognizer__postprocess6ko(ITextRecognizer):
    #see:TextRecognizer__trial
    #see:ITextRecognizer__postprocess6errmsg
    __slots__ = ()
    @property
    @abstractmethod
    def _txt_rgnr_(sf, /):
        '-> ITextRecognizer'
    @abstractmethod
    def _postprocess6ko_(sf, errmsg, severe, /):
        'errmsg -> severe -> (errmsg, severe)'
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        txt_rgnr = sf._txt_rgnr_
        eresult = yield txt_rgnr._parse_text_(env, txt, begin, end)
        match eresult:
            case OResult():
                pass
            case Errmsg(errmsg=errmsg, severe=severe):
                (_errmsg, _severe) = sf._postprocess6ko_(errmsg, severe)
                if not (_errmsg is errmsg and _severe is severe):
                    eresult = eresult._replace(errmsg=_errmsg, severe=_severe)
                eresult
            case _:
                raise 000
            #case
        return mk_Right(eresult)
class ITextRecognizer__postprocess6errmsg(ITextRecognizer__postprocess6ko):
    __slots__ = ()
    @property
    @abstractmethod
    def _imay_num_args4postprocess6errmsg_(sf, /):
        '-> imay uint%3'
    @property
    @abstractmethod
    def _postprocess6errmsg_(sf, /):
        '-> (case _imay_num_args4postprocess6errmsg_ of {-1:errmsg; 0:(() -> errmsg); 1:(errmsg -> errmsg); 2:(errmsg -> severe -> errmsg);})'
    @override
    def _postprocess6ko_(sf, errmsg, severe, /):
        xf = sf._postprocess6errmsg_
        match sf._imay_num_args4postprocess6errmsg_:
            case 2:
                errmsg_severe2errmsg_ = xf
                _errmsg = errmsg_severe2errmsg_(errmsg, severe)
            case 1:
                errmsg2errmsg_ = xf
                _errmsg = errmsg2errmsg_(errmsg)
            case 0:
                lazy_errmsg_ = xf
                _errmsg = lazy_errmsg_()
            case -1:
                _errmsg = xf
            case bad:
                raise TypeError('not in [-1..=2]:', bad, sf)
            #
        return (_errmsg, severe)


class ITextRecognizer__postprocess(ITextRecognizer):
    __slots__ = ()
    @property
    @abstractmethod
    def _txt_rgnr_(sf, /):
        '-> ITextRecognizer'
    @property
    @abstractmethod
    def _imay_num_args4postprocess_(sf, /):
        '-> imay uint%7'
    @property
    @abstractmethod
    def _postprocess_(sf, /):
        '-> callable # mk_default(sf._imay_num_args4postprocess_, sf._postprocess_, sf._txt_rgnr_, env, txt, begin, end, eresult)'
        '-> (sf -> txt -> begin -> end -> eresult -> eresult)'
    #.@abstractmethod
    #.def _postprocess_(sf, _txt_rgnr_, env, txt, begin, end, eresult, /):
    #.    'sf -> txt -> begin -> end -> eresult -> eresult'
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        txt_rgnr = sf._txt_rgnr_
        eresult = yield txt_rgnr._parse_text_(env, txt, begin, end)
        _eresult = mk_default(sf._imay_num_args4postprocess_, sf._postprocess_, txt_rgnr, env, txt, begin, end, eresult)
        if not _eresult is eresult:
            check_parse_result__between_(begin, end, _eresult)
        return mk_Right(_eresult)

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
class ITextRecognizer__postprocess6oresult(ITextRecognizer__postprocess6ok):
    __slots__ = ()
    @property
    @abstractmethod
    def _imay_num_args4postprocess6oresult_(sf, /):
        '-> imay uint%2'
    @property
    @abstractmethod
    def _postprocess6oresult_(sf, /):
        '-> (case _imay_num_args4postprocess6oresult_ of {-1:oresult; 0:(() -> oresult); 1:(oresult -> oresult);})'
    @override
    def _postprocess6ok_(sf, oresult, /):
        xf = sf._postprocess6oresult_
        match sf._imay_num_args4postprocess6oresult_:
            case 1:
                oresult2oresult_ = xf
                _oresult = oresult2oresult_(oresult)
            case 0:
                lazy_oresult_ = xf
                _oresult = lazy_oresult_()
            case -1:
                _oresult = xf
            case bad:
                raise TypeError('not in [-1..=1]:', bad, sf)
            #
        return _oresult



class TextRecognizer__inside(ITextRecognizer):
    'see:mk_txt_rgnr__span6regex_, mk_txt_rgnr__span_ #inside_'
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnr7span, txt_rgnr7oresult, no_seekback=False, /):
        check_type_is(bool, no_seekback)
        check_type_le(ITextRecognizer, txt_rgnr7span)
        check_type_le(ITextRecognizer, txt_rgnr7oresult)
        sf._rgnr7span = txt_rgnr7span
        sf._rgnr7oresult = txt_rgnr7oresult
        sf._nsb = no_seekback
    @property
    def _no_seekback_(sf, /):
        '-> bool'
        return sf._nsb
    @property
    def _txt_rgnr7span_(sf, /):
        '-> ITextRecognizer'
        return sf._rgnr7span
    @property
    def _txt_rgnr7oresult_(sf, /):
        '-> ITextRecognizer'
        return sf._rgnr7oresult
    def __repr__(sf, /):
        if sf._no_seekback_:
            return repr_helper(sf, sf._txt_rgnr7span_, sf._txt_rgnr7oresult_, sf._no_seekback_)
        return repr_helper(sf, sf._txt_rgnr7span_, sf._txt_rgnr7oresult_)
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        no_seekback = sf._no_seekback_
        txt_rgnr7span = sf._txt_rgnr7span_
        txt_rgnr7oresult = sf._txt_rgnr7oresult_
        eresult = yield txt_rgnr7span._parse_text_(env, txt, begin, end)
        if not eresult.ok:
            return mk_Right(eresult)
        (_begin, _end) = span = eresult.oresult
        if not begin <= _begin <= _end <= end:raise TypeError((begin, end), (_begin, _end))
        gi = txt_rgnr7oresult._parse_text_(env, txt, _begin, _end)
        if not no_seekback:
            #seekback
            return mk_Left(gi)
        #no_seekback
        _eresult = yield gi
        if not _eresult.end == eresult.end:
            _eresult = _eresult._replace(end=eresult.end)
        return mk_Right(_eresult)

class TextRecognizer__span(ITextRecognizer):
    'see:TextRecognizer__inside; mk_txt_rgnr__span_,mk_txt_rgnr__span6regex_'
    ___no_slots_ok___ = True
    def __init__(sf, may_txt_rgnr7begin, may_txt_rgnr7end, backward=False, /):
        check_type_is(bool, backward)
        check_may_([check_type_le, ITextRecognizer], may_txt_rgnr7begin)
        check_may_([check_type_le, ITextRecognizer], may_txt_rgnr7end)
        sf._bw = backward
        sf._mrgnr7begin = may_txt_rgnr7begin
        sf._mrgnr7end = may_txt_rgnr7end
    @property
    def _backward_(sf, /):
        '-> bool'
        return sf._bw
    @property
    def _may_txt_rgnr7begin_(sf, /):
        '-> may ITextRecognizer'
        return sf._mrgnr7begin
    @property
    def _may_txt_rgnr7end_(sf, /):
        '-> may ITextRecognizer'
        return sf._mrgnr7end
    def __repr__(sf, /):
        if sf._backward_:
            return repr_helper(sf, sf._may_txt_rgnr7begin_, sf._may_txt_rgnr7end_, sf._backward_)
        return repr_helper(sf, sf._may_txt_rgnr7begin_, sf._may_txt_rgnr7end_)
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        backward = sf._backward_
        may_txt_rgnr7begin = sf._may_txt_rgnr7begin_
        may_txt_rgnr7end = sf._may_txt_rgnr7end_
        x = yield from (_4backward if backward else _4forward)(env, txt, begin, end, may_txt_rgnr7begin, may_txt_rgnr7end)
        if x.is_right:
            return x
        (span, _tend) = x.left

        eresult = OResult(oresult:=span, end=_tend)#no-seekback
        return mk_Right(eresult)
        #.eresult = eresult._replace(oresult=oresult)#no-seekback
        #.return mk_Right(eresult)
        #eresult = OResult(oresult, end=begin)#seekback
        #eresult = OResult(oresult, end=eresult.end)#no-seekback

def _gparse4idx7default(default, may_txt_rgnr, env, txt, begin, end, /):
    if not None is (txt_rgnr:=may_txt_rgnr):
        eresult = yield txt_rgnr._parse_text_(env, txt, begin, end)
        if not eresult.ok:
            return mk_Right(eresult)
        j = eresult.oresult
        _tend = eresult.end
    else:
        j = default
        _tend = j #end #?begin?
    j
    if not begin <= j <= _tend <= end:raise TypeError((begin, end), j, _tend)
    #return mk_Left(j)
    return mk_Left((j, _tend))
def _4forward(env, txt, begin, end, may_txt_rgnr7begin, may_txt_rgnr7end, /):
    ##################
    x = yield from _gparse4idx7default(default:=begin, may_txt_rgnr7begin, env, txt, begin, end)
    if x.is_right:
        return x
    #_begin = x.left
    (_begin, _tend) = x.left

    ##################
    x = yield from _gparse4idx7default(default:=end, may_txt_rgnr7end, env, txt, _tend, end)
    if x.is_right:
        return x
    #_end = x.left
    (_end, _tend) = x.left

    ##################
    span = (_begin, _end)
    return mk_Left((span, _tend))
def _4backward(env, txt, begin, end, may_txt_rgnr7begin, may_txt_rgnr7end, /):
    ##################
    x = yield from _gparse4idx7default(default:=end, may_txt_rgnr7end, env, txt, begin, end)
    if x.is_right:
        return x
    #_end = x.left
    (_end, _tend) = x.left

    ##################
    x = yield from _gparse4idx7default(default:=begin, may_txt_rgnr7begin, env, txt, begin, _end)
    if x.is_right:
        return x
    #_begin = x.left
    (_begin, _000tend) = x.left

    ##################
    span = (_begin, _end)
    return mk_Left((span, _tend))







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

class TextRecognizer__fullmatched(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess):
    'see:TextRecognizer__inside; parse_text7full_, parse_text7exact_#.fullmatched_'
    #@override
    _imay_num_args4postprocess_ = 4
    @override
    def _postprocess_(sf, txt, begin, end, eresult, /):
        if eresult.ok and not eresult.end == end:
            #from:_parse7full_()
            errmsg = (eresult, sz:=end-eresult.end, txt[eresult.end:min(eresult.end+200, end)])
            _eresult = Errmsg(errmsg, eresult.end, severe=False)
        else:
            _eresult = eresult
        return _eresult

class TextRecognizer__unbox(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6ok):
    'see:TextRecognizer__enclosed'
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
    'see:TextRecognizer__serial__cased'
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
class TextRecognizer__postprocess6ko(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6ko):
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnr, _postprocess6ko_, /):
        _ITextRecognizer__init__wrapped_txt_rgnr.__init__(sf, txt_rgnr)
        check_callable(_postprocess6ko_)
        sf._pf6ko = _postprocess6ko_
    @override
    def _postprocess6ko_(sf, errmsg, severe, /):
        return sf._pf6ko(errmsg, severe)
    def __repr__(sf, /):
        return repr_helper(sf, sf._txt_rgnr_, sf._pf6ko)
class TextRecognizer__postprocess6errmsg(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6errmsg):
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnr, _imay_num_args4postprocess6errmsg_, _postprocess6errmsg_, /):
        _ITextRecognizer__init__wrapped_txt_rgnr.__init__(sf, txt_rgnr)
        check_int_ge_le(-1, 2, _imay_num_args4postprocess6errmsg_)
        if not _imay_num_args4postprocess6errmsg_ == -1:check_callable(_postprocess6errmsg_)
        sf._imay4pf6errmsg = _imay_num_args4postprocess6errmsg_
        sf._pf6errmsg = _postprocess6errmsg_
    @property
    @override
    def _imay_num_args4postprocess6errmsg_(sf, /):
        return sf._imay4pf6errmsg
    @property
    @override
    def _postprocess6errmsg_(sf, /):
        return sf._pf6errmsg
    def __repr__(sf, /):
        return repr_helper(sf, sf._txt_rgnr_, sf._imay4pf6errmsg, sf._pf6errmsg)
class TextRecognizer__named(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6errmsg):
    r'''[[[
    ++@20260322

    main intent:
        + simplify repr() output
        + locate errmsg

    global_vs_local:
        * global_name:
            unique to be referred via env
        * local_name:
            eg:
                idx4child{serial}
                attr4child{serial}
                idx4branch{fallback}
                tag4branch{fallback}
    ]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, global_vs_local, name, txt_rgnr, /):
        check_type_is(bool, global_vs_local)
        hash(name)
        _ITextRecognizer__init__wrapped_txt_rgnr.__init__(sf, txt_rgnr)
        sf._nm = name
        sf._gl = global_vs_local
    @property
    def global_vs_local(sf, /):
        return sf._gl
    @property
    def name(sf, /):
        return sf._nm
    #@override
    _imay_num_args4postprocess6errmsg_ = 1
    @override
    def _postprocess6errmsg_(sf, errmsg, /):
        errmsg = (sf.global_vs_local, sf.name, errmsg)
        return errmsg
    def __repr__(sf, /):
        from seed.helper.ConstantRepr import repr_as_3dot #ConstantRepr
        return repr_helper(sf, sf.global_vs_local, sf.name, repr_as_3dot)
    def __str__(sf, /):
        return repr_helper(sf, sf.global_vs_local, sf.name, sf._txt_rgnr_)

class TextRecognizer__postprocess6oresult(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6oresult):
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnr, _imay_num_args4postprocess6oresult_, _postprocess6oresult_, /):
        _ITextRecognizer__init__wrapped_txt_rgnr.__init__(sf, txt_rgnr)
        check_int_ge_le(-1, 1, _imay_num_args4postprocess6oresult_)
        if not _imay_num_args4postprocess6oresult_ == -1:check_callable(_postprocess6oresult_)
        sf._imay4pf6oresult = _imay_num_args4postprocess6oresult_
        sf._pf6oresult = _postprocess6oresult_
    @property
    @override
    def _imay_num_args4postprocess6oresult_(sf, /):
        return sf._imay4pf6oresult
    @property
    @override
    def _postprocess6oresult_(sf, /):
        return sf._pf6oresult
    def __repr__(sf, /):
        return repr_helper(sf, sf._txt_rgnr_, sf._imay4pf6oresult, sf._pf6oresult)

class TextRecognizer__tag(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6oresult):
    #++@20260322
    # !! env4ops4oresult_seq__ftSeq
    # !! force:oresult be pair
    ___no_slots_ok___ = True
    def __init__(sf, tag, txt_rgnr, /):
        _ITextRecognizer__init__wrapped_txt_rgnr.__init__(sf, txt_rgnr)
        sf._tag = tag
    @property
    def tag(sf, /):
        return sf._tag
    #@override
    _imay_num_args4postprocess6oresult_ = 1
    @override
    def _postprocess6oresult_(sf, oresult, /):
        oresult = (sf.tag, oresult)
        return oresult
    def __repr__(sf, /):
        return repr_helper(sf, sf.tag, sf._txt_rgnr_)





#.class TextRecognizer__trial(_ITextRecognizer__init__wrapped_txt_rgnr):
#.    ___no_slots_ok___ = True
#.    @override
#.    def _parse_text_(sf, env, txt, begin, end, /):
#.        txt_rgnr = sf._txt_rgnr_
#.        eresult = yield txt_rgnr._parse_text_(env, txt, begin, end)
#.        match eresult:
#.            case OResult():
#.                pass
#.            case Errmsg(severe=_severe):
#.                if _severe:
#.                    eresult = eresult._replace(severe=False)
#.                pass
#.            case _:
#.                raise 000
#.            #case
#.        return mk_Right(eresult)
class TextRecognizer__trial(_ITextRecognizer__init__wrapped_txt_rgnr, ITextRecognizer__postprocess6ko):
    ___no_slots_ok___ = True
    @override
    def _postprocess6ko_(sf, errmsg, severe, /):
        return (errmsg, False)





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


def check_xgroup_(rgx, xgroup, /):
    match xgroup:
        case int(idx4group):
            num_groups = rgx.groups
            check_int_ge_le(0, num_groups, idx4group)
                # [0]++[1..=num_groups]
        case str(nm4group):
            nm2idx = rgx.groupindex
            if not nm4group in nm2idx:raise TypeError(nm2idx, nm4group, rgx)
        case _:
            raise TypeError(xgroup, rgx)

def check_may_group_or_groups_(rgx, may_group_or_groups, /):
    match may_group_or_groups:
        case str('1..'):
            pass
        case None:
            pass
        case int(idx4group):
            num_groups = rgx.groups
            check_int_ge_le(0, num_groups, idx4group)
                # [0]++[1..=num_groups]
        case str(nm4group):
            nm2idx = rgx.groupindex
            if not nm4group in nm2idx:raise TypeError(nm2idx, nm4group, rgx)
        case tuple(groups):
            for may_group_or_groups in groups:
                check_may_group_or_groups_(rgx, may_group_or_groups)
        case _:
            raise TypeError(may_group_or_groups, rgx)
def xget_groups5re_match_(m, may_group_or_groups, /):
    match may_group_or_groups:
        case str('1..'):
            return m.groups() # except: group0
        case None:
            return m
        case int(idx4group):
            return m[idx4group]
        case str(nm4group):
            return m[nm4group]
        case tuple(groups):
            return tuple(xget_groups5re_match_(m, may_group_or_groups) for may_group_or_groups in groups)
        case _:
            raise TypeError(may_group_or_groups, type(may_group_or_groups), m, m.re)
    raise 000

class TextRecognizer__regex(ITextRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, regex_or_pattern, may_group_or_groups=None, /):
        rgx = mk_regex5or_pattern_(regex_or_pattern)
        check_may_group_or_groups_(rgx, may_group_or_groups)
        sf._rgx = rgx
        sf._ms = may_group_or_groups
    def __repr__(sf, /):
        if None is sf._may_group_or_groups_:
            return repr_helper(sf, sf._regex_)
        return repr_helper(sf, sf._regex_, sf._may_group_or_groups_)
    #.    return repr_helper(sf, sf._pattern_)
    #.@property
    #.def _pattern_(sf, /):
    #.    '-> pattern'
    #.    return sf._regex_.pattern
    @property
    def _regex_(sf, /):
        '-> regex'
        return sf._rgx
    @property
    def _may_group_or_groups_(sf, /):
        '-> may_group_or_groups'
        return sf._ms
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        regex = sf._regex_
        may_group_or_groups = sf._may_group_or_groups_
        m = regex.match(txt, begin, end)
        if not m:
            return mk_Right(Errmsg(errmsg=('unmatched:', regex), end=begin, severe=False))
        _end = m.end()
        #.txt7actual = m.group(0)
        #.oresult = txt7actual
        #.oresult = (txt7actual, m)
        oresult = xget_groups5re_match_(m, may_group_or_groups)
        return mk_Right(OResult(oresult=oresult, end=_end))
        777;yield



class TextRecognizer__span6regex(ITextRecognizer):
    'see:mk_txt_rgnr__span6regex_#method:(2/span|0/start|1/end)'
    ___no_slots_ok___ = True
    def __init__(sf, regex_or_pattern, xgroup, method=None, /):
        (rgx, case4method, txt_rgnr) = _ex_mk_txt_rgnr__span6regex_(regex_or_pattern, xgroup, method)
        sf._rgx = rgx
        sf._xg = xgroup
        sf._rgnr = txt_rgnr
        sf._cm = case4method
    def __repr__(sf, /):
        case4method = sf._cm
        if not case4method == 2:
            return repr_helper(sf, sf._regex_, sf._xgroup_, case4method)
        return repr_helper(sf, sf._regex_, sf._xgroup_)
    @property
    def _regex_(sf, /):
        '-> regex'
        return sf._rgx
    @property
    def _xgroup_(sf, /):
        '-> xgroup'
        return sf._xg
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        #.regex = sf._regex_
        #.xgroup = sf._xgroup_
        return sf._rgnr._parse_text_(env, txt, begin, end)


def name5or_named_obj_(name_or_named_obj, /):
    if type(name_or_named_obj) is str:
        name = name_or_named_obj
    else:
        named_obj = name_or_named_obj
        try:
            name = named_obj.__name__
        except AttributeError:
            name = type(named_obj).__name__
        #.    name = None
        #.if not type(name) is str or not name.isidentifier(): name = type(named_obj).__name__
    return name


class TextRecognizer__repr(ITextRecognizer):
    'see:_ex_mk_txt_rgnr__span6regex_ #.repr_as_'
    ___no_slots_ok___ = True
    def __init__(sf, txt_rgnr, name_or_named_obj, /, *args4repr, **kwds4repr):
        check_type_le(ITextRecognizer, txt_rgnr)
        name = name5or_named_obj_(name_or_named_obj)
        sf._rgnr = txt_rgnr
        sf._nmx = name_or_named_obj
        sf._args4repr = args4repr
        sf._kwds4repr = kwds4repr
        sf._nm = name
    def __str__(sf, /):
        txt_rgnr = sf._rgnr
        name_or_named_obj = sf._nmx
        args4repr = sf._args4repr
        kwds4repr = sf._kwds4repr
        return repr_helper(sf, txt_rgnr, name_or_named_obj, *args4repr, **kwds4repr)
    def __repr__(sf, /):
        txt_rgnr = sf._rgnr
        name = sf._nm
        args4repr = sf._args4repr
        kwds4repr = sf._kwds4repr
        return repr_helper__str(name, *args4repr, **kwds4repr)
    #.@property
    #.def _txt_rgnr_(sf, /):
    #.    return sf._rgnr
    @override
    def _parse_text_(sf, env, txt, begin, end, /):
        return sf._rgnr._parse_text_(env, txt, begin, end)

























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



#before@20260322
#   no:TextRecognizer__tag
#      impl-ver1:
#          from seed.types.Either import TagT
#          TextRecognizer__postprocess6ok(txt_rgnr, TagT(tag))
#      impl-ver2:
#          TextRecognizer__serial([TextRecognizer__constant_oresult(tag), txt_rgnr])
#
#@20260322:++TextRecognizer__tag
def mk_tagged_txt_rgnr_(tag, txt_rgnr, /):
    return TextRecognizer__tag(tag, txt_rgnr)
    return TextRecognizer__serial([TextRecognizer__constant_oresult(tag), txt_rgnr])
    from seed.types.Either import TagT
    return TextRecognizer__postprocess6ok(txt_rgnr, TagT(tag))
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





def __():
    for nm in dir(_BaseTextRecognizer__ops4mkr()):
        print(nm)
if __name__ == "__main__":
    __()

__all__
from seed.recognize.text_recognizer.ITextRecognizer import check_parse_result__between_, check_parse_result_
from seed.recognize.text_recognizer.ITextRecognizer import parse_text_, parse_text7full_, parse_text7raise_, parse_text7exact_, ParseFail, env4ops4oresult_seq__ftSeq, env4ops4oresult_seq__list
    #def parse_text_(txt_rgnr, env, txt, begin, end, /, *, fullmatched=False, to_raise_if_fail=False):
    #   'ITextRecognizer -> env -> txt/str -> begin/uint%(1+len(txt)) -> end/uint%(1+len(txt)) -> ParseResult/(OResult|Errmsg)'
    #   Errmsg(errmsg,end,severe){ok:=False}{ko:=True}
    #   OResult(oresult,end){ok:=True}{ko:=False}
from seed.recognize.text_recognizer.ITextRecognizer import (
#after:_BaseTextRecognizer__ops4mkr
#   other_mkrs:goto
ITextRecognizer
,mk_tagged_txt_rgnr_fallback_
,mk_ignorable_txt_rgnr_serial_
,mk_txt_rgnr__regex_#kw:as_regex
,mk_txt_rgnr__text_#kw:as_regex
,mk_txt_rgnr__oresult_
,mk_txt_rgnr__errmsg_
,mk_txt_rgnr__span_#kw:backward
,mk_txt_rgnr__span6regex_#kw:method
#_BaseTextRecognizer__ops4mkr::
#   .on_ok_
#   .on_ko_
#   .on_errmsg6ko_
#   .named_#kw:global_vs_local,to_tag
#   .tagnamed_#kw:global_vs_local,to_tag
#
#   .fullmatched_
#   .inside_#kw:no_seekback
#   .insideR_#kw:no_seekback
#   .insideV_#kw:backward,no_seekback
#   .span_#kw:backward
#   .spanB_#kw:backward
#   .repr_as_
#
#   .enclosed_by_#kw:as_regex
#   .end_by_#kw:cased
#   .many0_#kw:cased
#   .many1_#kw:cased
#   .many_#kw:cased
#   .optional_#kw:cased
#   .sep_by_#kw:cased
#   .sep_end_by_#kw:cased
#
#   #tag for kw:cased
#   .tag7echo_
#   .tag7ignore_
#   .tag7unpack_
#   .__neg__ = tag7ignore_
#   .__pos__ = tag7echo_
#   .__invert__ = tag7unpack_
#   .__matmul__ = then_tag_
#
#   .then_#kw:cased
#   .then_box_
#   .then_getitem_
#   .then_tag_
#   .then_to_finger_tree_seq_
#   .then_to_tuple_
#   .then_unbox_#see:enclosed_by_
#
#   .else_
#   .else_trial_
)
from seed.recognize.text_recognizer.ITextRecognizer import *
