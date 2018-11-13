
def calc_CFG_nonterminal_idx2sorted_production_idc(*
    ,num_nonterminals
    ,production_idx2nonterminal_idx
    ):
    nonterminal_idx2sorted_production_idc = [
        [] for _ in range(num_nonterminals)]
    for production_idx, nonterminal_idx in enumerate(production_idx2nonterminal_idx):
        nonterminal_idx2sorted_production_idc[nonterminal_idx].append(production_idx)

    nonterminal_idx2sorted_production_idc = tuple(map(
        tuple, nonterminal_idx2sorted_production_idc))
    return nonterminal_idx2sorted_production_idc


