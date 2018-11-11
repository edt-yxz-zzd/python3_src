
#filters__simplified_in_more_simplified
__all__ = '''
    Filters__simplified_in_more_simplified
    filter_name2func
    filter_ex_name2func
    '''.split()



from ..errors import ParseFailError
from .filters.to_unit import to_unit
from .filters.lnk2list import lnk2list
from .abstract_syntax_datatype import (
    Production
    ,OP3
    ,OP2
    ,FilteredRefName
    ,OP2_FilteredRefName
    ,OP3_FilteredRefName

    ,Discard
    ,Unit
    ,UnitUnpack
    ,Tuple
    ,TupleWithAlias

    ,collect_rhs_ref_symbol_names
    )



def remove_Nones(args):
    return [x for x in args if x is not None]

def to_list(args):
    return list(args)
def const_False(args):
    return False
def const_True(args):
    return True
def const_None(args):
    return None
#def const_neg1(args): return -1

def mk_multi_ref_name(args):
    ref_name, op_multi = args
    return ref_name+op_multi
def mk_user_ref_name(value):
    return value
def mk_kw_ref_name(value):
    return value

def mk_discard(args):
    filters0, def_name, DiscardBody = args
    ref_names0 = DiscardBody

    filter_names = filters0
    nonterminal_name = def_name
    filtered_ref_names = [FilteredRefName((), ref_name) for ref_name in ref_names0]
    #FilteredRefName(filter_names, ref_symbol_name)
    return Discard(filter_names, nonterminal_name, filtered_ref_names)

def mk_unit(args):
    filtered_def_name, UnitBody = args
    filter_names, nonterminal_name = filtered_def_name
    (filtered_ref_names_left
    ,filtered_ref_name
    ,filtered_ref_names_right
    ) = UnitBody
    return Unit(filter_names, nonterminal_name
                , filtered_ref_names_left
                , filtered_ref_name
                , filtered_ref_names_right
                )
def mk_unit_body_from_name(filtered_ref_name):
    return [], filtered_ref_name, []
def mk_unit_body_from_triple(args):
    _, _, _ = args
    return args
def mk_unit_unpack(args):
    filtered_def_name, UnitUnpackBody = args
    filter_names, nonterminal_name = filtered_def_name
    op3_filtered_ref_names = UnitUnpackBody
    return UnitUnpack(filter_names, nonterminal_name, op3_filtered_ref_names)
def mk_unit_unpack_body(args):
    (op2_filtered_ref_names0, filtered_ref_name, op3_filtered_ref_names0
    ) = args
    op3_filtered_ref_names = [
        OP3_FilteredRefName(mk_op3_from_op2(op2), filtered_ref_name)
        for op2, filtered_ref_name in op2_filtered_ref_names0
        ]
    op3_filtered_ref_names.append(
        OP3_FilteredRefName(OP3.OP_UNPACK, filtered_ref_name))
    op3_filtered_ref_names.extend(op3_filtered_ref_names0)
    return op3_filtered_ref_names
def mk_tuple(args):
    #mk tuple_production
    filtered_def_name, TupleBody = args
    may_op2_filtered_ref_names0 = TupleBody
    #may_op2_filtered_ref_name : +may_op2 +filtered_ref_name
    op2_filtered_ref_names = __mk_op2_filtered_ref_names(
        may_op2_filtered_ref_names0, 0, -1, filtered_def_name)
    filter_names, nonterminal_name = filtered_def_name
    return Tuple(filter_names, nonterminal_name, op2_filtered_ref_names)

def __mk_op2_filtered_ref_names(
    tuples, may_op2_idx, filtered_ref_name_idx, lhs_def_name
    ):
    may_op2__seq = [t[may_op2_idx] for t in tuples]
    may__op2_seq = may_op2__seq2may__op2_seq(may_op2__seq)
    if may__op2_seq is None:
        raise ParseFailError(f'tuple_production/tuple_with_alias_production error: 3 ops =([+-]|): {lhs_def_name} : {tuples}')

    op2_seq = may__op2_seq
    op2_filtered_ref_names = [
        OP2_FilteredRefName(op2, t[filtered_ref_name_idx])
        for op2, t in zip(op2_seq, tuples)
        ]
    return op2_filtered_ref_names


def may_op2__seq2may__op2_seq(may_op2_seq):
    # [(None|bool)] -> (None|[bool])
    may_op2_set = set(may_op2_seq)
    ALL = {None, False, True}
    if may_op2_set - ALL:
        raise logic-error
    if may_op2_set == ALL:
        return None # fail
    if True in may_op2_set:
        pos_op = True
    else:
        pos_op = None
    return [may_op2 is pos_op for may_op2 in may_op2_seq]


def mk_tuple_with_alias(args):
    filtered_ex_def_name, TupleWithAliasBody = args
    filters0, filter_ex, def_name = filtered_ex_def_name
    decorated_ref_names0 = TupleWithAliasBody
    #decorated_ref_name : +may_op2 +may_decorator +filtered_ref_name
    alias_name2idx = {}
    for i, (_, may_decorator, filtered_ref_name) in enumerate(decorated_ref_names0):
        if not may_decorator:pass
        [decorator] = may_decorator
        assert decorator and decorator[-1] == '@'
        decorator_name = decorator[:-1]
        if decorator_name == '~':
            decorator_name = filtered_ref_name.ref_symbol_name
        if decorator_name in alias_name2idx:
            raise ParseFailError(f'duplicate alias: {decorator_name!r} : {filtered_ex_def_name} : {decorated_ref_names0}')
        alias_name2idx[decorator_name] = i

    op2_filtered_ref_names = __mk_op2_filtered_ref_names(
        decorated_ref_names0, 0, -1, filtered_ex_def_name)
    filter_names, filter_ex_name, nonterminal_name = filtered_ex_def_name
    return TupleWithAlias(
                filter_names, filter_ex_name, nonterminal_name
                , op2_filtered_ref_names, alias_name2idx
                )

def mk_op3_filtered_ref_name(args):
    return OP3_FilteredRefName(*args)
def const_op3_unpack(args):
    return OP3.OP_UNPACK
def mk_op3_from_op2(op2):
    return OP3.OP_SELECT if op2 else OP3.OP_DISCARD
def mk_filtered_ref_name(args):
    return FilteredRefName(*args)
class Names:
    def __init__(self, names):
        self.names = set(names)
class TerminalSetNames(Names):pass
class StartNonterminalNames(Names):pass
class AmbiguousNonterminalNames(Names):pass
class MaybedeadNonterminalNames(Names):pass
mk_terminal_set_names = TerminalSetNames
mk_start_nonterminal_names = StartNonterminalNames
mk_ambiguous_nonterminal_names = AmbiguousNonterminalNames
mk_maybedead_nonterminal_names = MaybedeadNonterminalNames


def mk_main_result(ls):
    (productions
    , terminal_set_names
    , start_nonterminal_names
    , ambiguous_nonterminal_names
    , maybedead_nonterminal_names
    ) = r = mk_main_result1(ls)
    #return r
    productions = mk_main_result2__update_productions(productions)
    terminal_set_names = mk_main_result3__update_terminal_set_names(terminal_set_names)

    r = (productions
        , terminal_set_names
        , start_nonterminal_names
        , ambiguous_nonterminal_names
        , maybedead_nonterminal_names
        )
    return r


def mk_main_result3__update_terminal_set_names(terminal_set_names):
    # should update find_terminal_set_idc too!!!
    terminal_set_names = set(terminal_set_names)
    terminal_set_names.add('@none@')
    terminal_set_names.add('@any@')
    return terminal_set_names
def mk_main_result2__update_productions(productions):
    '''handle X+, X*, X?
auto generate productions for ?*+

; @@lnk2list@@$ X+ = @@multi_lnk<X+>@@
; @@lnk2list@@$ X* = @@multi_lnk<X*>@@
; @@lnk2list@@$ X? = @@multi_lnk<X?>@@

; @@multi_lnk<X?>@@ : X
; @@multi_lnk<X?>@@ :
; @@multi_lnk<X+>@@ : @@multi_lnk<X*>@@ X
; @@multi_lnk<X*>@@ = @@multi_lnk<X+>@@
; @@multi_lnk<X*>@@ :

'''
    ref_symbol_names = collect_rhs_ref_symbol_names(productions)
    ref_symbol_names =set(ref_symbol_names)

    ref_symbol_names_to_handle = set()
    def put(ref_symbol_name):
        while ref_symbol_name[-1] in '?*+':
            #assert ref_symbol_name
            if ref_symbol_name in ref_symbol_names_to_handle:
                continue
            ref_symbol_names_to_handle.add(ref_symbol_name)
            ref_symbol_name = ref_symbol_name[:-1]

    #usr_X2optional = {}
    #usr_X2plus = {}
    #usr_X2star = {}
    #usr_ref_symbol_names = set()
    for ref_symbol_name in ref_symbol_names:
        case = ref_symbol_name[-1]
        if case not in '?*+': continue
        put(ref_symbol_name)
        #usr_ref_symbol_names.add(ref_symbol_name)
        continue

        X = ref_symbol_name[:-1]
        if case == '?':
            d = usr_X2optional
        elif case == '*':
            d = usr_X2star
        else:
            d = usr_X2plus
        d[X] = ref_symbol_name
    usr_ref_symbol_names = ref_symbol_names_to_handle \
        = frozenset(ref_symbol_names_to_handle)



    #internal_ref_symbol_names_to_handle = set()
    lnk_X2optional = {}
    lnk_X2plus = {}
    lnk_X2star = {}
    for ref_symbol_name in ref_symbol_names_to_handle:
        case = ref_symbol_name[-1]
        X = ref_symbol_name[:-1]
        assert case in '?*+'
        if case == '?':
            lnk_X2optional[X] = f'@@multi_lnk<{X}?>@@'
        else:
            lnk_X2star[X] = f'@@multi_lnk<{X}*>@@'
            lnk_X2plus[X] = f'@@multi_lnk<{X}+>@@'


    #update productions
    productions = list(productions)

    def ref_name_to_filtered_ref_name(ref_name):
        return FilteredRefName((), ref_name)
    #; @@lnk2list@@$ X+ = @@multi_lnk<X+>@@
    #; @@lnk2list@@$ X* = @@multi_lnk<X*>@@
    #; @@lnk2list@@$ X? = @@multi_lnk<X?>@@
    filter_names = ['@@lnk2list@@$']
    for def_name in usr_ref_symbol_names:
        lnk_name = f'@@multi_lnk<{def_name}>@@'
        filtered_ref_name = ref_name_to_filtered_ref_name(lnk_name)
        productions.append(
            Unit(filter_names, def_name, [], filtered_ref_name, [])
            )

    def ref_name_to_op2_filtered_ref_name(ref_name):
        return OP2_FilteredRefName(True, FilteredRefName([], ref_name))
    #; @@multi_lnk<X?>@@ : X
    #; @@multi_lnk<X?>@@ :
    for X, def_name in lnk_X2optional.items():
        op2_filtered_ref_name = ref_name_to_op2_filtered_ref_name(X)
        productions.extend([
            Tuple([], def_name, [op2_filtered_ref_name])
            ,Tuple([], def_name, [])
            ])
    #; @@multi_lnk<X+>@@ : @@multi_lnk<X*>@@ X
    for X, def_name in lnk_X2plus.items():
        op2_filtered_ref_names = [
            ref_name_to_op2_filtered_ref_name(lnk_X2star[X])
            ,ref_name_to_op2_filtered_ref_name(X)
            ]
        productions.append(
            Tuple([], def_name, op2_filtered_ref_names)
            )
    #; @@multi_lnk<X*>@@ = @@multi_lnk<X+>@@
    #; @@multi_lnk<X*>@@ :
    for X, def_name in lnk_X2star.items():
        filtered_ref_name = ref_name_to_filtered_ref_name(lnk_X2plus[X])
        productions.extend([
            Unit([], def_name, [], filtered_ref_name, [])
            ,Tuple([], def_name, ())
            ])

    #update maybedead_nonterminal_names???
    #   neednot - since we already defined!
    return productions

def mk_main_result1(ls):
    productions = []
    terminal_set_names = set()
    start_nonterminal_names = set()
    ambiguous_nonterminal_names = set()
    maybedead_nonterminal_names = set()
    for e in ls:
        if isinstance(e, Production):
            productions.append(e)
        elif isinstance(e, Names):
            if isinstance(e, TerminalSetNames):
                terminal_set_names |= e.names
            elif isinstance(e, StartNonterminalNames):
                start_nonterminal_names |= e.names
            elif isinstance(e, AmbiguousNonterminalNames):
                ambiguous_nonterminal_names |= e.names
            elif isinstance(e, MaybedeadNonterminalNames):
                maybedead_nonterminal_names |= e.names
            else:
                raise logic-error
        else:
            raise logic-error
    return (productions
            , terminal_set_names
            , start_nonterminal_names
            , ambiguous_nonterminal_names
            , maybedead_nonterminal_names
            )


# imported
to_unit
lnk2list

# collect "all_filter_names" from raised exception when missing
all_filter_names = \
{'remove_Nones$'
,'mk_unit_unpack_body$'
,'mk_unit_body_from_name$'
,'mk_tuple_with_alias$'
,'const_False$'
,'const_None$'
,'mk_start_nonterminal_names$'
,'mk_discard$'
,'mk_unit$'
,'mk_maybedead_nonterminal_names$'
,'mk_unit_unpack$'
,'to_list$'
,'mk_multi_ref_name$'
,'mk_user_ref_name$'
,'mk_ambiguous_nonterminal_names$'
,'mk_unit_body_from_triple$'
,'mk_kw_ref_name$'
,'const_True$'
,'mk_terminal_set_names$'
,'mk_tuple$'
,'mk_op3_filtered_ref_name$'
,'const_op3_unpack$'
,'mk_op3_from_op2$'
,'mk_filtered_ref_name$'
,'mk_main_result$'
,'to_unit$'
,'lnk2list$'
}
def _mk_filter_name2func():
    filter_name2func = {}
    for filter_name in all_filter_names:
        assert filter_name and filter_name[-1] == '$'
        func_name = filter_name[:-1]
        func = globals()[func_name]
        filter_name2func[filter_name] = func
    return filter_name2func

class Filters__simplified_in_more_simplified:
    filter_name2func = _mk_filter_name2func()
    filter_ex_name2func = {}
    result_cfg_internal_filter_name2func = {'@@lnk2list@@$':lnk2list}
    result_cfg_internal_filter_ex_name2func = {}

filter_name2func = Filters__simplified_in_more_simplified.filter_name2func
filter_ex_name2func = Filters__simplified_in_more_simplified.filter_ex_name2func



