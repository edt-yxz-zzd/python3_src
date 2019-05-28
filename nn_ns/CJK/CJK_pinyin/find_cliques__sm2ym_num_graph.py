
__all__ = '''
    iter_find_cliques__sm2ym_num_graph
    '''.split()

from .sm2ym_num_graph__for_good_hanzis import sm2ym_num_graph__for_good_hanzis
import networkx # find_cliques
import itertools # chain
from seed.for_libs.raw_input import raw_input__echo


def make_complete_graph(iter_vertices, create_using=None):
    idx2vertices = dict(enumerate(iter_vertices))
    n = len(idx2vertices)
    G = networkx.complete_graph(n, create_using=create_using)
    H = networkx.relabel_nodes(G, idx2vertices)
    return H

def iter_find_cliques__sm2ym_num_graph(sm2ym_num_graph, sm_remove_h, ym_remove_g):
    # -> Iter (sm_vertex_set, ym_vertex_set)
    sm_vertices = set(sm2ym_num_graph.keys())
    ym_vertices = set(itertools.chain.from_iterable(sm2ym_num_graph.values()))
    assert not (sm_vertices & ym_vertices)


    G = networkx.from_dict_of_lists(sm2ym_num_graph)
    def std_ym(ym):
        assert '0' <= ym[-1] <= '9'
        if ym[-2] == 'g':
            n = -2
        else:
            n = -1
        return ym[:n]
    def std_sm(sm):
        if len(sm) == 2:
            assert sm[-1] == 'h'
            r = sm[:-1]
        else:
            r = sm
        assert len(r) == 1
        return r
    def add_xm(xm_vertices, std_xm):
        for xm1 in xm_vertices:
            std_xm1 = std_xm(xm1)
            for xm2 in xm_vertices:
                std_xm2 = std_xm(xm2)
                if std_xm1 == std_xm2: continue
                if xm1 < xm2:
                    G.add_edge(xm1, xm2)
    if sm_remove_h:
        add_xm(sm_vertices, std_sm)
    else:
        SM = make_complete_graph(sm_vertices)
        G.add_edges_from(SM.edges())
    if ym_remove_g:
        add_xm(ym_vertices, std_ym)
    else:
        YM = make_complete_graph(ym_vertices)
        G.add_edges_from(YM.edges())

    it = networkx.find_cliques(G)
    for vertices in it:
        vertex_set = set(vertices)
        sm_vertex_set = vertex_set & sm_vertices
        ym_vertex_set = vertex_set & ym_vertices
        assert sm_vertex_set | ym_vertex_set == vertex_set
        assert len(sm_vertex_set) + len(ym_vertex_set) == len(vertex_set)

        yield sm_vertex_set, ym_vertex_set

def main(args=None):
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description=f'find_cliques from sm2ym_num_graph'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-s', '--sm_remove_h', action='store_true'
                        , default = False
                        , help='sm_remove_h: e.g. treat z/zh the same')
    parser.add_argument('-y', '--ym_remove_g', action='store_true'
                        , default = False
                        , help='ym_remove_g: e.g. treat an/ang the same')
    parser.add_argument('-q', '--quiet', action='store_true'
                        , default = False
                        , help='quiet: e.g. not ask when success')

    args = parser.parse_args(args)
    quiet = args.quiet
    it = iter_find_cliques__sm2ym_num_graph(
        sm2ym_num_graph__for_good_hanzis
        ,sm_remove_h = args.sm_remove_h
        ,ym_remove_g = args.ym_remove_g
        )
    for sm_vertex_set, ym_vertex_set in it:
        if len(sm_vertex_set) >= 8 <= len(ym_vertex_set):
            print('=====')
            print(f'{len(sm_vertex_set)}, {sorted(sm_vertex_set)}')
            print(f'{len(ym_vertex_set)}, {sorted(ym_vertex_set)}')
            sys.stdout.flush()

            if not quiet:
                prompt = '(input "n" to quit)>>>'
                user_input = raw_input__echo(prompt)
                if user_input == 'n': break
if __name__ == '__main__':
    main()



