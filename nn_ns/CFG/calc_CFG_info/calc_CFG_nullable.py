
r'''
for CFG_Parser__Earley
    static build a tree for each nullable nonterminal
        arbitrary one if ambiguous

see: "def - CFG.txt"
    idxalternative = [ref_symbol_psidx]
    idxproduction = (production_idx, [ref_symbol_psidx])
    production_idx2idxalternative = [idxalternative] = [[ref_symbol_psidx]]
    nonterminal_idx2sorted_production_idc = [[production_idx]]

    used_location = (production_idx, production_rhs_idx)
    nonterminal_idx2sorted_used_locations = [[used_location]]
        nonterminal_idx to production_idx who use the nonterminal_idx and where
'''


__all__ = '''
    calc_CFG_nullable__basic
    calc_CFG_nullable__is_nullable
    calc_CFG_nullable__one_tree
    '''.split()




from ..CFG import CFG, explain_ref_symbol_psidx


def calc_CFG_nullable__one_tree(*
    ,production_idx2nonterminal_idx
    ,nonterminal_idx2sorted_used_locations
    ,production_idx2maybe_nullable_bottomup_order_idx
    ,nonterminal_idx2maybe_first_discovered_nullable_production_idx
    ):
    r'''
input:
    production_idx2nonterminal_idx

    nonterminal_idx2sorted_used_locations
        from calc_CFG_nonterminal_idx2sorted_used_locations

    production_idx2maybe_nullable_bottomup_order_idx
    nonterminal_idx2maybe_first_discovered_nullable_production_idx
        from calc_CFG_nullable__basic
output:
    nonterminal_idx2sorted_nullable_production_idc :: [[production_idx]]
        nullable <<== len > 0
        is_directly_ambiguous_nullable <<== len > 1
        # not consider ambiguous subtree
        # for indirectly ambiguous see nonterminal_idx2maybe_one_null_tree
    nonterminal_idx2maybe_one_null_tree :: [()|(is_ambiguous_nullable, production_idx)]
        () if not nullable
        (is_ambiguous_nullable, production_idx) if nullable
        # is_ambiguous_nullable == is_indirectly_ambiguous_nullable
        #   consider ambiguous subtree
    has_ambiguous_nullable_nonterminal :: bool
'''
    num_nonterminals = len(nonterminal_idx2sorted_used_locations)

    def is_nullable_production_idx(production_idx):
        return production_idx2maybe_nullable_bottomup_order_idx[production_idx] is not None

    nonterminal_idx2sorted_nullable_production_idc = [[] for _ in range(num_nonterminals)]
    for production_idx, nonterminal_idx in enumerate(production_idx2nonterminal_idx):
        if is_nullable_production_idx(production_idx):
            nonterminal_idx2sorted_nullable_production_idc[nonterminal_idx].append(production_idx)



    def on_production_idx_is_ambiguous_nullable(production_idx):
        nonterminal_idx = production_idx2nonterminal_idx[production_idx]
        on_nonterminal_idx_is_ambiguous_nullable(nonterminal_idx)
    def on_nonterminal_idx_is_ambiguous_nullable(nonterminal_idx):
        if nonterminal_idx2maybe_one_null_tree[nonterminal_idx]: return
        may_nullable_production_idx = nonterminal_idx2maybe_first_discovered_nullable_production_idx[nonterminal_idx]
        assert may_nullable_production_idx is not None
        nullable_production_idx = may_nullable_production_idx

        is_ambiguous_nullable = True
        null_tree = nullable_production_idx
        nonterminal_idx2maybe_one_null_tree[nonterminal_idx] = (
            is_ambiguous_nullable, null_tree)
        for production_idx, _ in nonterminal_idx2sorted_used_locations[nonterminal_idx]:
            on_production_idx_is_ambiguous_nullable(production_idx)


    nonterminal_idx2maybe_one_null_tree = [()]*num_nonterminals
    for nonterminal_idx, nullable_production_idc in enumerate(nonterminal_idx2sorted_nullable_production_idc):
        if len(nullable_production_idc) > 1:
            on_nonterminal_idx_is_ambiguous_nullable(nonterminal_idx)

    has_ambiguous_nullable_nonterminal = False
    for nonterminal_idx, may_nullable_production_idx in enumerate(nonterminal_idx2maybe_first_discovered_nullable_production_idx):
        if may_nullable_production_idx is not None:
            # nonterminal_idx is nullable
            nullable_production_idx = may_nullable_production_idx
            if nonterminal_idx2maybe_one_null_tree[nonterminal_idx]:
                # ambiguous nullable
                has_ambiguous_nullable_nonterminal = True
            else:
                # not ambiguous nullable
                is_ambiguous_nullable = False
                null_tree = nullable_production_idx
                nonterminal_idx2maybe_one_null_tree[nonterminal_idx] = (
                    is_ambiguous_nullable, null_tree)

    nonterminal_idx2sorted_nullable_production_idc = map(tuple, nonterminal_idx2sorted_nullable_production_idc)

    nonterminal_idx2sorted_nullable_production_idc = tuple(nonterminal_idx2sorted_nullable_production_idc)
    nonterminal_idx2maybe_one_null_tree = tuple(nonterminal_idx2maybe_one_null_tree)
    has_ambiguous_nullable_nonterminal
    return (nonterminal_idx2sorted_nullable_production_idc
            ,nonterminal_idx2maybe_one_null_tree
            ,has_ambiguous_nullable_nonterminal
            )




def is_not_None(x):
    return x is not None
def list_map_is_not_None(iterable):
    return list(map(is_not_None, iterable))
def calc_CFG_nullable__is_nullable(*
    ,production_idx2maybe_nullable_bottomup_order_idx
    ,nonterminal_idx2maybe_first_discovered_nullable_production_idx
    ):
    '''
input:
    production_idx2maybe_nullable_bottomup_order_idx
    nonterminal_idx2maybe_first_discovered_nullable_production_idx
        from calc_CFG_nullable__basic
output:
    production_idx2is_nullable
    nonterminal_idx2is_nullable
'''
    production_idx2is_nullable = list_map_is_not_None(
        production_idx2maybe_nullable_bottomup_order_idx)
    nonterminal_idx2is_nullable = list_map_is_not_None(
        nonterminal_idx2maybe_first_discovered_nullable_production_idx)
    return production_idx2is_nullable, nonterminal_idx2is_nullable


def calc_CFG_nullable__basic(*
    ,production_idx2nonterminal_idx
    ,production_idx2idxalternative
    ,nonterminal_idx2sorted_used_locations
    ):
    r'''
input:
    production_idx2nonterminal_idx
    production_idx2idxalternative
        from calc_CFG_production_idx2idxalternative
    nonterminal_idx2sorted_used_locations
        from calc_CFG_nonterminal_idx2sorted_used_locations

output:
    nullable_production_idc_in_bottomup_order :: [nullable_production_idx]
    production_idx2maybe_nullable_bottomup_order_idx :: [None|UInt]
        <-> nullable_production_idc_in_bottomup_order
            # bijection:
    nonterminal_idx2maybe_first_discovered_nullable_production_idx
        :: [None|nullable_production_idx]

    #production_idx2is_nullable :: [bool]
        = map(\x->x is not None, production_idx2maybe_nullable_bottomup_order_idx)
    #nonterminal_idx2is_nullable :: [bool]
        = map(\x->x is not None, nonterminal_idx2maybe_first_discovered_nullable_production_idx)


'''
    num_nonterminals = len(nonterminal_idx2sorted_used_locations)
    num_productions = len(production_idx2idxalternative)
    assert num_productions == len(production_idx2nonterminal_idx)

    #production_idx2is_nullable = [False]*num_productions
    #nonterminal_idx2is_nullable = [False]*num_nonterminals
        # used as cache to avoid redudant calc
    production_idx2num_rhs_nonnulls = list(map(len, production_idx2idxalternative))

    nullable_production_idc_in_bottomup_order = []
    production_idx2maybe_nullable_bottomup_order_idx = [None]*num_productions
    nonterminal_idx2maybe_first_discovered_nullable_production_idx = [None]*num_nonterminals
    def is_nullable_nonterminal_idx(nonterminal_idx):
        return nonterminal_idx2maybe_first_discovered_nullable_production_idx[nonterminal_idx] is not None
    def is_nullable_production_idx(production_idx):
        return production_idx2maybe_nullable_bottomup_order_idx[production_idx] is not None
    def on_nullable_production_idx(production_idx):
        assert not is_nullable_production_idx(production_idx)
        #assert not production_idx2is_nullable[production_idx]
        nullable_bottomup_order_idx = len(nullable_production_idc_in_bottomup_order)
        production_idx2maybe_nullable_bottomup_order_idx[production_idx] = nullable_bottomup_order_idx
        nullable_production_idc_in_bottomup_order.append(production_idx)

        #production_idx2is_nullable[production_idx] = True
        nonterminal_idx = production_idx2nonterminal_idx[production_idx]
        if not is_nullable_nonterminal_idx(nonterminal_idx):
            nonterminal_idx2maybe_first_discovered_nullable_production_idx[nonterminal_idx] = production_idx

            #nonterminal_idx2is_nullable[nonterminal_idx] = True
            for production_idx, _ in nonterminal_idx2sorted_used_locations[nonterminal_idx]:
                n = production_idx2num_rhs_nonnulls[production_idx]
                n -= 1
                production_idx2num_rhs_nonnulls[production_idx] = n
                assert n >= 0
                if n == 0:
                    on_nullable_production_idx(production_idx)

    for production_idx, idxalternative in enumerate(production_idx2idxalternative):
        if not idxalternative:
            on_nullable_production_idx(production_idx)

    #production_idx2is_nullable = tuple(production_idx2is_nullable)
    #nonterminal_idx2is_nullable = tuple(nonterminal_idx2is_nullable)
    #return production_idx2is_nullable, nonterminal_idx2is_nullable
    (nullable_production_idc_in_bottomup_order
    ,production_idx2maybe_nullable_bottomup_order_idx
    ,nonterminal_idx2maybe_first_discovered_nullable_production_idx
    ) = r = tuple(map(tuple, [
        nullable_production_idc_in_bottomup_order
        ,production_idx2maybe_nullable_bottomup_order_idx
        ,nonterminal_idx2maybe_first_discovered_nullable_production_idx
        ]))
    return r




