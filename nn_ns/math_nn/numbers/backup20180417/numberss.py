
import itertools


class NumberList:
    def _calc_neg(self, n, nums):
        raise NotImplementedError
    def _calc_pos(self, n, nums):
        raise NotImplementedError
    def direct_calc(self, n):
        raise NotImplementedError
    def _fill_when_neg(self, n):
        raise NotImplementedError
    
    def __init__(self, init_values=()):
        self.nums = list(init_values)

    def lookup(self, n):
        '''without fill'''
        if n >= 0:
            return self.nums[n]
        return self.calc_neg(n)

    def calc_neg(self, n):
        '''without fill'''
        assert n < 0

        return self._calc_neg(n, self.nums)
    
    def calc_pos(self, n):
        '''without fill; using calc_neg and lookup;

assume nums[m] is known for m < n'''
        assert n >= 0
        assert len(self.nums) >= n

        return self._calc_pos(n, self.nums)
    
    

    def fill_next_pos(self):
        n = len(self.nums)
        p = self.calc_pos(n)
        self.nums.append(p)
        return
    def fill_len(self, L):
        for _ in range(len(self.nums), L):
            self.fill_next_pos()
        assert len(self.nums) >= L
        return

    def fill_then_lookup(self, n):
        if n >= 0:
            self.fill_len(n+1)
        else:
            self._fill_when_neg(n)
        return self.lookup(n)

    def __iter__(self):
        return self.iter()
    def iter(self, begin=0, step=1):
        for i in itertools.count(begin, step):
            yield self(i)
        
    def __call__(self, n):
        return self.fill_then_lookup(n)

    def get_least_len(self, L):
        self.fill_len(L)
        return self.nums
    def get_first(self, L):
        return self.get_least_len(L)[:L]

    def direct_first(self, n):
        '''direct_calc --> fill_lookup'''
        try:
            return self.direct_calc(n)
        except NotImplementedError:
            return self(n)
    def lookup_first(self, n):
        '''lookup_without_fill --> direct_calc --> fill_lookup'''
        if 0 <= n < len(self.nums):
            return self(n)
        return self.direct_first(n)
    pass

class NumberList__neg2zero(NumberList):
    def _calc_neg(self, n, nums):
        return 0
    def _calc_pos(self, n, nums):
        raise NotImplementedError
    def direct_calc(self, n):
        if n < 0:
            return 0
        raise NotImplementedError
    def _fill_when_neg(self, n):
        pass


        

class NumberTable:
    def _calc_neg(self, n, k, table):
        raise NotImplementedError
    def _calc_pos(self, n, k, table):
        raise NotImplementedError
    def _calc_pos_beyond(self, n, k, table):
        raise NotImplementedError
    def direct_calc(self, n, k):
        raise NotImplementedError
    def row_len(self, n):
        return n+1
    def _fill_when_neg(self, n):pass
    
        
    def __init__(self, init_table=()):
        self.table = list(list(row) for row in init_table)
        assert all(len(row) == self.row_len(n) for n, row in enumerate(self.table))
        
        

    def lookup(self, n, k):
        '''without fill'''
        if n < 0:
            return self.calc_neg(n, k)
        if 0 <= k < len(self.table[n]):
            return self.table[n][k]
        return self.calc_pos_beyond(n,k)
        

    def calc_neg(self, n, k):
        '''without fill'''
        assert n < 0

        return self._calc_neg(n, k, self.table)

    def calc_pos_beyond(self, n, k):
        '''without fill'''
        assert n >= 0

        return self._calc_pos_beyond(n, k, self.table)
    
    def calc_pos(self, n, k):
        '''without fill; using calc_neg and lookup;

assume nums[m] is known for m < n'''
        assert n >= 0
        assert len(self.table) > n
        assert len(self.table[n]) >= k

        return self._calc_pos(n, k, self.table)
    
    

    def fill_next_pos(self, n):
        row = self.table[n]
        k = len(row)
        p = self.calc_pos(n, k)
        row.append(p)
        return

    def fill_row(self, n):
        L = self.row_len(n)
        assert L >= 0
        
        row = self.table[n]
        for _ in range(len(row), L):
            self.fill_next_pos(n)
        assert len(row) == L
        return
    
    def fill_len(self, L):
        table = self.table
        for n in range(len(table), L):
            table.append([])
            self.fill_row(n)
        assert len(table) >= L
        return

    def fill_then_lookup(self, n, k):
        if n >= 0:
            self.fill_len(n+1)
        else:
            self._fill_when_neg(n)
        return self.lookup(n, k)

    def __call__(self, n,k=None):
        if k is None:
            return self.get_row(n)
        return self.fill_then_lookup(n,k)

    def get_least_len(self, L):
        self.fill_len(L)
        return self.table
    def get_first(self, L):
        return self.get_least_len(L)[:L]
    def get_row(self, row):
        assert row >= 0
        return self.get_least_len(row+1)[row]

    def direct_first(self, n,k):
        '''direct_calc --> fill_lookup'''
        try:
            return self.direct_calc(n,k)
        except NotImplementedError:
            return self(n,k)
    def lookup_first(self, n,k):
        '''lookup_without_fill --> direct_calc --> fill_lookup'''
        if 0 <= n < len(self.table) and 0 <= k < len(self.table[n]):
            return self(n,k)
        return self.direct_first(n,k)

    pass

        
