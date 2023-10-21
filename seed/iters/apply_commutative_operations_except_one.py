#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/apply_commutative_operations_except_one.py


seed.iters.apply_commutative_operations_except_one
py -m nn_ns.app.debug_cmd   seed.iters.apply_commutative_operations_except_one -x
py -m nn_ns.app.doctest_cmd seed.iters.apply_commutative_operations_except_one:__doc__ -ff -v
py_adhoc_call   seed.iters.apply_commutative_operations_except_one   @f

>>> [*iter_apply_commutative_operations_except_one_(int.__add__, range(1, 6), 2)]
[16, 15, 14, 13, 12]
>>> [*iter_apply_commutative_operations_except_one_(int.__mul__, range(1, 6), 2)]
[240, 120, 80, 60, 48]
>>> [*iter_apply_commutative_operations_except_one_(int.__rpow__, range(1, 6), 2)]
[1329227995784915872903807060280344576, 1152921504606846976, 1099511627776, 1073741824, 16777216]
>>> 2**24
16777216
>>> 16777216**5
1329227995784915872903807060280344576


#]]]'''
__all__ = r'''
    iter_apply_commutative_operations_except_one_
'''.split()#'''
__all__



def iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0, /):
    r'''[[[
    :: (k->x->x) -> [k] -> x -> (iter x)

    :: apply_/(k->x->x) -> keys/[k] -> x0/x -> xs/(iter x){xs[i] == (II<mul=(.)> (apply_ keys[j]) {j :<- [0..<len(keys)] | [j=!=i]})(x0)}

    e.g. eval (a**((n-1)///p) %n) for each prime factor p of (n-1) # [x0 == a**((n-1)///(II p {p})) %n]

    [L := len(commutative_operation_keys)]
    directly impl: (L*(L-1))*op
    plain recur impl: (L*(L-1)/2 + (L-1))*op
    layer bisect impl: O(L*log2(L))*op
        <==> the impl in use

    #]]]'''#'''
    if 1:
        #check seq:
        len(commutative_operation_keys)
        commutative_operation_keys[:0]
    if not len(commutative_operation_keys):
        return

    ks = commutative_operation_keys
    stack = [(0, len(ks), x0, 0, 0)]
    while stack:
        begin, end, x, begin2, end2 = stack.pop()
            # ops has been applied except those in ks[begin:end] and ks[begin2:end2] to makeup x
        assert begin < end
        assert begin2 <= end2
        for k in ks[begin2:end2]:
            x = apply_(k, x)
        x
            # ops has been applied except those in ks[begin:end] to makeup x

        sz = end -begin
        if sz == 1:
            yield x
            continue
        #mid = begin+ sz//2
        mid = end- sz//2
        stack.append((mid, end, x, begin, mid))
        stack.append((begin, mid, x, mid, end))

__all__


from seed.iters.apply_commutative_operations_except_one import iter_apply_commutative_operations_except_one_
from seed.iters.apply_commutative_operations_except_one import *
