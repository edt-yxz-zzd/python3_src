#__all__:goto
#LinearInequationSolverOverRealNumber:TODO
r'''
e ../../python3_src/seed/math/matrix/solve_matrix.py
seed.math.matrix.solve_matrix
py -m seed.math.matrix.solve_matrix
py -m nn_ns.app.debug_cmd   seed.math.matrix.solve_matrix -x
from seed.math.matrix.solve_matrix import NoRowMatrix, linear_solver, ring_ex_ops__Fraction

used in:
    seed.algo.page_rank




[[[

>>> from seed.math.matrix.solve_matrix import NoRowMatrix, linear_solver, ring_ex_ops__Fraction

>>> from functools import partial
>>> solve = partial(linear_solver.solve_equations__matrix__to_representative_solutions, ring_ex_ops__Fraction, validate=True)
>>> invL_tm = partial(linear_solver.invL__matrix__tmay_arbitrary, ring_ex_ops__Fraction, validate=True)
>>> invR_tm = partial(linear_solver.invR__matrix__tmay_arbitrary, ring_ex_ops__Fraction, validate=True)
>>> inv_tm = partial(linear_solver.inv__matrix__tmay, ring_ex_ops__Fraction, validate=True)
>>> fr = Fraction

>>> mx_0_0 = NoRowMatrix(0)
>>> mx_0_1 = NoRowMatrix(1)
>>> mx_1_0 = [[]]
>>> mx_1_1 = [[fr(4)]]
>>> mx_2_1__bad = [[fr(4)], [fr(5)]]
>>> mx_2_1__ok = [[fr(4)], [fr(4)]]
>>> mx_1_2__bad = [[fr(4), fr(5)]]
>>> mx_1_2__ok = [[fr(4), fr(4)]]

>>> mx_1_1__zeros = [[fr(0)]]
>>> mx_2_1__zeros = [[fr(0)], [fr(0)]]
>>> mx_1_2__zeros = [[fr(0), fr(0)]]

>>> inv_tm(mx_0_0)
(NoRowMatrix(0),)
>>> inv_tm(mx_1_1)
([[Fraction(1, 4)]],)


>>> inv_tm(mx_0_1) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
DataDimensionalError
>>> invL_tm(mx_0_1) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
NonInvertibleError
>>> invR_tm(mx_0_1)
([[]],)

>>> inv_tm(mx_1_0) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
DataDimensionalError
>>> invL_tm(mx_1_0)
(NoRowMatrix(1),)
>>> invR_tm(mx_1_0) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
NonInvertibleError



>>> invR_tm(mx_1_2__ok)
([[Fraction(1, 4)], [Fraction(0, 1)]],)
>>> invL_tm(mx_2_1__ok)
([[Fraction(1, 4), Fraction(0, 1)]],)


>>> invR_tm(mx_1_2__bad)
([[Fraction(1, 4)], [Fraction(0, 1)]],)
>>> invL_tm(mx_2_1__bad)
([[Fraction(1, 4), Fraction(0, 1)]],)


>>> inv_tm(mx_1_1__zeros)
()
>>> invR_tm(mx_1_2__zeros)
()
>>> invL_tm(mx_2_1__zeros)
()




>>> solve(mx_2_1__bad, mx_2_1__ok)
[]
>>> solve(mx_2_1__ok, mx_2_1__bad)
[]
>>> solve(mx_2_1__bad, mx_2_1__bad)
[[[Fraction(1, 1)]]]
>>> solve(mx_2_1__ok, mx_2_1__ok)
[[[Fraction(1, 1)]]]

>>> solve(mx_1_2__bad, mx_1_2__ok)
[[[Fraction(1, 1), Fraction(1, 1)], [Fraction(0, 1), Fraction(0, 1)]], [[Fraction(-1, 4), Fraction(1, 1)], [Fraction(1, 1), Fraction(0, 1)]], [[Fraction(1, 1), Fraction(-1, 4)], [Fraction(0, 1), Fraction(1, 1)]]]
>>> solve(mx_1_2__ok, mx_1_2__bad)
[[[Fraction(1, 1), Fraction(5, 4)], [Fraction(0, 1), Fraction(0, 1)]], [[Fraction(0, 1), Fraction(5, 4)], [Fraction(1, 1), Fraction(0, 1)]], [[Fraction(1, 1), Fraction(1, 4)], [Fraction(0, 1), Fraction(1, 1)]]]
>>> solve(mx_1_2__bad, mx_1_2__bad)
[[[Fraction(1, 1), Fraction(5, 4)], [Fraction(0, 1), Fraction(0, 1)]], [[Fraction(-1, 4), Fraction(5, 4)], [Fraction(1, 1), Fraction(0, 1)]], [[Fraction(1, 1), Fraction(0, 1)], [Fraction(0, 1), Fraction(1, 1)]]]
>>> solve(mx_1_2__ok, mx_1_2__ok)
[[[Fraction(1, 1), Fraction(1, 1)], [Fraction(0, 1), Fraction(0, 1)]], [[Fraction(0, 1), Fraction(1, 1)], [Fraction(1, 1), Fraction(0, 1)]], [[Fraction(1, 1), Fraction(0, 1)], [Fraction(0, 1), Fraction(1, 1)]]]




>>> solve(mx_2_1__zeros, mx_2_1__ok)
[]
>>> solve(mx_2_1__zeros, mx_2_1__bad)
[]
>>> solve(mx_2_1__zeros, mx_2_1__zeros)
[[[Fraction(0, 1)]], [[Fraction(1, 1)]]]



>>> solve(mx_1_2__zeros, mx_1_2__ok)
[]
>>> solve(mx_1_2__zeros, mx_1_2__bad)
[]
>>> solve(mx_1_2__zeros, mx_1_2__zeros)
[[[Fraction(0, 1), Fraction(0, 1)], [Fraction(0, 1), Fraction(0, 1)]], [[Fraction(1, 1), Fraction(0, 1)], [Fraction(0, 1), Fraction(0, 1)]], [[Fraction(0, 1), Fraction(1, 1)], [Fraction(0, 1), Fraction(0, 1)]], [[Fraction(0, 1), Fraction(0, 1)], [Fraction(1, 1), Fraction(0, 1)]], [[Fraction(0, 1), Fraction(0, 1)], [Fraction(0, 1), Fraction(1, 1)]]]
>>> len(_) == 1+2*2
True









]]]


#'''
#################################
#HHHHH
__all__ = '''
    NoRowMatrix
    LinearEquationSolver
        linear_solver
    FractionRingExOps
        ring_ex_ops__Fraction
    BinaryFieldRingExOps
        ring_ex_ops__BinaryField




    NoRowMatrix
    BasicMatrixOps
        BasicOps4MatrixOverRing
            LinearEquationSolver
                linear_solver

    ValidateFailure
    DataDimensionalError
    MatrixPivotFailure
    EmplaceUpdateWithSameObjsError
    TypeError__not_mx_up1
    TypeError__not_mx_up1__solid_square
    TypeError__not_mx_low
    TypeError__not_swap_list


    list_reversed
    '''.split()
            #LinearInequationSolverOverRealNumber
    #InequalitySign
    #total_inequality_signs
    #all_inequality_signs
    #sorted_inequality_signs

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from fractions import Fraction
from operator import is_
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import echo, fst
from seed.tiny import print_err#, mk_fprint, mk_assert_eq_f, expectError
from seed.tiny import check_callable, check_uint, check_tmay, check_type_is
from seed.tiny import curry1
from seed.helper.repr_input import repr_helper
from seed.seq_tools.lsls52ls import sizes_to_ground_idx2super_idx_inner_idx_pair, sizes_to_ground_idx2super_idx, sizes_to_super_idx2ground_offset
from functools import reduce
from seed.math.IRingOps import (
    NonInvertibleError
    ,IRingOps
        ,IRingExOps
            ,BinaryFieldRingExOps
                ,ring_ex_ops__BinaryField
        ,IRingOpsOverRealNumber
            ,IRingExOpsOverRealNumber
        ,IPyRingOps
            ,IPyRingExOps
            ,IPyRingOpsOverRealNumber
                ,IPyRingExOpsOverRealNumber
                    ,FractionRingExOps
                        ,ring_ex_ops__Fraction
                ,IntegerRingOps
    )


___end_mark_of_excluded_global_names__0___ = ...


#HHHHH
def list_reversed(reverseable, /):
    return [*reversed(reverseable)]











class NoRowMatrix(int):
    __slots__ = ()
    def __init__(sf, /, *args, **kwargs):
        #bug:super().__init__(*args, **kwargs)
        super().__init__()
        if int(sf) < 0: raise TypeError
    def get_num_rows(sf, /):
        return 0
    def get_num_columns(sf, /):
        return int(sf)
    def __getitem__(sf, k, /):
        return [][k]
    def __bool__(sf, /):
        return False
    def __len__(sf, /):
        return 0
    def __iter__(sf, /):
        return;yield
    def __reversed__(sf, /):
        return;yield
    def __repr__(sf, /):
        return repr_helper(sf, int(sf))


class ValidateFailure(AssertionError):pass
    #validate
#class NonInvertibleError(ZeroDivisionError):pass
    #invertible
class DataDimensionalError(ArithmeticError):pass
class MatrixPivotFailure(ArithmeticError):pass

class EmplaceUpdateWithSameObjsError(Exception):pass
    #('emplace update but objs are not distinguish')
class TypeError__not_mx_up1(TypeError):pass
class TypeError__not_mx_up1__solid_square(TypeError__not_mx_up1):pass
class TypeError__not_mx_low(TypeError):pass
class TypeError__not_swap_list(TypeError):pass



class BasicMatrixOps(ABC):
    __slots__ = ()
    #@staticmethod
    @classmethod
    def convert_matrix__emplace_(cls, may_convert_element, mx, /):
        cls.convert_matrixT__emplace(may_convert_element)(mx)
    #@staticmethod
    @classmethod
    def convert_matrixT__emplace(cls, may_convert_element, /):
        if may_convert_element is None or may_convert_element is echo:
            def convert_matrix__emplace(mx, /):
                pass
        else:
            convert_element = may_convert_element
            check_callable(convert_element)
            def convert_matrix__emplace(mx, /):
                for row in mx:
                    for i in range(len(row)):
                        row[i] = convert_element(i)
        return convert_matrix__emplace


    def get_matrix_shape(sf, mx, /):
        M = len(mx)
        if not M:
            N = mx.get_num_columns()
            check_uint(N)
        else:
            N = len(mx[0])
        return M, N
    def check_matrix_shape(sf, M, N, mx, /):
        if not len(mx) == M:raise DataDimensionalError
        if M:
            if not {*map(len, mx)} == {N}:raise DataDimensionalError
        else:
            if not mx.get_num_columns() == N:raise DataDimensionalError
    def get_and_check_matrix_shape(sf, mx, /):
        M, N = sf.get_matrix_shape(mx)
        sf.check_matrix_shape(M, N, mx)
        return M, N

    #def copy_matrix__list(sf, mx, /):
    def copy_matrix__list__NoRowMatrix(sf, mx, /):
        M, N = sf.get_and_check_matrix_shape(mx)
        if not mx:
            if type(mx) is not NoRowMatrix:
                mx = NoRowMatrix(mx.get_num_columns())
        else:
            mx = [*map(list, mx)]
        sf.check_matrix_shape(M, N, mx)
        return mx


    def join__matrix(sf, num_rows_ls, num_cols_ls, super_mx, /, *, validate):
        len(num_rows_ls)
        len(num_cols_ls)
        sM, sN = len(num_rows_ls), len(num_cols_ls)
        gM, gN = sum(num_rows_ls), sum(num_cols_ls)

        sf.check_matrix_shape(sM, sN, super_mx)
        for i, num_rows in enumerate(num_rows_ls):
            for j, num_cols in enumerate(num_cols_ls):
                sf.check_matrix_shape(num_rows, num_cols, super_mx[i][j])
        ##end-check

        gi2si_ni = sizes_to_ground_idx2super_idx_inner_idx_pair(num_rows_ls)
        gj2sj_nj = sizes_to_ground_idx2super_idx_inner_idx_pair(num_cols_ls)

        def ij2v(gi, gj, /):
            si, ni = gi2si_ni[gi]
            sj, nj = gj2sj_nj[gj]
            return super_mx[si][sj][ni][nj]

        ground_mx = sf.mk_matrix__ij2v(gM, gN, ij2v)
        if validate:
            if not sf.eq__matrix_(curry1(sf.eq__matrix_, is_), super_mx, sf.split__matrix(num_rows_ls, num_cols_ls, ground_mx, validate=False)):raise ValidateFailure
        return ground_mx

    def split__matrix(sf, num_rows_ls, num_cols_ls, ground_mx, /, *, validate):
        len(num_rows_ls)
        len(num_cols_ls)
        sM, sN = len(num_rows_ls), len(num_cols_ls)
        gM, gN = sum(num_rows_ls), sum(num_cols_ls)
        sf.check_matrix_shape(gM, gN, ground_mx)
        ##end-check
        si2gi0 = sizes_to_super_idx2ground_offset(num_rows_ls)
        sj2gj0 = sizes_to_super_idx2ground_offset(num_cols_ls)

        def ij2v(si, sj, /):
            gi0 = si2gi0[si]
            gj0 = sj2gj0[sj]
            num_rows = num_rows_ls[si]
            num_cols = num_cols_ls[sj]

            def ij2v(ni, nj, /):
                gi = gi0 + ni
                gj = gj0 + nj
                return ground_mx[gi][gj]

            inner_mx = sf.mk_matrix__ij2v(num_rows, num_cols, ij2v)
            return inner_mx

        super_mx = sf.mk_matrix__ij2v(sM, sN, ij2v)

        if validate:
            if not sf.eq__matrix_(is_, ground_mx, sf.join__matrix(num_rows_ls, num_cols_ls, super_mx, validate=False)):raise ValidateFailure
        return super_mx

    def mk_matrix__using_NoRowMatrix(sf, num_rows, num_cols, mk_matrix_on_nonzero_num_rows, /, *args, **kwargs):
        check_uint(num_rows)
        check_uint(num_cols)
        check_callable(mk_matrix_on_nonzero_num_rows)
        if not num_rows:
            mx = NoRowMatrix(num_cols)
        else:
            mx = mk_matrix_on_nonzero_num_rows(num_rows, num_cols, *args, **kwargs)
        sf.check_matrix_shape(num_rows, num_cols, mx)
        return mx

    def mk_matrix__ij2v(sf, num_rows, num_cols, ij2v, /):
        check_callable(ij2v)
        return sf.mk_matrix__using_NoRowMatrix(num_rows, num_cols, sf._mk_matrix__ij2v_, ij2v)
    def _mk_matrix__ij2v_(sf, num_rows, num_cols, ij2v, /):
        return [[ij2v(i,j) for j in range(num_cols)] for i in range(num_rows)]
    def mk_matrix__repeat_row(sf, num_rows, num_cols, row, /, *, copy_row):
        if type(copy_row) is bool:
            copy_row = list if copy_row else echo
        check_callable(copy_row)
        if not len(row)==num_cols: raise DataDimensionalError
        return sf.mk_matrix__using_NoRowMatrix(num_rows, num_cols, sf._mk_matrix__repeat_row_, row, copy_row=copy_row)
    def _mk_matrix__repeat_row_(sf, num_rows, num_cols, row, /, *, copy_row):
        return [copy_row(row) for _ in range(num_rows)]
    def mk_matrix__default(sf, num_rows, num_cols, default, /):
        return sf.mk_matrix__using_NoRowMatrix(num_rows, num_cols, sf._mk_matrix__default_, default)
    def _mk_matrix__default_(sf, num_rows, num_cols, default, /):
        return [[default]*num_cols for _ in range(num_rows)]



    def mk_matrix__diagonal(sf, num_rows, num_cols, zero, diagonal_elements, /):
        '-> diagonalmx<M,N>'
        if not len(diagonal_elements) == min(num_rows, num_cols):raise DataDimensionalError
        diagonal_elements[:0]
        return sf.mk_matrix__using_NoRowMatrix(num_rows, num_cols, sf._mk_matrix__diagonal_, zero, diagonal_elements)
    def _mk_matrix__diagonal_(sf, num_rows, num_cols, zero, diagonal_elements, /):
        return sf.mk_matrix__ij2v(num_rows, num_cols, lambda i,j,/: diagonal_elements[i] if i==j else zero)

    def mk_matrix__echo_(sf, num_rows, num_cols, zero, one, /):
        '-> echo_mx<M,N>'
        return sf.mk_matrix__using_NoRowMatrix(num_rows, num_cols, sf._mk_matrix__echo_, zero, one)
    def _mk_matrix__echo_(sf, num_rows, num_cols, zero, one, /):
        return sf.mk_matrix__ij2v(num_rows, num_cols, lambda i,j,/: one if i==j else zero)

    def transpose__matrix(sf, mx, /):
        M, N = sf.get_and_check_matrix_shape(mx)
        return sf.mk_matrix__ij2v(N, M, lambda i,j,/:mx[j][i])

    def eq__row_(sf, eq__element, lhs_row, rhs_row, /):
        if not len(lhs_row) == len(rhs_row): raise DataDimensionalError
        return all(map(eq__element, lhs_row, rhs_row))
    def eq__matrix_(sf, eq__element, lhs_mx, rhs_mx, /):
        #NOTE:NoRowMatrix
        #bug:return len(lhs_mx) == len(rhs_mx) and all(sf.eq__row_(eq__element, lhs_row, rhs_row) for lhs_row, rhs_row in zip(lhs_mx, rhs_mx))
        MN = sf.get_and_check_matrix_shape(lhs_mx)
        _MN = sf.get_and_check_matrix_shape(rhs_mx)
        if not MN == _MN: raise DataDimensionalError
        return all(map(curry1(sf.eq__row_, eq__element), lhs_mx, rhs_mx))

    def map4matrix__element_wise_op(sf, element_wise_op, head_mx, /, *mx_ls):
        M, N = sf.get_and_check_matrix_shape(head_mx)
        for mx in mx_ls:
            sf.check_matrix_shape(M, N, mx)
        check_callable(element_wise_op)
        op = element_wise_op
        def ij2v(i, j, /):
            return op(head_mx[i][j], *(mx[i][j] for mx in mx_ls))
        return sf.mk_matrix__ij2v(M, N, ij2v)
    def map4row__element_wise_op(sf, element_wise_op, head_row, /, *row_ls):
        N = len(head_row)
        for row in row_ls:
            if not N == len(row):raise DataDimensionalError
        check_callable(element_wise_op)
        op = element_wise_op
        return [*map(op, head_row, *row_ls)]



    def iapply_swap_list_to_swap_rows__emplace(sf, swap_list, mx, /, *, emplace):
        '-> mx # swap_list comes from LinearEquationSolver.mk_matrix_mx_up1__emplace'
        sf.check_swap_list(swap_list)

        if not emplace:
            mx = sf.copy_matrix__list__NoRowMatrix(mx)
        for i, ii in swap_list:
            mx[i], mx[ii] = mx[ii], mx[i]
        return mx



    def check_swap_list(sf, swap_list, /):
        if 1:
            #uint_pairs
            len(swap_list)
            swap_list[:0]
            if not {*map(len, swap_list)} <= {2}:raise TypeError__not_swap_list
            fsts = [*map(fst, swap_list)]
            for i, ii in swap_list:
                check_uint(i)
                check_uint(ii)

        fsts
        if 1:
            #sorted strict.fst
            if not fsts == sorted(fsts):raise TypeError__not_swap_list
            if not len({*fsts}) == len(fsts):raise TypeError__not_swap_list
        if 1:
            #sorted strict.pair
            for i, ii in swap_list:
                if not i < ii:raise TypeError__not_swap_list




class BasicOps4MatrixOverRing(BasicMatrixOps):
    'matrix<M,N, a> :: [[a]{len=N}]{len=M} if M>0 else NoRowMatrix<N>'
    __slots__ = ()
    def mk_matrix__echo(sf, num_rows, num_cols, ring_ops, /):
        zero = ring_ops.get_zero()
        one = ring_ops.get_one()
        return sf.mk_matrix__echo_(num_rows, num_cols, zero, one)
    def eq__row(sf, ring_ops, lhs_row, rhs_row, /):
        return sf.eq__row_(ring_ops.eq, lhs_row, rhs_row)
    def eq__matrix(sf, ring_ops, lhs_mx, rhs_mx, /):
        return sf.eq__matrix_(ring_ops.eq, lhs_mx, rhs_mx)

    def mul__row__inner_product(sf, ring_ops, lhs_row, rhs_row, /):
        if not len(lhs_row) == len(rhs_row):raise DataDimensionalError
        zero = ring_ops.get_zero()
        #if 0b1:print_err(lhs_row, rhs_row)
        return reduce(ring_ops.add, map(ring_ops.mul, lhs_row, rhs_row), zero)
    def mul__matrix(sf, ring_ops, lhs_mx, rhs_mx, /):
        M, N = sf.get_and_check_matrix_shape(lhs_mx)
        _N, K = sf.get_and_check_matrix_shape(rhs_mx)
        if not N == _N:raise DataDimensionalError
        def ij2v(i, j, /):
            lhs_row = lhs_mx[i]
            rhs_column = [row[j] for row in rhs_mx]
            return sf.mul__row__inner_product(ring_ops, lhs_row, rhs_column)
        return sf.mk_matrix__ij2v(M, K, ij2v)


    def add__row(sf, ring_ops, lhs_row, rhs_row, /):
        return sf.map4row__element_wise_op(ring_ops.add, lhs_row, rhs_row)
        if not len(lhs_row) == len(rhs_row):raise DataDimensionalError
        return [*map(ring_ops.add, lhs_row, rhs_row)]
    def add__matrix(sf, ring_ops, lhs_mx, rhs_mx, /):
        return sf.map4matrix__element_wise_op(ring_ops.add, lhs_mx, rhs_mx)
        if not len(lhs_mx) == len(rhs_mx):raise DataDimensionalError
        return [*map(sf.add__row, [ring_ops]*len(lhs_mx), lhs_mx, rhs_mx)]
    def scaleL__row(sf, ring_ops, lhs_scale, rhs_row, /):
        op = curry1(ring_ops.mul, lhs_scale)
        return sf.map4row__element_wise_op(op, rhs_row)
        return [ring_ops.mul(lhs_scale, rhs_x) for rhs_x in rhs_row]
    def scaleL__matrix(sf, ring_ops, lhs_scale, rhs_mx, /):
        op = curry1(ring_ops.mul, lhs_scale)
        return sf.map4matrix__element_wise_op(op, rhs_mx)
        return [sf.scaleL__row(ring_ops, lhs_scale, rhs_row) for rhs_row in rhs_mx]
    def neg__row(sf, ring_ops, row, /):
        op = ring_ops.neg
        return sf.map4row__element_wise_op(op, row)
    def neg__matrix(sf, ring_ops, mx, /):
        op = ring_ops.neg
        return sf.map4matrix__element_wise_op(op, mx)




    def check_mx_up1__solid_square(sf, ring_ops, mx_up1__solid_square, /):
        L, _L = sf.get_matrix_shape(mx_up1__solid_square)
        if not L==_L: raise DataDimensionalError
        if 0:
            sf.check_mx_up1(ring_ops, mx_up1__solid_square)
            if not all(ring_ops.is_one(mx_up1__solid_square[i][i]) for i in range(L)): raise TypeError__not_mx_up1__solid_square
            if not all(ring_ops.is_zero(mx_up1__solid_square[i][j]) for i in range(L) for j in range(i)): raise logic-err
        else:
            indentsL__strict = sf._check_and_calc_indentsL__strict5mx_up1(ring_ops, mx_up1__solid_square)
            if not indentsL__strict == [*range(L)]:raise TypeError__not_mx_up1__solid_square

    def check_mx_low(sf, ring_ops, mx_low, /):
        M, N = sf.get_and_check_matrix_shape(mx_low)
        if not all(ring_ops.is_zero(x) for i, row in enumerate(mx_low) for x in row[i+1:]): raise TypeError__not_mx_low
    def check_mx_up1(sf, ring_ops, mx_up1, /):
        indentsL__strict = sf._check_and_calc_indentsL__strict5mx_up1(ring_ops, mx_up1)
        return
    def _check_and_calc_indentsL__strict5mx_up1(sf, ring_ops, mx_up1, /):
        'mx_up1<M,N> -> indentsL__strict/[num_leading0s__followed1]/sorted__strict[uint%N]{len<=M}'
        M, N = sf.get_and_check_matrix_shape(mx_up1)
        def find_fst_nonzero(row, /):
            j = -1
            for j, x in enumerate(row):
                if not ring_ops.is_zero(x):
                    break
            else:
                j += 1
            return j

        if 1:
            indentsL = [*map(find_fst_nonzero, mx_up1)] #num_leading0s
            assert len(indentsL) == M
            if not indentsL == sorted(indentsL):raise TypeError__not_mx_up1 #sorted
            sz = M - indentsL.count(N)
            indentsL__strict = indentsL[:sz]
            if not len(indentsL__strict) == len({*indentsL__strict}): raise TypeError__not_mx_up1 #sorted__strict
            if not all(ring_ops.is_one(mx_up1[i][j]) for i, j in enumerate(indentsL__strict)): raise TypeError__not_mx_up1 # followed1
        return indentsL__strict



    def info5mx_up1(sf, ring_ops, mx_up1, /):
        r'''mx_up1 -> info4mx_up1/(M, N, L, icolumn2is_fixed, fixed_icolumns4unknown, free_icolumns4unknown, mx_up1__solid_square, coeff_matrix4free_vars)

        mx_up1 :: matrix<M,N>
        icolumn2is_fixed :: [bool]{len=N}
        fixed_icolumns4unknown :: sorted[uint%N]{len=L}
        free_icolumns4unknown :: sorted[uint%N]{len=N-L}
        icolumn2is_fixed <==> fixed_icolumns4unknown&free_icolumns4unknown

        mx_up1__solid_square :: matrix<L,L>
        coeff_matrix4free_vars :: matrix<L,N-L>

        =======
        =======

        [mx_up1*X == V][V <- matrix<M,K>] <==>:
            * [V[L:,:] =/= zeros(M-L, K)]:
                [no solution]
            * [V[L:,:] === zeros(M-L, K)]:
                [mx_up1__solid_square * X[*fixed_icolumns4unknown] === V[:L,:] + rhs_mx__ex4free_vars * X[*free_icolumns4unknown]]
                [X[*fixed_icolumns4unknown] === solve_equations__mx_up1__solid_square(mx_up1__solid_square, V[:L,:]) + coeff_matrix4free_vars * X[*free_icolumns4unknown]]
        #'''
        indentsL__strict = sf._check_and_calc_indentsL__strict5mx_up1(ring_ops, mx_up1)
        M, N = sf.get_matrix_shape(mx_up1)

        if 1:
            fixed_icolumns4unknown = indentsL__strict
            icolumn2is_fixed = [False]*N
            for j in fixed_icolumns4unknown:
                icolumn2is_fixed[j] = True
            free_icolumns4unknown = [j for j, is_fixed in enumerate(icolumn2is_fixed) if not is_fixed]
            assert len(fixed_icolumns4unknown)+len(free_icolumns4unknown) == N
            assert sorted([*fixed_icolumns4unknown, *free_icolumns4unknown]) == [*range(N)]
        icolumn2is_fixed
        fixed_icolumns4unknown
        free_icolumns4unknown



        L = len(fixed_icolumns4unknown)
        mx_up1__solid_square = sf.mk_matrix__ij2v(L, L, lambda i,j,/: mx_up1[i][fixed_icolumns4unknown[j]])
        rhs_mx__ex4free_vars = sf.mk_matrix__ij2v(L, N-L, lambda i,j,/: ring_ops.neg(mx_up1[i][free_icolumns4unknown[j]]))

        coeff_matrix4free_vars = sf.solve_equations__mx_up1__solid_square(ring_ops, mx_up1__solid_square, rhs_mx__ex4free_vars, validate=True)
        return (M, N, L, icolumn2is_fixed, fixed_icolumns4unknown, free_icolumns4unknown, mx_up1__solid_square, coeff_matrix4free_vars)



    def _solve_equations__mx_up1__solid_square_(sf, ring_ops, mx_up1__solid_square, rhs_mx, /):
        L, K = sf.get_matrix_shape(rhs_mx)

        #list_reversed(mx_up1__solid_square)
        if 1:
            #reverse order of unknowns
            reversed_mx_up1 = sf.mk_matrix__ij2v(L, L, lambda i,j,/:mx_up1__solid_square[L-1-i][L-1-j])
                # matrix<L,L>
            #vectors = sf.transpose__matrix(list_reversed(rhs_mx) if L else rhs_mx)
            vectors = sf.mk_matrix__ij2v(K, L, lambda i,j,/:rhs_mx[L-1-j][i])
                # [vector]
                # matrix<K, L>
        xss = []
            # to be matrix<K, L>
        for vector in vectors:
            xs = []
                # to be row<L>
            for i, row in enumerate(reversed_mx_up1):
                assert len(xs) == i
                # xs[i] := V[i] - ...
                xs.append(ring_ops.sub(vector[i], sf.mul__row__inner_product(ring_ops, row[:i], xs)))
            #bug:xss.append(xss)
            xss.append(xs)

        if 1:
            #reverse order of unknowns
            #X = list_reversed(sf.transpose__matrix(xss) if K else ...)
            X = sf.mk_matrix__ij2v(L, K, lambda i,j,/:xss[j][L-1-i])
        assert (L, K) == sf.get_and_check_matrix_shape(X)
        return X
    #def _solve_equations__mx_up1__solid_square_(sf, ring_ops, mx_up1__solid_square, rhs_mx, /):
    def solve_equations__mx_up1__solid_square(sf, ring_ops, mx_up1__solid_square, rhs_mx, /, *, validate):
        'mx_up1__solid_square<L, L, a> -> V/matrix<L, K, a> -> X/matrix<L, K, a> # [mx_up1__solid_square*X = V] ==>> X'
        L = len(mx_up1__solid_square)
        _L = len(rhs_mx)
        if not L == _L: raise DataDimensionalError
        #if L:
        if 1:
            M, N = sf.get_and_check_matrix_shape(mx_up1__solid_square)
            _M, K = sf.get_and_check_matrix_shape(rhs_mx)
            if not L == M == _M == N: raise DataDimensionalError
            del M, _M, N
            L, K
            sf.check_mx_up1__solid_square(ring_ops, mx_up1__solid_square)
            X = sf._solve_equations__mx_up1__solid_square_(ring_ops, mx_up1__solid_square, rhs_mx)
        else:
            raise ...
            #empty
            X = [] # sf.mk_matrix__default(0, 0, None)

        if validate:
            if not sf.eq__matrix(ring_ops, rhs_mx, sf.mul__matrix(ring_ops, mx_up1__solid_square, X)): raise ValidateFailure
        return X

    def solve_equations__info4mx_up1(sf, ring_ops, info4mx_up1, rhs_mx, /):
        r'''info4mx_up1 -> tmay solution # info4mx_up1 comes from info5mx_up1
        solution = (fixed_icolumns4unknown, partial_particular_solution, (coeff_matrix4free_vars, free_icolumns4unknown))

        [X[*fixed_icolumns4unknown] === solve_equations__mx_up1__solid_square(mx_up1__solid_square, V[:L,:]) + coeff_matrix4free_vars * X[*free_icolumns4unknown]]

        fixed_icolumns4unknown :: sorted[uint%N]{len=L}
        partial_particular_solution :: matrix<L,K>
            a_particular_solution :: matrix<N,K>
        coeff_matrix4free_vars :: matrix<L,N-L>
        free_icolumns4unknown :: sorted[uint%N]{len=N-L}
        #'''
        (M, N, L, icolumn2is_fixed, fixed_icolumns4unknown, free_icolumns4unknown, mx_up1__solid_square, coeff_matrix4free_vars) = info4mx_up1
        _M, K = sf.get_and_check_matrix_shape(rhs_mx)
        if not M == _M:raise DataDimensionalError
        if not 0 <= L <= min(M, N):raise DataDimensionalError
        if not all(ring_ops.is_zero(x) for row in rhs_mx[L:] for x in row):
            tmay_solution = ()
        else:
        #elif L:
            partial_particular_solution = sf.solve_equations__mx_up1__solid_square(ring_ops, mx_up1__solid_square, (rhs_mx[:L] if L else NoRowMatrix(K)), validate=True)
            solution = (fixed_icolumns4unknown, partial_particular_solution, (coeff_matrix4free_vars, free_icolumns4unknown))
            tmay_solution = (solution,)
        return tmay_solution
    def is_solution_unique(sf, solution, /):
        'solution -> is_unique/bool'
        (fixed_icolumns4unknown, partial_particular_solution, (coeff_matrix4free_vars, free_icolumns4unknown)) = solution
        return not free_icolumns4unknown

    def solution2a_particular_solution(sf, ring_ops, solution, /, *, may_setting4free_unknowns):
        'solution -> a_particular_solution/matrix<N,K>'
        (fixed_icolumns4unknown, partial_particular_solution, (coeff_matrix4free_vars, free_icolumns4unknown)) = solution
        L, K = sf.get_and_check_matrix_shape(partial_particular_solution)
        N = len(fixed_icolumns4unknown)+len(free_icolumns4unknown)
        sf.check_matrix_shape(L, N-L, coeff_matrix4free_vars)
        assert L == len(fixed_icolumns4unknown)

        zero = ring_ops.get_zero()
        if may_setting4free_unknowns is None:
            setting4free_unknowns = [zero]*(N-L)
        else:
            setting4free_unknowns = may_setting4free_unknowns
        if not len(setting4free_unknowns)==N-L: raise DataDimensionalError

        [offset4fixed] = sf.transpose__matrix(sf.mul__matrix(ring_ops, coeff_matrix4free_vars, sf.transpose__matrix([setting4free_unknowns])))
        #offset_mx = ([offset4fixed]*K)**T
        offset_mx = sf.transpose__matrix(sf.mk_matrix__repeat_row(K, L, offset4fixed, copy_row=False))
        offseted_partial_particular_solution = sf.add__matrix(ring_ops, offset_mx, partial_particular_solution)



        a_particular_solution = [None]*N if N else NoRowMatrix(K)
        for i, solution_row in zip(fixed_icolumns4unknown, offseted_partial_particular_solution):
            #a_particular_solution[i] = [*solution_row]
            a_particular_solution[i] = solution_row
        for i, v in zip(free_icolumns4unknown, setting4free_unknowns):
            a_particular_solution[i] = [v]*K
        if not all(solution_row is not None for solution_row in a_particular_solution): raise logic-err

        sf.check_matrix_shape(N, K, a_particular_solution)
        return a_particular_solution
    def solution2zero_space(sf, ring_ops, solution, /):
        'solution -> zero_space/matrix<N, N-L, a>'
        (fixed_icolumns4unknown, partial_particular_solution, (coeff_matrix4free_vars, free_icolumns4unknown)) = solution
        del partial_particular_solution
        N = len(fixed_icolumns4unknown)+len(free_icolumns4unknown)
        L = len(fixed_icolumns4unknown)
        sf.check_matrix_shape(L, N-L, coeff_matrix4free_vars)

        zero = ring_ops.get_zero()
        one = ring_ops.get_one()
        #zero_space = sf.mk_matrix__default(N, N-L, None)
        zero_space = [None]*N if N else NoRowMatrix(N-L)
        for idx4fixed_unknow, coeff_row in zip(fixed_icolumns4unknown, coeff_matrix4free_vars):
            zero_space[idx4fixed_unknow] = [*coeff_row]
        for idx4free_unknow in free_icolumns4unknown:
            zero_space[idx4free_unknow] = [one if i==idx4free_unknow else zero for i in free_icolumns4unknown]

        #assert all(x is not None for row in zero_space for x in row)
        if not all(row is not None for row in zero_space): raise logic-err
        sf.check_matrix_shape(N, N-L, zero_space)
        return zero_space

    def tmay_solution2iter_representative_solutions(sf, ring_ops, tmay_solution, /):
        '-> (Iter matrix<N,K,a>){total=0|1+(N-L)*K}'
        if tmay_solution:
            [solution] = tmay_solution
            a_particular_solution = sf.solution2a_particular_solution(ring_ops, solution, may_setting4free_unknowns=None)
            yield a_particular_solution
                # matrix<N,K>
            N, K = sf.get_matrix_shape(a_particular_solution)

            zero_space = sf.solution2zero_space(ring_ops, solution)
                # matrix<N,N-L>
            #bug:yield from sf.transpose__matrix(zero_space)
                # row<N>
            vectors = sf.transpose__matrix(zero_space)
            for vector in vectors:
                for j in range(K):
                    _particular_solution = sf.copy_matrix__list__NoRowMatrix(a_particular_solution)
                    for i, x in enumerate(vector):
                        _particular_solution[i][j] += x
                    yield _particular_solution
        return
    def tmay_solution2tmay_a_particular_solution(sf, ring_ops, tmay_solution, /, *, may_setting4free_unknowns):
        'tmay solution -> tmay a_particular_solution'
        if tmay_solution:
            [solution] = tmay_solution
            a_particular_solution = sf.solution2a_particular_solution(ring_ops, solution, may_setting4free_unknowns=may_setting4free_unknowns)
            tmay_a_particular_solution = (a_particular_solution,)
        else:
            tmay_a_particular_solution = ()
        return tmay_a_particular_solution







    def solve_equations__mx_up1(sf, ring_ops, mx_up1, rhs_mx, /, *, validate, may_info4mx_up1):
        'mx_up1<M, N, a> -> rhs_mx/V/matrix<M, K, a> -> tmay solution # [mx_up1*X = V] ==>> X<N,K>'
        if may_info4mx_up1 is None:
            info4mx_up1 = sf.info5mx_up1(ring_ops, mx_up1)
        else:
            info4mx_up1 = may_info4mx_up1

        tmay_solution = sf.solve_equations__info4mx_up1(ring_ops, info4mx_up1, rhs_mx)
        if validate:
            for a_particular_solution in sf.tmay_solution2iter_representative_solutions(ring_ops, tmay_solution):
                if not sf.eq__matrix(ring_ops, rhs_mx, sf.mul__matrix(ring_ops, mx_up1, a_particular_solution)):raise ValidateFailure
        return tmay_solution








class LinearEquationSolver(BasicOps4MatrixOverRing):
    __slots__ = ()
    def _mk_matrix_mx_up1__emplace_(sf, ring_ex_ops, lhs_mx, may_rhs_mx, /):
        "lhs_mx -> may rhs_mx -> tmay (mx_low, swap_list)&[emplace:lhs_mx-->lhs_mx'=mx_up1, rhs_mx-->rhs_mx'] #[lhs_mx is not rhs_mx]"
        def swap_row(i, ii, /):
            if i == ii:
                return
            if not i < ii: raise logic-err
            _swap_row(lhs_mx, i, ii)
            if swap_list is None:
                _swap_row(rhs_mx, i, ii)
            else:
                # original_rhs_mx === echo<M, M>
                # now:
                # rhs_mx[i:, i:] === echo<M-i, M-i>
                # swap<0,ii-i> * rhs_mx[i:, i:] === rhs_mx[i:, i:] * swap<0,ii-i>
                # swap<i,ii> * rhs_mx === rhs_mx * swap<i,ii>
                swap_list.append((i, ii))
        def _swap_row(mx, i, ii, /):
            mx[i], mx[ii] = mx[ii], mx[i]
        def scale_row_tail(i, j, coeff, /):
            _scale_row_tail(lhs_mx, i, j, coeff)
            _scale_row_tail(rhs_mx, i, 0, coeff)
        def _scale_row_tail(mx, i, j, coeff, /):
            row_i = mx[i]
            #bug:for jj in range(j, num_cols):
            for jj in range(j, len(row_i)):
                x = row_i[jj]
                row_i[jj] = ring_ex_ops.mul(x, coeff)
        def subtract_scale_row_tail(ii, i, j, coeff, /):
            _subtract_scale_row_tail(lhs_mx, ii, i, j, coeff)
            _subtract_scale_row_tail(rhs_mx, ii, i, 0, coeff)
        def _subtract_scale_row_tail(mx, ii, i, j, coeff, /):
            row_ii = mx[ii]
            row_i = mx[i]
            c = coeff
            #bug:for jj in range(j, num_cols):
            for jj in range(j, len(row_i)):
                x = row_ii[jj]
                y = row_i[jj]
                c_y = ring_ex_ops.mul(c, y)
                row_ii[jj] = ring_ex_ops.sub(x, c_y)

        zero = ring_ex_ops.get_zero()
        one = ring_ex_ops.get_one()
        M, N = sf.get_and_check_matrix_shape(lhs_mx)
        if may_rhs_mx is None:
            swap_list = []
            rhs_mx = sf.mk_matrix__echo(M, M, ring_ex_ops)
        else:
            swap_list = None
            rhs_mx = may_rhs_mx
        _M, K = sf.get_and_check_matrix_shape(rhs_mx)
        num_rows = M
        num_cols = N
        num_var_rows = N
        num_var_cols = K
        if not M == _M:raise DataDimensionalError
        if 0:
            if not M:raise DataDimensionalError
            if not N:raise DataDimensionalError
            if not K:pass
        i = j = 0
        while j < num_cols and i < num_rows:
            for ii in range(i, num_rows):
                pivot = lhs_mx[ii][j]
                tm = ring_ex_ops.inv__tmay(pivot)
                if tm:
                    [inv_pivot] = tm
                    break
            else:
                if not all(map(ring_ex_ops.is_zero,  (lhs_mx[ii][j] for ii in range(i, num_rows)))): raise MatrixPivotFailure('fail: below rows(include curr_row) at curr_column are all non_invertible and at least one non_zero_non_invertible')
                for ii in range(i, num_rows):
                    lhs_mx[ii][j] = zero
                j += 1
                continue
            ii, inv_pivot
            swap_row(i, ii)
            del ii

            ########
            if 1:
                #mx[i] /= mx[i][j]
                row_i = lhs_mx[i]
                row_i[j] = one
                scale_row_tail(i, j+1, inv_pivot)

            ########
            if 1:
                #mx[ii] -= mx[i] * mx[ii][j]
                for ii in range(i+1, num_rows):
                    row_ii = lhs_mx[ii]
                    coeff = row_ii[j]
                    row_ii[j] = zero
                    subtract_scale_row_tail(ii, i, j+1, coeff)
            ########
            i += 1
            j += 1
            ########
            ########
            ########
        #end-while
        mx_up1 = lhs_mx
        if swap_list is None:
            tmay_pair = ()
        else:
            mx_low = rhs_mx
            tmay_pair = ((mx_low, swap_list),)
        return tmay_pair
    #def _mk_matrix_mx_up1__emplace_(sf, ring_ex_ops, lhs_mx, rhs_mx, /):
    def mk_matrix_mx_up1__emplace(sf, ring_ex_ops, lhs_mx, may_rhs_mx, /, *, validate):
        r'''lhs_mx -> may rhs_mx -> tmay (mx_low, swap_list)&[emplace:lhs_mx-->lhs_mx'=mx_up1, rhs_mx-->rhs_mx'] #[lhs_mx may be rhs_mx]

        -> swap_list
        mx_up1 <-- lhs_mx
        rhs_mx' <-- rhs_mx if may_rhs_mx is not None
        result = () if may_rhs_mx is not None else ((mx_low, swap_list),)
        #'''
        if lhs_mx is may_rhs_mx: raise EmplaceUpdateWithSameObjsError #('emplace update but objs are not distinguish')
        tmay_pair = sf._mk_matrix_mx_up1__emplace_(ring_ex_ops, lhs_mx, may_rhs_mx)
        check_tmay(tmay_pair)

        if validate:
            mx_up1 = lhs_mx
            sf.check_mx_up1(ring_ex_ops, mx_up1)
            if tmay_pair:
                [(mx_low, swap_list)] = tmay_pair
                sf.check_mx_low(ring_ex_ops, mx_low)
                sf.check_swap_list(swap_list)
            else:
                [] = tmay_pair
        return tmay_pair
    #def mk_matrix_mx_up1__emplace(sf, ring_ex_ops, lhs_mx, rhs_mx, /):

    def mk_matrix_mx_up1(sf, ring_ex_ops, lhs_mx, may_rhs_mx, /, *, may_convert_element, emplace, validate):
        "ring_ex_ops -> lhs_mx -> may_rhs_mx -> (lhs_mx'/mx_up1, either/((False, (mx_low, swap_list)) if may_rhs_mx is None else (True, rhs_mx')))"
        if emplace and lhs_mx is may_rhs_mx: raise EmplaceUpdateWithSameObjsError

        if emplace:
            copy_mx = echo
        else:
            copy_mx = sf.copy_matrix__list__NoRowMatrix

        convert_mx__emplace = BasicMatrixOps.convert_matrixT__emplace(may_convert_element)

        def f(mx, /):
            mx = copy_mx(mx)
            convert_mx__emplace(mx)
            return mx
        if validate and not emplace and may_rhs_mx is None:
            saved_lhs_mx = lhs_mx
        lhs_mx = f(lhs_mx)
        if may_rhs_mx is not None:
            rhs_mx = may_rhs_mx
            rhs_mx = f(rhs_mx)
            may_rhs_mx = rhs_mx
        tmay_pair = sf.mk_matrix_mx_up1__emplace(ring_ex_ops, lhs_mx, may_rhs_mx, validate=validate)
        mx_up1 = lhs_mx
        if tmay_pair:
            [(mx_low, swap_list)] = tmay_pair
            either = (False, (mx_low, swap_list))
        else:
            [] = tmay_pair
            either = (True, rhs_mx)

        if validate and not emplace and may_rhs_mx is None:
            if not sf.eq__matrix(ring_ex_ops, mx_up1, sf.mul__matrix(ring_ex_ops, mx_low, sf.iapply_swap_list_to_swap_rows__emplace(swap_list, saved_lhs_mx, emplace=False))): raise ValidateFailure
        return (mx_up1, either)
    #def mk_matrix_mx_up1(sf, ring_ex_ops, lhs_mx, may_rhs_mx, /, *, may_convert_element, emplace, validate):

    def decompose_matrix__LU(sf, ring_ex_ops, mx, /, *, validate):
        r'''mx -> (mx_up1, mx_low, swap_list) #[mx_up1 === mx_low * to_matrix(swap_list) * mx]

        mx :: matrix<M,N>
        swap_list :: [(idx4row, idx4row)]
        mx_low :: matrix<M,M>
        mx_up1 :: matrix<M,N>

        * mx_up1:
            * [@i. ?j. [mx_up1[i]==[0]*j]or[mx_up1[i][:j]==[0]*j][mx_up1[i][j]==1]]
                row = regex"0*1.*"
            * [@i. @j. [[0 <= i < i+1 < mx_up1.num_rows][mx_up1[i][:j]==[0]*j] -->> [mx_up1[i+1][:j+1]==[0]*(j+1)]]]
                row[i]   = regex"0{n}1.*"
                row[i+1] = regex"0{n}0.*"
        * mx_low:
            row[i]   = regex".*[^0]0{mx_low.num_cols-1-i}"

        * [mx_low * apply<swap_list> * mx === mx_up1]
            [mx*X = V]:
                [mx_low*apply<swap_list>*mx*X = mx_low*apply<swap_list>*V]
                [mx_up1*X = mx_low*apply<swap_list>*V]
                [mx_up1*X = mx_low*iapply_swap_list_to_swap_rows__emplace(swap_list, V)]

        #'''
        M, N = sf.get_and_check_matrix_shape(mx)
        if 0:
            if not M:raise DataDimensionalError
            if not N:raise DataDimensionalError
        #allow M =/= N

        lhs_mx = mx
        may_rhs_mx = None
        (mx_up1, (_, (mx_low, swap_list))) = sf.mk_matrix_mx_up1(ring_ex_ops, lhs_mx, may_rhs_mx, may_convert_element=None, emplace=False, validate=False)
        if validate:
            sf.check_mx_up1(ring_ex_ops, mx_up1)
            sf.check_mx_low(ring_ex_ops, mx_low)
            sf.check_swap_list(swap_list)
            if not sf.eq__matrix(ring_ex_ops, mx_up1, sf.mul__matrix(ring_ex_ops, mx_low, sf.iapply_swap_list_to_swap_rows__emplace(swap_list, mx, emplace=False))): raise ValidateFailure

        return (mx_up1, mx_low, swap_list)
    #def decompose_matrix__LU(sf, ring_ex_ops, mx, /, *, may_convert_element):



    def _solve_equations__matrix_(sf, ring_ex_ops, lhs_mx, rhs_mx, /):
        (mx_up1, mx_low, swap_list) = sf.decompose_matrix__LU(ring_ex_ops, lhs_mx, validate=False)
        rhs_mx = sf.iapply_swap_list_to_swap_rows__emplace(swap_list, rhs_mx, emplace=False)
        rhs_mx = sf.mul__matrix(ring_ex_ops, mx_low, rhs_mx)
        tmay_solution = sf.solve_equations__mx_up1(ring_ex_ops, mx_up1, rhs_mx, may_info4mx_up1=None, validate=False)
        return tmay_solution
    def solve_equations__matrix__to_representative_solutions(sf, ring_ex_ops, lhs_mx, rhs_mx, /, *, validate):
        '-> representative_solutions/Array<(0|(1+(N-L)*K)), matrix<N,K> >'
        tmay_solution = sf.solve_equations__matrix(ring_ex_ops, lhs_mx, rhs_mx, validate=validate)
        representative_solutions = [*sf.tmay_solution2iter_representative_solutions(ring_ex_ops, tmay_solution)]
            #Array<(0|(1+(N-L)*K)), matrix<N,K> >
        return representative_solutions
    def solve_equations__matrix(sf, ring_ex_ops, lhs_mx, rhs_mx, /, *, validate):
        r'''lhs_mx/matrix<M, N, a> -> rhs_mx/matrix<M, K, a> -> tmay solution # [lhs_mx*X = rhs_mx] ==>> X<N,K>

        [mx_up1*X = mx_low*iapply_swap_list_to_swap_rows__emplace(swap_list, V)]
        #'''
        tmay_solution = sf._solve_equations__matrix_(ring_ex_ops, lhs_mx, rhs_mx)
        if validate:
            for a_particular_solution in sf.tmay_solution2iter_representative_solutions(ring_ex_ops, tmay_solution):
                if not sf.eq__matrix(ring_ex_ops, rhs_mx, sf.mul__matrix(ring_ex_ops, lhs_mx, a_particular_solution)):raise ValidateFailure

        return tmay_solution
    #def solve_equations__matrix(sf, ring_ex_ops, lhs_mx, rhs_mx, /, *, validate):



    def _invR__matrix__tmay_arbitrary_(sf, ring_ex_ops, mx, /):
        M, N = sf.get_matrix_shape(mx)
        #assert M <= N
        lhs_mx = mx
        rhs_mx = echo_mx__M_M = sf.mk_matrix__echo(M, M, ring_ex_ops)
            # rhs_mx :: matrix<M,M>
            # an_invR_mx :: matrix<N,M>
        tmay_solution = sf.solve_equations__matrix(ring_ex_ops, lhs_mx, rhs_mx, validate=False)
        tmay_a_particular_solution = sf.tmay_solution2tmay_a_particular_solution(ring_ex_ops, tmay_solution, may_setting4free_unknowns=None)

        tmay_an_invR_mx = tmay_a_particular_solution
        return tmay_an_invR_mx
    def invR__matrix__tmay_arbitrary(sf, ring_ex_ops, mx, /, *, validate):
        'mx<M  N> -> tmay an_invR_mx<N, M> # M<=N #  [mx * an_invR_mx === echo_mx<M,M>]'
        M, N = sf.get_and_check_matrix_shape(mx)

        if not M <= N:raise NonInvertibleError
        if 0:
            if not M:raise DataDimensionalError


        if 0:
            lhs_mx = sf.copy_matrix__list__NoRowMatrix(mx)
        else:
            lhs_mx = mx

        tmay_an_invR_mx = sf._invR__matrix__tmay_arbitrary_(ring_ex_ops, mx)
        check_tmay(tmay_an_invR_mx)

        if validate:
            # [echo_mx<M,M> === mx * an_invR_mx]
            if tmay_an_invR_mx:
                [an_invR_mx] = tmay_an_invR_mx
                sf.check_matrix_shape(N, M, an_invR_mx)

                echo_mx__M_M = sf.mk_matrix__echo(M, M, ring_ex_ops)
                if not sf.eq__matrix(ring_ex_ops, echo_mx__M_M, sf.mul__matrix(ring_ex_ops, mx, an_invR_mx)): raise ValidateFailure
        return tmay_an_invR_mx
    #def invR__matrix__tmay_arbitrary(sf, ring_ex_ops, mx, /, *, validate):



    def _invL__matrix__tmay_arbitrary_(sf, ring_ex_ops, mx, /):
        _mx = sf.transpose__matrix(mx)
        _tmay_an_invR_mx = sf.invR__matrix__tmay_arbitrary(ring_ex_ops, _mx, validate=False)
        if _tmay_an_invR_mx:
            [_an_invR_mx] = _tmay_an_invR_mx
            an_invL_mx = sf.transpose__matrix(_an_invR_mx)
            tmay_an_invL_mx = (an_invL_mx,)
        else:
            [] = _tmay_an_invR_mx
            tmay_an_invL_mx = ()
        return tmay_an_invL_mx

    def invL__matrix__tmay_arbitrary(sf, ring_ex_ops, mx, /, *, validate):
        'mx<M  N> -> tmay an_invL_mx<N, M> # M>=N #  [an_invL_mx * mx === echo_mx<N,N>]'
        M, N = sf.get_and_check_matrix_shape(mx)
        if not M >= N:raise NonInvertibleError
        if 0:
            if not M:raise DataDimensionalError

        tmay_an_invL_mx = sf._invL__matrix__tmay_arbitrary_(ring_ex_ops, mx)
        check_tmay(tmay_an_invL_mx)

        if validate:
            # [echo_mx<N,N> === an_invL_mx * mx]
            if tmay_an_invL_mx:
                [an_invL_mx] = tmay_an_invL_mx
                sf.check_matrix_shape(N, M, an_invL_mx)

                echo_mx__N_N = sf.mk_matrix__echo(N, N, ring_ex_ops)
                if not sf.eq__matrix(ring_ex_ops, echo_mx__N_N, sf.mul__matrix(ring_ex_ops, an_invL_mx, mx)): raise ValidateFailure
        return tmay_an_invL_mx
    #def invL__matrix__tmay_arbitrary(sf, ring_ex_ops, mx, /, *, validate):


    def inv__matrix__tmay(sf, ring_ex_ops, mx, /, *, validate):
        'mx<L  L> -> tmay inv_mx<L, L> # [inv_mx * mx === echo_mx<L,L> == mx * inv_mx]'
        L, _L = sf.get_and_check_matrix_shape(mx)
        if not L == _L:raise DataDimensionalError
        if 0:
            if not L:raise DataDimensionalError
        tmay_an_invR_mx = sf.invR__matrix__tmay_arbitrary(ring_ex_ops, mx, validate=False)
        tmay_inv_mx = tmay_an_invR_mx
            #unique

        if validate:
            # [echo_mx<L,L> === inv_mx * mx === mx * inv_mx]
            if tmay_inv_mx:
                [inv_mx] = tmay_inv_mx
                sf.check_matrix_shape(L, L, inv_mx)

                echo_mx__L_L = sf.mk_matrix__echo(L, L, ring_ex_ops)
                if not sf.eq__matrix(ring_ex_ops, echo_mx__L_L, sf.mul__matrix(ring_ex_ops, inv_mx, mx)): raise ValidateFailure
                if not sf.eq__matrix(ring_ex_ops, echo_mx__L_L, sf.mul__matrix(ring_ex_ops, mx, inv_mx)): raise ValidateFailure
        return tmay_inv_mx
    #def inv__matrix__tmay(sf, ring_ex_ops, mx, /, *, validate):



    #def solve_LU(sf, ring_ex_ops, lhs_mx, rhs_mx, /, *, may_convert_element, emplace):
    #def solve_LU__emplace(sf, ring_ex_ops, lhs_mx, rhs_mx, /):
#class LinearEquationSolver(ABC):
linear_solver = LinearEquationSolver()
ring_ex_ops__Fraction = FractionRingExOps()

from enum import IntEnum, auto, unique
@unique
class InequalitySign(IntEnum):
    # 6=2*3=(==/!=)*(?/</>)
    # start from EQ=0, sorted by name
    EQ = 0 # auto() #auto start from 1!!
    GE = auto()
    GT = auto()
    LE = auto()
    LT = auto()
    NE = auto()

total_inequality_signs = len(InequalitySign)
assert 0 == InequalitySign.EQ
range(total_inequality_signs)[InequalitySign.LE]

all_inequality_signs = set(InequalitySign)
sorted_inequality_signs = sorted(InequalitySign)
_sorted_inequality_signs = sorted(InequalitySign, key=lambda sgn:sgn.name)
assert sorted_inequality_signs == _sorted_inequality_signs
#print(sorted_inequality_signs)

r'''[[[
class LinearInequationSolverOverRealNumber(LinearEquationSolver):
    __slots__ = ()
    #def solve_equations__matrix
    #def _solve_equations__matrix_(sf, ring_ex_ops, lhs_mx, rhs_mx, /):
    def _solve_inequations__matrix_(sf, ring_ex_ops__real_number, lhs_mx, rhs_mx, irow2inequality_sign, /):
        (mx_up1, mx_low, swap_list) = sf.decompose_matrix__LU(ring_ex_ops, lhs_mx, validate=False)
        rhs_mx = sf.iapply_swap_list_to_swap_rows__emplace(swap_list, rhs_mx, emplace=False)
        rhs_mx = sf.mul__matrix(ring_ex_ops, mx_low, rhs_mx)
        tmay_solution = sf.solve_equations__mx_up1(ring_ex_ops, mx_up1, rhs_mx, may_info4mx_up1=None, validate=False)
        return tmay_solution
    def solve_inequations__matrix(sf, ring_ex_ops__real_number, lhs_mx, rhs_mx, irow2inequality_sign, /, *, validate):
        M, N = sf.get_and_check_matrix_shape(lhs_mx)
        _M, K = sf.get_and_check_matrix_shape(rhs_mx)
        if not M==_M: raise DataDimensionalError
        if not M==len(irow2inequality_sign): raise DataDimensionalError
        if not all(cls is InequalitySign for cls in map(type, irow2inequality_sign)):raise TypeError

        if 0:
            sgn2irows = [[] for _ in InequalitySign]
            for irow, inequality_sign in enumerate(irow2inequality_sign):
                sgn2irows[inequality_sign].append(irow)
            assert M == sum(map(len, sgn2irows))
            num_new_relax_unknowns = M - len(sgn2irows[InequalitySign.EQ])
            assert 0 == InequalitySign.EQ
            sizes = [*map(len, sgn2irows)]
            del sizes[InequalitySign.EQ]
            isgn2irelax_var_offset = sizes_to_super_idx2ground_offset(sizes)
            irelax_var2isgn_iinner_pair = sizes_to_ground_idx2super_idx_inner_idx_pair(sizes)

        #N+irelax_var==icolumn

        irelax_var2irow_sgn_pair = []
        #irow2may_irelax_var = [None]*M
        for irow, inequality_sign in enumerate(irow2inequality_sign):
            if not inequality_sign == InequalitySign.EQ
                irelax_var2irow_sgn_pair.append((irow, inequality_sign))
                #irow2may_irelax_var[irow] = irelax_var
        num_new_relax_unknowns = len(irelax_var2irow_sgn_pair)
        zero = ring_ex_ops.get_zero()
        one = ring_ex_ops.get_one()
        neg_one = ring_ex_ops.get_neg_one()
        sgn2coeff = dict.fromkeys(InequalitySign, one)
        del sgn2coeff[InequalitySign.EQ]
        sgn2coeff[InequalitySign.GT] = neg_one
        sgn2coeff[InequalitySign.GE] = neg_one
        def ij2v(i, j, /):
            _irow = i
            irelax_var = j
            irow, sgn = irelax_var2irow_sgn_pair[irelax_var]
            if not irow == _irow:
                return zero
            else:
                coeff = sgn2coeff[sgn]
                return coeff
        coeff_mx4new_relax_vars = sf.mk_matrix__ij2v(M, num_new_relax_unknowns, ij2v)
        lhs_mx_ex = sf.join__matrix([M], [N, num_new_relax_unknowns], [[lhs_mx, coeff_mx4new_relax_vars]])
            # matrix<M, N+num_new_relax_unknowns>
        tmay_solution = sf.solve_equations__matrix(ring_ex_ops__real_number, lhs_mx_ex, rhs_mx, validate=validate)
        ... ...线性规划？
        . ...解结构是什么？


todo:MOVE OUT sizes_to_ground_idx2super_idx_inner_idx_pair...



        pass
        #......
'''#]]]'''

from seed.math.matrix.solve_matrix import NoRowMatrix, linear_solver, ring_ex_ops__Fraction, ring_ex_ops__BinaryField
from seed.math.matrix.solve_matrix import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()
