
def make_rule_name2alternative_names(
    alternative_name2rule_name
    , alternative_name_fullmapping_ops
    , rule_name_fullmapping_ops
    , alternative_name_mutable_set_ops
        # IMutableSetOps__alternative_name_mutable_set_ops
    ):
    rule_name2alternative_names = rule_name_fullmapping_ops\
            .static_make_fullmapping_from_fdefault(
                alternative_name_mutable_set_ops.static_make_empty_set)
    for alternative_name, rule_name in alternative_name_fullmapping_ops\
        .iter_items(alternative_name2rule_name):
        alternative_names = rule_name_fullmapping_ops.key2value(
                rule_name2alternative_names, rule_name)
        alternative_name_mutable_set_ops.add(
                alternative_names, alternative_name)
    return rule_name2alternative_names

