
__all__ = '''
    canon_label_hweighted_nonedgeless_rigid_connected_ugraph_planar_embedding
    '''.split()

#from ..UIntBijectionBuilder import UIntBijectionBuilder
from ..inverse_uint_bijection import inverse_uint_bijection
from ..is_uint_bijection import is_uint_bijection
from ..UGraphFakeEmbedding import UGraphFakeEmbedding
from ..UGraphFakeEmbeddingLabelling import UGraphFakeEmbeddingLabelling
from ..is_uint_sequence import is_uint_sequence
from .make_compact_uint2group_idx import make_compact_uint2group_idx
from .canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge import \
    canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge
from seed.algo.bucket_sort.radix_sort_with_table import radix_sort_with_table
from seed.types.OneTime import OneTimeMap, OneTimeSet
from seed.math.floor_ceil import floor_log2
from itertools import accumulate, groupby

class canon_label_hweighted_nonedgeless_rigid_connected_ugraph_planar_embedding:
    '''
input:
    #hweighted rigid_connected nonedgeless ugraph_planar_embedding
    #   fvertex-color and fface-area can merge into hedge-hweight
    nonedgeless_rigid_connected_ugraph_planar_embedding :: UGraphFakeEmbedding
    hedge2hweight
output:
    ugraph_fake_embedding_labelling :: UGraphFakeEmbeddingLabelling
'''

    @classmethod
    def by_partition_distinguishable_hedges__O_E_logE(cls, *
        ,nonedgeless_rigid_connected_ugraph_planar_embedding
        ,hedge2hweight
        ,num_hweights
        ):
        '''
nonedgeless_rigid_connected_ugraph_planar_embedding -> hedge2hweight -> num_hweights -> ugraph_fake_embedding_labelling
ugraph_fake_embedding_labelling :: UGraphFakeEmbeddingLabelling


by partition distinguishable_hedges; O(E*log(E))


ref:
    "[planar_graph][triconnected][isomorphism][1973]A V log V algorithm for isomorphism of triconnected planar graphs[good].pdf"
        # but in this_func, neednot triconnected
        #   requires: planar & rigid_connected
see:
    .make_hedge2hweight.from_color_hweight_area
    by_partition_distinguishable_hedges_ex__O_E_logE
'''
        (ugraph_fake_embedding_labelling, hedge_classes
        ) = cls.by_partition_distinguishable_hedges_ex__O_E_logE(
                nonedgeless_rigid_connected_ugraph_planar_embedding
                    = nonedgeless_rigid_connected_ugraph_planar_embedding
                ,hedge2hweight = hedge2hweight
                ,num_hweights = num_hweights
                )
        return ugraph_fake_embedding_labelling

    @classmethod
    def by_partition_distinguishable_hedges_ex__O_E_logE(cls, *
        ,nonedgeless_rigid_connected_ugraph_planar_embedding
        ,hedge2hweight
        ,num_hweights
        ):

        '''
nonedgeless_rigid_connected_ugraph_planar_embedding -> hedge2hweight -> num_hweights -> (ugraph_fake_embedding_labelling, hedge_classes)

ugraph_fake_embedding_labelling :: UGraphFakeEmbeddingLabelling
hedge_classes :: [[HEdge]]

see:
    by_partition_distinguishable_hedges__O_E_logE
        diff only output
'''

        assert isinstance(nonedgeless_rigid_connected_ugraph_planar_embedding, UGraphFakeEmbedding)

        if not nonedgeless_rigid_connected_ugraph_planar_embedding.calc.is_ugraph_fake_embedding_nonedgeless_rigid_connected: raise ValueError
        if not nonedgeless_rigid_connected_ugraph_planar_embedding.calc.is_ugraph_fake_embedding_planar: raise ValueError

        ugraph_planar_embedding = nonedgeless_rigid_connected_ugraph_planar_embedding
        del nonedgeless_rigid_connected_ugraph_planar_embedding

        assert ugraph_planar_embedding.num_fvertices > 0
        assert ugraph_planar_embedding.num_hedges > 0
        assert ugraph_planar_embedding.num_ffaces > 0

        assert is_uint_sequence(hedge2hweight)
        assert len(hedge2hweight) == ugraph_planar_embedding.num_hedges
        assert num_hweights <= ugraph_planar_embedding.num_hedges
        assert max(hedge2hweight) < num_hweights
        assert min(hedge2hweight) >= 0

        (hedge2class_idx, class_idx2size, sorted_hedges
        ) = make_hedge2class_idx__via_radix_sort(
            ugraph_planar_embedding, num_hweights, hedge2hweight)


        #partition hedges by hedge2class_idx
        position2hedge = list(sorted_hedges)
        hedge2position = list(inverse_uint_bijection(position2hedge))
        hedge2class_idx = list(hedge2class_idx)
        class_idx2end = list(accumulate(class_idx2size))
        class_idx2begin = [0] if class_idx2end else []
        class_idx2begin.extend(class_idx2end[:-1])
        partition = Partition(
                ugraph_planar_embedding=ugraph_planar_embedding
                ,position2hedge=position2hedge
                ,hedge2position=hedge2position
                ,hedge2class_idx=hedge2class_idx
                ,class_idx2begin=class_idx2begin
                ,class_idx2end=class_idx2end
                )

        hedge_classes = partition.main()
        #choose root_hedge
        root_hedge = hedge_classes[0][0]

        ugraph_fake_embedding_labelling = canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge.by_dfs_preorder__O_E(
            rigid_connected_ugraph_fake_embedding=ugraph_planar_embedding
            ,root_hedge=root_hedge
            )
        return ugraph_fake_embedding_labelling, hedge_classes


class Partition:
    def __init__(self, *
        ,ugraph_planar_embedding
        ,position2hedge
        ,hedge2position
        ,hedge2class_idx
        ,class_idx2begin
        ,class_idx2end
        ):
        assert type(position2hedge) is list
        assert type(hedge2position) is list
        assert type(hedge2class_idx) is list
        assert type(class_idx2begin) is list
        assert type(class_idx2end) is list

        num_class_idc = len(class_idx2end)
        assert num_class_idc == len(class_idx2end) == len(class_idx2begin)
        assert 1+max(hedge2class_idx, default=-1) == num_class_idc

        num_hedges = ugraph_planar_embedding.num_hedges
        assert num_hedges == len(position2hedge)
        assert num_hedges == len(hedge2position) == len(hedge2class_idx)
        assert is_uint_bijection(hedge2position, position2hedge)
        assert all(0 <= class_idx2begin[class_idx] <= hedge2position[hedge] < class_idx2end[class_idx] <= num_hedges for hedge, class_idx in enumerate(hedge2class_idx))

        to_prev_L_hedge, to_prev_R_hedge = self.make_to_prev_LorR_hedge(ugraph_planar_embedding)

        self.ugraph_planar_embedding = ugraph_planar_embedding
        self.position2hedge = position2hedge
        self.hedge2position = hedge2position
        self.hedge2class_idx = hedge2class_idx
        self.class_idx2begin = class_idx2begin
        self.class_idx2end = class_idx2end
        self.to_prev_L_hedge = to_prev_L_hedge
        self.to_prev_R_hedge = to_prev_R_hedge
        self.class_idx2new_class_idx = OneTimeMap([None]*num_class_idc)
        self.set_of_class_idx_with_LorR = OneTimeSet([None]*(2*num_class_idc))

        for class_idx in range(num_class_idc):
            self.add_class_idx_LorR(class_idx, False)
            self.add_class_idx_LorR(class_idx, True)

        #self.stack = [(class_idx, to_partition_prev_LorR_hedge) for class_idx in range(num_class_idc) for to_partition_prev_LorR_hedge in (False, True)]
        #self.queue_begin = 0
        #self.queue_end = num_class_idc*2

    def add_class_idx_LorR(self, class_idx, LorR:bool):
        # L = False
        # R = True
        class_idx_with_LorR = self.make_class_idx_with_LorR(class_idx, LorR)
        self.set_of_class_idx_with_LorR.add(class_idx_with_LorR)
    def make_class_idx_with_LorR(self, class_idx, LorR:bool):
        if LorR not in (0, 1): raise ValueError
        #LorR = bool(LorR)
        class_idx_with_LorR = (class_idx << 1) | LorR
        return class_idx_with_LorR
    def pop_class_idx_LorR(self):
        class_idx_with_LorR = self.set_of_class_idx_with_LorR.pop()
        class_idx, LorR = divmod(class_idx_with_LorR, 2)
        return class_idx, LorR
    def contains_class_idx_LorR(self, class_idx, LorR:bool):
        class_idx_with_LorR = self.make_class_idx_with_LorR(class_idx, LorR)
        return class_idx_with_LorR in self.set_of_class_idx_with_LorR

    def make_to_prev_LorR_hedge(self, ugraph_planar_embedding):
        hedge2another_hedge = ugraph_planar_embedding.hedge2another_hedge
        hedge2fake_clockwise_prev_hedge_around_fface = ugraph_planar_embedding.hedge2fake_clockwise_prev_hedge_around_fface
        hedge2fake_clockwise_next_hedge_around_fface = ugraph_planar_embedding.hedge2fake_clockwise_next_hedge_around_fface
        def _to_prev_L_hedge(hedge):
            # clockwise
            return hedge2fake_clockwise_prev_hedge_around_fface[hedge]
        def _to_prev_R_hedge(hedge):
            # counterclockwise
            other = hedge2another_hedge(hedge)
            other_next = hedge2fake_clockwise_next_hedge_around_fface[other]
            other_next_other = hedge2another_hedge(other_next)
            return other_next_other

        num_hedges = ugraph_planar_embedding.num_hedges
        to_prev_R_hedge = tuple(map(_to_prev_R_hedge, range(num_hedges)))
        to_prev_L_hedge = hedge2fake_clockwise_prev_hedge_around_fface
        return to_prev_L_hedge, to_prev_R_hedge

    def get_hedge_block(self, class_idx):
        return self.position2hedge[self.class_idx2begin[class_idx]: self.class_idx2end[class_idx]]

    def make_new_class_idx(self, class_idx):
        new_class_idx = num_class_idc = len(self.class_idx2end)
        i = self.class_idx2end[class_idx]
        self.class_idx2begin.append(i)
        self.class_idx2end.append(i)
        #num_class_idc += 1
        self.class_idx2new_class_idx.buffer.append(None)
        # queue.append_right
        #self.queue_end += 2
        #error: should not append auto; check to filter out...
        #self.stack.append((new_class_idx, False))
        #self.stack.append((new_class_idx, True))
        self.set_of_class_idx_with_LorR.buffer.append(None)
        self.set_of_class_idx_with_LorR.buffer.append(None)
        return new_class_idx

    def get_class_size(self, class_idx):
        return self.class_idx2end[class_idx] - self.class_idx2begin[class_idx]
    def refine_partition(self):
        step = 0
        while self.set_of_class_idx_with_LorR:
            #queue.pop_left()
            #queue_idx = queue_begin
            #queue_begin += 1
            #class_idx, to_partition_prev_LorR_hedge = divmod(queue_idx, 2)
            class_idx, to_partition_prev_LorR_hedge = self.pop_class_idx_LorR()

            class_size = self.get_class_size(class_idx)
            step += class_size
            if not class_size: continue

            to_prev_LorR_hedge = (
                self.to_prev_R_hedge if to_partition_prev_LorR_hedge
                else self.to_prev_L_hedge
                )
            to_prev_LorR_hedge = to_prev_LorR_hedge.__getitem__

            #
            self.class_idx2new_class_idx.clear()
            hedge_block = self.get_hedge_block(class_idx)
            for prev_hedge in map(to_prev_LorR_hedge, hedge_block):
                self.move_to_new_class(prev_hedge)
            for class_idx, new_class_idx in self.class_idx2new_class_idx.items():
                for LorR in (False, True):
                    if self.contains_class_idx_LorR(class_idx, LorR):
                        class_idx_ = new_class_idx
                    else:
                        class_size = self.get_class_size(class_idx)
                        new_class_size = self.get_class_size(new_class_idx)
                        if new_class_size < class_size:
                            class_idx_ = new_class_idx
                        else:
                            class_idx_ = class_idx
                    self.add_class_idx_LorR(class_idx_, LorR)

        '''
        for a given (hedge, LorR):
            let sz[i] = block_size of i-th block that contains hedge
            sz[0] = block_size of block that contains hedge initially
            ...
            ...
            ==>> [sz[i+1] <= sz[i]/2]

            [block contains hedge]
            ==>> [sz[i] >= 1]
            ==>> [0 <= i < 1+floor_log2(sz[0]) <= 1+floor_log2(num_hedges)]
            ==>> at most (1+floor_log2) blocks had contains hedge
            ==>> we have pop and handle hedge at most (1+floor_log2) times
        ==>> step <= num_LorR * num_hedges * (1+floor_log2)
        ==>> step <= 2 * num_hedges * (1+floor_log2(num_hedges))

        '''
        # H = 2*E
        H = self.ugraph_planar_embedding.num_hedges
        #assert step <= 2*H*log2(H)
        assert step <= 2*H*(1+floor_log2(H))
    def main(self):
        # -> [[HEdge]]
        #
        self.refine_partition()

        self.position2hedge
        self.hedge2position

        self.hedge2class_idx
        self.class_idx2begin
        self.class_idx2end
        hedge_classes = [] # [[hedge]]
        for class_idx, hedges in groupby(self.position2hedge, key=lambda hedge: self.hedge2class_idx[hedge]):
            hedge_block = tuple(hedges)
            assert hedge_block
            hedge_classes.append(hedge_block)

        assert sum(map(len, hedge_classes)) == self.ugraph_planar_embedding.num_hedges
        return hedge_classes

    def move_to_new_class(self, hedge):
        class_idx = self.hedge2class_idx[hedge]
        maybe_new_class_idx = self.class_idx2new_class_idx.get(class_idx)
        if maybe_new_class_idx is not None:
            new_class_idx = maybe_new_class_idx
        else:
            new_class_idx = self.make_new_class_idx(class_idx)
            self.class_idx2new_class_idx[class_idx] = new_class_idx

        #bug:
        #   once forgot:
        #       self.hedge2class_idx[hedge] = new_class_idx
        #
        self.hedge2class_idx[hedge] = new_class_idx

        position = self.hedge2position[hedge]
        eb = self.class_idx2end[class_idx]
        assert self.class_idx2begin[new_class_idx] == eb
        eb -= 1

        if __debug__:
            try:
                assert 0 <= self.class_idx2begin[class_idx] <= eb < self.ugraph_planar_embedding.num_hedges
            except:
                raise BaseException(self.class_idx2begin[class_idx], eb, self.ugraph_planar_embedding.num_hedges)

        self.class_idx2end[class_idx] = self.class_idx2begin[new_class_idx] = eb

        self.swap_position(eb, position)
    def swap_position(self, position0, position1):
        if position0 == position1: return
        position2hedge = self.position2hedge
        hedge2position = self.hedge2position

        hedge0 = position2hedge[position0]
        hedge1 = position2hedge[position1]

        hedge2position[hedge0] = position1
        position2hedge[position1] = hedge0

        hedge2position[hedge1] = position0
        position2hedge[position0] = hedge1


def make_hedge2class_idx__via_radix_sort(ugraph_planar_embedding, num_hweights, hedge2hweight):
    # -> (hedge2class_idx, class_idx2size, sorted_hedges)

    def hedge2fface_degree(hedge):
        fface = ugraph_planar_embedding.hedge2fake_clockwise_fface[hedge]
        return ugraph_planar_embedding.fface2degree[fface]
    def hedge2fvertex_degree(hedge):
        fvertex = ugraph_planar_embedding.hedge2fvertex[hedge]
        return ugraph_planar_embedding.fvertex2degree[fvertex]
    def hedge2class_data__func(hedge):
        other = ugraph_planar_embedding.hedge2another_hedge(hedge)
        return  (hedge2fvertex_degree(hedge)
                ,hedge2fvertex_degree(other)
                ,hedge2fface_degree(hedge)
                ,hedge2fface_degree(other)
                ,hedge2hweight[hedge]
                ,hedge2hweight[other]
                )

    hedge2class_data = tuple(map(hedge2class_data__func
        , range(ugraph_planar_embedding.num_hedges)))

    fvertex_degree_UB = 1+max(ugraph_planar_embedding.fvertex2degree, default=-1)
    fface_degree_UB = 1+max(ugraph_planar_embedding.fface2degree, default=-1)

    alphabet_sizes = (fvertex_degree_UB, fvertex_degree_UB, fface_degree_UB, fface_degree_UB, num_hweights, num_hweights)
    table = tuple([] for _ in range(max(alphabet_sizes)))
    num_hedges = ugraph_planar_embedding.num_hedges
    key = hedge2class_data.__getitem__

    sorted_hedges = radix_sort_with_table(alphabet_sizes, range(num_hedges), table, key=key)

    (hedge2group_idx, group_idx2key, group_idx2size
    ) = make_compact_uint2group_idx(num_hedges, sorted_hedges, key=key)

    hedge2class_idx = hedge2group_idx
    class_idx2size = group_idx2size
    return hedge2class_idx, class_idx2size, sorted_hedges




