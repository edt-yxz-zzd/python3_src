#__all__:goto
r'''[[[
e ../../python3_src/seed/types/Reproduceable.py
view ../../python3_src/seed/types/HistorySaver.py
view ../../python3_src/seed/math/primality_test/reproduceable7probable_primes.py

seed.types.Reproduceable
py -m nn_ns.app.debug_cmd   seed.types.Reproduceable -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.Reproduceable:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
view ../../python3_src/seed/math/factor_pint/smooth_group_order_method.py

move_from:
view ../../python3_src/seed/abc/IReproduceable.py
]]
[[
mv -i ../../python3_src/seed/abc/IReproduceable.py ../../python3_src/seed/types/Reproduceable.py
]]
[[
%s/\(st\|IN\|OUT\)\zs\[\([a-z0-9+-]*\)\]/{\2}/g

%s/seed\.abc\.IReproduceable/seed.types.Reproduceable/g

]]



'#'; __doc__ = r'#'
>>> Reproduceable5seq('0123456789', 0)
Reproduceable5seq('0123456789', 0)
>>> iter_pairs4reproduceable_(Reproduceable5seq('0123456789', 0))
Iter4IReproduceable(Reproduceable5seq('0123456789', 0))
>>> [*iter_pairs4reproduceable_(Reproduceable5seq('0123456789', 0))]
[('0', Reproduceable5seq('0123456789', 1)), ('1', Reproduceable5seq('0123456789', 2)), ('2', Reproduceable5seq('0123456789', 3)), ('3', Reproduceable5seq('0123456789', 4)), ('4', Reproduceable5seq('0123456789', 5)), ('5', Reproduceable5seq('0123456789', 6)), ('6', Reproduceable5seq('0123456789', 7)), ('7', Reproduceable5seq('0123456789', 8)), ('8', Reproduceable5seq('0123456789', 9)), ('9', Reproduceable5seq('0123456789', 10))]



>>> [*iter_pairs4reproduceable_(Reproduceable5seq('0123456789', 7))]
[('7', Reproduceable5seq('0123456789', 8)), ('8', Reproduceable5seq('0123456789', 9)), ('9', Reproduceable5seq('0123456789', 10))]
>>> [*iter_fsts4reproduceable_(Reproduceable5seq('0123456789', 7))]
['7', '8', '9']
>>> [*iter_snds4reproduceable_(Reproduceable5seq('0123456789', 7))]
[Reproduceable5seq('0123456789', 8), Reproduceable5seq('0123456789', 9), Reproduceable5seq('0123456789', 10)]






>>> rp7null = Reproduceable5seq('', 0)
>>> rp03 = Reproduceable5seq('012', 0)
>>> rp34 = Reproduceable5seq('3', 0)
>>> rp_ls = [rp7null, rp7null, rp03, rp7null, rp7null, rp34, rp7null, rp7null]

Reproduceable7chain5iterable
Reproduceable7chain5reproduceable
>>> rp = Reproduceable7chain5iterable(iter(rp_ls))
>>> rp
Reproduceable7chain5iterable([Reproduceable5seq('', 0), Reproduceable5seq('', 0), Reproduceable5seq('012', 0), Reproduceable5seq('', 0), Reproduceable5seq('', 0), Reproduceable5seq('3', 0), Reproduceable5seq('', 0), Reproduceable5seq('', 0)])
>>> [*iter_fsts4reproduceable_(rp)]
['0', '1', '2', '3']


>>> rp = Reproduceable7chain5reproduceable(None, Reproduceable5seq(rp_ls, 0))
>>> rp
Reproduceable7chain5reproduceable(None, Reproduceable5seq([Reproduceable5seq('', 0), Reproduceable5seq('', 0), Reproduceable5seq('012', 0), Reproduceable5seq('', 0), Reproduceable5seq('', 0), Reproduceable5seq('3', 0), Reproduceable5seq('', 0), Reproduceable5seq('', 0)], 0))
>>> [*iter_fsts4reproduceable_(rp)]
['0', '1', '2', '3']



Reproduceable7fmap
Reproduceable7transform
>>> rp = Reproduceable7fmap(int, rp03)
>>> rp
Reproduceable7fmap(<class 'int'>, Reproduceable5seq('012', 0))
>>> [*iter_fsts4reproduceable_(rp)]
[0, 1, 2]

>>> rp = Reproduceable7transform(lambda st,ch:(f'{st}:{ch}', st-1), 999, rp03)
>>> rp #doctest: +ELLIPSIS
Reproduceable7transform(<function <lambda> at 0x...>, 999, Reproduceable5seq('012', 0))
>>> [*iter_fsts4reproduceable_(rp)]
['999:0', '998:1', '997:2']




Reproduceable7rdiff
Reproduceable7foldl
>>> rp = Reproduceable7rdiff(int.__rsub__, 40, Reproduceable5seq(range(5), 0))
>>> rp
Reproduceable7rdiff(<slot wrapper '__rsub__' of 'int' objects>, 40, Reproduceable5seq(range(0, 5), 0))
>>> [*iter_fsts4reproduceable_(rp)]
[-40, 1, 1, 1, 1]


>>> rp = Reproduceable7foldl(int.__add__, 40, Reproduceable5seq(range(5), 0))
>>> rp
Reproduceable7foldl(<slot wrapper '__add__' of 'int' objects>, 40, Reproduceable5seq(range(0, 5), 0))
>>> [*iter_fsts4reproduceable_(rp)]
[40, 41, 43, 46, 50]





>>> class C:
...     def ___xnext4reproduceable___(sf, /):return 66666
>>> issubclass(C, IReproduceable)
True
>>> isinstance(C(), IReproduceable)
True
>>> is_reproduceable_(C())
True
>>> check_reproduceable_(C())
>>> xnext4reproduceable_(C())
66666
>>> xnext4reproduceable7check_(C())
Traceback (most recent call last):
    ...
TypeError: <class 'int'>






>>> rp = Reproduceable5seq(range(5), 0)
>>> xnext4reproduceable_(rp)
NextEx(0, Reproduceable5seq(range(0, 5), 1))
>>> check_result5xnext4reproduceable_(xnext4reproduceable_(rp))
>>> xnext4reproduceable7check_(rp)
NextEx(0, Reproduceable5seq(range(0, 5), 1))



>>> rp = Reproduceable5seq('', 0)
>>> xnext4reproduceable_(rp)
StopEx(0)
>>> check_result5xnext4reproduceable_(xnext4reproduceable_(rp))
>>> xnext4reproduceable7check_(rp)
StopEx(0)

>>> next(iter_pairs4reproduceable_(Reproduceable5seq('', 0)))
Traceback (most recent call last):
    ...
StopIteration: 0
>>> next(iter_fsts4reproduceable_(Reproduceable5seq('', 0)))
Traceback (most recent call last):
    ...
StopIteration: 0
>>> next(iter_snds4reproduceable_(Reproduceable5seq('', 0)))
Traceback (most recent call last):
    ...
StopIteration: 0













>>> from itertools import islice

Reproduceable7repeat
>>> rp = Reproduceable7repeat(999, 3)
>>> rp
Reproduceable7repeat(999, 3)
>>> [*iter_fsts4reproduceable_(rp)]
[999, 999, 999]
>>> [*iter_snds4reproduceable_(rp)]
[Reproduceable7repeat(999, 2), Reproduceable7repeat(999, 1), Reproduceable7repeat(999, 0)]

>>> rp = Reproduceable7repeat(999, -1)
>>> rp
Reproduceable7repeat(999, -1)
>>> [*islice(iter_fsts4reproduceable_(rp), 5)]
[999, 999, 999, 999, 999]
>>> [*islice(iter_snds4reproduceable_(rp), 5)]
[Reproduceable7repeat(999, -1), Reproduceable7repeat(999, -1), Reproduceable7repeat(999, -1), Reproduceable7repeat(999, -1), Reproduceable7repeat(999, -1)]


Reproduceable7customized_repr
>>> rp = Reproduceable7customized_repr(lambda rp:f'<{rp!r}>', Reproduceable7repeat(999, 3))
>>> rp
<Reproduceable7repeat(999, 3)>
>>> str(rp) #doctest: +ELLIPSIS
'Reproduceable7customized_repr(<function <lambda> at 0x...>, Reproduceable7repeat(999, 3))'
>>> [*iter_fsts4reproduceable_(rp)]
[999, 999, 999]
>>> [*iter_snds4reproduceable_(rp)]
[<Reproduceable7repeat(999, 2)>, <Reproduceable7repeat(999, 1)>, <Reproduceable7repeat(999, 0)>]





Reproduceable7cached_oresult
Reproduceable7tmay_prev_oresult
>>> rp0 = Reproduceable7cached_oresult(Reproduceable5seq(range(2), 0))
>>> rp0
Reproduceable7cached_oresult(Reproduceable5seq(range(0, 2), 0))
>>> rp0.oresult
0
>>> [*iter_fsts4reproduceable_(rp0)]
[0, 1]
>>> (oresult0, rp1) = xnext4reproduceable_(rp0)
>>> (oresult1, rp2) = xnext4reproduceable_(rp1)
>>> rp1.oresult
1
>>> rp2.exit_status
2
>>> rp2.oresult
Traceback (most recent call last):
    ...
ValueError
>>> rp1.exit_status
Traceback (most recent call last):
    ...
ValueError


>>> rp0 = Reproduceable7tmay_prev_oresult((), Reproduceable5seq(range(2), 0))
>>> rp0
Reproduceable7tmay_prev_oresult((), Reproduceable5seq(range(0, 2), 0))
>>> rp0.prev_oresult
Traceback (most recent call last):
    ...
ValueError
>>> [*iter_fsts4reproduceable_(rp0)]
[0, 1]
>>> (oresult0, rp1) = xnext4reproduceable_(rp0)
>>> (oresult1, rp2) = xnext4reproduceable_(rp1)
>>> rp1.prev_oresult
0
>>> rp2.prev_oresult
1
>>> rp1
Reproduceable7tmay_prev_oresult((0,), Reproduceable5seq(range(0, 2), 1))





list_pairs4reproduceable_
    list_fsts4reproduceable_
    list_snds4reproduceable_

Reproduceable7transform_via_ops
    the_ops4transform7stated7echo
        get_ops4transform7stated7echo_
    StatedTransformOps7fork
    StatedTransformOps
    StatedTransformOps7rdiff
    StatedTransformOps7foldl
    StatedTransformOps7fmap

>>> ops_ls = []
>>> st0_ls = []

>>> get_ops4transform7stated7echo_() is the_ops4transform7stated7echo
True
>>> ops = the_ops4transform7stated7echo
>>> ops
StatedTransformOps7echo()
>>> rp = Reproduceable7transform_via_ops(ops, None, Reproduceable5seq(range(0, 2), 0))
>>> pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp
Reproduceable7transform_via_ops(StatedTransformOps7echo(), None, Reproduceable5seq(range(0, 2), 0))
>>> [*iter_fsts4reproduceable_(rp)]
[0, 1]
>>> list_pairs4reproduceable_(rp, with_exit_status=True)
([(0, Reproduceable7transform_via_ops(StatedTransformOps7echo(), None, Reproduceable5seq(range(0, 2), 1))), (1, Reproduceable7transform_via_ops(StatedTransformOps7echo(), None, Reproduceable5seq(range(0, 2), 2)))], 2)
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
([0, 1], 2)
>>> list_snds4reproduceable_(rp, with_exit_status=True)
([Reproduceable7transform_via_ops(StatedTransformOps7echo(), None, Reproduceable5seq(range(0, 2), 1)), Reproduceable7transform_via_ops(StatedTransformOps7echo(), None, Reproduceable5seq(range(0, 2), 2))], 2)
>>> rp__echo = rp


>>> ops = StatedTransformOps7fork(False, [the_ops4transform7stated7echo]*3)
>>> rp = Reproduceable7transform_via_ops(ops, (None,)*3, Reproduceable5seq(range(0, 2), 0))
>>> pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp
Reproduceable7transform_via_ops(StatedTransformOps7fork(False, (StatedTransformOps7echo(), StatedTransformOps7echo(), StatedTransformOps7echo())), (None, None, None), Reproduceable5seq(range(0, 2), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
([(0, 0, 0), (1, 1, 1)], (2, 2, 2))


>>> ops = StatedTransformOps7fork(True, [the_ops4transform7stated7echo]*3)
>>> rp = Reproduceable7transform_via_ops(ops, (None,)*3, Reproduceable5seq(range(0, 2), 0))
>>> #pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp
Reproduceable7transform_via_ops(StatedTransformOps7fork(True, (StatedTransformOps7echo(), StatedTransformOps7echo(), StatedTransformOps7echo())), (None, None, None), Reproduceable5seq(range(0, 2), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
([(0, 0, 0), (1, 1, 1)], ((None, None, None), (2, 2, 2)))


>>> ops = StatedTransformOps(lambda st, oresult6IN, /: (f'{st}:{oresult6IN}', st+oresult6IN))
>>> rp = Reproduceable7transform_via_ops(ops, 0, Reproduceable5seq(range(0, 9), 0))
>>> pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps(<function <lambda> at 0x...>), 0, Reproduceable5seq(range(0, 9), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
(['0:0', '0:1', '1:2', '3:3', '6:4', '10:5', '15:6', '21:7', '28:8'], (36, 9))

>>> ops = StatedTransformOps(lambda st, oresult6IN, /: (f'{st}:{oresult6IN}', st+oresult6IN), lambda st, exit_status6IN, /: f'{st}:{exit_status6IN}')
>>> rp = Reproduceable7transform_via_ops(ops, 0, Reproduceable5seq(range(0, 9), 0))
>>> pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps(<function <lambda> at 0x...>, <function <lambda> at 0x...>), 0, Reproduceable5seq(range(0, 9), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
(['0:0', '0:1', '1:2', '3:3', '6:4', '10:5', '15:6', '21:7', '28:8'], '36:9')


>>> ops = StatedTransformOps7rdiff(lambda oresult6IN_jmm, oresult6IN_j, /: f'{oresult6IN_jmm}:{oresult6IN_j}')
>>> rp = Reproduceable7transform_via_ops(ops, 999, Reproduceable5seq(range(0, 9), 0))
>>> pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7rdiff(<function <lambda> at 0x...>), 999, Reproduceable5seq(range(0, 9), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
(['999:0', '0:1', '1:2', '2:3', '3:4', '4:5', '5:6', '6:7', '7:8'], (8, 9))





>>> ops = StatedTransformOps7foldl(lambda st, oresult6IN, /: st+oresult6IN)
>>> rp = Reproduceable7transform_via_ops(ops, 1000, Reproduceable5seq(range(0, 9), 0))
>>> pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7foldl(<function <lambda> at 0x...>), 1000, Reproduceable5seq(range(0, 9), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
([1000, 1001, 1003, 1006, 1010, 1015, 1021, 1028, 1036], (1036, 9))
>>> rp__sum1000 = rp


>>> ops = StatedTransformOps7foldl(lambda st, oresult6IN, /: st+oresult6IN, lambda st, exit_status6IN, /: f'{st}:{exit_status6IN}')
>>> rp = Reproduceable7transform_via_ops(ops, 1000, Reproduceable5seq(range(0, 9), 0))
>>> pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7foldl(<function <lambda> at 0x...>, <function <lambda> at 0x...>), 1000, Reproduceable5seq(range(0, 9), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
([1000, 1001, 1003, 1006, 1010, 1015, 1021, 1028, 1036], '1036:9')




>>> ops = StatedTransformOps7fmap(lambda oresult6IN, /: 111*oresult6IN)
>>> rp = Reproduceable7transform_via_ops(ops, 1000, Reproduceable5seq(range(0, 9), 0))
>>> pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7fmap(<function <lambda> at 0x...>), 1000, Reproduceable5seq(range(0, 9), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
([0, 111, 222, 333, 444, 555, 666, 777, 888], 9)

>>> ops = StatedTransformOps7fmap(lambda oresult6IN, /: 111*oresult6IN, lambda exit_status6IN, /: f':{exit_status6IN}')
>>> rp = Reproduceable7transform_via_ops(ops, 1000, Reproduceable5seq(range(0, 9), 0))
>>> pass;ops_ls.append(rp.ops4transform7stated); st0_ls.append(rp.initial_state)
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7fmap(<function <lambda> at 0x...>, <function <lambda> at 0x...>), 1000, Reproduceable5seq(range(0, 9), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
([0, 111, 222, 333, 444, 555, 666, 777, 888], ':9')
>>> rp__mul111 = rp




>>> #ops_ls; st0_ls;
>>> ops = StatedTransformOps7fork(False, ops_ls)
>>> rp = Reproduceable7transform_via_ops(ops, tuple(st0_ls), Reproduceable5seq(range(0, 9), 0))
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7fork(False, (StatedTransformOps7echo(), ...)), (None, (None, None, None), 0, 0, 999, 1000, 1000, 1000, 1000), Reproduceable5seq(range(0, 9), 0))
>>> ls6False = list_fsts4reproduceable_(rp, with_exit_status=True)
>>> ls6False
([(0, (0, 0, 0), '0:0', '0:0', '999:0', 1000, 1000, 0, 0), (1, (1, 1, 1), '0:1', '0:1', '0:1', 1001, 1001, 111, 111), (2, (2, 2, 2), '1:2', '1:2', '1:2', 1003, 1003, 222, 222), (3, (3, 3, 3), '3:3', '3:3', '2:3', 1006, 1006, 333, 333), (4, (4, 4, 4), '6:4', '6:4', '3:4', 1010, 1010, 444, 444), (5, (5, 5, 5), '10:5', '10:5', '4:5', 1015, 1015, 555, 555), (6, (6, 6, 6), '15:6', '15:6', '5:6', 1021, 1021, 666, 666), (7, (7, 7, 7), '21:7', '21:7', '6:7', 1028, 1028, 777, 777), (8, (8, 8, 8), '28:8', '28:8', '7:8', 1036, 1036, 888, 888)], (9, (9, 9, 9), (36, 9), '36:9', (8, 9), (1036, 9), '1036:9', 9, ':9'))

>>> ops = StatedTransformOps7fork(True, ops_ls)
>>> rp = Reproduceable7transform_via_ops(ops, tuple(st0_ls), Reproduceable5seq(range(0, 9), 0))
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7fork(True, (StatedTransformOps7echo(), ...)), (None, (None, None, None), 0, 0, 999, 1000, 1000, 1000, 1000), Reproduceable5seq(range(0, 9), 0))
>>> ls6True = list_fsts4reproduceable_(rp, with_exit_status=True)
>>> ls6True[0] == ls6False[0]
True
>>> ls6True[1]
((None, (None, None, None), 36, 36, 8, 1036, 1036, 1000, 1000), (9, (9, 9, 9), (36, 9), '36:9', (8, 9), (1036, 9), '1036:9', 9, ':9'))











    StatedTransformOps7flow
>>> rp_ls = [rp__mul111, rp__sum1000, rp__echo]
>>> ops_ls = [rp.ops4transform7stated for rp in rp_ls]
>>> st0_ls = [rp.initial_state for rp in rp_ls]
>>> #ops_ls; st0_ls;
>>> ops = StatedTransformOps7flow(False, ops_ls)
>>> rp = Reproduceable7transform_via_ops(ops, tuple(st0_ls), Reproduceable5seq(range(0, 9), 0))
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7flow(False, (StatedTransformOps7fmap(<function <lambda> at 0x...>, <function <lambda> at 0x...>), StatedTransformOps7foldl(<function <lambda> at 0x...>), StatedTransformOps7echo())), (1000, 1000, None), Reproduceable5seq(range(0, 9), 0))
>>> list_fsts4reproduceable_(rp, with_exit_status=True)
([1000, 1111, 1333, 1666, 2110, 2665, 3331, 4108, 4996], (4996, ':9'))


>>> ops = StatedTransformOps7flow(False, ops_ls, slice(None), slice(None))
>>> rp = Reproduceable7transform_via_ops(ops, tuple(st0_ls), Reproduceable5seq(range(0, 9), 0))
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7flow(False, (StatedTransformOps7fmap(<function <lambda> at 0x...>, <function <lambda> at 0x...>), StatedTransformOps7foldl(<function <lambda> at 0x...>), StatedTransformOps7echo()), slice(None, None, None), slice(None, None, None)), (1000, 1000, None), Reproduceable5seq(range(0, 9), 0))
>>> ls6False = list_fsts4reproduceable_(rp, with_exit_status=True)
>>> ls6False
([(0, 1000, 1000), (111, 1111, 1111), (222, 1333, 1333), (333, 1666, 1666), (444, 2110, 2110), (555, 2665, 2665), (666, 3331, 3331), (777, 4108, 4108), (888, 4996, 4996)], (':9', (4996, ':9'), (4996, ':9')))


>>> ops = StatedTransformOps7flow(True, ops_ls, slice(None), slice(None))
>>> rp = Reproduceable7transform_via_ops(ops, tuple(st0_ls), Reproduceable5seq(range(0, 9), 0))
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7flow(True, (StatedTransformOps7fmap(<function <lambda> at 0x...>, <function <lambda> at 0x...>), StatedTransformOps7foldl(<function <lambda> at 0x...>), StatedTransformOps7echo()), slice(None, None, None), slice(None, None, None)), (1000, 1000, None), Reproduceable5seq(range(0, 9), 0))
>>> ls6True = list_fsts4reproduceable_(rp, with_exit_status=True)
>>> ls6True[0] == ls6False[0]
True
>>> ls6True[1]
((1000, 4996, None), (':9', (4996, ':9'), (4996, ':9')))



#swap...
>>> rp_ls = [rp__mul111, rp__sum1000, rp__echo]
>>> rp_ls = [rp__sum1000, rp__echo, rp__mul111]
>>> ops_ls = [rp.ops4transform7stated for rp in rp_ls]
>>> st0_ls = [rp.initial_state for rp in rp_ls]
>>> #ops_ls; st0_ls;
>>> ops = StatedTransformOps7flow(False, ops_ls)
>>> rp = Reproduceable7transform_via_ops(ops, tuple(st0_ls), Reproduceable5seq(range(0, 9), 0))
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7flow(False, (StatedTransformOps7foldl(<function <lambda> at 0x...>), StatedTransformOps7echo(), StatedTransformOps7fmap(<function <lambda> at 0x...>, <function <lambda> at 0x...>))), (1000, None, 1000), Reproduceable5seq(range(0, 9), 0))
>>> ls6False = list_fsts4reproduceable_(rp, with_exit_status=True)
>>> ls6False
([111000, 111111, 111333, 111666, 112110, 112665, 113331, 114108, 114996], ':(1036, 9)')

>>> ops = StatedTransformOps7flow(True, ops_ls)
>>> rp = Reproduceable7transform_via_ops(ops, tuple(st0_ls), Reproduceable5seq(range(0, 9), 0))
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7flow(True, (StatedTransformOps7foldl(<function <lambda> at 0x...>), StatedTransformOps7echo(), StatedTransformOps7fmap(<function <lambda> at 0x...>, <function <lambda> at 0x...>))), (1000, None, 1000), Reproduceable5seq(range(0, 9), 0))
>>> ls6True = list_fsts4reproduceable_(rp, with_exit_status=True)
>>> ls6True[0] == ls6False[0]
True
>>> ls6True[1]
((1036, None, 1000), ':(1036, 9)')








>>> ops = StatedTransformOps7flow(False, ops_ls, slice(None), slice(None))
>>> rp = Reproduceable7transform_via_ops(ops, tuple(st0_ls), Reproduceable5seq(range(0, 9), 0))
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7flow(False, (StatedTransformOps7foldl(<function <lambda> at 0x...>), StatedTransformOps7echo(), StatedTransformOps7fmap(<function <lambda> at 0x...>, <function <lambda> at 0x...>)), slice(None, None, None), slice(None, None, None)), (1000, None, 1000), Reproduceable5seq(range(0, 9), 0))
>>> ls6False = list_fsts4reproduceable_(rp, with_exit_status=True)
>>> ls6False
([(1000, 1000, 111000), (1001, 1001, 111111), (1003, 1003, 111333), (1006, 1006, 111666), (1010, 1010, 112110), (1015, 1015, 112665), (1021, 1021, 113331), (1028, 1028, 114108), (1036, 1036, 114996)], ((1036, 9), (1036, 9), ':(1036, 9)'))

>>> ops = StatedTransformOps7flow(True, ops_ls, slice(None))
>>> rp = Reproduceable7transform_via_ops(ops, tuple(st0_ls), Reproduceable5seq(range(0, 9), 0))
>>> rp  #doctest: +ELLIPSIS
Reproduceable7transform_via_ops(StatedTransformOps7flow(True, (StatedTransformOps7foldl(<function <lambda> at 0x...>), StatedTransformOps7echo(), StatedTransformOps7fmap(<function <lambda> at 0x...>, <function <lambda> at 0x...>)), slice(None, None, None)), (1000, None, 1000), Reproduceable5seq(range(0, 9), 0))
>>> ls6True = list_fsts4reproduceable_(rp, with_exit_status=True)
>>> ls6True[0] == ls6False[0]
True
>>> ls6True[1]
((1036, None, 1000), ':(1036, 9)')












py_adhoc_call   seed.types.Reproduceable   @f
]]]'''#'''
__all__ = r'''
IStatedTransformOps
    IStatedTransformOps7fork
        IStatedTransformOps7fork7default_mixin
    IStatedTransformOps7flow
        IStatedTransformOps7flow7default_mixin
    IReproduceable
        IReproduceable7transform
            IReproduceable7fmap
            IReproduceable7transform_via_ops




IReproduceable
    is_reproduceable_
        check_reproduceable_

    xnext4reproduceable_
        xnext4reproduceable7check_
        check_result5xnext4reproduceable_
            ResultTypes4xnext
                NextEx
                StopEx

    Iter4IReproduceable
        iter_pairs4reproduceable_
            iter_fsts4reproduceable_
            iter_snds4reproduceable_
        list_pairs4reproduceable_
            list_fsts4reproduceable_
            list_snds4reproduceable_

IReproduceable
    Reproduceable5seq


    Reproduceable7chain5iterable
    Reproduceable7chain5reproduceable
    IReproduceable7transform
        IReproduceable7fmap
            Reproduceable7fmap
        Reproduceable7transform

        IReproduceable7transform7init
        IReproduceable7rdiff
            Reproduceable7rdiff
        IReproduceable7foldl
            Reproduceable7foldl

    Reproduceable7repeat
    IReproduceable7wrapper
        Reproduceable7customized_repr

    Reproduceable7cached_oresult
    Reproduceable7tmay_prev_oresult

    IReproduceable7transform7fork
    IReproduceable7transform_via_ops
        Reproduceable7transform_via_ops


IReproduceable
    Reproduceable5seq

    Reproduceable7chain5iterable
    Reproduceable7chain5reproduceable
    Reproduceable7fmap
    Reproduceable7transform
    Reproduceable7rdiff
    Reproduceable7foldl
    Reproduceable7transform_via_ops

    Reproduceable7repeat
    Reproduceable7customized_repr

    Reproduceable7cached_oresult
    Reproduceable7tmay_prev_oresult






IStatedTransformOps
    IReproduceable
    IStatedTransformOps7fork
        IReproduceable7transform7fork
        IStatedTransformOps7fork7default_mixin
            StatedTransformOps7fork
    IStatedTransformOps7flow
        IStatedTransformOps7flow7default_mixin
            StatedTransformOps7flow

    IStatedTransformOps7init
        StatedTransformOps

    IStatedTransformOps7fmap
        StatedTransformOps7fmap
        StatedTransformOps7echo
            the_ops4transform7stated7echo
                get_ops4transform7stated7echo_
    IStatedTransformOps7rdiff
        StatedTransformOps7rdiff
    IStatedTransformOps7foldl
        StatedTransformOps7foldl

IStatedTransformOps
    StatedTransformOps7fork
    StatedTransformOps7flow
    StatedTransformOps
    StatedTransformOps7rdiff
    StatedTransformOps7foldl
    StatedTransformOps7fmap
    StatedTransformOps7echo
        the_ops4transform7stated7echo
            get_ops4transform7stated7echo_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.types5py import curry1
    from seed.iters.generator_iterator_capturer import GeneratorIteratorCapturer
    from seed.iters.unzip import unzip# unzip_keys
    from seed.tiny_.containers import mk_tuple
    from seed.tiny_.check import check_type_le, check_type_is, check_may_, check_callable, check_type_in, check_int_ge, check_tmay, check_non_ABC, check_all_
    from seed.helper.repr_input import repr_helper
    from seed.tiny_.funcs import fst, snd
    from seed.data_funcs.lnkls import get_empty_lflnkls, lflnkls_ipush_left, lflnkls_ipop_left, lflnkls2iterable, lflnkls5reversed_iterable
    from seed.seq_tools.force_reversed import force_reversed

    from seed.types.CachedProperty import CachedProperty
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):

#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#.    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#.    #    def _check6make_(sf, /):
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

_NextEx = mk_namedtuple__check6make_(__name__, '_NextEx', 'oresult,tail')
    #followup,following,subsequent
    #tail_reproduceable
class NextEx(_NextEx):
    stopped = False
    def _check6make_(sf, /):
        #check_type_le(IReproduceable, tail_reproduceable)
        check_type_le(IReproduceable, sf.tail)
_StopEx = mk_namedtuple__check6make_(__name__, '_StopEx', 'exit_status')
class StopEx(_StopEx):
    #def _check6make_(sf, /): pass
    stopped = True
class _Type4ResultTypes4xnext(tuple):
    NextEx = NextEx
    StopEx = StopEx
ResultTypes4xnext = _Type4ResultTypes4xnext((NextEx, StopEx))
    #used:check_type_in
    #used:match-case * lazy_import__func7context{arbitrary_ok=True}
assert NextEx is ResultTypes4xnext.NextEx
assert StopEx is ResultTypes4xnext.StopEx

class IReproduceable(ABC):
    'reproduceable'
    __slots__ = ()
    @abstractmethod
    def ___xnext4reproduceable___(sf, /):
        'IReproduceable{x} -> (NextEx(x, IReproduceable{x}) | StopEx(exit_status))'
        #'IReproduceable{x} -> ((True, x, IReproduceable{x}) | (False, exit_status))'
    @classmethod
    def __subclasshook__(cls, cls7testing, /):
        #return _is_reproduceable_type_(cls)
        if cls is __class__:
            if any("___xnext4reproduceable___" in B.__dict__ for B in cls7testing.__mro__):
                return True
        return NotImplemented

#class StopReprodution(BaseException)
def check_result5xnext4reproduceable_(r, /):
    check_type_in(ResultTypes4xnext, r)
    return
r'''[[[
    match r:
        case tuple([bool(True), oresult, IReproduceable() as tail_reproduceable]):
            pass
        case tuple([bool(False), exit_status]):
            pass
        case bad:
            raise TypeError('xnext4reproduceable_()->???', bad)
    return
#]]]'''#'''

def is_reproduceable_(reproduceable, /):
    cls = type(reproduceable)
    return _is_reproduceable_type_(cls)
def _is_reproduceable_type_(cls, /):
    try:
        cls.___xnext4reproduceable___
    except AttributeError:
        return False
    return True
def _gcheck_reproduceable_(reproduceable, /):
    cls = type(reproduceable)
    try:
        return cls.___xnext4reproduceable___
    except AttributeError:
        raise TypeError('not IReproduceable:', cls)
def check_reproduceable_(reproduceable, /):
    _gcheck_reproduceable_(reproduceable)
        # ^TypeError
def xnext4reproduceable_(reproduceable, /, *, to_check=False):
    'IReproduceable{x} -> (NextEx(x, IReproduceable{x}) | StopEx(exit_status))'
    #'IReproduceable{x} -> ((True, x, IReproduceable{x}) | (False, exit_status))'
    ___xnext4reproduceable___ = _gcheck_reproduceable_(reproduceable)
        # ^TypeError
    r = ___xnext4reproduceable___(reproduceable)
    if to_check:
        check_result5xnext4reproduceable_(r)
    return r
def xnext4reproduceable7check_(reproduceable, /, *, to_check=True):
    'IReproduceable{x} -> (NextEx(x, IReproduceable{x}) | StopEx(exit_status))'
    #'IReproduceable{x} -> ((True, x, IReproduceable{x}) | (False, exit_status))'
    return xnext4reproduceable_(reproduceable, to_check=to_check)
def iter_fsts4reproduceable_(reproduceable, /):
    return map(fst, iter_pairs4reproduceable_(reproduceable))
def iter_snds4reproduceable_(reproduceable, /):
    return map(snd, iter_pairs4reproduceable_(reproduceable))
def iter_pairs4reproduceable_(reproduceable, /):
    #old:return iter(reproduceable)
    return Iter4IReproduceable(reproduceable)
def list_pairs4reproduceable_(reproduceable, /, *, with_exit_status=False, fst_only=False, snd_only=False):
    if fst_only and snd_only:raise TypeError
    it = iter_pairs4reproduceable_(reproduceable)
    if fst_only:
        it = map(fst, it)
    elif snd_only:
        it = map(snd, it)
    if with_exit_status:
        it = GeneratorIteratorCapturer(it)
    ls = list(it)
    if with_exit_status:
        [exit_status] = it.get_tmay_result()
        return (ls, exit_status)
    return ls
def list_fsts4reproduceable_(reproduceable, /, *, with_exit_status=False):
    return list_pairs4reproduceable_(reproduceable, with_exit_status=with_exit_status, fst_only=True)
def list_snds4reproduceable_(reproduceable, /, *, with_exit_status=False):
    return list_pairs4reproduceable_(reproduceable, with_exit_status=with_exit_status, snd_only=True)


r'''[[[
%s/def \zs\<xnext_\>\ze/___xnext4reproduceable___/g
%s/\([a-zA-Z_.]\+\)\.\<xnext_\>()/xnext4reproduceable_(\1)/g
0|1 --> bool --> NextEx|StopEx

TODO:只保留___xnext4reproduceable___
    StopReprodution(BaseException)
    iter_pairs4reproduceable_
    iter_fsts4reproduceable_
    iter_snds4reproduceable_
    check_result5xnext4reproduceable_
    check_reproduceable_ hasattr
    from seed.helper.Echo import theEcho
old:
    @abstractmethod
    def xnext_(sf, /):
        'IReproduceable{x} -> ((True, x, IReproduceable{x}) | (False, exit_status))'
    def __iter__(sf, /):
        '-> (Iter (x, IReproduceable)){return:exit_status}'
        return Iter4IReproduceable(sf)
    def iter_fsts_(sf, /):
        return map(fst, iter(sf))
    def iter_snds_(sf, /):
        return map(snd, iter(sf))
    def iter_pairs_(sf, /):
        return iter(sf)
#]]]'''#'''
class Iter4IReproduceable:
    def __init__(sf, reproduceable, /):
        check_type_le(IReproduceable, reproduceable)
        sf._rp = reproduceable
    def __repr__(sf, /):
        reproduceable = sf._rp
        return repr_helper(sf, reproduceable)
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        match xnext4reproduceable_(sf._rp):
            case NextEx(x, rp):
                #case (True, x, IReproduceable() as rp):
                sf._rp = rp
                return (x, rp)
            case StopEx(exit_status):
                #case (False, exit_status):
                raise StopIteration(exit_status)
            case bad:
                raise TypeError('xnext4reproduceable_()->???', bad)
check_non_ABC(Iter4IReproduceable)

class Reproduceable5seq(IReproduceable):
    '[x] -> IReproduceable{x}'
    ___no_slots_ok___ = True
    @classmethod
    def mk5seq_and_xidx_(cls, seq, j, /):
        return cls(seq, j)
    def __init__(sf, seq, j, /):
        assert 0 <= j <= len(seq)
        sf._ls = seq
        sf._j = j
    def __repr__(sf, /):
        return repr_helper(sf, sf.seq, sf.xidx)
    @property
    def seq(sf, /):
        return sf._ls
    @property
    def xidx(sf, /):
        return sf._j
    @override
    def ___xnext4reproduceable___(sf, /):
        ls = sf.seq
        j = sf.xidx
        if j == len(ls):
            return StopEx(j)
        cls = type(sf)
        ot = cls.mk5seq_and_xidx_(ls, 1+j)
        return NextEx(ls[j], ot)
check_non_ABC(Reproduceable5seq)


class Reproduceable7chain5iterable(IReproduceable):
    'Iter IReproduceable{x} -> IReproduceable{x}'
    ###############
    #vs:Reproduceable7chain5iterable
    #vs:Reproduceable7chain5reproduceable
    ###############
    ___no_slots_ok___ = True
    @classmethod
    def mk5lflnkls4reproduceable_(cls, lflnkls4reproduceable, /):
        return cls(lflnkls4reproduceable, is_lflnkls=True)
    def __init__(sf, reproduceables, /, *, is_lflnkls=False):
        lflnkls4reproduceable = reproduceables if is_lflnkls else lflnkls5reversed_iterable(force_reversed(reproduceables))
        sf._s = lflnkls4reproduceable
    def __repr__(sf, /):
        return repr_helper(sf, sf.list_reproduceables_())
    @property
    def _lflnkls4reproduceable_(sf, /):
        return sf._s
    def iter_reproduceables_(sf, /):
        return lflnkls2iterable(sf._lflnkls4reproduceable_)
    def list_reproduceables_(sf, /):
        return list(sf.iter_reproduceables_())
    @CachedProperty
    def _hway_xnext_(sf, /):
        _0_lflnk = sf._lflnkls4reproduceable_
        y = None
        while _0_lflnk:
            (_1_lflnk, rp) = lflnkls_ipop_left(_0_lflnk)
            match xnext4reproduceable_(rp):
                case NextEx(x, _rp):
                    #bug:_2_lflnk = lflnkls_ipush_left(_1_lflnk, _rp)
                    (_2_lflnk, _None) = lflnkls_ipush_left(_1_lflnk, _rp)
                    return (x, _2_lflnk)
                case StopEx(y):
                    _0_lflnk = _1_lflnk
                    continue
                case bad:
                    raise TypeError(bad)
            #end-match xnext4reproduceable_(rp):
            raise 000
        #end-while 1:
        return (y,)
    @override
    def ___xnext4reproduceable___(sf, /):
        match sf._hway_xnext_:
            case (x, _2_lflnk):
                cls = type(sf)
                ot = cls.mk5lflnkls4reproduceable_(_2_lflnk)
                return NextEx(x, ot)
            case (y,):
                return StopEx(y)
        raise 000
check_non_ABC(Reproduceable7chain5iterable)
class Reproduceable7chain5reproduceable(IReproduceable):
    'IReproduceable{IReproduceable{x}} -> IReproduceable{x}'
    ###############
    #vs:Reproduceable7chain5iterable
    #vs:Reproduceable7chain5reproduceable
    ###############
    # use Reproduceable5seq => [IReproduceable{x}] -> IReproduceable{IReproduceable{x}}
    # use Reproduceable7fmap => (a -> IReproduceable{x}) -> IReproduceable{a} -> IReproduceable{IReproduceable{x}}
    ___no_slots_ok___ = True
    @classmethod
    def mk5may_head_and_tail_reproduceable_(cls, may_head_reproduceable, tail_reproduceable4reproduceable, /):
        return cls(may_head_reproduceable, tail_reproduceable4reproduceable)
    def __init__(sf, may_head_reproduceable, tail_reproduceable4reproduceable, /):
        check_may_([check_type_le, IReproduceable], may_head_reproduceable)
        check_type_le(IReproduceable, tail_reproduceable4reproduceable)
        sf._mh = may_head_reproduceable
        sf._tl = tail_reproduceable4reproduceable
    def __repr__(sf, /):
        return repr_helper(sf, sf.may_head_reproduceable, sf.tail_reproduceable4reproduceable)
    @property
    def may_head_reproduceable(sf, /):
        return sf._mh
    @property
    def tail_reproduceable4reproduceable(sf, /):
        return sf._tl
    def list_reproduceables_(sf, /):
        return list(sf.iter_reproduceables_())
    def iter_reproduceables_(sf, /):
        if not None is (head_reproduceable:=sf.may_head_reproduceable):
            yield head_reproduceable
        yield from iter_fsts4reproduceable_(sf.tail_reproduceable4reproduceable)
        return
    def iter_head_and_tail_reproduceable_pairs_(sf, /):
        if not None is (head_reproduceable:=sf.may_head_reproduceable):
            yield (head_reproduceable, sf.tail_reproduceable4reproduceable)
        yield from iter_pairs4reproduceable_(sf.tail_reproduceable4reproduceable)
        return
    @CachedProperty
    def _hway_xnext_(sf, /):
        y = None
        for (head, tail) in sf.iter_head_and_tail_reproduceable_pairs_():
            match xnext4reproduceable_(head):
                case NextEx(x, _head):
                    return (x, _head, tail)
                case StopEx(y):
                    continue
                case bad:
                    raise TypeError(bad)
            #end-match xnext4reproduceable_(head):
            raise 000
        #end-for...:
        return (y,)
    @override
    def ___xnext4reproduceable___(sf, /):
        match sf._hway_xnext_:
            case (x, _head, tail):
                cls = type(sf)
                ot = cls.mk5may_head_and_tail_reproduceable_(_head, tail)
                    # [_head never be None]
                    # i.e. [head be None => at beginning]
                return NextEx(x, ot)
            case (y,):
                return StopEx(y)
        raise 000
check_non_ABC(Reproduceable7chain5reproduceable)

#.class IReproduceable7fmap(IReproduceable):
#.    '(x->y) -> IReproduceable{x} -> IReproduceable{y}'
#.    __slots__ = ()
#.    '(oresult6IN{j}->oresult6OUT{j}) -> IReproduceable{as IN[0:]} -> IReproduceable{as OUT[0:]}'
#.    @property
#.    @abstractmethod
#.    def reproduceable8input(sf, /):
#.        '-> IReproduceable{as IN[0:]} # vs: [sf :: IReproduceable{as OUT[0:]}]'
#.    @abstractmethod
#.    def transform7fmap_(sf, oresult6IN_j, /):
#.        'oresult6IN{j} -> oresult6OUT{j}'
#.        # vs:transform7stated_
#.        # vs:transform7fmap_#stateless
#.    @abstractmethod
#.    def mk5reproduceable8tail_input_(sf, reproduceable8tail_input, /):
#.        'IReproduceable{as IN[j:]} -> IReproduceable{as OUT[j:]}'
#.    def transform4exit_status7fmap_(sf, exit_status6IN, /):
#.        'exit_status6IN -> exit_status6OUT'
#.        exit_status6OUT = exit_status6IN
#.        return exit_status6OUT
#.    @override
#.    def ___xnext4reproduceable___(sf, /):
#.        rp = sf.reproduceable8input
#.        match xnext4reproduceable_(rp):
#.            case NextEx(x, _rp):
#.                y = sf.transform7fmap_(x)
#.                ot = sf.mk5reproduceable8tail_input_(_rp)
#.                return NextEx(y, ot)
#.            case StopEx(z):
#.                _z = sf.transform4exit_status7fmap_(z)
#.                return StopEx(_z)
#.            case bad:
#.                raise TypeError(bad)
#.        #end-match xnext4reproduceable_(rp):
#.        raise 000



class IStatedTransformOps(ABC):
    __slots__ = ()
    #used by:IReproduceable7transform_via_ops
    @abstractmethod
    def transform7stated_(sf, st_j, oresult6IN_j, /):
        'st{j} -> oresult6IN{j} -> (oresult6OUT{j}, st{1+j})'
    @abstractmethod
    def transform4exit_status7stated_(sf, st, exit_status6IN, /):
        'st -> exit_status6IN -> exit_status6OUT'

class IStatedTransformOps7fork(IStatedTransformOps):
    __slots__ = ()
    #########
    #used by:IReproduceable7transform7fork,IReproduceable7transform_via_ops
    #   like:itertools.tee()
    #   eg: lift oresult up from low_layer
    #########
    @override
    def transform7stated_(sf, st_j, oresult6IN_j, /):
        'st{j} -> oresult6IN{j} -> (oresult6OUT{j}, st{1+j})'
        seq4ops7branch = sf.branch_transform_ops_seq
        seq4st7branch__j = sf.unpack_state_(st_j)
        seq4oresult7branch6IN_j = sf.unpack_oresult6input_(oresult6IN_j)
        it4oresult7branch6OUT_and_st7branch = (transform_ops7branch.transform7stated_(st7branch__j, oresult7branch6IN_j) for transform_ops7branch, st7branch__j, oresult7branch6IN_j in zip(seq4ops7branch, seq4st7branch__j, seq4oresult7branch6IN_j))
        (seq4oresult7branch6OUT_j, seq4st7branch__jpp) = map(mk_tuple, unzip(2, it4oresult7branch6OUT_and_st7branch))
        (oresult6OUT_j, st_jpp) = sf.pack_oresult6output_and_state_(st_j, oresult6IN_j, seq4oresult7branch6OUT_j, seq4st7branch__jpp)
        return (oresult6OUT_j, st_jpp)
    @override
    def transform4exit_status7stated_(sf, st, exit_status6IN, /):
        'st -> exit_status6IN -> exit_status6OUT'
        seq4ops7branch = sf.branch_transform_ops_seq
        seq4st7branch = sf.unpack_state_(st)
        seq4exit_status7branch6IN = sf.unpack_exit_status6input_(exit_status6IN)
        seq4exit_status7branch6OUT = tuple(transform_ops7branch.transform4exit_status7stated_(st7branch, exit_status7branch6IN) for transform_ops7branch, st7branch, exit_status7branch6IN in zip(seq4ops7branch, seq4st7branch, seq4exit_status7branch6IN))
        exit_status6OUT = sf.pack_exit_status6output_(st, exit_status6IN, seq4exit_status7branch6OUT)
        return exit_status6OUT
    @property
    def num_branches(sf, /):
        '-> uint'
        #def arity(sf, /):
        return len(sf.branch_transform_ops_seq)
    #def dispatch_state_(sf, st, /):
    #def unpack_state_(sf, st, /):
    #def split_state_(sf, st, /):
    def unpack_state_(sf, st, /):
        'st -> [st7branch]{len=num_branches}'
        seq4st7branch = sf._unpack_state_(st)
        assert len(seq4st7branch) == sf.num_branches
        return seq4st7branch
    def unpack_oresult6input_(sf, oresult6IN, /):
        'oresult6IN -> [oresult7branch6IN]{len=num_branches}'
        seq4oresult7branch6IN = sf._unpack_oresult6input_(oresult6IN)
        assert len(seq4oresult7branch6IN) == sf.num_branches
        return seq4oresult7branch6IN
    def unpack_exit_status6input_(sf, exit_status6IN, /):
        'exit_status6IN -> [exit_status7branch6IN]{len=num_branches}'
        seq4exit_status7branch6IN = sf._unpack_exit_status6input_(exit_status6IN)
        assert len(seq4exit_status7branch6IN) == sf.num_branches
        return seq4exit_status7branch6IN
    def pack_oresult6output_and_state_(sf, st_j, oresult6IN_j, seq4oresult7branch6OUT_j, seq4st7branch__jpp, /):
        'st{j} -> oresult6IN{j} -> [oresult7branch6OUT{j}]{len=num_branches} -> [st7branch[1+j]]{len=num_branches} -> (oresult6OUT{j}, st{1+j})'
        assert len(seq4oresult7branch6OUT_j) == sf.num_branches
        assert len(seq4st7branch__jpp) == sf.num_branches
        (oresult6OUT_j, st_jpp) = sf._pack_oresult6output_and_state_(st_j, oresult6IN_j, seq4oresult7branch6OUT_j, seq4st7branch__jpp)
        return (oresult6OUT_j, st_jpp)
    def pack_exit_status6output_(sf, st, exit_status6IN, seq4exit_status7branch6OUT, /):
        'st -> exit_status6IN -> [exit_status7branch6OUT]{len=num_branches} -> exit_status6OUT'
        assert len(seq4exit_status7branch6OUT) == sf.num_branches
        exit_status6OUT = sf._pack_exit_status6output_(st, exit_status6IN, seq4exit_status7branch6OUT)
        return exit_status6OUT
    ######################
    @property
    @abstractmethod
    def branch_transform_ops_seq(sf, /):
        '-> [IStatedTransformOps]{len=num_branches}'
    @abstractmethod
    def _unpack_state_(sf, st, /):
        'st -> [st7branch]{len=num_branches}'
    @abstractmethod
    def _unpack_oresult6input_(sf, oresult6IN, /):
        'oresult6IN -> [oresult7branch6IN]{len=num_branches}'
    @abstractmethod
    def _unpack_exit_status6input_(sf, exit_status6IN, /):
        'exit_status6IN -> [exit_status7branch6IN]{len=num_branches}'
    @abstractmethod
    def _pack_oresult6output_and_state_(sf, st_j, oresult6IN_j, seq4oresult7branch6OUT_j, seq4st7branch__jpp, /):
        'st{j} -> oresult6IN{j} -> [oresult7branch6OUT{j}]{len=num_branches} -> [st7branch[1+j]]{len=num_branches} -> (oresult6OUT{j}, st{1+j})'
    @abstractmethod
    def _pack_exit_status6output_(sf, st, exit_status6IN, seq4exit_status7branch6OUT, /):
        'st -> exit_status6IN -> [exit_status7branch6OUT]{len=num_branches} -> exit_status6OUT'
    ######################

class IStatedTransformOps7flow(IStatedTransformOps):
    __slots__ = ()
    #########
    @override
    def transform7stated_(sf, st_j, oresult6IN_j, /):
        'st{j} -> oresult6IN{j} -> (oresult6OUT{j}, st{1+j})'
        seq4ops7segment = sf.segment_transform_ops_seq
        seq4st7segment__j = sf.unpack_state_(st_j)
        #.seq4oresult7segment6IN_j = sf.unpack_oresult6input_(oresult6IN_j)
        def __():
            oresult7segment6IN_j = oresult6IN_j
            for transform_ops7segment, st7segment__j in zip(seq4ops7segment, seq4st7segment__j):
                (oresult7segment6OUT_j, st7segment__jpp) = transform_ops7segment.transform7stated_(st7segment__j, oresult7segment6IN_j)
                yield (oresult7segment6OUT_j, st7segment__jpp)
                ##next segment:
                oresult7segment6IN_j = oresult7segment6OUT_j
        #end-def __():
        it4oresult7segment6OUT_and_st7segment = __()
        (seq4oresult7segment6OUT_j, seq4st7segment__jpp) = map(mk_tuple, unzip(2, it4oresult7segment6OUT_and_st7segment))
        (oresult6OUT_j, st_jpp) = sf.pack_oresult6output_and_state_(st_j, oresult6IN_j, seq4oresult7segment6OUT_j, seq4st7segment__jpp)
        return (oresult6OUT_j, st_jpp)
    @override
    def transform4exit_status7stated_(sf, st, exit_status6IN, /):
        'st -> exit_status6IN -> exit_status6OUT'
        seq4ops7segment = sf.segment_transform_ops_seq
        seq4st7segment = sf.unpack_state_(st)
        #.seq4exit_status7segment6IN = sf.unpack_exit_status6input_(exit_status6IN)
        def __():
            exit_status7segment6IN = exit_status6IN
            for transform_ops7segment, st7segment in zip(seq4ops7segment, seq4st7segment):
                exit_status7segment6OUT = transform_ops7segment.transform4exit_status7stated_(st7segment, exit_status7segment6IN)
                yield exit_status7segment6OUT
                ##next segment:
                exit_status7segment6IN = exit_status7segment6OUT
        #end-def __():
        seq4exit_status7segment6OUT = tuple(__())
        exit_status6OUT = sf.pack_exit_status6output_(st, exit_status6IN, seq4exit_status7segment6OUT)
        return exit_status6OUT
    @property
    def num_segmentes(sf, /):
        '-> uint'
        return len(sf.segment_transform_ops_seq)
    def unpack_state_(sf, st, /):
        'st -> [st7segment]{len=num_segmentes}'
        seq4st7segment = sf._unpack_state_(st)
        assert len(seq4st7segment) == sf.num_segmentes
        return seq4st7segment
    def pack_oresult6output_and_state_(sf, st_j, oresult6IN_j, seq4oresult7segment6OUT_j, seq4st7segment__jpp, /):
        'st{j} -> oresult6IN{j} -> [oresult7segment6OUT{j}]{len=num_segmentes} -> [st7segment[1+j]]{len=num_segmentes} -> (oresult6OUT{j}, st{1+j})'
        assert len(seq4oresult7segment6OUT_j) == sf.num_segmentes
        assert len(seq4st7segment__jpp) == sf.num_segmentes
        (oresult6OUT_j, st_jpp) = sf._pack_oresult6output_and_state_(st_j, oresult6IN_j, seq4oresult7segment6OUT_j, seq4st7segment__jpp)
        return (oresult6OUT_j, st_jpp)
    def pack_exit_status6output_(sf, st, exit_status6IN, seq4exit_status7segment6OUT, /):
        'st -> exit_status6IN -> [exit_status7segment6OUT]{len=num_segmentes} -> exit_status6OUT'
        assert len(seq4exit_status7segment6OUT) == sf.num_segmentes
        exit_status6OUT = sf._pack_exit_status6output_(st, exit_status6IN, seq4exit_status7segment6OUT)
        return exit_status6OUT
    ######################
    @property
    @abstractmethod
    def segment_transform_ops_seq(sf, /):
        '-> [IStatedTransformOps]{len=num_segmentes}'
    @abstractmethod
    def _unpack_state_(sf, st, /):
        'st -> [st7segment]{len=num_segmentes}'
    @abstractmethod
    def _pack_oresult6output_and_state_(sf, st_j, oresult6IN_j, seq4oresult7segment6OUT_j, seq4st7segment__jpp, /):
        'st{j} -> oresult6IN{j} -> [oresult7segment6OUT{j}]{len=num_segmentes} -> [st7segment[1+j]]{len=num_segmentes} -> (oresult6OUT{j}, st{1+j})'
    @abstractmethod
    def _pack_exit_status6output_(sf, st, exit_status6IN, seq4exit_status7segment6OUT, /):
        'st -> exit_status6IN -> [exit_status7segment6OUT]{len=num_segmentes} -> exit_status6OUT'
    ######################









class IStatedTransformOps7fork7default_mixin(IStatedTransformOps7fork):
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def to_include_state_in_exit_status6output(sf, /):
        '-> bool'
    ######################
    @override
    def _unpack_state_(sf, st, /):
        'st -> [st7branch]{len=num_branches}'
        seq4st7branch = st
        return seq4st7branch
    @override
    def _unpack_oresult6input_(sf, oresult6IN, /):
        'oresult6IN -> [oresult7branch6IN]{len=num_branches}'
        oresult7branch6IN = oresult6IN
        return (oresult7branch6IN,)*sf.num_branches
    @override
    def _unpack_exit_status6input_(sf, exit_status6IN, /):
        'exit_status6IN -> [exit_status7branch6IN]{len=num_branches}'
        exit_status7branch6IN = exit_status6IN
        return (exit_status7branch6IN,)*sf.num_branches
    @override
    def _pack_oresult6output_and_state_(sf, st_j, oresult6IN_j, seq4oresult7branch6OUT_j, seq4st7branch__jpp, /):
        'st{j} -> oresult6IN{j} -> [oresult7branch6OUT{j}]{len=num_branches} -> [st7branch[1+j]]{len=num_branches} -> (oresult6OUT{j}, st{1+j})'
        oresult6OUT_j = seq4oresult7branch6OUT_j
        st_jpp = seq4st7branch__jpp
        return (oresult6OUT_j, st_jpp)
    @override
    def _pack_exit_status6output_(sf, st, exit_status6IN, seq4exit_status7branch6OUT, /):
        'st -> exit_status6IN -> [exit_status7branch6OUT]{len=num_branches} -> exit_status6OUT'
        exit_status6OUT = seq4exit_status7branch6OUT if not sf.to_include_state_in_exit_status6output else (st, seq4exit_status7branch6OUT)
        return exit_status6OUT
    ######################
class IStatedTransformOps7flow7default_mixin(IStatedTransformOps7flow):
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def to_include_state_in_exit_status6output(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def key4exit_status6output(sf, /):
        '-> [int|slice]'
    @property
    @abstractmethod
    def key4oresult6output(sf, /):
        '-> [int|slice]'
    ######################
    @override
    def _unpack_state_(sf, st, /):
        'st -> [st7segment]{len=num_segmentes}'
        seq4st7segment = st
        return seq4st7segment
    @override
    def _pack_oresult6output_and_state_(sf, st_j, oresult6IN_j, seq4oresult7segment6OUT_j, seq4st7segment__jpp, /):
        'st{j} -> oresult6IN{j} -> [oresult7segment6OUT{j}]{len=num_segmentes} -> [st7segment[1+j]]{len=num_segmentes} -> (oresult6OUT{j}, st{1+j})'
        oresult6OUT_j = seq4oresult7segment6OUT_j[sf.key4oresult6output]
        st_jpp = seq4st7segment__jpp
        return (oresult6OUT_j, st_jpp)
    @override
    def _pack_exit_status6output_(sf, st, exit_status6IN, seq4exit_status7segment6OUT, /):
        'st -> exit_status6IN -> [exit_status7segment6OUT]{len=num_segmentes} -> exit_status6OUT'
        exit_status6OUT = seq4exit_status7segment6OUT[sf.key4exit_status6output]
        if sf.to_include_state_in_exit_status6output:
            exit_status6OUT = (st, exit_status6OUT)
        return exit_status6OUT
    ######################



class IReproduceable7transform(IReproduceable, IStatedTransformOps):
    'st -> (st->x->(y,st)) -> IReproduceable{x} -> IReproduceable{y}'
    __slots__ = ()
    r'''[[[
    #########
    IReproduceable7transform transform one input to one output
        vs:Reproduceable7chain5reproduceable is not IReproduceable7transform
    #########
    use Reproduceable7tmay_prev_oresult or (Reproduceable7chain5reproduceable+Reproduceable5seq) to include st_0/(x_0mm|y_0mm)
    #########
    st_0 -> (st_j->IN_j->(OUT_j,st_jpp)) -> IReproduceable{IN} -> IReproduceable{OUT}
        * [y_0mm:=st_0][y_jmm:=st_j][y_j:=IN_j][OUT_j:=dy_j{y_j-y_jmm}][st_jpp:=y_j]
        * [x_0mm:=st_0][x_jmm:=st_j][y_j:=IN_j][OUT_j:=x_j][st_jpp:=x_j]
    #########
    ==>>:
    y_0mm -> (y_jmm->y_j->dy_j) -> IReproduceable{y} -> IReproduceable{dy}
    x_0mm -> (x_jmm->y_j->x_j) -> IReproduceable{y} -> IReproduceable{x}
        f(x,y):=pow_(x,y)
            # @stage1
        g(x,y):=mul_(x,cached_pow_(x_0mm,y))
            # @stage2
    #########

    #]]]'''#'''
    @property
    @abstractmethod
    def reproduceable8input(sf, /):
        '-> IReproduceable{as IN[0:]} # vs: [sf :: IReproduceable{as OUT[0:]}]'
    @property
    @abstractmethod
    def initial_state(sf, /):
        '-> st{0}'
    @abstractmethod
    def transform7stated_(sf, st_j, oresult6IN_j, /):
        'st{j} -> oresult6IN{j} -> (oresult6OUT{j}, st{1+j})'
        # vs:transform7stated_
        # vs:transform7fmap_#stateless
    @abstractmethod
    def mk5tail_state_and_reproduceable8tail_input_(sf, tail_state, reproduceable8tail_input, /):
        'st{j} -> IReproduceable{as IN[j:]} -> IReproduceable{as OUT[j:]}'
    def transform4exit_status7stated_(sf, st, exit_status6IN, /):
        'st -> exit_status6IN -> exit_status6OUT'
        exit_status6OUT = (st, exit_status6IN)
        return exit_status6OUT
    @override
    def ___xnext4reproduceable___(sf, /):
        return sf.xnext4reproduceable7transform_()
    def xnext4reproduceable7transform_(sf, /, *, to_output_more=False):
        rp = sf.reproduceable8input
        st_0 = sf.initial_state
        xnext4rp = xnext4reproduceable_(rp)
        return sf.raw_xnext4reproduceable7transform_(rp, st_0, xnext4rp, to_output_more=to_output_more)
    def raw_xnext4reproduceable7transform_(sf, rp, st_0, xnext4rp, /, *, to_output_more=False):
        #to be used in IReproduceable7transform7fork
        match xnext4rp:
            #match xnext4reproduceable_(rp):
            case NextEx(x, _rp):
                (y, st_1) = sf.transform7stated_(st_0, x)
                ot = sf.mk5tail_state_and_reproduceable8tail_input_(st_1, _rp)
                if to_output_more:
                    y = ((sf,ot), (rp,_rp), (st_0,st_1), (x,y))
                return NextEx(y, ot)
            case StopEx(z):
                _z = sf.transform4exit_status7stated_(st_0, z)
                if to_output_more:
                    _z = (sf, rp, st_0, (z,_z))
                return StopEx(_z)
            case bad:
                raise TypeError(bad)
        #end-match xnext4reproduceable_(rp):
        raise 000

class IReproduceable7fmap(IReproduceable7transform):
    '(x->y) -> IReproduceable{x} -> IReproduceable{y} #stateless'
    __slots__ = ()
    '(oresult6IN{j}->oresult6OUT{j}) -> IReproduceable{as IN[0:]} -> IReproduceable{as OUT[0:]}'
    @abstractmethod
    def transform7fmap_(sf, oresult6IN_j, /):
        'oresult6IN{j} -> oresult6OUT{j}'
        # vs:transform7stated_
        # vs:transform7fmap_#stateless
    @abstractmethod
    def mk5reproduceable8tail_input_(sf, reproduceable8tail_input, /):
        'IReproduceable{as IN[j:]} -> IReproduceable{as OUT[j:]}'
    def transform4exit_status7fmap_(sf, exit_status6IN, /):
        'exit_status6IN -> exit_status6OUT'
        exit_status6OUT = exit_status6IN
        return exit_status6OUT

    #@override
    initial_state = None
    @override
    def transform7stated_(sf, st_j, oresult6IN_j, /):
        'st{j} -> oresult6IN{j} -> (oresult6OUT{j}, st{1+j})'
        assert st_j is None#initial_state
        oresult6OUT_j = sf.transform7fmap_(oresult6IN_j)
        st_jpp = st_j
        return (oresult6OUT_j, st_jpp)
    @override
    def mk5tail_state_and_reproduceable8tail_input_(sf, tail_state, reproduceable8tail_input, /):
        'st{j} -> IReproduceable{as IN[j:]} -> IReproduceable{as OUT[j:]}'
        assert tail_state is None#initial_state
        return sf.mk5reproduceable8tail_input_(reproduceable8tail_input)
    @override
    def transform4exit_status7stated_(sf, st, exit_status6IN, /):
        'st -> exit_status6IN -> exit_status6OUT'
        assert st is None#initial_state
        exit_status6OUT = sf.transform4exit_status7fmap_(exit_status6IN)
        return exit_status6OUT



class IReproduceable7transform_via_ops(IReproduceable7transform):
    __slots__ = ()
    @property
    @abstractmethod
    def ops4transform7stated(sf, /):
        '-> IStatedTransformOps{as IN[0:] -> OUT[0:]} # vs: [sf :: IReproduceable{as OUT[0:]}]'
    @override
    def transform7stated_(sf, st_j, oresult6IN_j, /):
        return sf.ops4transform7stated.transform7stated_(st_j, oresult6IN_j)
    @override
    def transform4exit_status7stated_(sf, st, exit_status6IN, /):
        return sf.ops4transform7stated.transform4exit_status7stated_(st, exit_status6IN)

class IReproduceable7transform7fork(IReproduceable7transform, IStatedTransformOps7fork):
    'st -> (st -> [st7branch]) -> (I -> [I7branch]) -> [(st7branch->I7branch->(O7branch,st7branch))] -> ([(O7branch,st7branch)]->(O,st)) -> IReproduceable{I} -> IReproduceable{O}'
    #'st -> (st -> (st7core, st7edge)) -> (I -> (I7core, I7edge)) -> (st7core->I7core->(O7core,st7core)) -> (st7edge->I7edge->(O7edge,st7edge)) -> ((O7core,st7core)->(O7edge,st7edge)->(O,st)) -> IReproduceable{I} -> IReproduceable{O}'
    'st -> (st->I->(O,st)) -> IReproduceable{I} -> IReproduceable{O}'
    __slots__ = ()
    #see:raw_xnext4reproduceable7transform_()




class IReproduceable7rdiff(IReproduceable7transform):
    'x -> (x->x->dx) -> IReproduceable{x} -> IReproduceable{dx} # flip __sub__'
    __slots__ = ()
    @abstractmethod
    def rdiff_(sf, oresult6IN_jmm, oresult6IN_j, /):
        'oresult6IN{j-1} -> oresult6IN{j} -> oresult6OUT{j}'
        return oresult6IN_j -oresult6IN_jmm
    @override
    def transform7stated_(sf, st_j, oresult6IN_j, /):
        'st{j} -> oresult6IN{j} -> (oresult6OUT{j}, st{1+j})'
        oresult6IN_jmm = st_j
        oresult6OUT_j = sf.rdiff_(oresult6IN_jmm, oresult6IN_j)
        st_jpp = oresult6IN_j
        return (oresult6OUT_j, st_jpp)


class IReproduceable7foldl(IReproduceable7transform):
    'z -> (z->x->z) -> IReproduceable{x} -> IReproduceable{z}'
    __slots__ = ()
    @abstractmethod
    def ljoin_(sf, oresult6OUT_jmm, oresult6IN_j, /):
        'oresult6OUT{j-1} -> oresult6IN{j} -> oresult6OUT{j}'
        return oresult6OUT_jmm +oresult6IN_j
    @override
    def transform7stated_(sf, st_j, oresult6IN_j, /):
        'st{j} -> oresult6IN{j} -> (oresult6OUT{j}, st{1+j})'
        oresult6OUT_jmm = st_j
        oresult6OUT_j = sf.ljoin_(oresult6OUT_jmm, oresult6IN_j)
        st_jpp = oresult6OUT_j
        return (oresult6OUT_j, st_jpp)

class IReproduceable7transform7init(IReproduceable7transform):
    ___no_slots_ok___ = True
    def __init__(sf, _op_, initial_state, reproduceable8input, /):
        check_callable(_op_)
        check_type_le(IReproduceable, reproduceable8input)
        sf._f = _op_
        sf._st = initial_state
        sf._rp = reproduceable8input
    @property
    @override
    def reproduceable8input(sf, /):
        return sf._rp
    @property
    @override
    def initial_state(sf, /):
        return sf._st
    @property
    @override
    def _op_(sf, /):
        return sf._f
    def __repr__(sf, /):
        return repr_helper(sf, sf._op_, sf.initial_state, sf.reproduceable8input)
    @override
    def mk5tail_state_and_reproduceable8tail_input_(sf, tail_state, reproduceable8tail_input, /):
        cls = type(sf)
        return cls(sf._op_, tail_state, reproduceable8tail_input)





class Reproduceable7fmap(IReproduceable7fmap):
    '(x->y) -> IReproduceable{x} -> IReproduceable{y}'
    #vs:Reproduceable7fmap
    #vs:Reproduceable7transform
    ___no_slots_ok___ = True
    def __init__(sf, transform7fmap_, reproduceable8input, /):
        check_callable(transform7fmap_)
        check_type_le(IReproduceable, reproduceable8input)
        sf._f = transform7fmap_
        sf._rp = reproduceable8input
    @property
    @override
    def reproduceable8input(sf, /):
        return sf._rp
    @property
    @override
    def transform7fmap_(sf, /):
        return sf._f
    def __repr__(sf, /):
        return repr_helper(sf, sf.transform7fmap_, sf.reproduceable8input)
    @override
    def mk5reproduceable8tail_input_(sf, reproduceable8tail_input, /):
        cls = type(sf)
        return cls(sf.transform7fmap_, reproduceable8tail_input)
check_non_ABC(Reproduceable7fmap)

class Reproduceable7transform(IReproduceable7transform7init):
    'st -> (st->x->(y,st)) -> IReproduceable{x} -> IReproduceable{y}'
    #vs:Reproduceable7fmap
    #vs:Reproduceable7transform
    ___no_slots_ok___ = True
    @property
    @override
    def transform7stated_(sf, /):
        return sf._op_
check_non_ABC(Reproduceable7transform)


class Reproduceable7rdiff(IReproduceable7transform7init, IReproduceable7rdiff):
    'x -> (x->x->dx) -> IReproduceable{x} -> IReproduceable{dx} # flip __sub__'
    ___no_slots_ok___ = True
    @property
    @override
    def rdiff_(sf, /):
        return sf._op_
check_non_ABC(Reproduceable7rdiff)
class Reproduceable7foldl(IReproduceable7transform7init, IReproduceable7foldl):
    'z -> (z->x->z) -> IReproduceable{x} -> IReproduceable{z}'
    ___no_slots_ok___ = True
    @property
    @override
    def ljoin_(sf, /):
        return sf._op_
check_non_ABC(Reproduceable7foldl)


class Reproduceable7repeat(IReproduceable):
    'z -> imay uint -> IReproduceable{z}'
    ___no_slots_ok___ = True
    def __init__(sf, oresult6OUT, imay_size, /):
        check_int_ge(-1, imay_size)
        sf._o = oresult6OUT
        sf._im = imay_size
    @property
    def the_oresult(sf, /):
        return sf._o
    @property
    def imay_size(sf, /):
        return sf._im
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_oresult, sf.imay_size)
    def mk5imay_size_(sf, imay_size, /):
        cls = type(sf)
        return cls(sf.the_oresult, imay_size)
    @override
    def ___xnext4reproduceable___(sf, /):
        oresult6OUT = sf.the_oresult
        imay_size = sf.imay_size
        if imay_size > 0:
            ot = sf.mk5imay_size_(imay_size-1)
        elif imay_size == 0:
            return StopEx(oresult6OUT)
        else:
            # [imay_size == -1]
            ot = sf
        ot
        return NextEx(oresult6OUT, ot)
check_non_ABC(Reproduceable7repeat)



class IReproduceable7wrapper(IReproduceable):
    __slots__ = ()
    @property
    @abstractmethod
    def the_wrapped_reproduceable(sf, /):
        '-> IReproduceable{as OUT[0:]}'
    @abstractmethod
    def mk5tail_reproduceable7wrapped_(sf, tail_reproduceable7wrapped, /):
        'IReproduceable{as OUT[j:]} -> IReproduceable{as OUT[j:]}'
    @override
    def ___xnext4reproduceable___(sf, /):
        r = xnext4reproduceable_(sf.the_wrapped_reproduceable)
        match r:
            case NextEx(x, tail7wrapped):
                tail = sf.mk5tail_reproduceable7wrapped_(tail7wrapped)
                return r if tail is tail7wrapped else NextEx(x, tail)
            case _:
                return r
        raise 000
class Reproduceable7customized_repr(IReproduceable7wrapper):
    ___no_slots_ok___ = True
    def __init__(sf, repr4reproduceable7wrapped_, reproduceable7wrapped, /):
        check_callable(repr4reproduceable7wrapped_)
        check_type_le(IReproduceable, reproduceable7wrapped)
        sf._f = repr4reproduceable7wrapped_
        sf._rp = reproduceable7wrapped
    @property
    def repr4reproduceable7wrapped_(sf, /):
        return sf._f
    @property
    @override
    def the_wrapped_reproduceable(sf, /):
        return sf._rp
    def __repr__(sf, /):
        s = sf.repr4reproduceable7wrapped_(sf.the_wrapped_reproduceable)
        check_type_is(str, s)
        return s
    def __str__(sf, /):
        return repr_helper(sf, sf.repr4reproduceable7wrapped_, sf.the_wrapped_reproduceable)
    @override
    def mk5tail_reproduceable7wrapped_(sf, tail_reproduceable7wrapped, /):
        cls = type(sf)
        return cls(sf.repr4reproduceable7wrapped_, tail_reproduceable7wrapped)
check_non_ABC(Reproduceable7customized_repr)

class Reproduceable7cached_oresult(IReproduceable7wrapper):
    ___no_slots_ok___ = True
    def __init__(sf, reproduceable7wrapped, /):
        check_type_le(IReproduceable, reproduceable7wrapped)
        sf._m = None#(Either exit_status, oresult)
        sf._rp = reproduceable7wrapped
    #@CachedProperty
    @property
    def xresult(sf, /):
        m = sf._m
        if None is m:
            xnext4reproduceable_(sf)
            m = sf._m
        return m
    @property
    def tmay_oresult(sf, /):
        match sf.xresult:
            case (True, oresult):
                return (oresult,)
            case (False, exit_status):
                return ()
        raise 000
    @property
    def tmay_exit_status(sf, /):
        match sf.xresult:
            case (True, oresult):
                return ()
            case (False, exit_status):
                return (exit_status,)
        raise 000
    @property
    def exit_status(sf, /):
        for exit_status in sf.tmay_exit_status:
            return exit_status
        raise ValueError
    @property
    def oresult(sf, /):
        for oresult in sf.tmay_oresult:
            return oresult
        raise ValueError
    @property
    @override
    def the_wrapped_reproduceable(sf, /):
        return sf._rp
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_wrapped_reproduceable)
    @override
    def mk5tail_reproduceable7wrapped_(sf, tail_reproduceable7wrapped, /):
        cls = type(sf)
        return cls(tail_reproduceable7wrapped)
    @override
    def ___xnext4reproduceable___(sf, /):
        r = super().___xnext4reproduceable___()
        if None is sf._m:
            match r:
                case NextEx(oresult):
                    either = (True, oresult)
                case StopEx(exit_status):
                    either = (False, exit_status)
                case bad:
                    raise TypeError(bad)
            either
            sf._m = either
        return r
check_non_ABC(Reproduceable7cached_oresult)

class Reproduceable7tmay_prev_oresult(IReproduceable):
    ___no_slots_ok___ = True
    def __init__(sf, tmay_prev_oresult, reproduceable7wrapped, /):
        check_tmay(tmay_prev_oresult)
        check_type_le(IReproduceable, reproduceable7wrapped)
        #sf._pv = prev_oresult
        sf._tm_pv = tmay_prev_oresult
        sf._rp = reproduceable7wrapped
    def __repr__(sf, /):
        return repr_helper(sf, sf.tmay_prev_oresult, sf.the_wrapped_reproduceable)
    @property
    def tmay_prev_oresult(sf, /):
        return sf._tm_pv
    @property
    def prev_oresult(sf, /):
        for prev_oresult in sf.tmay_prev_oresult:
            return prev_oresult
        raise ValueError
    @property
    def the_wrapped_reproduceable(sf, /):
        '-> IReproduceable{as OUT[0:]}'
        return sf._rp
    def mk5curr_oresult_and_tail_reproduceable7wrapped_(sf, curr_oresult, tail_reproduceable7wrapped, /):
        'IReproduceable{as OUT[j:]} -> IReproduceable{as OUT[j:]}'
        cls = type(sf)
        return cls((curr_oresult,), tail_reproduceable7wrapped)
    @override
    def ___xnext4reproduceable___(sf, /):
        r = xnext4reproduceable_(sf.the_wrapped_reproduceable)
        match r:
            case NextEx(x, tail7wrapped):
                tail = sf.mk5curr_oresult_and_tail_reproduceable7wrapped_(x, tail7wrapped)
                return NextEx(x, tail)
            case _:
                return r
        raise 000
check_non_ABC(Reproduceable7tmay_prev_oresult)
















class Reproduceable7transform_via_ops(IReproduceable7transform_via_ops):
    ___no_slots_ok___ = True
    def __init__(sf, ops4transform7stated, initial_state, reproduceable8input, /):
        check_type_le(IStatedTransformOps, ops4transform7stated)
        check_type_le(IReproduceable, reproduceable8input)
        sf._ops = ops4transform7stated
        sf._st = initial_state
        sf._rp = reproduceable8input
    def __repr__(sf, /):
        return repr_helper(sf, sf.ops4transform7stated, sf.initial_state, sf.reproduceable8input)
    @property
    @override
    def ops4transform7stated(sf, /):
        return sf._ops
    @property
    @override
    def initial_state(sf, /):
        return sf._st
    @property
    @override
    def reproduceable8input(sf, /):
        return sf._rp
    @override
    def mk5tail_state_and_reproduceable8tail_input_(sf, tail_state, reproduceable8tail_input, /):
        cls = type(sf)
        return cls(sf.ops4transform7stated, tail_state, reproduceable8tail_input)

check_non_ABC(Reproduceable7transform_via_ops)


class IStatedTransformOps7fmap(IStatedTransformOps):
    '#stateless'
    __slots__ = ()
    @abstractmethod
    def transform7fmap_(sf, oresult6IN_j, /):
        'oresult6IN{j} -> oresult6OUT{j}'
    @abstractmethod
    def transform4exit_status7fmap_(sf, exit_status6IN, /):
        'exit_status6IN -> exit_status6OUT'
    @override
    def transform7stated_(sf, st_j, oresult6IN_j, /):
        'st{j} -> oresult6IN{j} -> (oresult6OUT{j}, st{1+j})'
        oresult6OUT_j = sf.transform7fmap_(oresult6IN_j)
        st_jpp = st_j
        return (oresult6OUT_j, st_jpp)
    @override
    def transform4exit_status7stated_(sf, st, exit_status6IN, /):
        'st -> exit_status6IN -> exit_status6OUT'
        exit_status6OUT = sf.transform4exit_status7fmap_(exit_status6IN)
        return exit_status6OUT
class StatedTransformOps7echo(IStatedTransformOps7fmap):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf)

    @override
    def transform7fmap_(sf, oresult6IN_j, /):
        'oresult6IN{j} -> oresult6OUT{j}'
        oresult6OUT_j = oresult6IN_j
        return oresult6OUT_j
    #@override
    transform4exit_status7fmap_ = IReproduceable7fmap.transform4exit_status7fmap_
    #.@override
    #.def transform4exit_status7fmap_(sf, exit_status6IN, /):
    #.    'exit_status6IN -> exit_status6OUT'
    #.    exit_status6OUT = exit_status6IN
    #.    return exit_status6OUT
check_non_ABC(StatedTransformOps7echo)
the_ops4transform7stated7echo = StatedTransformOps7echo()
def get_ops4transform7stated7echo_():
    return the_ops4transform7stated7echo

class IStatedTransformOps7rdiff(IStatedTransformOps):
    __slots__ = ()
    #@abstractmethod
    rdiff_ = IReproduceable7rdiff.rdiff_
    #@override
    transform7stated_ = IReproduceable7rdiff.transform7stated_
    #@override
    #transform4exit_status7stated_ = IReproduceable7rdiff.transform4exit_status7stated_#@IReproduceable7transform
class IStatedTransformOps7foldl(IStatedTransformOps):
    __slots__ = ()
    #@abstractmethod
    ljoin_ = IReproduceable7foldl.ljoin_
    #@override
    transform7stated_ = IReproduceable7foldl.transform7stated_
    #@override
    #transform4exit_status7stated_ = IReproduceable7foldl.transform4exit_status7stated_#@IReproduceable7transform


class IStatedTransformOps7init(IStatedTransformOps):
    ___no_slots_ok___ = True
    def __init__(sf, _op1_, _may_op2_=None, /):
        check_callable(_op1_)
        check_may_(check_callable, _may_op2_)
        sf._f1 = _op1_
        sf._mf2 = _may_op2_
    @property
    @override
    def _op1_(sf, /):
        return sf._f1
    @property
    @override
    def _may_op2_(sf, /):
        return sf._mf2
    def __repr__(sf, /):
        if not None is sf._may_op2_:
            return repr_helper(sf, sf._op1_, sf._may_op2_)
        return repr_helper(sf, sf._op1_)
    @property
    @override
    def transform4exit_status7stated_(sf, /):
        if not None is (op2:=sf._may_op2_):
            return op2
        f = IReproduceable7transform.transform4exit_status7stated_
        return curry1(f, sf)
    #.@override
    #.def transform4exit_status7stated_(sf, st, exit_status6IN, /):
    #.    'st -> exit_status6IN -> exit_status6OUT'
    #.    if not None is (op2:=sf._may_op2_):
    #.        exit_status6OUT = op2(st, exit_status6IN)
    #.    else:
    #.        exit_status6OUT = (st, exit_status6IN)
    #.    return exit_status6OUT

class StatedTransformOps(IStatedTransformOps7init, IStatedTransformOps):
    '(st->x->(y,st))'
    ___no_slots_ok___ = True
    @property
    @override
    def transform7stated_(sf, /):
        return sf._op1_
check_non_ABC(StatedTransformOps)

class StatedTransformOps7rdiff(IStatedTransformOps7init, IStatedTransformOps7rdiff):
    '(x->x->dx) # flip __sub__'
    ___no_slots_ok___ = True
    @property
    @override
    def rdiff_(sf, /):
        return sf._op1_
check_non_ABC(StatedTransformOps7rdiff)
class StatedTransformOps7foldl(IStatedTransformOps7init, IStatedTransformOps7foldl):
    '(z->x->z)'
    ___no_slots_ok___ = True
    @property
    @override
    def ljoin_(sf, /):
        return sf._op1_
check_non_ABC(StatedTransformOps7foldl)

class StatedTransformOps7fmap(IStatedTransformOps7init, IStatedTransformOps7fmap):
    '(x->y)'
    ___no_slots_ok___ = True
    @property
    @override
    def transform7fmap_(sf, /):
        return sf._op1_
    #@override#using:
    transform4exit_status7stated_ = IStatedTransformOps7fmap.transform4exit_status7stated_
    @property
    @override
    def transform4exit_status7fmap_(sf, /):
        if not None is (op2:=sf._may_op2_):
            return op2
        #f = StatedTransformOps7echo.transform4exit_status7fmap_
        f = IReproduceable7fmap.transform4exit_status7fmap_
        return curry1(f, sf)
check_non_ABC(StatedTransformOps7fmap)




class StatedTransformOps7fork(IStatedTransformOps7fork7default_mixin):
    ___no_slots_ok___ = True
    def __init__(sf, to_include_state_in_exit_status6output, branch_transform_ops_seq, /):
        check_type_is(bool, to_include_state_in_exit_status6output)
        branch_transform_ops_seq = mk_tuple(branch_transform_ops_seq)
        check_all_([check_type_le, IStatedTransformOps], branch_transform_ops_seq)
        sf._b = to_include_state_in_exit_status6output
        sf._opss = branch_transform_ops_seq
    def __repr__(sf, /):
        return repr_helper(sf, sf.to_include_state_in_exit_status6output, sf.branch_transform_ops_seq)

    @property
    @override
    def branch_transform_ops_seq(sf, /):
        return sf._opss
    @property
    @override
    def to_include_state_in_exit_status6output(sf, /):
        return sf._b
check_non_ABC(StatedTransformOps7fork)

class StatedTransformOps7flow(IStatedTransformOps7flow7default_mixin):
    ___no_slots_ok___ = True
    def __init__(sf, to_include_state_in_exit_status6output, segment_transform_ops_seq, /, key4oresult6output=-1, key4exit_status6output=-1):
        check_type_is(bool, to_include_state_in_exit_status6output)
        segment_transform_ops_seq = mk_tuple(segment_transform_ops_seq)
        check_all_([check_type_le, IStatedTransformOps], segment_transform_ops_seq)
        segment_transform_ops_seq[key4oresult6output]
        segment_transform_ops_seq[key4exit_status6output]
        sf._b = to_include_state_in_exit_status6output
        sf._opss = segment_transform_ops_seq
        sf._k4o = key4oresult6output
        sf._k4e = key4exit_status6output
    def __repr__(sf, /):
        L = sf.num_segmentes
        k4o = _to_neg_one_if_possible(L, sf.key4oresult6output)
        k4e = _to_neg_one_if_possible(L, sf.key4exit_status6output)
        args = [k4o, k4e]
        match args:
            case [-1, -1]:
                args.clear()
            case [_, -1]:
                args.pop()
        return repr_helper(sf, sf.to_include_state_in_exit_status6output, sf.segment_transform_ops_seq, *args)

    @property
    @override
    def segment_transform_ops_seq(sf, /):
        return sf._opss
    @property
    @override
    def to_include_state_in_exit_status6output(sf, /):
        return sf._b
    @property
    @override
    def key4oresult6output(sf, /):
        return sf._k4o
    @property
    @override
    def key4exit_status6output(sf, /):
        return sf._k4e
check_non_ABC(StatedTransformOps7flow)
def _to_neg_one_if_possible(L, x, /):
    return -1 if x in [L-1] else x
def _eq_neg_one(L, x, /):
    match x:
        case -1:
            return True
        case int() as y if y == L-1:
            return True
    return False




__all__
from seed.types.Reproduceable import is_reproduceable_, check_reproduceable_
from seed.types.Reproduceable import xnext4reproduceable_, xnext4reproduceable7check_, check_result5xnext4reproduceable_
from seed.types.Reproduceable import NextEx, StopEx, ResultTypes4xnext

from seed.types.Reproduceable import iter_pairs4reproduceable_, iter_fsts4reproduceable_, iter_snds4reproduceable_
from seed.types.Reproduceable import list_pairs4reproduceable_, list_fsts4reproduceable_, list_snds4reproduceable_
from seed.types.Reproduceable import Iter4IReproduceable
from seed.types.Reproduceable import IReproduceable, IReproduceable7fmap, IReproduceable7transform, IReproduceable7transform7init, IReproduceable7rdiff, IReproduceable7foldl, IReproduceable7wrapper
from seed.types.Reproduceable import Reproduceable5seq, Reproduceable7chain5iterable, Reproduceable7chain5reproduceable, Reproduceable7fmap, Reproduceable7transform, Reproduceable7rdiff, Reproduceable7foldl, Reproduceable7repeat, Reproduceable7customized_repr, Reproduceable7cached_oresult, Reproduceable7tmay_prev_oresult, Reproduceable7transform_via_ops

from seed.types.Reproduceable import IStatedTransformOps, IStatedTransformOps7fork, IStatedTransformOps7fork7default_mixin, IStatedTransformOps7flow, IStatedTransformOps7flow7default_mixin
from seed.types.Reproduceable import StatedTransformOps7fork, StatedTransformOps7flow, StatedTransformOps, StatedTransformOps7rdiff, StatedTransformOps7foldl, StatedTransformOps7fmap, StatedTransformOps7echo, the_ops4transform7stated7echo, get_ops4transform7stated7echo_


from seed.types.Reproduceable import *
