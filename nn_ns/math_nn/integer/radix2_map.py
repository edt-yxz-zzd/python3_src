


from sand import is_main


r'''
S = binary string ::= [01]*
token requirement:
    exists a token SEP s.t.
        for any token list A not containing SEP: SEP not in ''.join(A)
    no token is a prefix of another. // prefix-code?
    // there are only finite unrecognizable suffixes
    exists suffixes SUFS s.t.
        "" in SUFS
        for any S exists one and only one suffix in SUFS s.t.
            S - suffix is tokenizable
            
therefore, "" is not a token
tokens is a leaf of a binary tree:
    if finite, then:
        let L=len(tokens)
        there are L-1 internal node
        therefore L-1 == len(SUFS)
        exists bijection between SUFS and tokens-{SEP}
        let ts = tokenize(S)
        len(ts) > 0
        ts[-1] != SEP
        
        tss = ts.split(SEP)
        len(tss) > 0
        len(tss[-1]) > 0
        suitable for (>=0..., >0)
        continued_fraction = [i; >=1..., >1]
        continued_fraction in (0,1) = [0; >=1..., >1]
        
    elif infinite, then:
        exists bijection between SUFS and tokens
        

if tokens = {1, 01, 001, 0001, 0000},
    SUFS = {"", 0, 00, 000}
    let S$ = S+"1"
    let 0000 be the seperater SEP
    let Ts = tokenize(S$)
    then len(Ts) > 0, Ts[-1] != SEP
    NOTE: Ts[-1] can be any token except SEP

if tokens = {0, 10, 11}, SEP = 11,
    let $ = 0
    
    
'''


def radix_tuple2uint(radix_tuple, radix):
    assert radix > 1
    assert all(0 <= d < radix for d in radix_tuple)

    n = 0
    for d in radix_tuple:
        n *= radix
        n += d

    return n

def shift_radix_tuple2uint(radix_tuple, radix):
    L = len(radix_tuple)
    offset = (radix ** L - 1) // (radix - 1)
    n = radix_tuple2uint(radix_tuple, radix)
    return offset + n

    
    

def parse_1s0(string, sep_len=2, zero='0', one='1'):
    '''parse binary string into [(int,)]

sep     - newline    - ','
zero    - space      - digit token boundary
1       - \\w        -
len(1s) - word       - digit value, in range(radix)
sep_len -            - radix

example:
    >>> parse_1s0('')
    [(0,)]
    >>> parse_1s0('1')
    [(1,)]
    >>> parse_1s0('0')
    [(0, 0)]
    >>> parse_1s0('11')
    [(0,), (0,)]
    >>> parse_1s0('00')
    [(0, 0, 0)]
    >>> parse_1s0('01')
    [(0, 1)]
    >>> parse_1s0('10')
    [(1, 0)]
    >>> parse_1s0('111')
    [(0,), (1,)]


'''

    assert sep_len >= 2
    radix = sep_len
    sep = one * sep_len # like newline
    lines = string.split(sep)


    ls = []
    for line in lines:
        words = line.split(zero)
        assert words
        assert all(c == '1' for word in words for c in word)

        lens = tuple(len(word) for word in words)
        assert lens
        assert all(L < radix for L in lens)
        
        ls.append(lens)

    assert ls
    return ls
    
    



if is_main(__name__):
    import doctest
    doctest.testmod()


xxxxxxxxxxxxxxx = r'''
error


using a non-self-overlap seperator SEP of length L, ie: "0001"
let S be a string that does not contain SEP
we can cut S+$ into tokens
$ is a token and the suffix of some tokens
requirement: for any token list A: SEP not in ''.join(A)

while SEP = 0001:
    there are L token prefixes {1, 01, 001, 0000}
    if all tokens are {1, 01, 001, 0000}
        then there are 4 other tokens {$, 0$, 00$, 000$} at the end
        let ($, 0$, 00$, 000$) == (1, 01, 001, 0000)
        note that $ may be 0 while in 000$
        NOTE: '0000' + '1' contains 0001, bad design
        
    SHOULD NOT have tokens in 0+ style
    so, all tokens are {1, 01, 001,     00001, 0...01, ...}
    0001 is not a good SEP

while SEP = 0011:
    prefixes = {1, 01, 000, 0010}
    if tokens = {1, 01, 000, 0010}

'''

xxxxxxxxxxxxxxxxxxxxx = r'''
to positive rational number / positive fractions
Stern Brocot tree / Farey series of order N
concrete_mathematics(2nd) :: 4 Number Theory 4.5 RELATIVE PRIMALITY page 116


---------------------------------------------------------------
Stern Brocot tree
start = (0/1, 1/0)
let mediant(a/b, m/n) = (a+m)/(b+n)
insert mediant between two adjacent fractions
0/1                                           1/0
                      1/1
          1/2                    2/1
     1/3        2/3         3/2         3/1
  1/4   2/5  3/5  3/4   4/3   5/3   5/2   4/1 

if (a/b, m/n), then mb-an == 1. ie: (1/2, 1/1) or (1/2, 2/3)
---------------------------------------------------------------


let L denote left, R denote right, S denote a string of {L,R}
let f(S) denote the fraction represented by S in Stern Brocot tree
f("") = 1/1, 1/f(S) = f(flip(S)), I = flip*flip

ie: f(L) = 1/2, f(R) = 2/1

f(RS) = 1 + f(S)
f(LS) = 1/f(flip(LS)) = 1/f(R+flip(S)) = 1/(1+f(flip(S))) = 1/(1+1/f(S))
= f(S)/(1+f(S))


let f(S) = a/b
f(R*n + S) = n + f(S) = (n*b+a) / b
f(L*n + S) = f(S)/(1 + n*f(S)) = a / (n*a+b)

continued fraction!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


---------------------------------------------------------------
The Farey series of order N, denoted by F_N, is the set of all reduced
fractions between 0 and 1 whose denominators are N or less, arranged in
increasing order. 
Farey_series(N=3) = 0/1   1/3  1/2   2/3   1/1   3/2   2/1  3/1  1/0

'''
























