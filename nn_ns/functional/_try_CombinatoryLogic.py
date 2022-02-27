
r'''
py -m nn_ns.app.debug_cmd   nn_ns.functional.CombinatoryLogic
py -m nn_ns.functional._try_CombinatoryLogic
    指数增长？！！！
py -m nn_ns.functional._try_CombinatoryLogic > $my_tmp/out4py/nn_ns.functional._try_CombinatoryLogic.case0.1-14.txt
    view /sdcard/0my_files/tmp//out4py/nn_ns.functional._try_CombinatoryLogic.case0.1-14.txt
#'''

from nn_ns.functional.CombinatoryLogic import (Expr, Variable, NamedVariable, Abstraction, Application, is_free, is_combinator__SKIBC, is_combinator, substitute, is_primitive_combinator__SKIBC
    ,has_no_frees
    ,has_no_abstraction
    ,frozen_set__list
    ,empty_frozen_set
    ,collect_frees
    ,call
    ,EvaluationStrategy
    ,FullBetaReduction
    ,NormalOrder
    ,CallByName
    ,CallByNeed
    ,CallByValue
    ,evalue
    ,py_id
    ,L,V
    ,S,K,I,B,C
    ,implication_elimination, reader_apply, const, _id_, composition, flip

    ,PrintArg
    ,show_expr
    ,show_expr__SKIBC
    ,print_expr
    ,print_expr__SKIBC
    ,remove_abstraction__SKIBC
    ,POS_outermost
    )




def _t(n, /,*, case):
    from seed.tiny import echo
    if case==0:
        body = I
        for i in reversed(range(n)):
            body = body[V(f'x{i!s}')]
        body = body[I]
    elif case==1:
        body = I
        for i in (range(n)):
            body = body[V(f'x{i!s}')]
            if 0:
                assert isinstance(body, NamedVariable)
                assert isinstance(body, Expr)
                assert not callable(body)
                    #__getitem__ instead of call!!
        body = body[I]
    elif case==2:
        body = V(f'z')
        for i in reversed(range(n)):
            body = V(f'x{i!s}')[body]
    else:
        raise Exception(f'case not in [0..2]: case={case!r}')

    expr = body
    for i in reversed(range(n)):
        expr = Abstraction(f'x{i!s}', expr)

    if 0:
        #print_expr(expr)
        s0 = show_expr(expr, POS_outermost)
    else:
        #print_expr__SKIBC(expr)
        s0 = show_expr__SKIBC(expr, POS_outermost)
    print(s0)
    L0 = len(s0)

    expr__SKIBC = remove_abstraction__SKIBC(expr)
    if 1:
        #print_expr__SKIBC(expr__SKIBC)
        s1 = show_expr__SKIBC(expr__SKIBC, POS_outermost)
    print(s1)
    L1 = len(s1)

    print(f'{L0}; {L1}')


def _tt(n):
    for case in range(3):
        for i in range(n+1):
            _t(i, case=case)

if __name__ == "__main__":
    #_tt(10)
    #_t(100, case=0)
        #RecursionError: maximum recursion depth exceeded in comparison
    #_t(20, case=0)
        # 163; 5781
    for j in range(15):
        _t(j, case=0)
        print(j)
    r'''case=0
3; 3
0
10; 5
1
17; 15
2
24; 35
3
31; 69
4
38; 121
5
45; 195
6
52; 295
7
59; 425
8
66; 589
9
73; 791
10
82; 1035
11
91; 1325
12
100; 1665
13
109; 2059
14
    #_t(20, case=0)
        # 163; 5781
    #'''

