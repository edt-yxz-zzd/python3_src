

'''
row_idx in [0..num_rows-1]
generalize:
    row_idx in row_domain
but:
    key vs idx / dict vs seq
    sub_matrix: key stable, idx changes
'''


from .IRingOps import IRingOps
from .IDomain import IFiniteDomain, ICompositeFiniteDomain
from enum import Enum
from abc import ABCMeta, abstractmethod
from itertools import islice, starmap, repeat
from seed.iters.null_iter import null_iter












class IFiniteKeyDomainMappingOps(metaclass=ABCMeta):
    @abstractmethod
    def is_mapping(self, m):pass
    @abstractmethod
    # assert isinstance(get_key_domain(m), IFiniteDomain)
    def get_key_domain(self, m):pass
    @abstractmethod
    def get_mapping_value_at(self, m, key):pass

    @abstractmethod
    # key_values2new_value :: key -> old_value... -> new_value
    def map1(self, key_values2new_value, mx, *matrices):pass

    def get_mapping_size(self, m):
        key_domain = self.get_key_domain(m)
        return len(key_domain)
    def to_dict(self, m):
        key_domain = self.get_key_domain(m)
        it = iter(key_domain)
        get = self.get_mapping_value_at
        d = {key:get(m, key) for key in it}
        return d
class IFiniteKeyDomainMappingOps__make(IFiniteCompositeKeyDomainMappingOps):
    @abstractmethod
    # assert isinstance(get_key_domain_domain(), IDomain)
    def get_key_domain_domain(self):pass
    @abstractmethod
    # assert get_key_domain_domain().is_element(get_key_domain(m))
    # assert isinstance(get_key_domain(m), IFiniteDomain)
    def get_key_domain(self, m):pass

    @abstractmethod
    # how to construct key_domain s.t. acceptable??
    def __domain_key2value_to_mapping__(self, key_domain, key2value):pass
    def domain_key2value_to_mapping(self, key_domain, key2value):
        assert self.get_key_domain_domain().is_element(key_domain)
        return self.__domain_key2value_to_mapping__(key_domain, key2value)
    def map1(self, key_values2new_value, mx, *matrices):
        # key_values2new_value :: key -> old_value... -> new_value
        get_key_domain = self.get_key_domain
        key_domain = get_key_domain(mx)
        if not all(key_domain == get_key_domain(mx) for mx in matrices): raise TypeError
        get = self.get_mapping_value_at
        def key2value(key):
            new_value = key_values2new_value(key
                        , get(mx, key), *(get(mx, key) for mx in matrices))
            return new_value
        return self.domain_key2element_to_mapping(key_domain, key2value)



class ICompositeFiniteKeyDomainMappingOps(IFiniteKeyDomainMappingOps):
    # the key domain decomposited to sides (e.g. row/column)
    @abstractmethod
    # assert isinstance(get_key_domain(m), ICompositeFiniteDomain)
    def get_key_domain(self, m):pass
    def get_composite_size(self, m):
        # return a tuple of UInt
        key_domain = self.get_key_domain(m)
        assert isinstance(key_domain, ICompositeFiniteDomain)
        return tuple(map(len, key_domain.domains))

class ICompositeFiniteKeyDomainMappingOps__extract(ICompositeFiniteKeyDomainMappingOps):
    @abstractmethod
    def extract_facet(self, mx, subdomain_idx2subkey):pass
    @abstractmethod
    def extract_facet_ops(self, subdomain_idc):pass
class IFiniteKeyDomainMappingOps__ring_value(IFiniteKeyDomainMappingOps):
    @abstractmethod
    def get_mapping_value_ring_ops(self):pass
class ICompositeFiniteKeyDomainMappingOps__ring_value(
    IFiniteKeyDomainMappingOps__ring_value
    , ICompositeFiniteKeyDomainMappingOps):pass
class IFiniteKeyDomainVectorOps(IFiniteKeyDomainMappingOps__ring_value):
    # vector is not matrix!!
    #   1) there are no column(or row) domain
    #   2) should be row or column??
    # matrix is not vector; vector of what??
    #   1) a vector of (rc -> element)
    #   2) a vector of (row_key -> row)
    #   3) a vector of (column_key -> column)
    pass



class IFiniteKeyDomainMatrixOps(ICompositeFiniteKeyDomainMappingOps__ring_value, ICompositeFiniteKeyDomainMappingOps__extract):
    # allow matrix size: (0 by C) and (R by 0)
    # fixed to single element ops
    # infinite??? how to mul??
    # matrix mul ==>> require: row key domain ops == column key domain ops
    # row_key_domain, column_key_domain :: SideKeyDomain
    # rc_key_domain = (row_key_domain, column_key_domain)
    # row_key in row_key_domain
    # column_key in column_key_domain
    # rc_pair = (row_key, column_key)
    #
    # num_rows, num_columns :: UInt
    # size = (num_rows, num_columns)
    #
    # if (r,L), (L,c) in KeyDomain then (r,c) in KeyDomain
    # if (r,c) in KeyDomain then (c,r) in KeyDomain

    @abstractmethod
    # composite of 2 key domain
    def get_key_domain(self, mx):pass



    def get_vector_ops(self):
        return self.extract_facet_ops([0]) # == extract_facet_ops([1])
    def get_rc_key_domain(self, mx):
        key_domain = self.get_key_domain(mx)
        row_key_domain, column_key_domain = key_domain.domains
        return row_key_domain, column_key_domain

    # (num_rows, num_columns)
    def get_matrix_size(self, mx):
        num_rows, num_columns = self.get_composite_size()
        return num_rows, num_columns
    def extract_row(self, mx, row_key):
        return self.extract_facet(mx, {0:row_key})
    def extract_column(self, mx, column_key):
        return self.extract_facet(mx, {1:column_key})


    #neg/add/sub/mul/transpose
    def neg(self, x):
        ops = self.get_mapping_value_ring_ops()
        f = ops.neg
        return self.map1(f, x)
    def sum1(self, mx, matrices):
        ops = self.get_mapping_value_ring_ops()
        f = ops.sum1
        return self.map1(f, mx, *matrices)
    def sub(self, x, y):
        ops = self.get_mapping_value_ring_ops()
        f = ops.sub
        return self.map1(f, x, y)
    def product1(self, mx, matrices):
        size_of = self.get_matrix_size
        num_rows, num_mids = size_of(x)
        _num_mids, num_columns = size_of(y)
        if num_mids != _num_mids: raise TypeError
        size = num_rows, num_columns
        if min(num_rows, num_mids, num_columns) == 0:
            return self.zero(size)

        extract_row = self.extract_row
        extract_column = self.extract_column
        ops = self.get_mapping_value_ring_ops()
        vmul = ops.vector_mul
        sum = ops.sum
        def dot_product(v,u):
            return sum(vmul(v, u))
        def rc_pair_to_element(rc):
            row_idx, column_idx = rc
            row = extract_row(x, row_idx)
            column = extract_column(y, column_idx)
            return dot_product(row, column)
        return self.make_matrix_from_rc_pair2element(size, rc_pair_to_element)


dimension
class IMatrixChainOrderingProblem(ABC):
    '''matrix_chain_ordering_problem :: [UInt] -> {(UInt, UInt):(UInt, UInt)}

matrix_chain_ordering_problem(side_length_seq) -> arc2cost_middle_pair
arc :: (UInt, UInt)
arc = (side_length_begin_idx, side_length_end_idx)
cost_middle_pair = (cost, side_length_middle_idx) :: (UInt, UInt)

side_length_begin_idx+2 <= side_length_end_idx
let N = num_matrices
    L = len(side_length_seq)
    R = L-2
N >= 2
L == N+1 >= 3
len(arc2cost_middle_pair) == R == L-2 >= 1
arc2cost_middle_pair[(0, L-1)] = min_total_cost
def inside(arc_in, arc_out): # polygon
    begin_in, end_in = arc_in
    begin_out, end_out = arc_out
    return begin_out <= begin_in <= end_in <= end_out
def before(arcL, arcR): # eval order, left to right, inside to outside
    beginL, endL = arcL
    beginR, endR = arcR
    return endL <= beginR or inside(arcL, arcR)
def cross(arcL, arcR):
    def crossLR(arcL, arcR):
        beginL, endL = arcL
        beginR, endR = arcR
        return beginL <= beginR < endL <= endR
    return crossLR(arcL, arcR) or crossLR(arcR, arcL)
d = arc2cost_middle_pair
for arcL, arcR in product(d, d):
    costL, middleL = arc2cost_middle_pair[arcL]
    costR, middleR = arc2cost_middle_pair[arcR]
    if arcL != arcR:
        assert not cross(arcL, arcR)
        assert before(arcL, arcR) or before(arcR, arcL)
def cost_f(begin, middle, end):
    assert begin < middle < end
    s = side_length_seq
    return s[begin]*s[middle]*s[end]
def search_cost(side_or_arc):
    s = side_length_seq
    begin, end = side_or_arc
    assert begin+1 <= end
    if begin+1 == end:
        return (0, None)
    arc = side_or_arc
    return d[arc]
for (begin, end), (cost, middle) in arc2cost_middle_pair.items():
    assert 0 <= begin < middle < end <= L
    left_cost,_ = search_cost((begin,j))
    middle_cost = cost_f(begin, j, end)
    right_cost,_ = search_cost((j,end))
    assert cost == left_cost + middle_cost + right_cost
    '''
    @abstractmethod
    def __matrix_chain_ordering_problem__(self, side_length_seq):pass
    def matrix_chain_ordering_problem(self, side_length_seq):
        L = len(side_length_seq)
        assert L >= 3
        assert all(length >= 0 for length in side_length_seq)
        ordered_cost_arc_pairs = self.__matrix_chain_ordering_problem__(side_length_seq)
        assert len(ordered_cost_arc_pairs) == L-2
        return ordered_cost_arc_pairs


class MatrixChainOrderingProblem__dymanic(IMatrixChainOrderingProblem):
    def __matrix_chain_ordering_problem__(self, side_length_seq):
        s = side_length_seq
        def cost_f(begin, middle, end):
            assert begin < middle < end
            return s[begin]*s[middle]*s[end]

        d = {} # arc2cost_middle_pair
        def search_cost(side_or_arc):
            begin, end = side_or_arc
            assert begin < end
            if begin + 1 == end:
                # side
                return (0, None)
            # arc
            arc = side_or_arc
            may_cost_middle_pair = d.get(arc)
            if may_cost_middle_pair is not None:
                cost_middle_pair = may_cost_middle_pair
                return cost_middle_pair

            min_cost = float('inf')
            middle = None
            for j in range(begin+1, end):
                left_cost,_ = search_cost((begin,j))
                middle_cost = cost_f(begin, j, end)
                right_cost,_ = search_cost((j,end))
                cost = left_cost + middle_cost + right_cost
                if cost < min_cost:
                    min_cost = cost
                    middle = j
            r = d[arc] = (min_cost, middle)
            return r

        arc = (0, L-1)
        search_cost(arc)
        arcs = [arc]
        result = {}
        while arcs:
            begin, end = arc = arcs.pop()
            if begin+1 == end: continue
            cost, middle = cost_middle_pair = d[arc]
            result[arc] = cost_middle_pair
            arcs.append((begin, middle))
            arcs.append((middle, end))
        return result



def min_matrix_product(side_length_seq):
    # a*b*c
    # size_of a,b,c === (A,B),(B,C),(C,D)
    # side_length_seq == [A, B, C, D]
    # count[a*b] == A*C*(B mul + (B-1) add) == O(A*B*C)
    # count[(a*b)*c] = ABC + ACD
    # count[a*(b*c)] = ABD + BCD
    # (A<=D)(C<=B) ==>> ABC+ACD <= ABD+BCD
    # (A<=B)(C<=D) ==>> ABC+ACD <= ABD+BCD
    # side_length_seq = [A, B, B, B, C], A<=C<=B
    # count[(abb)c] = 2ABB + ABC = the min
    # count[a(bb)c] = BBB + ABB + ABC >= ABB + ABB + ABC = count[(abb)c]
    # count[a(bbc)] = ABC + 2BBC >= ABC + 2ABB = count[(abb)c]

















##############
class MatrixImplCase(Enum):
    # matrix = (num_rows, num_columns, data)
    # num_rows >= 0
    # num_columns >= 0
    Rows            # data = rows = [row]
    Columns         # data = columns = [column]
    RowFirst        # data = elements = [element]
                        # if num_rows: data[:num_columns] = rows[0]
    ColumnFirst     # data = elements = [element]
                        # if num_columns: data[:num_rows] = columns[0]

def is_null_matrix_size(size)
    num_rows, num_columns = size
    return not num_rows or not num_columns
def rc_key_domain2iter_rc_pairs(is_row_first, key_domain_ops, rc_key_domain):
    (row_key_domain, column_key_domain) = rc_key_domain
    iter_f = key_domain_ops.iter_elements
    if is_row_first:
        return ((row_key, column_key)
                for row_key in iter_f(row_key_domain)
                for column_key in iter_f(column_key_domain)
            )
    else:
        return ((row_key, column_key)
                for column_key in iter_f(column_key_domain)
                for row_key in iter_f(row_key_domain)
            )



def rc_key_domain2iter_rc_pairs__column_first(key_domain_ops, rc_key_domain):


###################

    def extract_submatrix(self, mx, new_rc_key_domain
        , new2old_row_key, new2old_column_key):
        # why?
        #   to wrap around unstable "idx"
        #   mx[4:6, 3:6]: (4,5)*(3,4,5) ==>> (0,1)*(0,1,2)
        def new2old_rc(new_rc):
            new_row_key, new_column_key = new_rc
            old_row_key = new2old_row_key(new_row_key)
            old_column_key = new2old_column_key(new_column_key)
            return (old_row_key, old_column_key)
        return self.extract_matrix(mx, new_rc_key_domain, new2old_rc)
    def extract_matrix(self, mx, new_rc_key_domain, new2old_rc):
        # new2old_rc :: new_rc_pair -> old_rc_pair
        get = self.get_mapping_value_at
        def rc_pair_to_element(new_rc):
            old_rc = new2old_rc(new_rc)
            return get(mx, old_rc)
        return self.make_matrix_from_rc_pair2element(new_rc_key_domain, rc_pair_to_element)
        new_row_key_domain, new_column_key_domain = new_rc_key_domain
        ops = self.get_key_domain_ops()
        iter_f = ops.iter_elements
        row_keys = iter_f(new_row_key_domain)
        column_keys = iter_f(new_column_key_domain)
    def extract_row(self, mx, row_key):
        row_key_domain, column_key_domain = self.get_rc_key_domain(mx)
        ops = self.get_key_domain_ops()
        make_vector = self.get_vector_ops().make_vector_from_key2element
        get = self.get_mapping_value_at
        def key2element(column_key):
            return get(mx, row_key, column_key)
        return make_vector(column_key_domain, key2element)
    def extract_column(self, mx, column_key):
        row_key_domain, column_key_domain = self.get_rc_key_domain(mx)
        ops = self.get_key_domain_ops()
        make_vector = self.get_vector_ops().make_vector_from_key2element
        get = self.get_mapping_value_at
        def key2element(row_key):
            return get(mx, row_key, column_key)
        return make_vector(row_key_domain, key2element)



    def to_dict(self, mx):
        rc_key_domain = self.get_rc_key_domain(mx)
        rc_pairs = self.iter_rc_pairs(None, rc_key_domain)
        get = self.get_mapping_value_at
        d = {rc:get(mx, rc) for rc in rc_pairs}
        return d
    def iter_rc_pairs(self, is_row_first, rc_key_domain):
        ops = self.get_key_domain_ops()
        rc_pairs = rc_key_domain2iter_rc_pairs(is_row_first, ops, rc_key_domain)
        return rc_pairs
        

domain_ops.iter_elements/get_size

def iter_rc_pairs__row_first(size):
    num_rows, num_columns = size
    if not num_rows or not num_columns: return null_iter
    rc_pairs = ((row_idx, column_idx)
            for row_idx in range(num_rows)
            for column_idx in range(num_columns)
        )
    return rc_pairs
def iter_rc_pairs__column_first(size):
    num_rows, num_columns = size
    if not num_rows or not num_columns: return null_iter
    rc_pairs = ((row_idx, column_idx)
            for column_idx in range(num_columns)
            for row_idx in range(num_rows)
        )
    return rc_pairs
def iterable2columns(size, iterable):
    num_rows, num_columns = size
    columns = iterable2rows((num_columns, num_rows), iterable)
    return columns
def iterable2rows(size, iterable):
    num_rows, num_columns = size
    assert num_rows >= 0
    assert num_columns >= 0
    it = iter(iterable)
    rows = []
    for row_idx in range(num_rows+1):
        row = tuple(islice(it, num_columns))
        rows.append(row)
    if rows[-1]: raise ValueError('too many elements')
    rows.pop()
    assert len(rows) == num_rows
    if rows and len(rows[-1]) != num_columns: raise ValueError('too few elements')
    assert all(len(row) == num_columns for row in rows)
    return rows


class IFiniteIndexDomainMatrixOps(IFiniteKeyDomainMatrixOps):
    # row_idx, column_idx :: UInt
    # rc_pair = (row_idx, column_idx)
    # diagonal_idx :: Int
    # diagonal_idx = row_idx - column_idx
    @abstractmethod
    def extract_row(self, mx, row_idx):pass
    @abstractmethod
    def extract_column(self, mx, column_idx):pass

    @abstractmethod
    def __rows2matrix__(self, size, rows):pass
    @abstractmethod
    def __columns2matrix__(self, size, columns):pass
    @abstractmethod
    def is_X_row(self):pass
    @abstractmethod
    def iter_row_first(self, mx):pass
    @abstractmethod
    def iter_column_first(self, mx):pass
    @abstractmethod
    def iter_rows(self, mx):pass
    @abstractmethod
    def iter_columns(self, mx):pass



    def get_num_rows(self, mx):
        num_rows, num_columns = self.get_matrix_size(mx)
        return num_rows
    def get_num_columns(self, mx):
        num_rows, num_columns = self.get_matrix_size(mx)
        return num_columns
    def get_num_elements(self, mx):
        num_rows, num_columns = self.get_matrix_size(mx)
        return num_rows * num_columns
    def rows2matrix(self, size, rows):
        return self.__rows2matrix__(size, rows)
    def columns2matrix(self, size, columns):
        return self.__columns2matrix__(size, columns)
    def row_first2matrix(self, size, iterable):
        rows = iterable2rows(size, iterable)
        return self.rows2matrix(size, rows)
    def colunm_first2matrix(self, size, iterable):
        columns = iterable2columns(size, iterable)
        return self.columns2matrix(size, columns)
    @property
    def iter_X_first(self):
        if self.is_X_row():
            return self.iter_row_first
        return self.iter_column_first
    def X_first2matrix(self, size, iterable):
        f = self.row_first2matrix if self.is_X_row() else self.colunm_first2matrix
        return f(size, iterable)
    def iter_pointwise_map(self, f, *matrices, is_row_first=None):
        # is_row_first = None | True | False
        if not matrices: return null_iter
        mx = matrices[0]
        size_of = self.get_matrix_size
        size = size_of(mx)
        if not all(size_of(mx) == size for mx in matrices[1:]): raise TypeError
        if is_row_first is None:
            is_row_first = self.is_X_row()
        if is_row_first:
            elements_of = self.iter_row_first
        else:
            elements_of = self.iter_column_first
        elements = starmap(f, zip(*map(elements_of, matrices)))
        return elements
    def pointwise(self, f, mx, *matrices):
        # f(*elements) -> element
        size_of = self.get_matrix_size
        size = size_of(mx)
        elements = self.iter_pointwise_map(f, mx, *matrices)
        mx = self.X_first2matrix(size, elements)
        return mx
    def transpose(self, mx, map_f=None):
        num_rows, num_columns = size_of(mx)
        if self.is_X_row():
            # reverse
            elements_of = self.iter_column_first
        else:
            elements_of = self.iter_row_first
        if map_f is None:
            f = elements_of
        else:
            def f(mx):
                return map(map_f, elements_of(mx))
        mx = self.X_first2matrix((num_columns, num_rows), f(mx))
        return mx

    def make_matrix_of_same_elements(self, size, element):
        num_rows, num_columns = size
        num_elements = num_rows * num_columns
        ops = self.get_mapping_value_ring_ops()
        assert ops.is_element(element)
        elements = repeat(element, num_elements)
        return self.X_first2matrix(size, elements)
    def zero(self, size):
        ops = self.get_mapping_value_ring_ops()
        z = ops.zero
        return self.make_matrix_of_same_elements(size, z)
    def diagonal_square(self, iterable):
        ls = list(iterable)
        L = len(ls)
        return self.diagonal((L,L), ls)
    def diagonal_square_of_same_elements(self, length, element):
        return self.diagonal_of_same_elements((length, length), element)
    def diagonal_of_same_elements(self, size, element):
        L = min(size)
        ls = [element]*L
        return self.diagonal(size, ls)
    def diagonal(self, size, iterable):
        ops = self.get_mapping_value_ring_ops()
        z = ops.zero
        fz = lambda diagonal_idx: z
        return self.gdiagonal(size, {0:list(iterable)}, fz)
    def gdiagonal(self, size
        , diagonal_idx2element_seq, diagonal_idx2pad_element):
        # diagonal_idx = row_idx - column_idx
        # diagonal_idx2element_seq :: Map Int [Elem]
        # diagonal_idx2pad_element :: Int -> Elem
        num_rows, num_columns = size
        def diagonal_idx2length(diagonal_idx):
            if diagonal_idx >= 0:
                L = min(num_rows - diagonal_idx, num_columns)
            else:
                L = min(num_rows, num_columns + diagonal_idx)
            return max(L, 0)
        if not all(diagonal_idx2length(diagonal_idx) == len(seq) for diagonal_idx, seq in diagonal_idx2element_seq.items()): raise TypeError
        def _diagonal_idx2pad_element(diagonal_idx):
            if diagonal_idx in diagonal_idx2element_seq:
                raise logic-error
            return diagonal_idx2pad_element(diagonal_idx)
        return self.gdiagonal_relaxed(size
            , diagonal_idx2element_seq, _diagonal_idx2pad_element)
    def gdiagonal_relaxed(self, size
        , diagonal_idx2element_seq, diagonal_idx2pad_element):
        # diagonal_idx = row_idx - column_idx
        # diagonal_idx2element_seq :: Map Int [Elem]
        # diagonal_idx2pad_element :: Int -> Elem
        def rc_pair_to_element(rc):
            row_idx, column_idx = rc
            diagonal_idx = row_idx - column_idx
            may_seq = diagonal_idx2element_seq.get(diagonal_idx)
            if may_seq is None:
                return diagonal_idx2pad_element(diagonal_idx)
            seq = may_seq
            idx = column_idx if diagonal_idx >= 0 else row_idx
            if idx >= len(seq):
                return diagonal_idx2pad_element(diagonal_idx)
            return seq[idx]
        return self.make_matrix_from_rc_pair2element(size, rc_pair_to_element)

    def make_matrix_from_rc_pair2element(self, size, rc_pair_to_element):
        # rc_pair_to_element :: (UInt, UInt) -> Elem
        # rc_pair = (row_idx, column_idx)
        if self.is_X_row():
            iter_f = iter_rc_pairs__row_first
        else:
            iter_f = iter_rc_pairs__column_first
        rc_pairs = iter_f(size)
        it = map(rc_pair_to_element, rc_pairs)
        return self.X_first2matrix(size, it)

    def expand_relaxed(self, size, mx):
        if is_null_matrix_size(size):
            return self.X_first2matrix(size, null_iter)
        num_rows, num_columns = self.get_matrix_size(mx)
        get = self.get_mapping_value_at
        def rc_pair_to_element(rc):
            row_idx, column_idx = rc
            row_idx %= num_rows
            column_idx %= num_columns
            return get(mx, rc)
        return self.make_matrix_from_rc_pair2element(size, rc_pair_to_element)
    def expand__repeat(self, mx, row_times, column_times):
        num_rows, num_columns = self.get_matrix_size(mx)
        num_rows *= row_times
        num_columns *= column_times
        size = (num_rows, num_columns)
        return self.expand_relaxed(size, mx)



    def element_equal(self, x, y):
        if not self.is_element(x): raise TypeError
        if not self.is_element(y): raise TypeError
        ops = self.get_mapping_value_ring_ops()
        eq = ops.element_equal
        iter_f = self.iter_X_first
        return all(map(eq, iter_f(x), iter_f(y)))
    def neg(self, x):
        ops = self.get_mapping_value_ring_ops()
        f = ops.neg
        return self.pointwise(f, x)
    def add(self, x, y):
        ops = self.get_mapping_value_ring_ops()
        f = ops.add
        return self.pointwise(f, x, y)
    def sub(self, x, y):
        ops = self.get_mapping_value_ring_ops()
        f = ops.sub
        return self.pointwise(f, x, y)
    def mul(self, x, y):
        size_of = self.get_matrix_size
        num_rows, num_mids = size_of(x)
        _num_mids, num_columns = size_of(y)
        if num_mids != _num_mids: raise TypeError
        size = num_rows, num_columns
        if min(num_rows, num_mids, num_columns) == 0:
            return self.zero(size)

        extract_row = self.extract_row
        extract_column = self.extract_column
        ops = self.get_mapping_value_ring_ops()
        vmul = ops.vector_mul
        sum = ops.sum
        def dot_product(v,u):
            return sum(vmul(v, u))
        def rc_pair_to_element(rc):
            row_idx, column_idx = rc
            row = extract_row(x, row_idx)
            column = extract_column(y, column_idx)
            return dot_product(row, column)
        return self.make_matrix_from_rc_pair2element(size, rc_pair_to_element)





    # TODO
class IGMatrixOps(IMatrixOps):
    # for any element ops
    @classmethod
    @abstractmethod
    def ops_rows2matrix(cls, element_ops, size, rows):pass
    @classmethod
    @abstractmethod
    def ops_columns2matrix(cls, element_ops, size, columns):pass

    def __rows2matrix__(self, size, rows):
        return type(self).ops_rows2matrix(self.get_mapping_value_ring_ops()
            , size, rows)
    def __columns2matrix__(self, size, columns):
        return type(self).ops_columns2matrix(self.get_mapping_value_ring_ops()
            , size, columns)

