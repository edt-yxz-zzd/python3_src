
'''
sm remove 'h': e.g. 'zh'==>>'z'
ym remove 'g': e.g. 'ang1' ==>> 'an1'
ym remove digit: e.g. 'ang1' ==>> 'ang'

sms_yms_pair :: ([sm], [ym])
cliques :: {(size, size):sms_yms_pair}
'''

__all__ = '''
    make_max_refined_pair2original_max_pairs
        make_max_refined_cliques__sm2ym_num_graph
            refined_cliques
                __refine_pair
            make_max_cliques__sm2ym_num_graph
        make_refined_pair2original_pairs
            __refine_pair
    '''.split()

from collections import defaultdict
from .make_max_cliques__sm2ym_num_graph import make_max_cliques__sm2ym_num_graph
from .max_cliques__sm2ym_num_graph import max_cliques__sm2ym_num_graph
import itertools # chain


def make_max_refined_pair2original_max_pairs(
    max_cliques__sm2ym_num_graph, *
    ,sm_remove_h:bool
    ,ym_remove_g:bool
    ,ym_remove_digit:bool
    ,min_len_sm_ls=0
    ,min_len_ym_ls=0
    ):
    # -> max_refined_pair2original_max_pairs
    (max_refined_cliques
    ) = make_max_refined_cliques__sm2ym_num_graph(
                max_cliques__sm2ym_num_graph
                ,sm_remove_h=sm_remove_h
                ,ym_remove_g=ym_remove_g
                ,ym_remove_digit=ym_remove_digit
                )
    (max_refined_pair2original_max_pairs
    ) = make_refined_pair2original_pairs(
                max_refined_cliques
                ,max_cliques__sm2ym_num_graph
                ,sm_remove_h=sm_remove_h
                ,ym_remove_g=ym_remove_g
                ,ym_remove_digit=ym_remove_digit
                )

    for pair in list(max_refined_pair2original_max_pairs):
        sm_vertices, ym_vertices = pair
        if (len(sm_vertices) < min_len_sm_ls
            or len(ym_vertices) < min_len_ym_ls):
            del max_refined_pair2original_max_pairs[pair]
    return max_refined_pair2original_max_pairs

def sort_dict_values(d):
    for value in d.values():
        value.sort()
    return None
def iter_cliques(cliques):
    #cliques -> Iter sms_yms_pair
    it_sms_yms_pairs = itertools.chain.from_iterable(cliques.values())
    return it_sms_yms_pairs

def make_refined_pair2original_pairs(
    refined_cliques, original_cliques, *
    ,sm_remove_h:bool
    ,ym_remove_g:bool
    ,ym_remove_digit:bool
    ):
    # -> refined_pair2original_pairs
    refined_pair2original_pairs = {
        refined_sms_yms_pair : []
        for refined_sms_yms_pair in iter_cliques(refined_cliques)
        }
    for old_pair in iter_cliques(original_cliques):
        new_pair = __refine_pair(*old_pair
                ,sm_remove_h=sm_remove_h
                ,ym_remove_g=ym_remove_g
                ,ym_remove_digit=ym_remove_digit
                )
        may_ls = refined_pair2original_pairs.get(new_pair)
        if may_ls is not None:
            original_pairs = may_ls
            original_pairs.append(old_pair)

    sort_dict_values(refined_pair2original_pairs)
    return refined_pair2original_pairs

def make_max_refined_cliques__sm2ym_num_graph(
    max_cliques__sm2ym_num_graph, *
    ,sm_remove_h:bool
    ,ym_remove_g:bool
    ,ym_remove_digit:bool
    ):
    # -> max_refined_cliques
    refined_cliques = refine_cliques__sm2ym_num_graph(
                max_cliques__sm2ym_num_graph
                ,sm_remove_h=sm_remove_h
                ,ym_remove_g=ym_remove_g
                ,ym_remove_digit=ym_remove_digit
                )
    max_refined_cliques = make_max_cliques__sm2ym_num_graph(
                iter_cliques(refined_cliques))
    return max_refined_cliques

def refine_cliques__sm2ym_num_graph(
    max_cliques__sm2ym_num_graph, *
    ,sm_remove_h:bool
    ,ym_remove_g:bool
    ,ym_remove_digit:bool
    ):
    # -> refined_cliques
    refined_cliques = defaultdict(list)
        # {(size,size):[new_pair]}
    for sms_yms_pairs in max_cliques__sm2ym_num_graph.values():
        for sm_vertices, ym_vertices in sms_yms_pairs:
            new_pair = __refine_pair(sm_vertices, ym_vertices
                ,sm_remove_h=sm_remove_h
                ,ym_remove_g=ym_remove_g
                ,ym_remove_digit=ym_remove_digit
                )
            new_sizes = tuple(map(len, new_pair))
            refined_cliques[new_sizes].append(new_pair)

    sort_dict_values(refined_cliques)
    refined_cliques = dict(refined_cliques)
    return refined_cliques

def __refine_pair(sm_vertices, ym_vertices, *
    ,sm_remove_h:bool
    ,ym_remove_g:bool
    ,ym_remove_digit:bool
    ):
    #-> new_pair = (new_sm_vertices, new_ym_vertices)
    new_sm_vertices = set()
    if sm_remove_h:
        for sm in sm_vertices:
            if len(sm) == 2:
                assert sm[-1] == 'h'
                sm = sm[:-1]
            assert len(sm) == 1
            new_sm_vertices.add(sm)
    else:
        new_sm_vertices.update(sm_vertices)

    new_ym_vertices = set()
    if ym_remove_g:
        for ym in ym_vertices:
            assert '0' <= ym[-1] <= '9'
            if ym[-2] == 'g':
                ym = ym[:-2] + ym[-1:]
            assert ym[-2] != 'g'
            new_ym_vertices.add(ym)
    else:
        new_ym_vertices.update(ym_vertices)

    new_ym_vertices0 = new_ym_vertices
    new_ym_vertices = set()
    if ym_remove_digit:
        for ym in new_ym_vertices0:
            assert '0' <= ym[-1] <= '9'
            ym = ym[:-1]
            assert not ('0' <= ym[-1] <= '9')
            new_ym_vertices.add(ym)
    else:
        new_ym_vertices.update(new_ym_vertices0)

    new_sm_vertices = tuple(sorted(new_sm_vertices))
    new_ym_vertices = tuple(sorted(new_ym_vertices))
    new_pair = new_sm_vertices, new_ym_vertices
    return new_pair


def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdout # may_open_stdin
    from pprint import pprint
    from pathlib import PurePath as Path
    this_file = Path(__file__)
    this_folder = this_file.parent
    this_file_name = this_file.name

    parser = argparse.ArgumentParser(
        description=f'refine max_cliques from max_cliques__sm2ym_num_graph.py'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-oe', '--output_encoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-sh', '--sm_remove_h', action='store_true'
                        , default = False
                        , help='sm_remove_h: e.g. treat z/zh the same')
    parser.add_argument('-yg', '--ym_remove_g', action='store_true'
                        , default = False
                        , help='ym_remove_g: e.g. treat an/ang the same')
    parser.add_argument('-yd', '--ym_remove_digit', action='store_true'
                        , default = False
                        , help='ym_remove_digit: e.g. treat an1/an3 the same')
    parser.add_argument('-nsm', '--min_len_sm_ls', type=int, default=0
                        , help='control output')
    parser.add_argument('-nym', '--min_len_ym_ls', type=int, default=0
                        , help='control output')

    args = parser.parse_args(args)
    output_encoding = args.output_encoding
    omode = 'wt' if args.force else 'xt'
    sm_remove_h = args.sm_remove_h
    ym_remove_g = args.ym_remove_g
    ym_remove_digit = args.ym_remove_digit
    min_len_sm_ls=args.min_len_sm_ls
    min_len_ym_ls=args.min_len_ym_ls

    def bool2TF(b):
        return 'T' if b else 'F'
    var_name = f'max_refined_pair2original_max_pairs__sh{bool2TF(sm_remove_h)}_yg{bool2TF(ym_remove_g)}_yd{bool2TF(ym_remove_digit)}_nsm{min_len_sm_ls}_nym{min_len_ym_ls}'
    (max_refined_pair2original_max_pairs
    ) = make_max_refined_pair2original_max_pairs(
                max_cliques__sm2ym_num_graph
                ,sm_remove_h=sm_remove_h
                ,ym_remove_g=ym_remove_g
                ,ym_remove_digit=ym_remove_digit
                ,min_len_sm_ls=min_len_sm_ls
                ,min_len_ym_ls=min_len_ym_ls
                )

    may_ofname = args.output
    if may_ofname is None:
        may_ofname = this_folder / f'{var_name}.py'
    with may_open_stdout(may_ofname, omode, encoding=output_encoding) as fout:
        print(f'#{var_name} generated by {this_file_name}', file=fout);
        print(f'{var_name} = \\', file=fout);
        pprint(max_refined_pair2original_max_pairs, stream=fout)



if __name__ == '__main__':
    main()

