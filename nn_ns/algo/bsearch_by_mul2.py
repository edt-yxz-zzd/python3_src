# @Programming_Pearls(2nd)::14.6.7
# construct a static set for query
# static_set: size(), begin(), end(), next(i), before(i), find(T&)
# impliment static_set: sorted_array_based_set, heap_shape_tree_based_set
# when performing find() on these two set type,
#    sorted_array_based_set uses binary_search, needed divided by 2
#    heap_shape_tree_based_set just double the current index
# what we want to do is move the data from sorted_array_based_set to heap_shape_tree_based_set

class heap_shape_tree_based_set:
    def __init__(self, n):
        assert n >= 0
        self.n = n
        return

    def size(self):
        return self.n

    def begin(self):
        if self.size() == 0: return self.end()
        ln = self.size().bit_length()
        return 2**(ln-1) - 1

    def last(self):
        big = heap_shape_tree_based_set(self.size()+1) # big.size() > 0
        #return big.begin() - 1 # maybe -1 that is self.end()
        i = big.begin() - 1
        if i not in range(self.size()):
            return self.end()
        else:
            return i

    def end(self):
        #return -1
        return 0.3 # I don't think end() should be a meaningful value
        
    def left_child(self, i):
        m = i*2 + 1
        if m < self.size(): return m
        return self.end()
        
    def right_child(self, i):
        m = i*2 + 2
        if m < self.size(): return m
        return self.end()
    
    def parent(self, i):
        if i == 0: return self.end()
        return (i-1)//2
    
    def left_parent(self, i):
        if i%2 == 0: return self.parent(i)
        return self.end()
    
    def right_parent(self, i):
        if i%2 == 1: return self.parent(i)
        return self.end()
    
    def left_most_descendant(self, i):
        'return left_child(i) == self.end()? i : left_most_descendant(left_child(i))'
        while True:
            j = self.left_child(i)
            if j == self.end(): return i
            i = j
            
    def right_most_descendant(self, i):
        while True:
            j = self.right_child(i)
            if j == self.end(): return i
            i = j
            
    def left_most_ancestor(self, i):
        while True:
            j = self.left_parent(i)
            if j == self.end(): return i
            i = j
            
    def right_most_ancestor(self, i):
        while True:
            j = self.right_parent(i)
            if j == self.end(): return i
            i = j

    def before_i(self, i):
        if i == self.end():
            return self.last()
        
        b = self.left_child(i)
        if b != self.end():
            return self.right_most_descendant(b)

        b = self.right_most_ancestor(i)
        b = self.left_parent(b)
        if b != self.end():
            return b
        return self.end()
        
    def next_i(self, i):
        b = self.right_child(i)
        if b != self.end():
            return self.left_most_descendant(b)

        b = self.left_most_ancestor(i)
        b = self.right_parent(b)
        if b != self.end():
            return b
        return self.end()
        

def sorted_array_to_heap_shape_tree(sorted_array):
    n = len(sorted_array)
    h = heap_shape_tree_based_set(n)
    ls = [[]] * h.size()
    i = h.begin()
    for j in range(h.size()):
        ls[i] = sorted_array[j]
        i = h.next_i(i)
    assert i == h.end()
    return ls
        


def list_n_index(n, ls = [], root = 1, offset = 0):
    assert n >= 0
    assert root > 0

    this_func = list_n_index
    if n == 0: pass
    elif n == 1:
        ls[root] = offset+0
    else: 
        ln = n.bit_length()
        bn = bin(n)[-ln:]
        #print('root = ', root, 'n=', n, 'ln=', ln, 'bn=', bn)
        if bn[1] == '1':
            n_left = 2**(ln-1) - 1
            n_right = n - n_left - 1
        else:
            n_right = 2**(ln-2) - 1
            n_left = n - n_right - 1
        assert n_left >= n_right >= 0 and n_left + 1 + n_right == n

        #print('n=', n, '; n_left=', n_left, '; n_right=', n_right)
        ls[root] = offset + n_left
        this_func(n_left, ls, 2*root, offset+0)
        this_func(n_right, ls, 2*root+1, ls[root]+1)
    return ls


def reorder_index_using_stack(n):
    def left_of_i(i): return 2*i + 1
    def right_of_i(i): return 2*i + 2
    
    assert n >= 0
    if n == 0: return []
    length = n
    L = ['*']*length
    U = ['*']*length
    x = ['*']*length
    L[0] = 0 # note n >= 1
    U[0] = n # [l,u)
    for i in range(n):
        assert L[i] < U[i]
        m = U[i] - L[i] # m > 0
        if m < 3:
            if m == 1:
                x[i] = L[i]
            else: # m == 2
                x[i] = L[i]+1
                i_left = left_of_i(i)
                #print('n=', n, 'm=', m, 'i=', i, 'i_left=', i_left)
                #print('L=', L, 'U=', U, 'x=', x)
                L[i_left] = L[i]
                U[i_left] = x[i]
        else:
            lm = m.bit_length()
            assert lm >= 2
            min_right_plus_1 = 2**(lm-2)
            max_left_plus_1 = 2 * min_right_plus_1
            th = min_right_plus_1 + max_left_plus_1
            if m < th:
                m_right = min_right_plus_1 - 1
                m_left = m - min_right_plus_1
            else:
                m_left = max_left_plus_1 - 1
                m_right = m - max_left_plus_1
            assert m == m_left + 1 + m_right
            assert m_left >= m_right > 0

            x[i] = L[i] + m_left
            i_left = left_of_i(i)
            L[i_left] = L[i]
            U[i_left] = x[i]
            i_right = right_of_i(i)
            L[i_right] = x[i] + 1
            U[i_right] = U[i]
        assert L[i] <= x[i] < U[i]
    return x




def t2(m=6, n=1):
    for i in range(n,m):
        print(i, ',', reorder_index_using_stack(i))
        assert list_n_index(i, ['*']*(i+1))[1:] == reorder_index_using_stack(i)

def t(m=6, n=0):
    for i in range(n,m):
        h = heap_shape_tree_based_set(i)
        ls = sorted_array_to_heap_shape_tree(range(i))
        r = reorder_index_using_stack(i)
        if ls != r:
            print('ls=', ls, 'r=', r)
        else:
            print(ls)
        assert ls == r
        

    


    
