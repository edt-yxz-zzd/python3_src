
__all__ = '''
    calc_CFG_inits
    '''.split()


from collections.abc import Hashable
from .iter_rule_names_for_calc_CFG_inits import iter_rule_names_for_calc_CFG_inits
#from .make_rule_name2alternative_names import make_rule_name2alternative_names



def calc_CFG_inits(
    max_init_length # [head]++tail, init++[last]
    #rule_names <<== rule_name_fullmapping_ops
    #,alternative_names <<== alternative_name_fullmapping_ops
    ,alternative_name2rule_name
    ,alternative_name2ixsymbols

    #optional#
    ,rule_name2alternative_names

    ,alternative_name_set_ops
    ,alternative_name_fullmapping_ops
    ,rule_name_fullmapping_ops
    ):
    '''
input:
    alternative_name2rule_name  :: {alternative_name: rule_name}
    alternative_name2ixsymbols  :: {alternative_name: [ixsymbol]}
        ixsymbol = (False, terminal_set_name) | (True, rule_name)
                = (is_rule_name, terminal_set_name_or_rule_name
        # vs xsymbol = (False, terminal_set) | (True, rule_name)
        rule_name = nonterminal
        terminal_set_name should be Hashable
    [optional]rule_name2alternative_names :: {rule_name: {alternative_name}}
        # optional
        #   can be derived by others
        #   but should avoid such work
        # see:
        #   make_rule_name2alternative_names

    alternative_name_set_ops
        .iter
    alternative_name_fullmapping_ops
    rule_name_fullmapping_ops
        # why? so that we can use sequence as fullmapping directly
        fullmapping_ops:
            .static_make_fullmapping_from_fdefault
            .static_contains_key
            .key2value
            .iter_items
output:
    rule_name2inits             :: {rule_name: inits}
    alternative_name2initss     :: {alternative_name: [inits]}
        # alternative_name2idx2inits
        where
            inits :: {init}
            init :: [terminal_set_name]
            len(init) <= max_init_length
'''

    #verify rule_name
    for rule_name in iter_rule_names_for_calc_CFG_inits(
                        alternative_name2rule_name
                        ,alternative_name2ixsymbols
                        ,alternative_name_fullmapping_ops
                        ):
        assert rule_name_fullmapping_ops.static_contains_key(rule_name)

    #verify Hashable
    for alternative_name, ixsymbols in alternative_name_fullmapping_ops\
        .iter_items(alternative_name2ixsymbols):
        for is_rule_name, terminal_set_name_or_rule_name in ixsymbols:
            assert type(is_rule_name) is bool
            if is_rule_name:
                rule_name = terminal_set_name_or_rule_name
            else:
                terminal_set_name = terminal_set_name_or_rule_name
                assert isinstance(terminal_set_name, Hashable)

    ####################### naive algo #############################
    #EOR = end_of_rule = object()

    #init
    #   rule_name2inits
    #   alternative_name2initss
    rule_name2inits = rule_name_fullmapping_ops\
        .static_make_fullmapping_from_fdefault(set)
        # here require Hashable terminal_set_name
    alternative_name2initss = alternative_name_fullmapping_ops\
        .static_make_fullmapping_from_fdefault(list)

    for alternative_name, ixsymbols in alternative_name_fullmapping_ops\
        .iter_items(alternative_name2ixsymbols):
        idx2inits = initss = alternative_name_fullmapping_ops.key2value(
                alternative_name2initss, alternative_name)

        for is_rule_name, terminal_set_name_or_rule_name in ixsymbols:
            if is_rule_name:
                rule_name = terminal_set_name_or_rule_name
                #s = rule_name_fullmapping_ops.key2value(
                #       rule_name2inits, rule_name)
                s= set()
            else:
                terminal_set_name = terminal_set_name_or_rule_name
                s = set()
            idx2inits.append(s)
        idx2inits.append(frozenset({()}))

    # main-loop
    dirty = True
    while dirty:
        dirty = False

        #begin-of-fill alternative_name2initss
        for alternative_name, ixsymbols in alternative_name_fullmapping_ops\
            .iter_items(alternative_name2ixsymbols):
            idx2inits = initss = alternative_name_fullmapping_ops.key2value(
                    alternative_name2initss, alternative_name)

            assert len(ixsymbols) + 1 == len(idx2inits)
            inits = idx2inits[-1]
            for i in reversed(range(len(ixsymbols))):
                succ_inits = inits
                inits = idx2inits[i]
                saved_inits_len = len(inits)
                is_rule_name, terminal_set_name_or_rule_name = ixsymbols[i]
                if is_rule_name:
                    rule_name = terminal_set_name_or_rule_name
                    left_inits = rule_name_fullmapping_ops.key2value(
                            rule_name2inits, rule_name)
                else:
                    terminal_set_name = terminal_set_name_or_rule_name
                    left_inits = [(terminal_set_name,)]

                for left_init in left_inits:
                    L = max_init_length - len(left_init)
                    #bug: if L <= 0: continue
                    if L <= 0:
                        inits.add(left_init)
                        continue
                    for succ_init in succ_inits:
                        inits.add(left_init + succ_init[:L])
                if saved_inits_len < len(inits):
                    dirty = True
            #end-of-fill idx2inits
        #end-of-fill alternative_name2initss

        #begin-of-fill rule_name2inits
        for rule_name, inits in rule_name_fullmapping_ops\
            .iter_items(rule_name2inits):
            saved_inits_len = len(inits)

            alternative_names = rule_name_fullmapping_ops.key2value(
                    rule_name2alternative_names, rule_name)
            for alternative_name in alternative_name_set_ops.iter(alternative_names):
                initss = alternative_name_fullmapping_ops.key2value(
                        alternative_name2initss, alternative_name)
                inits |= initss[0]
            if saved_inits_len < len(inits):
                dirty = True
        #end-of-fill rule_name2inits
    #end-of main-loop

    return rule_name2inits, alternative_name2initss





