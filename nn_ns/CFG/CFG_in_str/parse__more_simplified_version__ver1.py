
__all__ = '''
    parse__more_simplified_version__ver1
    '''.split()


from ..CFG import CFG
from ..the_py_terminal_set_ops import the_py_terminal_set_ops
from ..ExplainRefSymbolName__using_terminal_set_names import \
    ExplainRefSymbolName__using_terminal_set_names

from ..errors import ParseFailError
from .concrete_CFG_syntax import more_simplified_concrete_CFG_syntax
from .basic_parse__more_simplified_version import \
    basic_parse__more_simplified_version




def parse__more_simplified_version__ver1(source, *
    ,terminal_set_ops
    ,terminal_set_name2terminal_set
    ,allowed_undefined_nonterminal_names = ()
    ):
    # -> (CFG, production_idx2filter_names, production_idx2selected_idc)
    #
    (tuple_productions, terminal_set_names
    , nonterminal_names, undefined_xsymbol_names
    ) = basic_parse__more_simplified_version(source)

    if undefined_xsymbol_names:
        allowed = set(allowed_undefined_nonterminal_names)
        undefined = undefined_xsymbol_names
        not_allowed = undefined - allowed
        if not_allowed:
            raise ParseFailError(f'exist not_allowed undefined_xsymbol_names: {not_allowed}')

    explain_ref_symbol_name = ExplainRefSymbolName__using_terminal_set_names(terminal_set_names)

    # pair = (nonterminal_name, [ref_symbol_name])
    pairs = []
    production_idx2filter_names = []
    production_idx2selected_idc = []
    for p in tuple_productions:
        production_idx = len(pairs)
        production_idx2filter_names.append(p.filter_names)

        selected_idc, ref_symbol_names = \
            __handle_op2_filtered_ref_names(p.op2_filtered_ref_names)
        production_idx2selected_idc.append(selected_idc)

        pair = p.nonterminal_name, ref_symbol_names
        pairs.append(pair)

    cfg = CFG.make_CFG__hashable_name__less(pairs
        ,terminal_set_ops=terminal_set_ops
        ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
        ,explain_ref_symbol_name=explain_ref_symbol_name
        )
    return cfg, production_idx2filter_names, production_idx2selected_idc


def __handle_op2_filtered_ref_names(op2_filtered_ref_names):
    selected_idc = []
    ref_symbol_names = []
    for i, op2_filtered_ref_name in enumerate(op2_filtered_ref_names):
        op2 = op2_filtered_ref_name.op2
        if op2:
            selected_idc.append(i)

        filtered_ref_name = op2_filtered_ref_name.filtered_ref_name
        assert not filtered_ref_name.filter_names
        ref_symbol_names.append(filtered_ref_name.ref_symbol_name)
    return selected_idc, ref_symbol_names


if __name__ == "__main__":
    #######################
    (cfg, production_idx2filter_names, production_idx2selected_idc
    ) = parse__more_simplified_version__ver1(
            more_simplified_concrete_CFG_syntax
            ,terminal_set_ops=the_py_terminal_set_ops
            ,terminal_set_name2terminal_set=lambda a:{a}
            )

    print(cfg)
    print(production_idx2filter_names)
    print(production_idx2selected_idc)

