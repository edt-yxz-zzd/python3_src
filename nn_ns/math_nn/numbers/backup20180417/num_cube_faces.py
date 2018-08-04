
'''

@The Math Book::Tesseract 1888::page282
these kinds of higher-dimensional objects: 
-----           Comers  Edges   Faces   Solids  HypervoJumes 
Point           1       0       0       0       0
Line segment    2       1       0       0       0 
Square          4       4       1       0       0 
Cube            8       12      6       1       0 
Hypercube       16      32      24      8       1 
Hyperhypercube  32      80      80      40      10


num_faces(dim_solid, dim_face) = num_faces(dim_solid-1, dim_face)*2 + num_faces(dim_solid-1, dim_face-1)
num_faces(n,n-0) = 1
num_faces(n,n-1) = sum 2*1 {i=0..k} = 2(k+1) = 2*C(k+1,1)
num_faces(n,n-2) = sum 2*2(i+1) {i=0..k} = 2*(k+1)(k+2) = 4*C(k+2,2) = 4*sum C(i+1, 1) {i<=k}
num_faces(n,n-3) = sum 2*2(i+1)(i+2) {i=0..k} = 8*sum C(i+2,2) {i<=k} = 8*C(k+3,3)
num_faces(n,n-x) = 2**x *C((n-x)+x,x) = 2**x *C(n,x)
num_faces(n,k) = 2**x *C((n-x)+x,x) = 2**(n-k) *C(n,n-k)


'''

from .choose import C
from .Pascal_number_like import PascalNumberLike

_data = [[1], [2, 1], [4, 4, 1], [8, 12, 6, 1],
         [16, 32, 24, 8, 1], [32, 80, 80, 40, 10, 1]]

def calc_num_cube_faces(dim_solid, dim_face):
    d = dim_solid - dim_face
    if dim_solid < 0 or d < 0 or dim_face < 0:
        return 0
    return 2**d * C(dim_solid, d)

class NumCubeFaces(PascalNumberLike):
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 + n1_k*2
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        return 0
        raise NotImplementedError()
    def _calc_pos_beyond(self, n, k, table):
        return 0
        raise NotImplementedError()
    def direct_calc(self, n, k):
        return calc_num_cube_faces(n,k)
        raise NotImplementedError()

num_cube_faces = NumCubeFaces()

#print(num_cube_faces.get_first(6))
assert num_cube_faces.get_first(len(_data)) == _data
assert num_cube_faces(9, 3) == calc_num_cube_faces(9,3)












