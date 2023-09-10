#__all__:goto
r'''[[[
e ../../python3_src/seed/math/ops/algebra/IAlgebraOps.py
e ../../python3_src/seed/math/ops/algebra/IRingOps.py
    view ../../python3_src/seed/math/IRingOps.py

e others/数学/四则运算.txt

view ../../python3_src/nn_ns/math_nn/algebra/IAlgebra.py
xxx view ../../python3_src/nn_ns/math_nn/algebra/IField.py
xxx view ../../python3_src/nn_ns/math_nn/algebra/IObject.py
view ../../python3_src/nn_ns/math_nn/algebra/IGroup.py
grep idempo -r . -l -a
square matrix multiplication
reciprocal
multiplicative inverse
multiplicative identity
commutative property 交换律
associative property 结合律
distributive property 分配律

idempotent
commutative
associative
distributive
associativity
commutativity
idempotency
division
identity
divisibility
invertibility
inverse
abelian
group
monoid
magma
quasigroup
semigroup
semilattice


absorbing
distributive property
semiring



view others/数学/function.txt












seed.math.ops.algebra.IAlgebraOps
py -m nn_ns.app.debug_cmd   seed.math.ops.algebra.IAlgebraOps -x

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IAlgebraOps:IAlgebraOps@T    =T

#]]]'''
__all__ = r'''
IAlgebraOps
NonInvertibleError
    NonInvertibleError__not_implemented
    NonInvertibleError__not_commutative
    NonInvertibleError__not_injective
    NonInvertibleError__out_of_domain
'''.split()#'''
__all__


from seed.tiny import check_type_is
from seed.tiny import print_err#echo, , mk_fprint, mk_assert_eq_f, expectError
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.lang.hasattr__as_cls import hasattr__as_cls
from seed.tiny import mk_frozenset, null_frozenset
from seed.helper.str2__all__ import str2__all__




#class NonInvertibleError(ZeroDivisionError):pass
class NonInvertibleError(Exception):pass
class NonInvertibleError__not_implemented(NonInvertibleError):
    'see:try_truediv()'
class NonInvertibleError__not_commutative(NonInvertibleError):
    r'''
    eg: [try_inv_(x) but try_left_inv_(x) =!= try_right_inv_(x)]
    eg: [try_truediv(n,d) but try_left_div(n,d) =!= try_right_div(n,d)]
    '''#'''
class NonInvertibleError__not_injective(NonInvertibleError):
    'e.g. [Ring square matrix] => [1/[1,0;0,0] --> not_injective]'
class NonInvertibleError__out_of_domain(NonInvertibleError):
    'e.g. [Ring int] => [6/2 == 3][1/2 --> out_of_domain]'

#class Symbol:pass
def _collect_exported_names_of_bases(__class__, __bases__, /):
    #(vars(T).get('___all___') for T in cls.__bases__ if isinstance(T, __class__))
    ss = [T.___all___ for T in __bases__ if issubclass(T, __class__)]
    ss = [s for s in ss if s]
    if ss:
        s = set()
        s.update(*ss)
        s = mk_frozenset(s)
        x = max(ss, key=len)
        assert len(s) >= len(x)
        if len(s) == len(x):
            assert s == x
            s = x # reuse
    else:
        s = null_frozenset
    check_type_is(frozenset, s)
    # [s :: frozenset<nm>]
    nms = s
    return nms
def _nms5str_or_nms(str_or_nms, /):
    s = str_or_nms
    # [s :: (str | Iter nm)]
    if type(s) is str:
        s = s.replace('`', ' ')
        s = str2__all__(s)
        # [s :: Iter nm]
    # [s :: Iter nm]
    s = mk_frozenset(s)
    # [s :: frozenset<nm>]
    nms = s
    return nms
_excluded_nms = mk_frozenset([])
class IAlgebraOps(ABC):
    r'''[[[
    ___all___
        :: (None | ... | str | Iter nm)
        all_exported_names
        if ___all___ is None:
            as if [___bases4all___ := True]
        if ___all___ is ...:
            ==>> warning



    ___hidden_names___
        :: (None | str | Iter nm)
        explicitly declare to hidden some names



    ___bases4all___
        :: (None | True | Iter basecls)
        bases to import their ___all___
        if ___bases4all___ is None:
            ___bases4all___ = []
        if ___bases4all___ is True:
            ___bases4all___ = cls.__bases__
        for T in ___bases4all___:
            all_exported_names |= T.___all___


    #]]]'''#'''
    __slots__ = ()
    ___all___ = r'''
    '''.split()#'''
    ___all___ = mk_frozenset(___all___)
    @override
    def __dir__(ops, /):
        return type(ops).___all___
    @override
    def __getattribute__(ops, nm, /):
        nms = type(ops).___all___
        if nms is ...:
            print_err(f'warn:require fix:{type(ops)}: [type(ops).___all___ is ...]:ops.{nm!s}')
            pass
        elif not nm in nms:
            raise AttributeError(nm)
        return super().__getattribute__(nm)
    @override
    def __init_subclass__(cls, /, *args, **kwargs):
        nms5bases = _collect_exported_names_of_bases(__class__, cls.__bases__)
        # [nms5bases :: frozenset<nm>]

        #s = cls.___all___
        m = vars(cls).get('___all___')
        if m is None:
            s = nms5bases
            # !! [nms5bases :: frozenset<nm>]
            # [s :: frozenset<nm>]
            # [s :: Iter nm]
        else:
            s = m
            # [s :: (... | str | Iter nm)]
        # [s :: (... | str | Iter nm)]
        if s is ...:
            print_err(f'warn:require fix:{cls}: [cls.___all___ is ...]')
            pass
        else:
            # [s :: (str | Iter nm)]
            s = _nms5str_or_nms(s)
            # [s :: frozenset<nm>]
            m = vars(cls).get('___bases4all___')
            if m is True:
                imported_nms5bases = nms5bases
                # [imported_nms5bases :: frozenset<nm>]
            elif m:
                _bases = m
                imported_nms5bases = _collect_exported_names_of_bases(__class__, _bases)
                # [imported_nms5bases :: frozenset<nm>]
            else:
                imported_nms5bases = null_frozenset
                # [imported_nms5bases :: frozenset<nm>]
            # [imported_nms5bases :: frozenset<nm>]
            if s <= imported_nms5bases:
                s = imported_nms5bases
                # [s :: frozenset<nm>]
            else:
                s |= imported_nms5bases
                # [s :: frozenset<nm>]
            # [s :: frozenset<nm>]
            cls.___all___ = s
            ___hidden_names___ = vars(cls).get('___hidden_names___', null_frozenset)
            # [___hidden_names___ :: (str | Iter nm)]
            ___hidden_names___ = _nms5str_or_nms(___hidden_names___)
            # [___hidden_names___ :: frozenset<nm>]
            hidden_nms = nms5bases - s -___hidden_names___
            if hidden_nms:
                hidden_nms = sorted(hidden_nms)
                print_err(f'warn:require fix:{cls}: cls.___hidden_names___ not include: [hidden_nms == {hidden_nms}]')

            for nm in s:
                getattr(cls, nm)
                    #check existence
            undeclared_nms = []
            for nm in vars(cls):
                if nm.startswith('_'):
                    continue
                if nm in _excluded_nms:
                    continue
                if not nm in s:
                    undeclared_nms.append(nm)
            if undeclared_nms:
                undeclared_nms.sort()
                #raise TypeError(f'undeclared names: {undeclared_nms}')
                print_err(f'warn:require fix:{cls}: undeclared names: {undeclared_nms}')

        super(__class__, cls).__init_subclass__(*args, **kwargs)

    @classmethod
    @override
    def __subclasshook__(cls, C, /):
        # ABCMeta::__subclasshook__
        #if cls is __class__:
        if 1:
            nms = cls.___all___
            if nms is ...:
                print_err(f'warn:require fix:{cls}: [cls.___all___ is ...]')
                pass
            elif not nms:
                pass
            #else:
            #    return all(hasattr__as_cls(C, nm) for nm in nms)
            #    # return False will disable .register()
            elif all(hasattr__as_cls(C, nm) for nm in nms):
                #IAlgebraOps.register(C)
                #print('IAlgebraOps.register(C)')
                #   ==>> will be registered by lib!
                return True
        return NotImplemented




    #___no_slots_ok___ = True
    #from seed.helper.repr_input import repr_helper
    #def __repr__(sf, /):
        #return repr_helper(sf, *args, **kwargs)
def __():
    save = mk_frozenset(IAlgebraOps.___all___)
    IAlgebraOps.___all___ = ['__']
    assert not save

    class T:pass
    assert not issubclass(T, IAlgebraOps)
    IAlgebraOps.register(T)
    assert issubclass(T, IAlgebraOps)

    class T:pass
    assert not issubclass(T, IAlgebraOps)
    class T:
        __ = 1
    assert issubclass(T, IAlgebraOps)

    IAlgebraOps.___all___ = save

    class T:pass
    assert not issubclass(T, IAlgebraOps)
    class T:
        __ = 1
    assert not issubclass(T, IAlgebraOps)
__()
__all__


from seed.math.ops.algebra.IAlgebraOps import IAlgebraOps, NonInvertibleError, NonInvertibleError__not_injective, NonInvertibleError__out_of_domain, NonInvertibleError__not_implemented, NonInvertibleError__not_commutative
from seed.math.ops.algebra.IAlgebraOps import *
