
__all__ = '''
    parse__more_simplified_version__ver2
    '''.split()



from .make_CFG import make_CFG_ex
from .basic_parse__more_simplified_version import \
    basic_parse__more_simplified_version
from .concrete_CFG_syntax import more_simplified_concrete_CFG_syntax


def parse__more_simplified_version__ver2(source, *
    ,terminal_set_ops
    ,terminal_set_name2terminal_set
    ,start_nonterminal_names
    ,ambiguous_nonterminal_names
    ,maybedead_nonterminal_names
    ):
    '''

input:
    source :: str
        which satisfy more_simplified_version syntax
    terminal_set_ops
    terminal_set_name2terminal_set
    start_nonterminal_names
    ambiguous_nonterminal_names
    maybedead_nonterminal_names
output:
    (cfg, production_name2production, filter_names, filter_ex_names, start_nonterminal_idc, ambiguous_nonterminal_idc)

vs ver1:
    * using make_CFG_ex
    * result are diff
    ver1 -> (cfg, production_idx2filter_names, production_idx2selected_idc)
    ver2 -> (cfg, production_name2production, filter_names, filter_ex_names, start_nonterminal_idc, ambiguous_nonterminal_idc)

'''
    (tuple_productions, terminal_set_names
    , nonterminal_names, undefined_xsymbol_names
    ) = basic_parse__more_simplified_version(source)

    (cfg, production_name2production
    , filter_names, filter_ex_names
    , start_nonterminal_idc, ambiguous_nonterminal_idc
    ) = make_CFG_ex(
        productions=tuple_productions
        ,terminal_set_names=terminal_set_names
        ,start_nonterminal_names=start_nonterminal_names
        ,ambiguous_nonterminal_names=ambiguous_nonterminal_names
        ,maybedead_nonterminal_names=maybedead_nonterminal_names

        ,terminal_set_ops=terminal_set_ops
        ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
        )

    return (cfg
        , production_name2production
        , filter_names
        , filter_ex_names
        , start_nonterminal_idc
        , ambiguous_nonterminal_idc
        )

if __name__ == "__main__":
    from ..the_py_terminal_set_ops import the_py_terminal_set_ops

    (cfg, production_name2production
    , filter_names, filter_ex_names
    , start_nonterminal_idc, ambiguous_nonterminal_idc
    ) = parse__more_simplified_version__ver2(
            more_simplified_concrete_CFG_syntax
            ,terminal_set_ops=the_py_terminal_set_ops
            ,terminal_set_name2terminal_set=lambda a:{a}
            ,start_nonterminal_names=()
            ,ambiguous_nonterminal_names=()
            ,maybedead_nonterminal_names=()
            )

    print(cfg)
    print(filter_names)
    print(filter_ex_names)
    print(start_nonterminal_idc)
    print(ambiguous_nonterminal_idc)

