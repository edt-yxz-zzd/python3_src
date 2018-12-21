'''
see:
    "planar/algo - is fake_embedding relax_planar[ver2].txt"
    "def - relax biconnected.txt"
'''


__all__ = '''
    is_ugraph_fake_embedding_relax_planar
    '''.split()
from ..iter_cycle_from import iter_cycle_from
from ..UGraphFakeEmbedding import UGraphFakeEmbedding
from .ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex import\
    ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex

from seed.iters.group_by import group_by
from seed.tiny import snd
from seed.verify.common_verify import (
    is_UInt, is_Sequence, is_tuple
    #is_int, is_UInt, is_pair, is_tuple
    )
from seed.helper.repr_input import repr_helper_ex


def new_path2old_path(hedges):
    '''[new_HXY] -> [old_hedge]
convert back to original hedges
    HPM/HNM -> old hedges
        HPM -> HPM//6
        HNM -> HNM//6
    remove other HXY
'''
    for hedge in hedges:
        q,r = divmod(hedge, 6)
        if r in (1,4):
            hedge = q
            yield hedge


def is_tuple_of_UInt(obj):
    return is_tuple.of(obj, is_UInt)
def is_tuple_of_UInt_lt(obj, upper_bound):
    return is_tuple_of_UInt(obj) and max(obj, default=upper_bound-1) < upper_bound
def is_hedges1(num_hedges, obj):
    return is_tuple_of_UInt_lt(obj, num_hedges) and len(obj) >= 1
def is_connected(ugraph_fake_embedding, hedge_before, hedge_after):
    fvertex0 = ugraph_fake_embedding.hedge2fvertex[ugraph_fake_embedding.hedge2another_hedge(hedge_before)]
    fvertex1 = ugraph_fake_embedding.hedge2fvertex[hedge_after]
    return fvertex1 == fvertex0
def is_path_hedges1(ugraph_fake_embedding, hedges):
    return (is_hedges1(ugraph_fake_embedding.num_hedges, hedges)
        and all(is_connected(ugraph_fake_embedding, hedges[i-1], hedges[i]) for i in range(1, len(hedges)))
        )
def is_path_hedges1__without_crossing(ugraph_fake_embedding, hedges):
    if not is_path_hedges1(ugraph_fake_embedding, hedges):
        return False
    fvertices = set(ugraph_fake_embedding.hedge2fvertex[hedge] for hedge in hedges)
    if len(fvertices) != len(hedges):
        return False

    begin_fvertex = ugraph_fake_embedding.hedge2fvertex[hedges[0]]
    end_fvertex = ugraph_fake_embedding.hedge2fvertex[ugraph_fake_embedding.hedge2another_hedge(hedges[-1])]
    return end_fvertex == begin_fvertex or end_fvertex not in fvertices
def is_cycle_hedges1__without_crossing(ugraph_fake_embedding, hedges):
    if not is_path_hedges1__without_crossing(ugraph_fake_embedding, hedges):
        return False
    begin_fvertex = ugraph_fake_embedding.hedge2fvertex[hedges[0]]
    end_fvertex = ugraph_fake_embedding.hedge2fvertex[ugraph_fake_embedding.hedge2another_hedge(hedges[-1])]
    return begin_fvertex == end_fvertex

def hedges_are_in_clockwise_around_vertex(ugraph_fake_embedding, hedges):
    hedges = tuple(hedges)
    if len(hedges) <= 1: return True

    fvertices = tuple(ugraph_fake_embedding.hedge2fvertex[hedge] for hedge in hedges)
    if not all(fvertices[0] == fvertex for fvertex in fvertices):
        raise logic-error

    hedges__set = set(hedges)
    f = ugraph_fake_embedding.hedge2iter_fake_clockwise_hedges_around_vertex
    hedges__tuple = tuple(hedge for hedge in f(hedges[0]) if hedge in hedges__set)
    return hedges == hedges__tuple

def verify_non_relax_planar_condition(
    ugraph_fake_embedding, cycle_hedges1, path_hedges1
    ):
    '''verify result from is_ugraph_fake_embedding_relax_planar_ex
    verify non_relax_planar_condition
'''
    if not (is_cycle_hedges1__without_crossing(cycle_hedges1)
        and is_path_hedges1__without_crossing(path_hedges1)
        ):
        return False


    begin_fvertex = ugraph_fake_embedding.hedge2fvertex[path_hedges1[0]]
    end_fvertex = ugraph_fake_embedding.hedge2fvertex[ugraph_fake_embedding.hedge2another_hedge(path_hedges1[-1])]

    fvertices = tuple(ugraph_fake_embedding.hedge2fvertex[hedge] for hedge in cycle_hedges1)
    i = fvertices.index(begin_fvertex)
    j = fvertices.index(end_fvertex)

    hedge2another_hedge = ugraph_fake_embedding.hedge2another_hedge
    clockwise_hedgess = [(cycle_hedges1[i]
                        , path_hedges1[0]
                        , hedge2another_hedge(cycle_hedges1[i-1])
                        )#inner
                        ,(cycle_hedges1[j]
                        , hedge2another_hedge(cycle_hedges1[j-1])
                        , hedge2another_hedge(path_hedges1[-1])
                        )
                        ]
    return all(map(hedges_are_in_clockwise_around_vertex, clockwise_hedgess))


def is_ugraph_fake_embedding_relax_planar_ex(*
    ,ugraph_fake_embedding, hedge2aedge
    ):
    '''
input:
    ugraph_fake_embedding :: UGraphFakeEmbedding
    hedge2aedge
        if no ugraph on hand:
            see: .make_hedge2fake_aedge
output:
    () | (cycle_hedges1, path_hedges1)
        ()
            relax_planar
        (cycle_hedges1, path_hedges1)
            non-relax_planar
            when treat cycle_hedges1 as clockwise cycle:
                path_hedges1 begin inside&on cycle_hedges1
                path_hedges1 end outside&on cycle_hedges1
'''
    #assert isinstance(ugraph_fake_embedding, UGraphFakeEmbedding)
    (ugraph_fake_embedding__new, hedge2aedge__new
    ) = ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex(
        ugraph_fake_embedding=ugraph_fake_embedding
        , hedge2aedge=hedge2aedge
        )

    (case, result
    ) = is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex(
            relax_biconnected_ugraph_fake_embedding
                = ugraph_fake_embedding__new
            )
    if case == 0:
        return ()
    elif case == 2:
        (cycle_hedges1, path_hedges1) = result
        assert verify_non_relax_planar_condition(
            ugraph_fake_embedding__new, cycle_hedges1, path_hedges1)

        # convert back to original hedges
        #   HPM/HNM -> old hedges
        #   remove other HXY
        cycle_hedges1 = new_path2old_path(cycle_hedges1)
        path_hedges1 = new_path2old_path(path_hedges1)

        assert verify_non_relax_planar_condition(
            ugraph_fake_embedding, cycle_hedges1, path_hedges1)
        return (cycle_hedges1, path_hedges1)
    elif case == 1:
        # ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex
        #   should no fface contain duplicated fvertex
        raise logic-error
    else:
        raise logic-error-unknown-case



def is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex(*,
    relax_biconnected_ugraph_fake_embedding
    ):
    '''is relax_biconnected-ugraph_fake_embedding relax_planar?

input:
    relax_biconnected_ugraph_fake_embedding
        # allow multiedge
        no self_loops
        vertex degree >= 2
        for each connected component cc:
            * cc is an isolated vertex
            OR:
            * cc is biconnected
                cc.num_vertices >= 2
                cc.num_aedges >= 2
output:
    (0, [[fface]]) | (1, (fface, fvertex)) | (2, (cycle_hedges1, path_hedges1))
        (0, [[fface]])
            relax_planar
            ffaces per connected component except isolated vertex
                ffaces is nonempty
                when merge ffaces in-order, the middle temp graphs are biconnected too
                    i.e. avoid merge fface touch frontier_hedges exactly once
                touch(frontier_hedges, fface) = [(start_vertex, max_common_path_hedges0)]

        (1, (fface, fvertex))
            non_relax_planar
            fface which visited a fvertex twices

        (2, (cycle_hedges1, path_hedges1))
            non_relax_planar
            when treat cycle_hedges1 as clockwise cycle:
                path_hedges1 begin inside&on cycle_hedges1
                path_hedges1 end outside&on cycle_hedges1

'''
    return _calc(relax_biconnected_ugraph_fake_embedding).calc()



class NonRelaxPlanarError(Exception):pass
class _NonRelaxPlanarError(NonRelaxPlanarError):
    '''
outer_fface in rstack
fface == hedge2outer_fface(block_reprs[-1])
hedge is the first forbidden hedge in fface2anothers_of_forbidden_hedges[fface]
'''
    attrs = '''
        outer_fface
        fface

        nonfirst_block_repr
        first_block_repr
        forbidden_hedge
        '''.split()
    def __init__(self, *, outer_fface, fface
        ,nonfirst_block_repr = None
        ,first_block_repr = None
        ,forbidden_hedge = None
        )
        super().__init__()

        assert fface != outer_fface
        self.outer_fface = outer_fface
        self.fface = fface

        assert sum([first_block_repr is None, nonfirst_block_repr is None, forbidden_hedge is None]) == 1
        self.nonfirst_block_repr = nonfirst_block_repr
        self.first_block_repr = first_block_repr
        self.forbidden_hedge = forbidden_hedge

    def __repr__(self):
        return repr_helper_ex(self, (), __class__.attrs, {}, ordered_attrs_only=True)


class _calc:
    '''

# clockwise to distinguish outer or inner
#   for both cycle or path!
frontier_hedges :: [hedge]
    a clockwise cycle
    v0-[h0]-><-[]-v1-[h1]-><-[]-v2...
    h1 maynot be hedge2fake_clockwise_next_hedge_around_fface[h0]
block :: nonempty[hedge]
    a clockwise path # NOTE: outer/inner
    a block on a circle is a max path that collect same outer fface
    * block on frontier_hedges
    * block on outer fface that touch frontier_hedges by aedges
block_repr :: hedge
    #block_repr of block
    = block[0]
start_hedge :: hedge
    #start_hedge of block
    block_repr on frontier_hedges
    start_hedge on outer fface
    start_hedge = hedge2fake_clockwise_prev_hedge_around_vertex[block_repr]
touch :: [fvertex-on-frontier or flip(block-on-frontier)]
    outer fface touch frontier
rstack :: [fface]
    we try to merge block_reprs[-1] into frontier
    but some times fail:
        iff len(touch) >= 2
    then we push hedge2outer_fface(block_reprs.pop()) into rstack
    later when we meet hedge2outer_fface(block_reprs[-1]) == rstack[-1]
        we pop rstack iff block_repr2start_hedge(block_reprs[-1]) == hedge2another_hedge[fface2anothers_of_forbidden_hedges[rstack[-1]][0]] == fface2maybe_expected_start_hedge[rstack[-1]]
        otherwise pop block_reprs
fface2anothers_of_forbidden_hedges :: [[hedge]]
    hs = fface2anothers_of_forbidden_hedges[ff]
        if hs is not empty, hs is a clockwise path of which ff is the inner fface
        we will forbidden hedge2another_hedge[h] for h <- hs

    when we push fface into rstack:
        assert block_reprs[-1] is a touch of fface and frontier
        eval the external blocks of fface
            s.t. no fvertex except end-fvertex are on frontier
        before we unlock forbidden_hedges, any fface to be merged touch them will make up non_planar condition
            (frontier cycle
            ,fface which set frontier_hedges
            ,fface to be merged, which touch a frontier_hedge
            )

_hedge2is_forbidden :: [Bool]
    _hedge2is_forbidden[h] =[def]= hedge2another_hedge[h] in chain(fface2anothers_of_forbidden_hedges)

'''
    def __init__(self, relax_biconnected_ugraph_fake_embedding):
        self.embedding = relax_biconnected_ugraph_fake_embedding
        self.__hedge2outer_fface__array = tuple(
            map(self.__hedge2outer_fface__func, range(self.num_hedges)))


        self.ffacess = []
        self.fface2visited = [False]*self.num_ffaces
        self.fvertex2on_or_inside_frontier = [False]*self.num_fvertices
            # or in other connected component

        self._hedge2is_forbidden = [False]*self.num_hedges
        self.fface2anothers_of_forbidden_hedges = [[] for _ in range(self.num_ffaces)]
        #fface2maybe_expected_start_hedge = [None]*num_ffaces
            # fface2maybe_expected_start_hedge[h] = fface2anothers_of_forbidden_hedges[h][0]
            # when the fface push into rstack
            #   remember the start_hedge
            #   we will meet fface again and again:
            #   when we meet fface with start_hedge, pop it from rstack
        self.rstack = [] # :: [fface]
            # "r" means reverse stack; right stack
            # with fface2maybe_expected_start_hedge/fface2anothers_of_forbidden_hedges

        self.block_reprs = []
            # frontier <<== block_reprs+rstack+fface2maybe_expected_start_hedge
            # block_reprs :: [hedge]
            # rstack :: [fface]

        self.outer_fface0 = None
        #self.outer_fface0 = self.hedge2outer_fface(self.block_reprs[0]):

    def __getattr__(self, attr):
        return getattr(self.embedding, attr)
    def hedge2outer_fface(self, hedge):
        return self.__hedge2outer_fface__array[hedge]
    def __hedge2outer_fface__func(self, hedge):
        return self.embedding.hedge2fake_clockwise_fface[
            self.embedding.hedge2fake_clockwise_prev_hedge_around_vertex[hedge]]
        return self.embedding.hedge2fake_clockwise_fface[self.embedding.hedge2another_hedge(hedge)]



    '''
    ###################
    num_hedges = embedding.num_hedges
    num_fvertices = embedding.num_fvertices
    num_ffaces = embedding.num_ffaces

    hedge2fvertex = embedding.hedge2fvertex
    hedge2another_hedge = embedding.hedge2another_hedge
    hedge2fake_clockwise_fface = embedding.hedge2fake_clockwise_fface
    hedge2fake_clockwise_next_hedge_around_fface = \
        embedding.hedge2fake_clockwise_next_hedge_around_fface
    hedge2fake_clockwise_prev_hedge_around_vertex = \
        embedding.hedge2fake_clockwise_prev_hedge_around_vertex
    fface2iter_fake_clockwise_hedges = \
        embedding.fface2iter_fake_clockwise_hedges
    hedge2iter_fake_clockwise_hedges_around_fface = \
        embedding.hedge2iter_fake_clockwise_hedges_around_fface

    '''


    def calc(self):
        try:
            return self._calc()
        except _NonRelaxPlanarError as e:
            return self.handle_error(e)
    def handle_error(self, e):
        '''
outer_fface in rstack
fface == hedge2outer_fface(block_reprs[-1])

####deprecated: hedge is the first forbidden hedge in fface2anothers_of_forbidden_hedges[fface]
'''
        outer_fface = e.outer_fface
        fface = e.fface
        #hedge = e.hedge
        assert not self.fface2visited[outer_fface]
        assert not self.fface2visited[fface]

        path_right = self.fface2anothers_of_forbidden_hedges[outer_fface]
        path_left = self.fface2anothers_of_forbidden_hedges[fface]
        assert path_right
        assert path_left

        block_reprs = self.block_reprs
        rstack = self.rstack
        from seed.tiny import print_err
        print_err(block_reprs)
        print_err(rstack)
        print_err(repr(e))
        for key, value in self.__dict__.items():
            print_err(f'{key} = {value!r}')

        assert outer_fface in rstack
        assert fface == self.hedge2outer_fface(block_reprs[-1])

        if e.forbidden_hedge is not None:
            hedge = e.forbidden_hedge
            i = path_left.index(hedge)
            assert self.is_hedge_forbidden(hedge)
            assert all(not self.is_hedge_forbidden(hedge) for hedge in path_left[:i])
            path_left_half = path_left[:i]
            del i, hedge

        frontier_hedges = self.iter_frontier_hedges()
        frontier_fvertices = tuple(self.hedge2fvertex[h] for h in frontier_hedges)

        fvertex2on_frontier_hedges = [False]*self.num_fvertices
        for fvertex in frontier_fvertices:
            fvertex2on_frontier_hedges[fvertex] = True

        def hedge_from_frontier_fvertex(hedge):
            return fvertex2on_frontier_hedges[self.hedge2fvertex[hedge]]
        def hedge_to_frontier_fvertex(hedge):
            return hedge_from_frontier_fvertex(self.hedge2another_hedge(hedge))
        def path_from_to_frontier_fvertex(path):
            return (hedge_from_frontier_fvertex(path[0])
                and hedge_to_frontier_fvertex(path[-1])
                )
        assert path_from_to_frontier_fvertex(path_left)
        assert path_from_to_frontier_fvertex(path_right)

        def path2ends(path):
            begin = self.hedge2fvertex[path[0]]
            end = self.hedge2fvertex[self.hedge2another_hedge(path[-1])]
            return begin, end
        def hedge_to_frontier_fvertex(hedge):
            return hedge_from_frontier_fvertex(self.hedge2another_hedge(hedge))

        path_left_begin, path_left_end = path2ends(path_left)
        path_right_begin, path_right_end = path2ends(path_right)
        i = frontier_fvertices.index(path_right_begin)
        j = frontier_fvertices.index(path_left_begin, i)
        k = frontier_fvertices.index(path_right_end, j)

        if e.forbidden_hedge is not None:
            cycle = chain(frontier_fvertices[:i], path_right, frontier_fvertices[k:])
            path = chain(frontier_fvertices[i:j], path_left_half)

        cycle = tuple(cycle)
        path = tuple(path)
        return (2, (cycle, path))


    def iter_frontier_hedges(self):
        it = self.__iter_frontier_hedges()
        for hedge in it:
            assert not self.fface2visited[self.hedge2outer_fface(hedge)]
            assert self.fface2visited[self.hedge2fake_clockwise_fface(hedge)]
        else:
            raise logic-error

        prev_hedge = hedge
        it = self.__iter_frontier_hedges()
        for hedge in it:
            assert self.hedge2fvertex[self.hedge2another_hedge(hedge)] == self.hedge2fvertex[hedge]

        return self.__iter_frontier_hedges()
    def __iter_frontier_hedges(self):
        for block_repr in self.block_reprs:
            break
        else:
            raise logic-error

        it = self.hedge2iter_fake_clockwise_hedges_around_fface(block_repr)
        for hedge in it:
            yield hedge
            break

        while True:
            # iter hedges of one block
            for hedge in it:
                if hedge == block_repr:
                    return
                if self.fface2visited[self.hedge2outer_fface(hedge)]:
                    break
                yield hedge

            # find next block_repr
            it = iter_cycle_from(self.hedge2fake_clockwise_prev_hedge_around_vertex, hedge)
            for hedge in it:
                if not self.fface2visited[self.hedge2outer_fface(hedge)]:
                    break
            it = self.hedge2iter_fake_clockwise_hedges_around_fface(hedge)


    def _calc(self):
        may_r = self.detect_duplicated_fvertex_in_fface()
        if not may_r:
            may_r = self.build_ffacess_by_grow_frontier_hedges__no_duplicated_fvertex_per_fface()

        if not may_r:
            raise logic-error

        r = may_r
        return r

    def detect_duplicated_fvertex_in_fface(self):
        # -> () | (1, (fface, fvertex))
        # detect fface contain a fvertex twices
        fvertex2visited = [False]*self.num_fvertices
        for fface in range(self.num_ffaces):
            for hedge in self.fface2iter_fake_clockwise_hedges(fface):
                fvertex = self.hedge2fvertex[hedge]
                if fvertex2visited[fvertex]:
                    # non_relax_planar
                    return (1, (fface, fvertex))
                fvertex2visited[fvertex] = True

            # clear
            for hedge in self.fface2iter_fake_clockwise_hedges(fface):
                fvertex = self.hedge2fvertex[hedge]
                fvertex2visited[fvertex] = False
        return ()


    def group_by(self, hedges):
        [*keyed_block_pairs] = group_by(hedges, key=self.hedge2outer_fface)
        [*block_reprs] = [hedges[0] for fface, hedges in keyed_block_pairs]
            # block_repr :: hedge # the first one in clockwise
        return block_reprs

    def build_ffacess_by_grow_frontier_hedges__no_duplicated_fvertex_per_fface(self):
        build_ffaces = self.build_ffaces_by_grow_frontier_hedges__no_duplicated_fvertex_per_fface
        for fface in range(self.num_ffaces):
            if self.fface2visited[fface]: continue

            #begin a new connected component
            self.ffacess.append([])
            self.basic_merge_fface(fface)

            block_reprs = self.group_by(self.fface2iter_fake_clockwise_hedges(fface))

            L = len(block_reprs)
            assert L
            if L >= 2 and self.hedge2outer_fface(block_reprs[-1]) == self.hedge2outer_fface(block_reprs[0]):
                last_block_repr = block_reprs.pop()
                block_reprs[0] = last_block_repr



            assert not self.block_reprs
            assert not self.rstack
            self.outer_fface0 = self.hedge2outer_fface(block_reprs[0])
            self.block_reprs__extend(block_reprs)
            build_ffaces()
        return (0, self.ffacess)

    def block_reprs__extend(self, block_reprs):
        block_reprs = list(block_reprs)
        for block_repr in block_reprs:
            assert self.fface2visited[self.hedge2fake_clockwise_fface[block_repr]]
            assert not self.fface2visited[self.hedge2outer_fface(block_repr)]

        self.block_reprs.extend(block_reprs)
        return

        for block_repr in block_reprs:
            start_hedge = self.block_repr2start_hedge(block_repr)
    def visit_fvertices_on_fface(self, fface):
        self.fface2visited[fface] = True
        it = self.fface2iter_fake_clockwise_hedges(fface)
        for hedge in it:
            fvertex = self.hedge2fvertex[hedge]
            # fvertex may be visited
            self.fvertex2on_or_inside_frontier[fvertex] = True
    def basic_merge_fface(self, fface):
        self.visit_fvertices_on_fface(fface)
        self.ffacess[-1].append(fface)




    def block_repr2start_hedge(self, block_repr):
        start_hedge = self.hedge2fake_clockwise_prev_hedge_around_vertex[block_repr]
        return start_hedge

    def fface2maybe_expected_start_hedge(self, fface):
        hedges = self.fface2anothers_of_forbidden_hedges[fface]
        return hedges[0] if hedges else None
    def is_hedge_forbidden(self, hedge):
        return (not self.fface2visited[self.hedge2outer_fface(hedge)]
            and self._hedge2is_forbidden[hedge]
            )

    def calc_expected_start_hedge_of_last_block_on_frontier(self):
        # -> expected_start_hedge | raise _NonRelaxPlanarError(outer_fface, fface)
        #   verify anothers_of_forbidden_hedges are not forbidden
        #   update fface2anothers_of_forbidden_hedges
        #   update _hedge2is_forbidden
        if len(self.block_reprs) <= 1: raise logic-error

        hedge0 = self.block_reprs[-1]
        #fface = self.hedge2outer_fface(hedge0)
        other = self.hedge2another_hedge(hedge0)
        fface = self.hedge2fake_clockwise_fface[other]

        if self.fface2anothers_of_forbidden_hedges[fface]:
            assert self.rstack
            raise _NonRelaxPlanarError(outer_fface=fface, fface=self.rstack[-1], nonfirst_block_repr=hedge0)

        assert not self.fface2visited[fface]

        it = iter_cycle_from(self.hedge2fake_clockwise_prev_hedge_around_fface, other)
        assert iter(it) is it
        for hedge in it:
            if not self.fface2visited[self.hedge2outer_fface(hedge)]:
                break

        it = iter_cycle_from(self.hedge2fake_clockwise_prev_hedge_around_fface, hedge)
        anothers_of_forbidden_hedges = []
        for hedge in it:
            anothers_of_forbidden_hedges.append(hedge)
            if self.fvertex2on_or_inside_frontier[self.hedge2fvertex[hedge]]:
                break
        anothers_of_forbidden_hedges.reverse()

        # verify anothers_of_forbidden_hedges are not forbidden
        for other in anothers_of_forbidden_hedges:
            if self.is_hedge_forbidden(other):
                outer_fface = self.hedge2outer_fface(other)
                assert outer_fface != fface
                # non_relax_planar
                raise _NonRelaxPlanarError(
                    outer_fface=outer_fface, fface=fface, forbidden_hedge=other
                    )


        # update fface2anothers_of_forbidden_hedges
        self.fface2anothers_of_forbidden_hedges[fface] = anothers_of_forbidden_hedges

        # update _hedge2is_forbidden
        for other in anothers_of_forbidden_hedges:
            hedge = self.hedge2another_hedge(other)
            assert not self._hedge2is_forbidden[hedge]
            self._hedge2is_forbidden[hedge] = True # init once


        expected_start_hedge = anothers_of_forbidden_hedges[0]
        return expected_start_hedge


    def build_ffaces_by_grow_frontier_hedges__no_duplicated_fvertex_per_fface(self):
        # grow frontier_hedges
        #
        # frontier <<== block_reprs+rstack+fface2maybe_expected_start_hedge
        # block_reprs :: [hedge]
        # rstack :: [fface]

        assert not self.rstack # fface2maybe_expected_start_hedge
        assert self.block_reprs
        while True:
            assert self.block_reprs
            if len(self.block_reprs) == 1:
                block_repr = self.block_reprs.pop()
                fface = self.hedge2outer_fface(block_repr)
                if self.rstack: raise logic-error
                self.basic_merge_fface(fface)
                break

            expected_start_hedge = self.calc_expected_start_hedge_of_last_block_on_frontier()
            block_repr = self.block_reprs.pop()
            fface = self.hedge2outer_fface(block_repr)

            assert self.block_reprs
            start_hedge = self.block_repr2start_hedge(block_repr)
            if start_hedge == expected_start_hedge:
                self.merge_fface(fface)
            else:
                self.rstack.append(fface)

    def merge_fface(self, fface):
        assert self.block_reprs
        hedges = self.fface2anothers_of_forbidden_hedges[fface]
        self.basic_merge_fface(fface); del fface

        non_touch_block_reprs = self.group_by(hedges)

        first_block_repr = non_touch_block_reprs[0]
        first_fface = self.hedge2outer_fface(first_block_repr)
        i = int(self.hedge2outer_fface(self.block_reprs[-1]) == first_fface)
        assert 0 <= i <= 1
        self.block_reprs__extend(non_touch_block_reprs[i:])


        last_block_repr = self.block_reprs[-1]
        last_fface = self.hedge2outer_fface(last_block_repr)
        if self.rstack:
            if self.rstack[-1] == last_fface:
                expected_start_hedge = self.fface2maybe_expected_start_hedge(last_fface)
                assert expected_start_hedge is not None
                start_hedge = self.block_repr2start_hedge(last_block_repr)
                if start_hedge == expected_start_hedge:
                    self.rstack.pop()
                else:
                    self.block_reprs.pop()

            last_block_repr = self.block_reprs[-1]
            last_fface = self.hedge2outer_fface(last_block_repr)
            if last_fface == self.outer_fface0:
                assert self.rstack
                assert last_fface != self.rstack[-1]
                assert last_fface not in self.rstack
                self.calc_expected_start_hedge_of_last_block_on_frontier()
                raise _NonRelaxPlanarError(outer_fface=self.rstack[-1], fface=last_fface, first_block_repr = last_block_repr)

        elif len(self.block_reprs) >= 2:
            #assert not self.rstack
            if last_fface == self.outer_fface0:
                block_repr = self.block_reprs.pop()
                self.block_reprs[0] = block_repr
        return




