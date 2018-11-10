
'''
use abstract_syntax_datatype as input to make_CFG_ex

make_CFG_ex :: [Production] -> (...) -> (CFG, ...)
'''

__all__ = '''
    make_CFG_ex
    basic_make_CFG
    '''.split()


from ..CFG import CFG
from ..ExplainRefSymbolName__using_terminal_set_names import \
    ExplainRefSymbolName__using_terminal_set_names
from ..errors import ParseFailError
from .abstract_syntax_datatype import (
    Production
    ,productions2basic_productions
    ,collect_lhs_defined_nonterminal_names
    ,collect_rhs_ref_symbol_names
    ,collect_filter_ex_names
    ,collect_filter_names
    ,remove_duplicated_productions
    ,collect_duplicated_actions
    )




def make_CFG_ex(*
    ,productions
    ,terminal_set_names
    ,start_nonterminal_names
    ,ambiguous_nonterminal_names
    ,maybedead_nonterminal_names

    ,terminal_set_ops
    ,terminal_set_name2terminal_set
    ):
    '''
input:
    see: basic_make_CFG.__doc__
output:
    cfg :: CFG
    production_name2production :: {production_name: production}
    filter_names :: {filter_name}
    filter_ex_names :: {filter_ex_name}
    start_nonterminal_idc :: sorted[nonterminal_idx]
    ambiguous_nonterminal_idc :: sorted[nonterminal_idx]
'''
    len(productions)
    terminal_set_names = set(terminal_set_names)
    start_nonterminal_names = set(start_nonterminal_names)
    ambiguous_nonterminal_names = set(ambiguous_nonterminal_names)
    maybedead_nonterminal_names = set(maybedead_nonterminal_names)

    cfg, production_name2production = basic_make_CFG(
            productions=productions
            ,terminal_set_names=terminal_set_names
            ,maybedead_nonterminal_names=maybedead_nonterminal_names
            ,ambiguous_nonterminal_names=ambiguous_nonterminal_names
            ,start_nonterminal_names=start_nonterminal_names
            ,terminal_set_ops=terminal_set_ops
            ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
            )
    filter_names = collect_filter_names(productions)
    filter_ex_names = collect_filter_ex_names(productions)


    ambiguous_nonterminal_idc = sorted(set(map(
        cfg.nonterminal_name2nonterminal_idx
        , ambiguous_nonterminal_names
        )))
    start_nonterminal_idc = sorted(set(map(
        cfg.nonterminal_name2nonterminal_idx
        , start_nonterminal_names
        )))
    return (cfg, production_name2production
            , filter_names, filter_ex_names
            , start_nonterminal_idc, ambiguous_nonterminal_idc
            )


def basic_make_CFG(*
    ,productions
    ,terminal_set_names
    ,maybedead_nonterminal_names
    ,ambiguous_nonterminal_names
    ,start_nonterminal_names

    ,terminal_set_ops
    ,terminal_set_name2terminal_set
    ):
    '''
input:
    productions :: [Production]
    terminal_set_names :: Set terminal_set_name
        come from @terminal_set@
    maybedead_nonterminal_names :: Set nonterminal_name
        come from @maybedead_nonterminal@
    ambiguous_nonterminal_names :: Set nonterminal_name
        come from @ambiguous_nonterminal@
    start_nonterminal_names :: Set nonterminal_name
        come from @start_nonterminal@

    terminal_set_ops
        see: CFG
    terminal_set_name2terminal_set
        see: CFG
output:
    cfg :: CFG
    production_name2production
        # production_name is basic_production # a pair
'''
    # use maybedead_nonterminal_names here only
    nonterminal_names = make_nonterminal_names_and_check_post_parse_args__distinguishable_ref_symbol_name(
        productions=productions
        ,terminal_set_names=terminal_set_names
        ,maybedead_nonterminal_names=maybedead_nonterminal_names
        ,ambiguous_nonterminal_names=ambiguous_nonterminal_names
        ,start_nonterminal_names=start_nonterminal_names
        )
    del maybedead_nonterminal_names
    del ambiguous_nonterminal_names
    del start_nonterminal_names

    productions
    terminal_set_names
    nonterminal_names
    terminal_set_ops
    terminal_set_name2terminal_set


    explain_ref_symbol_name = ExplainRefSymbolName__using_terminal_set_names(terminal_set_names)

    (idx2production, production2idx
    ) = remove_duplicated_productions(productions)
    assert len(idx2production) == len(production2idx) <= len(productions)
    del productions


    bads = collect_duplicated_actions(idx2production)
    if bads:
        raise ParseFailError(f'same basic_production but have diff actions: {bads}')


    basic_production2production = {
        production.to_basic_production() : production
        for production in idx2production
        }
    if len(basic_production2production) < len(idx2production):
        raise logic-error # since not bads

    # production_name = basic_production
    # pair = basic_production
    basic_productions = set(basic_production2production)

    production_names = basic_productions
    production_name2production = basic_production2production

    production_name2basic_production = {
        basic_production : basic_production
        for basic_production in production_names
        }
    __production_name2pair = production_name2basic_production

    cfg = CFG.make_CFG__hashable_name(
        __production_name2pair

        ,terminal_set_names=terminal_set_names
        ,nonterminal_names=nonterminal_names
        ,production_names=production_names

        ,terminal_set_ops=terminal_set_ops
        ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
        ,explain_ref_symbol_name=explain_ref_symbol_name
        )

    return cfg, production_name2production
def _set_make_CFG_ex_doc():
    sep = '='*20
    sepline = f'\n{sep}   basic_make_CFG.__doc__   {sep}\n'
    make_CFG_ex.__doc__ += f'{sepline}{basic_make_CFG.__doc__}'
_set_make_CFG_ex_doc();
del _set_make_CFG_ex_doc

def make_nonterminal_names_and_check_post_parse_args__distinguishable_ref_symbol_name(*
    ,productions
    ,terminal_set_names
    ,maybedead_nonterminal_names
    ,ambiguous_nonterminal_names
    ,start_nonterminal_names
    ):
    len(productions)
    lhs_defined_nonterminal_names = collect_lhs_defined_nonterminal_names(productions)
    rhs_ref_symbol_names = collect_rhs_ref_symbol_names(productions)
    nonterminal_names = (
        lhs_defined_nonterminal_names
        | maybedead_nonterminal_names
        | ambiguous_nonterminal_names
        | start_nonterminal_names
        )

    both_xsymbol_names = nonterminal_names & terminal_set_names
    if both_xsymbol_names:
        raise ParseFailError(f'both nonterminal_names&terminal_set_names: {both_xsymbol_names}')

    undefined_xsymbol_names = rhs_ref_symbol_names - nonterminal_names - terminal_set_names
    if undefined_xsymbol_names:
        raise ParseFailError(f'exist undefined_xsymbol_names: {undefined_xsymbol_names}')
    return nonterminal_names


