
#e ../../python3_src/seed/algo/iter_pair_schedule4complete_graph_.py

# 完全图K[L]: 枚举两点，尝试一笔画，最小化 笔画数
#   [L == 2]: 1笔
#   [L > 2][L%2==1]: 1笔
#       K[5] == K[3] --> 0 --3-> 1 --4-> 2 --3-4-> 0
#   [L > 2][L%2==0]: L///2笔#其中(L///2-1)笔 各连接两点，消除(L-2)各奇节点，剩下两个奇节点 可一笔画
#       K[4] == K[3] --> 0 --3-> 1; 3 --> 2.
def iter_pair_schedule4complete_graph_(L, /):
    '-> Iter (int%L, int%L) # [total num pairs == L*(L-1)///2] # [total num sort phases == if L<2 then 0 elif L==2 or L&1==1 then L*(L-1)///2+1 else L*L///2]'
    if L < 3:
        if L == 2:
            yield (0, 1)
        return
    # [3 <= L]
    n = 3 #K[3]
    yield (0, 1)
    yield (1, 2)
    yield (2, 0)
    # !! [3 <= L]
    # !! [n == 3]
    # [n <= L]
    # [n%2 == 1]
    while n+2 <= L:
        # [n+2 <= L]
        # [n%2 == 1]
        n += 2
        # [n <= L]
        # [n%2 == 1]
        # K[n] except K[n-2]
        n3 = n-3
        n2 = n-2
        n1 = n-1
        for i in range(0, n3, 2):
            yield (i, n2)
            yield (n2, i+1)
            yield (i+1, n1)
            yield (n1, i+2)
        yield (n3, n2)
        yield (n2, n1)
        yield (n1, 0)
        # [n <= L]
        # [n%2 == 1]
    # [n <= L]
    # [n%2 == 1]
    # [n+2 > L]
    # [L-1 <= n <= L]
    if n == L:
        return
    # [n == L-1]
    # !! [n%2 == 1]
    # [L%2 == 0]
    assert n == L-1
    for i in range(0, n-1, 2):
        yield (i, n)
        yield (n, i+1)
    yield (n-1, n)
    return
def test4iter_pair_schedule4complete_graph_():
    for L in range(10):
        ps = [*iter_pair_schedule4complete_graph_(L)]
        assert all(0 <= i < L for p in ps for i in p)
        assert not any(i == j for i,j in ps)
        assert len(ps) == L*(L-1)//2
        assert len(ps) == len({*ps})
        assert len(ps) == len({(*sorted(p),) for p in ps})
        prev = -1
        acc = 0
        num_strokes = 0
        for i, j in ps:
            num_strokes += not i == prev
            acc += not i == prev
            acc += 1
            prev = j
        if L < 2:
            assert acc == 0
            assert num_strokes == 0
        elif L&1 == 0 and L >= 4:
            assert acc == L**2//2
            assert num_strokes == L//2
        else:
            assert acc == 1 +L*(L-1)//2
            assert num_strokes == 1
if __name__ == "__main__":
    test4iter_pair_schedule4complete_graph_()











from seed.algo.iter_pair_schedule4complete_graph_ import iter_pair_schedule4complete_graph_
