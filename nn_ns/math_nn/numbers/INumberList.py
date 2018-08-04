
'''
number_table[n][i]
    | 0<=i<=n   = ???
    | otherwise = raise
'''

__all__ = '''
    INumberList
    INumberList__neg2zero
    INumberList__nums__concrete_mixins
    '''.split()


from .numbers_common import\
    (ABC, optional_method, abstract_method, override, define)
import itertools # for count


class INumberList(ABC):
    '''INumberList for calc/cache a number sequence

abstract_method:
    get_nums
    _calc_pos
optional_method:
    _lookup_neg
    _calc_neg
    direct_calc
    _fill_when_neg

other_method:
    lookup
    calc_neg
    calc_pos
    fill_next_pos
    fill_len
    fill_then_lookup
    __iter__
    iter
    __call__
    get_least_len
    get_first
    direct_first
    lookup_first
'''
    __slots__ = ()

    ####### abstract_method

    @abstract_method
    def get_nums(self):
        # -> [num]
        # for __slots__ == ()
        raise NotImplementedError

    @abstract_method
    def _calc_pos(self, n, nums):
        '''without fill; use cached list

precondition:
    0 <= n <= len(nums)
postcondition:
    may raise LookupError
    after fill_len(n):
        _calc_pos(n) should not raise LookupError
'''
        assert 0 <= n <= len(nums)
        if n < len(nums):
            return nums[n]
        raise NotImplementedError


    ####### optional_method

    @optional_method
    def _lookup_neg(self, n, nums):
        '''without fill; use cached list

like _calc_neg but should be O(1)

precondition:
    n < 0
postcondition:
    may raise LookupError
    after _fill_when_neg(n):
        _lookup_neg(n) should not raise LookupError
'''
        assert n < 0
        raise LookupError

    @optional_method
    def _calc_neg(self, n, nums):
        '''without fill; use cached list

like direct_calc, but use cached list
may want to override _fill_when_neg too

precondition:
    n < 0
postcondition:
    may raise LookupError/NotImplementedError
    should not raise LookupError if n==-1
    if n+1 < 0:
        after _fill_when_neg(n+1):
            _calc_neg(n) should not raise LookupError
'''
        assert n < 0
        raise NotImplementedError

    @optional_method
    def direct_calc(self, n):
        '''without fill; donot use cached list

precondition:
    any n
postcondition:
    may raise NotImplementedError
        * if n < 0 and no defined for n
        * if n >= 0 and no better method than use cached list
'''
        raise NotImplementedError

    @optional_method
    def _fill_when_neg(self, n):
        '''fill cached list so that we can lookup [n..-1]; n < 0


precondition:
    n < 0
postcondition:
    may raise NotImplementedError
    if success:
        _lookup_neg(n) should not raise
        _calc_neg(n-1) should not raise LookupError
        calc_neg(n-1) should not raise LookupError
'''
        assert n < 0
        raise NotImplementedError
        return # no effect


    @define
    def lookup(self, n):
        '''without fill; use cached list

precondition:
    any n
postcondition:
    may raise LookupError

    if n >= 0:
        after fill_len(n+1):
            lookup(n) should not raise

    after _fill_when_neg(n) if n<0:
        lookup(n) should not raise
'''
        if n >= 0:
            return self.get_nums()[n]
        return self._lookup_neg(n, self.get_nums())

    @define
    def calc_neg(self, n):
        '''without fill; use cached list

see: _calc_neg

precondition:
    any n
postcondition:
    may raise ValueError/LookupError/NotImplementedError

    if not n < 0: raise ValueError
    should not raise LookupError if n==-1
    if n+1 < 0:
        after _fill_when_neg(n+1):
            calc_neg(n) should not raise LookupError
'''
        if not n < 0: raise ValueError
        return self._calc_neg(n, self.get_nums())

    @define
    def calc_pos(self, n):
        '''without fill; use cached list

see: _calc_pos
assume nums[n] = calc_pos(nums[:n])

precondition:
    0 <= n <= len(nums)
postcondition:
    may raise ValueError/LookupError

    if not (0 <= n <= len(nums)): raise ValueError
    after fill_len(n):
        calc_pos(n) should not raise LookupError

'''
        if not (0 <= n <= len(self.get_nums())): raise LookupError
        return self._calc_pos(n, self.get_nums())



    @define
    def fill_next_pos(self):
        '''fill 1 more num

precondition:
    None
postcondition:
    len(post_self.get_nums()) == 1+len(pre_self.get_nums())

'''
        n = len(self.get_nums())
        p = self.calc_pos(n)
        self.get_nums().append(p)
        return

    @define
    def fill_len(self, L):
        '''fill until total at least L numbers

precondition:
    None
postcondition:
    len(post_self.get_nums()) >= L
    if 0 <= n < L:
        lookup(n) should not raise
    if 0 <= n <= L:
        _calc_pos(n) should not raise LookupError
        calc_pos(n) should not raise LookupError/ValueError
'''
        for _ in range(len(self.get_nums()), L):
            self.fill_next_pos()
        assert len(self.get_nums()) >= L
        return

    @define
    def fill_then_lookup(self, n):
        '''fill enough elements to lookup, return lookup result

precondition:
    None
postcondition:
    may raise NotImplementedError
    if n >= 0:
        fill_then_lookup(n) should not raise
'''
        if n >= 0:
            self.fill_len(n+1) # should not raise
        else:
            self._fill_when_neg(n) # may raise NotImplementedError
        return self.lookup(n)  # should not raise


    @define
    def __iter__(self):
        'iter nums[0..+oo]'
        return self.iter()
    @define
    def iter(self, begin=0, step=1):
        'iter nums[begin, step..+oo]'
        for i in itertools.count(begin, step):
            yield self(i)

    @define
    def __call__(self, n):
        'self(n) =[def]= self.fill_then_lookup(n)'
        return self.fill_then_lookup(n)

    @define
    def get_least_len(self, L):
        'len(output_nums) >= L; should not modify it'
        self.fill_len(L)
        return self.get_nums()
    @define
    def get_first(self, L):
        'len(output_nums) == L; should not modify it'
        return self.get_least_len(L)[:L]

    @define
    def direct_first(self, n):
        '''try direct_calc first, if fail then use fill_then_lookup'''
        try:
            return self.direct_calc(n)
        except NotImplementedError:
            return self.fill_then_lookup(n)

    @define
    def lookup_first(self, n):
        '''try lookup first, if fail than use direct_first'''
        #if 0 <= n < len(self.get_nums()): return self.lookup(n)
        #   what if n < 0???
        try:
            return self.lookup(n)
        except (LookupError, NotImplementedError):
            return self.direct_first(n)
    pass

class INumberList__neg2zero(INumberList):
    '''INumberList mixins for calc/cache a number sequence s.t. seq[-n]=0

abstract_method:
    get_nums
    _calc_pos
'''
    __slots__ = ()

    @override
    def _calc_neg(self, n, nums):
        '''without fill

precondition:
    n < 0
postcondition:
    always return 0
'''
        assert n < 0
        return 0


    @override
    def direct_calc(self, n):
        '''without fill; donot use cached list

precondition:
    any n
postcondition:
    may raise NotImplementedError
        iff n >= 0 and no better method than use cached list

    if n < 0:
        return 0
'''

        if n < 0:
            return 0
        raise NotImplementedError


    @override
    def _fill_when_neg(self, n):
        # need not fill
        pass
    _fill_when_neg.__doc__ = INumberList._fill_when_neg.__doc__




class INumberList__nums__concrete_mixins(INumberList):
    '''INumberList mixins for calc/cache a number sequence
    "concrete" means should be base class of concrete class

abstract_method:
    _calc_pos
    __please_add_nums_to_slots__
'''
    __slots__ = ()
    @abstract_method
    def __please_add_nums_to_slots__(self):
        '__slots__ = (..., "nums")'
        pass

    @override
    def get_nums(self):
        return self.nums

    @override
    def __init__(self, init_values=()):
        self.nums = list(init_values)




