#__all__:goto
r'''
e ../../python3_src/seed/algo/page_rank.py
py -m seed.algo.page_rank
    view ../../python3_src/seed/math/matrix/solve_matrix.py

py -m nn_ns.app.debug_cmd   seed.algo.page_rank

py -m seed.algo.page_rank --doctest_only__turnoff_main -pm page_rank__matrix
py -m seed.algo.page_rank -nv4gr 20 -threshold4gr 0.6    -pm page_rank__matrix    -pm page_rank__max_stable -max_stable 7 -nstep4round4stable 17

echo '[[7, 8, 10, 13, 15, 17], [2, 3, 5, 7, 12, 14, 17, 18, 19], [1, 3, 4, 6, 7, 13, 14, 16, 17, 18], [0, 2, 4, 6, 7, 9, 13, 15], [0, 1, 7, 8, 14], [6, 8, 9, 10, 11], [0, 2, 12, 13, 14, 15, 19], [3, 4, 5, 10, 11, 12, 13, 15, 17], [5, 12, 13, 14, 15, 17], [1, 4, 7, 10, 11, 16, 19], [0, 1, 2, 3, 4, 6, 7, 8, 13, 14, 16, 17], [4, 5, 7, 8, 9, 10, 13, 14, 17], [0, 2, 5, 6, 8, 11, 17, 18], [1, 4, 11, 12, 15, 16, 19], [1, 6, 8, 9, 10, 12, 13, 15, 19], [1, 3, 5, 6, 9, 11, 14, 16], [0, 11, 12, 13, 14, 18], [1, 3, 4, 9, 11, 12, 13, 16, 19], [1, 10, 11, 14, 15], [5, 6, 11, 17]]' | py -m seed.algo.page_rank    -pm page_rank__matrix    -pm page_rank__max_stable -max_stable 7 -nstep4round4stable 17




我的实现 稍微不同于(自动添加 自环边):
    view others/数学/编程/graph/Page Rank--Random Walk method.txt
    view others/数学/编程/graph/Page Rank--py.networkx.txt

>>> vtx2vtc = [[7, 8, 10, 13, 15, 17], [2, 3, 5, 7, 12, 14, 17, 18, 19], [1, 3, 4, 6, 7, 13, 14, 16, 17, 18], [0, 2, 4, 6, 7, 9, 13, 15], [0, 1, 7, 8, 14], [6, 8, 9, 10, 11], [0, 2, 12, 13, 14, 15, 19], [3, 4, 5, 10, 11, 12, 13, 15, 17], [5, 12, 13, 14, 15, 17], [1, 4, 7, 10, 11, 16, 19], [0, 1, 2, 3, 4, 6, 7, 8, 13, 14, 16, 17], [4, 5, 7, 8, 9, 10, 13, 14, 17], [0, 2, 5, 6, 8, 11, 17, 18], [1, 4, 11, 12, 15, 16, 19], [1, 6, 8, 9, 10, 12, 13, 15, 19], [1, 3, 5, 6, 9, 11, 14, 16], [0, 11, 12, 13, 14, 18], [1, 3, 4, 9, 11, 12, 13, 16, 19], [1, 10, 11, 14, 15], [5, 6, 11, 17]]






>>> nv = len(vtx2vtc)
>>> nv
20
>>> seq_vs_mapping = False
>>> sorted_vtcA, v2scA = page_rank__matrix(vtx2vtc, seq_vs_mapping=seq_vs_mapping, float64_vs_Fraction=False, add_a_virtual_vertex_to_connect_all_vertex=False)
>>> sorted_vtcA_, v2scA_ = page_rank__matrix(vtx2vtc, seq_vs_mapping=seq_vs_mapping, float64_vs_Fraction=True, add_a_virtual_vertex_to_connect_all_vertex=False)

>>> sorted_vtcB, v2scB = page_rank__max_stable(vtx2vtc, seq_vs_mapping=seq_vs_mapping, max_num_stable=7, num_step_per_round=17)
>>> sorted_vtcA == sorted_vtcA_ == sorted_vtcB
True
>>> import numpy
>>> numpy.allclose(v2scA, v2scA_, v2scB)
True

>>> from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
>>> sorted_vtcA
[18, 2, 3, 16, 0, 9, 10, 7, 19, 4, 15, 6, 8, 1, 5, 12, 17, 14, 13, 11]
>>> print(stable_repr__expand_top_layer(v2scA_))
[0.039859915790325356
,0.05668651415787809
,0.02870165937860064
,0.03206787031522439
,0.05022248300834763
,0.057246440558260475
,0.05467868028035219
,0.047060075425335746
,0.05524005426015531
,0.0442759059791896
,0.04680842162430301
,0.07313254419922215
,0.057826679824189466
,0.06851335614616055
,0.06403768107533976
,0.05363155720264083
,0.03760023449102687
,0.059611631648618255
,0.02408945027370916
,0.0487088443611205
]

#above using my:seed.math.matrix.solve_matrix.linear_solver
#below using numpy..linalg.solve:
>>> print(stable_repr__expand_top_layer(v2scA))
[0.039859915790325426
,0.05668651415787809
,0.028701659378600603
,0.032067870315224366
,0.05022248300834761
,0.05724644055826048
,0.054678680280352186
,0.047060075425335725
,0.05524005426015533
,0.044275905979189595
,0.04680842162430302
,0.07313254419922216
,0.05782667982418947
,0.06851335614616057
,0.06403768107533973
,0.05363155720264085
,0.03760023449102687
,0.059611631648618255
,0.02408945027370915
,0.048708844361120565
]



>>> import networkx as nx
>>> g = nx.DiGraph()
>>> g = vtx2vtc_to_networkx_DiGraph(vtx2vtc, seq_vs_mapping=seq_vs_mapping)
>>> v2scC = nx.pagerank(g, 0.4)
>>> v2scC = [sc for _, sc in sorted(v2scC.items())]
>>> nv = len(v2scC)
>>> sorted_vtcC = sort_by_v2sc(range(nv), v2scC)
>>> sorted_vtcC == sorted_vtcA
False
>>> sorted_vtcC
[18, 2, 3, 16, 9, 0, 19, 10, 7, 4, 8, 5, 6, 12, 15, 1, 17, 14, 13, 11]
>>> sorted_vtcA
[18, 2, 3, 16, 0, 9, 10, 7, 19, 4, 15, 6, 8, 1, 5, 12, 17, 14, 13, 11]
>>> print(stable_repr__expand_top_layer(v2scC))
[0.04694308568026914
,0.053173047914908914
,0.041992560873629264
,0.0435593764097535
,0.050003793160377015
,0.05127130202595952
,0.05171074663994817
,0.04981065873036884
,0.05075915156577432
,0.04675930232370155
,0.04930873751051751
,0.05892594346856954
,0.051746848934858265
,0.05733972743669675
,0.05626390561820836
,0.052291682231232144
,0.04529725313883653
,0.053391470798815094
,0.04129537785198241
,0.04815602768559314
]


>>> sorted_vtcA__vvtx, v2scA__vvtx = page_rank__matrix(vtx2vtc, seq_vs_mapping=seq_vs_mapping, float64_vs_Fraction=False, add_a_virtual_vertex_to_connect_all_vertex=True)
>>> sorted_vtcA__vvtx == sorted_vtcA
False
>>> sorted_vtcA__vvtx == sorted_vtcC
False
>>> sorted_vtcC
[18, 2, 3, 16, 9, 0, 19, 10, 7, 4, 8, 5, 6, 12, 15, 1, 17, 14, 13, 11]
>>> sorted_vtcA__vvtx
[18, 2, 3, 16, 0, 9, 10, 19, 7, 4, 8, 6, 15, 5, 1, 12, 17, 14, 13, 11]
>>> sorted_vtcA
[18, 2, 3, 16, 0, 9, 10, 7, 19, 4, 15, 6, 8, 1, 5, 12, 17, 14, 13, 11]

>>> print(stable_repr__expand_top_layer(v2scA__vvtx))
[0.04129899104588357
,0.05657093517944549
,0.03176720678341583
,0.03518584991335841
,0.05060391479718297
,0.05486396735118748
,0.053522423802643625
,0.048195369096873594
,0.05346005084056507
,0.04445851615636844
,0.04718176120404263
,0.06959956146158075
,0.05664871453772116
,0.0668666155593635
,0.06280440259157254
,0.053649454521160996
,0.0394428737392946
,0.058125187109493534
,0.027838905769653664
,0.047915298539192415
]


#'''

#HHHHH
__all__ = '''
    page_rank__matrix
    page_rank__max_stable



    vtx2vtc_to_networkx_DiGraph
    generate__vtx2vtc__seq
    mk_pseudo_mapping_opss
    mapping2seq__vtx2vtc
    sort_by_v2sc
    page_rank__matrix
    page_rank__max_stable
    '''.split()


import random
#from functools import partial
from seed.math.matrix.solve_matrix import NoRowMatrix, linear_solver, ring_ex_ops__Fraction
from seed.seq_tools.seq_as_mapping import SeqAsMapping
from seed.mapping_tools.mapping_as_seq import MappingAsSeq

#_solve = partial(linear_solver.solve_equations__matrix__to_representative_solutions, ring_ex_ops__Fraction, validate=True)
_solve = lambda mx, b, /: [*map(linear_solver.transpose__matrix, linear_solver.solve_equations__matrix__to_representative_solutions(ring_ex_ops__Fraction, mx, linear_solver.transpose__matrix([b]), validate=True))]

def vtx2vtc_to_networkx_DiGraph(vtx2vtc, /, *, seq_vs_mapping:bool):
    import networkx as nx
    g = nx.DiGraph()
    (to_keys, to_items, has_key, mk_k2v, mk_k2fv) = mk_pseudo_mapping_opss(seq_vs_mapping)
    for v, us in to_items(vtx2vtc):
        us = {v, *us}
        for u in us:
            g.add_edge(v, u)
    return g

def generate__vtx2vtc__seq(nv, threshold, /):
    if not 0.0 < threshold < 1.0: raise TypeError(threshold)
    vtc = range(nv)
    i2js = [[v for v in vtc if v != _u and random.random() > threshold] for _u in vtc]
    vtx2vtc = i2js
    return vtx2vtc

def mk_pseudo_mapping_opss(seq_vs_mapping, /):
    from seed.seq_tools.seq_as_mapping import SeqAsMapping
    from seed.mapping_tools.mapping_as_seq import MappingAsSeq
    if seq_vs_mapping:
        #mapping
        def to_keys(d, /):
            return iter(d.keys())
        def to_items(d, /):
            return iter(d.items())
        def has_key(d, k, /):
            return k in d
        def mk_k2v(d, v0, /):
            return dict.fromkeys(d, v0)
        def mk_k2fv(d, fv0, /):
            return {k:fv0() for k in d}
    else:
        #seq
        def to_keys(ls, /):
            return iter(range(len(ls)))
        def to_items(ls, /):
            return enumerate(ls)
        def has_key(ls, i, /):
            return 0 <= i < len(ls)
        def mk_k2v(ls, v0, /):
            return [v0]*len(ls)
        def mk_k2fv(ls, fv0, /):
            return [fv0() for _ in to_keys(ls)]
    return to_keys, to_items, has_key, mk_k2v, mk_k2fv




def mapping2seq__vtx2vtc(vtx2vtc, /):
    i2v = [*vtx2vtc.keys()]
    v2i = {v:i for i, v in enumerate(i2v)}
    i2js = []
    for i, v in enumerate(i2v):
        us = vtx2vtc[v]
        js = [v2i[u] for u in us]
        i2js.append(js)
    return (i2v, v2i, i2js)

def sort_by_v2sc(vtc, v2sc, /):
    key_func = lambda v:v2sc[v]
    sorted_vtc = sorted(vtc, key=key_func)
    return sorted_vtc

def page_rank__matrix(vtx2vtc, /, *, seq_vs_mapping:bool, float64_vs_Fraction:bool, add_a_virtual_vertex_to_connect_all_vertex:bool):
    seq_vs_mapping = bool(seq_vs_mapping)
    float64_vs_Fraction = bool(float64_vs_Fraction)
    add_a_virtual_vertex_to_connect_all_vertex = bool(add_a_virtual_vertex_to_connect_all_vertex)

    if seq_vs_mapping:
        #mapping
        (i2v, v2i, i2js) = mapping2seq__vtx2vtc(vtx2vtc)
    else:
        #seq
        i2js = vtx2vtc
    i2js
    nv = len(i2js)

    if 0:
        zero = 0.0
        one = 1.0
        neg_one = -1.0
    elif not float64_vs_Fraction:
        'float64'
        from numpy import float64
        zero = float64(0)
        one = float64(1)
        neg_one = float64(-1)
    else:
        'Fraction'
        zero = ring_ex_ops__Fraction.get_zero()
        one = ring_ex_ops__Fraction.get_one()
        neg_one = ring_ex_ops__Fraction.get_neg_one()

    nv_ex = nv + add_a_virtual_vertex_to_connect_all_vertex
    mx = dst_vtx2src_vtc2coeff = linear_solver.mk_matrix__default(nv_ex, nv_ex, zero)
        #[[zero]*nv_ex for _ in range(nv_ex)]
    i_js_pairs = [*enumerate(i2js)]
    if add_a_virtual_vertex_to_connect_all_vertex:
        i_js_pairs.append((nv, range(nv)))
            # nv --> any j
    for i, js in i_js_pairs:
        js = {i, *js} #implictly self-loop, s.t. [n>0]
        if add_a_virtual_vertex_to_connect_all_vertex:
            js.add(nv)
            # any i --> nv
        n = len(js)
        coeff = neg_one/n
        for j in js:
            dst_vtx2src_vtc2coeff[j][i] = coeff
                # i --> j (include i)
        else:
            dst_vtx2src_vtc2coeff[i][i] += one
                # [i2sc**T === dst_vtx2src_vtc2coeff * i2sc**T]
                # [EchoMatrix<nv_ex, nv_ex> * i2sc**T === dst_vtx2src_vtc2coeff * i2sc**T]
                # ==>> {zero, neg_one/n, one+neg_one/n}
                # [(EchoMatrix<nv_ex, nv_ex> - dst_vtx2src_vtc2coeff) * i2sc**T === zeros<nv_ex, nv_ex>]
    # !![mx * unknowns4vtc = zero_vector]
    #       ==>> mx.rank < nv
    # add new constraint: [sum unknowns4vtc = one]


    if 0:
        mx.append([one]*nv); mx_ex = mx; del mx
        vec_0s_1 = [zero]*nv; vec_0s_1.append(one)
        #solve(mx_ex, vec_0s_1)
    elif not mx:
        b = []
    else:
        #add new constraint
        #
        #sum all rows in mx == zeros
        #   at least one row is useless
        mx[-1] = [one]*nv_ex
        b = [zero]*nv_ex
        b[-1] = one
        if add_a_virtual_vertex_to_connect_all_vertex and nv:
            # virtual vtx nv donot take part in probability
            mx[-1][-1] = zero
    if 0:
        from sympy import linsolve, Matrix
        #help(linsolve)
        #linsolve((A, b))
        #i2sc = linsolve((Matrix(mx_ex), Matrix(vec_0s_1)))
        i2sc = linsolve((Matrix(mx), Matrix(b)))
    elif not float64_vs_Fraction:
        #https://www.scriptverse.academy/tutorials/python-solve-linear-equations.html
        from numpy.linalg import solve
        import numpy as np
        #help(solve)
        #numpy.linalg.solve(A, b)
        #i2sc = solve(np.array(mx_ex), np.array(vec_0s_1))
        A = np.array(mx)
        B = np.array(b)
        X = solve(A, B)
        assert np.allclose(np.dot(A, X), B)
            #check
        i2sc = X
    else:
        #linear_solver.
        i2sc__lsls = _solve(mx, b)
        [[i2sc]] = i2sc__lsls # ???exist and unique???
    i2sc
    i2sc = [*map(float, i2sc)]
        #<class 'numpy.ndarray'>
        #<class 'numpy.float64'>
        #<class 'fractions.Fraction'>
    if add_a_virtual_vertex_to_connect_all_vertex:
        i2sc.pop()



    i2sc
    assert len(i2sc) == nv
    sorted_js = sort_by_v2sc(range(nv), i2sc)

    if seq_vs_mapping:
        #mapping
        v2sc = dict(zip(i2v, i2sc))
        sorted_vtc = [i2v[i] for i in sorted_js]
    else:
        #seq
        v2sc = i2sc
        sorted_vtc = sorted_js
    return sorted_vtc, v2sc
#def page_rank__matrix(vtx2vtc, /, *, seq_vs_mapping:bool):



#def page_rank(dst_vtx2src_vtc, /, *, seq_vs_mapping:bool, num_step_per_round = 20, max_num_stable = 7):
#    'input: reversed simple dgraph; no self-loop, auto attach implictly!'
def page_rank__max_stable(vtx2vtc, /, *, seq_vs_mapping:bool, num_step_per_round:20, max_num_stable:7):
    'input: simple dgraph; no self-loop, auto attach implictly!'
    (to_keys, to_items, has_key, mk_k2v, mk_k2fv) = mk_pseudo_mapping_opss(seq_vs_mapping)

    def step(vtx2vtc, v2scI, /, *, v2scO):
        for v in to_keys(vtx2vtc):
            v2scO[v] = 0.0
        for v, us in to_items(vtx2vtc):
            n = len(us)+1 #implictly self-loop
            sc = v2scI[v]/n
            for u in us:
                v2scO[u] += sc
            v2scO[v] += sc
        return

    def check(vtx2vtc, /):
        for v, us in to_items(vtx2vtc):
            if v in us: raise TypeError('self-loop')
        for v, us in to_items(vtx2vtc):
            if not len(us) == len({*us}): raise TypeError('multiedge')
    def main():
        check(vtx2vtc)

        nv = len(vtx2vtc)
        score0 = 1.0/nv
        v2scL = mk_k2v(vtx2vtc, score0)
        v2scR = mk_k2v(vtx2vtc, score0)
        num_stable = 0
        sorted_vtc = list(to_keys(vtx2vtc))
        #key_func = lambda v:v2scL[v]
        while num_stable < max_num_stable:
            for _ in range(num_step_per_round):
                step(vtx2vtc, v2scL, v2scO=v2scR)
                step(vtx2vtc, v2scR, v2scO=v2scL)
            #_sorted_vtc = sorted(sorted_vtc, key=key_func)
            _sorted_vtc = sort_by_v2sc(sorted_vtc, v2scL)
                #donot use to_keys()
                #   since sorted_vtc is almost sorted, faster
            if _sorted_vtc == sorted_vtc:
                num_stable += 1
            else:
                num_stable = 0
                sorted_vtc = _sorted_vtc
        return sorted_vtc, v2scL
    return main()



def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    from ast import literal_eval
    from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer

    parser = argparse.ArgumentParser(
        description='my page rank algo impl'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )

    page_rank_methods = [page_rank__matrix, page_rank__max_stable]
    page_rank_method_names = [f.__name__ for f in page_rank_methods]
    parser.add_argument('-pm', '--page_rank_method', type=str, required=True, choices=page_rank_method_names, action='append'
                        , help='select at least one page_rank_method')

    parser.add_argument('-vvtx52vtc', '--add_a_virtual_vertex_to_connect_all_vertex', action='store_true'
                        , default = False
                        , help='add_a_virtual_vertex_to_connect_all_vertex@page_rank__matrix (default=False)')
    parser.add_argument('-Fraction', '--float64_vs_Fraction', action='store_true'
                        , default = False
                        , help='float64_vs_Fraction@page_rank__matrix (default=False:float64)')
    parser.add_argument('-max_stable', '--max_num_stable4page_rank__max_stable', type=int, default=7
                        , help='max_num_stable@page_rank__max_stable (default=7)')
    parser.add_argument('-nstep4round4stable', '--num_step_per_round4page_rank__max_stable', type=int, default=20
                        , help='num_step_per_round@page_rank__max_stable (default=20)')

    parser.add_argument('-threshold4gr', '--threshold4generate_random_dgraph', type=float, default=0.7
                        , help='0.0 < threshold < 1.0; how hard to produce edge; probability to "DONOT" produce an edge')
    parser.add_argument('-nv4gr', '--num_vertices4generate_random_dgraph', type=int, default=0
                        , help='disable -i/--input')
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('--doctest_only__turnoff_main', action='store_true'
                        , default = False
                        , help='doctest, not run main()')

    args = parser.parse_args(args)
    if args.doctest_only__turnoff_main:return

    iencoding = args.iencoding
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'

    nv = args.num_vertices4generate_random_dgraph
    threshold = args.threshold4generate_random_dgraph
    if nv > 0:
        vtx2vtc = generate__vtx2vtc__seq(nv, threshold)
        seq_vs_mapping = False
    else:
        may_ifname = args.input
        with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin:
            txt = fin.read()
        vtx2vtc = literal_eval(txt)
        cls = type(vtx2vtc)
        if cls is dict:
            seq_vs_mapping = True
        elif cls in (list, tuple):
            seq_vs_mapping = False
        else:
            raise TypeError(cls)
    vtx2vtc, seq_vs_mapping

    page_rank_method_name2kwargs = dict(
        page_rank__matrix = dict(float64_vs_Fraction=args.float64_vs_Fraction, add_a_virtual_vertex_to_connect_all_vertex=add_a_virtual_vertex_to_connect_all_vertex)
        ,page_rank__max_stable = dict(max_num_stable=args.max_num_stable4page_rank__max_stable
                ,num_step_per_round=args.num_step_per_round4page_rank__max_stable
                )
        )

    selected_page_rank_method_names = {*args.page_rank_method}
    nm2kwargs_result = {}
    for nm in page_rank_method_names:
        page_rank_method = globals()[nm]
        kwds = page_rank_method_name2kwargs[nm]
        sorted_vtc, v2sc = page_rank_method(vtx2vtc, seq_vs_mapping=seq_vs_mapping, **kwds)
        kwargs_result = dict(kwargs=kwds, sorted_vtc=sorted_vtc, v2sc=v2sc)
        nm2kwargs_result[nm] = kwargs_result

    io_data = dict(vtx2vtc=vtx2vtc, page_rank_method_name2kwargs_result=nm2kwargs_result)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        stable_repr_print__expand_top_layer(fout, io_data)

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

