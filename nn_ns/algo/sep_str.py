from uint_map import choose

import test_all
exec(test_all.text)


'''
FA
symbol table is [0,W)
any symbol is an input, so a string is a sequence of inputs.
inital state: i = 0, stop state: i = L
jump_count table: T[i][j] = number of symbols that make FA of state i to go to state j.
assert sum T(i,:) <= W, W-sum T(i,:) is the number of symbols that lead state i stop.
state_count_vector records the count of each state
let e0 = [1,0...], len(e0) = L
e0*T^n tells us how many n length strings get FA of state 0 becoming state i.

given a string D to separate string s,L = len(D) > 0
we get s = (... + p[1] + D +) p[0]
D is not a substring of p[0] or p[j] + D[:-1], j > 0
the case of p[0]: how many strings of length n do not have D as a substring?
    we can construct a FA. what T(D) looks like?
    T(D) is a matrix of L*L
    T(D)[i][i+1] = 1
    T(D)[i][j] = 0, j > i+1
    T(D)[i][j] = xxxx D[:j-1] != D[i-(j-1):i]?0:1, 1 <= j <= i, bug!!!!!!!!!!!!!!!!!!!!!!!!!!lengthest prefix own char
    sum T(D)(i,:) = W, i != L-1
    sum T(D)(L-1,:) = W-1
    T(D) can be built from the KMP_failure_function
    NOTE:T('011') = T('012')
    let v1 = [1...]'
    ans = e0*T^n*v1
    NOTE:T('001')!=T('011') but ans is the same
the case of p[>0]: how many strings of length n that do not have D as a substring after append D[:-1] is there?
    let v2[i] = D is a substring of D[:i]+D[:-1]? 0:1
    ans = e0*T^n*v2
the case of s that does not have p[m]: how many strings of length n that contain D less than m time. m > 0
    let Tm be an mL*mL matrix
    Tm(m*i:m*i+m,m*i:m*i+m) = T(D)
    Tm(m*i+m-1,m*i+m) = 1
    other elements of Tm is 0
    ans = [1,0..]*Tm^n*[1..] = u*Tm^n*v
    change v will give more details.
    
T = B^-1 * TJ * B
     |...  0   0  |
TJ = | 0   J   0  | = diag(J0,J1,...)
     | 0   0  ... |
    |r 1 0 0..|
J = |0 r 1 0..|
    |0 0 r 1 0|
    |..    .. |
    |..    0 r|
T^n -> TJ^n -> J^n
in this case, W = 1+r, D='0', T(D)=[r], Tm(D) = J, m = len(J[i])
J is a FA that reject a string that contain more than m-1 0's.
J^n[i] = I[i] * J^n = [num of strs of len n contain j 0's after put i 0's before it]
= [num of strs of len n contain j-i 0's]
so J^n[i][j] = choose(j-i,n)*r^(n-(j-i))
choose(j-i,n) is a polynomial of n less than m times.
guess: given vector of len(L) u,v.
    for T1, T2 are both L*L matrice, 
    1) T1^i*v = T2^i*v
    2) u'*T1^i*v = u'*T2^i*v
    if 1) is true for i in [1,L] then 1) is true for any i in N
    proof:
        if T^k*v is in the space of <T^i*v for i in [0,k)>, then any j >=k, T^j*v is, too.
        min k <= L
        let T^L*v = [T^j*v for j in [0,L)]*b, b may not be unique.
        T^i*v = [T^j*v for j in [0,L)]*[I[:,1:),b]^i*I[:,0]
        T^i*v is determined by the previous L+1 values since b is yielded from T^[0,L].
    note that each 1) contains L equations, so L 1)'s is total L*L equations that is of the same number of the various in T.
    since each 2) is only one equation, maybe if 2) is true for i in [1,L^2] then true for any i.
    if 2) is true for i in [1,2L-1] then 2) is true for any i in N
    proof:
        like above, we have:
        f(i) = u'*T^i*v = u'*[T^j*v for j in [0,L)]*[I[:,1:),b]^i*I[:,0] = [f(i)]'*[I[:,1:),b]^i*I[:,0]
        F(i) = [f(j) for j in [i,i+L)] = [I[:,1:),b]'^i*F(0)
        so 1) says F(i) is determined by F(0..L)
        that is, f(i) is determined by f(0..2L-1)

    
D => T(D) <=> KMPff(D) => 1) I[0]*T^i 2) T^i*v1 3)T^i*v2 4)I[0]*T^i*v1 5) I[0]*T^i*v2

'''

def std_sep_str(s):
    'given a string, we can map it into the standard separate string form'
    f = []
    d = dict()
    new_id = 0
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = new_id
            new_id += 1
        f.append(d[s[i]])
    return tuple(f)



def enum_std_sep_str(n):
    'yields all the standard separate string forms of length n'
    assert n > 0
    s = [0] * n
    m = [0] * n # m[i] = max(s[0:i])
    m[0] = -1
    ss = [tuple(s)]
    i = n - 1 # the last member that can grow
    while(i > 0):
        s[i] += 1
        s[i+1:] = [0] * (n-i-1)
        m[i+1:] = [max([m[i],s[i]])] * len(m[i+1:])
        ss.append(tuple(s))
        for i in range(n-1,-1,-1):
            if s[i] <= m[i]:
                break
    return ss
        
def total_std_sep_str(n):
    assert n > 0
    if n == 1:
        return 1
    tot = 1 # for i == n
    self = total_std_sep_str
    for i in range(1,n):
        tot += choose(i-1, n-1) * self(n-i)
    return tot

def total_std_sep_str_2nd(n):
    assert n >= 0
    self = [0,1]
    if n < 2:
        return self[:n+1]
    for j in range(2,n+1):
        tot = 1 # for i == j since '' is not a std_sep_str so that self[0] == 0
        for i in range(1,j):
            tot += choose(i-1, j-1) * self[j-i]
        self.append(tot)
    return self


def match_FA_def(s):
    assert len(s) > 0
    fa = [{s[0]:1}]
    for i in range(1,len(s)):
        jump = {}
        suffix_list = ([s[j:i] for j in range(i)] + [s[0:1]])
        suffix_list.sort()
        beg = suffix_list.index(s[0:1])
        this = suffix_list.index(s[:i], beg+1)
        suffix_list = [s[0:0]] + suffix_list[beg+1:this+1]
        
        for sj in suffix_list:
            L = len(sj)
            if sj == s[:L]:
                jump[s[L]] = L+1
        fa.append(jump)
    return tuple(fa)


def failure_function_of_Knuth_Morris_Pratt(s):
    L = len(s)
    j = 0
    ff = [0]
    for i in range(1,L):
        while j != 0 and s[i] != s[j]:
            j = ff[j-1]
        if s[i] == s[j]: j += 1
        ff.append(j)

    assert len(ff) == L
    return tuple(ff)

def match_FA_KMP(s):
    ff = failure_function_of_Knuth_Morris_Pratt(s)
    L = len(s)
    fa = [{s[0]:1}]
    for i in range(1,L):
        jump = dict(fa[ff[i-1]])
        jump[s[i]] = i+1
        fa.append(jump)
    return tuple(fa)

def fmt_mx_uv(mx, u, v1, v2):
    #mx = (tuple(r) for r in mx)
    #u = (tuple(r) for r in u)
    mx = tuple(map(tuple, mx))
    u = tuple(map(tuple, u))
    v1,v2 = map(tuple, (v1,v2))
    return (mx, u, v1, v2)

def sep_str_mx_uv_def(s):# without W!!!!
    'u*([[W]+[0]*(L-1)]*L+T)^n*v1 ( or v2 if not the last chunk)'
    L = len(s)
    
    u = [0]*L
    u[0] = 1
    u = [u] # row vector
    
    v1 = [1]*L
    v2 = [1]*L
    for i in range(L):
        s_ = s[:i] + s[:-1]
        for j in range(i):
            if s == s_[j:j+L]:
                v2[i] = 0
                break
    mx = []
    for i in range(L):
        r = [0]*L
        r[0] = -1
        used = [s[i]]
        for j in range(i,0,-1):
            if s[:j-1] == s[i-(j-1):i] and s[j-1] not in used:
                used.append(s[j-1])
                r[j] = 1
                r[0] -= 1
        mx.append(r)
    for i in range(L-1):
        mx[i][i+1] = 1
    
    return fmt_mx_uv(mx, u, v1, v2)

def sep_str_mx_uv_KMP(s):
    L = len(s)
    
    u = [0]*L
    u[0] = 1
    u = [u] # row vector
    
    v1 = [1]*L
    
    v2 = [1]*L
    ff = failure_function_of_Knuth_Morris_Pratt(s)
    j = ff[-1]
    while j != 0:
        v2[L-j] = 0 # since s == s[:L-j] + s[:j], s[L-j]+s will be treated as s+s[j+1:]
        j = ff[j-1]

    fa = match_FA_KMP(s)
    mx = []
    for i in range(L):
        jump = fa[i]
        r = [0]*L
        r[0] = -len(jump)
        for ch in jump:
            if jump[ch] != L:
                r[jump[ch]] += 1
        mx.append(r)
        
    return fmt_mx_uv(mx, u, v1, v2)

def sort_and_unify(ls):
    ls = list(ls)
    ls.sort()
    i = len(ls)-1
    while i > 0:
        for j in range(i-1, -1, -1):
            if ls[j] != ls[i]:
                ls[j+2:i+1] = []
                i = j
                break
        if i != j:
            ls[1:i+1] = []
            i = j
    return ls
                
    
def classify_sep_str_mx(n):
    ss = enum_std_sep_str(n)
    #cls = [sep_str_mx_uv(s)[0] for s in ss]
    #return sort_and_unify(cls)
    cls = list({sep_str_mx_uv_def(s)[0] for s in ss})
    return cls
    

def enum_KMPff_def(n):
    ss = enum_std_sep_str(n)
    #cls = [failure_function_of_Knuth_Morris_Pratt(s) for s in ss]
    #return sort_and_unify(cls)
    cls = list({tuple(failure_function_of_Knuth_Morris_Pratt(s)) for s in ss}) #unify
    cls.sort() # fuck the unordered set!!!
    return cls

def enum_KMPff_choose_symbol_impl(n):
    self = enum_KMPff_choose_symbol_impl
    ff = (0,)*n
    d = ((0,),)*n # == [ [ff^j[i] for any j if ff^(j-1)[i] != 0] ] in decrease order
    p = tuple(range(n))
    # 0 <= p[i] <= i,
    # s[p[i]] == s[i],
    # s[i] not in s[:p[i]];

    ffs = [(ff,d,p)]
    if n == 1: return ffs
    ffs_ = self(n-1)
    ffs = []
    for (ff,d,p) in ffs_:
        ids = set()
        for i in range(len(d[-1])):
            #s[d[-1][i]] not in s[d[-1][:i]]
            #s[d[-1][i]] == s[n-1]
            id_ = p[d[-1][i]]
            if id_ in ids: continue
            ids.add(id_)
            new_fn = d[-1][i]+1
            new_d = d + ((new_fn,)+d[new_fn-1],)
            new_ff = ff + (new_fn,)
            new_p = p + (id_,)
            ffs.append((new_ff,new_d,new_p))
        id_ = n-1
        new_fn = 0
        new_d = d + ((new_fn,),)
        new_ff = ff + (new_fn,)
        new_p = p + (id_,)
        ffs.append((new_ff,new_d,new_p))
    return ffs
            
    
def enum_KMPff_choose_symbol(n):
    assert n > 0
    ffs = [t[0] for t in enum_KMPff_choose_symbol_impl(n)]
    ffs.sort()
    return ffs

def enum_KMPff_choose_symbol_2nd_impl(n):
    self = enum_KMPff_choose_symbol_2nd_impl
    ff = (0,)*n
    p = tuple(range(n))
    # 0 <= p[i] <= i,
    # s[p[i]] == s[i],
    # s[i] not in s[:p[i]];

    ffs = [(ff,p)]
    if n == 1: return [[], ffs]
    ffss = self(n-1)
    ffs_ = ffss[-1]
    ffs = []
    for (ff,p) in ffs_:
        ids = set()
        i = n-1
        while i:
            i = ff[i-1]
            id_ = p[i]
            if id_ in ids: continue
            ids.add(id_)
            new_ff = ff + (i+1,)
            new_p = p + (id_,)
            ffs.append((new_ff,new_p))
        id_ = n-1
        new_ff = ff + (0,)
        new_p = p + (id_,)
        ffs.append((new_ff,new_p))
    ffss.append(ffs)
    return ffss

def enum_KMPff_choose_symbol_2nd(n):
    assert n > 0
    ffs = [t[0] for t in enum_KMPff_choose_symbol_2nd_impl(n)[-1]]
    ffs.reverse() # == ffs.sort()
    return ffs


class IntUnionSet:
    # for i in range(len(self.ls)): assert 0 <= self.ls[i] <= i
    def __init__(self, L):
        self.ls = [range(L)]
        return
    def id(self, x):
        ls = self.ls
        y = ls[x]
        while(y != x):
            ls[x] = ls[y] # skip y
            x = y
            y = ls[x]

        return x
            
    def union(self,a,b):
        ls = self.ls
        a = self.id(a)
        b = self.id(b)
        ls[a] = ls[b] = min([a,b])
        return

    def std(self):
        ls = self.ls
        for i in range(len(ls)):
            ls[i] = ls[ls[i]]
        return self

    def __eq__(self,other):
        return self.std().ls == other.std().ls

    def __ne__(self,other):
        return not (self == other)


def border_width_def(s):
    L = len(s)
    assert L > 0
    ls = []
    for i in range(L, -1, -1):
        if s[:i] == s[L-i:]: # since s[-0:] == s !!!
            ls.append(i)
    return tuple(ls)
    
def KMPff2border_width(ff):
    L = len(ff)
    assert L > 0
    ls = [L]
    while ls[-1]:
        ls.append(ff[ls[-1] - 1])
    return tuple(ls)

def border_width_by_KMP(s):
    ff = failure_function_of_Knuth_Morris_Pratt(s)
    return KMPff2border_width(ff)
    
        
def enum_border_width_def_impl(L):
    bwss = []
    ffss = enum_KMPff_choose_symbol_2nd_impl(L)
    for ffs in ffss:
        bws = set()
        for ff,p in ffs:
            bws.add(KMPff2border_width(ff))
        bwss.append(list(bws))
    return bwss
    
def enum_border_width_def(L):
    bws = enum_border_width_def_impl(L)[-1]
    #bws.sort()
    return bws
    '''
    e = enum_border_width_def
    f = lambda n: len(e(n))
    g = lambda n: [f(i) for i in range(1,n)]
    g(17) == [1, 2, 3, 4, 6, 8, 10, 13, 17, 21, 27, 30, 37, 47, 57, 62]
    '''

def enum_border_width_by_IntUnionSet_impl(L):
    fself = enum_border_width_by_IntUnionSet_impl
    assert L > 0
    bws = [(L,0)] # t == L
    m = L//2
    for t in range(m+1,L):
        bws += [(L,) + bw_L_t for bw_L_t in fself(L-t)]

    for t in range(1,m+1):
        k = L//t
        r = L - k*t
        s = t+r
        assert s < L
        bws += [tuple(range(L, s, -t)) + bw_sr for bw_sr in enum_border_width_sr_by_IntUnionSet(s,r)]

    return bws

def enum_border_width_sr_by_IntUnionSet(s,r):
    # string x s.t. len s, r is a border width,
    #               and not exist string y and n>1, s.t. x[:s-r] == y*n
    #               and
    pass
    

def enum_border_width_by_IntUnionSet(L):
    bws = enum_border_width_by_IntUnionSet_impl(L)
    bws.sort() # unify
    return bws
    
def border_width2int(bw):
    e = bw[0]
    u = 0
    for i in bw[1:]:
        u += 1
        u <<= e-i
        e = i
    u >>= 1
    return u

def enum_bwint(L):
    bwss = enum_border_width_def_impl(L)
    ls = []
    for bws in bwss:
        for bw in bws:
            ls.append(border_width2int(bw))
    ls.sort()
    return ls


def test_border_width2int():
    d = [\
        ((10,5,3,1,0), 533),\
        ]
    for (bw, i) in d:
        assert border_width2int(bw) == i
    return
        
def test_border_width_by_KMP(n = 8):
    for i in range(1,n):
        ss = enum_std_sep_str(i)
        for s in ss:
            bwDEF = border_width_def(s)
            bwKMP = border_width_by_KMP(s)
            if bwDEF != bwKMP:
                print(i, s)
                print(bwDEF, bwKMP)
                return



def test_enum_KMPff_def():pass

def test_enum_KMPff_choose_symbol(n=10):
    for i in range(1,n):
        cs = enum_KMPff_choose_symbol(i)
        df = enum_KMPff_def(i)
        if cs != df:
            print(i)
            print(df)
            print(cs)
            break
            
def test_enum_KMPff_choose_symbol_2nd(n=12):
    for i in range(1,n):
        cs = enum_KMPff_choose_symbol(i)
        cs2 = enum_KMPff_choose_symbol_2nd(i)
        if cs != cs2:
            print(i)
            print(cs)
            print(cs2)
            break
    

def test_total_std_sep_str(n=6):
    for i in range(1,n):
        ss = enum_std_sep_str(i)
        L = total_std_sep_str(i)
        if L != len(ss):
            print(L)
            print(ss)
            break
            
def test_match_FA_def():
    d = [\
        ('0', [{'0':1}]),\
        ('00',[{'0':1},{'0':2}]),\
        ('01',[{'0':1},{'0':1,'1':2}]),\
        ('000',[{'0':1},{'0':2},{'0':3}]),\
        ('001',[{'0':1},{'0':2},{'0':2,'1':3}]),\
        ('010',[{'0':1},{'0':1,'1':2},{'0':3}]),\
        ('011',[{'0':1},{'0':1,'1':2},{'0':1,'1':3}]),\
        ('012',[{'0':1},{'0':1,'1':2},{'0':1,'2':3}]),\
        ]
    for s, fa in d:
        fa_ = match_FA_def(s)
        if tuple(fa) != fa_:
            print(s, fa)
            print(fa_)
            break
        

def test_match_FA_KMP(n=9):
    for s in enum_std_sep_str(n):
        DEF = match_FA_def(s)
        KMP = match_FA_KMP(s)
        if DEF != KMP:
            print(s, DEF)
            print(KMP)
            break

def test_sep_str_mx_uv_def():
    d = [\
        ('0', [[-1]], [[1]], [1], [1]),\
        ('00',[[-1,1],[-1,0]], [[1,0]], [1,1], [1,0]),\
        ('01',[[-1,1],[-2,1]], [[1,0]], [1,1], [1,1]),\
        ('000',[[-1,1,0],[-1,0,1],[-1,0,0]], [[1,0,0]], [1,1,1], [1,0,0]),\
        ('001',[[-1,1,0],[-1,0,1],[-2,0,1]], [[1,0,0]], [1,1,1], [1,1,1]),\
        ('010',[[-1,1,0],[-2,1,1],[-1,0,0]], [[1,0,0]], [1,1,1], [1,1,0]),\
        ('011',[[-1,1,0],[-2,1,1],[-2,1,0]], [[1,0,0]], [1,1,1], [1,1,1]),\
        ('012',[[-1,1,0],[-2,1,1],[-2,1,0]], [[1,0,0]], [1,1,1], [1,1,1]),\
        ]
    for s, mx, u, v1, v2 in d:
        mx_uv = fmt_mx_uv(mx, u, v1, v2)
        mx_uv_ = sep_str_mx_uv_def(s)
        if mx_uv != mx_uv_:
            print(s, mx_uv)
            print(mx_uv_)
            break

def test_sep_str_mx_uv_KMP(n=7):
    for s in enum_std_sep_str(n):
        mx_uv = sep_str_mx_uv_def(s)
        mx_uv_= sep_str_mx_uv_KMP(s)
        if mx_uv != mx_uv_:
            print(n,s)
            print(mx_uv)
            print(mx_uv_)
            break

def test_total_std_sep_str_2nd(n=14):
    ls2 = total_std_sep_str_2nd(n)
    for i in range(1,n):
        tot = total_std_sep_str(i)
        if ls2[i] != tot:
            print(i, tot)
            print(ls2[i])
            break

t = test_border_width_by_KMP
ffKMP = failure_function_of_Knuth_Morris_Pratt
