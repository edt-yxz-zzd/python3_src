#HHHHH
r'''
py -m seed.types.TriBoolOps

from seed.types.TriBoolOps import TriBoolOps
from seed.util_class.Lazy__call import Lazy


改动:
    TriBoolOps 更新 XNOR
        NXOR ---> XNOR
            标准名 由 NOT_XOR ---> XNOR

=====
同或 XNOR
    e others/数学/编程/术语/同或XNOR.txt
    异或 XOR = [is_odd total_1s]
    同或 XNOR = ???
      if = not $ fold XOR<2> =[is_even total_1s]
      if = fold XNOR<2> =[is_even total_0s]
      if = pairwise EQU<2> =[0 == total_0s]or[0 == total_1s]
    同或 XNOR/ENOR/ExNOR 同或门=异或非门
#'''

__all__ = '''
    TriBoolOps
    TriBoolOps__std_name_and_aliases
        LazyTriBoolOps
    '''.split()




import itertools
from seed.tiny import assert_eq, assert_eq_f, mk_assert_eq_f
from seed.util_class.Lazy__call import Lazy

#HHHHH
class TriBoolOps:
    r'''
    tri_bool :: TriBool = (False|True|...)

    NOT
    AND OR XOR~NOT_EQU

    XNOR=NOT_XOR~EQU
    NAND=NOT_AND
    NOR=NOT_OR
    IMPLY = OR_notL_idR
    FLIP_IMPLY = OR_idL_notR
    NOT_IMPLY = AND_idL_notR
    NOT_FLIP_IMPLY = FLIP_NOT_IMPLY = AND_notL_idR

1 vars bool ops: (out=T/F)**((in=T/F)**1) = 2**2**1 = 4
    need no vars:2
    need 1 var = remain 2
2 vars bool ops: (out=T/F)**((in=T/F)**2) = 2**2**2 = 16
    need no vars:2
    need 1 vars:(choose=L/R)*(1 var ops&need 1 var) = 2*(2**2-2) =4
    need both = remain 10:
        symmetry = 6:
            AND OR XOR
            NAND NOR XNOR
        asymmetry = 4:
            IMPLY  FLIP_IMPLY
            NOT_IMPLY  NOT_FLIP_IMPLY


2 vars tribool ops: 3**3**2 = 3**9 = 19683
    need no vars:3
    need 1 vars:(choose=L/R)*(1 var ops&need 1 var) = 2*(3**3-3) = 48
    need both = remain 19632
    required bool closoure:
        3**(3**2-2**2) * 2**(2**2) = 3888

    constraint: ... = [True|False]
        i.e. when input var is ..., input both, if output both then out is ...

    #'''
    @classmethod
    def is_bool(cls, x):
        return x is True or x is False
        return type(x) is bool
    @classmethod
    def is_tribool(cls, x):
        return x is ... or x is True or x is False
        return x is ... or cls.is_bool(x)
    @classmethod
    def NOT(cls, rhs):
        if rhs is ...:
            return ...
        if rhs is False:
            return True
        if rhs is True:
            return False
        raise TypeError
        return not rhs

    @classmethod
    def AND(cls, lhs, rhs):
        if lhs is False or rhs is False:
            return False
        if lhs is ... or rhs is ...:
            return ...
        if lhs is True is rhs:
            return True
        raise TypeError
    @classmethod
    def OR(cls, lhs, rhs):
        if lhs is True or rhs is True:
            return True
        if lhs is ... or rhs is ...:
            return ...
        if lhs is False is rhs:
            return False
        raise TypeError
    @classmethod
    def XOR(cls, lhs, rhs):
        if lhs is ... or rhs is ...:
            return ...
        if lhs is rhs:
            return False
        if lhs is True and rhs is False:
            return True
        if lhs is False and rhs is True:
            return True
        raise TypeError
    @classmethod
    def IMPLY(cls, lhs, rhs):
        if lhs is False or rhs is True:
            return True
        if lhs is ... or rhs is ...:
            return ...
        if lhs is True and rhs is False:
            return False
        raise TypeError
    @classmethod
    def FLIP_IMPLY(cls, lhs, rhs):
        return cls.IMPLY(rhs, lhs)
    @classmethod
    def NOT_FLIP_IMPLY(cls, lhs, rhs):
        return cls.NOT(cls.FLIP_IMPLY(lhs, rhs))
    @classmethod
    def NOT_IMPLY(cls, lhs, rhs):
        return cls.NOT(cls.IMPLY(lhs, rhs))
    @classmethod
    #def NOT_XOR(cls, lhs, rhs):
    def XNOR(cls, lhs, rhs):
        return cls.NOT(cls.XOR(lhs, rhs))
    @classmethod
    def NOT_OR(cls, lhs, rhs):
        return cls.NOT(cls.OR(lhs, rhs))
    @classmethod
    def NOT_AND(cls, lhs, rhs):
        return cls.NOT(cls.AND(lhs, rhs))
    #XNOR = NOT_XOR
    NOT_XOR = XNOR
    NOR = NOT_OR
    NAND = NOT_AND

    OR_notL_idR = IMPLY
    OR_idL_notR = FLIP_IMPLY
    AND_idL_notR = NOT_IMPLY
    AND_notL_idR = FLIP_NOT_IMPLY = NOT_FLIP_IMPLY


#HHHHH
class test_TriBool_binary_ops:
    #test bool by py op
    #test tribool by bool and constraint
    #test all tribool by assert output tables are all diff


    @classmethod
    def test_bool_by_py_op(cls, tribool_op, py_op):
        for x, y in  itertools.product([False, True], repeat=2):
            r = py_op(x, y)
            assert_eq_f(r, tribool_op, x, y)
    @classmethod
    def bools2tri(cls, bools):
        [a, *ls] = set(bools)
        return ... if ls else a
    @classmethod
    def tri2bools(cls, tribool):
        if tribool is ...:
            return (True, False)
        return (tribool,)
    @classmethod
    def test_tribool_by_bool_and_constraint(cls, tribool_op, py_op):

        for xy in  itertools.product([..., False, True], repeat=2):
            r = cls.bools2tri(py_op(a,b) for a, b in  itertools.product(*map(cls.tri2bools, xy)))
            assert_eq_f(r, tribool_op, *xy)

    @classmethod
    def mk_table_of_tribpol_binary_op(cls, tribool_op):
        d = {}
        for xy in  itertools.product([..., False, True], repeat=2):
            r = tribool_op(*xy)
            d[xy] = r
        return d

    @classmethod
    def test_all_tribool_by_assert_output_tables_are_all_diff(cls, all_tribool_ops):
        all_tribool_ops = tuple(all_tribool_ops)
        ls = tuple(frozenset(cls.mk_table_of_tribpol_binary_op(f).items()) for f in all_tribool_ops)
        ss = set(ls)
        assert_eq(len(ls), len(ss))
    @classmethod
    def get_all_xbool_ops(cls, T):
        x = T
        return (x.AND, x.OR, x.XOR, x.IMPLY, x.FLIP_IMPLY, x.NOT_AND, x.NOT_OR, x.XNOR, x.NOT_IMPLY, x.NOT_FLIP_IMPLY)
        #return (x.AND, x.OR, x.XOR, x.IMPLY, x.FLIP_IMPLY, x.NOT_AND, x.NOT_OR, x.NOT_XOR, x.NOT_IMPLY, x.NOT_FLIP_IMPLY)
    @classmethod
    def main_test(cls):
        T = TriBoolOps
        B = BoolOps
        all_tribool_ops = cls.get_all_xbool_ops(T)
        all_py_bool_ops = cls.get_all_xbool_ops(B)
        for tribool_op, py_op in zip(all_tribool_ops, all_py_bool_ops):
            cls.test_bool_by_py_op(tribool_op, py_op)
            cls.test_tribool_by_bool_and_constraint(tribool_op, py_op)
        cls.test_all_tribool_by_assert_output_tables_are_all_diff(all_tribool_ops)

#HHHHH
class BoolOps:
    @classmethod
    def NOT(cls, rhs):
        return not rhs
    @classmethod
    def AND(cls, lhs, rhs):
        return lhs and rhs
    @classmethod
    def OR(cls, lhs, rhs):
        return lhs or rhs
    @classmethod
    def XOR(cls, lhs, rhs):
        return lhs ^ rhs
    @classmethod
    def IMPLY(cls, lhs, rhs):
        return (not lhs) or rhs
    @classmethod
    def FLIP_IMPLY(cls, lhs, rhs):
        return lhs or (not rhs)
        return cls.IMPLY(rhs, lhs)
    @classmethod
    def NOT_FLIP_IMPLY(cls, lhs, rhs):
        return (not lhs) and rhs
        return cls.NOT(cls.FLIP_IMPLY(lhs, rhs))
    @classmethod
    def NOT_IMPLY(cls, lhs, rhs):
        return lhs and (not rhs)
        return cls.NOT(cls.IMPLY(lhs, rhs))
    @classmethod
    #def NOT_XOR(cls, lhs, rhs):
    def XNOR(cls, lhs, rhs):
        return lhs is rhs
        return cls.NOT(cls.XOR(lhs, rhs))
    @classmethod
    def NOT_OR(cls, lhs, rhs):
        return cls.NOT(cls.OR(lhs, rhs))
    @classmethod
    def NOT_AND(cls, lhs, rhs):
        return cls.NOT(cls.AND(lhs, rhs))
    #XNOR = NOT_XOR
    NOT_XOR = XNOR
    NOR = NOT_OR
    NAND = NOT_AND

    OR_notL_idR = IMPLY
    OR_idL_notR = FLIP_IMPLY
    AND_idL_notR = NOT_IMPLY
    AND_notL_idR = FLIP_NOT_IMPLY = NOT_FLIP_IMPLY

if __name__ == '__main__':
    test_TriBool_binary_ops.main_test()

#HHHHH
class TriBoolOps__std_name_and_aliases:
    r'''
    binary_tribool_op_alias2std_name
    binary_tribool_op_std_name2aliases
    #'''

    @classmethod
    def _mk_binary_tribool_op_alias2std_name_and_invert(cls):
        binary_tribool_op_std_name_and_aliases__lines = r'''
    AND
    OR
    XOR

    NOT_AND NAND
    NOT_OR  NOR
    XNOR NOT_XOR

    IMPLY       OR_notL_idR
    FLIP_IMPLY  OR_idL_notR
    NOT_IMPLY   AND_idL_notR
    NOT_FLIP_IMPLY FLIP_NOT_IMPLY AND_notL_idR
    #'''
    # NOT_XOR XNOR ---> XNOR NOT_XOR
        binary_tribool_op_std_name2aliases = {}
        binary_tribool_op_alias2std_name = d = {}
        lines = binary_tribool_op_std_name_and_aliases__lines.replace('#', '')
        for line in lines.split('\n'):
            line = line.strip()
            names = line.split()
            if names:
                std_name, *__aliases = names
                for alias in names:
                    #aliases include std_name
                    if alias in d: raise logic-err
                    d[alias] = std_name
                binary_tribool_op_std_name2aliases[std_name] = frozenset(names)
                    #aliases include std_name
        return binary_tribool_op_alias2std_name, binary_tribool_op_std_name2aliases
    #aliases include std_name
    [binary_tribool_op_alias2std_name
    ,binary_tribool_op_std_name2aliases
    ] = _mk_binary_tribool_op_alias2std_name_and_invert.__func__(None)


#HHHHH
class LazyTriBoolOps(TriBoolOps__std_name_and_aliases):
    r'''
    tri_bool :: TriBool = (False|True|...)
    foldl/foldr

    NOT

lhs/rhs-determine-value, foldl0/foldr0 init-value
    AND
        False/False
        True/True
    OR
        True/True
        False/False
    XOR
        .../...
        False/False

    XNOR=NOT_XOR
        .../...
        True/True
    NAND=NOT_AND
        False/False
        ?/? no-init-value
        foldl1/foldr1
    NOR=NOT_OR
        True/True
        ?/? no-init-value
        foldl1/foldr1
    IMPLY = OR_notL_idR
        (not lhs) or rhs
        False/True
        True/None
        (((True==>>x0)==>>x1)==>>...)
        !!! xxx (...==>>(x_2==>>(x_1==>>False)))
    FLIP_IMPLY = OR_idL_notR
        lhs or not rhs
        True/False
        None/True
    NOT_IMPLY = AND_idL_notR
        lhs and not rhs
        False/True
        None/False
    NOT_FLIP_IMPLY = FLIP_NOT_IMPLY = AND_notL_idR
        (not lhs) and rhs
        True/False
        False/None
    #'''
    @classmethod
    def _find_maybe_foldx0_start_value4tribool_op(cls, tribool_op, foldl0_or_foldr0:bool):
        'foldl0_or_foldr0: False-foldl0, True-foldr0'
        vs = (False, True, ...)
        ls = []
        for xhs in vs:
            rs = tuple(tribool_op(yhs, xhs) if foldl0_or_foldr0 else tribool_op(xhs, yhs) for yhs in vs)
            if rs == vs:
                ls.append(xhs)
        if not len(ls) <= 1: raise logic-err
        if ls:
            [maybe_foldx0_start_value] = ls
        else:
            maybe_foldx0_start_value = None
        return maybe_foldx0_start_value
    @classmethod
    def _find_tribool_op_xhs_determine_value_and_result(cls, tribool_op, lhs_or_rhs:bool):
        'lhs_or_rhs: False-lhs, True-rhs'
        vs = (False, True, ...)
        ps = []
        for xhs in vs:
            rs = {tribool_op(yhs, xhs) if lhs_or_rhs else tribool_op(xhs, yhs) for yhs in vs}
            if len(rs) == 1:
                [result4xhs_determine_value] = rs
                xhs_determine_value = xhs
                ps.append((xhs_determine_value, result4xhs_determine_value))
        if len(ps) != 1: raise logic-err
        [(xhs_determine_value, result4xhs_determine_value)] = ps
        return xhs_determine_value, result4xhs_determine_value
    @classmethod
    def _find_tribool_op_xhs_determine_value_and_result_and_maybe_foldx0_start_value(cls, tribool_op, left_or_right:bool):
        [xhs_determine_value, result4xhs_determine_value] = cls._find_tribool_op_xhs_determine_value_and_result(tribool_op, left_or_right)
        maybe_foldx0_start_value = cls._find_maybe_foldx0_start_value4tribool_op(tribool_op, left_or_right)
        return (xhs_determine_value, result4xhs_determine_value, maybe_foldx0_start_value)
    @classmethod
    def _mk_lazy_info4tribool_op(cls, tribool_op_name):
        'lazy_info = (std_name, (lhs_determine_value, result4lhs_determine_value, maybe_foldl0_start_value), (rhs_determine_value, result4rhs_determine_value, maybe_foldr0_start_value))'
        #name = tribool_op.__name__
        tribool_op = getattr(TriBoolOps, tribool_op_name)
        name = tribool_op_name
        std_name = cls.binary_tribool_op_alias2std_name[name]
        ls = [std_name]
        for left_or_right in (False, True):
            triple = cls._find_tribool_op_xhs_determine_value_and_result_and_maybe_foldx0_start_value(tribool_op, left_or_right)
            ls.append(triple)
        lazy_info = (*ls,)
        return lazy_info
    @classmethod
    def _mk_binary_tribool_op_std_name2lazy_info(cls):
        binary_tribool_op_std_name2lazy_info = d = {}
        X = TriBoolOps
        for std_name in cls.binary_tribool_op_std_name2aliases:
            #tribool_op = getattr(X, std_name)
            tribool_op_name = std_name
            lazy_info = cls._mk_lazy_info4tribool_op(tribool_op_name)
            assert lazy_info[0] == std_name
            d[std_name] = lazy_info

        return binary_tribool_op_std_name2lazy_info

    #binary_tribool_op_std_name2lazy_info = _mk_binary_tribool_op_std_name2lazy_info.__func__(TriBoolOps__std_name_and_aliases)
    dict(
        AND= ('AND', (False,False,True), (False,False,True))
        )

    @classmethod
    def _lazy_binary_tribool_op(cls, left_or_right_first, tribool_op_name, lazy_lhs, lazy_rhs):
        #name = tribool_op.__name__
        tribool_op = getattr(TriBoolOps, tribool_op_name)
        name = tribool_op_name
        std_name = cls.binary_tribool_op_alias2std_name[name]
        assert name == std_name or name in cls.binary_tribool_op_std_name2aliases[std_name]
        lazy_info = cls.binary_tribool_op_std_name2lazy_info[std_name]
        (_std_name, (lhs_determine_value, result4lhs_determine_value, maybe_foldl0_start_value), (rhs_determine_value, result4rhs_determine_value, maybe_foldr0_start_value)) = (_, lazy_infoL, lazy_infoR) = lazy_info
        assert _std_name == std_name
        if left_or_right_first:
            #right_first
            lazy_xhs = lazy_rhs
            lazy_yhs = lazy_lhs
            lazy_infoX = lazy_infoR
        else:
            #left_first
            lazy_xhs = lazy_lhs
            lazy_yhs = lazy_rhs
            lazy_infoX = lazy_infoL

        xhs = lazy_xhs()
        (xhs_determine_value, result4xhs_determine_value, maybe_foldx0_start_value) = lazy_infoX
        if xhs is xhs_determine_value:
            return result4xhs_determine_value
        else:
            yhs = lazy_yhs()
            return tribool_op(yhs, xhs) if left_or_right_first else tribool_op(xhs, yhs)

    @classmethod
    def _lazy_not(cls, lazy_rhs):
        return TriBoolOps.NOT(lazy_rhs())
    @classmethod
    def lazy_NOT(cls, lazy_rhs):
        return Lazy(cls._lazy_not, lazy_rhs)

    @classmethod
    def lazyL_AND(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'AND', lazy_lhs, lazy_rhs)
    @classmethod
    def lazyR_AND(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'AND', lazy_lhs, lazy_rhs)

    @classmethod
    def lazyL_OR(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'OR', lazy_lhs, lazy_rhs)
    @classmethod
    def lazyR_OR(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'OR', lazy_lhs, lazy_rhs)

    @classmethod
    def lazyL_XOR(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'XOR', lazy_lhs, lazy_rhs)
    @classmethod
    def lazyR_XOR(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'XOR', lazy_lhs, lazy_rhs)

    @classmethod
    def lazyL_NOT_AND(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'NOT_AND', lazy_lhs, lazy_rhs)
    @classmethod
    def lazyR_NOT_AND(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'NOT_AND', lazy_lhs, lazy_rhs)

    @classmethod
    def lazyL_NOT_OR(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'NOT_OR', lazy_lhs, lazy_rhs)
    @classmethod
    def lazyR_NOT_OR(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'NOT_OR', lazy_lhs, lazy_rhs)

    @classmethod
    #def lazyL_NOT_XOR(cls, lazy_lhs, lazy_rhs):
    def lazyL_XNOR(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'XNOR', lazy_lhs, lazy_rhs)
        #return Lazy(cls._lazy_binary_tribool_op, False, 'NOT_XOR', lazy_lhs, lazy_rhs)
    @classmethod
    #def lazyR_NOT_XOR(cls, lazy_lhs, lazy_rhs):
    def lazyR_XNOR(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'XNOR', lazy_lhs, lazy_rhs)
        #return Lazy(cls._lazy_binary_tribool_op, True, 'NOT_XOR', lazy_lhs, lazy_rhs)

    @classmethod
    def lazyL_IMPLY(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'IMPLY', lazy_lhs, lazy_rhs)
    @classmethod
    def lazyR_IMPLY(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'IMPLY', lazy_lhs, lazy_rhs)

    @classmethod
    def lazyL_FLIP_IMPLY(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'FLIP_IMPLY', lazy_lhs, lazy_rhs)
    @classmethod
    def lazyR_FLIP_IMPLY(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'FLIP_IMPLY', lazy_lhs, lazy_rhs)

    @classmethod
    def lazyL_NOT_IMPLY(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'NOT_IMPLY', lazy_lhs, lazy_rhs)
    @classmethod
    def lazyR_NOT_IMPLY(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'NOT_IMPLY', lazy_lhs, lazy_rhs)

    @classmethod
    def lazyL_NOT_FLIP_IMPLY(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, False, 'NOT_FLIP_IMPLY', lazy_lhs, lazy_rhs)
    @classmethod
    def lazyR_NOT_FLIP_IMPLY(cls, lazy_lhs, lazy_rhs):
        return Lazy(cls._lazy_binary_tribool_op, True, 'NOT_FLIP_IMPLY', lazy_lhs, lazy_rhs)

    lazyL_NAND = lazyL_NOT_AND
    lazyL_NOR = lazyL_NOT_OR
    #lazyL_XNOR = lazyL_NOT_XOR
    lazyL_NOT_XOR = lazyL_XNOR
    lazyL_OR_notL_idR = lazyL_IMPLY
    lazyL_OR_idL_notR = lazyL_FLIP_IMPLY
    lazyL_AND_idL_notR = lazyL_NOT_IMPLY
    lazyL_FLIP_NOT_IMPLY = lazyL_NOT_FLIP_IMPLY
    lazyL_AND_notL_idR = lazyL_NOT_FLIP_IMPLY
    #
    lazyR_NAND = lazyR_NOT_AND
    lazyR_NOR = lazyR_NOT_OR
    #lazyR_XNOR = lazyR_NOT_XOR
    lazyR_NOT_XOR = lazyR_XNOR
    lazyR_OR_notL_idR = lazyR_IMPLY
    lazyR_OR_idL_notR = lazyR_FLIP_IMPLY
    lazyR_AND_idL_notR = lazyR_NOT_IMPLY
    lazyR_FLIP_NOT_IMPLY = lazyR_NOT_FLIP_IMPLY
    lazyR_AND_notL_idR = lazyR_NOT_FLIP_IMPLY
    #

_cached__binary_tribool_op_std_name2lazy_info = \
        {'AND': ('AND', (False, False, True), (False, False, True))
        , 'OR': ('OR', (True, True, False), (True, True, False))
        , 'XOR': ('XOR', (Ellipsis, Ellipsis, False), (Ellipsis, Ellipsis, False))

        , 'NOT_AND': ('NOT_AND', (False, True, None), (False, True, None))
        , 'NOT_OR': ('NOT_OR', (True, False, None), (True, False, None))
        #, 'NOT_XOR': ('NOT_XOR', (Ellipsis, Ellipsis, True), (Ellipsis, Ellipsis, True))
        , 'XNOR': ('XNOR', (Ellipsis, Ellipsis, True), (Ellipsis, Ellipsis, True))

        , 'IMPLY': ('IMPLY', (False, True, True), (True, True, None))
        , 'FLIP_IMPLY': ('FLIP_IMPLY', (True, True, None), (False, True, True))
        , 'NOT_IMPLY': ('NOT_IMPLY', (False, False, None), (True, False, False))
        , 'NOT_FLIP_IMPLY': ('NOT_FLIP_IMPLY', (True, False, False), (False, False, None))
        }

if 0:
    LazyTriBoolOps.binary_tribool_op_std_name2lazy_info = LazyTriBoolOps._mk_binary_tribool_op_std_name2lazy_info()
else:
    LazyTriBoolOps.binary_tribool_op_std_name2lazy_info = _cached__binary_tribool_op_std_name2lazy_info

#aliases include std_name
TriBoolOps__std_name_and_aliases.binary_tribool_op_alias2std_name
TriBoolOps__std_name_and_aliases.binary_tribool_op_std_name2aliases

LazyTriBoolOps.binary_tribool_op_alias2std_name
LazyTriBoolOps.binary_tribool_op_std_name2aliases


LazyTriBoolOps.binary_tribool_op_std_name2lazy_info
if __name__ == '__main__':
    #LazyTriBoolOps.binary_tribool_op_std_name2lazy_info = LazyTriBoolOps._mk_binary_tribool_op_std_name2lazy_info()
    #################################
    #################################
    #################################
    from pprint import pprint
    #pprint(LazyTriBoolOps.binary_tribool_op_std_name2lazy_info)
    assert LazyTriBoolOps.binary_tribool_op_std_name2lazy_info == _cached__binary_tribool_op_std_name2lazy_info
    assert LazyTriBoolOps._mk_binary_tribool_op_std_name2lazy_info() == _cached__binary_tribool_op_std_name2lazy_info


#HHHHH
class test_TriBool_lazy_binary_ops:
    #LazyTriBoolOps
    #test op result
    #test op lazyness
    @classmethod
    def _test_op(cls, f, data):
        d = LazyTriBoolOps.binary_tribool_op_alias2std_name
        def get_op(name):
            return getattr(TriBoolOps, name)
        def get_lazyL_op(name):
            return getattr(LazyTriBoolOps, f'lazyL_{name!s}')
        def get_lazyR_op(name):
            return getattr(LazyTriBoolOps, f'lazyR_{name!s}')
        for alias, std_name in d.items():
            op = get_op(alias)
            std_op = get_op(std_name)
            lazyL_op = get_lazyL_op(alias)
            lazyR_op = get_lazyR_op(alias)
            assert op is not None
            for x, y in  itertools.product([False, True, ...], repeat=2):
                f(data, alias, std_name, op, std_op, lazyL_op, lazyR_op, x, y)
    @classmethod
    def _test_op_result(cls, data, alias, std_name, op, std_op, lazyL_op, lazyR_op, lhs, rhs):
        call2 = data.call2
        #assert_eq_f = data.assert_eq_f
        assert_eq_f = mk_assert_eq_f(alias=alias, std_name=std_name)
        r = std_op(lhs, rhs)
        assert_eq_f(r, op, lhs, rhs)
        assert_eq_f(r, call2, lazyL_op, lambda:lhs, lambda:rhs)
        assert_eq_f(r, call2, lazyR_op, lambda:lhs, lambda:rhs)
    @classmethod
    def _test_op_lazyness(cls, data, alias, std_name, op, std_op, lazyL_op, lazyR_op, lhs, rhs):

        lazy_info = LazyTriBoolOps.binary_tribool_op_std_name2lazy_info[std_name]
        (_, lazy_infoL, lazy_infoR) = lazy_info
        export_called_pair = data.export_called_pair

        (lhs_determine_value, result4lhs_determine_value, maybe_foldl0_start_value) = lazy_infoL
        a, b = export_called_pair(lazyL_op, lhs, rhs)
        assert_eq(a, True)
        assert_eq(b, lhs is not lhs_determine_value)

        (rhs_determine_value, result4rhs_determine_value, maybe_foldr0_start_value) = lazy_infoR
        a, b = export_called_pair(lazyR_op, lhs, rhs)
        assert_eq(a, rhs is not rhs_determine_value)
        assert_eq(b, True)


    @classmethod
    def test_op_result(cls):
        class data:
            call2 = lambda f, /, *args, **kwargs: f(*args, **kwargs)()
        cls._test_op(cls._test_op_result, data)
    @classmethod
    def test_op_lazyness(cls):
        class data:
            class Called:
                def __init__(sf, x):
                    sf.__x = x
                    sf.__b = False
                def __call__(sf):
                    sf.__b = True
                    return sf.__x
                @property
                def called(sf):
                    return sf.__b
            @classmethod
            def export_called_pair(cls, lazy_op, lhs, rhs):
                Called = cls.Called
                lazy_lhs = Called(lhs)
                lazy_rhs = Called(rhs)
                lazy_op(lazy_lhs, lazy_rhs)()
                (a, b) = (lazy_lhs.called, lazy_rhs.called)
                return a, b
        cls._test_op(cls._test_op_lazyness, data)
    @classmethod
    def main_test(cls):
        cls.test_op_result()
        cls.test_op_lazyness()
if __name__ == '__main__':
    test_TriBool_lazy_binary_ops.main_test()

#HHHHH


