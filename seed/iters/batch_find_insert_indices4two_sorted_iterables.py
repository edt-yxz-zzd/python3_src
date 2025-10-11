#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/batch_find_insert_indices4two_sorted_iterables.py
view ../../python3_src/seed/iters/merge_two_sorted_iterables.py

seed.iters.batch_find_insert_indices4two_sorted_iterables
py -m nn_ns.app.debug_cmd   seed.iters.batch_find_insert_indices4two_sorted_iterables -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.batch_find_insert_indices4two_sorted_iterables:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.iters.batch_find_insert_indices4two_sorted_iterables:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
]]


'#'; __doc__ = r'#'
>>> batch_find_insert_indices4two_sorted_iterables([], [1,23])
((), (0, 0))
>>> batch_find_insert_indices4two_sorted_iterables([0,1,2,22,24,25], [1,23])
((0, 0, 1, 1, 2, 2), (2, 4))


py_adhoc_call   seed.iters.batch_find_insert_indices4two_sorted_iterables   @f
]]]'''#'''
__all__ = r'''
batch_find_insert_indices4two_sorted_iterables
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import operator as opss
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_

merge_two_sorted_iterables = lazy_import4func_('seed.iters.merge_two_sorted_iterables', 'merge_two_sorted_iterables', __name__)
if 0:from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
#def merge_two_sorted_iterables(lefts, rights, /, *, left_key=None, right_key=None, before=None, Left=None, Right=None):
#    ':: (a->b->Bool) -> [a] -> [b] -> [Either a b] # before :: KeyA -> KeyB -> Bool'



lazy_import4funcs_('seed.tiny', 'ifNone,echo,fst,snd', __name__)
if 0:from seed.tiny import ifNone,echo,fst,snd #,mk_tuple,print_err

lazy_import4funcs_('seed.types.Either', 'mk_Left,mk_Right', __name__)
if 0:from seed.types.Either import mk_Left,mk_Right

lazy_import4funcs_('seed.func_tools.dot_', 'dot_', __name__)
if 0:from seed.func_tools.dot_ import dot_

___end_mark_of_excluded_global_names__0___ = ...


def batch_find_insert_indices4two_sorted_iterables(lefts, rights, *, left_key=None, right_key=None, before=None):
    r'''[[[
    :: (sorted-Iter a) -> (sorted-Iter b) -> ([uint], [uint])


    :: lefts/(sorted-Iter a) -> rights/(sorted-Iter b)
        -> (kw:left_key/may (a->KeyA))
        -> (kw:right_key/may (b->KeyB))
        -> (kw:before/may (KeyA->KeyB->Bool))
        -> (idc4LintoR, idc4RintoL)
            /([uint%(1+len(rights))]{len=len(lefts)}, [uint%(1+len(lefts))]{len=len(rights)})

    [all(all(((k<=j) is before(a,b)) for j,b in enumerate(rights)) for i,a in enumerate(lefts) let k:=idc4LintoR[i])]
        # 『<=』
    [all(all(((i<k) is before(a,b)) for i,a in enumerate(lefts)) for j,b in enumerate(rights) let k:=idc4RintoL[j])]
        # 『<』

    #]]]'''#'''
    left_key = ifNone(left_key, echo)
    right_key = ifNone(right_key, echo)
    before = ifNone(before, opss.le)

    _lefts = enumerate(map(left_key, lefts))
        # :: Iter (idxA, KeyA)
    _rights = enumerate(map(right_key, rights))
        # :: Iter (idxB, KeyB)

    #.def _before(_a, _b, /):
    #.    (jA, kA) = _a
    #.    (jB, kB) = _b
    #.    return before(kA, kB)
    #._before


    it = merge_two_sorted_iterables(_lefts, _rights, left_key=snd, right_key=snd, before=before, Left=dot_(mk_Left,fst), Right=dot_(mk_Right,fst))
        # :: Iter (Either idxA idxB)
        #it = merge_two_sorted_iterables(_lefts, _rights, left_key=snd, right_key=snd, before=before, Left=lambda jkA:mk_Left(fst(jkA)), Right=lambda jkB:mk_Right(fst(jkB)))

    idc4LintoR = []
    idc4RintoL = []
    idxA = -1
    idxB = -1
    for x in it:
        if x.is_left:
            idxA = x.left
            assert idxA == len(idc4LintoR)
            idc4LintoR.append(1+idxB)
                # :: [uint%(1+len(rights))]{len=len(lefts)}
            #assert 1+idxA == len(idc4LintoR)
        else:
            idxB = x.right
            assert idxB == len(idc4RintoL)
            idc4RintoL.append(1+idxA)
                # :: [uint%(1+len(lefts))]{len=len(rights)}
            #assert 1+idxB == len(idc4RintoL)
    idc4LintoR = tuple(idc4LintoR)
    idc4RintoL = tuple(idc4RintoL)
    return (idc4LintoR, idc4RintoL)

__all__
#[batch_find_insert_indices4two_sorted_iterables] = lazy_import4funcs_('seed.iters.batch_find_insert_indices4two_sorted_iterables', 'batch_find_insert_indices4two_sorted_iterables', __name__)
from seed.iters.batch_find_insert_indices4two_sorted_iterables import batch_find_insert_indices4two_sorted_iterables
from seed.iters.batch_find_insert_indices4two_sorted_iterables import *
