

class GrayCodeFocus:
    def __init__(self, n):
        if n < 0:
            n = 0
        self.n = n
    def __iter__(self):
        
        n = self.n
        focus = list(range(n+1))
        assert focus[-1] == n
        while True:
            j = focus[0]
            focus[0] = 0
            if j == n: break
            j1 = j+1
            focus[j] = focus[j1]
            focus[j1] = j1
            yield j


class GrayCode_LooplessReflectedMixedRadices:
    def __init__(self, radices):
        self.radices = tuple(radices)
        if any(radix <= 1 for radix in radices):
            raise ValueError('any(radix <= 1 for radix in radices)')
        
    def __iter__(self):
        radices = self.radices
        n = len(radices)
        if n == 0:
            return
        
        deltas = [1] * n
        code = [0] * n
        focus = list(range(n+1))
        
        yield n-1, -1, code
        while True:
            j = focus[0]
            focus[0] = 0
            if j == n: break
            old_delta = deltas[j]
            code[j] += old_delta

            if code[j] == 0 or code[j] == radices[j]-1:
                deltas[j] = -deltas[j]
                j1 = j+1
                focus[j] = focus[j1]
                focus[j1] = j1
            
            yield j, old_delta, code
        
        
def gray_code(n):
    focus = GrayCodeFocus(n)
    code = [False] * n
    yield code
    for j in focus:
        code[j] = not code[j]
        yield code

def gray_code_for_reflected_mixed_radices(radices):
    gg = GrayCode_LooplessReflectedMixedRadices(radices)
    yield from gg

def permutation_easy(iterable):
    perm = list(iterable)
    n = len(perm)
    yield perm

    changes = permutation_easy_idx(n)
    for _ in changes:
        break
    else:
        return
    
    for it_pos, other_pos in changes:
        perm[it_pos], perm[other_pos] = perm[other_pos], perm[it_pos]
        yield perm
def permutation_easy_idx(n):
    gg = GrayCode_LooplessReflectedMixedRadices(range(2, n+1))
    perm_count = list(range(n))
    perm_count[-1] = 1
    
    for j, delta, code in gg:
        print('perm_count', perm_count)
        it_pos = j+1
        
        init_it = it_pos # initial perm[it_pos]
        init_order = -1  # initial change it, the order of perm[:it_pos], is descending

        it = perm_count[it_pos]
        if it == 0: raise logic-error
        
        order = (init_it-it)%2 * 2 - 1
        if order == 1:
            other_pos = it - 1
            print(other_pos, it_pos, it, init_it)
        else:
            assert order == -1
            other_pos = it_pos - it
            print(other_pos, it_pos, it)
        #assert it - 1 == perm[other_pos] only at init change
        if it > 1:
            perm_count[it_pos] -= 1
        else:
            perm_count[it_pos] = init_it
        yield it_pos, other_pos

        
    
def permutation_plain_change(iterable):
    perm = list(iterable)
    n = len(perm)
    yield perm
    

    changes = permutation_plain_change_idx(n)
    for _ in changes:
        break
    else:
        return
    for it_pos, delta in changes:
        other_pos = it_pos + delta
        perm[it_pos], perm[other_pos] = perm[other_pos], perm[it_pos]
        yield perm
    
def permutation_plain_change_idx(n):
    if not isinstance(n, int):
        raise TypeError('not isinstance(n, int)')
    if not n >= 2:
        return iter(())
        raise ValueError('not n >= 2')
    
    return __impl_permutation_plain_change_idx(n)
def __impl_permutation_plain_change_idx(n):
    assert n >= 2
    gg = GrayCode_LooplessReflectedMixedRadices(range(n, 1, -1))
    perm = list(range(n))
    perm[1], perm[0] = perm[0], perm[1]

    # each round : there is a range rng=(begin, end), size = end-begin
    # in block=perm[begin:end] is 0 ~ size-1, let it = size-1, radix=size
    # all x >= size are at left or right of this range
    # we need to find out 'end', that is block_base[it]
    # obviousely, it < size <= block_base[it] <= n
    # gray_code point out which two items in perm to be changed
    # j indicates that radix = n-j, therefore it = n-1-j
    # -1-old_code[j] and -1-code[j] are index in block for it to change from to.
    # after interchange 'end' of it-code[j] increase +/-1
    block_base = list(range(1, n+1))
    block_base[0] = 2
    
    for j, delta, code in gg:
        radix = n-j
        assert 0 <= j < n-1
        assert 0 <= code[j] < radix
        it = n-1-j
        codej = code[j]
        old_codej = codej - delta

        end = block_base[it]
        other_pos = end-1 - codej
        it_pos = end-1 - old_codej
##        print(dict(j=j, it=it, delta=delta, codej=codej, old_codej=old_codej,
##                   end=end, it_pos=it_pos, other_pos=other_pos, perm=perm,
##                   block_base=block_base))
        
        assert perm[it_pos] == it
        perm[it_pos], perm[other_pos] = perm[other_pos], perm[it_pos]
        assert other_pos == it_pos - delta
        yield it_pos, -delta
        del it_pos, other_pos

        his = it - max(codej, old_codej)
        assert 0 <= his < it
        block_base[his] += delta
##        if not his < block_base[his] <= n:
##            print(his, block_base, delta)
        assert his < block_base[his] <= n
        #yield perm
    return

def _show():
    print('\n'.join(str(gc) for gc in gray_code(5)))
    print('\n'.join(str(gc) for gc in 
                gray_code_for_reflected_mixed_radices(range(3,2,-1))))
    print('\n'.join(str(gc) for gc in 
                gray_code_for_reflected_mixed_radices(range(3,1,-1))))
    print('\n'.join(str(gc) for gc in 
                gray_code_for_reflected_mixed_radices(range(4,1,-1))))
    print('\n'.join(str(gc) for gc in 
                gray_code_for_reflected_mixed_radices([2]*3)))

    for i in reversed(range(6)):
        print('\n'.join(str(p) for p in permutation_plain_change(range(i))))
        

_show()


print('\n'.join(str(gc) for gc in 
                gray_code_for_reflected_mixed_radices(range(2,5))))

list(map(print, permutation_easy(range(4))))
