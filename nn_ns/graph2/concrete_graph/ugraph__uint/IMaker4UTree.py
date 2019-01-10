
__all__ = '''
    IMaker4UTree
    '''.split()

from .abc import ABC, abstractmethod
from seed.types.ImmutableNamespace import ImmutableNamespace


class IMaker4UTree(ABC):
    '''

why IMaker4UTree instead of Maker4UTree?
    I donot determine the type of utree:
        utree :: UGraph/UGraphBasic/...???

see:
    "def - 6. utree.txt"
    "def - 6.2. rooted utree.txt"


distinguished by root_vertex/root_aedge
    # i.e. unicenter_vertex/bicenter_aedge
    make_*_from_utree_with_root_vertex
    make_*_from_utree_with_root_aedge

upper_hedge incident to parent vertex
lower_hedge incident to child vertex
parent_aedge may or may not incident to parent vertex
    if parent_aedge is not the root_aedge, then incident to parent vertex

depth/level/height
    # depth
    depth node tree = length (path_to_root node tree)
    [depth (root tree) tree == 0]

    # level
    level node tree = 1 + depth node tree

    # height
    -- root_height tree = max [depth leaf tree | leaf <- leafs tree]
    -- height node tree = root_height (subtree node tree)
    height node tree
        | is_leaf node tree = 0
        | otherwise = 1 + max . map (flip height tree) $ children node tree
    [is_leaf node tree] <==> [height node tree == 0]
    root_height tree = height (root tree) tree



depth
    depth_idx depends on depth
    depth2vertices1 == depth2depth_idx2vertex
    depth2depth_idx2vertex <==> (vertex2depth, vertex2depth_idx)


required attrs of utree:
    num_vertices
    num_aedges
    hedge2vertex
    hedge2another_hedge
    hedge2aedge
    vertex2degree
    aedge2arbitrary_hedge

result attrs of make_all_rooted_utree_attrs:
    aedge2maybe_upper_hedge
    vertex2maybe_parent_aedge
    either_root
    vertex2child_aedges
    vertex2maybe_parent_vertex
    vertex2depth
    depth2vertices1
    depth2depth_idx2vertex
    vertex2depth_idx

methods:
    make_all_rooted_utree_attrs
    `vertex2unstable_iter_hedges
    hedge2unstable_iter_other_hedges_around_another_vertex
    vertex2unstable_iter_incident_aedge_neighbor_hedge_neighbor_vertex_triples

    aedge2maybe_upper_hedge
        aedge2maybe_upper_hedge__using_center_as_root
        aedge2maybe_upper_hedge__with_root_vertex
        aedge2maybe_upper_hedge__with_root_aedge
        _inplace_aedge2maybe_upper_hedge4subtree_with_root_lower_hedge


usage:
    ns = Subclass_of_IMaker4UTree(utree).make_all_rooted_utree_attrs(maybe_either_root=None)
    ns.either_root
        # either_root == either_center if above maybe_either_root=None
'''
    #__slots__ = ()

    all_attr_seq = '''
        aedge2maybe_upper_hedge
        vertex2maybe_parent_aedge
        either_root
        vertex2child_aedges
        vertex2maybe_parent_vertex
        vertex2depth
        depth2vertices1
        depth2depth_idx2vertex
        vertex2depth_idx
        '''.split()
    all_attr_set = frozenset(all_attr_seq)

    def __init__(self, utree):
        assert utree.num_vertices == utree.num_aedges + 1
        self.utree = utree

    def make_all_rooted_utree_attrs(self, *, maybe_either_root):
        # no "utree"??
        # maybe_either_root - see: aedge2maybe_upper_hedge()
        aedge2maybe_upper_hedge = self.aedge2maybe_upper_hedge(
            maybe_either_root=maybe_either_root)
        vertex2maybe_parent_aedge = self.vertex2maybe_parent_aedge(
            aedge2maybe_upper_hedge=aedge2maybe_upper_hedge)
        either_root = self.either_root(
            aedge2maybe_upper_hedge=aedge2maybe_upper_hedge
            ,vertex2maybe_parent_aedge=vertex2maybe_parent_aedge)
        vertex2child_aedges = self.vertex2child_aedges(
            aedge2maybe_upper_hedge=aedge2maybe_upper_hedge
            ,vertex2maybe_parent_aedge=vertex2maybe_parent_aedge)
        vertex2maybe_parent_vertex = self.vertex2maybe_parent_vertex(
            aedge2maybe_upper_hedge=aedge2maybe_upper_hedge
            ,vertex2maybe_parent_aedge=vertex2maybe_parent_aedge)
        vertex2depth = self.vertex2depth(
            vertex2maybe_parent_vertex=vertex2maybe_parent_vertex)
        depth2vertices1 = self.depth2vertices1(vertex2depth=vertex2depth)
        depth2depth_idx2vertex = self.depth2depth_idx2vertex(depth2vertices1=depth2vertices1)
        vertex2depth_idx = self.vertex2depth_idx(depth2vertices1=depth2vertices1)

        ################
        del self, maybe_either_root
        d = dict(locals()) # __class__ in locals???
        for name in (frozenset(d) - __class__.all_attr_set):
            del d[name]

        try:
            assert frozenset(d) == __class__.all_attr_set
        except:
            from seed.tiny import print_err
            print_err(__class__.all_attr_set - frozenset(d))
            print_err(frozenset(d) - __class__.all_attr_set)
            raise

        ns = ImmutableNamespace(**d)
        return ns

    @abstractmethod
    def vertex2unstable_iter_hedges(self, vertex):
        # -> Iter HEdge
        raise NotImplementedError

    def hedge2unstable_iter_other_hedges_around_another_vertex(self, hedge):
        # -> Iter HEdge
        other_hedge0 = self.utree.hedge2another_hedge[hedge]
        other_vertex = self.utree.hedge2vertex[other_hedge0]
        for other_hedge in self.vertex2unstable_iter_hedges(other_vertex):
            if other_hedge != other_hedge0:
                yield other_hedge

    def vertex2unstable_iter_incident_aedge_neighbor_hedge_neighbor_vertex_triples(self, vertex):
        hedge2vertex = self.utree.hedge2vertex
        hedge2another_hedge = self.utree.hedge2another_hedge
        hedge2aedge = self.utree.hedge2aedge
        for hedge in self.vertex2unstable_iter_hedges(vertex):
            incident_aedge = hedge2aedge[hedge]
            neighbor_hedge = hedge2another_hedge[hedge]
            neighbor_vertex =  hedge2vertex[neighbor_hedge]
            yield incident_aedge, neighbor_hedge, neighbor_vertex


    def aedge2maybe_upper_hedge(self, *, maybe_either_root):
        # (None|either_root) -> [(None|upper_hedge)]
        # either_root = (is_root_aedge, (root_vertex|root_aedge))
        # either_root = (False, root_vertex) | (True, root_aedge)
        # maybe_either_root is None <==> either_root = (False, unicenter_vertex)|(True, bicenter_aedge)
        # aedge2maybe_upper_hedge
        if maybe_either_root is None:
            return self.aedge2maybe_upper_hedge__using_center_as_root()
        else:
            (is_root_aedge, root) = either_root = maybe_either_root
            if is_root_aedge:
                root_aedge = root
                return self.aedge2maybe_upper_hedge__with_root_aedge(
                            root_aedge=root_aedge)
            else:
                root_vertex = root
                return self.aedge2maybe_upper_hedge__with_root_vertex(
                            root_vertex=root_vertex)
        pass

    def _inplace_aedge2maybe_upper_hedge4subtree_with_root_lower_hedge(self, *
        , aedge2maybe_upper_hedge, subtree_root_lower_hedge
        ):
        # -> None
        # OUT: aedge2maybe_upper_hedge
        # donot set aedge2maybe_upper_hedge[subtree_root_aedge]
        utree = self.utree
        hedge2another_hedge = utree.hedge2another_hedge
        aedge2arbitrary_hedge = utree.aedge2arbitrary_hedge
        hedge2vertex = utree.hedge2vertex

        upper_hedge = hedge2another_hedge[subtree_root_lower_hedge]
        upper_hedges = [upper_hedge]
        iter_child_hedges = self.hedge2unstable_iter_other_hedges_around_another_vertex
        while upper_hedges:
            parent_upper_hedge = upper_hedges.pop()
            for child_upper_hedge in iter_child_hedges(parent_upper_hedge):
                child_aedge = hedge2aedge[child_upper_hedge]
                aedge2maybe_upper_hedge[child_aedge] = child_upper_hedge
                upper_hedges.append(child_upper_hedge)
        return None

    def aedge2maybe_upper_hedge__with_root_aedge(self, *, root_aedge):
        # nonedgeless utree
        utree = self.utree
        hedge2another_hedge = utree.hedge2another_hedge

        root_lower_hedge0 = utree.aedge2arbitrary_hedge[root_aedge]
        root_lower_hedge1 = hedge2another_hedge[root_lower_hedge0]

        aedge2maybe_upper_hedge = [None]*utree.num_aedges
        inplace = self._inplace_aedge2maybe_upper_hedge4subtree_with_root_lower_hedge
        inplace(aedge2maybe_upper_hedge=aedge2maybe_upper_hedge
                , subtree_root_lower_hedge=root_lower_hedge0)
        inplace(aedge2maybe_upper_hedge=aedge2maybe_upper_hedge
                , subtree_root_lower_hedge=root_lower_hedge1)

        #aedge2maybe_upper_hedge[root_aedge] = None
        assert aedge2maybe_upper_hedge[root_aedge] is None
        num_None_upper_hedges = sum(h is None for h in aedge2maybe_upper_hedge)
        assert num_None_upper_hedges == 1
        return tuple(aedge2maybe_upper_hedge)
    def aedge2maybe_upper_hedge__with_root_vertex(self, *, root_vertex):
        # maybe edgeless utree
        utree = self.utree

        for upper_hedge in self.vertex2unstable_iter_hedges(root_vertex):
            break
        else:
            assert not utree.num_aedges
            aedge2maybe_upper_hedge = ()
            return aedge2maybe_upper_hedge
        pseudo_root_aedge = utree.hedge2aedge[upper_hedge]
        aedge2maybe_upper_hedge = self.aedge2maybe_upper_hedge__with_root_aedge(root_aedge=pseudo_root_aedge)
        aedge2maybe_upper_hedge = list(aedge2maybe_upper_hedge)
        aedge2maybe_upper_hedge[pseudo_root_aedge] = upper_hedge
        return tuple(aedge2maybe_upper_hedge)
    def aedge2maybe_upper_hedge__using_center_as_root(self):
        # -> [(None|upper_hedge)]
        # aedge2maybe_upper_hedge
        #
        # unicenter_vertex or bicenter_aedge as root
        utree = self.utree
        vertex2height = [0]*utree.num_vertices
        vertex2remain = list(utree.vertex2degree)
        assert vertex2remain

        aedge2maybe_upper_hedge = [None]*utree.num_aedges
        vertices_le1 = [v for v,r in enumerate(vertex2remain) if r <= 1]
        assert vertices_le1


        i = 0
        # bug: done = False
        #   when num_vertices == 1
        done = utree.num_vertices == 1
        while i < len(vertices_le1):
            vertex = vertices_le1[i]
            i += 1

            remain = vertex2remain[vertex]
            assert 0 <= remain <= 1

            if remain:
                # 1
                if done: raise logic-error
                for incident_aedge, neighbor_hedge, neighbor_vertex in self.vertex2unstable_iter_incident_aedge_neighbor_hedge_neighbor_vertex_triples(vertex):
                    if aedge2maybe_upper_hedge[incident_aedge] is None:
                        assert vertex2remain[neighbor_vertex] >= 1
                        vertex2remain[vertex] -= 1
                        vertex2remain[neighbor_vertex] -= 1
                        neighbor_remain = vertex2remain[neighbor_vertex]
                        if neighbor_remain == 1:
                            vertices_le1.append(neighbor_vertex)
                            # since ==0 must already inside vertices_le1
                        ###
                        neighbor_height = vertex2height[neighbor_vertex]
                        height = vertex2height[vertex]
                        if neighbor_remain or neighbor_height > height:
                            # incident_aedge is not root_aedge
                            upper_hedge = neighbor_hedge
                            aedge2maybe_upper_hedge[incident_aedge] = upper_hedge
                            if neighbor_height == height:
                                #vertex2height[neighbor_vertex] = max(neighbor_height, 1+height)
                                vertex2height[neighbor_vertex] = 1+height
                        else:
                            # incident_aedge is root_aedge
                            assert neighbor_remain == 0 and neighbor_height == height
                        if not neighbor_remain:
                            done = True
                        break
                    else:
                        assert vertex2remain[neighbor_vertex] == 0
                else:
                    raise logic-error
            else:
                # 0
                if not (done and i == len(vertices_le1)): raise logic-error
                break
        else:
            raise logic-error

        num_None_upper_hedges = sum(h is None for h in aedge2maybe_upper_hedge)
        assert 0 <= num_None_upper_hedges <= 1
        return tuple(aedge2maybe_upper_hedge)


    def vertex2maybe_parent_aedge(self, *, aedge2maybe_upper_hedge):
        # -> [(None|parent_aedge)]
        # vertex2maybe_parent_aedge
        utree = self.utree
        hedge2vertex = utree.hedge2vertex
        hedge2another_hedge = utree.hedge2another_hedge
        aedge2arbitrary_hedge = utree.aedge2arbitrary_hedge

        vertex2maybe_parent_aedge = [None]*utree.num_vertices
        for aedge, maybe_upper_hedge in enumerate(aedge2maybe_upper_hedge):
            if maybe_upper_hedge is None:
                # aedge is root_aedge
                hedge = aedge2arbitrary_hedge[aedge]
                other = hedge2another_hedge[hedge]
                lower_hedges = [hedge, other]
            else:
                # aedge is directed tree aedge
                upper_hedge = maybe_upper_hedge
                lower_hedge = hedge2another_hedge[upper_hedge]
                lower_hedges = [lower_hedge]

            parent_aedge = aedge
            for lower_hedge in lower_hedges:
                child_vertex = hedge2vertex[lower_hedge]
                assert vertex2maybe_parent_aedge[child_vertex] is None
                vertex2maybe_parent_aedge[child_vertex] = parent_aedge

        num_None_parent_aedges = sum(e is None for e in vertex2maybe_parent_aedge)
        num_None_upper_hedges = sum(h is None for h in aedge2maybe_upper_hedge)
        assert num_None_parent_aedges + num_None_upper_hedges == 1
        assert 0<= num_None_parent_aedges <= 1
        assert 0<= num_None_upper_hedges <= 1

        return tuple(vertex2maybe_parent_aedge)

    def either_root(self, *, aedge2maybe_upper_hedge, vertex2maybe_parent_aedge):
        # -> (is_root_aedge, root_vertex_or_root_aedge)
        # -> (False, root_vertex)|(True, root_aedge)
        for vertex, maybe_parent_aedge in enumerate(vertex2maybe_parent_aedge):
            if maybe_parent_aedge is None:
                # vertex is root_vertex
                root_vertex = vertex
                either_root = (False, root_vertex)
                break
            else:
                parent_aedge = maybe_parent_aedge
                maybe_upper_hedge = aedge2maybe_upper_hedge[parent_aedge]
                if maybe_upper_hedge is None:
                    # parent_aedge is root_aedge
                    root_aedge = parent_aedge
                    either_root = (True, root_aedge)
                    break
        else:
            raise logic-error
        return either_root
    def vertex2child_aedges(self, *, aedge2maybe_upper_hedge, vertex2maybe_parent_aedge):
        # -> [[aedge]]
        # vertex2child_aedges

        utree = self.utree
        aedge2arbitrary_hedge = utree.aedge2arbitrary_hedge
        hedge2another_hedge = utree.hedge2another_hedge
        hedge2vertex = utree.hedge2vertex
        vertex2child_aedges = []
        for vertex, maybe_parent_aedge in enumerate(vertex2maybe_parent_aedge):
            if maybe_parent_aedge is None:
                # vertex is root_vertex
                it = self.vertex2unstable_iter_hedges(vertex)
            else:
                parent_aedge = maybe_parent_aedge
                maybe_upper_hedge = aedge2maybe_upper_hedge[parent_aedge]
                if maybe_upper_hedge is None:
                    # parent_aedge is root_aedge
                    hedge = aedge2arbitrary_hedge[parent_aedge]
                    if vertex == hedge2vertex[hedge]:
                        pseudo_lower_hedge = hedge
                        pseudo_upper_hedge = hedge2another_hedge[pseudo_lower_hedge]
                    else:
                        pseudo_upper_hedge = hedge
                else:
                    upper_hedge = maybe_upper_hedge
                    pseudo_upper_hedge = upper_hedge
                it = self.hedge2unstable_iter_other_hedges_around_another_vertex(pseudo_upper_hedge)
            vertex2child_aedges.append(tuple(it))
        return tuple(vertex2child_aedges)
    def vertex2maybe_parent_vertex(self, *, aedge2maybe_upper_hedge, vertex2maybe_parent_aedge):
        # -> [(None|parent_vertex)]
        # vertex2maybe_parent_vertex
        #
        hedge2vertex = self.utree.hedge2vertex
        vertex2maybe_parent_vertex = []
        for maybe_parent_aedge in vertex2maybe_parent_aedge:
            if maybe_parent_aedge is None:
                # curr vertex is root_vertex # unicenter_vertex
                maybe_parent_vertex = None
            else:
                parent_aedge = maybe_parent_aedge
                maybe_upper_hedge = aedge2maybe_upper_hedge[parent_aedge]
                if maybe_upper_hedge is None:
                    # parent_aedge is root_aedge
                    # curr vertex is one of bicenter_vertices
                    maybe_parent_vertex = None
                else:
                    upper_hedge = maybe_upper_hedge
                    parent_vertex = hedge2vertex[upper_hedge]
                    maybe_parent_vertex = parent_vertex
            vertex2maybe_parent_vertex.append(maybe_parent_vertex)
        return tuple(vertex2maybe_parent_vertex)

    def verify_vertex2depth(self, *, vertex2depth, vertex2maybe_parent_vertex):
        L = len(vertex2maybe_parent_vertex)
        if len(vertex2depth) != L: raise ValueError
        for vertex, depth in enumerate(vertex2depth):
            maybe_parent_vertex = vertex2maybe_parent_vertex[vertex]
            if maybe_parent_vertex is None:
                if depth != 0: raise ValueError
            else:
                parent_vertex = maybe_parent_vertex
                if depth != 1+vertex2depth[parent_vertex]: raise ValueError
        return True
    def vertex2depth(self, *, vertex2maybe_parent_vertex):
        # -> [depth]
        # vertex2depth
        # vertex2depth[root_vertex] == 0 if unicenter_vertex
        # vertex2depth[vertex incident to root_aedge] == 0 if bicenter_aedge
        L = len(vertex2maybe_parent_vertex)
        vertex2maybe_depth = [None]*L
        descendants = []
        for vertex in range(L):
            while True:
                maybe_depth = vertex2maybe_depth[vertex]
                if maybe_depth is not None:
                    last_descendant_depth = maybe_depth+1
                    break

                descendants.append(vertex)
                maybe_parent_vertex = vertex2maybe_parent_vertex[vertex]
                if maybe_parent_vertex is None:
                    last_descendant_depth = 0
                    break

                vertex = maybe_parent_vertex
            while descendants:
                vertex = descendants.pop()
                vertex2maybe_depth[vertex] = last_descendant_depth
                last_descendant_depth += 1
        assert all(h is not None for h in vertex2maybe_depth)
        vertex2depth = vertex2maybe_depth

        assert self.verify_vertex2depth(vertex2depth=vertex2depth, vertex2maybe_parent_vertex=vertex2maybe_parent_vertex)
        return tuple(vertex2depth)

    def depth2vertices1(self, *, vertex2depth):
        # -> [[vertex]]
        # depth2vertices1
        # -> [nonempty[vertex]]
        L = 1+max(vertex2depth, default=-1)
        depth2vertices1 = [[] for _ in range(L)]
        for vertex, depth in enumerate(vertex2depth):
            depth2vertices1[depth].append(vertex)
        assert all(depth2vertices1)
        return tuple(map(tuple, depth2vertices1))


    def depth2depth_idx2vertex(self, *, depth2vertices1):
        # -> [[vertex]]
        # depth2depth_idx2vertex
        depth2depth_idx2vertex = depth2vertices1
        return depth2depth_idx2vertex
    def vertex2depth_idx(self, *, depth2vertices1):
        # -> [depth_idx]
        # vertex2depth_idx
        # depth_idx depends on depth
        vertex2depth_idx = [None]*self.utree.num_vertices
        for vertices in depth2vertices1:
            for depth_idx, vertex in enumerate(vertices):
                vertex2depth_idx[vertex] = depth_idx
        assert all(i is not None for i in vertex2depth_idx)

        return tuple(vertex2depth_idx)

