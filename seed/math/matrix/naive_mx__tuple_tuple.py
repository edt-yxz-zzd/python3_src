#__all__:goto
r'''[[[
e ../../python3_src/seed/math/matrix/naive_mx__tuple_tuple.py
view ../../python3_src/seed/math/matrix/solve_matrix.py
view ../../python3_src/seed/algo/FFT/Walsh_transform.py


seed.math.matrix.naive_mx__tuple_tuple
py -m nn_ns.app.debug_cmd   seed.math.matrix.naive_mx__tuple_tuple -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.matrix.naive_mx__tuple_tuple:__doc__ -ht # -ff -df
#######

[[
used in:
view ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/white_and_primary_chromaticities.py
    using:inv_mx_3x3_
]]
[[
assume:[[mx :: [[v]]][len(mx) > 0][len(mx[0]) > 0]]
assume:[[vec :: [v]][len(vec) > 0]]
old:[mul_mx_vec_ :: mx{H,W} -> vec{H} -> mx{H,1}]
new:[mul_mx_vec_ :: mx{H,W} -> vec{H} -> vec{H}]

]]



'#'; __doc__ = r'#'
>>> mx_2x3 = mx5scanline_per_(3, range(6))
>>> mx_3x2 = mx5scanline_per_(2, range(6))
>>> mx_2x3
((0, 1, 2), (3, 4, 5))
>>> mx_3x2
((0, 1), (2, 3), (4, 5))
>>> mx2scanline_(mx_3x2)
(0, 1, 2, 3, 4, 5)
>>> mx2hw_shape_(mx_3x2)
(3, 2)
>>> vec_3 = vec5mx_at_(1, mx_3x2)
>>> vec_3
(1, 3, 5)
>>> mx_3x1 = mx5vec_(vec_3)
>>> mx_3x1
((1,), (3,), (5,))
>>> transpose_mx_(mx_3x1)
((1, 3, 5),)
>>> mul_vec_(vec_3, vec_3)
35
>>> mul_mx_vec_(mx_2x3, vec_3)
(13, 40)
>>> mul_mx_(mx_2x3, mx_3x1)
((13,), (40,))
>>> mx_2x2 = mul_mx_(mx_2x3, mx_3x2)
>>> mx_2x2
((10, 13), (28, 40))
>>> mx_3x3 = mul_mx_(mx_3x2, mx_2x3)
>>> mx_3x3
((3, 4, 5), (9, 14, 19), (15, 24, 33))
>>> scale_vec_(5, vec_3)
(5, 15, 25)
>>> scale_mx_(5, mx_2x3)
((0, 5, 10), (15, 20, 25))




>>> inv_mx_2x2_(mx_2x2)
((1.1111111111111112, -0.3611111111111111), (-0.7777777777777778, 0.2777777777777778))
>>> mul_mx_(mx_2x2, inv_mx_2x2_(mx_2x2))
((1.0, 0.0), (3.552713678800501e-15, 1.0))



>>> inv_mx_3x3_(mx_3x3)
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> _mx_3x3 = mx5scanline_per_(3, range(2,9))
Traceback (most recent call last):
    ...
ValueError: ('mx5scanline_per_():remain:', 1)
>>> _mx_3x3 = mx5scanline_per_(3, [*range(2,9), 11,12])
>>> _inv_mx_3x3 = inv_mx_3x3_(_mx_3x3)
>>> mul_mx_(_mx_3x3, _inv_mx_3x3)
((1.0, -2.220446049250313e-16, 0.0), (0.0, 0.9999999999999991, 0.0), (0.0, 0.0, 1.0))


>>> _mx_3x3
((2, 3, 4), (5, 6, 7), (8, 11, 12))
>>> _inv_mx_3x3
((-0.8333333333333334, 1.3333333333333333, -0.5), (-0.6666666666666666, -1.3333333333333333, 1.0), (1.1666666666666667, 0.3333333333333333, -0.5))

>>> neg_if_odd_(1, 999)
-999
>>> neg_if_odd_(2, 999)
999
>>> mk_mx__ij2v_(3, 2, lambda i,j,/:(i,j))
(((0, 0), (0, 1)), ((1, 0), (1, 1)), ((2, 0), (2, 1)))
>>> remove_cross5mx_(0, 2, mx_2x3)
((3, 4),)
>>> remove_row5mx_(0, mx_3x2)
((2, 3), (4, 5))
>>> slow__companion_mx_(_mx_3x3)
((-5, -4, 7), (8, -8, 2), (-3, 6, -3))
>>> slow__determinant5mx_(_mx_3x3)
6
>>> _2__inv_mx_3x3 = slow__inv_mx_(_mx_3x3)
>>> _2__inv_mx_3x3
((-0.8333333333333334, 1.3333333333333333, -0.5), (-0.6666666666666666, -1.3333333333333333, 1.0), (1.1666666666666667, 0.3333333333333333, -0.5))
>>> _2__inv_mx_3x3 == _inv_mx_3x3
True


>>> add_mx_(mx_3x2, mx_3x2)
((0, 2), (4, 6), (8, 10))
>>> sub_mx_(mx_3x2, mx_3x2)
((0, 0), (0, 0), (0, 0))
>>> add_vec_(vec_3, vec_3)
(2, 6, 10)
>>> sub_vec_(vec_3, vec_3)
(0, 0, 0)



>>> vec_3
(1, 3, 5)
>>> vec2square_geo_length_(vec_3)
35
>>> square_geo_distance_(vec_3, [2, 2, 3])
6




>>> def test__inv_mx_3x3_(mx, /):
...     I3 = mul_mx_(mx, inv_mx_3x3_(mx))
...     assert sum(map(abs, chain.from_iterable(sub_mx_(eye_mx_3x3, I3)))) < 1e-12, I3
...     return I3

>>> test__inv_mx_3x3_([(1, 7, 3), (99, -44, 5), (-9, 777, 0)])
((0.9999999999999998, 0.0, 0.0), (0.0, 1.0, 0.0), (-2.7755575615628914e-17, 0.0, 0.9999999999999999))
>>> test__inv_mx_3x3_([(111, 7, 3), (79, -4, 50), (-45, 577, 10)])
((1.0, 6.938893903907228e-18, 6.505213034913027e-19), (-1.1102230246251565e-16, 1.0, 3.469446951953614e-18), (2.7755575615628914e-17, 0.0, 1.0))
>>> test__inv_mx_3x3_([(111, 79, 3), (79, -4, 50), (-45, 57, 170)])
((1.0, -1.3877787807814457e-17, 1.5612511283791264e-17), (0.0, 1.0, 0.0), (-1.1102230246251565e-16, 2.220446049250313e-16, 1.0))
>>> test__inv_mx_3x3_([(11, 79, 13), (7, -4, 509), (-4, 57, 1750)])
((1.0, -1.231653667943533e-16, -4.0766001685454967e-17), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))









py_adhoc_call   seed.math.matrix.naive_mx__tuple_tuple   @f
]]]'''#'''
__all__ = r'''
    mx2hw_shape_
    mx2scanline_
    mx5scanline_per_
    mx5vec_
    vec5mx_at_
    vec2square_geo_length_
    square_geo_distance_

    transpose_mx_
    mul_vec_
    mul_mx_
    mul_mx_vec_
    scale_vec_
    scale_mx_
    inv_mx_2x2_
    inv_mx_3x3_



    mk_mx__ij2v_
        mk_eye_mx_
            eye_mx_3x3
    remove_cross5mx_
        remove_column5mx_
        remove_row5mx_
    slow__companion_mx_
    neg_if_odd_
    slow__determinant5mx_
    slow__inv_mx_


    add_mx_
    sub_mx_
    add_vec_
    sub_vec_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from operator import __eq__
from itertools import islice, chain
from seed.tiny_.containers import mk_tuple
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...



#view ../../python3_src/seed/algo/FFT/Walsh_transform.py
def transpose_mx_(mx, /):
    _nc = nr = len(mx)
    _nr = nc = len(mx[0])
    return tuple(tuple(mx[_jc][_jr] for _jc in range(_nc)) for _jr in range(_nr))
def mul_vec_(lhs_vec, rhs_vec, /):
    assert len(lhs_vec) == len(rhs_vec)
    return sum(a*b for a,b in zip(lhs_vec, rhs_vec))
def mul_mx_(lhs_mx, rhs_mx, /):
    assert len(lhs_mx[0]) == len(rhs_mx)
    _rhs_mx = transpose_mx_(rhs_mx)
    return tuple(tuple(mul_vec_(rowL, columnR) for columnR in _rhs_mx) for rowL in lhs_mx)
def mx5vec_(vec, /):
    return tuple((x,) for x in vec)
def mul_mx_vec_(lhs_mx, rhs_vec, /):
    '[mul_mx_vec_ :: mx{H,W} -> vec{H} -> vec{H}] #old:[mul_mx_vec_ :: mx{H,W} -> vec{H} -> mx{H,1}]'
    #old-API:return tuple((mul_vec_(rowL, rhs_vec),) for rowL in lhs_mx)
    return tuple(mul_vec_(rowL, rhs_vec) for rowL in lhs_mx)
def scale_vec_(lhs_v, rhs_vec, /):
    return tuple(lhs_v*x for x in rhs_vec)
def scale_mx_(lhs_v, rhs_mx, /):
    return tuple(scale_vec_(lhs_v, rowR) for rowR in rhs_mx)
def inv_mx_2x2_(mx_2x2, /):
    [(a00,a01)
    ,(a10,a11)
    ] = mx_2x2
    D = a00*a11-a01*a10
    inv_mx =((+a11/D,-a01/D)
            ,(-a10/D,+a00/D)
            )
    return inv_mx
def inv_mx_3x3_(mx_3x3, /):
    r'''[[[
    [a00,a01,a02
    ;a10,a11,a12
    ;a20,a21,a22
    ]
    transpose:
        [+(a11*a22-a12*a21),-(a10*a22-a12*a20),+(a10*a21-a11*a20)
        ;-(a01*a22-a02*a21),+(a00*a22-a02*a20),-(a00*a21-a01*a20)
        ;+(a01*a12-a02*a11),-(a00*a12-a02*a10),+(a00*a11-a01*a10)
        ]/D
    D := +a00*(a11*a22-a12*a21)-a01*(a10*a22-a12*a20)+a02*(a10*a21-a11*a20)

    view ../../python3_src/seed/math/matrix/solve_matrix.py
    #]]]'''#'''
    [(a00,a01,a02)
    ,(a10,a11,a12)
    ,(a20,a21,a22)
    ] = mx_3x3
    ls =(+(a11*a22-a12*a21),-(a10*a22-a12*a20),+(a10*a21-a11*a20)
        ,-(a01*a22-a02*a21),+(a00*a22-a02*a20),-(a00*a21-a01*a20)
        ,+(a01*a12-a02*a11),-(a00*a12-a02*a10),+(a00*a11-a01*a10)
        )
    D = +a00*ls[0]+a01*ls[1]+a02*ls[2]
    ls = tuple(x/D for x in ls)
    inv_mx = (ls[0::3], ls[1::3], ls[2::3])
    return inv_mx
def mx5scanline_per_(num_columns, xs, /):
    assert num_columns > 0
    xs = iter(xs)
    def __(it, /):
        while 1:
            row = tuple(islice(it, 0, num_columns))
            if len(row) == num_columns:
                yield row
            elif not row:
                return
            else:
                raise ValueError('mx5scanline_per_():remain:', len(row))
    return tuple(__(xs))
def mx2scanline_(mx, /):
    return tuple(chain.from_iterable(mx))
def mx2hw_shape_(mx, /):
    'hw_shape == (height, width) == (num_rows, num_columns)'
    return (len(mx), len(mx[0]))

def vec5mx_at_(j, mx, /):
    return tuple(row[j] for row in mx)





def neg_if_odd_(k, v, /):
    '-> (-1)**k * v'
    return -v if k&1 else v
def mk_mx__ij2v_(num_rows, num_columns, ij2v_, /):
    assert num_rows > 0
    assert num_columns > 0
    return tuple(tuple(ij2v_(i, j) for j in range(num_columns)) for i in range(num_rows))
def remove_cross5mx_(jrow, jcolumn, mx, /):
    (num_rows, num_columns) = mx2hw_shape_(mx)
    assert 0 <= jrow < num_rows
    assert 0 <= jcolumn < num_columns
    return mk_mx__ij2v_(num_rows-1, num_columns-1, lambda i,j,/:mx[i+(i>=jrow)][j+(j>=jcolumn)])
def remove_column5mx_(jcolumn, mx, /):
    (num_rows, num_columns) = mx2hw_shape_(mx)
    assert 0 <= jcolumn < num_columns
    return mk_mx__ij2v_(num_rows, num_columns-1, lambda i,j,/:mx[i][j+(j>=jcolumn)])
def remove_row5mx_(jrow, mx, /):
    (num_rows, num_columns) = mx2hw_shape_(mx)
    assert 0 <= jrow < num_rows
    return tuple(mk_tuple(row) for i,row in enumerate(mx) if not i == jrow)
def slow__companion_mx_(mx, /):
    (num_rows, num_columns) = mx2hw_shape_(mx)
    assert num_rows == num_columns > 0
    if num_rows == 1:
        [[v]] = mx
        return ((v,),)
    return mk_mx__ij2v_(num_rows, num_columns, lambda i,j,/:neg_if_odd_(i+j, slow__determinant5mx_(remove_cross5mx_(i,j,mx))))

def slow__determinant5mx_(mx, /):
    (num_rows, num_columns) = mx2hw_shape_(mx)
    assert num_rows == num_columns > 0
    if num_rows == 1:
        [[v]] = mx
        return v
    _mx = remove_column5mx_(0,mx)
    return sum(mx[i][0]*neg_if_odd_(i, slow__determinant5mx_(remove_row5mx_(i,_mx))) for i in range(num_rows))
def slow__inv_mx_(mx, /):
    companion_mx = slow__companion_mx_(mx)
    det = mul_vec_(mx[0], companion_mx[0])
    (num_rows, num_columns) = mx2hw_shape_(mx)
    inv_mx = mk_mx__ij2v_(num_rows, num_columns, lambda i,j,/:companion_mx[j][i]/det)
    return inv_mx


def add_mx_(lhs_mx, rhs_mx, /):
    (num_rows, num_columns) = mx2hw_shape_(lhs_mx)
    assert (num_rows, num_columns) == mx2hw_shape_(rhs_mx)
    return mk_mx__ij2v_(num_rows, num_columns, lambda i,j,/:lhs_mx[i][j]+rhs_mx[i][j])
def sub_mx_(lhs_mx, rhs_mx, /):
    (num_rows, num_columns) = mx2hw_shape_(lhs_mx)
    assert (num_rows, num_columns) == mx2hw_shape_(rhs_mx)
    return mk_mx__ij2v_(num_rows, num_columns, lambda i,j,/:lhs_mx[i][j]-rhs_mx[i][j])
def add_vec_(lhs_vec, rhs_vec, /):
    assert len(lhs_vec) == len(rhs_vec)
    return tuple(a+b for a,b in zip(lhs_vec, rhs_vec))
def sub_vec_(lhs_vec, rhs_vec, /):
    assert len(lhs_vec) == len(rhs_vec)
    return tuple(a-b for a,b in zip(lhs_vec, rhs_vec))

def vec2square_geo_length_(vec, /):
    return mul_vec_(vec, vec)
def square_geo_distance_(lhs_vec, rhs_vec, /):
    return vec2square_geo_length_(sub_vec_(lhs_vec, rhs_vec))


def mk_eye_mx_(num_rows, num_columns=None, /):
    #assert num_rows > 0
    if num_columns is None:
        num_columns = num_rows
    return mk_mx__ij2v_(num_rows, num_columns, __eq__)
eye_mx_3x3 = mk_eye_mx_(3)
assert eye_mx_3x3 == ((1,0,0),(0,1,0),(0,0,1))


__all__
#lazy_import4funcs_('seed.math.matrix.naive_mx__tuple_tuple', '', __name__)
from seed.math.matrix.naive_mx__tuple_tuple import mk_mx__ij2v_, mx5scanline_per_, mx5vec_, mk_eye_mx_, eye_mx_3x3

from seed.math.matrix.naive_mx__tuple_tuple import mx2hw_shape_, mx2scanline_, vec5mx_at_, vec2square_geo_length_, square_geo_distance_

from seed.math.matrix.naive_mx__tuple_tuple import transpose_mx_, remove_cross5mx_, remove_column5mx_, remove_row5mx_

from seed.math.matrix.naive_mx__tuple_tuple import mul_vec_, mul_mx_, mul_mx_vec_, scale_vec_, scale_mx_, add_mx_, sub_mx_, add_vec_, sub_vec_

from seed.math.matrix.naive_mx__tuple_tuple import inv_mx_2x2_, inv_mx_3x3_

from seed.math.matrix.naive_mx__tuple_tuple import slow__companion_mx_, slow__determinant5mx_, slow__inv_mx_


from seed.math.matrix.naive_mx__tuple_tuple import *
