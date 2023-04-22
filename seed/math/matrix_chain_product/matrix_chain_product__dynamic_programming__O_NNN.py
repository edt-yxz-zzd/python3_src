#__all__:goto
r'''[[[
e ../../python3_src/seed/math/matrix_chain_product/matrix_chain_product__dynamic_programming__O_NNN.py

seed.math.matrix_chain_product.matrix_chain_product__dynamic_programming__O_NNN
py -m nn_ns.app.debug_cmd   seed.math.matrix_chain_product.matrix_chain_product__dynamic_programming__O_NNN

from seed.math.matrix_chain_product.matrix_chain_product__dynamic_programming__O_NNN import matrix_chain_product__dynamic_programming__O_NNN, std_api4matrix_chain_product__dynamic_programming__O_NNN


#]]]'''
__all__ = r'''
matrix_chain_product__dynamic_programming__O_NNN
    矩阵乘法链囗所有最优打括号方案囗暂存子问题结果囗立方性算法
    std_api4matrix_chain_product__dynamic_programming__O_NNN
    tail4std_api4matrix_chain_product__dynamic_programming__O_NNN
'''.split()#'''
__all__


from seed.math.matrix_chain_product.matrix_chain_product__common import check_matrix_chain_product_arg

def matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, /):
    '-> num_matrices2mno_begin_mids_end_tpls/[[(mno, begin, mids, end)]]{N} #DP:O(N**3):[N>=2]:total (N-1) matrices'
    check_matrix_chain_product_arg(矩阵乘法链维数序列)
    ls = 矩阵乘法链维数序列
    L = N = len(ls)
    #if L == 2: num_matrices2mno_begin_mids_end_tpls = [[], []]
    def _MNO__lookup(begin, end, /):
        assert begin+2 <= end
        if begin+2 == end:
            return 0
        assert begin+3 <= end
        idx = j = end-begin-1
        assert 0 <= idx <= len(lss)
        if not idx == len(lss):
            return lss[idx][begin][0]
        raise LookupError
    def _MNO__mid_(k, begin, end, /):
        #assert begin+1 <= k < k+2 <= end
        assert begin < k < end-1
        return (_MNO__lookup(begin,k+1)+_MNO__lookup(k,end)+ls[begin]*ls[k]*ls[end-1])
    def _MNO__min(begin, end, /):
        assert begin+2 <= end
        return min(_MNO__mid_(k, begin, end) for k in range(begin+1,end-1))
    def MNO(begin, end, /):
        assert begin+2 <= end
        try:
            return _MNO__lookup(begin, end)
        except LookupError:
            return _MNO__min(begin, end)
        pass

    #table_2 = [(ls[i-1]*ls[i]*ls[i+1], i-1,[i],i+1) for i in range(1,L-1)]
    #lss = [None, None, table_2]
    lss = [None, None]
        # lss[j]:j 是 矩阵个数,j==end-begin-1
    for j in range(2,L):
        table_j = [(MNO(begin,end), begin,[],end) for begin in range(L-j) for end in [begin+j+1]]
        lss.append(table_j)
    #rint(lss)

    for j in range(2,L):
        table_j = lss[j]
        for (mno, begin, mids, end) in table_j:
            assert mids == []
            mids.extend(k for k in range(begin+1,end-1) if _MNO__mid_(k, begin, end)==mno)
            assert mids

    if L > 2:
        [(mno, begin, mids, end)] = lss[L-1]
        assert begin == 0
        assert end == L

    todo = [[False for end in range(j+1, L+1)] for j in range(L)]
    ouputss = [[] for j in range(L)]
    num_matrices2mno_begin_mids_end_tpls = ouputss
    def _get(begin, end, /):
        j = end-begin-1
        table_j = lss[j]
        r = (mno, _begin, mids, _end) = table_j[begin]
        assert _begin == begin
        assert _end == end
        return r
    def _put(begin, end, /):
        j = end-begin-1
        todo[j][begin] = True
        return
    _put(0,L)
    for j in reversed(range(2,L)):
        ouputss_j = ouputss[j]
        for begin, required in enumerate(todo[j]):
            if not required: continue
            end = j+begin+1
            # output (begin, end)
            r = (mno, _begin, mids, _end) = _get(begin, end)
            for k in mids:
                _put(begin, k+1)
                _put(k, end)
            ouputss_j.append(r)

    return num_matrices2mno_begin_mids_end_tpls
    return ouputss
#end-def matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, /):

矩阵乘法链囗所有最优打括号方案囗暂存子问题结果囗立方性算法 = matrix_chain_product__dynamic_programming__O_NNN

def std_api4matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, /, *, version=1):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    num_matrices2mno_begin_mids_end_tpls = matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列)
    if version==1:
        mno_tree = tail4std_api4matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, num_matrices2mno_begin_mids_end_tpls)
    elif version==2:
        raise Exception(version) #词典序最先的最优三角化方案囗立方算法囗
    else:
        raise Exception(version)
    return mno_tree
def tail4std_api4matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, num_matrices2mno_begin_mids_end_tpls, /):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    assert len(num_matrices2mno_begin_mids_end_tpls) == len(矩阵乘法链维数序列)
    ls = 矩阵乘法链维数序列
    L = len(num_matrices2mno_begin_mids_end_tpls)
    def mk_one_mno_tree(begin, end, /):
        i = end-begin-1
        assert i >= 1
        if i == 1:
            return (0, begin, (ls[begin],ls[begin+1]))
        assert i >= 2
        for (mno, _begin, mids, _end) in num_matrices2mno_begin_mids_end_tpls[i]:
            if _begin == begin:
                break
        else:
            raise logic-err
        assert _end == end
        mid = mids[0]
        lhs_mno_tree = mk_one_mno_tree(begin, mid+1)
        rhs_mno_tree = mk_one_mno_tree(mid, end)
        return (mno, begin, lhs_mno_tree, mid, rhs_mno_tree, end, (ls[begin],ls[mid],ls[end-1]))
    return mk_one_mno_tree(0, L)



