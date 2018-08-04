
'''
NOTE:
    CT(n)
        ~ uint O(4^n)
        ~ space bit size O(n)
        ~ time O(n^2 * log(n))
            very slow!!!

Catalan Number
    CT(n) = C(2n, n)/(n+1) = O(4**n/(pi*n**3)**.5 (1+O(1/n)))
        for n >= 0
        CT(0) = 1

    CT(n) = sum CT(i)*CT(n-1-i) {i<-[0..n-1]}
        for n >= 1
        CT(0) = 1

    sum CT(i)z**i = f(z) = 1 + z*f*f = [1-sqrt(1-4z)]/(2z)

    CT(n)/CT(n-1) for n >= 1
        = 2*(2n-1)/(n+1)
        proof:
        = C(2n,n)/(n+1) / C(2n-2,n-1) * n
        = 2n!/n!/n!/(n+1) / (2n-2)! * (n-1)! * (n-1)! * n
        = 2n*(2n-1)/n!/n!/(n+1) * (n-1)! * n!
        = 2*(2n-1)/n!/n!/(n+1) * n! * n!
        = 2*(2n-1)/(n+1)



balanced Dyck word of length 2n:
    # length of Dyck word = len(Dyck word)
    # but size of Dyck word == sum(Dyck word)
    # Dyck word is a prefix of some balanced Dyck word
    # balanced Dyck word of length 2n is of size n
    # 1 is open, 0 is close
    rex = [01]*
    and sum(BDW[:i]) >= ceil(i/2) for any i
    and sum(BDW) == len(BDW)/2 == n

    1 -> '('; 0 -> ')': oriented-rooted-tree[n+1]
    1 -> dxy = (1,1); 0 -> dxy = (1,-1)
        ==> (x, y) in [0..2n]*[0..n]; begin (0,0); end (2n,0)
    y is height, note abs(dy) == 1
    1 -> 1; 0 -> -1: dy list; +/-1 RMQ (range minimum quary)

    num_BDW(2n) == |{balanced Dyck word of length 2n}| == CT(n)
    |BDW|(0) = 1
    |BDW|(2n) = sum |BDW|(2i-2) * |BDW|(2n-2i) for i in [1..n]
                where 2i is the length of first complete '(...)'

    CT(n) =?= sum CT(i-1)*CT(n-i) for i in [1..n]
    =?= sum CT(i)*CT(n-1-i) for i in [0..n-1]

    sum CT(i)z**i =?= f(z) = 1 + f(z)*f(z)*z
    zf**2 - f + 1 = 0 ==>> f=(1+/-sqrt(1-4z))/(2z)
    sqrt(1-4z) = sum C(1/2, i)*(-4z)**i = sum z**i * II(-4(1/2-k) for k in [0..i-1])/i!
        = sum z**i * II(2(k+1)(2k-1) for k in [0..i-1])/i!**2
        = sum z**i * -(2i)!/(2i-1)/i!**2 for i >= 0
    f- = (1-sqrt)/(2z) = sum z**i * (2i)!/(2i-1)/i!**2 / (2z) for i > 0
        = sum z**i * (2i+2)!/(2i+1)/(i+1)!**2 / 2 for i >= 0
        = sum z**i * (2i)!/(i+1)/i!**2 for i >= 0
        = sum CT(i)z**i
    YES!


balanced_Dyck_word[2n] <==> oriented-rooted-tree[n+1]:
    # bug: '' <-> v2children = [[]]
    ''      <-> ORT = []        <-> errFORBT = (();())
    '()'    <-> ORT = [[]]      <-> errFORBT = ((();());())
    '()()'  <-> ORT = [[], []]  <-> errFORBT = ((();(();()));())
    '(())'  <-> ORT = [[[]]]    <-> errFORBT = (((();());());())
                                # why error?
                                #   since root.right is always "()"
                                #   we should remove the root!!
    BDW2ORT(bdw) = [BDW2ORT(sub_bdw) for sub_bdw in bdw.split_by_top_group('(', ')')]
                = eval(''.join(['[', bdw.replace({'(':'[', ')':'],'}), ']']))
        where bdw = rex'[()]*'

    num_ORT(n) == |{oriented-rooted-tree of size n}| == CT(n-1); n > 0
    |ORT|(n) = sum (product |..|(i) for i in p) where sum(p) == n-1 and all(i>0 for i in p)
    CT(n) =?= sum (II CT(i) for i in p)

oriented-rooted-tree[n+1] <==> full-oriented-rooted-binary-tree[2n+1]:
num_nonleaf_nodes2num_FORBT(n) == CT(n)
    # "oriented/ordered" means left/right children are distinguished
    # "full" means FORBT.nonleaf_node should have 2 children
    #       i.e. can not have only 1 child
    for n >= 0

    ORT_nonroot_node become FORBT_nonleaf_node
        except ORT_root, which was removed!!
        ORT_root.first_child become FORBT_root
    parent2children
        = (ORT_last_leaf_child->new_FORBT_leaf, ORT_last_leaf_child->new_FORBT_leaf)
        | (ORT_last_child->first_child, ORT_last_child->new_FORBT_leaf)
        | (ORT_leaf->new_FORBT_leaf, ORT_leaf->next_sibling)
        | (ORT_node->first_child, ORT_node->next_sibling)
        # ORT_root is deleted, neither ORT_last_child nor ORT_leaf

        ORT_nonroot_node become FORBT.nonleaf_node
            num_ORT_nodes = n+1
            ==>> num_ORT_nonroot_nodes = n
            ==>> num_FORBT_nonleaf_nodes = n
            ==>> num_FORBT_leaf_nodes = n+1
            ==>> num_FORBT_nodes = 2n+1


    num_FORBT = ?
      1)
        num_FORBT(2n) = 0
        num_FORBT(1) = 1
        num_FORBT(2n+3) = CT(n) for n >= 0
            since num_FORBT(2n+1) = num_ORT(n) = CT(n-1) for n >= 1
      2)
        num_FORBT(0) = 0
        num_FORBT(1) = 1
        num_FORBT(n+2) = sum` num_FORBT(i)*num_FORBT(n+1-i) `{i<-[0..n+1]} for n>=0
    ==>> num_nonleaf_nodes2num_FORBT(n) = num_FORBT(2n+1) = num_ORT(n+1) = CT(n)

    other way:
        num_nonleaf_nodes2num_FORBT(n) = f n where
            f 0 = 1 # single root leaf
            f n | n>0 = sum` f(i)*f(n-1-i) `{i<-[0..n-1]}
        ==>> num_nonleaf_nodes2num_FORBT(n) = CT(n) # by definition (2)
    explain:
        FORBT_nonleaf_node is binary-operator
        FORBT_leaf_node is argument

    # full-unoriented-rooted-binary-tree
    num_FURBT = ?
        num_FURBT(0) = 0
        num_FURBT(1) = 1
        num_FURBT(n+2) = sum` num_FURBT(i)*num_FURBT(n+1-i) `{i<-[0..(n+1)//2]} for n>=0

full-oriented-rooted-binary-tree[2n+1] <==> partial-oriented-rooted-binary-tree[n]
num_PORBT(n) == CT(n)
    # 'partial' means PORBT_nonleaf_node have 1 or 2 children
    # allow empty tree!!!!!!
    for n >= 0

    * remove all leaves from FORBT ==>> PORBT
    * PORBT add leaves to nodes that have 0 or 1 child ==>> FORBT
    num_PORBT(n) = num_nonleaf_nodes2num_FORBT(n) = num_FORBT(2n+1) = CT(n)


Non-Decreasing Parking Function:
    f : [1..n] -> [1..n]
    f(i-1) <= f(i) <= i
    |{nondecreasing_parking_function of size n}| == CT(n)

    from_balanced_Dyck_word of length 2n:
        f(i) = 1 + BDW[:index of ith '1'].count(0)

    let balanced_Dyck_word : 1->(1,1); 0->(1,-1)
    let balanced_Dyck_word : 1->(1,0); 0->(0,1)




example:
    >>> Catalan_number(0)
    1
    >>> Catalan_number(1)
    1
    >>> Catalan_numbers(5)
    [1, 1, 2, 5, 14]
    >>> Catalan_number(19)
    1767263190
    >>> Catalan_numbers(len(some_Catalan_numbers)) == some_Catalan_numbers
    True

    >>> it1 = iter_Catalan_numbers_by_mul_ratio
    >>> it2 = iter_Catalan_numbers_by_sum_product
    >>> Catalan_numbers(14, it1) == Catalan_numbers(14, it2)
    True

'''

__all__ = '''
    Catalan_number
    iter_Catalan_numbers_by_mul_ratio


    iter_Catalan_numbers_by_sum_product
    Catalan_numbers
    '''.split()

from itertools import count, islice
from operator import mul

# 5*4
some_Catalan_numbers = \
    [ 1, 1, 2, 5, 14
    , 42, 132, 429, 1430, 4862
    , 16796, 58786, 208012, 742900, 2674440
    , 9694845, 35357670, 129644790, 477638700, 1767263190]

def Catalan_number(n):
    '''CT(n) = C(2n,n)/(n+1)
    time O(n^2 * log(n))
'''
    if n < 0: raise ValueError
    for i, CT in enumerate(iter_Catalan_numbers_by_mul_ratio()):
        if i == n: return CT

    #return Catalan_numbers(n+1)[-1]

def iter_Catalan_numbers_by_sum_product():
    '''iter_CTs = (CT(n) for n in [0..])
    where
        CT(n) =[concept]= C(2n,n)/(n+1)

        CT(0) =[compute]= 1
        CT(n) =[compute]= sum` CT(i)*CT(n-1-i)`{i<-[0..n-1]}

    time O(log(CT(n))^2 * n) per iteration
        = O(n^3) per iteration since CT(n) = O(4^n)
'''
    CT = 1
    CTs = []

    while True:
        CTs.append(CT)
        yield CT

        #CT = sum(CT_i * CT_n_1_i for CT_i, CT_n_1_i in zip(CTs, reversed(CTs)))
        CT = sum(map(mul, CTs, reversed(CTs)))
    pass


def iter_Catalan_numbers_by_mul_ratio():
    '''iter_CTs = (CT(n) for n in [0..])
    where
        CT(n) =[concept]= C(2n,n)/(n+1)

        CT(0) =[compute]= 1
        CT(n) =[compute]= CT(n-1) * 2*(2n-1)/(n+1) for n >= 1

    time O(log(CT(n))*log(n)) per iteration
        = O(n*log(n)) per iteration
            since CT(n) = uint O(4^n) = space bit size O(n)
'''
    CT = 1
    yield CT
    for n in count(1):
        CT = CT*(4*n-2)//(n+1)
        yield CT
    pass

def Catalan_numbers(n, iter_Catalan_numbers=None):
    '''CTs(n) = [CT(i) for i in range(n)]
    where
        CT(n) = C(2n, n)/(n+1)
    time O(n^2 * log(n))

input:
    n :: uint
        the length of output
        len(CTs(n)) == n
    iter_Catalan_numbers :: None | (() -> Iter<CT>)
        = None
        | iter_Catalan_numbers_by_mul_ratio     # default
        | iter_Catalan_numbers_by_sum_product
'''
    if iter_Catalan_numbers is None:
        iter_Catalan_numbers = iter_Catalan_numbers_by_mul_ratio
    return list(islice(iter_Catalan_numbers(), n))



if __name__ == "__main__":
    import doctest
    doctest.testmod()

