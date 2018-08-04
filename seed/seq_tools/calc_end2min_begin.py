
__all__ = '''
    calc_begin2max_end
    calc_end2min_begin
'''.split()

from itertools import repeat

        
    
    
def calc_end2min_begin(iterable, pred=None):
    '''largest rng that be allowed

end2begin[i] <= i && all pred seq[end2begin[i]:i]
end2begin[i] == 0 || not . pred $ end2begin[i] - 1
len(end2begin) == len(seq) + 1
'''
    if pred is None:
        pred = bool

    rng_end2begin = []
    rng_begin = len(rng_end2begin)
    rng_end2begin.append(rng_begin)
    for x in iterable:
        if not pred(x):
            rng_begin = len(rng_end2begin) # next idx
        rng_end2begin.append(rng_begin) # next idx 2 rng_begin

    # assert len(rng_end2begin) == len(iterable) + 1
    return rng_end2begin

def calc_begin2max_end_from_reversed(reversed_iterable, pred=None):
    '''largest rng that be allowed

begin2end[i] >= i && all pred seq[i:begin2end[i]]
begin2end[i] == len(seq) || not (pred begin2end[i])
len(begin2end) == len(seq) + 1
'''
    rend2rbegin = calc_end2min_begin(reversed_iterable, pred)
    L = len(rend2rbegin) - 1 # == len(seq)
    begin2end = [L-rbegin for rbegin in reversed(rend2rbegin)]
    return begin2end

def calc_begin2max_end(iterable, pred=None):
    '''largest rng that be allowed

begin2end[i] >= i && all pred seq[i:begin2end[i]]
begin2end[i] == len(seq) || not (pred begin2end[i])
len(begin2end) == len(seq) + 1
'''
    if pred is None:
        pred = bool

    begin2max_end = []
    i = -1
    for i, x in enumerate(iterable):
        if not pred(x):
            begin2max_end.extend(repeat(i, i+1-len(begin2max_end)))
            assert len(begin2max_end) == i+1
    else:
        i += 1 # len(seq)
        begin2max_end.extend(repeat(i, i+1-len(begin2max_end)))

    # assert len(rng_end2begin) == len(iterable) + 1
    return begin2max_end
          
assert calc_begin2max_end_from_reversed(reversed([1,0,1,1,0,0,1])) \
       == [1,1,4,4,4,5,7,7]
assert calc_begin2max_end([1,0,1,1,0,0,1]) \
       == [1,1,4,4,4,5,7,7]



if 0: # errrrrrrrrrrrrrrrrrrrrooooooooooorrrrrr
    def calc_rng_end2begin(iterable, pred=None):
        return rngs_to_end2begin(group_Trues_and_False(iterable, pred))
    def calc_rng_begin2end(iterable, pred=None):
        return rngs_to_begin2end(group_Trues_and_False(iterable, pred))
    print(calc_rng_begin2end([1,0,1,1,0,0,1]))
    assert calc_rng_begin2end([1,0,1,1,0,0,1]) \
           == [1,1,4,4,4,5,7,7]




