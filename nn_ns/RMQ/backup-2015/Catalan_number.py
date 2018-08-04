
'''
Catalan Number
CT(n) = C(2n, n)/(n+1) = O(4**n/(pi*n**3)**.5 (1+O(1/n)))

CT(n) = sum CT(i)*CT(n-1-i)
sum CT(i)z**i = f(z) = 1 + z*f*f = [1-sqrt(1-4z)]/(2z)



balanced Dyck word of length 2n:
    # length of Dyck word = len(Dyck word)
    # but size of Dyck word == sum(Dyck word)
    # Dyck word is a prefix of some balanced Dyck word
    # balanced Dyck word of length 2n is of size n
    rex = [01]*
    and sum(BDW[:i]) >= ceil(i/2) for any i
    and sum(BDW) == len(BDW)/2 == n
    
    1 -> '('; 0 -> ')': oriented-rooted-tree[n+1] <==> binary-tree[2n+3]
    1 -> dxy = (1,1); 0 -> dxy = (1,-1)
        ==> (x, y) in [0..2n]*[0..n]; begin (0,0); end (2n,0)
    y is height, note abs(dy) == 1
    1 -> 1; 0 -> -1: dy list; +/-1 RMQ (range minimum quary)

    |{balanced Dyck word of length 2n}| == CT(n)
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
    '' <-> v2children = [[]]
    '(...)*' <-> (root -> sub)*
    |oriented-rooted-tree of size n| == CT(n-1); n > 0
    |ORT|(n) = sum (product |..|(i) for i in p) where sum(p) == n-1 and all(i>0 for i in p)
    CT(n) =?= sum (II CT(i) for i in p)

oriented-rooted-tree[n] <==> binary_tree[2n+1]:
    root <-> root->(None, next_sibling) (next_sibling may be a leaf, that is a new node)
    (root->sub)* <-> root->(first_children, root->next_sibling)
    since each last child(or root) brings a new right leaf,
        each old leaf brings a new left leaf,
        size(binary_tree) == size(tree) + size(last child or root) + size(leaf (root may be a leaf))
            == n + size(nonleaf + virtual-root-parent) + size(leaf)
            == 2n+1




Non-Decreasing Parking Function:
    f : [1..n] -> [1..n]
    f(i-1) <= f(i) <= i
    |{nondecreasing_parking_function of size n}| == CT(n)

    let balanced_Dyck_word : 1->(1,1) -> (1,0); 0->(1,-1)->(0,1)
    then from_balanced_Dyck_word of length 2n:
        f(i) = 1 + BDW[:index of ith 1].count(0)
    
    

    
'''


'''
Number of Binary Tree of order n
N(n) = 1 for n = 0, 1
N(n+1) = sum(N(i)*N(n-i) for i in [0,n])
error: N(n) =?= n! (imagine [1..n] -> Cartesian Tree; and any binary tree can be labelled like this, too)
tree: [2 1 3] and [3 1 2] one tree count twice

N(n) =?= C(2n, n)/(n+1) # Catalan Number

'''

def Catalan_number(n):
    return Catalan_numbers(n+1)[-1]

def Catalan_numbers(n):
    if n <= 0: return []
    
    ls = [None] * n
    ls[0] = pre = 1
    for i in range(1, n):
        #pre = ls[i-1]
        #pre *= (2*i-1)*(2*i)*i
        #pre //= (i + 1)*i*i
        pre *= (2*i-1)*2
        pre //= i+1
        ls[i] = pre
    return ls

    
def numbers_of_binary_trees_of_order_lt(n):
    if n <= 0: return []
    
    ls = [None] * n
    ls[0] = 1
    for i in range(1, n):
        ls[i] = sum(ls[j]*ls[i-1-j] for j in range(0, i))
    return ls

def test_guess(n = 100):
    assert numbers_of_binary_trees_of_order_lt(0) == Catalan_numbers(0)
    assert numbers_of_binary_trees_of_order_lt(1) == Catalan_numbers(1)
    assert numbers_of_binary_trees_of_order_lt(n) == Catalan_numbers(n)
test_guess()


