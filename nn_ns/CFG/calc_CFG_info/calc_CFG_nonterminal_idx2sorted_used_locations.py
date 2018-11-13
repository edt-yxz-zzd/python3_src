
__all__ = '''
    calc_CFG_nonterminal_idx2sorted_used_locations
    '''.split()



from ..CFG import explain_ref_symbol_psidx

def calc_CFG_nonterminal_idx2sorted_used_locations(*
    ,num_nonterminals
    ,production_idx2idxalternative
    ):
    '''
input:
    num_nonterminals
    production_idx2idxalternative
        from calc_CFG_production_idx2idxalternative
output:
    nonterminal_idx2sorted_used_locations :: [[used_location]]
        used_location = (production_idx, production_rhs_idx)
'''
    nonterminal_idx2sorted_used_locations = [[] for _ in range(num_nonterminals)]
    for production_idx, idxalternative in enumerate(production_idx2idxalternative):
        for rhs_idx, ref_symbol_psidx in enumerate(idxalternative):
            is_nonterminal, idx = explain_ref_symbol_psidx(ref_symbol_psidx)
            if is_nonterminal:
                nonterminal_idx = idx
                nonterminal_idx2sorted_used_locations[
                    nonterminal_idx].append((production_idx, rhs_idx))
    return tuple(map(tuple, nonterminal_idx2sorted_used_locations))




