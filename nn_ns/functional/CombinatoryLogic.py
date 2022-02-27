
r'''
py -m nn_ns.app.debug_cmd   nn_ns.functional.CombinatoryLogic
py -m nn_ns.functional._try_CombinatoryLogic
    指数增长？！！！
#'''


#################################
__all__ = '''
    Expr
    is_free
    is_combinator__SKIBC
    is_combinator
    substitute
    frozen_set__list
    has_no_frees
    empty_frozen_set
    collect_frees
    Variable
    NamedVariable
    Application
    call
    Abstraction
    EvaluationStrategy
    UnknownExprCase
    FullBetaReduction
    NormalOrder
    CallByName
    CallByNeed
    CallByValue
    evalue
    Use_py_id_InsteadOf_id
    py_id
    id
    L
    V
    I
    K
    const
    S
    implication_elimination
    reader_apply
    C
    flip
    B
    composition
    primitive_combinators__SKIBC
    primitive_combinator_id_set__SKIBC
    is_primitive_combinator__SKIBC
    POS_body
    POS_outermost
    POS_func
    POS_arg
    POS_paran
    PrintArg
    print_expr
    print_expr__SKIBC
    short_hand__SKIBC
    show_expr__SKIBC
    show_expr
    has_no_abstraction
    remove_abstraction__SKIBC
    newtype_container
    right_apply
    C_I
    apply_self
    divergent
    omega
    fix
    '''.split()
#################################


from abc import ABCMeta, abstractmethod
class Expr(metaclass=ABCMeta):
    # Expr = Abstraction | Application | Variable
    # Expr = Expr -> Expr
    #   newtype Expr = Expr (_Expr -> _Expr)
    #   data _Expr = _Expr (Expr)
    '''
    @abstractmethod
    def ___eval___(self):
        raise NotImplementedError
    @abstractmethod
    # def __reduce__(self):
    def ___reduce___(self):
        raise NotImplementedError
    '''
    pass

    #@abstractmethod
    def ___call___(self, expr : 'Expr'):
        return Application(self, expr)
        raise NotImplementedError
    def __getitem__(self, expr : 'Expr'):
        assert isinstance(expr, Expr)
        r = type(self).___call___(self, expr)
        if isinstance(r, Expr):
            return r
        raise TypeError

    @abstractmethod
    def ___substitute___(self, name : str
                        , expr : 'Expr', frees : 'frozen_set'):
        # frees of expr: {.__contains__}
        # if bounded variables in frees, cause undefined behaviour
        raise NotImplementedError
    @abstractmethod
    def ___is_free___(self, name : str):
        raise NotImplementedError
    @abstractmethod
    def ___is_combinator___(self, is_primitive_combinator):
        # is_primitive_combinator or without abstraction
        if is_primitive_combinator(self):
            return True
        raise NotImplementedError
    @abstractmethod
    def ___has_no_frees___(self, bounded_names : 'frozen_set'):
        # has no frees
        # bounded_names { .__contains__, .frozen_iadd }
        raise NotImplementedError
    @abstractmethod
    def ___frees___(self
                    , outer_known_frees : 'mutable_or_frozen_set'
                    , bounded_names : 'frozen_set'):
        # bounded_names { .__contains__, .frozen_iadd }
        # outer_known_frees { .mutable_or_frozen_iadd }
        raise NotImplementedError
def is_free(name : str, expr : Expr):
    assert isinstance(expr, Expr)
    assert isinstance(name, str)
    return bool(type(expr).___is_free___(expr, name))
def is_combinator__SKIBC(expr : Expr):
    return is_combinator(expr, is_primitive_combinator__SKIBC)
def is_combinator(expr : Expr, is_primitive_combinator):
    assert isinstance(expr, Expr)
    if is_primitive_combinator(expr):
        return True
    return bool(type(expr).___is_combinator___(
                            expr, is_primitive_combinator))

def substitute(body : Expr, name : str, expr : Expr, frees : 'frozen_set'):
    # frees of expr {.__contains__}
    assert isinstance(body, Expr)
    assert isinstance(name, str)
    assert isinstance(expr, Expr)
    # frees = collect_frees(expr)
    r = type(body).___substitute___(body, name, expr, frees)
    if isinstance(r, Expr):
        return r
    raise TypeError

class frozen_set__list:
    def __init__(self):
        self._set = ()
    def __bool__(self):
        return bool(self._set)
    def __contains__(self, e):
        return any(map((lambda x: x==e), self))
    def __iter__(self):
        s = self._set
        while s:
            e, s = s
            yield e
    def frozen_iadd(self, e):
        new = frozen_set__list()
        new._set = (e, self._set)
        return new
    mutable_or_frozen_iadd = frozen_iadd
def has_no_frees(expr : Expr
                , bounded_names : 'frozen_set' = frozen_set__list()
                ):
    # Elem frozen_set == str
    # frozen_set { .__contains__, .frozen_iadd }
    #   where .frozen_iadd :: set -> Elem set -> set
    assert isinstance(expr, Expr)
    return bool(type(expr).___has_no_frees___(expr, bounded_names))
empty_frozen_set = frozen_set__list()
def collect_frees\
        ( expr : Expr
        , outer_known_frees : 'mutable_or_frozen_set' = empty_frozen_set
        , bounded_names : 'frozen_set' = empty_frozen_set
        ):
    assert isinstance(expr, Expr)
    return type(expr).___frees___(expr, outer_known_frees, bounded_names)
class Variable(Expr):
    # x
    pass
class NamedVariable(Variable):
    def __init__(self, name : str):
        assert isinstance(name, str)
        self.name = name
    #def ___substitute___(self, name : str, expr : 'Expr'):
    def ___substitute___(self, name : str
                        , expr : 'Expr', frees : 'frozen_set'):
        return expr if self.name == name else self
    def ___is_free___(self, name : str):
        return name == self.name
    def ___is_combinator___(self, is_primitive_combinator):
        # is_primitive_combinator or without abstraction
        return True
        if is_primitive_combinator(self):
            return True
    def ___has_no_frees___(self, bounded_names : 'frozen_set'):
        return self.name in bounded_names
    def ___frees___(self
                    , outer_known_frees : 'mutable_or_frozen_set'
                    , bounded_names : 'frozen_set'):
        if self.name in bounded_names:
            return outer_known_frees
        return outer_known_frees.mutable_or_frozen_iadd(
            self.name)
    pass

class Application(Expr):
    # f x
    def __init__(self, function : Expr, argument : Expr):
        assert isinstance(function, Expr)
        assert isinstance(argument, Expr)
        self.function = function
        self.argument = argument
    #def ___substitute___(self, name : str, expr : 'Expr'):
    def ___substitute___(self, name : str
                        , expr : 'Expr', frees : 'frozen_set'):
        return Application(substitute(self.function, name, expr, frees)
                         , substitute(self.argument, name, expr, frees))
    def ___is_free___(self, name : str):
        return is_free(name, self.function) and\
                is_free(name, self.argument)
    def ___is_combinator___(self, is_primitive_combinator):
        # is_primitive_combinator or without abstraction
        return is_combinator(self.function, is_primitive_combinator) \
            and is_combinator(self.argument, is_primitive_combinator)
        if is_primitive_combinator(self):
            return True
    def ___has_no_frees___(self, bounded_names : 'frozen_set'):
        return has_no_frees(self.function, bounded_names) and \
                has_no_frees(self.argument, bounded_names)
    def ___frees___(self
                    , outer_known_frees : 'mutable_or_frozen_set'
                    , bounded_names : 'frozen_set'):
        frees = outer_known_frees
        frees = collect_frees(self.function, frees, bounded_names)
        frees = collect_frees(self.argument, frees, bounded_names)
        return frees
    pass

def call(function : Expr, argument : Expr):
    assert isinstance(function, Expr)
    assert isinstance(argument, Expr)
    return function(argument)
class Abstraction(Expr):
    # \x expr :: A -> A where A is Abstraction
    def __init__(self, name : str, body : Expr):
        assert isinstance(name, str)
        assert isinstance(body, Expr)
        self.bound = NamedVariable(name)
        self.body = body
    def apply_substitute(self, expr : Expr):
        assert isinstance(expr, Expr)
        return substitute(self.body, self.bound.name, expr)
    #def ___substitute___(self, name : str, expr : 'Expr'):
    def ___substitute___(self, name : str
                        , expr : 'Expr', frees : 'frozen_set'):
        self_name = self.bound.name
        if name == self_name:
            return self
        elif self_name in frees:
            raise Exception('variable capture substitute: {!r}'
                            .format(self_name))
        else:
            body_ = substitute(self.body, name, expr, frees)
            return Abstraction(self_name, body_)

    def ___is_free___(self, name : str):
        return name != self.bound.name and \
                is_free(name, self.body)
    def ___is_combinator___(self, is_primitive_combinator):
        # is_primitive_combinator or without abstraction
        return False
        if is_primitive_combinator(self):
            return True
    def ___has_no_frees___(self, bounded_names : 'frozen_set'):
        bounded_names = bounded_names.frozen_iadd(self.bound.name)
        return has_no_frees(self.body, bounded_names)
    def ___frees___(self
                    , outer_known_frees : 'mutable_or_frozen_set'
                    , bounded_names : 'frozen_set'):
        name = self.bound.name
        bounded_names = bounded_names.frozen_iadd(name)
        frees = outer_known_frees
        frees = collect_frees(self.body, frees, bounded_names)
        return frees


class EvaluationStrategy(metaclass=ABCMeta):
    @abstractmethod
    def ___evalue___(self, expr : Expr):
        raise NotImplementedError
    pass

UnknownExprCase = TypeError('Expr but not NamedVariable|Application|Abstraction')
class FullBetaReduction(EvaluationStrategy):
    # in any order
    @abstractmethod
    def ___evalue___(self, expr : Expr):
        raise NotImplementedError
    pass
class NormalOrder(EvaluationStrategy):
    def ___evalue___(self, expr : Expr):
        if isinstance(expr, Variable):
            return expr
        elif isinstance(expr, Abstraction):
            return Abstraction(expr.bound.name, evalue(self, expr.body))
        elif isinstance(expr, Application):
            f = evalue(self, expr.function)
            if isinstance(f, Abstraction):
                r = f.apply_substitute(expr.argument)
                return evalue(self, r)
            elif isinstance(f, Variable):
                raise Exception('unknown howto eval(v x)')
            elif isinstance(f, Application):
                raise logic-error
            else:
                raise UnknownExprCase
        else:
            raise UnknownExprCase
    pass
class CallByName(EvaluationStrategy):
    def ___evalue___(self, expr : Expr):
        if isinstance(expr, Variable):
            return expr
        elif isinstance(expr, Abstraction):
            return expr
        elif isinstance(expr, Application):
            f = evalue(self, expr.function)
            if isinstance(f, Abstraction):
                r = f.apply_substitute(expr.argument)
                return evalue(self, r)
            elif isinstance(f, Variable):
                raise Exception('unknown howto eval(v x)')
            elif isinstance(f, Application):
                raise logic-error
            else:
                raise UnknownExprCase
        else:
            raise UnknownExprCase


class CallByNeed(EvaluationStrategy):
    # Haskell
    pass

class CallByValue(EvaluationStrategy):
    def ___evalue___(self, expr : Expr):
        # value :: abstraction
        # only lambda functions are value!
        if isinstance(expr, Variable):
            raise Exception('unknown howto eval free variable x')
            return expr
        elif isinstance(expr, Abstraction):
            return expr
        elif isinstance(expr, Application):
            f = evalue(self, expr.function)
            if isinstance(f, Abstraction):
                x = evalue(self, expr.argument)
                r = f.apply_substitute(x)
                return evalue(self, r)
            elif isinstance(f, Variable):
                raise logic-error
                raise Exception('unknown howto eval(v x)')
            elif isinstance(f, Application):
                raise logic-error
            else:
                raise UnknownExprCase
        else:
            raise UnknownExprCase




#def evalue(expr : Expr):
#    v = type(expr).___eval___(self, expr)
def evalue(strategy : EvaluationStrategy, expr : Expr):
    assert isinstance(strategy, EvaluationStrategy)
    assert isinstance(expr, Expr)
    v = type(strategy).___eval___(strategy, expr)
    if isinstance(v, Expr):
        return v
    raise TypeError



class Use_py_id_InsteadOf_id:
    def __init__(self, *args, **kwargs):
        raise Exception('Use "py_id" InsteadOf "id"')
    pass
py_id, id = id, Use_py_id_InsteadOf_id

#L = Abstraction # lambda name, body
def L(**kwargs):
    assert len(kwargs) == 1
    (name, body), = kwargs.items()
    return Abstraction(name, body)
V = NamedVariable
_f, _g, _a, _b, _x, _y = map(V, 'fgabxy')
# I :: a -> a
# ($) :: (a->b) -> (a->b)
I = _id_ = L(a = _a)
# K :: a -> b -> a
K = const = L(a = L(b = _a))
# S :: (a -> (b->c)) -> ((a->b) -> (a->c))
# "a -> (b->c), a->b, a |- c"
S = implication_elimination = reader_apply = \
    L(f = L(g = L(a = _f[_a][_g[_a]])))
# C :: (a -> b -> c) -> (b -> a -> c)
C = flip = L(f = L(b = L(a = _f[_a][_b])))
# B :: (b->c) -> (a->b) -> (a->c)
# (.) == B
B = composition = L(f = L(g = L(a = _f[_g[_a]])))

primitive_combinators__SKIBC = [I, K, S, B, C]
primitive_combinator_id_set__SKIBC = \
    frozenset(map(py_id, primitive_combinators__SKIBC))
def is_primitive_combinator__SKIBC(expr : Expr):
    return py_id(expr) in primitive_combinator_id_set__SKIBC
'''
def is_primitive_combinator(expr : Expr
                            , primitive_combinator_id_set=
                                frozenset(map(py_id, primitive_combinators))
                            ):
    return py_id(expr) in primitive_combinator_id_set
'''
# outer
# NeedNotParan = ''
# NeedParan = '()'
POS_body = r'\{name} {body}'
POS_outermost = r'{expr}'
POS_func = r'{func} ...'
POS_arg = r'... {arg} ...'
POS_paran = r'({paran})'

class PrintArg:
    # show_name: str, repr
    # lambda_str: '\\', 'lambda '
    # begin_body_str: ' ', '->', '.'
    # short_hand: (), {id(S):'S', ...} # id2object
    def __init__(self
            , show_name = str
            , lambda_str = '\\'
            , begin_body_str = ' '
            , short_hand = ()
            ):
        self.show_name = show_name
        self.lambda_str = lambda_str
        self.begin_body_str = begin_body_str
        self.short_hand_dict = dict(short_hand)
    def copy(self):
        return __class__(self.show_name
                        , self.lambda_str
                        , self.begin_body_str
                        , self.short_hand_dict)
def print_expr(expr : Expr, outer=POS_outermost, params = PrintArg()):
    print(show_expr(expr, outer, params))
def print_expr__SKIBC(expr : Expr, outer=POS_outermost, params = PrintArg()):
    print(show_expr__SKIBC(expr, outer, params))



short_hand__SKIBC = {py_id(globals()[name]) : name for name in 'SKIBC'}
def show_expr__SKIBC(expr : Expr, outer, params = PrintArg()):
    params = params.copy()
    params.short_hand_dict.update(short_hand__SKIBC)
    return show_expr(expr, outer, params)
def show_expr(expr : Expr, outer, params = PrintArg()):
    # outer = POS_outermost | POS_body | POS_func | POS_arg
    # xxxxx outer = NeedParan | NeedNotParan | ???
    this_function = show_expr
    short_hand = params.short_hand_dict
    if py_id(expr) in short_hand:
        return short_hand[py_id(expr)]
    elif isinstance(expr, NamedVariable):
        return params.show_name(expr.name)
    elif isinstance(expr, Abstraction):
        s = '{lambda_str}{name}{begin_body_str}{body}'.format\
            ( lambda_str = params.lambda_str
            , name = params.show_name(expr.bound.name)
            , begin_body_str = params.begin_body_str
            , body = this_function(expr.body, POS_body, params)
            )
        need_paran = outer == POS_func
    elif isinstance(expr, Application):
        f = this_function(expr.function, POS_func, params)
        a = this_function(expr.argument, POS_arg, params)
        s = '{} {}'.format(f, a)
        need_paran = outer == POS_arg
    else:
        raise UnknownExprCase

    if need_paran:
        s = '({})'.format(s)
    return s


def _test():
    def _has_no_frees(expr : Expr):
        return not collect_frees(expr)
    assert all(has_no_frees(c) == _has_no_frees(c)
                for c in primitive_combinators__SKIBC)
    for c in primitive_combinators__SKIBC:
        # print(set(collect_frees(c)))
        if not has_no_frees(c):
            print_expr(c)
    assert all(map(has_no_frees, primitive_combinators__SKIBC))
    #for c in primitive_combinators__SKIBC:
    #    print_expr(c)
    for c, s in zip([S, K, I, B, C],
                        [ r'\f \g \a f a (g a)'
                        , r'\a \b a'
                        , r'\a a'
                        , r'\f \g \a f (g a)'
                        , r'\f \b \a f a b'
                        ]):
        assert show_expr(c, POS_outermost) == s

_test()


def has_no_abstraction(expr : Expr):
    assert isinstance(expr, Expr)
    this_function = has_no_abstraction
    if isinstance(expr, NamedVariable):
        return True
    elif isinstance(expr, Abstraction):
        return False
    elif isinstance(expr, Application):
        return this_function(expr.function) and\
                this_function(expr.argument)
    else:
        raise UnknownExprCase

# SKIBC_id_set = frozenset(map(py_id, primitive_combinators__SKIBC))
def remove_abstraction__SKIBC(expr : Expr):
    assert isinstance(expr, Expr)
    # assert has_no_frees(expr) # allow frees
    T = this_function = remove_abstraction__SKIBC
    r'''
T[x] => x
T[(f e)] => (T[f] T[e])
T[\x->e] => (K T[e]) (if x is not free in e)
T[\x->x] => I
T[\x->\y->e] => T[\x->T[\y->e]] (if x is free in e)
+ eta-reduction: T[\x->(f x)] = T[f] (if x is not free in f)
    <==> B I e == e; B e I == e
T[\x->(f e)] => (S T[\x->f] T[\x->e]) (if x is free in both f and e)
T[\x->(f e)] => (C T[\x->f] T[e]) (if x is free in f but not e)
T[\x->(f e)] => (B T[f] T[\x->e]) (if x is free in e but not f)
'''
    if isinstance(expr, NamedVariable):
        return expr
    elif is_primitive_combinator__SKIBC(expr):
        return expr
    elif isinstance(expr, Application):
        return T(expr.function)[T(expr.argument)]
    elif isinstance(expr, Abstraction):
        name = expr.bound.name
        body = expr.body
        if name not in collect_frees(body):
            return K[T(body)]
        elif isinstance(body, NamedVariable):
            assert body.name == name
            return I
        elif isinstance(body, Abstraction):
            return T(Abstraction(name, T(body)))
        elif isinstance(body, Application):
            f = body.function
            e = body.argument
            in_f = name in collect_frees(f)
            in_e = name in collect_frees(e)
            assert in_f or in_e # since "x in frees(f e)"

            x_f = Abstraction(name, f)
            x_e = Abstraction(name, e)
            if in_f and in_e:
                return S[T(x_f)][T(x_e)]
            elif in_f and not in_e:
                # flip
                return C[T(x_f)][T(e)]
            elif not in_f and in_e:
                # (.)
                # B__eta_reduction
                # return B[T(f)][T(x_e)]
                Tf = T(f)
                Tx_e = T(x_e)
                if Tf is I:
                    return Tx_e
                elif Tx_e is I:
                    return Tf
                return B[Tf][Tx_e]
            else:
                raise logic-error
        else:
            raise UnknownExprCase
    else:
        raise UnknownExprCase

newtype_container = right_apply = L(a = L(f = _f[_a]))
C_I = remove_abstraction__SKIBC(right_apply)
assert not is_combinator__SKIBC(right_apply)
assert is_combinator__SKIBC(C_I)
assert show_expr__SKIBC(C_I, POS_outermost) == 'C I'
#print_expr__SKIBC(C_I)
#print_expr(C_I)







r'''
-- list_container as reduce/fold_left
list_container :: (a->b->b) -> b -> b
list_container op init = ...
[1,2,3] op a0 = op 1 (op 2 (op 3 a0))
[] op a0 = a0
    ==>> [] = flip const
(h:t) op a0 = op h (t op a0)
    ==>> (:) h t op a0 = op h (t op a0)
    ==>> (:) = \h\t\f\b = f h (t f b)


-- list_container2 as constructor sum
data List a = List (b -> (a -> List a -> b) -> b)
list_container2 :: b -> (a -> list_container2 -> b) -> b
    -- which constructor?
                   []   (:)
[] = const
    [] = \b\f b
(h:t) b f = f h t
    cons h t b f = f h t
    cons = \h\t\b\f f h t

'''

# \f -> f f
apply_self = L(f = _f[_f])
# (\x-> x x)(\x-> x x)
divergent = omega = apply_self[apply_self]

# fix__call_by_value = \f. (\x. f (\y. x x y)) (\x. f (\y. x x y));
# fix__call_by_name  = \f. (\x. f (    x x  )) (\x. f (    x x  ))
# Y
fix = L(f = apply_self[L(x = _f[apply_self[_x]])])


if __name__ == "__main__":
    print_expr(fix)
    print_expr(apply_self)


