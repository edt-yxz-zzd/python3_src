

r'''
Monad m ==>>
    haskell: m a === py: (~m. \a. (m, (@b. (a->b)-> m b))) a
that is too complex without typing
so here using a simpler version to ease debugging
    haskell: m a === py: (m -> (a, m) | MonadExcept)

functions work with Monad has form:
    (m, *args, **kwargs) -> (a, m)

'''


class MonadBaseException(BaseException):pass
class MonadExceptBase(BaseException):pass
    def __init__(self, m, *args, **kwargs):
        self.monad = m
        super().__init__(*args, **kwargs)
        return
class MonadErrorBase(BaseException):pass
class Monad:
    # immutable

    # can be override by their subclass
    MonadExcept = MonadExceptBase
    MonadError = MonadErrorBase
    def throw(self, *args, **kwargs):
        # noreturn
        # but should by called by:
        #   "raise self.throw(...)"
        raise self.MonadExcept(self, *args, **kwargs)
    def throwError(self, *args, **kwargs):
        # noreturn
        # but should by called by:
        #   "raise self.throwError(...)"
        raise self.MonadError(self, *args, **kwargs)
    @property
    def w(self):
        # self.w.m is self
        # self.w is (ref m); it is mutable
        return MonadWraper(self)
    '''
    def __init__(self, st:'immutable'):
        # m a === st val === (val, st)
        self.st = st

    def __ilshift__(self:'m', m_x:'m x === (m->(x,m)|MonadExcept)'):
        # (m, m -> (x, m)) -> m
        _x, m = m2mx(self)
        return m
    '''

def mkMonad(m_args_to_a_m, *args, **kwargs):
    # ((m, *args, **kwargs) -> (a, m)) -> ((m) -> (a, m))
    return lambda m: m_args_to_a_m(*args, **kwargs)
class MonadWraper:
    def __init__(self, m):
        self.m = m
    def call(self, m_args_to_a_m, *args, **kwargs):
        a, m = m_args_to_a_m(self, *args, **kwargs):
        self.m = m
        return a
    __call__ = call

def mapM(a2b, ma):
    return forM(ma, a2b)
def forM(ma, a2b):
    # forM = flip mapM = flip fmap
    def forM(self):
        a, m = ma(self)
        b = a2b(a)
        return b
    return forM
def seqM(ma_ls):
    # [m a] -> m [a]
    # [m->(a,m)] -> (m->([a],m))
    ma_ls = to_tuple(ma_ls)
    def seqM(self:'Monad'):
        f = MonadWraper(self)
        ls = []
        try:
            for ma in ma_ls:
                ls.append(f(ma))
        except f.m.MonadExcept:
            return ls, f.m
    return seqM
def to_tuple(ls):
    if isinstance(ls, tuple):
        return ls
    return tuple(ls)
def indexM(idx, ma_ls):
    ma_ls = to_tuple(ma_ls)
    ma_ls[idx] # check
    def indexM(self):
        ls, m = seqM(ma_ls)
        return ls[idx]
    return indexM
def lastM(ma_ls):
    return indexM(-1, ma_ls)
def firstM(ma_ls):
    return firstM(0, ma_ls)
def between(open, ma, close):
    return indexM(1, [open, ma, close])
def choiceM(ma_ls, *, err=None):
    i_mls = _choiceM_ex(ma_ls)
    def choiceM(self):
        i, mls = i_mls(self)
        return mls
    return choiceM
def choiceWithIndexM(ma_ls, *, err=None):
    i_mls = _choiceM_ex(ma_ls)
    def choiceM(self):
        i, (ls, m) = i_mls(self)
        return (i, ls), m
    retur choiceM
def _choiceM_ex(ma_ls, *, expected=None):
    # check, not empty
    ma_ls = to_tuple(ma_ls)
    if not ma_ls:
        def choiceM(self):
            if expected is None:
                raise self.throw('choiceM []')
            raise self.MonadExcept(expected)
    else:
        def choiceM(self):
            for i, ma in enumerate(ma_ls):
                try:
                    return i, ma(self)
                except self.MonadExcept:
                    continue
            else:
                if expected is None:
                    raise
                raise self.MonadExcept(expected)
    return choiceM

def raiseM(*args, **kwargs):
    # args for MonadExcept
    def raiseM(self):
        raise self.throw(*args, **kwargs)
    return raiseM
def notM(ma):
    ma = mayM(ma)
    # raise_ = raiseM('notM success_ma')
    def notM(self):
        may, m = ma(self)
        if may:
            raise self.throw('notM success_ma')
        assert m is self
        return may, m
def mayM(ma):
    # None | (a,)
    def mayM(self):
        try:
            a, m = ma(self)
            return (a,), m
        except self.MonadExcept:
            return None, self
    return mayM

def err_pairM(Error, ma, mb):
    # (?!a) -> raise MonadExcept
    # a (?!b) -> raise Error
    # a b -> (a,b)
    def err_pairM(self):
        m = self
        a, m = ma(m)
        try:
            r = mb(m)
        except self.MonadExcept:
            raise Error(m, "err_pairM a (?!b)")
        b, m = r
        return (a,b), m
    return err_pairM
def may_err_pairM(Error, ma, mb):
    # (?!a) -> None
    # a (?!b) -> raise Error
    # a b -> (a,b)
    ma = mayM(ma)
    mb = mayM(mb)
    def may_err_pairM(self):
        f = MonadWraper(self)
        may = f(ma)
        if may is None:
            return None, self
        [a] = may
        may = f(mb)
        if may is None:
            raise Error(f.m, "may_err_pairM a (?!b)")
        [b] = may
        return (a,b), f.m
    return may_err_pairM
def snd(ls):
    return ls[1]
class _Many1Error_private(Exception):pass
class _Many1SepError_private(Exception):pass
def iterMin(min):
    while True:
        yield min
        min += 1
def iterMax(max):
    return iterMinMax(0, max)
def iterMinMax(min, max):
    if max is None:
        return iterMin(min)
    return range(min, max)
def _handle_min_max(min, max):
    assert max is None or type(max) is int
    if min < 0:
        min = 0
    if max is not None:
        if min > max:
            raise ValueError('min > max')
    return min, max
def manyM(ma, *, min=0, max=None):
    # a{min,max} -> [a]
    # [min..max] not [min..max-1]
    min, max = _handle_min_max(min, max)
    def manyM(self:'Monad'):
        f = MonadWraper(self)
        ls = []
        try:
            for _ in iterMax(max):
                ls.append(f(ma))
            assert min <= len(ls) == max
        except self.MonadExcept:
            if len(ls) < min:
                raise
        return ls, f.m
    return manyM

def endByM(ma, end, *, min=0, max=None):
    # ((?!end) a)* end -> [a]
    min, max = _handle_min_max(min, max)
    may_end = mayM(end)
    def endByM(self:'Monad'):
        f = MonadWraper(self)
        ls = []
        for _ in iterMax(max):
            if f(may_end): break
            ls.append(f(ma))
        else:
            f(end)
        if len(ls) < min:
            raise self.MonadExcept('endByM: len(result) < min')
        return ls, f.m
    return endByM
def sepByM(ma, sep, *, min=0, max=None):
    # (a sep)* (a (?!sep)) | (?!a) -> [a]
    # (a sep)+ (?!a) -> raise MonadExcept
    min, max = _handle_min_max(min, max)
    may_sep = mayM(sep)
    def sepByM(self):
        f = MonadWraper(self)
        ls = []
        def body():
            for _ in iterMax(max if max is None else max-1):
                try:
                    a = f(ma)
                except self.MonadExcept as e:
                    if not ls:
                        return e, ls, f.m
                    raise
                ls.append(a)
                try:
                    f(sep)
                except f.m.MonadExcept as e:
                    return e, ls, f.m
            else:
                ls.append(f(ma))
                assert len(ls) == max
                return None, ls, f.m
        e, ls, m = body()
        if len(ls) < min:
            raise e
        return ls, m
    return sepByM




def many1M_ex(ma, *, sep=None, end=None, max=None):
    # many1(ma) = a+ (?!a) -> [a]
    # many1(ma, sep) = a (sep a)* (?!sep) -> [a]
    #               (a sep)* a (?!sep) -> [a]
    # many1(ma, sep, end) = a ((?!end) sep a)* end -> [a]
    # many1(ma, end) = ((?!end) a)+ end -> [a]
    return manyM_ex(ma, sep=sep, end=end, max=max, min=1)
def manyM_ex(ma, *, sep=None, end=None, min=0, max=None):
    # manyM/sepByM/endByM/manyM_ex
    # manyM_ex(ma, sep, end) = end | ((?!end) a) ((?!end) sep a)* end -> [a]
    # manyM_ex(ma, sep, end) = end | ((?!end) a) ((?!end) sep a)* end -> [a]
    if sep is None:
        if end is None:
            return manyM(ma, min=min, max=max)
        else:
            return endByM(ma, end, min=min, max=max)
    elif end is None:
        return sepByM(ma, end, min=min, max=max)
    assert sep is not None and end is not None
    min, max = _handle_min_max(min, max)
    may_end = mayM(end)
    def manyM_ex(self):
        def g():
            f = MonadWraper(self)
            ls = []
            # end
            if max < 1:
                f(end)
                return ls, f.m
            if f(may_end):
                return ls, f.m

            # a ...
            a = f(ma)
            ls.append(a)

            # [a] (end | sep a) ...
            for _ in iterMax(max if max is None else max-1):
                if f(may_end): break
                f(sep)
                ls.append(f(ma))
            else:
                f(end)
            return ls, f.m
        ls, m = g()
        if len(ls) < min:
            raise self.throw('manyM_ex: len(result) < min')
        return ls, m


def make_predicator(f):
    # callable or container
    return f if callable(f) else lambda x: x in f
def ors(default:bool, preds):
    # debug: call ors by: ors(True, *preds) # NOTE: the '*'
    # callable or container
    default = bool(default)
    if not preds:
        return lambda _: default
    return OrPredicators(preds)
class OrPredicators:
    def __init__(self, fs):
        # callable or container
        self.fs = tuple(map(make_predicator, fs))
    def __call__(self, x):
        for f in self.fs:
            if f(x):
                return True
        return False


class StreamMonadExcept(MonadExceptBase):pass
class Stream(Monad):
    MonadExcept = StreamMonadExcept
    def tell_pos(self):
        # m -> pos # pos may not be int!
        raise NotImplementedError
    def tell_eof(self):
        # m -> pos
        raise NotImplementedError
    def seek_pos(self, pos):
        # (m, pos) -> m
        raise NotImplementedError
    def read_le(self, n):
        # int -> ([token], remain_stream)
        raise NotImplementedError
    #def __iter__(self):
    def iter_pos_token_pairs(self):
        # [(pos, token)]
        try:
            while True:
                pos = self.tell_pos()
                ch = self.any_token()
                yield pos, ch
        except self.MonadExcept:
            return
    def is_eof(self):
        return self.tell_eof() == self.tell_pos()
    def eof(self):
        # parser version
        # see: is_eof
        if self.is_eof():
            raise self.throw('expected EOF')
        return None, self
    def read_to_pos(self, to_pos):
        # not:
        #   return read_le(to_pos-self.tell_pos())
        # since pos may not be int
        raise NotImplementedError
    def read_from_to(self, from_pos, to_pos):
        m = self.seek_pos(from_pos)
        return m.read_to_pos(to_pos)
    def read_eq(self, n):
        ls, ts = self.read_le(n)
        if len(ls) < n:
            raise self.throw('unexpected EOF: not enough tokens')
    def read_while(self, pred, *preds):
        pred = ors(False, pred, preds)
        f = self.w
        for pos, ch in self.iter_pos_token_pairs():
            if not pred(ch):
                break
        else:
            pos = self.tell_eof()
        return self.read_to(pos)
    def any_token(self):
        return self.read_eq(1)
    def any_token_if(self, *preds, charset_name="any_token"):
        ch, ts = self.read_eq(1)
        f = ors(True, preds)
        if f(ch):
            return ch, ts
        raise self.throw("excepted: {!r}".format(charset_name))
        ch, ts = self.any_token()
    def const_prefix(self, prefix):
        L = len(prefix)
        pre, ts = self.read_le(L)
        if pre != prefix:
            raise self.throw("expected: {!r}".format(prefix))
        return pre, ts



class ArrayStream(Stream):
    # immutable
    def tell_pos(self):
        # m -> pos # pos may not be int!
        return self.pos
    def tell_eof(self):
        # m -> pos
        return self.end
    def seek_pos(self, pos):
        # (m, pos) -> m
        return self.replace(pos=pos)
    def read_le(self, n):
        # int -> ([token], remain_stream)
        s, begin, end, pos = self.get_args()
        if n < 0:
            n = 0
        i = min(end, pos+n)
        return s[pos:i], self.replace(pos=pos)
    def __init__(self, s:'array', begin, end, pos):
        if not 0 <= begin <= pos <= end <= len(s):
            raise ValueError
        self.array = s
        self.begin = begin
        self.pos = pos
        self.end = end
    def as_array(self):
        s, begin, pos, end = self.get_args()
        return s[begin:end]
    def get_args(self):
        # s, begin, end, pos = self.get_args()
        return self.array, self.begin, self.end, self.pos

    def replace(self, begin=None, end=None, pos=None):
        if begin is None:
            begin = self.begin
        if end is None:
            end = self.end
        if pos is None:
            pos = self.pos
        return type(self)(self.array, begin, end, pos)
    def __len__(self):
        return self.end - self.begin
    def __repr__(self):
        return '{}{}'.format(type(self).__name__, self.get_args())
class CharStreamMixin:#(Stream):
    def spaces(self):
        return self.read_while(str.isspace)
    def skip_spaces(self):
        return self.spaces()[1]
    def read_idHead(self):
        return self.any_char(str.isalpha, '_', charset_name='idHead')
    def read_idNotHead(self):
        return self.any_char(str.isalnum, '_', charset_name='idNotHead')
    def read_identifier(self):
        ts = self
        h, ts = ts.read_idHead()
        s, ts = ts.read_while(str.isalnum, '_')
        return h+s, ts
    def any_alpha(self):
        return self.any_char(pred=str.isalpha, charset_name="alpha")
    def any_alnum(self):
        return self.any_char(pred=str.isalnum, charset_name="alpha_number")
    def any_char(self, *preds, charset_name="any_char"):
        return self.any_token(*preds, charset_name=charset_name)


class Str2Stream(ArrayStream, CharStreamMixin):
    def __init__(self, s:'str', begin, end, pos):
        assert type(s) is str
        super().__init__(s, begin, end, pos)
    def as_str(self):
        return self.as_array()

import Lazy
class LambdaGrammar:
    __grammar__ = '''
Expr-1 *= Abs
Expr-2 *= Apps
Atom-1 *= var
Atom-2 *=  -open $$ -spaces Expr -spaces -close
Abs = -lambda $$ -spaces var -spaces -dot -spaces Expr
# Apps = Atom+ Abs?
# Apps = Atom_spaces+ Abs?
# Atom_spaces *= Atom -spaces
Apps = Atom $$ spaces_Atom* spaces_Abs?
spaces_Atom *= -spaces Atom $$
spaces_Abs *= -spaces Abs $$
'''
    @property
    def GM_Expr(self):
        choices = Lazy(lambda:
                    choiceM([ self._GM_Expr_1
                            , self._GM_Expr_2
                            , self._GM_Expr_3]))
        def GM_Expr(m):
            a, m = choices.v(m)
            return self.G_Expr(a), m
        return GM_Expr
    @property
    def GM_Atom(self):
        return self.mkGM('Atom', '12')
    @property
    def GM_Abs(self):
        return self.mkGM('Abs', [''])
    @property
    def GM_Apps(self):
        return self.mkGM('Apps', [''])
    @property
    def GM_Atom_spaces(self):
        return self.mkGM('Atom_spaces', [''])
    def mkGM(self, name, indices:'[str]'):
        fmtAlt = '_GM_{}_{}'
        if not len(indices):
            indices = ['']
        attrs = map(lambda i: fmtAlt.format(name, i), indices)
        choices = Lazy(lambda:
                    choiceM(map(lambda attr: getattr(self, attr), attrs)))
        fmtG = 'G_{}'
        G_XXX = fmtG.format(name)
        G_XXX = getattr(self, G_XXX)
        def GM_XXX(m):
            a, m = choices.v(m)
            return G_XXX(a), m
        return GM_XXX

    @property
    def _GM_Expr_1(self):
        sel = [1]
        unbox = True
        seq = Lazy(lambda: compressM(
            [self.GM_Abs]
            , sel, unbox=unbox, map=self._G_Expr_1
            ))
        def _GM_Expr_1(m):
            return seq.v(m)
        return _GM_Expr_1
    @property
    def _GM_Expr_2(self):
        sel = [1]
        unbox = True
        names = 'Apps'.split()
        f = self._G_Expr_2
        return self.mk_GM(sel, unbox, names, f)

    @property
    def _GM_Atom_1(self):
        sel = [1]
        unbox = True
        names = 'var'.split()
        f = self._G_Atom_1
        return self.mk_GM(sel, unbox, names, f)
    @property
    def _GM_Atom_2(self):
        sel = [0, 0, 1, 0, 0]
        unbox = True
        names = 'open spaces Expr spaces close'.split()
        f = self._G_Atom_2
        return self.mk_GM(sel, unbox, names, f)
    def _GM_Abs_(self):
        sel = [0, 0, 1, 0, 0, 0, 1]
        unbox = False
        names = 'lambda spaces var spaces dot spaces Expr'.split()
        f = self._G_Abs_
        return self.mk_GM(sel, unbox, names, f)
    def _GM_Atom_spaces_(self):
        sel = [1, 0]
        unbox = True
        names = 'Atom spaces'.split()
        f = self._G_Atom_spaces_
        return self.mk_GM(sel, unbox, names, f)
    def mk_GM(self, sel, unbox, names, f):
        attrs = map('GM_{}'.format, names)
        seq = Lazy(lambda: compressM(
            map(lambda attr: getattr(self, attr), attrs)
            , sel, unbox=unbox, map=f
            ))
        def _GM_XXX(m):
            return seq.v(m)
        return _GM_XXX
    @property
    def _GM_Apps_(self):
        sel = [1, 1]
        unbox = False
        seq = Lazy(lambda: compressM(
            [many1M_ex(self.GM_Atom_spaces), mayM(self.GM_Abs)]
            , sel, unbox=unbox, map=self._G_Apps_
            ))
        def _GM_Apps_(m):
            return seq.v(m)
        return _GM_Apps_
    def _G_Apps_(self, x): return x
    def _G_Atom_spaces_(self, x): return x
    def _G_Abs_(self, x): return x
    def _G_Atom_2(self, x): return x
    def _G_Atom_1(self, x): return x
    def _G_Expr_1(self, x): return x
    def _G_Expr_2(self, x): return x
#def lazy_compressM(ma_ls, sel, unbox=False, map=None):
#    return Lazy(lambda: compressM(ma_ls, sel, unbox=unbox, map=map))
def compressM(ma_ls, sel, *, unbox=False, map=None):
    seq = seqM(ma_ls)
    def compressM(self):
        ls, m = seq(self)
        ls = list(compress(ls, sel))
        if unbox:
            [ls] = ls
        if map is not None:
            ls = map(ls)
        return ls, m
    return compressM



r'''
class Grammar:
    __grammar__ = """
A = B C* B/S$E+
B-1 = A Skip(Spaces) C
C = * Skip(Spaces) A Skip(Spaces) # unbox the singleton list
"""
    __parsed_grammar__ = OrderedDict(
        [ ('A', ['B', Star('C'), Many('B', sep='S', end='E', min=1)])
        , ('B-1', ['A', Skip('Spaces'), 'C'])
        , ('C', Unbox([Skip('Spaces'), 'A', Skip('Spaces')]))
        ]
    )
    @cached
    def GM_A(self)->m A:
        def GM_A(m):
            return mapM(self.G_A, choiceM([self._GM_A_])(m))
    @cached
    def _GM_A_(self)->m a:
        def _GM_A_(m):
            return mapM(composition(self.G_A, remove_skip), seqM([self.GM_B, ...])(m))

    def G_A(self, a)->A:
        default: return a
    def G_B(self, b)->B: # b is the result from _G_B_x
    def G_C(self, c)->C:
    def _G_A_(self, B_Cs_Bs:[B,[C...],[B...]])->a:
        default: return B_Cs_Bs
    def _G_B_1(self, A_C:[A,C])->b:
    def _G_C_(self, A)->c:
'''

