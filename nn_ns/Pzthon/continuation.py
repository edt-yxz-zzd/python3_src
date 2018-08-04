

r'''
    # continuation: # keyword cor
    #   continuation = tail :: a -> r
    #   cps :: continuation -> r # CPS r a # missing a tail
            # (a->r)->r # <=[as-if]=> (r | a | (a,a,a, r->r->r->r->r->r)|...)
    #       continuation = lambda a: r
    #       cps = lambda continuation: continuation(a)
    #   def a2mb(a): mb # a -> CPS r b # a -> (b->r) -> r # <=[as-if]=> a -> b
    #   mb = ma >>= a2mb # @ma \n def mb(a): mb
    #       = lambda b2r: ma(lambda a: a2mb(a)(b2r))
    #   callCC :: ((a -> CPS r b) -> CPS r a) -> CPS r a
    #       # == CPS (CPS r a) (a -> CPS r b)
    #       # <=[as-if]=> (a -> CPS r b)
    #       # <=[as-if]=> (a -> CPS r AnyThing)
    #   callCC f = (\k -> (f (\a -> (\_ -> k a))) k)
    #   callCC a2bEr_to_aEr = aEr@(\a2r -> r@(a2r_to_r@aEr@(a2bEr_to_aEr a2bEr@(\a -> bEr@b2r_to_r@(\_b2r -> a2r a))) a2r))
    #
    ###################
    #   but in Pzthon:
    #   tail :: r_middle -> r
    #   continuation :: () -> r
    #   # ctail :: continuation -> r # (() -> r_middle) -> r
    #   cps     :: continuation -> r # (()->r)->r
    #   cps(continuation) = r
    #   cps // continuation1 = continuation2 = lambda: cps(continuation1)
    #   cps1 ** cps2 = cps3 = lambda continuation: cps1(cps2 // continuation)
    #       cps ** (cps ** (...))
    #   tail1 >> tail2 >> tail3 = tail = lambda x: tail3(tail2(tail1(x)))
    #       ((...) >> tail) >> tail
    #   continuation1 >> tail = continuation2 = lambda: tail(continuation1())
    #   0) cps cor cps  # a cps again
    #       a cor b cor c = a ** b ** c
    #   1) cps cor: lazy_expr         # a normal value = cps(lambda: lazy_expr)
    #       cps1 cor: cps2 cor: expr = cps1(lambda: cps2(lambda:expr))
    #       val = dict.cps_get(key) cor: eval_default()
    #   2) return cps cor:
    #      body # no indent
    #
'''

from typing import TypeVar, Generic, Callable # Callable as typing_Callable

# Callable = typing_Callable

'''
class MyCallable:
    def __getitem__(self, ReturnT):
        return lambda *args: typing_Callable[list(args), ReturnT]
Callable = MyCallable()
# Callable[R](A,B)
# how to forbid some type in annotation?
#   e.g. how to avoid "Callable[R]" and force to be "Callable[R](A,B)"?
'''



R = TypeVar('R')
R2 = TypeVar('R2')
Middle_R = TypeVar('Middle_R')

#ContinuationF = Callable[R]()
ContinuationF = Callable[[], R]
class Continuation(Generic[R]):
    def __init__(self, f : ContinuationF) -> None:
        # Continuation <= ContinuationF
        assert callable(f)
        self.__continuation = f
    def __call__(self) -> R:
        return self.__continuation()
    def __rshift__(self, tail : 'Tail[R, R2]') -> 'Continuation[R2]':
        return Continuation(lambda: tail(self()))
    pass

#TailF = Callable[(Middle_R,), R]
TailF = Callable[[Middle_R], R]
class Tail(Generic[Middle_R, R]):
    def __init__(self, f : TailF) -> None:
        assert callable(f)
        self.__tail = f
    def __call__(self, middle_r:Middle_R) -> R:
        return self.__tail(middle_r)
    def __rshift__(self, tail : 'Tail[R, R2]') -> 'Tail[Middle_R, R2]':
        return Tail(lambda middle_r: tail(self(middle_r)))
    pass

continuation_f_Rstr : ContinuationF = lambda: ''
continuation_Rstr : Continuation[str] = Continuation(continuation_f_Rstr)
#tail_f_str2int : TailF = lambda (s:str): len(s)
tail_f_str2int : TailF = lambda s: len(s)
tail__str2int : Tail[str, int] = Tail(tail_f_str2int)
continuation_Rint : Continuation[int] = continuation_Rstr >> tail__str2int


CPS_F = Callable[[ContinuationF], R]
class CPS(Generic[R]):
    def __init__(self, cps : CPS_F) -> None:
        # CPS <= CPS_F
        assert callable(cps)
        self.__cps = cps
    def __call__(self, f : ContinuationF) -> R:
        return self.__cps(f)
    def __floordiv__(self, f : ContinuationF) -> Continuation[R]:
        return Continuation(lambda: self(f))
    def __pow__(self, cps : CPS_F) -> 'CPS[R]':
        return CPS(lambda continuation: self(lambda: cps(continuation)))





