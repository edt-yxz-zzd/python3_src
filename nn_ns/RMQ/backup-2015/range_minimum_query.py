
'''
range minimum query (RMQ)

RMQ[array](i,j) ::= arg[k] min((array[k], k) for k in [i..j-1])


'''

'''
normal blocks: |--0--|....|--i--|--i+1--|...
super  blocks: |--0--|..|--k--|--k+1--|...
if begin of normal_block in the super_block, then normal block belong to super_block
i to k; i+1 to k+1;

but array_idx j which in normal block i, may be in super block k+1

'''

from .Catalan_number import Catalan_number
from .ballot_number import encode_binary_tree_struct_of_canonical_Cartesian_tree_of_array_of_same_length \
     as _encode

debug = 0


def max_twopow_le(n):
    assert n > 0
    return 1 << (n.bit_length()-1)
class range_minimum_query:
    def __init__(self, array):
        self.n = len(array)
        self.array = array
        self.super_block_size, self.num_super_blocks, \
           self.normal_block_size, self.num_normal_blocks, \
           self.max_power_for_superblock, \
           self.num_normal_blocks_in_one_superblock,\
           self.max_power_for_normalblock,\
           self.super_block2minidx_in_next_twopow_superblocks, \
           self.normal_block2offseted_minidx_in_next_twopow_normalblocks, \
           self.normal_block2code, self.code2offseted_inblock_query_table = \
           range_minimum_query_args(array)


        if debug:
            block2power2minidx = self.normal_block2offseted_minidx_in_next_twopow_normalblocks
            block_size = self.normal_block_size
            begin = 0
            for block, power2minidx in enumerate(block2power2minidx):
                offset = begin + block * block_size
                super_block = self.in_which_superblock(offset)
                minidx_offset = self.first_normalblock_in_superblock(super_block)*block_size
                
                for power, minidx in enumerate(power2minidx):
                    to = offset + block_size * (1<<power)
                    subarray = array[offset: to]
                    minidx += minidx_offset
                    if not (minidx) == offset + subarray.index(min(subarray)):
                        print('array', array)
                        print('minidx', minidx)
                        print(offset, to, subarray, subarray.index(min(subarray)))
                        print('power2minidx', power2minidx)
                        print('power', power)
                        print('block', block)
                        print('block_size', block_size)
                        print('block2power2minidx', block2power2minidx)
                    assert minidx == offset + subarray.index(min(subarray))
                
    def __call__(self, i, j):
        return self.query(i,j)
    def query(self, i, j):
        assert 0 <= i < j <= self.n
        normal_head_begin = self.in_which_normalblock(i)
        normal_tail_end = self.in_which_normalblock(j)
        normal_L = normal_tail_end - normal_head_begin

        # in-normal-block-query
        if normal_L == 0:
            mins_in_one_normalblock = self.in_one_normalblock_query(normal_head_begin, i, j)
            r, = mins_in_one_normalblock
            return r
        
        assert normal_L >= 1
        array_head_end = (normal_head_begin+1) * self.normal_block_size
        mins1_in_one_normalblock = self.in_one_normalblock_query(normal_head_begin, i, array_head_end)
        
        array_tail_begin = normal_tail_end * self.normal_block_size
        mins2_in_one_normalblock = self.in_one_normalblock_query(normal_tail_end, array_tail_begin, j)
        mins_in_one_normalblock = mins1_in_one_normalblock + mins2_in_one_normalblock


        # blocks
        super_begin = self.in_which_superblock(array_head_end)
        super_end = self.in_which_superblock(array_tail_begin)
        super_L = super_end - super_begin
        
        normal_head_begin = self.in_which_normalblock(array_head_end)
        normal_tail_end = self.in_which_normalblock(array_tail_begin)
        normal_L = normal_tail_end - normal_head_begin

        # in super block query
        if super_L == 0:
            mins_in_one_superblock = self.in_one_superblock_query(
                super_begin, normal_head_begin, normal_tail_end)
            pass
        elif super_L >= 1:
            normal_head_end = self.first_normalblock_in_superblock(super_begin+1)
            normal_tail_begin = self.first_normalblock_in_superblock(super_end)
            mins1 = self.in_one_superblock_query(super_begin, normal_head_begin, normal_head_end)
            mins2 = self.in_one_superblock_query(super_end, normal_tail_begin, normal_tail_end)

            pre_tail = normal_tail_begin-1
            pre_tail_array_end = normal_tail_begin * self.normal_block_size
            pre_tail_array_begin = pre_tail_array_end - self.normal_block_size
            mins3 = self.in_one_normalblock_query(pre_tail, pre_tail_array_begin, pre_tail_array_end)
            mins_in_one_superblock = mins1 + mins2 + mins3


        # cross super blocks query
        if super_L > 1:
            mins_cross_superblocks = self.cross_superblocks_query(super_begin+1, super_end)
        else:
            mins_cross_superblocks = []

        min_idc = mins_in_one_normalblock + mins_in_one_superblock + mins_cross_superblocks
        min_idc.sort() # bug : without this
        min_values = [self.array[i] for i in min_idc]
        m = min(min_values)
        i = min_values.index(m)
        return min_idc[i]


    def first_normalblock_in_superblock(self, super_block):
        array_idx = super_block * self.super_block_size
        normal_block = self.in_which_normalblock(array_idx)
        if normal_block * self.normal_block_size < array_idx:
            normal_block += 1

        assert normal_block == (array_idx + self.normal_block_size-1)//self.normal_block_size
        return normal_block
        
    
    def cross_superblocks_query(self, super_begin, super_end):
        L = super_end - super_begin
        floor_logL = L.bit_length() - 1
        assert 1 << (floor_logL + 1) >= L

        half_L = 1 << floor_logL
        min1 = self.super_block2minidx_in_next_twopow_superblocks\
               [super_begin][floor_logL          ]
        min2 = self.super_block2minidx_in_next_twopow_superblocks\
               [super_begin+L-half_L][floor_logL ]

        mins = [min1, min2]
        if debug:
            begin = super_begin * self.super_block_size
            end = super_end * self.super_block_size
            assert minidx_of(self.array, begin, end) in mins
            
        return mins
        
    def in_one_superblock_query(self, super_block, normal_begin, normal_end):
        L = normal_end - normal_begin
        if L == 0:
            return []
        
        floor_logL = L.bit_length() - 1
        assert 1 << (floor_logL + 1) >= L

        #array_offset = self.array_offset_in_superblock(super_block, normal_begin)
        array_offset = self.array_offset_of_first_normalblock_of_superblock(super_block)
        half_L = 1 << floor_logL
        min1 = array_offset + self.normal_block2offseted_minidx_in_next_twopow_normalblocks\
               [normal_begin][floor_logL         ]
        min2 = array_offset + self.normal_block2offseted_minidx_in_next_twopow_normalblocks\
               [normal_begin+L-half_L][floor_logL]

        mins = [min1, min2]
        if debug:
            begin = normal_begin * self.normal_block_size
            end = normal_end * self.normal_block_size
            assert minidx_of(self.array, begin, end) in mins
        return mins
        
    def in_one_normalblock_query(self, normal_block, array_begin, array_end):
        if array_begin == array_end:
            return []
        code = self.normal_block2code[normal_block]
        offset = normal_block * self.normal_block_size
        offseted_idx = self.code2offseted_inblock_query_table[code]\
                       [array_begin-offset][array_end-offset]
        mins = [offset + offseted_idx]
        
        if debug:
            assert minidx_of(self.array, array_begin, array_end) in mins
        return mins
    
    def in_which_superblock(self, array_idx):
        return array_idx // self.super_block_size
    def in_which_normalblock(self, array_idx):
        return array_idx // self.normal_block_size

    def array_offset_of_first_normalblock_of_superblock(self, super_block):
        normal_begin = self.first_normalblock_in_superblock(super_block)
        return normal_begin * self.normal_block_size
         
##    def array_offset_in_superblock(self, super_block, normal_block):
##        normal_begin = self.first_normalblock_in_superblock(super_block)
##        return (normal_block - normal_begin) * self.normal_block_size
        
        
        
def range_minimum_query_args(array):
    n = len(array)
    n2 = n*n
    # n == 0: super_block_size == 0; normal_block_size = -1 --> 1
    # n == 1: super_block_size == 1; normal_block_size = 0
    # n == 2: super_block_size == 3; normal_block_size = 0
    # n == 3: super_block_size == 4; normal_block_size = 0
    # n == 4: super_block_size == 5; normal_block_size = 0 --> 1
    # n == 5: super_block_size == 5; normal_block_size = 1
    # n == 6: super_block_size == 6; normal_block_size = 1
    # n == 16: super_block_size == 9; normal_block_size = 1
    # n == 17: super_block_size == 9; normal_block_size = 2

    # floor_log(i) == k == i.bit_length()-1 for i == 2**k + (<2**k)
    logn2_more = n2.bit_length() # log(n)**(2+delta_x)
    assert 1<<logn2_more > n2
    
    super_block_size = logn2_more # log(n)**(2.x) == s'
    assert super_block_size >= 0
    if super_block_size == 0:
        super_block_size = 1
        
    num_super_blocks = (n+super_block_size-1) // super_block_size # n/s'


    floor_logn = n.bit_length()
    logn_div_2 = (floor_logn+1)//2
    while logn_div_2 > 0 and 1<<(2*logn_div_2) >= n:
        logn_div_2 -= 1
    assert (logn_div_2 == 0 and n <= 4) or 1<<(2*logn_div_2) < n
    
    normal_block_size = logn_div_2 # log(n)/(2.y) == s maybe <= 0
    if normal_block_size == 0:
        normal_block_size = 1

    num_normal_blocks = (n+normal_block_size-1)//normal_block_size # n/s
    num_normal_blocks_in_one_superblock = (
        super_block_size+normal_block_size-1)//normal_block_size
    # which normal_block in super_block ?
    # if begin of normal_block in the super_block


    

    max_power_for_superblock = floor_log_num_super_blocks = \
                               num_super_blocks.bit_length()-1
    super_block2minidx_in_next_twopow_superblocks = [
        [None]*max_power_for_superblock for _ in range(num_super_blocks)]

    super_block2minidx_in_next_twopow_superblocks = \
        calc_block_idx2minidx_in_next_twopow_blocks( # [i..i+2**j) for j in [0..max_pow]
            array, 0, len(array), super_block_size, max_power_for_superblock)



    max_power_for_normalblock = floor_log_num_normal_blocks_in_one_superblock = \
                               num_normal_blocks_in_one_superblock.bit_length()-1
    normal_block2minidx_in_next_twopow_normalblocks = \
        calc_block_idx2minidx_in_next_twopow_blocks(
            array, 0, len(array), normal_block_size, max_power_for_normalblock)

    normal_block2offseted_minidx_in_next_twopow_normalblocks = []
    for normal_block, power2minidx in enumerate(normal_block2minidx_in_next_twopow_normalblocks):
        super_block = normal_block * normal_block_size // super_block_size
        offset = first_normal_block_array_idx = \
                 (super_block_size * super_block + normal_block_size -1)\
                 //normal_block_size*normal_block_size
        power2minidx = [minidx - offset for minidx in power2minidx]
        assert all(offseted_idx >= 0 for offseted_idx in power2minidx)
        normal_block2offseted_minidx_in_next_twopow_normalblocks.append(power2minidx)
    del normal_block2minidx_in_next_twopow_normalblocks






    normal_block2code = []
    code2offseted_inblock_query_table = [None] * Catalan_number(normal_block_size)
    for normal_block in range(num_normal_blocks):
        begin = normal_block * normal_block_size
        end = begin + normal_block_size
        subarray = array[begin:end]
        code = _encode(subarray)
        normal_block2code.append(code)
        if code2offseted_inblock_query_table[code] is None:
            code2offseted_inblock_query_table[code] = calc_offseted_inblock_query_table(subarray)

    return (super_block_size, num_super_blocks, 
            normal_block_size, num_normal_blocks, 
            max_power_for_superblock, 
            num_normal_blocks_in_one_superblock,
            max_power_for_normalblock,
            super_block2minidx_in_next_twopow_superblocks, 
            normal_block2offseted_minidx_in_next_twopow_normalblocks, 
            normal_block2code, code2offseted_inblock_query_table)

def minidx_of(array, begin, end):
    subarray = array[begin:end]
    i = subarray.index(min(subarray))
    return i + begin

           
def calc_offseted_inblock_query_table(array):
    # O(n^2)
    n = len(array)
    table = [[None]*(n+1) for _ in range(n)]

    L = 1
    for i in range(n):
        table[i][i+L] = i

    for L in range(2, n+1):
        for i in range(n-L+1):
            idx1 = table[i][i+L-1]
            idx2 = table[i+1][i+L]

            val1, val2 = array[idx1], array[idx2]

            table[i][i+L] = idx2 if val2 < val1 else idx1
    assert table[0][n] is not None

    if debug:
        for i in range(n):
            for L in range(1, n-i+1):
                idx = table[i][i+L]
                ans = minidx_of(array, i, i+L)
                assert idx == ans
    return table

def calc_block_idx2minidx_in_next_twopow_blocks(
    array, begin, end, block_size, max_power):
    # [i..i+2**j) for j in [0..max_pow]

    num_blocks = (end - begin + block_size-1) // block_size
    block2power2minidx = [[None]*(1+max_power) for _ in range(num_blocks)]

    power = 0
    for block, power2minidx in enumerate(block2power2minidx):
        offset = begin + block * block_size
        subarray = array[offset: offset+block_size]
        power2minidx[power] = subarray.index(min(subarray)) + offset

    for power in range(1, max_power+1):
        for block, power2minidx in enumerate(block2power2minidx):
            # bug: << precedence lower than +
            next = min(block+(1<<(power-1)), num_blocks-1)
            #print('block, power, next', block, power, next)

            idx1, idx2 = power2minidx[power-1], block2power2minidx[next][power-1]
            val1, val2 = array[idx1], array[idx2]

            power2minidx[power] = idx2 if val2 < val1 else idx1

    if debug == 1:
        for block, power2minidx in enumerate(block2power2minidx):
            offset = begin + block * block_size
            
            for power, minidx in enumerate(power2minidx):
                to = offset + block_size * (1<<power)
                subarray = array[offset: to]
                if not minidx == offset + subarray.index(min(subarray)):
                    print('array', array)
                    print('minidx', minidx)
                    print(offset, to, subarray, subarray.index(min(subarray)))
                    print('power2minidx', power2minidx)
                    print('power', power)
                    print('block', block)
                    print('block_size', block_size)
                    print('block2power2minidx', block2power2minidx)
                assert minidx == offset + subarray.index(min(subarray))
        
    return block2power2minidx
            
        
    
def test_calc_block_idx2minidx_in_next_twopow_blocks():
    from random import randint
    for _ in range(100):
        array = [randint(1000+0, 1000+10) for _ in range(10)]
        block2power2minidx = calc_block_idx2minidx_in_next_twopow_blocks(array, 0, len(array), 2, 2)
        
        for i in range(10):
            for j in range(i+1, 11):
                idx = rmq(i,j)
                ans = array.index(min(array[i:j]))
                if not ans == idx:
                    print(array)
                    print(ans, idx)
                    print(i, j)
                    print(i, array[i:j])
                assert ans == idx


    
    
def test_range_minimum_query(n=10, times=100):
    from random import randint
    for _ in range(times):
        array = [randint(1000+0, 1000+n) for _ in range(n)]
        rmq = range_minimum_query(array)
        
        for i in range(n):
            for j in range(i+1, n+1):
                idx = rmq(i,j)
                ans = minidx_of(array, i, j)
                if not ans == idx:
                    print('array', array)
                    print('ans, idx', ans, idx)
                    print('i, j', i, j)
                    print('array[i:j]', array[i:j])
                assert ans == idx

def test_range_minimum_query2():
    for n in range(10):
        test_range_minimum_query(n)
        
test_range_minimum_query2()

        
    
    
    
    







    
