

'''

example:
    # rooted_tree_to_depth2vertices
    # rooted_tree_to_binary_string
    >>> t = RootedTree__ContainerAsNode([[], [(), {}]]);
    >>> rooted_tree_to_depth2vertices(t)
    [([[], [(), {}]],), ([], [(), {}]), ((), {})]
    >>> rooted_tree_to_binary_string(t)
    '1101101000'

    >>> t = RootedTree__UIntAsVertex([3,2,3, 6,6,6, 7]);
    >>> rooted_tree_to_depth2vertices(t)
    [(7,), (6,), (3, 4, 5), (0, 2), (1,)]
    >>> rooted_tree_to_binary_string(t)
    '1111011000101000'

    # rooted_tree_canonization__leveled_DAG
    >>> C = rooted_tree_canonization__leveled_DAG;
    >>> leveled_DAG, new2olds = C.canonization_ex(t);
    >>> leveled_DAG
    [[[0]], [[0, 0, 1]], [[], [0, 1]], [[], [0]], [[]]]
    >>> new2olds
    [[[7]], [[6]], [[4, 5], [3]], [[0], [2]], [[1]]]

    >>> ct = RootedTree__leveled_DAG_as_Tree(leveled_DAG);
    >>> rooted_tree_to_depth2vertices(ct)
    [((0, 0),), ((1, 0),), ((2, 0), (2, 0), (2, 1)), ((3, 0), (3, 1)), ((4, 0),)]
    >>> rooted_tree_to_binary_string(ct) # canonization binary
    '1110101101100000'
    >>> C.to_canonization_binary_string(t) == _
    True

    >>> vtx2color = [1,1,0, 1,2,0, 0,0]
    >>> leveled_DAG, new2olds = C.colored_canonization_ex(t, 3, vtx2color);
    >>> leveled_DAG
    [[[0]], [[0, 1, 2]], [[], [0, 1], []], [[0], []], [[]]]
    >>> new2olds
    [[[7]], [[6]], [[5], [3], [4]], [[2], [0]], [[1]]]

    >>> leveled_DAG2, new2olds2 = C.weighted_colored_canonization_ex(t, 3, vtx2color, 3, [1,2,0,2,1,2,0,2]);
    >>> leveled_DAG == leveled_DAG2
    True
    >>> new2olds == new2olds2
    True
'''



__all__ = '''
    rooted_tree_canonization__leveled_DAG
    rooted_tree_to_binary_string
    rooted_tree_to_depth2vertices

    RootedTree__leveled_DAG_as_Tree
    RootedTree__ContainerAsNode
    RootedTree__UIntAsVertex

    IRootedTree
    IRootedTree__parent
    RootedTreeCanonizationRequires

GraphError
NotVertexError
IGraphBase
    IVerticesAreUInt
        IBoundedVertex
    ITreeBase
        IRootedTree
            IRootedTreeWrapper

            RootedTree__leveled_DAG_as_Tree
            RootedTree__ContainerAsNode
            rooted_tree_to_binary_string
            rooted_tree_to_depth2vertices

            IRootedTree__parent
                IRootedTree__parent_Wrapper

                RootedTreeCanonizationRequires
                    RootedTree__UIntAsVertex
                    RootedTreeCanonization__leveled_DAG
                        rooted_tree_canonization__leveled_DAG
    '''.split()


from itertools import chain
from io import StringIO
from abc import ABCMeta, abstractmethod, ABC

from ..bucket_sort.echo import fst
from ..bucket_sort.GroupBy import GroupBy
from ..bucket_sort.UIntSeqSort import UIntSeqSort
from ..bucket_sort.inplace_bucket_sort import inplace_bucket_sort
from ..bucket_sort.reiterable import is_seq
from ..bucket_sort.BucketSortableSort import (
    IBucketSortableTV
    , KnownTVs
    , BucketSortableSort
    , BoundedUIntTV
    , TplTV
    , SwitchTV
    , maybeTV
    , Just
    , Nothing
    )


class GraphError(Exception):pass
class NotVertexError(GraphError):pass
class IGraphBase(ABC):...
class ITreeBase(IGraphBase):...

#class IRootedUnorientatedTree
class IRootedTree(ITreeBase):
    # why no parent()?
    #   we may treat a DAG as compact tree representation
    #   so, an node may have more than 1 parent
    # why no vertex_eq()?
    #   we may use container as node, which require 'is'
    #   we may use uint as node, which require '=='
    #   sometimes the node may not define '==' yet.
    @abstractmethod
    def root(self):...
    @abstractmethod
    def unstable_iter_children(self, v):...
    def is_leaf(self, v):
        for _ in self.unstable_iter_children(v):
            return False
        return True
    def unstable_iter_vertices(self):
        root = self.root()
        iters = [iter([root])]
        iter_children = self.unstable_iter_children
        while iters:
            for v in iters[-1]:
                yield v
                iters.append(iter_children(v))
                break
            else:
                iters.pop()
        pass

class IRootedTreeWrapper(IRootedTree):
    @abstractmethod
    def get_underlying_tree(self):...
    def root(self):
        return self.get_underlying_tree().root()
    def unstable_iter_children(self, v):
        return self.get_underlying_tree().unstable_iter_children(v)
    def is_leaf(self, v):
        return self.get_underlying_tree().is_leaf(v)
    def unstable_iter_vertices(self):
        return self.get_underlying_tree().unstable_iter_vertices()




class RootedTree__leveled_DAG_as_Tree(IRootedTree):
    def __init__(self, leveled_DAG):
        # leveled_DAG :: [[[uint]]] # see below depth2idx2seq
        self.__DAG = leveled_DAG
        assert leveled_DAG
        assert len(leveled_DAG[0]) == 1
    def root(self):
        return (0, 0) # (depth, idx)
    def unstable_iter_children(self, v):
        depth, idx = v
        seq = self.__DAG[depth][idx]
        d = depth+1
        return ((d, idx) for idx in seq)
    def is_leaf(self, v):
        depth, idx = v
        seq = self.__DAG[depth][idx]
        return bool(seq)


class RootedTree__ContainerAsNode(IRootedTree):
    def __init__(self, container):
        self.__root = container
    def root(self):
        return self.__root
    def unstable_iter_children(self, v):
        return iter(v)
    def is_leaf(self, v):
        return bool(v)

def rooted_tree_to_binary_string(__tree):
    # '1' - open; '0' - close
    # output: regex'[10]+'; len == num_vertices*2
    tree = __tree
    assert isinstance(tree, IRootedTree)
    root = tree.root()
    out = StringIO()
    def this_func(v):
        out.write('1')
        for u in tree.unstable_iter_children(v):
            this_func(u)
        out.write('0')

    this_func(root)
    return out.getvalue()

def rooted_tree_to_depth2vertices(__tree, __container=tuple):
    # depth root == 0
    # output: depth2vertices :: [[Vertex]]
    tree = __tree
    T = __container
    assert isinstance(tree, IRootedTree)

    vss = []
    vs = T([tree.root()])
    while vs:
        vss.append(vs)
        vs = T(chain.from_iterable(map(tree.unstable_iter_children, vs)))
    return vss




class IRootedTree__parent(IRootedTree):
    @abstractmethod
    def is_root(self, v):...
    @abstractmethod
    def unsafe_parent(self, v):...
        # v should not be a root
        # if v is root, raise
    #def vertex_eq(self, v, u):
class IRootedTree__parent_Wrapper(IRootedTreeWrapper):
    def is_root(self, v):
        return self.get_underlying_tree().is_root(v)
    def unsafe_parent(self, v):
        return self.get_underlying_tree().unsafe_parent(v)



'''
class IIsVertex(IGraphBase):
    @abstractmethod
    def is_vertex(self, v):...
'''
class IVerticesAreUInt(IGraphBase):...
class IBoundedVertex(IVerticesAreUInt):
    @abstractmethod
    def vertex_upper_bound(self):...




RootedTreeCanonizationRequires = (IBoundedVertex, IRootedTree__parent)
class RootedTree__UIntAsVertex(*RootedTreeCanonizationRequires):
    def __init__(self, vtx2may_parent):
        # vtx2may_parent :: [None|uint]
        # root = len(vtx2may_parent)
        # vtx2may_parent[vtx]
        #       = None -- vtx is not vertex
        #       | parent -- assert vtx < parent <= root
        vtx2may_parent = tuple(vtx2may_parent)
        root = len(vtx2may_parent)

        vtx2may_children = [None if may is None else [] for may in vtx2may_parent]
        vtx2may_children.append([]) # for root
        for vtx, may_parent in enumerate(vtx2may_parent):
            if may_parent is not None:
                parent = may_parent
                if not (vtx < parent <= root): raise ValueError
                vtx2may_children[parent].append(vtx)

        vtx2may_children = tuple(vtx2may_children)
        self.vtx2may_parent = vtx2may_parent
        self.vtx2may_children = vtx2may_children
    def root(self):
        return len(self.vtx2may_parent)
    def is_leaf(self, v):
        return v >= 0 and len(self.vtx2may_children[v]) == 0
    def unstable_iter_children(self, v):
        return iter(self.vtx2may_children[v])


    def is_root(self, v):
        return self.root() == v
    def unsafe_parent(self, v):
        may = self.vtx2may_parent[v]
        if may is None: raise NotVertexError
        return may
    def vertex_upper_bound(self):
        return self.root() + 1
    '''
    def _is_vertex(self, v):
        root = self.root()
        return 0 <= v <= root and self.vtx2may_children[v] is not None
    def root(self):
    def unstable_iter_children(self, v):
    def is_leaf(self, v):
    def is_root(self, v):
    def unsafe_parent(self, v):
    def vertex_upper_bound(self):
    #def _is_vertex(self, v):
    '''













"""
class IColoredVertices(IGraphBase):
    @abstractmethod
    def vtx2color(self, v):...
class IColorsAreUInt(IColoredVertices):pass
class IBoundedColor(IColorsAreUInt):
    @abstractmethod
    def color_upper_bound(self):...
ColoredRootedTreeCanonizationRequires = (IBoundedColor, *RootedTreeCanonizationRequires)
is_seq
class Color_RootedTree(*ColoredRootedTreeCanonizationRequires):
    # ColoredRootedTreeCanonizationRequires = vtx2color + RootedTreeCanonizationRequires
    def __init__(self, __tree, __vtx2color, __color_upper_bound=None):
        tree = __tree # underlying tree
        vtx2color = __vtx2color
        if not all(isinstance(tree, T) for T in RootedTreeCanonizationRequires): raise TypeError
        if not is_seq(vtx2color): raise TypeError
        colors = map(vtx2color.__getitem__, tree.unstable_iter_vertices())
        color_upper_bound = max(colors, default=-1)+1

        if __color_upper_bound is not None:
            if __color_upper_bound < color_upper_bound: raise ValueError
            color_upper_bound = __color_upper_bound
        self.__tree = tree
        self.__vtx2color = vtx2color
        self.__color_upper_bound = color_upper_bound
    def root(self):
        return self.__tree.root()
    def unstable_iter_children(self, v):
        return self.__tree.unstable_iter_children(v)
    def is_leaf(self, v):
        return self.__tree.is_leaf(v)
    def is_root(self, v):
        return self.__tree.is_root(v)
    def unsafe_parent(self, v):
        return self.__tree.unsafe_parent(v)
    def vertex_upper_bound(self):
        return self.__tree.vertex_upper_bound()
    def vtx2color(self, v):
        return self.__vtx2color[v]
    def color_upper_bound(self):
        return self.__color_upper_bound

    '''
    def _is_vertex(self, v):
        return self.__tree._is_vertex(v)
    def root(self):
    def unstable_iter_children(self, v):
    def is_leaf(self, v):
    def is_root(self, v):
    def unsafe_parent(self, v):
    def vertex_upper_bound(self):
    #def _is_vertex(self, v):
    def vtx2color(self, v):...
    def color_upper_bound(self):...
    '''
"""




# canonization



class RootedTreeCanonization__leveled_DAG:
    '''
    if the tree is colored and weighted,
        then we make a big new_color<vtx> =
            (old_color<vtx>, 0 if vtx is root else weight<parent<vtx>, vtx>)
    '''

    def to_canonization_binary_string(self, __tree
            , __colorTV=None, __vtx2color=None
            , *, vtx2seq=None, vtx_upper_bound=None):
        # '1' - open; '0' - close
        # output: regex'[10]+'; len == num_vertices*2
        leveled_DAG = self.canonization(
            __tree, __colorTV, __vtx2color
            , vtx2seq=vtx2seq, vtx_upper_bound=vtx_upper_bound)
        t = RootedTree__leveled_DAG_as_Tree(leveled_DAG)
        return rooted_tree_to_binary_string(t)


    def __call__(self, __tree
            , __colorTV=None, __vtx2color=None
            , *, vtx2seq=None, vtx_upper_bound=None):
        return self.canonization(
            __tree, __colorTV, __vtx2color
            , vtx2seq=vtx2seq, vtx_upper_bound=vtx_upper_bound)
    def canonization(self, __tree
            , __colorTV=None, __vtx2color=None
            , *, vtx2seq=None, vtx_upper_bound=None):
        # output: depth2idx2seq :: [[[uint]]]
        #   seq = [new_color; next level child idx...]
        #       new_color is compact color idx in curr level
        #       will be remove in final result
        # input:
        #   see canonization_ex
        depth2idx2seq, depth2idx2vtc = self.canonization_ex(
            __tree, __colorTV, __vtx2color
            , vtx2seq=vtx2seq, vtx_upper_bound=vtx_upper_bound)
        return depth2idx2seq

    def weighted_colored_canonization_ex(self, __tree
            , __weight_upper_bound, __nonroot_vtx2edge_weight
            , __color_upper_bound, __vtx2color
            , *, vtx2seq=None, vtx_upper_bound=None):
        # input:
        #   weight_upper_bound :: uint
        #   nonroot_vtx2edge_weight :: nonroot_vtx -> edge_weight which is uint
        #   or: nonroot_vtx2edge_weight.__getitem__ :: nonroot_vtx -> edge_weight
        # other input/output: see colored_canonization_ex
        W = __weight_upper_bound
        if W < 2:
            return self.colored_canonization_ex(__tree
                    , __color_upper_bound, __vtx2color
                    , vtx2seq=vtx2seq, vtx_upper_bound=vtx_upper_bound)

        C = __color_upper_bound
        if C < 2:
            def vtx2edge_weight(vtx):
                if tree.is_root(vtx): return 0
                return __nonroot_vtx2edge_weight(vtx)
            return self.colored_canonization_ex(__tree
                    , W, vtx2edge_weight
                    , vtx2seq=vtx2seq, vtx_upper_bound=vtx_upper_bound)
        colorTV = BoundedUIntTV(C)
        weightTV = BoundedUIntTV(W)
        return self.wc_canonization_ex(__tree
                , weightTV, __nonroot_vtx2edge_weight
                , colorTV, __vtx2color
                , vtx2seq=vtx2seq, vtx_upper_bound=vtx_upper_bound)

    def to_callable(self, f):
        assert f is not None
        if callable(f): return f
        return getattr(f, '__getitem__')
    def fix_root_weight(self, __is_root, __weightTV, __nonroot_vtx2edge_weight):
        nonroot_vtx2edge_weight = self.to_callable(__nonroot_vtx2edge_weight)
        weightTV = maybeTV(__weightTV)
            # SwitchTV([BoundedUIntTV(1), __weightTV])
        def vtx2edge_weight(vtx):
            if __is_root(vtx): return Nothing
            return Just(nonroot_vtx2edge_weight(vtx))
        return weightTV, vtx2edge_weight
    def make_big_color(self, __is_root
            , __weightTV, __nonroot_vtx2edge_weight
            , __colorTV, __vtx2color):
        weightTV, vtx2edge_weight = self.fix_root_weight(
            __is_root, __weightTV, __nonroot_vtx2edge_weight)
        vtx2color = self.to_callable(__vtx2color)

        big_colorTV = TplTV([weightTV, __colorTV])
        def vtx2big_color(vtx):
            return (vtx2edge_weight(vtx), vtx2color(vtx))
        return big_colorTV, vtx2big_color

    def wc_canonization_ex(self, __tree
            , __weightTV, __nonroot_vtx2edge_weight
            , __colorTV, __vtx2color
            , *, vtx2seq=None, vtx_upper_bound=None):
        big_colorTV, vtx2big_color = self.make_big_color(
            __tree.is_root
            , __weightTV, __nonroot_vtx2edge_weight
            , __colorTV, __vtx2color)
        return self.canonization_ex(__tree, big_colorTV, vtx2big_color
                    , vtx2seq=vtx2seq, vtx_upper_bound=vtx_upper_bound)

    def colored_canonization_ex(self, __tree
            , __color_upper_bound, __vtx2color
            , *, vtx2seq=None, vtx_upper_bound=None):
        # input:
        #   color_upper_bound :: uint
        #   vtx2color :: vtx -> color which is uint
        #   or: vtx2color.__getitem__ :: vtx -> color which is uint
        #
        #   tree, vtx2seq, vtx_upper_bound
        #       see canonization_ex
        # output:
        #       see canonization_ex
        C = __color_upper_bound
        if C > 1:
            colorTV = BoundedUIntTV(C)
            vtx2color = __vtx2color
        else:
            colorTV = vtx2color = None
        return self.canonization_ex(__tree, colorTV, vtx2color
                    , vtx2seq=vtx2seq, vtx_upper_bound=vtx_upper_bound)
    def canonization_ex(self, __tree
            , __colorTV=None, __vtx2color=None
            , *, vtx2seq=None, vtx_upper_bound=None):
        # input:
        #   vtx2seq is None and vtx_upper_bound is None
        #       tree :: IRootedTree__parent & IBoundedVertex
        #   or vtx2seq.__getitem__ :: vtx -> multi_seq which init empty per vtx
        #       tree :: IRootedTree__parent
        #       vtx may not be uint, now.
        #   or vtx_upper_bound :: uint
        #       tree :: IRootedTree__parent
        #
        #   vtx2color is None
        #       colorTV is None
        #   or: vtx2color :: vtx -> color which is element of colorTV
        #       vtx2color.__getitem__ :: vtx -> color which is element of colorTV
        #       colorTV :: IBucketSortableTV & KnownTVs
        # output:
        #   depth2idx2seq :: [[[uint]]]
        #   depth2idx2vtc :: [[[vtx]]]
        # depth2idx2seq[depth][idx] = seq
        #   means except head of seq:
        #       all nodes at the level of depth have children patterns
        #       descripted by seqs which are sorted as idx
        #       head - the new_color will be remove in final result
        # depth2idx2seq is indeed a DAG, which represent a compact tree
        #   it vertex has form (depth, idx)
        #       whose children are [(depth+1, i) for i in depth2idx2seq[depth][idx]]
        # depth2idx2vtc[depth][idx] = sorted[vtx]
        #   (depth, idx) <-[1:many]-> vtx under isomorphism
        tree = __tree
        colorTV = __colorTV
        vtx2color = __vtx2color

        if not isinstance(tree, IRootedTree__parent): raise TypeError
        vtx2seq = self.__make_vtx2seq(vtx2seq, vtx_upper_bound, tree)
        key__vtx2color = self.__make_key__vtx2color(vtx2color, colorTV)


        depth2vertices = rooted_tree_to_depth2vertices(tree, list)


        if key__vtx2color is None:
            to_del0_seq = False
            depth2new_color_upper_bound = [0]*len(depth2vertices)
        else:
            # new: depth2new_color_upper_bound
            # modify: depth2vertices, to_del0_seq, vtx2seq
            to_del0_seq = True
            depth2new_color_upper_bound = getattr(self,
                    '_RootedTreeCanonization__leveled_DAG'
                    '__inner_sort_depth2vertices'
                    '_and_save_new_color'
                    '_and_calc_depth2new_color_upper_bound'
                )(depth2vertices, vtx2seq,     key__vtx2color, colorTV)
        pass





        def key__vtx2seq(v): return vtx2seq[v]

        elem_upper_bound = 0 # depthest nodes are leaves, which have no children
        reversed_depth2idx2seq = []
            # :: [[[elem]]]; save
        reversed_depth2idx2vtc = []
            # :: [[[vtx]]]

        root_vs = depth2vertices[0]
        for vs, newC in zip(*map(reversed, [depth2vertices, depth2new_color_upper_bound])):
            is_root = vs is root_vs

            elem_upper_bound = max(elem_upper_bound, newC)
            vs = UIntSeqSort(elem_upper_bound, key=key__vtx2seq)(vs)
            seq_vs_pairs = GroupBy(key=key__vtx2seq)(vs)

            idx2seq = []
            idx2vtc = []
            if not is_root:
                for idx, (seq, vs) in enumerate(seq_vs_pairs):
                    # assert idx == len(idx2seq) == len(idx2vtc)
                    idx2seq.append(seq) # idx
                    idx2vtc.append(vs)

                    elem = idx
                    for v in vs:
                        p = tree.unsafe_parent(v)
                        vtx2seq[p].append(elem)
            else:
                [(seq, vs)] = seq_vs_pairs
                idx2seq.append(seq) # idx
                idx2vtc.append(vs)
            reversed_depth2idx2seq.append(idx2seq)
            reversed_depth2idx2vtc.append(idx2vtc)
            elem_upper_bound = len(idx2seq)

        reversed_depth2idx2seq.reverse(); reversed_depth2idx2vtc.reverse()
        depth2idx2seq, depth2idx2vtc = reversed_depth2idx2seq, reversed_depth2idx2vtc
        del reversed_depth2idx2seq, reversed_depth2idx2vtc

        self.__to_del0_seq(to_del0_seq, depth2idx2seq)
        return depth2idx2seq, depth2idx2vtc



    def __to_del0_seq(self, to_del0_seq, depth2idx2seq):
        if to_del0_seq:
            begin = 1
        else:
            begin = 0

        for idx2seq in depth2idx2seq:
            assert begin == 0 or list(map(fst, idx2seq)) == list(range(len(idx2seq)))
            #for seq in idx2seq: del seq[0] # remove new_color
            #seq is key__vtx2seq
            #here to create new one
            for i in range(len(idx2seq)):
                idx2seq[i] = idx2seq[i][begin:]
        return None


    def __make_key__vtx2color(self, vtx2color, colorTV):
        if vtx2color is None:
            assert colorTV is None
            key__vtx2color = None
        elif not isinstance(colorTV, KnownTVs): raise TypeError
        elif callable(vtx2color):
            key__vtx2color = vtx2color
        else:
            key__vtx2color = getattr(vtx2color, '__getitem__', None)
            if key__vtx2color is None:
                raise TypeError('vtx2color should be None or callable or hasattr __getitem__')
        return key__vtx2color


    def __make_vtx2seq(self, vtx2seq, vtx_upper_bound, tree):
        if vtx2seq is not None: return vtx2seq
        if vtx_upper_bound is None:
            if not isinstance(tree, IBoundedVertex): raise TypeError
            V = tree.vertex_upper_bound()
        else:
            V = vtx_upper_bound
        # seq = [new_color of vtx; next level idx of children]
        vtx2seq = [[] for _ in range(V)]
        return vtx2seq


    def __inner_sort_depth2vertices_and_save_new_color_and_calc_depth2new_color_upper_bound(self
            , depth2vertices # modify

            # to save icolor first and then save new_color
            , vtx2seq

            , key__vtx2color
            , colorTV):
        def iter_vertices():
            return chain.from_iterable(depth2vertices)

        # depth2vertices inner sorted by color
        sort = BucketSortableSort(colorTV, key=key__vtx2color)
        icolor2vertices = sort.sort_and_groups(iter_vertices())
        # now color -> icolor which is a uint

        C = len(icolor2vertices)
        for icolor, vs in enumerate(icolor2vertices):
            for v in vs:
                seq = vtx2seq[v]
                assert not seq # otherwise del seq[0] will error
                seq.append(icolor) # tmp! will pop soon
        def key__vtx2icolor(v): # tmp! will del soon
            return vtx2seq[v][-1]

        inplace_bucket_sort(depth2vertices, C, key=key__vtx2icolor)

        # [sorted[(old_color, [vtx])]]
        depth2new_color2vertices= list(map(GroupBy(key=key__vtx2icolor).groups, depth2vertices))

        # del tmp
        #for v in iter_vertices(): vtx2seq[v].pop()
        #see below: seq[-1] = ...


        # init head of seq in vtx2seq
        for new_color2vertices in depth2new_color2vertices:
            for new_color, vs in enumerate(new_color2vertices):
                for vtx in vs:
                    seq = vtx2seq[vtx]
                    seq[-1] = new_color

        depth2new_color_upper_bound = list(map(len, depth2new_color2vertices))
        return depth2new_color_upper_bound


#colored_rooted_tree_canonization__leveled_DAG = ColoredRootedTreeCanonization__leveled_DAG()
rooted_tree_canonization__leveled_DAG = RootedTreeCanonization__leveled_DAG()



if __name__ == "__main__":
    import sys
    def show(*args):
        print(*args, file=sys.stderr)
    import doctest
    doctest.testmod()
    for k in list(globals()): print(k)




'''
class IVerticesAreMinConsecutiveUInt(IVerticesAreUInt):
    def num_vertices(self):
    def stable_iter_vertices(self):
        return range(self.num_vertices())

def rooted_colored_tree_canonization(tree):
    assert isinstance(tree, IRootedTree__parent)
    assert isinstance(tree, IBoundedVertex)
    assert isinstance(tree, IIsVertex)
    assert isinstance(tree, IBoundedColor)
    



'''

