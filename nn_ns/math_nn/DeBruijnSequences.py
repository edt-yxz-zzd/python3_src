

from collections import OrderedDict
#from sympy import isprime
#.ntheory.primetest.isprime

class DeBruijDiGraph:
    def __init__(self, radix, length):
        # digraph of RADIX**LENGTH vertices
        # outgoing_degree(v) == radix
        # may contain one loop
        assert radix > 1
        assert length > 0
        self.radix = radix
        self.length = length
        self.mod = radix**(length-1)
        self.n = radix**length
    def nv(self):
        return self.n
    def veritices(self):
        return range(self.n)
    def neighbors(self, v):
        v %= self.mod
        v *= self.radix
        return range(v, v+self.radix)
    
        
class DeBruijnSequences:
    def __init__(self, radix, length):
        # digraph of RADIX**LENGTH vertices
        # all sequences begin at 0
        self.radix = radix
        self.length = length
        self.g = DeBruijDiGraph(radix, length)
    def __iter__(self):
        v2iter = OrderedDict()
        root = 0
        v2iter[root] = iter(self.g.neighbors(root))
        while v2iter:
            #print(v2iter)
            v, it = v2iter.popitem()
            for u in it:
                #print(v, u)
                #assert u in v2iter
                
                if u == root and len(v2iter)+1 == self.g.nv():
                    yield self.__make_seq(v2iter, v)
                if u not in v2iter and u != v:
                    break
            else:
                continue

            #raise
            v2iter[v] = it
            v2iter[u] = iter(self.g.neighbors(u))

        return
    
    def __make_seq(self, v2iter, last):
        ls = list(v % self.radix for v in v2iter)
        ls.append(last % self.radix)
        return ls[1-self.length:] + ls[:1-self.length]

    @staticmethod
    def circle_permutation(seq):
        return seq[1:] + seq[:1]
    @staticmethod
    def circle_permutations(seq):
        for _ in range(len(seq)):
            yield seq
            seq = DeBruijnSequences.circle_permutation(seq)
    @staticmethod
    def seq2num(radix, seq):
        i = 0
        for x in seq:
            i *= radix
            i += x
        return i
    





def test_DeBruijnSequences():
    for radix in range(2, 4):
        for length in range(1, 3):
            print(radix, length)
            for seq in DeBruijnSequences(radix, length):
                print(seq)
    return


def test_DeBruijnSequences2():
    for radix in range(2, 3):
        for length in range(1, 5):
            print(radix, length)
            for seq in DeBruijnSequences(radix, length):
                print(seq)
    return




#test_DeBruijnSequences2()
def find_prime_in_DeBruijnSequences():
    from sympy import isprime
    
    radix2primes = {}
    for radix in range(2, 4):
        radix2primes[radix] = primes = set()
        
        for length in range(1, 5+2*(2-radix)):
            print('#', radix, length)
            s = DeBruijnSequences(radix, length)
            nv = radix**length
            L = radix**nv
            len_base10 = len(str(L))
            tpl = '{{!s: >{width}}}  {{!s}}'.format(width=len_base10)
            #print(tpl)
            
            for seq0 in s:
                #print(seq)
                for seq in DeBruijnSequences.circle_permutations(seq0):
                    n = s.seq2num(radix, seq)
                    if isprime(n):
                        primes.add(n)
                        sseq = ''.join(map(str, seq))
                        print(tpl.format(n, sseq))

    keys = sorted(radix2primes)
    key0 = keys[0]
    set0 = radix2primes[key0]
    for keyi in keys[1:]:
        set0 &= radix2primes[keyi]
        print(set0) # set() none
    return


# find_prime_in_DeBruijnSequences()
'''
# 2 1
2  10
# 2 2
 3  0011
# 2 3
 23  00010111
113  01110001
197  11000101
139  10001011
 29  00011101
163  10100011
 71  01000111
# 2 4
44809  1010111100001001
24083  0101111000010011
57653  1110000100110101
 2539  0000100111101011
60169  1110101100001001
44071  1010110000100111
 2671  0000101001101111
19937  0100110111100001
30803  0111100001010011
 2683  0000101001111011
15749  0011110110000101
60457  1110110000101001
 3449  0000110101111001
51307  1100100001101011
 8623  0010000110101111
 3557  0000110111100101
 3929  0000111101011001
54851  1101011001000011
55619  1101100101000011
# 3 1
 5  012
19  201
 7  021
11  102
# 3 2
 5563  021122001
17599  220010211
 6211  022112001
13441  200102211
13469  200110212
 1049  001102212
 8641  102212001
 6089  022100112
 6947  100112022
12583  122021001
 5147  021001122
 6959  100112202
15809  210200112
 4507  020011221
 1291  001202211
 6991  100120221
 8521  102200121
 5881  022001211
 1399  001220211
 7027  100122021
18523  221102001
 3593  011221002
 4241  012211002
16097  211002012
 3571  011220021
12457  122002101
 9209  110122002
 4153  012200211
13721  200211012
17761  220100211
 2393  010021122
12503  122011002
17827  220110021
 1987  002201121
 3491  011210022
 1993  002201211
14447  201211002
16111  211002201
 8969  110022012
 2039  002210112
 7703  101120022
11161  120022101
 9161  110120022
13807  200221101
16553  211201002
 2417  010022112
 2083  002212011
'''





















        
