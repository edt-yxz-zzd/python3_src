
'''
number_table[n][i]
    | 0<=i<=n   = ???
    | otherwise = raise
'''

__all__ = '''
    INumberTable
    INumberTable__table__concrete_mixins
    '''.split()



from .numbers_common import\
    (ABC, optional_method, abstract_method, override, define)


class UndefinedError(NameError):
    # e.g. table[-1][-3] is undefined, a hole
    pass
class INumberTable(ABC):
    '''INumberTable for calc/cache a number table

table
    # complete_table - grow_only_complete_table - complete_rows
    all(len(row) == row_len(n) for n, row in enumerate(table))
incomplete_table
    # temp_incomplete_table
    all(len(row) == row_len(n) for n, row in enumerate(table[:-1]))
    not table or len(table[-1]) <= row_len(len(table)-1)

abstract_method:
    get_table
    _calc_pos
    row_len
optional_method:
    lookup_static
    _lookup_pos_overflow
    _lookup_pos_underflow
    direct_calc
    _fill_when_neg
        # a "to be overrided" version of fill_when_neg
        # fill_when_neg try lookup_static first, may bypass _fill_when_neg
    _lookup_neg
        # lookup_static is a fallback of _lookup_neg in lookup
other_method:
    fill_when_neg
    lookup
    _lookup
        # a "free table" version of lookup
        # so, can be used in other "free table" method
    _lookup_pos_beyond
    __fill_next_pos
    __fill_row
    fill_len
    _fill_len
        # a "free table" version of fill_len
    lookup_static_first_else_fill_then_lookup
    __call__
    get_least_len
    get_first
    get_row
    direct_first
    lookup_first

neg - means n < 0
pos - means n >= 0
overflow - means n >= 0, k >= row_len(n)
underflow - means n >= 0, k < 0
'''
    __slots__ = ()

    ####### abstract_method

    @abstract_method
    def get_table(self):
        # -> [[num]]
        # for __slots__ == ()
        raise NotImplementedError
    @abstract_method
    def _calc_pos(self, n, k, incomplete_table):
        '''without fill; use cached table

precondition:
    0 <= n < len(incomplete_table)
    0 <= k <= min(len(incomplete_table[n]), row_len(n)-1)
    incomplete_table :: [[num]]
        incomplete_table[:n] is complete_table
        incomplete_table[n] may be incomplete
postcondition:
    should not raise
'''
        assert 0 <= n < len(incomplete_table)
        assert 0 <= k <= min(len(incomplete_table[n]), self.row_len(n)-1)
        raise NotImplementedError

    @abstract_method
    def row_len(self, n):
        '''len(final complete row n) = len(table[n])

precondition:
    n >= 0
postcondition:
    output >= 0
'''
        assert n >= 0
        raise NotImplementedError
        return n+1





    ###### optional_method

    @optional_method
    def lookup_static(self, n, k):
        '''lookup_static; donot use cached table

like direct_calc, but should be O(1)
e.g.
    choose n i | i < 0 = 0
    ballot p q | not (0 <= p <= q) = 0

precondition:
    any n, any k
postcondition:
    may raise LookupError/UndefinedError
'''
        raise LookupError

    @optional_method
    def _lookup_pos_underflow(self, n, k, table):
        '''without fill; use cached table

e.g.
    * table[n][k] = 0 if k < 0
    * table[n][k] = table[n][0] if k < 0
precondition:
    n >= 0
    k < 0
    table[:n] is complete_table
postcondition:
    may raise LookupError/UndefinedError
    if 0 <= n <= len(table):
        should not raise LookupError
'''
        assert n >= 0
        assert k < 0
        raise UndefinedError


    @optional_method
    def _lookup_pos_overflow(self, n, k, table):
        '''without fill; use cached table

e.g.
    * table[n][k] = 0 if k >= row_len(n)
    * table[n][k] = table[n][-1] if k >= row_len(n)
precondition:
    n >= 0
    k >= row_len(n)
    table[:n+1] is complete_table
postcondition:
    may raise LookupError/UndefinedError
    if 0 <= n < len(table):
        should not raise LookupError
'''
        assert n >= 0
        assert k >= self.row_len(n)
        raise UndefinedError


    @optional_method
    def direct_calc(self, n, k):
        '''without fill; donot use cached table

precondition:
    any n, any k
postcondition:
    may raise NotImplementedError/UndefinedError
        * no defined for (n,k)
        * if n >= 0 and 0 <= k < row_len(n) but no better method than use cached table
'''
        raise NotImplementedError



    @optional_method
    def _lookup_neg(self, n, k, table):
        '''without fill; lookup when n < 0; use cached table

should be O(1)
need not call lookup_static
    used only in lookup, which will fallback to lookup_static

precondition:
    n < 0, any k
postcondition:
    may raise LookupError/UndefinedError
'''
        raise LookupError
    @optional_method
    def _fill_when_neg(self, n, k):
        '''fill cached table so that we can lookup (n, k); n < 0


precondition:
    n < 0
postcondition:
    may raise NotImplementedError
    if success:
        ## no: _lookup_neg(n,k) should not raise LookupError
        lookup(n,k) should not raise LookupError
            # may raise UndefinedError
            i.e. lookup_static(n,k) or _lookup_neg(n,k)
                should not raise LookupError
'''
        assert n < 0
        raise NotImplementedError
        pass

    @define
    def fill_when_neg(self, n, k):
        'see: _fill_when_neg which is to be overrided\n'
        try:
            self.lookup_static(n,k)
            # need not fill
            # since lookup_static knowns answer
            return
        except LookupError:
            pass
        self._fill_when_neg(n,k)
    fill_when_neg.__doc__ += _fill_when_neg.__doc__




    @define
    def _lookup(self, n, k, table):
        '''without fill; use cached table

precondition:
    any n, any k
postcondition:
    may raise LookupError/UndefinedError

    if n >= 0 and 0 <= k < row_len(n):
        after fill_len(n+1):
            lookup(n,k) should not raise

    if n < 0:
        after fill_when_neg(n,k):
            lookup(n,k) should not raise LookupError
                # may raise UndefinedError
'''
        if n < 0:
            try:
                return self._lookup_neg(n, k, table)
            except LookupError:
                pass
        else:
            # n >= 0
            if 0 <= k < len(table[n]):
                return table[n][k]
            if not (0 <= k < self.row_len(n)):
                # _lookup_pos_beyond call lookup_static
                return self._lookup_pos_beyond(n,k, table)

        return self.lookup_static(n, k)
    @define
    def lookup(self, n, k):
        'see: _lookup which is a "free table" version\n'
        table = self.get_table()
        return self._lookup(n,k, table)
    lookup.__doc__ += _lookup.__doc__




    @define
    def _lookup_pos_beyond(self, n, k, table):
        '''without fill; use cached table; try lookup_static first

e.g. table[n][k] = 0 if not (0 <= k < row_len(n))
precondition:
    None
postcondition:
    may raise ValueError/LookupError/UndefinedError

    if n >= 0 and not (0 <= k < row_len(n)):
        should not raise ValueError
    if k < 0 and 0 <= n <= len(table):
        should not raise LookupError
    if k >= row_len(n) and 0 <= n < len(table):
        should not raise LookupError
'''
        if not (n >= 0): raise ValueError
        if 0 <= k < self.row_len(n): raise ValueError

        try:
            return self.lookup_static(n,k)
        except LookupError:
            pass

        if k < 0:
            #if not (0 <= n <= len(table)): raise LookupError # k < 0
            return self._lookup_pos_underflow(n, k, table)

        #if not (0 <= n < len(table)): raise LookupError # k >= row_len(n)
        return self._lookup_pos_overflow(n, k, table)
















    ###### fill
    @define
    def __fill_next_pos(self, n, incomplete_table):
        '''fill table[n] with 1 more element unless already complete

precondition:
    0 <= n < len(incomplete_table)
    incomplete_table :: [[num]]
        incomplete_table[:n] is complete_table
        incomplete_table[n] may be incomplete
postcondition:
    len(post_incomplete_table[n]) ==
        bool(len(pre_incomplete_table[n]) < row_len(n))
        + len(pre_incomplete_table[n])
'''
        assert 0 <= n < len(incomplete_table)
        L = self.row_len(n)
        incomplete_row = incomplete_table[n]
        k = len(incomplete_row)
        if k >= L:
            # already complete
            return

        # exist and incomplete
        assert 0 <= k < L
        p = self._calc_pos(n, k, incomplete_table)
        incomplete_row.append(p)
        assert len(incomplete_row) <= L
        return

    @define
    def __fill_row(self, n, incomplete_table):
        '''fill table[n] until complete

precondition:
    0 <= n < len(incomplete_table)
    incomplete_table :: [[num]]
        incomplete_table[:n] is complete_table
        incomplete_table[n] may be incomplete
postcondition:
    incomplete_table[n] is complete row
    i.e. len(incomplete_table[n]) >= row_len(n)
'''
        assert 0 <= n < len(incomplete_table)
        L = self.row_len(n)
        assert L >= 0

        incomplete_row = incomplete_table[n]
        if len(incomplete_row) >= L:
            return
        for _ in range(len(incomplete_row), L):
            self.__fill_next_pos(n, incomplete_table)
        assert len(incomplete_row) == L
        return

    @define
    def fill_len(self, L):
        '''fill until len(table) >= L

precondition:
    None
postcondition:
    len(post_self.get_table()) >= L
    if 0 <= n < L and 0 <= k < row_len(n):
        lookup(n, k) should not raise
'''
        self._fill_len(L, self.get_table())
        return
    @define
    def _fill_len(self, L, incomplete_table):
        '''fill incomplete_table until complete row (L-1) occur if L > 0

precondition:
    any L
    incomplete_table
        may be incomplete
        i.e. incomplete_table[-1] if exist may be incomplete row
postcondition:
    len(incomplete_table) >= L
    incomplete_table[:L] is complete_table
        i.e. not incomplete_table or len(incomplete_table[L-1]) == row_len(L-1)
'''
        begin = len(incomplete_table)
        if begin > 0:
            self.__fill_row(begin-1, incomplete_table)
        for n in range(begin, L):
            incomplete_table.append([])
            self.__fill_row(n, incomplete_table)
        assert len(incomplete_table) >= L
        return






    @define
    def lookup_static_first_else_fill_then_lookup(self, n, k):
        '''fill enough elements to lookup, return lookup result

precondition:
    any n, any k
postcondition:
    may raise NotImplementedError/UndefinedError
    if n >= 0 and 0 <= k < row_len(n):
        lookup_static_first_else_fill_then_lookup(n,k) should not raise
'''
        try:
            return self.lookup_static(n, k)
        except LookupError:
            pass

        if n >= 0:
            self.fill_len(n+1) # should not raise
        else:
            self.fill_when_neg(n,k) # may raise NotImplementedError
        return self.lookup(n,k)  # may raise UndefinedError


    @define
    def __call__(self, n, k=None):
        '''will fill
    self(n,k) =[def]= self.lookup_static_first_else_fill_then_lookup(n,k)
    self(n) =[def]= self.get_row(n)

precondition:
    * any int n, k is None
    * any int n, any int k
postcondition:
    may raise LookupError/NotImplementedError/UndefinedError

    * any int n, k is None
        if n < 0: raise LookupError
        if n >= 0:
            self(n) should not raise
    * any int n, any int k
        may raise NotImplementedError/UndefinedError
        if n >= 0 and 0 <= k < row_len(n):
            self(n,k) should not raise
'''
        if k is None:
            return self.get_row(n) # LookupError
        return self.lookup_static_first_else_fill_then_lookup(n,k)

    @define
    def get_least_len(self, L):
        '''will fill

precondition:
    any int L
postcondition:
    len(post_self.get_table()) >= L
output:
    output_table is a complete_table
    len(output_table) >= L
    output_table should not be modified
'''
        self.fill_len(L)
        return self.get_table()
    @define
    def get_first(self, L):
        '''will fill

precondition:
    any int L
postcondition:
    len(post_self.get_table()) >= L
output:
    output_table is a complete_table
    len(output_table) == max(0,L)
    output_table should not be modified
'''
        return self.get_least_len(L)[:L]

    @define
    def get_row(self, n):
        '''will fill
    get_row(n) =[def]= get_least_len(n+1)[n]

precondition:
    any int n
postcondition:
    may raise LookupError
    if n < 0: raise LookupError
    if n >= 0: should not raise
'''
        if not n >= 0: raise LookupError
        return self.get_least_len(n+1)[n]

    @define
    def direct_first(self, n,k):
        '''may fill
    try direct_calc first, if fail then use lookup_static_first_else_fill_then_lookup

precondition:
    any n, any k
postcondition:
    may raise NotImplementedError/UndefinedError
'''
        try:
            return self.direct_calc(n,k) # NotImplementedError/UndefinedError
        except NotImplementedError:
            pass
        return self.lookup_static_first_else_fill_then_lookup(n,k)
            # NotImplementedError/UndefinedError
    @define
    def lookup_first(self, n, k):
        '''try lookup first, if fail than use direct_first

precondition:
    any n, any k
postcondition:
    may raise UndefinedError/NotImplementedError
'''
        table = self.get_table()
        # what if n < 0?
        #   if 0 <= n < len(table) and 0 <= k < len(table[n]): return self(n,k)
        try:
            self.lookup(n,k) # LookupError/UndefinedError
        except LookupError:
            pass
        return self.direct_first(n,k)
            # NotImplementedError/UndefinedError







    # delete calc_pos
    """
    @define
    def calc_pos(self, n, k):
        '''without fill; using lookup;

see: _calc_pos
precondition:
    None
postcondition:
    may raise ValueError
        * if not (0 <= n < len(table))
        * if not (0 <= k <= min(len(table[n]), row_len(n)-1))

assume table[n][k] = f(table[:n], table[n][:k])
'''
        table =self.get_table()
        if not (0 <= n < len(table)): raise ValueError
        if not (0 <= k <= min(len(table[n]), self.row_len(n)-1)): raise ValueError

        return self._calc_pos(n, k, table)
    """



    '''
    @define
    def exist_row(self, n):
        return 0 <= n < len(self.get_table())
    @define
    def exist_complete_row(self, n):
        return (self.exist_row(n)
            and len(self.get_table()[n]) == self.row_len(n)
            )
    '''






    # delete _calc_neg calc_neg
    """
    @optional_method
    def _calc_neg(self, n, k, table):
        '''
may override fill_when_neg too
'''
        raise NotImplementedError

    @define
    def calc_neg(self, n, k):
        '''without fill; use cached table

see: _calc_neg

precondition:
    any n, any k
postcondition:
    may raise ValueError/LookupError/NotImplementedError

    if not n < 0: raise ValueError
    should not raise LookupError if n==-1
    if n+1 < 0:
        after fill_when_neg(n+1,k):
            calc_neg(n,k) should not raise LookupError
'''
        if not n < 0: raise ValueError
        return self._calc_neg(n, k, self.get_table())
    """
    pass


class INumberTable__table__concrete_mixins(INumberTable):
    '''INumberTable mixins for calc/cache a number table
    "concrete" means should be base class of concrete class

abstract_method:
    _calc_pos
    __please_add_table_to_slots__
'''
    __slots__ = ()
    @abstract_method
    def __please_add_table_to_slots__(self):
        '__slots__ = (..., "table")'
        pass

    @override
    def get_table(self):
        return self.table

    @override
    def __init__(self, init_table=()):
        self.table = table = list(list(row) for row in init_table)
        assert all(len(row) == self.row_len(n) for n, row in enumerate(table))



