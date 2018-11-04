
def iter_rule_names_for_calc_CFG_inits(
    alternative_name2rule_name
    ,alternative_name2ixsymbols
    ,alternative_name_fullmapping_ops
    ):
    yield from iter_rule_names_from_alternative_name2rule_name(
        alternative_name2rule_name
        ,alternative_name_fullmapping_ops
        )
    yield from iter_rule_names_from_alternative_name2ixsymbols(
        alternative_name2ixsymbols
        ,alternative_name_fullmapping_ops
        )



def iter_rule_names_from_alternative_name2rule_name(
    alternative_name2rule_name
    ,alternative_name_fullmapping_ops
    ):
    return alternative_name_fullmapping_ops.iter_values(alternative_name2rule_name)
def iter_rule_names_from_alternative_name2ixsymbols(
    alternative_name2ixsymbols
    ,alternative_name_fullmapping_ops
    ):
    for alternative_name, ixsymbols in alternative_name_fullmapping_ops\
        .iter_items(alternative_name2ixsymbols):
        for is_rule_name, terminal_set_name_or_rule_name in ixsymbols:
            assert type(is_rule_name) is bool
            if is_rule_name:
                rule_name = terminal_set_name_or_rule_name
                yield rule_name
            else:
                terminal_set_name = terminal_set_name_or_rule_name

