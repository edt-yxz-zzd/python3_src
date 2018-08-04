

'''
find a[i]
[NN k,b][NN a[i] for i=1..k][a[i]>=a[i+1] for i=1..k-1][a[1]<a[0]]
    a[0]**k == sum a[i]**k {i=1..k}
a[1]**k >= a[0]**k/k
a[1] >= ceil( ((a[0]**k+k-1)//k)**(1/k) )


'''

from math import *
from itertools import *
from pprint import pprint as print
from nn_ns.math_nn.numbers.pow_i_k import Pow_i_const_k

def ceil_nth_root(x, n):
    assert x > 0
    assert n > 0    
    root = x**(1/n)
    m = ceil(root)
    assert m**n >= x > (m-1)**n
    return m


def find_ai(k, max_a0):
    assert k>=2
    
    max_a1 = ceil_nth_root(max_a0, k)
    pow_i_k = tuple(i**k for i in range(max_a0+1))
    pows = {pow_i_k[i]:i for i in range(max_a0+1)}

    ans = []
    for b in combinations(range(max_a0+k-1), k):
        b = [x-i for i,x in enumerate(b)]
        if b[-2] == 0:
            continue
        s = sum(pow_i_k[ai] for ai in b)
        if s in pows:
            a = [pows[s]] + list(reversed(b))
            a = tuple(a)
            assert a[0]**k == sum(a[i+1]**k for i in range(k))
            ans.append(a)
    ans.sort()
    return ans


class Find_ai:
    def __init__(self, k):
        assert k >= 2
        self.k = k
        self.ls = Pow_i_const_k(k)
        self.i2pow = []
        self.pow2i = {}

    def extend_to(self, a0):
        old_a0 = len(self.i2pow) - 1
        if a0 <= old_a0:
            return

        ls = self.ls.get_least_len(a0+1)
        self.i2pow.extend(ls[old_a0+1:a0+1])
        self.pow2i.update((ls[i], i) for i in range(old_a0+1, a0+1))
        assert len(self.i2pow) == len(self.pow2i)
        
        
    def find_ai_for_a0(self, a0):
        self.extend_to(a0)
        k = self.k
        for tail in self.find_ai_for_sum(a0-1, k, self.i2pow[a0]):
            ls = [a0]
            ls.extend(reversed(tail))
            assert ls[0]**k == sum(ls[i+1]**k for i in range(k))
            assert a0 == ls[0] > ls[1]
            assert all(ls[i] >= ls[i+1] for i in range(k))
            yield tuple(ls)
        return

        
    
    def find_ai_for_sum(self, max_ai, L, sum_):
        assert L > 0
        if L == 1:
            a = self.pow2i.get(sum_, max_ai + 1)
            if a <= max_ai:
                yield [a]
            return

        k = self.k
        min_next = ceil_nth_root((sum_+L-1)//L, k)
        for a in range(min_next, max_ai+1):
            tail_sum = sum_ - self.i2pow[a]
            for tail in self.find_ai_for_sum(a, L-1, tail_sum):
                tail.append(a)
                assert len(tail) == L
                assert sum(self.i2pow[x] for x in tail) == sum_
                assert a == max(tail)
                yield tail
        return

def find_ai_ver2(k, max_a0):
    f = Find_ai(k).find_ai_for_a0
    f(max_a0)
    ans = []
    for a0 in range(max_a0, 0, -1):
        ans.extend(f(a0))
    ans.sort()
    return ans
##    
##ans = list(Find_ai(3).find_ai_for_a0(100))
##print(ans)




import timeit
'''
t1 = timeit.timeit(lambda:find_ai(3, 100), number=1)
t2 = timeit.timeit(lambda:find_ai_ver2(3, 100), number=1)
print(t1)
print(t2)
0.6453688829635161
0.062157442780268246
'''



ans1 = find_ai(3, 100)
ans2 = find_ai_ver2(3, 100)
if ans1 != ans2:
    print(ans1)
    print(ans2)
assert ans1 == ans2
##print(ans2)
##print(len(ans2))
    
'''
ans = find_ai(3, 100)
print(ans)
print(len(ans))

[(6, 5, 4, 3),
 (9, 8, 6, 1),
 (12, 10, 8, 6),
 (18, 15, 12, 9),
 (18, 16, 12, 2),
 (19, 18, 10, 3),
 (20, 17, 14, 7),
 (24, 20, 16, 12),
 (25, 22, 17, 4),
 (27, 24, 18, 3),
 (28, 21, 19, 18),
 (29, 27, 15, 11),
 (30, 25, 20, 15),
 (36, 30, 24, 18),
 (36, 32, 24, 4),
 (38, 36, 20, 6),
 (40, 34, 28, 14),
 (41, 33, 32, 6),
 (41, 40, 17, 2),
 (42, 35, 28, 21),
 (44, 41, 23, 16),
 (45, 40, 30, 5),
 (46, 37, 30, 27),
 (46, 37, 36, 3),
 (48, 40, 32, 24),
 (50, 44, 34, 8),
 (53, 44, 34, 29),
 (54, 45, 36, 27),
 (54, 48, 36, 6),
 (54, 53, 19, 12),
 (56, 42, 38, 36),
 (57, 54, 30, 9),
 (58, 49, 42, 15),
 (58, 54, 30, 22),
 (60, 50, 40, 30),
 (60, 51, 42, 21),
 (63, 56, 42, 7),
 (66, 55, 44, 33),
 (67, 54, 51, 22),
 (69, 61, 38, 36),
 (70, 57, 54, 7),
 (71, 70, 23, 14),
 (72, 60, 48, 36),
 (72, 64, 48, 8),
 (72, 65, 39, 34),
 (75, 66, 43, 38),
 (75, 66, 51, 12),
 (76, 72, 33, 31),
 (76, 72, 40, 12),
 (78, 65, 52, 39),
 (80, 68, 56, 28),
 (81, 72, 54, 9),
 (81, 74, 48, 25),
 (82, 66, 64, 12),
 (82, 69, 60, 19),
 (82, 80, 34, 4),
 (84, 63, 57, 54),
 (84, 70, 56, 42),
 (84, 75, 53, 28),
 (85, 64, 61, 50),
 (87, 78, 55, 26),
 (87, 79, 48, 38),
 (87, 79, 54, 20),
 (87, 81, 45, 33),
 (88, 82, 46, 32),
 (88, 84, 43, 21),
 (88, 86, 31, 25),
 (89, 86, 40, 17),
 (90, 69, 59, 58),
 (90, 75, 60, 45),
 (90, 80, 60, 10),
 (90, 87, 38, 25),
 (92, 74, 60, 54),
 (92, 74, 72, 6),
 (93, 85, 54, 32),
 (95, 90, 50, 15),
 (96, 80, 64, 48),
 (96, 90, 53, 19),
 (97, 79, 69, 45),
 (99, 88, 66, 11),
 (100, 85, 70, 35),
 (100, 88, 68, 16)]
82
'''




















