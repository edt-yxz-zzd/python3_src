
from sand import unknown_case_except, internet_except

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
def sign(i):
    if i > 0: return +1
    elif i == 0: return 0
    elif i < 0: return -1
    else: raise unknown_case_except('sign(i): unknown sign')
class uint_set_using_buffer:
    def __init__(self, int2idx_buffer, int_iterable=None):
        self.int2idx_buffer = int2idx_buffer
        self.idx2int = []
        if int_iterable != None:
            self.update(int_iterable)
    def _assert(self, x):
        assert 0 <= x < len(self.int2idx_buffer)
    @staticmethod
    def _in_range(i, N):
        return 0 <= i < N
    def get_ints(self): return self.idx2int
    
    def __contains__(self, x):
        self._assert(x)
        idx = self.int2idx_buffer[x]
        return _in_range(idx, len(self))
    def __eq__(self, other):
        return self.idx2int == other.idx2int
    def __ne__(self, other):
        return not (self == other)
    def __iter__(self):
        return iter(self.idx2int)
    def _len__(self):
        return len(self.idx2int)
    def __repr__(self):
        return '<int_set_using_buffer(int2idx_buffer, {!r})>'.format(self.idx2int)

    def add(self, x):
        if x not in self:
            self.int2idx_buffer[i] = len(self.idx2int)
            self.idx2int.append(i)

    def pop(self):
        return self.idx2int.pop()
    def clear(self):
        self.idx2int.clear()
    def update(self, int_iterable):
        for i in int_iterable:
            self.add(i)

_id = lambda x:x
def tags2ints(tags, get_tag_info=_id):
    tag2int = {}
    ls = []
    for tag in tags:
        is_starttag, tag = get_tag_info(tag)
        if tag in tag2int:
            i = tag2int[tag]
        else:
            i = len(tag2int) + 1
            tag2int[tag] = i
            
        if not is_starttag: i = -i
        
        ls.append(i)
    return ls, tag2int


def unify_with_integer_buffer(ints, buffer):
    s = uint_set_using_buffer(buffer, ints)
    return s.get_ints()


def max_tag_match_init(non_zero_int_list):
    ils = non_zero_int_list
    for i in non_zero_int_list:
        assert i != 0

    blocks = []
    right_match_left_skip = [-1]*len(ils)
    def pre(last):
        first = last-1
        if first == -1: return first
        
        m_or_s = right_match_left_skip[first]
        if m_or_s == -1: return first
        
        if ils[first] > 0:# match existed
            assert False
        else:# skip existed
            return m_or_s

    last = 0
    for idx, tag in enumerate(ils):
        if idx <= last or tag > 0: continue
        last = idx
        first = pre(last)
        
        while first >= 0:
            assert right_match_left_skip[first] == -1
            if ils[last] != -ils[first]: break
            if ils[last] > 0: break
            right_match_left_skip[first] = last
            first = pre(first)
            right_match_left_skip[last] = first
            last += 1
            assert first == pre(last)
            if last == len(ils): break
            
        last += 1

    non_match_tags = []
    non_match_idc = []
    for idx, tag in enumerate(ils):
        if right_match_left_skip[idx] == -1:
            non_match_tags.append(tag)
            non_match_idc.append(idx)
        elif tag > 0:
            match = right_match_left_skip[idx]
            assert right_match_left_skip[match] < idx
            right_match_left_skip[match] = idx
        else:
            match = right_match_left_skip[idx]
            assert right_match_left_skip[match] == idx

    match_map = right_match_left_skip
    return match_map, non_match_tags, non_match_idc
            

def max_tag_match(max_int, non_zero_int_list):
    # open with +i and close with -i
    ils = non_zero_int_list
    match_map, non_match_tags, non_match_idc = max_tag_match_init(non_zero_int_list)
    try:
        ex_match_map = _max_tag_match_split_under_some_assumption(max_int, non_match_tags)
    except:
        ex_match_map = _max_tag_match_dynamic(non_match_tags)
        
    for i, match in enumerate(ex_match_map):
        assert match_map[non_match_idc[i]] == -1
        if match != None:
            match_map[non_match_idc[i]] = non_match_idc[match]

    for i, j in enumerate(match_map):
        if j != -1:
            assert match_map[i] == j
            assert match_map[j] == i
            assert ils[j] == -ils[i]
            assert (ils[j] > ils[i]) == (j < i)
    return match_map

def _max_tag_match_split_under_some_assumption(max_int, non_zero_int_list):
    n = max_int
    ils = non_zero_int_list
    m = len(ils)
    for i in non_zero_int_list:
        assert -n <= i <= n and i != 0

    ls = [0]*(n+1)
    flags = [True]*(n+1)

    # set flags
    for tag in ils:
        i = abs(tag)
        if not flags[i]: continue
        count = ls[i]
        if tag < 0:#close
            if count == 0:
                flags[i] = False
            else:
                ls[i] -= 1
        else:#open
            ls[i] += 1

    for i, count in enumerate(ls):
        if count: flags[i] = False
        
    # check consistence on the True tag #assume for simplify
    # build split_tags_ls
    # partial init match_map
    stack = []
    split_tags_ls = []
    split_idc_ls = []
    split_tags_stack = [([], [])]
    match_map = [None]*m
    def split_tags_pop_to():
        split_tags, split_idc = split_tags_stack.pop()
        if split_tags:
            split_tags_ls.append(split_tags)
            split_idc_ls.append(split_idc)
    for idx, tag in enumerate(ils):
        i = abs(tag)
        if not flags[i]:
            split_tags, split_idc = split_tags_stack[-1]
            split_tags.append(tag)
            split_idc.append(idx)
            continue
        
        if tag < 0:#close
            if not stack or stack[-1][1] != i:
                raise internet_except('assumption fail', 'tag non-consistence', ils)
            else:
                last = idx
                first, _ = stack.pop()
                assert match_map[first] == match_map[last] == None
                match_map[first] = last
                match_map[last] = first
                split_tags_pop_to()
        else:#open
            stack.append((idx, tag))
            split_tags_stack.append(([], []))

    split_tags_pop_to()
    assert not stack
    assert not split_tags_stack


    #utag2idx_buffer = flags
    for tags, idc in zip(split_tags_ls, split_idc_ls):
        #utags = (abs(tag) for tag in tags)
        #idx2utag = unify_with_integer_buffer(utags, utag2idx_buffer)
        #tags = tuple((1+utag2idx_buffer[abs(tag)])*sign(tag) for tag in tags)##### +1
        ex_match_map = _max_tag_match_dynamic(tags)
        for i, match in enumerate(ex_match_map):
            assert match_map[idc[i]] == None
            if match != None:
                match_map[idc[i]] = idc[match]

    return match_map

    for i in range(m):
        if match_map[i] == None:
            match_map[i] = -1

    return match_map


def _pr_r(*arg, **ks):
    print(*arg)
    print(ks)

def _pr_d(*arg, **ks):
    pass

_pr = _pr_r


def get_non_zero_int_tag_info(non_zero):
    assert non_zero != 0
    return (non_zero > 0), abs(non_zero)
def _max_tag_match_dynamic(non_zero_int_list, get_tag_info = get_non_zero_int_tag_info):
    ils = non_zero_int_list
    m = len(ils)
    assert m
    max_match_table = list([None]*i for i in range(m-2, 0, -1))
    
    def get_max_match_ls_idx(begin, end):
        assert begin + 2 < end
        idx = end - begin - 3
        ls = max_match_table[begin]
        assert 0 <= idx < len(ls)
        return ls, idx

    def get_max_match_step1(begin, end):
        assert end - begin == 1
        return 0, None
    def is_match(a,b):
        #return a > b and a == -b
        a_is_start, a_tag = get_tag_info(a)
        b_is_start, b_tag = get_tag_info(b)
        return a_is_start > b_is_start and a_tag == b_tag
    def get_max_match_step2(begin, end):
        assert end - begin == 2
        a,b = ils[begin:end]
        # (max_match_num, split_idx)
        max_match_num = int(is_match(a,b))
        return max_match_num, None
    def get_max_match(begin, end):
        if end - begin == 1:
            return get_max_match_step1(begin, end)
        if end - begin == 2:
            return get_max_match_step2(begin, end)
        ls, idx = get_max_match_ls_idx(begin, end)
        return ls[idx]
    def set_max_match(begin, end, max_match):
        ls, idx = get_max_match_ls_idx(begin, end)
        ls[idx] = max_match # (max_match_num, split_idx)
    
    for step in range(3, m+1):
        for begin in range(m-step+1):
            end = begin + step
            #_pr(begin=begin, end=end)
            a,b = ils[begin : end : step-1]
            max_match_num  = 0 if not is_match(a,b) else 1+get_max_match(begin+1, end-1)[0]
            split_idx = None
            for mid in range(begin+1, end):
                n1, _ = get_max_match(begin, mid)
                n2, _ = get_max_match(mid, end)
                if n1 + n2 > max_match_num:
                    max_match_num = n1+n2
                    split_idx = mid
            set_max_match(begin, end, (max_match_num, split_idx))

    #_pr(max_match_table=max_match_table)
    match_map = [None]*m
    stack = [(0, m)]
    while stack:
        begin, end = stack.pop()
        if end - begin < 2:
            continue
        #_pr(begin=begin, end=end)
        _, mid = get_max_match(begin, end)
        if mid == None:
            a,b = ils[begin], ils[end-1]
            if is_match(a,b):
                assert match_map[begin] == match_map[end-1] == None
                match_map[begin] = end-1
                match_map[end-1] = begin
                begin += 1
                end -= 1
                stack.append((begin, end))
        else:
            stack.append((begin, mid))
            stack.append((mid, end))

    return match_map


def _test_max_tag_match_dynamic():
    data = [\
        ([1], [None]),\
        ([-1], [None]),\
        ([-1, 1], [None, None]),\
        ([1, 2, -1, -2], [None, 3, None, 1]),\
        ([1, -1, 2, -2], [1, 0, 3, 2]),\
        ([1, 2, -2, -1], [3, 2, 1, 0]),\
        ([-2, 2, 1, -1], [None, None, 3, 2]),\
        ([-2, 1, 2, -1], [None, 3, None, 1]),\
        ([2, -1, -2, 1], [2, None, 0, None]),\
        ]

    for ls, ans in data:
        assert ans == _max_tag_match_dynamic(ls)


    data = [\
        ([(True, 'tag'), (False, 'tag')], [1,0]),\
        ]
    get_tag_info = lambda x:x
    for ls, ans in data:
        assert ans == _max_tag_match_dynamic(ls, get_tag_info)


def _test_max_tag_match_split_under_some_assumption():
    data = [\
        (1, [1], [None]),\
        (1, [-1], [None]),\
        (1, [-1, 1], [None, None]),\
        #(2, [1, 2, -1, -2], [None, 3, None, 1]),\
        (2, [1, -1, 2, -2], [1, 0, 3, 2]),\
        (2, [1, 2, -2, -1], [3, 2, 1, 0]),\
        (2, [-2, 2, 1, -1], [None, None, 3, 2]),\
        (2, [-2, 1, 2, -1], [None, 3, None, 1]),\
        (2, [2, -1, -2, 1], [2, None, 0, None]),\
        ]

    for n, ls, ans in data:
        assert ans == _max_tag_match_split_under_some_assumption(n, ls)

if __name__ == "__main__":
    _test_max_tag_match_dynamic()
    _test_max_tag_match_split_under_some_assumption()
    ls = max_tag_match(10, [10, 9, 8, -7, -8, -9, 7, 5, 3, -3, 6, -5, 6, -6, -10])


    
