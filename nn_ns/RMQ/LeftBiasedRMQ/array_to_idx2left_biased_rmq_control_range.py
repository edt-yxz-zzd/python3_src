
__all__ = '''
    array_to_idx2left_biased_rmq_control_range
    VerifyLeftBiasedRMQ

'''

from .canonical_Cartesian_tree.canonical_Cartesian_tree import \
    canonical_Cartesian_tree

class VerifyLeftBiasedRMQ:
    '''verify left_biased_rmq result in O(1)

what?
    see: array_to_idx2left_biased_rmq_control_range

time and space:
    init time O(L)*(a."<" + uint[..L].'+')
    verify time O(1)*uint[..L].'<'
    space O(L*log2(L))*bit
        for both space(self) and working space
'''
    def __init__(self, array):
        '''see: array_to_idx2left_biased_rmq_control_range

time and space:
    time O(L)*(a."<" + uint[..L].'+')
    space O(L*log2(L))*bit
        for both space(self) and working space
'''
        self.array_idx2left_biased_rmq_control_range\
            = array_to_idx2left_biased_rmq_control_range(array)
    def verify_left_biased_rmq_result(self, begin, end, rmq_result):
        '''time O(1)*uint[..L]."<"'''
        idx2control_range = self.array_idx2left_biased_rmq_control_range
        L = len(idx2control_range)
        #if not 0 <= begin <= rmq_result < end <= L: raise ValueError
        if not 0 <= rmq_result < L: return False
        I,J = idx2control_range[rmq_result]
        return I <= begin <= rmq_result < end <= J

def array_to_idx2left_biased_rmq_control_range(array):
    '''Ord a => [a] -> [(ArrayIdx, ArrayIdx)]

what?
    [(I,J) == array_idx2left_biased_rmq_control_range<array>(k)]
        ==>> [[k == lb_RMQ<array>(i, j)] <==> [I <= i <= k < j <= J]]
why?
    use to verify left_biased_RMQ algorithm
        O(1)
    how to verify?
        see: VerifyLeftBiasedRMQ

time and space:
    time O(L)*(a."<" + uint[..L].'+')
    space O(L*log2(L))*bit
        for both space(output) and working space

example:
    >>> this = array_to_idx2left_biased_rmq_control_range
    >>> that = array_to_idx2left_biased_rmq_control_range__ver1
    >>> def test(array):
    ...     r = this(array)
    ...     if r == that(array): return r
    ...     return AssertionError

    >>> test('')
    []
    >>> test('1')
    [(0, 1)]
    >>> test('12')
    [(0, 2), (1, 2)]
    >>> test('21')
    [(0, 1), (0, 2)]
    >>> test('123')
    [(0, 3), (1, 3), (2, 3)]
    >>> test('132')
    [(0, 3), (1, 2), (1, 3)]
    >>> test('213')
    [(0, 1), (0, 3), (2, 3)]
    >>> test('231')
    [(0, 2), (1, 2), (0, 3)]
    >>> test('312')
    [(0, 1), (0, 3), (2, 3)]
    >>> test('321')
    [(0, 1), (0, 2), (0, 3)]
'''
    ###################### ver2
    L = len(array)

    # space O(L*log2(L))*bit
    idx2begin = []      # assign value when push to stack
    idx2end = [None]*L  # assign value when pop from stack
    stack = right_open_roots = []
    indices = []

    # time O(1)*ops
    def pop():
        return indices.pop(), stack.pop()
    def push(ix, x):
        indices.append(ix), stack.append(x)

    # each element push/pop one and only one time
    # time O(L)*(a."<" + uint[..L-1].'+')
    for ix, x in enumerate(array): # O(1)*uint[..L-1].'+'
        iy = None
        while stack and x < stack[-1]: # O(1)*a."<"
            # y is x.left_child.right_child*
            iy, y = pop()
            idx2end[iy] = ix
        push(ix, x)

        # y is x.left_child if exist
        x_begin = ix if iy is None else idx2begin[iy]
        idx2begin.append(x_begin)

    while stack:
        iy, y = pop()
        idx2end[iy] = L
    return list(zip(idx2begin, idx2end))


def array_to_idx2left_biased_rmq_control_range__ver1(array):
    ###################### ver1
    (may_root, v2may_parent, v2may_left, v2may_right) \
        = canonical_Cartesian_tree(array)

    idx2begin = []
    for v, may_left in enumerate(v2may_left):
        if may_left is None:
            # no left-subtree
            # so, the control range begin by self
            idx2begin.append(v)
        else:
            # control_range<v>.begin = control_range<v.left>.begin
            left_idx = may_left
            idx2begin.append(idx2begin[left_idx])

    L = len(v2may_right)
    idx2end = [None]*L
    for v, may_right in zip(range(L-1, -1, -1), reversed(v2may_right)):
        if may_right is None:
            idx2end[v] = v+1
        else:
            right_idx = may_right
            idx2end[v] = idx2end[right_idx]
    return list(zip(idx2begin, idx2end))
array_to_idx2left_biased_rmq_control_range__ver1.__doc__ \
    = array_to_idx2left_biased_rmq_control_range.__doc__


if __name__ == "__main__":
    import doctest
    doctest.testmod()

