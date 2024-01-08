useless:cancel
#__all__:goto
r'''[[[
e ../../python3_src/seed/types/frontier.py
view ../../python3_src/seed/types/linked_list.py
[[
source:
view ../../python3_src/seed/math/right_angled_triangle_side_length.py
    (sqrt__odd4B, odd4B, ez4B, b) = mk____B_ex_(floor_half_sqrt__odd4B, ceil_half_ez4B)
===
(floor_half_sqrt__odd4B, ceil_half_ez4B)
    where both are uint
but ???monotone nondecreasing:min_hypotenuse<(floor_half_sqrt__odd4B, ceil_half_ez4B)>???
try to proof:min_hypotenuse_is_monotone_nondecreasing_with_respect_to___floor_half_sqrt__odd4B___ceil_half_ez4B)
    !!!fail!!!

===
def mk____B_ex_(floor_half_sqrt__odd4B, ceil_half_ez4B, /):
    '-> (sqrt__odd4B, odd4B, ez4B, b)'
    check_int_ge(0, floor_half_sqrt__odd4B)
    check_int_ge(0, ceil_half_ez4B)
def mk__min_sqrt__plus_A_B_or_half__and_step___care_odd_(floor_half_sqrt__odd4B, ceil_half_ez4B, /):
    '-> (min_sqrt__plus_A_B_or_half, step) # !!!result diff from mk__min_sqrt__plus_A_B_or_half_!!! 『|=1』if necessary'
    min_sqrt__plus_A_B_or_half = mk__min_sqrt__plus_A_B_or_half_(floor_half_sqrt__odd4B, ceil_half_ez4B)
def iter__right_angled_triangle_side_length_difference_ratio__given_B_(floor_half_sqrt__odd4B, ceil_half_ez4B, /, *, with_side_length_ratio=False, with_params=False):
    '-> iter result_ex/(if not with_side_length_ratio then (a,b) elif not with_params then ((a,b), side_length_ratio) else ((a,b), side_length_ratio, params)) #side_length_ratio/(short_side, middle_side, long_side) #params/(floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half)'
    (with_side_length_ratio, with_params) = _std_with_xxx_(with_side_length_ratio, with_params)

    (min_sqrt__plus_A_B_or_half, step) = mk__min_sqrt__plus_A_B_or_half__and_step___care_odd_(floor_half_sqrt__odd4B, ceil_half_ez4B)
    for sqrt__plus_A_B_or_half in count_(min_sqrt__plus_A_B_or_half, step):
        try:
            (a, b) = mk__right_angled_triangle_side_length_difference_ratio_(floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half)
            # [[gcd(a,b) == 1][sqrt_(2*(a+b)*b) %1 == 0][a%2 == 1][a >= 1][b >= 1]]
        except Bad___gcd_A_B__gt1:
            continue
            pass

        (a,b)
        result_ex = _mk_result_ex5A_B_(floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half, a, b, with_side_length_ratio=with_side_length_ratio, with_params=with_params)
        yield result_ex
def mk__min_sqrt__plus_A_B_or_half_(floor_half_sqrt__odd4B, ceil_half_ez4B, /):
    '-> min sqrt__plus_A_B_or_half'
    (sqrt__odd4B, odd4B, ez4B, b) = mk____B_ex_(floor_half_sqrt__odd4B, ceil_half_ez4B)
    # [sqrt__odd4B >= 1]
    # [sqrt__odd4B %2 == 1]
    # [odd4B >= 1]
    # [odd4B %2 == 1]
    # [odd4B == sqrt__odd4B**2]
    # [ez4B >= 0]
    # [[ez4B == 0]or[ez4B %2 == 1]]
    # [b == odd4B*2**ez4B]

    ######################
    if 0:
        min_sqrt__plus_A_B_or_half = ceil_sqrt_((sqrt__odd4B**2 * 2**ez4B + 1) >> (ez4B==0))
    ######################
    # [a%2 == 1]
    min_a = 1
    min_plus_A_B = min_a + b
    if ez4B:
        # [b%2 == 0]
        # [min_plus_A_B%2 == 1]
        min_plus_A_B_or_half = min_plus_A_B
    else:
        # [b%2 == 1]
        # [min_plus_A_B%2 == 0]
        min_plus_A_B_or_half = min_plus_A_B >>1
    min_sqrt__plus_A_B_or_half = ceil_sqrt_(min_plus_A_B_or_half)
    return min_sqrt__plus_A_B_or_half


]]

[[
maintain a frontier to be visited
    [all_vtc == visited_vtc + frontier + remote_vtc]
    [unvisited_vtc(all_vtc, all_dedges; visited_vtc) =[def]= (all_vtc \-\ visited_vtc)]
    [frontier_(all_vtc, all_dedges; visited_vtc) =[def]= {vtx | [[vtx :<- unvisited_vtc][[(src,dst) :<- all_dedges] -> [dst == vtx] -> [src <- visited_vtc]]]}]
e.g.
    2-D grid DAG:
        all_vtc = {(x,y) | [x,y::uint]}
        all_dedges = {((x,y) --> (x,y+1)) | [x,y::uint]} \-/ {((x,y) --> (x+1,y)) | [x,y::uint]}
        srcs = {(0,0)}
]]


seed.types.frontier
py -m nn_ns.app.debug_cmd   seed.types.frontier -x
py -m nn_ns.app.doctest_cmd seed.types.frontier:__doc__ -ff -v
py_adhoc_call   seed.types.frontier   @f
from seed.types.frontier import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__


from seed.types.linked_list import DoublyLinkedList
class Frontier__2D_grid_DAG__uint_vtx:
    def __init__(sf, /):
        sf.frontier = [(0,0)]
unvisited_angles/corner
dfs wfs

[[

TODO
e ../../python3_src/seed/types/frontier.py


DONE
view ../../python3_src/seed/types/linked_list.py
DONE
view ../../python3_src/seed/math/RhoDetector.py
DONE
view ../../python3_src/seed/math/generate_partition4additive_semigroup__total_ordering__increasing.py
view ../../python3_src/seed/for_libs/for_heapq.py
DONE
HeapItem<key,__le__,reverse>
view ../../python3_src/seed/types/OverrideOrdering.py
view ../../python3_src/seed/types/Heap.py

DONE
?.xxx[iii].y[j] =[def]= lambda a:a.xxx[iii].y[j]
view ../../python3_src/seed/types/PlaceholderAsSelf.py


DONE
w2+1==2v2 无限递减证明？
e ../../python3_src/seed/math/right_angled_triangle_side_length.py
    # [:condition4_WW1_eq_2VV~~[w**2+1==2*v**2]=>???]:goto
e others/数学/condition4_WW1_eq_2VV.txt


TODO
total ordering cmp converter
单函数 le => (le,lt,ge,gt)
out\in:le   flip    not
    le      x       x
    lt      y       y
    ge      y       x
    gt      x       y
双函数 (le,lt),[flip=False] => (le,lt,ge,gt)
out\in:le   flip    not
    le      x       x
    gt      x       y
out\in:lt   flip    not
    lt      x       x
    ge      x       y
矩阵:数据关联:(flip,not)
out\in:     le  lt  ge  gt
    le      xx  yy  yx  xy
    lt      yy  xx  xy  yx
    ge      yx  xy  xx  yy
    gt      xy  yx  yy  xx
    [flip=False] => ({le,gt}*{lt,ge})
单函数 le => cmp
    cmp L R =[def]=
        | not$ le L R = +1 #GT
        | not$ le R L = -1 #LT
        | otherwise = 0 #EQ
双函数 (le,eq),[flip=False] => cmp
    cmp L R =[def]=
        | not$ le L R = +1 #GT
        | not$ eq L R = -1 #LT
        | otherwise = 0 #EQ


]]

def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
if __name__ == "__main__":
    pass
__all__


from seed.types.frontier import *
