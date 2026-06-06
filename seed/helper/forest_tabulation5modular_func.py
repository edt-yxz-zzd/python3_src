#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/forest_tabulation5modular_func.py

seed.helper.forest_tabulation5modular_func
py -m nn_ns.app.debug_cmd   seed.helper.forest_tabulation5modular_func -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.forest_tabulation5modular_func:__doc__ -ht # -ff -df
#######

[[
源起:
e script/整数分解牜尸方法牜吸引子.py
]]


'#'; __doc__ = r'#'
>>> f = lambda M, x, /:(1+pow(x,2,M))%M
>>> show4tab_(f, 24)
x2y=[1, 2, 5, 10, 17, 2, 13, 2, 17, 10, 5, 2, 1, 2, 5, 10, 17, 2, 13, 2, 17, 10, 5, 2]
y2num_xs=[0, 2, 8, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 2, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0]
y2xs=[[], [0, 12], [1, 5, 7, 11, 13, 17, 19, 23], [], [], [2, 10, 14, 22], [], [], [], [], [3, 9, 15, 21], [], [], [6, 18], [], [], [], [4, 8, 16, 20], [], [], [], [], [], []]
x2min_root=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
x2height=[2, 1, 0, 2, 2, 0, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1]
min_root2len_period={2: 2}
min_root2minmax_height={2: (1, 2)}
num_trees=1
max_len_period=2
max_height=2

>>> show4tab_(f, 35)
x2y=[1, 2, 5, 10, 17, 26, 2, 15, 30, 12, 31, 17, 5, 30, 22, 16, 12, 10, 10, 12, 16, 22, 30, 5, 17, 31, 12, 30, 15, 2, 26, 17, 10, 5, 2]
y2num_xs=[0, 1, 4, 0, 0, 4, 0, 0, 0, 0, 4, 0, 4, 0, 0, 2, 2, 4, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 4, 2, 0, 0, 0]
y2xs=[[], [0], [1, 6, 29, 34], [], [], [2, 12, 23, 33], [], [], [], [], [3, 17, 18, 32], [], [9, 16, 19, 26], [], [], [7, 28], [15, 20], [4, 11, 24, 31], [], [], [], [], [14, 21], [], [], [], [5, 30], [], [], [], [8, 13, 22, 27], [10, 25], [], [], []]
x2min_root=[5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 10, 10, 5, 5, 5, 5, 5, 10, 10, 5, 5]
x2height=[3, 2, 1, 1, 1, 0, 2, 3, 2, 1, 0, 1, 0, 2, 3, 2, 1, 0, 1, 1, 2, 3, 2, 1, 1, 1, 0, 2, 3, 2, 1, 0, 1, 1, 2]
min_root2len_period={5: 3, 10: 3}
min_root2minmax_height={5: (1, 3), 10: (1, 1)}
num_trees=2
max_len_period=3
max_height=3

>>> show4tab_(f, 19)
x2y=[1, 2, 5, 10, 17, 7, 18, 12, 8, 6, 6, 8, 12, 18, 7, 17, 10, 5, 2]
y2num_xs=[0, 1, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 0, 0, 0, 2, 2]
y2xs=[[], [0], [1, 18], [], [], [2, 17], [9, 10], [5, 14], [8, 11], [], [3, 16], [], [7, 12], [], [], [], [], [4, 15], [6, 13]]
x2min_root=[12, 12, 12, 12, 12, 12, 12, 12, 8, 12, 12, 8, 12, 12, 12, 12, 12, 12, 12]
x2height=[5, 4, 3, 7, 4, 2, 5, 1, 0, 6, 6, 1, 0, 5, 2, 4, 7, 3, 4]
min_root2len_period={8: 1, 12: 1}
min_root2minmax_height={8: (1, 1), 12: (2, 7)}
num_trees=2
max_len_period=1
max_height=7


>>> show4tab_(f, 19, more=1)
x2y=[1, 2, 5, 10, 17, 7, 18, 12, 8, 6, 6, 8, 12, 18, 7, 17, 10, 5, 2]
y2num_xs=[0, 1, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 0, 0, 0, 2, 2]
y2xs=[[], [0], [1, 18], [], [], [2, 17], [9, 10], [5, 14], [8, 11], [], [3, 16], [], [7, 12], [], [], [], [], [4, 15], [6, 13]]
x2min_root=[12, 12, 12, 12, 12, 12, 12, 12, 8, 12, 12, 8, 12, 12, 12, 12, 12, 12, 12]
x2height=[5, 4, 3, 7, 4, 2, 5, 1, 0, 6, 6, 1, 0, 5, 2, 4, 7, 3, 4]
min_root2len_period={8: 1, 12: 1}
min_root2minmax_height={8: (1, 1), 12: (2, 7)}
num_trees=2
max_len_period=1
max_height=7
min_root2root2tree={8: {8: {11: {}}}, 12: {12: {7: {5: {2: {1: {0: {}}, 18: {6: {9: {}, 10: {3: {}, 16: {}}}, 13: {}}}, 17: {4: {}, 15: {}}}, 14: {}}}}}
min_root2layers={8: [[8], [11]], 12: [[12], [7], [5, 14], [2, 17], [1, 4, 15, 18], [0, 6, 13], [9, 10], [3, 16]]}



>>> show4tab_(f, 5, more=1)
x2y=[1, 2, 0, 0, 2]
y2num_xs=[2, 1, 2, 0, 0]
y2xs=[[2, 3], [0], [1, 4], [], []]
x2min_root=[0, 0, 0, 0, 0]
x2height=[0, 0, 0, 1, 1]
min_root2len_period={0: 3}
min_root2minmax_height={0: (1, 1)}
num_trees=1
max_len_period=3
max_height=1
min_root2root2tree={0: {0: {3: {}}, 1: {}, 2: {4: {}}}}
min_root2layers={0: [[0, 1, 2], [3, 4]]}

>>> show4tab_(f, 7, more=1)
x2y=[1, 2, 5, 3, 3, 5, 2]
y2num_xs=[0, 1, 2, 2, 0, 2, 0]
y2xs=[[], [0], [1, 6], [3, 4], [], [2, 5], []]
x2min_root=[5, 5, 5, 3, 3, 5, 5]
x2height=[3, 2, 1, 0, 1, 0, 2]
min_root2len_period={3: 1, 5: 1}
min_root2minmax_height={3: (1, 1), 5: (2, 3)}
num_trees=2
max_len_period=1
max_height=3
min_root2root2tree={3: {3: {4: {}}}, 5: {5: {2: {1: {0: {}}, 6: {}}}}}
min_root2layers={3: [[3], [4]], 5: [[5], [2], [1, 6], [0]]}



>>> show4tab_(f, 13, more=1)
x2y=[1, 2, 5, 10, 4, 0, 11, 11, 0, 4, 10, 5, 2]
y2num_xs=[2, 1, 2, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0]
y2xs=[[5, 8], [0], [1, 12], [], [4, 9], [2, 11], [], [], [], [], [3, 10], [6, 7], []]
x2min_root=[0, 0, 0, 10, 4, 0, 0, 0, 0, 4, 10, 0, 0]
x2height=[0, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 1, 1]
min_root2len_period={0: 4, 4: 1, 10: 1}
min_root2minmax_height={0: (1, 2), 4: (1, 1), 10: (1, 1)}
num_trees=3
max_len_period=4
max_height=2
min_root2root2tree={0: {0: {8: {}}, 1: {}, 2: {12: {}}, 5: {11: {6: {}, 7: {}}}}, 4: {4: {9: {}}}, 10: {10: {3: {}}}}
min_root2layers={0: [[0, 1, 2, 5], [8, 11, 12], [6, 7]], 4: [[4], [9]], 10: [[10], [3]]}


>>> show4tab_(f, 7*13, more=1)
x2y=[1, 2, 5, 10, 17, 26, 37, 50, 65, 82, 10, 31, 54, 79, 15, 44, 75, 17, 52, 89, 37, 78, 30, 75, 31, 80, 40, 2, 57, 23, 82, 52, 24, 89, 65, 43, 23, 5, 80, 66, 54, 44, 36, 30, 26, 24, 24, 26, 30, 36, 44, 54, 66, 80, 5, 23, 43, 65, 89, 24, 52, 82, 23, 57, 2, 40, 80, 31, 75, 30, 78, 37, 89, 52, 17, 75, 44, 15, 79, 54, 31, 10, 82, 65, 50, 37, 26, 17, 10, 5, 2]
y2num_xs=[0, 1, 4, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 2, 0, 4, 0, 0, 0, 0, 0, 4, 4, 0, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 2, 4, 0, 0, 2, 0, 0, 2, 4, 0, 0, 0, 0, 0, 2, 0, 4, 0, 4, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 2, 2, 4, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0]
y2xs=[[], [0], [1, 27, 64, 90], [], [], [2, 37, 54, 89], [], [], [], [], [3, 10, 81, 88], [], [], [], [], [14, 77], [], [4, 17, 74, 87], [], [], [], [], [], [29, 36, 55, 62], [32, 45, 46, 59], [], [5, 44, 47, 86], [], [], [], [22, 43, 48, 69], [11, 24, 67, 80], [], [], [], [], [42, 49], [6, 20, 71, 85], [], [], [26, 65], [], [], [35, 56], [15, 41, 50, 76], [], [], [], [], [], [7, 84], [], [18, 31, 60, 73], [], [12, 40, 51, 79], [], [], [28, 63], [], [], [], [], [], [], [], [8, 34, 57, 83], [39, 52], [], [], [], [], [], [], [], [], [16, 23, 68, 75], [], [], [21, 70], [13, 78], [25, 38, 53, 66], [], [9, 30, 61, 82], [], [], [], [], [], [], [19, 33, 58, 72], []]
x2min_root=[5, 5, 5, 10, 17, 5, 5, 5, 5, 82, 10, 31, 5, 5, 5, 5, 75, 17, 31, 5, 5, 5, 82, 75, 31, 31, 5, 5, 5, 75, 82, 31, 31, 5, 5, 82, 75, 5, 31, 31, 5, 5, 75, 82, 5, 31, 31, 5, 82, 75, 5, 5, 31, 31, 5, 75, 82, 5, 5, 31, 31, 82, 75, 5, 5, 5, 31, 31, 75, 82, 5, 5, 5, 31, 17, 75, 5, 5, 5, 5, 31, 10, 82, 5, 5, 5, 5, 17, 10, 5, 5]
x2height=[3, 2, 1, 1, 1, 0, 2, 3, 2, 1, 0, 1, 1, 2, 3, 2, 1, 0, 1, 2, 2, 3, 2, 1, 1, 1, 0, 2, 3, 2, 1, 0, 2, 2, 2, 3, 2, 1, 1, 1, 0, 2, 3, 2, 1, 2, 2, 1, 2, 3, 2, 1, 0, 1, 0, 2, 3, 2, 2, 2, 1, 1, 2, 3, 2, 1, 0, 1, 1, 2, 3, 2, 2, 1, 1, 0, 2, 3, 2, 1, 0, 1, 0, 2, 3, 2, 1, 1, 1, 1, 2]
min_root2len_period={5: 4, 10: 1, 17: 1, 31: 4, 75: 1, 82: 1}
min_root2minmax_height={5: (1, 3), 10: (1, 1), 17: (1, 1), 31: (1, 2), 75: (1, 3), 82: (1, 3)}
num_trees=6
max_len_period=4
max_height=3
min_root2root2tree={5: {5: {2: {1: {0: {}}, 27: {}, 64: {}, 90: {}}, 37: {6: {}, 20: {}, 71: {}, 85: {}}, 89: {19: {}, 33: {}, 58: {}, 72: {}}}, 26: {44: {15: {14: {}, 77: {}}, 41: {}, 50: {7: {}, 84: {}}, 76: {}}, 47: {}, 86: {}}, 40: {65: {8: {}, 34: {}, 57: {28: {}, 63: {}}, 83: {}}}, 54: {12: {}, 51: {}, 79: {13: {}, 78: {21: {}, 70: {}}}}}, 10: {10: {3: {}, 81: {}, 88: {}}}, 17: {17: {4: {}, 74: {}, 87: {}}}, 31: {31: {11: {}, 24: {32: {}, 45: {}, 46: {}, 59: {}}, 67: {}}, 52: {18: {}, 60: {}, 73: {}}, 66: {39: {}}, 80: {25: {}, 38: {}, 53: {}}}, 75: {75: {16: {}, 23: {29: {}, 36: {42: {}, 49: {}}, 55: {}, 62: {}}, 68: {}}}, 82: {82: {9: {}, 30: {22: {}, 43: {35: {}, 56: {}}, 48: {}, 69: {}}, 61: {}}}}
min_root2layers={5: [[5, 26, 40, 54], [2, 12, 37, 44, 47, 51, 65, 79, 86, 89], [1, 6, 8, 13, 15, 19, 20, 27, 33, 34, 41, 50, 57, 58, 64, 71, 72, 76, 78, 83, 85, 90], [0, 7, 14, 21, 28, 63, 70, 77, 84]], 10: [[10], [3, 81, 88]], 17: [[17], [4, 74, 87]], 31: [[31, 52, 66, 80], [11, 18, 24, 25, 38, 39, 53, 60, 67, 73], [32, 45, 46, 59]], 75: [[75], [16, 23, 68], [29, 36, 55, 62], [42, 49]], 82: [[82], [9, 30, 61], [22, 43, 48, 69], [35, 56]]}




py_adhoc_call   seed.helper.forest_tabulation5modular_func   @show4tab_ ='lambda M, x, /:(1+pow(x,2,M))%M'  --more=1  =13
py_adhoc_call   seed.helper.forest_tabulation5modular_func   @show4tab_ ='lambda M, x, /:(1+pow(x,2,M))%M'  --more=1  ='7*13'
]]]'''#'''
__all__ = r'''
group_
    tab_
        show4tab_
        MAX_MODULUS
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_uint_lt
    from seed.debug.show_name_value_pairs_ import errshow_name_value_pairs_, show_name_value_pairs_, parse_xnms_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...
#max_M
#max_modulus = 2**17
MAX_MODULUS = 2**17

_max1_more = 2
def group_(x2y, /, *, more=0):
    check_uint_lt(_max1_more, more)
    M = len(x2y)
    for x in range(M):
        y = x2y[x]
        check_uint_lt(M, y)

    y2xs = [[] for x in range(M)]
    for x in range(M):
        y = x2y[x]
        y2xs[y].append(x)
    y2xs
    x2min_root = {}
    x2height = {}
    min_root2len_period = {}
    for x in range(M):
        if x in x2min_root:continue
        xs = [x]
        x2j = {x:0}
        for j in range(1,1+M):
            x = x2y[x]
            if x in x2min_root:break
            if x in x2j:break
            xs.append(x)
            x2j[x] = j
        else:
            raise Exception((M, xs[0]))
        x
        if x in x2min_root:
            min_root = x2min_root[x]
            height = x2height[x]
            extra = xs
            for x in xs:
                x2min_root[x] = min_root
            for height, x in enumerate(reversed(extra), 1+height):
                x2height[x] = height
            continue
        j = x2j[x]
        period = xs[j:]
        extra = xs[:j]
        min_root = min(period)
        min_root2len_period[min_root] = len(period)
        for x in xs:
            x2min_root[x] = min_root
        height = 0
        for x in period:
            x2height[x] = height
        for height, x in enumerate(reversed(extra), 1+height):
            x2height[x] = height
    x2min_root = [x2min_root[x] for x in range(M)]
    x2height = [x2height[x] for x in range(M)]
    y2num_xs = [*map(len, y2xs)]

    min_root2minmax_height = dict.fromkeys(min_root2len_period.keys(), (1+M, -1))
    for y, num_xs in enumerate(y2num_xs):
        if num_xs == 0:
            height = x2height[y]
            min_root = x2min_root[y]
            (a, b) = min_root2minmax_height[min_root]
            if b == -1:
                a = b = height
            elif height > b:
                assert 0 <= a <= b < height
                b = height
            elif height < a:
                assert 0 <= height < a <= b
                a = height
            else:
                assert 0 <= a <= height <= b
                continue
            min_root2minmax_height[min_root] = (a, b)
    min_root2minmax_height
    for min_root in min_root2len_period.keys():
        (a, b) = min_root2minmax_height[min_root]
        if b == -1:
            # tree be bare circle roots without leaf
            a = b = 0
            min_root2minmax_height[min_root] = (a, b)
    min_root2minmax_height

    max_height = max(ht for _, ht in min_root2minmax_height.values())
    max_len_period = max(min_root2len_period.values())
    num_trees = len(min_root2len_period)
    result0 = (x2y, y2num_xs, y2xs, x2min_root, x2height, min_root2len_period, min_root2minmax_height, (num_trees, max_len_period, max_height))
    if more == 0:
        return result0
    forest = _mk_forest_(y2xs, x2height, x2min_root, min_root2len_period.keys())
    777;min_root2root2tree = forest
    min_root2layers = _layout_(x2min_root, x2height, min_root2minmax_height)
    result1 = (*result0, min_root2root2tree, min_root2layers)
    if more == 1:
        return result1
    raise Exception(_max1_more, more)
_snms4result0 = '(x2y, y2num_xs, y2xs, x2min_root, x2height, min_root2len_period, min_root2minmax_height, (num_trees, max_len_period, max_height))'
_ex_snms4result1 = '(min_root2root2tree, min_root2layers)'
_more2xnms = {}
def _gmk_xnms5more_(more, /):
    check_uint_lt(_max1_more, more)
    try:
        return _more2xnms[more]
    except KeyError:
        pass
    if more == 0:
        xnms = parse_xnms_(_snms4result0)
    else:
        xnms_ = _gmk_xnms5more_(more-1)
        _xnms = parse_xnms_(globals()[f'_ex_snms4result{more}'])
        xnms = (*xnms_, *_xnms)
    xnms
    _more2xnms[more] = xnms
    return _gmk_xnms5more_(more)

def _mk_forest_(y2xs, x2height, x2min_root, min_roots, /):
    min_root2root2tree = {min_root:{} for min_root in min_roots}
    ls = []
    #min_root2roots = {min_root:[] for min_root in min_roots}
    for x, height in enumerate(x2height):
        if height == 0:
            root = x
            min_root = x2min_root[root]
            #roots = min_root2roots[min_root]
            #roots.append(root)
            root2tree = min_root2root2tree[min_root]
            #root2tree[root] = tree6root = {}
            ls.append((root, root2tree))
    #min_root2roots
    #root2tree = {root:{} for roots in min_root2roots.values() for root in roots}
    ls
    min_root2root2tree
    forest = min_root2root2tree

    #ls = [(min_root, forest) for min_root in min_roots]
    while ls:
        (y, y2tree) = ls.pop()
        tree6y = y2tree.setdefault(y, {})
        x2tree = tree6y
        height4y = x2height[y]
        for x in y2xs[y]:
            height4x = x2height[x]
            if height4x == 0:
                assert height4y == 0
                continue
            assert height4x == 1+height4y
            ls.append((x, x2tree))
    return forest

def _layout_(x2min_root, x2height, min_root2minmax_height, /):
    min_root2layers = {min_root: [[] for _ in range(1+b)] for min_root, (a,b) in min_root2minmax_height.items()}
    for x, min_root in enumerate(x2min_root):
        layers = min_root2layers[min_root]
        height2layer = layers
        height2xs = height2layer

        height4x = x2height[x]
        xs = height2xs[height4x]
        xs.append(x)
    return min_root2layers

def tab_(f, M, /, *args, max_M=MAX_MODULUS, more=0):
    #if M > 2**17:raise 000
    if M > max_M:raise OverflowError(M, max_M)#ValueError
    x2y = [None]*M
    for x in range(M):
        y = f(M, *args, x)
        check_uint_lt(M, y)
        x2y[x] = y
    x2y
    result_tuple = group_(x2y, more=more)
    return result_tuple
    #return (x2y, y2num_xs, y2xs, x2min_root, x2height, min_root2len_period, min_root2minmax_height, (num_trees, max_len_period, max_height))

def show4tab_(f, M, /, *args, max_M=MAX_MODULUS, more=0):
    result_tuple = tab_(f, M, *args, max_M=max_M, more=more)
    xnms = _gmk_xnms5more_(more)
    show_name_value_pairs_(xnms, result_tuple)



__all__
from seed.helper.forest_tabulation5modular_func import group_, tab_, show4tab_
    # (x2y, y2num_xs, y2xs, x2min_root, x2height, min_root2len_period, min_root2minmax_height, (num_trees, max_len_period, max_height)) = tab_(f, M, *args, max_M=max_M)
    # (x2y, y2num_xs, y2xs, x2min_root, x2height, min_root2len_period, min_root2minmax_height, (num_trees, max_len_period, max_height), min_root2root2tree, min_root2layers) = tab_(f, M, *args, max_M=max_M, more=1)
from seed.helper.forest_tabulation5modular_func import *
