
'''
ballot number


if 0 <= p <= q:
    if q == 0:
        ballot(0,0) = 1
    else:
        ballot(p,q) = ballot(p,q-1) + ballot(p-1,q) => ballot(>=0, 0) = 1
else:
    ballot(p,q) = 0


xballot(q,p) = ballot(p,q)
xballot(q,q) = xballot(q,q-1) = sum xballot(q-1,p) for all p , if q > 0
xballot(q,q) = Catalan_number[q]



-------------------------------------------------
f(q) = sum xballot(q,p)z**p
f(0) = 1
f(q) = [f(q) - xballot(q,q)*z**q]z + f(q-1) for q > 0
= (-xballot(q,q)*z**(q+1) + f(q-1))/(1-z)
= sum(-xballot(q-i,q-i)*z**(q-i+1)/(1-z)**(i+1) for i in [0..q-1]) + f(0)/(1-z)**q
1/(1-z)**k = sum((-z)**i * II([-k-i+1..-k])/i!) = sum(z**i * C(k+i-1,i))

xballot(q,p)*z**p == sum(-xballot(q-i,q-i)*z**(q-i+1) * z**(p-q+i-1)C(i+1+(p-q+i-1)-1, p-q+i-1) for i in [q-p+1..q-1]) + f(0)*z**p * C(q+p-1,p)
xballot(q,p) = sum(-xballot(q-i,q-i)*C(p-q+2i-1, i) for i in [q-p+1..q-1]) + C(q+p-1,p)




xballot(q,q)*z**q == sum(-xballot(q-i,q-i)*z**(q-i+1) * z**(i-1)C(i+1+(i-1)-1, i-1) for i in [0..q-1]) + f(0)*z**q * C(q+q-1,q)
xballot(q,q) = sum(-xballot(q-i,q-i)*C(2i-1, i-1) for i in [0..q-1]) + C(2q-1,q)
xballot(q,q) = C(2q-1,q) - sum(xballot(q-i,q-i)*C(2i-1, i-1) for i in [1..q-1])
xl(q) = xballot(q,q)
xl(q) + sum(xl(q-i)*C(2i-1, i-1) for i in [0..q]) = 2C(2q-1,q)
xl(q) =?= (2q)!/(q+1)!/q! = CT(q) # likely; simpy say YES.




2C(2q-1,q) - CT(q) = (2q-1)!/(q-1)!/q!(2 - 2/(q+1)) = (2q)!/(q-1)!/(q+1)! = C(2q, q-1)
xballot(q,p) = sum(-CT(q-i)*C(p-q+2i-1, i) for i in [q-p+1..q-1]) + C(q+p-1,p)
C(q+p-1,p) - xballot(q,p) = sum((2q-2i)!/(q-i)!**2/(q-i+1) * (p-q+2i-1)!/i!/(p-q+i-1)! for i in [q-p+1..q-1])





'''

'''
encode tree struct of Canonical Cartesian Tree of array of length n
array[n] <-> Canonical Cartesian Tree [n]
--> binary-tree[n] <-> path[n,n] <-> [0..CT(n)-1]



# what is a path
{path(q,p)} = {all path from (q, p), terminate at (0, 0),
                each node in talbe xballot_numberss(Q),
                that is each node (q',p') s.t. 0<=p'<=q',
                each step is a hstep or vstep}
(dq, dp) = step = hstep(0, -1) or vstep(-1, 0)

# path property, number of paths from (q,p)
|{path(0,0)}| = 1 == xballot(0,0)
|{path(q,p)}| = 0 == xballot(q,p) if not 0 <= p <= p
|{path(q,p)}| = |{path(q,p-1)}| + |{path(q-1,p)}| == xballot(q,p), otherwise
==>> |{path(q,p)}| == xballot(q,p)
==>> |{path(q,q)}| == xballot(q,q) == CT(q)


# encode path
encode path in {path(q,q)} -> [0..CT(q)-1]
since there xballot(q,p-1)'s paths in {path(q,p-1)},
we can give offset offset_qp +  0            to {path(q,p-1)} and
            offset offset_qp +xballot(q,p-1) to {path(q-1,p)}
    while encode {path(q,p)} with offset offset_qp
that is :
    for hstep '<' [(q,p)->(q,p-1)], we assign value 0              (or xballot(q-1,p))
    for vstep '^' [(q,p)->(q-1,p)], we assign value xballot(q,p-1) (or 0)
    encode(path) = sum(value(step in path))

    we may want encode(array) == encode(array+[?x]*?L)
    so, exists a path s.t. offset of (t,t) from (q,q) == 0
    first reverse path, (0,0)->(q,q)
    ==> value(-vstep) == 0; value(-hstep) = xballot(q-1,p);
    -vstep comes first, so {-v:+1, -h:-1} while map to +/-1 seq
    extended steps == [-vstep, -hstep]*?L ==>> ?x == -inf or min(array)
    ==>> [?x] non-increase; min(array) <= ?x;
    
    
    


# array -> right-hand-height[i] in Canonical Cartesian Tree
right-hand-height[i] = max len((some_p--to_right_child-->)* -->i)
binary tree struct of size 2n+1 -> right-hand-height of len n 
infix travel a binary tree of size 2n+1:
    # ignore (n+1)'s leaves
    # num_edges = 2n, num_none_leaf_nodes = n
    # num of to_right_child-edges = n
    when encounter to_left_child-edge: pass
    -----exit      to_left_child-edge: pass
    when encounter to_right_child-edge: put parent-node into stack
        now right-hand-height[parent-node] = len(stack) - 1
    -----exit      to_right_child-edge: pop parent-node from stack
array is in the infix order of its Canonical Cartesian Tree
right-hand-height -> binary tree struct
    assert right-hand-height[0] = 0
    assert 0 <= right-hand-height[i] <= right-hand-height[i-1]+1
    stack = [0]
    for i in [1..]:
        assert 0 <= right-hand-height[i] <= right-hand-height[i-1]+1 == len(stack) > 0
        if right-hand-height[i] == L:
            remove right-tree-edge between (stack[L-1], stack[L]) if 0 < L < len(stack)
            node i is the right child of node in stack[L-1] if L > 0
            node i is the parent of node in stack[L] if L < len(stack)
            stack[L:] = [i]

now, we have proved "right-hand-height <==> binary tree struct"

# right-hand-height of len n <-> sequence of +/-1's of len 2n with "x >= 0 for x in accumulate(seq)"
note 0 <= right-hand-height[i] <= right-hand-height[i-1]+1 for i > 0
seq[0] = +1
if right-hand-height[i] == right-hand-height[i-1]+1:
    # the same : seq += [-1]*(k+1)
    seq.append(+1)
if right-hand-height[i] == right-hand-height[i-1]-k: (k>=0)
    seq += [-1]*(k+1)
    seq.append(+1)
seq += [-1]*(right-hand-height[-1]+1)
total n's +1 in seq
num of -1's = sum(1+right-hand-height[i-1]-right-hand-height[i] for i > 0) + right-hand-height[-1]+1
    = n-1 + (right-hand-height[0]-right-hand-height[-1]) + right-hand-height[-1]+1
    = n
so, len(seq) == 2n
accumulate seq to each 1's will yield right-hand-height
assert x >= 0 for x in accumulate(seq)


# sequence of +/-1's of 2n with "x >= 0 for x in accumulate(seq)" <-> path in {path(n,n)}
since num(hstep's) >= num(vstep's) in partial path
+1 <-> hstep
-1 <-> vstep

or let's reverse the path, from (0,0) to (q,q)
+1 <-> -vstep (with value 0 to allow 0 offset of prefix in some cases)
-1 <-> -hstep




now, review:
    array of len n
    <-> Canonical Cartesian Tree of size n
    --> binary tree struct of size 2n+1
    <-> right-hand-height of len n with "rhh[0]=0 and 0<=rhh[i]<=rhh[i-1]"
    <-> sequence of +/-1's of len 2n with "x >= 0 for x in accumulate(seq)"
    <-> path in {path(n,n)}
    <-> [0..CT(n)-1]

'''


from .Catalan_number import Catalan_numbers, Catalan_number

import itertools
from .factorial import choose, factorial


#print([[choose(q+p-1, p) for p in range(q+1)] for q in range(10)])

class Xballot:
    def __init__(self, Q):
        self.table = xballot_numberss(Q)
    def __call__(self, q, p):
        if not 0 <= p <= q:
            return 0
        # assert q < Q
        return self.table[q][p]
    

def xballot_numberss_definition(Q):
    '''xballot(q, p) = ballot(p, q)


xballot(q>=0, p=0) = 1
xballot(q>p, p>0) = xballot(q-1, p) + xballot(q, p-1)
xballot(q=p, p>0) = xballot(q, p-1)
xballot(q,p) = 0, otherwise


fix q
note that accumulate pre row + ones
xballot(q,p) = sum (C(p+1, i) for all i) for p in [0..q]
= 2**(p+1) for p in [0..q]
'''
    xballot = [[None]*(q+1) for q in range(Q)]
    if Q <= 0:
        return xballot

    for q in range(Q):
        xballot[q][0] = 1

    for q in range(Q):
        for p in range(1, q):
            assert 0 < p < q
            xballot[q][p] = xballot[q-1][p] + xballot[q][p-1]
        xballot[q][q] = xballot[q][q-1]

    assert all(x > 0 for xs in xballot for x in xs)
    return xballot


def xballot_numberss_by_accumulate(Q):
    if Q <= 0:
        return []
    
    pre = [1]
    xballot = [pre]
    for q in range(1, Q):
        xqp = list(itertools.accumulate(pre))
        xqp.append(xqp[-1])
        pre = xqp
        xballot.append(pre)
    return xballot

def xballot_numberss(Q):
    return xballot_numberss_by_accumulate(Q)
    
                   
def test_xballot_numberss():
    for n in range(10):
        if not xballot_numberss(n) == xballot_numberss_by_accumulate(n) \
               == xballot_numberss_definition(n):
            print(xballot_numberss(n), xballot_numberss_by_accumulate(n), 
                  xballot_numberss_definition(n))
        assert xballot_numberss(n) == xballot_numberss_by_accumulate(n) \
               == xballot_numberss_definition(n)







def f():
    Q = 20
    xs = xballot_number_definition(Q)
    print(xs)
    xl = [xl[-1] for xl in xs]
    print([(q, x, factorint(x)) for q, x in enumerate(xl)])
    guess = Catalan_numbers(Q)
    print('guess/xl', [g/x for g, x in zip(guess, xl)])

    import sympy
    from sympy import factorint, binomial, Sum, simplify
    from sympy.abc import q, p, i
    s = binomial(q+p-1,p) - Sum(binomial(2*q-2*i, q-i)/(q-i+1) * binomial(p-q+2*i-1, i), (i, q-p+1, q-1))
    r = s.doit()
    print(s)
    print(simplify(r))
    t = s.subs(p, q).doit()
    print(simplify(t))

test_xballot_numberss()


def array2right_hand_height(array):
    L = len(array)

    right_hand_height = []
    stack = []
    # infix travel a binary tree of size 2n+1
    # ignore leaves
    for i in range(L):
        x = array[i]
        while stack:
            if x < stack[-1]:
                stack.pop()
            else:
                break
        right_hand_height.append(len(stack))
        stack.append(x)

    assert len(right_hand_height) == L
    assert not L or right_hand_height[0] == 0
    assert all(0 <= right_hand_height[i] <= right_hand_height[i-1]+1 for i in range(1, L))
    return right_hand_height

def right_hand_height2signed_ones(right_hand_height):
    n = len(right_hand_height)
    if not n:
        return []
    
    seq = [+1]
    assert right_hand_height[0] == 0
    for i in range(1, n):
        assert 0 <= right_hand_height[i] <= right_hand_height[i-1]+1
        k = right_hand_height[i-1] - right_hand_height[i]
        seq += [-1]*(k+1)
        seq.append(+1)
    seq += [-1]*(right_hand_height[-1]+1)
    
    assert len(seq) == 2*n
    assert sum(seq) == 0
    assert all(x >= 0 for x in itertools.accumulate(seq))
    assert all(abs(x) == 1 for x in seq)
    return seq


def encode_binary_tree_struct_of_canonical_Cartesian_tree_of_array_of_same_length(array):
    # O(n^2)
    # encode(array) == encode(array+[x]) where [x] non-increase; min(array)<=x
    
    n = len(array)
    right_hand_height = array2right_hand_height(array)
    signed_ones = right_hand_height2signed_ones(right_hand_height)
    
    xballot = Xballot(n+1)
    q = p = 0
    code = 0
    for signed_one in signed_ones:
        if signed_one == 1:
            # -vstep
            step = (1, 0)
            value = 0
        else:
            assert signed_one == -1
            # -hstep
            step = (0, 1)
            value = xballot(q-1, p+1)
            
        dq, dp = step
        q, p = q+dq, p+dp
        code += value
        
    assert q == p == n
    assert 0 <= code < Catalan_number(n)
    return code


def test_encode_binary_tree_struct_of_canonical_Cartesian_tree_of_array_of_same_length():
    array_ls = [
        [], [0], [0,1], [1,0],
        [0,1,2], [0,2,1], [1,0,2], [2,0,1], [1,2,0], [2,1,0],
        ]

    right_hand_height_ls = [
        [], [0], [0,1], [0,0],
        [0,1,2], [0,1,1], [0,0,1], [0,0,1], [0,1,0], [0,0,0],
        ]

    signed_ones_ls = [
        [], [1,-1], [1,1,-1,-1], [1,-1, 1,-1],
        [1,1,1,-1,-1,-1], [1,1,-1,1,-1,-1], [1,-1,1,1,-1,-1],
        [1,-1,1,1,-1,-1], [1,1,-1,-1,1,-1], [1,-1,1,-1,1,-1],
        ]
        
    code_ls = [
        0, 0, 1, 0,
        4, 3, 2,
        2, 1, 0,
        ]
    
    for array, right_hand_height, signed_ones, code in \
        zip(array_ls, right_hand_height_ls, signed_ones_ls, code_ls):
        try:
            assert right_hand_height == array2right_hand_height(array)
            assert signed_ones == right_hand_height2signed_ones(right_hand_height)
            assert code == encode_binary_tree_struct_of_canonical_Cartesian_tree_of_array_of_same_length(array)
        except:
            print('array', array)
            print(right_hand_height == array2right_hand_height(array),
                  right_hand_height, array2right_hand_height(array))
            print(signed_ones == right_hand_height2signed_ones(right_hand_height),
                  signed_ones, right_hand_height2signed_ones(right_hand_height))
            print(code == encode_binary_tree_struct_of_canonical_Cartesian_tree_of_array_of_same_length(array),
                  code, encode_binary_tree_struct_of_canonical_Cartesian_tree_of_array_of_same_length(array))
            raise
    
test_encode_binary_tree_struct_of_canonical_Cartesian_tree_of_array_of_same_length()













    
    
