r'''

r : rule index
i < j : rule pos
a <= x : string pos ! empty production
for some a < x: (a, x) -> (r, i, j)
src[a:x] parse to rule[r][i:j]
if rule[r][:]: -> ID[r] -> for some rk: (rk, n, n+1)


left[x] = {(r, j): {(i,a)}}
right[a] = {(r, i): {(j x)}}
place[r] = {(rk, n)}
token2rules[token] = [r...]

r2rks = {r:{rk}}
rk2refs = {(r,k):[ref...]}
'''




def update_left_right(rk, k,j, z,y):
    assert 0 <= k <= j
    assert 0 <= z <= y
    if (rk, k,j, z,y) not in decompose:
        q.append((rk, k, j,  z, y))
        left[y][(rk,j)] = (k,z)
        right[z][(rk,k)] = (j, y)
    else:
        assert not decompose[(rk, k,j, z,y)]
    
decompose = {}
def add(rk, k, i, j,   z, x, y):
    assert 0 <= k <= i <= j
    assert 0 <= z <= x <= y

    t = (rk, k,j, z,y)
    if t not in decompose:
        update_left_right(*t)
        decompose[t] = [(i,x)]
    else:
        decompose[t].append((i,x))
        pass
    
refs = {}
def try_expand_rij_if_full(rk, i,j, z,y):
    r, _ = rk
    if i == 0 and j == len(rk2refs[rk]):
        for rk_, n in place[r]:
            t = rk_, n, n+1,   z,y
            if t not in decompose:
                update_left_right(*t)
                decompose[t] = {rk}
            else:
                decompose[t].add(rk)









    
    




r2rks = {'m':{0, 1}, 'a':{5}}

rk2refs = {('m',0):['m', 'a', 'm'], ('m',1):['a']}
token2rules = {'T':'a'}

tokens = 'T' * 5

place = {}
for rk, ids in rk2refs.items():
    for n, ref in enumerate(ids):
        if ref not in place:
            place[ref] = []
        place[ref].append((rk, n))

token2place = {t: [(rk, n) for r in token2rules[t] for rk, n in place[r]] for t in set(tokens)}

q = []
L = len(tokens)
left = [{} for _ in range(L+1)]
right = [{} for _ in range(L+1)]
for x, t in enumerate(tokens):
    for rk, n in token2place[t]:
        update_left_right(rk, n, n+1, x, x+1)







while q:
    rk, i, j,   x, y = q.pop()
    try_expand_rij_if_full(rk, i,j, x,y)

    # z..x + x..y
    s = left[x].get((rk, i), [])
    for k, z in s:
        add(rk, k, i, j,   z, x, y)
        
    # x..y + y..z
    s = right[y].get((rk, j), [])
    for k, z in s:
        add(rk, i, j, k,   x, y, z)

    





