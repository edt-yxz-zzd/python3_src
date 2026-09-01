#__all__:goto
r'''[[[
e ../../python3_src/seed/io/join_columns.py

seed.io.join_columns
py -m nn_ns.app.debug_cmd   seed.io.join_columns -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.join_columns:__doc__ -ht # -ff -df
#######

[[
===
1:
view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_.py
view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
    view ../../python3_src/nn_ns/math_nn/numbers/b001918-least_positive_primitive_root_of_n_th_prime__fst_10000.txt
    view ../../python3_src/nn_ns/math_nn/numbers/b002233-least_positive_prime_primitive_root_of_n_th_prime__except_0th__fst_10000.txt

===
2:
view ../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt
view ../../python3_src/nn_ns/math_nn/numbers/b000924-class_number_of_QQ(sqrt(n_th_neg_squarefree))__fst_10000.txt

head '../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt'  | colrm 2 2
===
]]


'#'; __doc__ = r'#'
>>>



[[
view others/app/termux/help/cmd_intro.man1.20251130-group.txt

head '../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt' | cut -s -d' ' --output-delimiter=: -f1,2
paste -d' '   '../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt' '../../python3_src/nn_ns/math_nn/numbers/b000924-class_number_of_QQ(sqrt(n_th_neg_squarefree))__fst_10000.txt'  | head


py_adhoc_call   '' ,iter '%%:P'  ='P.seed.math.iter_sorted_squarefree_uints().iter_sorted_squarefree_uints_()' | head


py_adhoc_call   '' ,iter '%%:P'  ='((-u, -u if (-u)%4==1 else 4*-u) for u in P.seed.math.iter_sorted_squarefree_uints().iter_sorted_squarefree_uints_())' | paste -d' ' - '../../python3_src/nn_ns/math_nn/numbers/b000924-class_number_of_QQ(sqrt(n_th_neg_squarefree))__fst_10000.txt' | sed 's/^(\(-[0-9]\+\), \(-[0-9]\+\)) \([0-9]\+\) \([0-9]\+\)$/\3 \1 \2 \4/' | head
    1 -1 -4 1
    2 -2 -8 1
    3 -3 -3 1
    4 -5 -20 2
    5 -6 -24 2
    6 -7 -7 1
    7 -10 -40 2
    8 -11 -11 1
    9 -13 -52 2
    10 -14 -56 4

py_adhoc_call   '' ,iter ='(4*-u for u in range(1, 9+20000))' | paste -d' '  - '../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt' | sed 's/^\(-[0-9]\+\) \([0-9]\+\) \([0-9]\+\)$/\2 \1 \3/' | head
    1 -4 1
    2 -8 1
    3 -12 1
    4 -16 1
    5 -20 2
    6 -24 2
    7 -28 1
    8 -32 2
    9 -36 2
    10 -40 2

view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_.py
e ../../python3_src/nn_ns/math_nn/numbers/_cmds4patch_.txt
]]

py_adhoc_call   seed.io.join_columns   @f
from seed.io.join_columns import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__):
#.    from itertools import islice
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def iter5description4input_column__7file_(ipath, regex8sep, idx2nm, /):
    #skip empty lines???
    #skip comment lines???
    #skip head lines???
    raise 000-TODO


def join_columns_(format4output_row, /, *ls4description4input_column):
    r'''[[[
    [format4output_row :: str]
    [ls4description4input_column :: [description4input_column]]
        [description4input_column :: (case, payload)]
            ('fields', (Iter field), nm)
            ('fieldss', (Iter [field]), idx2nm)
            ('file', ipath, regex8sep, idx2nm)

    #]]]'''#'''
    raise 000-TODO

__all__
from seed.io.join_columns import *
