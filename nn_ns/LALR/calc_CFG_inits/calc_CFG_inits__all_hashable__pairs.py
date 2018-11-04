
__all__ = '''
    calc_CFG_inits__all_hashable__pairs
    '''.split()

from .calc_CFG_inits__all_hashable import calc_CFG_inits__all_hashable
from seed.seq_tools.split_tuples import split_tuples

def calc_CFG_inits__all_hashable__pairs(
    max_init_length
    ,rule_name_ixsymbols_pairs
    ,*
    ,rule_name_fullmapping_is_sequence : bool
    ,naive : bool
    ):
    '''wrapper for calc_CFG_inits__all_hashable/calc_CFG_inits

input:
    max_init_length             :: UInt
    rule_name_ixsymbols_pairs :: [(rule_name, [ixsymbol)]
    rule_name_fullmapping_is_sequence           :: bool
see:
    calc_CFG_inits
    calc_CFG_inits__all_hashable
'''
    alternative_name2rule_name, alternative_name2ixsymbols = split_tuples(
        2, rule_name_ixsymbols_pairs)
    return calc_CFG_inits__all_hashable(max_init_length
        ,alternative_name2rule_name
        ,alternative_name2ixsymbols
        ,naive=naive
        ,alternative_name_fullmapping_is_sequence=True
        ,rule_name_fullmapping_is_sequence
            =rule_name_fullmapping_is_sequence
        )


