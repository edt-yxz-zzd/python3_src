
'''
given a matrix_t and matrix_api_t, we can treat matrix_t as a matrix under operations given by matrix_api_t

'''

class matrix_t:pass
class matrix_api_t:
    def add(mxlhs, mxrhs):pass
    def sub(mxlhs, mxrhs):pass
    def mul(mxlhs, mxrhs):pass
    def scale(x, mx):pass  # x in ring
    def times(i, mx):pass  # i in N
    def power(mx,n):pass
    def transpose(mx):pass
    def inv(mx_nn):pass
    def Kronecker_product(mxlhs_ab, mxrhs_cd):pass # size(mx_ab) = (a,b)
    def size(mx):pass
    def sizer(mx):pass
    def sizec(mx):pass
    def get_submx(mx, left, top, right, buttom):pass
    def get_row(mx, nr):pass
    def get_column(mx, nc):pass
    def get(mx, nr, nc):pass
    ##############
    def get_ring_api():pass # work on mx elements
    ##############
    def build_mx(r,c,a):pass # size(mx) = (r,c), and get(mx,i,j) = a
    def identity_mx(r, c):pass # matrix with get(mx, nr, nc) = (nr==nc)
    def diagonal_mx(mx_n1):pass
    def resize(mx,r,c):pass # sizer(mx)*sizec(mx) == r*c
    def Vandermonde_mx(mx_n1):pass
    def symmetric_Vandermonde_matrix(n,a):pass

class ring_t: pass
class ring_api_t:
    def add(lhs, rhs):pass
    def sub(lhs, rhs):pass
    def neg(a):pass
    def mul(lhs, rhs):pass
    def times(i, a):pass
    def zero():pass

class ring_with_one_api_t(ring_api_t):
    def one():pass
    def inv():pass # if possible
    def root_of_unity(k):pass # return (rt,n), any x^m=unity, multiplicity(n,k) >= multiplicity(m,k)



class ring_with_one_api_impl_by_string(ring_with_one_api_t):
    '''
    generators are all lists contains one string.
    r = sum a[i]*II p[i]^e[i] -> map{[(p,e)]:n mod m(!=0)}
    0 = empty map
    1 = {[]:1}
    add = add values with same key
    mul = new key = lkey+rkey, new value = lvalue*rvalue
    '''








