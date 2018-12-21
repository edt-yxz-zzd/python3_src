'''
fail to make_case_2_result
    now change to [ver4]
    but the [[fface]] part is fine
        later I may split out this part
'''

'''
see:
    "planar/algo - is fake_embedding relax_planar[ver3].txt"
    "def - 3.3. relax biconnected.txt"
    "def - 3.4. simple clockwise path cycle.txt"



frontier fverties: A-arc1->B-arc2->C-arc3->D-arc4->A
fverties of two cross outer paths: A-arc5->C, B-arc6->D
==>> non_relax_planar condition:
    bug: path from outside to inside
        cycle: A-arc1->B-arc6->D-arc4->A
        path: A-arc5->C-arc3->D
    correct:
        cycle: A-arc5->C-arc3->D-arc4->A
        path: A-arc1->B-arc6->D

      -----arc5->
     /           |
    A -arc1-> B ----
    ^         |  |  |
    |         |  |  |
    arc4    arc2 |  arc6
    |         |  |  |
    |         v  |  |
    D <-arc3- C-/   |
     \----------<---
'''

__all__ = '''
    is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex
    '''.split()

from .detect_ABAB import detect_ABAB
from ..iter_cycle_from import iter_cycle_from
from ..UGraphFakeEmbedding import UGraphFakeEmbedding

from itertools import chain
from seed.types.OneTime import OneTimeSet, OneTimeMap
from seed.tiny import print_err
#hedge2iter_fake_counterclockwise_hedges_around_fface

def is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex(*
    ,relax_biconnected_ugraph_fake_embedding
    ,hedge2fake_counterclockwise_fface
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
    (0, [[fface]]) | (1, (fface, fvertex)) | (2, (simple_cycle_hedges1, simple_path_hedges1))
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

        (2, (simple_cycle_hedges1, simple_path_hedges1))
            non_relax_planar
            simple_cycle_hedges1 and simple_path_hedges1 are simple&nonempty
                simple_path_hedges1 may be a cycle
            when treat them as clockwise cycle/path:
                simple_path_hedges1 begin inside&on simple_cycle_hedges1
                simple_path_hedges1 end outside&on simple_cycle_hedges1

'''
    assert isinstance(relax_biconnected_ugraph_fake_embedding, UGraphFakeEmbedding)
    return _calc(relax_biconnected_ugraph_fake_embedding
                ,hedge2fake_counterclockwise_fface).calc_main()
    print_err(f'relax_biconnected_ugraph_fake_embedding={relax_biconnected_ugraph_fake_embedding}')
    print_err(f'hedge2fake_counterclockwise_fface={hedge2fake_counterclockwise_fface}')

class _calc:
    '''
ffacess

fvertex2is_on_or_inside_frontier
fface2is_inside_frontier
fface2num_fvertices_on_or_inside_frontier
fface2num_outer_hedges_inside_frontier
fface2num_touch_noncycle_paths

updated_fface_set
next_fface_set






fvertex2is_on_or_inside_frontier :: [Bool]
fface2is_inside_frontier :: [Bool]
    #hedge2is_inside_frontier :: [Bool]
    #hedge2is_inside_frontier[h] == fface2is_inside_frontier[hedge2fake_clockwise_fface[h]]

fface2num_fvertices_on_or_inside_frontier :: [UInt]
fface2num_outer_hedges_inside_frontier :: [UInt]
    # fface's inner hedges are clockwise
    # outer hedges are another_hedges of inner hedges

# num_noncycle_paths = numFV-numOH
#   no matter whether [form a cycle] or [form many0 noncycle paths]
fface2num_touch_noncycle_paths :: [UInt]

updated_fface_set :: OneTimeSet
next_fface_set :: OneTimeSet
    s.t. [not is_inside_frontier][num_noncycle_paths <= 1][numOH >= 1]
    each time merge a fface into frontier:
        1)  update fface2is_inside_frontier
            update fvertex2is_on_or_inside_frontier

            update fface2num_fvertices_on_or_inside_frontier
            update fface2num_outer_hedges_inside_frontier
            update updated_fface_set
                record which ffaces are affected
        2) for affected ffaces:
            update fface2num_touch_noncycle_paths
            if s.t. the above condition
                add fface into next_fface_set
            else:
                discard fface from next_fface_set



'''
    def __getattr__(self, attr):
        return getattr(self.embedding, attr)
    def hedge2outer_fface(self, hedge):
        return self.hedge2fake_counterclockwise_fface[hedge]
    def __init__(self
        ,relax_biconnected_ugraph_fake_embedding
        ,hedge2fake_counterclockwise_fface
        ):
        self.embedding = relax_biconnected_ugraph_fake_embedding
        self.hedge2fake_counterclockwise_fface = hedge2fake_counterclockwise_fface


        self.ffacess = [] # case 0 output result

        self.fvertex2is_on_or_inside_frontier = [False]*self.num_fvertices
        self.fface2is_inside_frontier = [False]*self.num_ffaces
        self.fface2num_fvertices_on_or_inside_frontier = [0]*self.num_ffaces
        self.fface2num_outer_hedges_inside_frontier = [0]*self.num_ffaces
        self.fface2num_touch_noncycle_paths = [0]*self.num_ffaces

        self.updated_fface_set = OneTimeSet([None]*self.num_ffaces)
        self.next_fface_set = OneTimeSet([None]*self.num_ffaces)


    def calc_main(self):
        may_r = self.detect_duplicated_fvertex_in_fface()
        if may_r:
            r = may_r
        else:
            r = self.calc__if_no_duplicated_fvertex_per_fface()
        return r
    def calc__if_no_duplicated_fvertex_per_fface(self):
        # -> (0, ffacess)|(2, (simple_cycle_hedges1, simple_path_hedges1))
        for fface in range(self.num_ffaces):
            if self.fface2is_inside_frontier[fface]:
                continue
            self.start_new_connected_component_by_fface(fface)

            while self.next_fface_set:
                fface = self.next_fface_set.pop()

                n = self.fface2num_touch_noncycle_paths[fface]
                assert 0 <= n <= 1
                if n == 0:
                    self.end_connected_component_by_final_fface(fface)
                    break
                elif n == 1:
                    self.merge_fface_into_frontier(fface)
                else:
                    raise logic-error
            else:
                assert not self.next_fface_set
                return self.make_case_2_result()

        return (0, self.ffacess)

    def detect_duplicated_fvertex_in_fface(self):
        # -> () | (1, (fface, fvertex))
        # detect fface contain a fvertex twices
        fvertex2visited = self.fvertex2is_on_or_inside_frontier
        def clear(fface):
            for hedge in self.fface2iter_fake_clockwise_hedges(fface):
                fvertex = self.hedge2fvertex[hedge]
                fvertex2visited[fvertex] = False

        for fface in range(self.num_ffaces):
            for hedge in self.fface2iter_fake_clockwise_hedges(fface):
                fvertex = self.hedge2fvertex[hedge]
                if fvertex2visited[fvertex]:
                    # non_relax_planar
                    clear(fface)
                    return (1, (fface, fvertex))
                fvertex2visited[fvertex] = True

            clear(fface)
        return ()


    def start_new_connected_component_by_fface(self, fface):
        self.ffacess.append([])
        self.basic_merge_fface_into_frontier(fface)
    def end_connected_component_by_final_fface(self, fface):
        self.basic_merge_fface_into_frontier(fface)
        assert not self.next_fface_set
    def merge_fface_into_frontier(self, fface):
        self.basic_merge_fface_into_frontier(fface)
    def basic_merge_fface_into_frontier(self, fface):
        if self.fface2is_inside_frontier[fface]:
            raise logic-error
        self.fface2is_inside_frontier[fface] = True

        self.ffacess[-1].append(fface)
        self.updated_fface_set.clear()
        for hedge in self.fface2iter_fake_clockwise_hedges(fface):
            fvertex = self.hedge2fvertex[hedge]
            self.basic_visit_hedge(hedge)
            self.basic_visit_fvertex(fvertex)


        for fface in self.updated_fface_set:
            self.fface2num_touch_noncycle_paths[fface] = (
                self.fface2num_fvertices_on_or_inside_frontier[fface]
                - self.fface2num_outer_hedges_inside_frontier[fface]
                )

        #[not is_inside_frontier][num_noncycle_paths <= 1][numOH >= 1]
        for fface in self.updated_fface_set:
            if (not self.fface2is_inside_frontier[fface]
                and self.fface2num_touch_noncycle_paths[fface] <= 1
                and self.fface2num_outer_hedges_inside_frontier[fface] >= 1
                ):
                self.next_fface_set.add(fface)
            else:
                self.next_fface_set.discard(fface)

    def basic_visit_hedge(self, hedge):
        # visit only once
        outer_fface = self.hedge2outer_fface(hedge)
        self.fface2num_outer_hedges_inside_frontier[outer_fface] += 1
        self.updated_fface_set.add(outer_fface)
    def basic_visit_fvertex(self, fvertex):
        # visit many times2
        if self.fvertex2is_on_or_inside_frontier[fvertex]:
            return
        self.fvertex2is_on_or_inside_frontier[fvertex] = True

        for hedge in self.fvertex2iter_fake_clockwise_hedges(fvertex):
            fface = self.hedge2fake_clockwise_fface[hedge]
            self.fface2num_fvertices_on_or_inside_frontier[fface] += 1
            self.updated_fface_set.add(fface)

    def make_case_2_result(self):
        assert self.ffacess
        assert self.ffacess[-1]
        assert not self.next_fface_set
        frontier_hedges = tuple(self.iter_frontier_hedges())
        assert frontier_hedges # otherwise should success

        '''
        # onffaces = outer ffaces that touch frontier_hedges
        # onfface_block_pairs # [(fface, [hedge])]
        onfface_block_pairs = self.group_cycle_into_outer_fface_block_pairs(frontier_hedges)
        for fface, _ in onfface_block_pairs:
            assert self.fface2num_touch_noncycle_paths[fface] >= 2
        if not len(onfface_block_pairs) >= 2:
            raise logic-error
        '''

        outer_ffaces_per_angle = []
        fvertices_per_angle = []
        hedges_per_angle = []
        bound_hedges_per_angle = [] # all on frontier_hedges, duplicates
        prev_hedge = frontier_hedges[-1]
        for hedge in frontier_hedges:
            other = self.hedge2another_hedge(prev_hedge)
            prev_hedge = hedge

            fvertex = self.hedge2fvertex[other]
            assert fvertex == self.hedge2fvertex[hedge]
            #bug:for other in self.hedge2iter_fake_clockwise_hedges_around_fface(other):
            for other in self.hedge2iter_fake_clockwise_hedges_around_vertex(other):
                if other == hedge: break
                outer_fface = self.hedge2fake_clockwise_fface[other]
                outer_ffaces_per_angle.append(outer_fface)
                fvertices_per_angle.append(fvertex)
                hedges_per_angle.append(other)
                bound_hedges_per_angle.append(hedge)

        #detect ABAB
        buffer__fface2XXX = OneTimeMap([None]*self.num_ffaces)
        a, b, c, d = detect_ABAB(outer_ffaces_per_angle, buffer__fface2XXX)
        assert outer_ffaces_per_angle[a] == outer_ffaces_per_angle[c]
        assert outer_ffaces_per_angle[b] == outer_ffaces_per_angle[d]
        assert outer_ffaces_per_angle[a] != outer_ffaces_per_angle[b]
        A = fvertices_per_angle[a]
        B = fvertices_per_angle[b]
        C = fvertices_per_angle[c]
        D = fvertices_per_angle[d]


        paths = []
        for begin_idx, end_idx in [(c,a), (d,b)]:
            begin_hedge = hedges_per_angle[begin_idx]
            endpass1_hedge = hedges_per_angle[end_idx]
            path = self.make_clockwise_path_of_fface(begin_hedge, endpass1_hedge)
            path = self.reverse_path(path)
            paths.append(path)

        # split frontier_hedges by a,b,c,d
        four_hedges = [bound_hedges_per_angle[idx] for idx in (a,b,c,d)]
        four_idc_on_frontier = []
        i = 0
        for hedge in four_hedges:
            i = frontier_hedges.index(hedge, i)
            four_idc_on_frontier.append(i)
            # should not i += 1 !!!!
            # len(set(four_idc_on_frontier)) <= 4

        a, b, c, d = four_idc_on_frontier
        arc1 = frontier_hedges[a:b]
        arc2 = frontier_hedges[b:c]
        arc3 = frontier_hedges[c:d]
        arc4 = frontier_hedges[d:] + frontier_hedges[:a]
        arc5, arc6 = paths

        A1,B1 = self.path2ends(arc1, A)
        B2,C2 = self.path2ends(arc2, B)
        C3,D3 = self.path2ends(arc3, C)
        D4,A4 = self.path2ends(arc4, D)
        A5,C5 = self.nonemtpy_path2ends(arc5)
        B6,D6 = self.nonemtpy_path2ends(arc6)
        #from seed.tiny import print_err
        #print_err(A1, A4, A5)

        '''
        d = dict(locals())
        for key, value in sorted(d.items()):
            if key[0] in 'ABCD':
                print_err(key, value)
        '''
        d = dict(locals())
        for key, value in sorted(d.items()):
            if key.startswith('arc'):
                print_err(key, value)

        assert A5 == A4 == A1 == A
        assert B6 == B2 == B1 == B
        assert C5 == C3 == C2 == C
        assert D6 == D4 == D3 == D

        #bug:
            #cycle: A-arc1->B-arc6->D-arc4->A
            #path: A-arc5->C-arc3->D
        #cycle: A-arc5->C-arc3->D-arc4->A
        #path: A-arc1->B-arc6->D

        cycle = tuple(chain(arc5, arc3, arc4))
        path = tuple(chain(arc1, arc6))
        return (2, (cycle, path))

    def path2ends(self, path, end):
        if not path:
            return (end, end)
        return self.nonemtpy_path2ends(path)
    def nonemtpy_path2ends(self, path):
        assert path
        first_hedge = path[0]
        last_hedge = path[-1]
        begin_fvertex = self.hedge2fvertex[first_hedge]
        end_fvertex = self.hedge2fvertex[self.hedge2another_hedge(last_hedge)]
        return begin_fvertex, end_fvertex
    def reverse_path(self, path):
        return tuple(map(self.hedge2another_hedge, reversed(path)))
    def make_clockwise_path_of_fface(self, begin_hedge, endpass1_hedge):
        return tuple(self.iter_clockwise_path_of_fface(begin_hedge, endpass1_hedge))
    def iter_clockwise_path_of_fface(self, begin_hedge, endpass1_hedge):
        assert self.hedge2fake_clockwise_fface[begin_hedge] == self.hedge2fake_clockwise_fface[endpass1_hedge]
        assert begin_hedge != endpass1_hedge
        for hedge in self.hedge2iter_fake_clockwise_hedges_around_fface(begin_hedge):
            if hedge == endpass1_hedge:
                return
            yield hedge

    def group_cycle_into_outer_fface_block_pairs(self, cycle):
        # Iter hedge -> [(outer_fface, [hedge])]
        #assert cycle

        outer_fface_block_pairs = []
        prev_fface = -1 # not a fface
        for hedge in cycle:
            fface = self.hedge2outer_fface(hedge)
            if fface == prev_fface:
                outer_fface_block_pairs[-1][1].append(hedge)
            else:
                outer_fface_block_pairs.append((fface, [hedge]))
                prev_fface = fface
        if prev_fface == -1:
            raise error-cycle is empty

        if len(outer_fface_block_pairs) >= 2:
            first_fface = outer_fface_block_pairs[0][0]
            last_fface = outer_fface_block_pairs[-1][0]
            if first_fface == last_fface:
                last_pair = outer_fface_block_pairs.pop()
                last_pair[1].extend(outer_fface_block_pairs[0][1])
                outer_fface_block_pairs[0] = last_pair
        return outer_fface_block_pairs

    def is_hedge_on_frontier_cycle(self, hedge):
        inner_fface = self.hedge2fake_clockwise_fface[hedge]
        outer_fface = self.hedge2outer_fface(hedge)
        return (self.fface2is_inside_frontier[inner_fface]
            and not self.fface2is_inside_frontier[outer_fface]
            )
    def iter_frontier_hedges(self):
        may_hedge = self.iter_frontier_hedges__part1__may_find_arbitray_hedge_on()
        if may_hedge is None:
            # frontier_hedges is empty
            return
            yield
        hedge = may_hedge
        assert self.is_hedge_on_frontier_cycle(hedge)

        hedge0 = hedge
        yield hedge
        while True:
            hedge = self.hedge2fake_clockwise_next_hedge_around_fface[hedge]
            #bug:for hedge in self.hedge2iter_fake_counterclockwise_hedges_around_fface(hedge):
            #bug:for hedge in self.hedge2iter_fake_clockwise_hedges_around_fface(hedge):
            for hedge in self.hedge2iter_fake_clockwise_hedges_around_vertex(hedge):
                if self.is_hedge_on_frontier_cycle(hedge):
                    break
            else:
                raise logic-error

            if hedge == hedge0:
                break
            yield hedge


    def iter_frontier_hedges__part1__may_find_arbitray_hedge_on(self):
        for fface, num in enumerate(self.fface2num_touch_noncycle_paths):
            if num == 0:
                # ==>> inside or (outer but not touch)
                # <<=xx= inside or (outer but not touch)
                continue

            b = bool(self.fface2is_inside_frontier[fface])
            for hedge in self.fface2iter_fake_clockwise_hedges(fface):
                outer_fface = self.hedge2outer_fface(hedge)
                if bool(self.fface2is_inside_frontier[outer_fface]) != b:
                    if b:
                        # fface inside frontier
                        return hedge
                    else:
                        # fface outside frontier
                        return self.hedge2another_hedge(hedge)
        return None



