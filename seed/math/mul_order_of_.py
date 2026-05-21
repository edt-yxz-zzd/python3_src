#__all__:goto
r'''[[[
e ../../python3_src/seed/math/mul_order_of_.py

seed.math.mul_order_of_
py -m nn_ns.app.debug_cmd   seed.math.mul_order_of_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.mul_order_of_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.mul_order_of_   @f
]]]'''#'''
__all__ = r'''
mul_order_of_
    prepare4mul_order_of_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.iters.apply_commutative_operations_except_one import iter_apply_commutative_operations_except_one_
    #.def iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0, /):
    #.    :: (k->x->x) -> [k] -> x -> (iter x)
    from seed.math.II import II
    from seed.types.FrozenDict import mk_FrozenDict
    from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division

#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def prepare4mul_order_of_(group_order, ps4group_order, /):
    'group_order/uint{>=1} -> ps4group_order/{prime} -> info4group_order # [group_order==len(group)]'
    p2e4group_order = complete_factor_pint_via_trial_division(ps4group_order, group_order)
    777;del ps4group_order
    #p2e4group_order = mk_FrozenDict(p2e4group_order)
    j2p4group_order = tuple(sorted(p2e4group_order))
    j2ep4group_order = tuple(p2e4group_order[p] for p in j2p4group_order)
    j2pw4group_order = tuple(p**p2e4group_order[p] for p in j2p4group_order)
    #.IIps4group_order = II(j2p4group_order)
    info4group_order = (group_order, j2p4group_order, j2ep4group_order, j2pw4group_order)
    return info4group_order

def mul_order_of_(info4group_order, is_one_, __rpow__, x0, /):
    'info{group_order} -> is_one_/(x->bool) -> __rpow__/(exp->x->x) -> x0/x/element{group} -> k/uint%D # [group_order==len(group)][x0**group_order == one][k == min{k | [k:<-[1..=group_order]][x0**k == one]}][group_order%k == 0] # see:prepare4mul_order_of_'
    if is_one_(x0):
        k = 1
    else:
        (group_order, j2p4group_order, j2ep4group_order, j2pw4group_order) = info4group_order
        j2ep4k = []
        for j, xw in enumerate(iter_apply_commutative_operations_except_one_(__rpow__, j2pw4group_order, x0)):
            p = j2p4group_order[j]
            ep4G = j2ep4group_order[j]
            if is_one_(xw):
                ep4k = 0
            else:
                for ep4k in range(1, 1+ep4G):
                    xw = __rpow__(p, xw)
                    if is_one_(xw):
                        ep4k
                        break
                else:
                    if not is_one_(__rpow__(group_order, x0)):raise ValueError(group_order, x0)
                    raise 000
                ep4k
            ep4k
            j2ep4k.append(ep4k)
        j2ep4k
        k = II(p**ep4k for p, ep4k in zip(j2p4group_order, j2ep4k))
    k
    return k



__all__
from seed.math.mul_order_of_ import mul_order_of_, prepare4mul_order_of_
from seed.math.mul_order_of_ import *
