
__all__ = '''
    calc_CFG_production_idx2idxalternative
    '''.split()

#from ..CFG import CFG, explain_ref_symbol_psidx

def calc_CFG_production_idx2idxalternative(*
    ,production_idx2alternative_tail_idx
    ,alternative_tail_idx2alternative_idx_maybe_pair
    ):
    production_idx2idxalternative = []
    for production_idx, alternative_tail_idx in enumerate(production_idx2alternative_tail_idx):
        idxalternative = []
        while True:
            may_pair = alternative_tail_idx2alternative_idx_maybe_pair[alternative_tail_idx]
            if not may_pair: break
            ref_symbol_psidx, alternative_tail_idx = pair = may_pair
            idxalternative.append(ref_symbol_psidx)
        production_idx2idxalternative.append(idxalternative)

    production_idx2idxalternative = tuple(map(tuple
        , production_idx2idxalternative))
    return production_idx2idxalternative




