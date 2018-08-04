
'''
ns = Nexts([A, B, C])
for a, b, c in ns:
    ...
    if used a:
        ns.use(0)
    if used b:
        ns.use(1)
else:
    iterators = ns.get_remains_and_destroy()
    at least one halts or no iterators at all

'''


__all__ = '''
    Nexts
    merge_two_sorted_lists
    intersect_two_sorted_lists
'''.split()



from itertools import chain


class Nexts:
    def __init__(self, iterables):
        self.iterators = tuple(map(iter, iterables))
        if not self.num_iters:
            raise ValueError('no iterables at all')
        
        self.next_iterator_indices = set(range(self.num_iters))
        self.remain_heads = [None] * self.num_iters
        self.halt_indices = set()
        self.step()


    @property
    def num_iters(self):
        return len(self.iterators)
    def step(self):
        if self.halt_indices:
            return
        for i in self.next_iterator_indices:
            if i < 0:
                raise ValueError
            
            it = self.iterators[i]
            for head in it:
                self.remain_heads[i] = head
                break
            else:
                self.halt_indices.add(i)
                self.remain_heads[i] = None
                continue
        
        self.next_iterator_indices.clear()
    def __iter__(self):
        while not self.halt_indices:
            yield tuple(self.remain_heads)
            self.step()
    def use(self, idx):
        if idx < 0:
            idx += self.num_iters
        if not 0 <= idx < self.num_iters:
            raise ValueError('not -num_iters <= idx < num_iters')
        self.next_iterator_indices.add(idx)
    def uses(self, idc):
        list(map(self.use, idc))
        return
        self.next_iterator_indices.update(idc)
    
    
    def get_remains_and_destroy(self):
        t = tuple(it if i in self.halt_indices
                     else chain([self.remain_heads[i]], it)
                  for i, it in enumerate(self.iterators))
        
        # close
        self.iterators = (None,)*self.num_iters
        
        return t
    


def merge_two_sorted_lists(xs, ys):
    ns = Nexts([xs, ys])
    for x, y in ns:
        if y < x:
            ns.use(1)
            yield y
        else:
            ns.use(0)
            yield x
    else:
        xs, ys = ns.get_remains_and_destroy()
        yield from xs
        yield from ys


def intersect_two_sorted_lists(xs, ys):
    'sorted list as multiset'
    ns = Nexts([xs, ys])
    for x, y in ns:
        if y < x:
            # discard y
            ns.use(1)
        elif x < y:
            # discard x
            ns.use(0)
        else:
            # x == y
            yield x
            ns.uses([0,1])
            

def test_merge_two_sorted_lists():
    data = [
        ([], []),
        ([], [1]),
        ([1], [1]),
        ([0,3], [1,2]),
        ]
    for xs, ys in data:
        ls = list(merge_two_sorted_lists(xs, ys))
        ans = xs+ys
        ans.sort()
        assert ls == ans

test_merge_two_sorted_lists()


def test_intersect_two_sorted_lists():
    data = [
        ([], []),
        ([], [1]),
        ([1], [1]),
        ([0,3], [1,2]),
        ([0,3,4,5], [1,2,4,6]),
        ]
    for xs, ys in data:
        ls = list(intersect_two_sorted_lists(xs, ys))
        ans = sorted(set(xs) & set(ys))
        try:
            assert ls == ans
        except:
            print(xs, ys, ls, ans)
            raise

test_intersect_two_sorted_lists()

    
def test_intersect_two_sorted_lists2():
    data = [
        ([], [], []),
        ([], [1], []),
        ([0], [1], []),
        ([1], [1], [1]),
        ([1], [0,1], [1]),
        ([0], [1,2], []),
        ([1], [1,2], [1]),
        ([2], [1,2], [2]),
        ([0,2], [1,2], [2]),
        ([0,1], [1,2], [1]),
        ([1,2], [1,2], [1,2]),
        ]
    for a, b, r in data:
        for a, b in [(a,b), (b,a)]:
            assert r == list(intersect_two_sorted_lists(a, b))



test_intersect_two_sorted_lists2()










    
