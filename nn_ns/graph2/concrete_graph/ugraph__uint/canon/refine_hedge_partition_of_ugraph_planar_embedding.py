
r'''
refine_hedge_partition_of_ugraph_planar_embedding

'''

__all__ = '''
    refine_hedge_partition_of_ugraph_planar_embedding
    '''.split()

#from ..UIntBijectionBuilder import UIntBijectionBuilder
#from ..inverse_uint_bijection import inverse_uint_bijection
from ..is_uint_bijection import is_uint_bijection
from ..UGraphFakeEmbedding import UGraphFakeEmbedding
#from ..UGraphFakeEmbeddingLabelling import UGraphFakeEmbeddingLabelling
#from ..is_uint_sequence import is_uint_sequence
from seed.types.OneTime import OneTimeMap, OneTimeSet
from seed.math.floor_ceil import floor_log2
from itertools import groupby



def refine_hedge_partition_of_ugraph_planar_embedding(*
    ,ugraph_planar_embedding
    ,position2hedge
    ,hedge2position
    ,hedge2class_idx
    ,class_idx2begin
    ,class_idx2end
    ):
    '''

input:
    ugraph_planar_embedding :: UGraphFakeEmbedding
    position2hedge :: [HEdge]
    hedge2position :: [Position]
    hedge2class_idx :: [ClassIdx]
    class_idx2begin :: [Position]
    class_idx2end :: [Position]
        HEdge = UInt
        Position = UInt
        ClassIdx = UInt
        # class - hedge equivalence class
        all input except ugraph_planar_embedding are mutable and will be modified inplace

        * hedge2class_idx
            initial partition in canon form = hedge2class_idx
        * position2hedge/class_idx2begin/class_idx2end
            initial partition in mutable grouped form = position2hedge + class_idx2begin + class_idx2end
            initial num_classes = len(class_idx2begin) = len(class_idx2end)
        * hedge2position
            is_uint_bijection(position2hedge, hedge2position)
output:
    hedge_classes :: [[HEdge]]
        # partition in immutable grouped form


#################################################
refine_hedge_partition_of_ugraph_planar_embedding

partition distinguishable_hedges; O(E*log(E))
ref:
    "[planar_graph][triconnected][isomorphism][1973]A V log V algorithm for isomorphism of triconnected planar graphs[good].pdf"
        # but in this_func, neednot triconnected
        #   requires: planar
        #   #neednot triconnected/connected/rigid_connected


'''
    return Partition(
        ugraph_planar_embedding=ugraph_planar_embedding
        ,position2hedge=position2hedge
        ,hedge2position=hedge2position
        ,hedge2class_idx=hedge2class_idx
        ,class_idx2begin=class_idx2begin
        ,class_idx2end=class_idx2end
        ).main()

class Partition:
    def __init__(self, *
        ,ugraph_planar_embedding
        ,position2hedge
        ,hedge2position
        ,hedge2class_idx
        ,class_idx2begin
        ,class_idx2end
        ):
        #assert type(ugraph_planar_embedding) is UGraphFakeEmbedding
        assert isinstance(ugraph_planar_embedding, UGraphFakeEmbedding)
        assert type(position2hedge) is list
        assert type(hedge2position) is list
        assert type(hedge2class_idx) is list
        assert type(class_idx2begin) is list
        assert type(class_idx2end) is list
        if not ugraph_planar_embedding.calc.is_ugraph_fake_embedding_planar: raise ValueError

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
        return tuple(hedge_classes)

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




