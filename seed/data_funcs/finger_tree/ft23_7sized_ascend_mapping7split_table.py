#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_ascend_mapping7split_table.py

seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######

[[
split_table: [ftMap==(ftSet,ftSeq)]

view ../../python3_src/seed/mapping_tools/determine_num_slots4hash_map.py_dict_impl.txt
]]


'#'; __doc__ = r'#'
>>> AscendMap()
AscendMap()
>>> AscendMap({3:33, 2:44})
mkAscendMap[2: 44, 3: 33]
>>> AscendMap([(3,33), (2,44)])
mkAscendMap[2: 44, 3: 33]
>>> AscendMap([2,3], [44,33])
mkAscendMap[2: 44, 3: 33]
>>> AscendMap([3,2], [33,44])
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError
>>> mkAscendMap[2: 44, 3: 33]
mkAscendMap[2: 44, 3: 33]
>>> AscendMap.bmk[2: 44, 3: 33]
mkAscendMap[2: 44, 3: 33]
>>> AscendMap.bmk[3: 33, 2: 44]
mkAscendMap[2: 44, 3: 33]
>>> AscendMap(AscendSet([2, 3]), [44,33], using_split_table=True)
AscendMap(AscendSet([2, 3]), Seq([44, 33]), using_split_table = True)
>>> AscendMap(AscendSet([2, 3]), [44], using_split_table=True)
AscendMap(AscendSet([2, 3]), Seq([44]), using_split_table = True)
>>> AscendMap(AscendSet([2, 3]), [44,33,99], using_split_table=True)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.TableLenError: (2, 3)
>>> AscendMap(AscendSet([2, 3]), [44])
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.TableLenError: (2, 1)
>>> AscendMap(AscendSet([2, 3]), [44,33,99])
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.TableLenError: (2, 3)


>>> AscendMap([2,3], [44,33]) == AscendMap.bmk[3: 33, 2: 44]
True
>>> hash(AscendMap([2,3], [44,33])) == hash(AscendMap.bmk[3: 33, 2: 44])
True
>>> AscendMap([2,3], [44,33])._args4hash == AscendMap.bmk[3: 33, 2: 44]._args4hash
True

#>>> AscendMap([2,3], [44,33])._args4hash
#>>> AscendMap.bmk[3: 33, 2: 44]._args4hash
#>>> AscendSet([2, 3]) == AscendSet([2, 3])
#>>> Seq([44, 33]) == Seq([44, 33])



>>> len(mkAscendMap[2: 44, 3: 33])
2
>>> [*iter(mkAscendMap[2: 44, 3: 33])]
[2, 3]
>>> [*reversed(mkAscendMap[2: 44, 3: 33])]
[3, 2]

>>> len(AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True))
2
>>> [*iter(AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True))]
[2, 3]
>>> [*reversed(AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True))]
[3, 2]




>>> mkAscendMap[2: 44, 3: 33][1]
Traceback (most recent call last):
    ...
KeyError: 1
>>> mkAscendMap[2: 44, 3: 33][2]
44
>>> mkAscendMap[2: 44, 3: 33][3]
33
>>> 1 in mkAscendMap[2: 44, 3: 33]
False
>>> 2 in mkAscendMap[2: 44, 3: 33]
True
>>> 3 in mkAscendMap[2: 44, 3: 33]
True


>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True)[2]
44
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True)[3]
33
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True)[6]
Traceback (most recent call last):
    ...
KeyError: 6
>>> 6 in AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True)
False
>>> 2 in AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True)
True
>>> 3 in AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True)
True






>>> mkAscendMap[2: 44, 3: 33].isetitem_(1, 99)
mkAscendMap[1: 99, 2: 44, 3: 33]
>>> mkAscendMap[2: 44, 3: 33].isetitem_(2, 99)
mkAscendMap[2: 99, 3: 33]
>>> mkAscendMap[2: 44, 3: 33].isetitem_(2.5, 99)
mkAscendMap[2: 44, 2.5: 99, 3: 33]
>>> mkAscendMap[2: 44, 3: 33].isetitem_(3, 99)
mkAscendMap[2: 44, 3: 99]
>>> mkAscendMap[2: 44, 3: 33].isetitem_(4, 99)
mkAscendMap[2: 44, 3: 33, 4: 99]



>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).isetitem_(4, 99)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.DisorderKeyError: 4
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).isetitem_(6, 99)
AscendMap(AscendSet([2, 3, 6]), Seq([44, 33, 99]), using_split_table = True)
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).isetitem_(3, 99)
AscendMap(AscendSet([2, 3, 6]), Seq([44, 99]), using_split_table = True)
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).isetitem_(2, 99)
AscendMap(AscendSet([2, 3, 6]), Seq([99, 33]), using_split_table = True)




idelitem_
vpopitem_
wdiscard
>>> mkAscendMap[2: 44, 3: 33].idelitem_(1)
Traceback (most recent call last):
    ...
KeyError: 1
>>> mkAscendMap[2: 44, 3: 33].idelitem_(2)
mkAscendMap[3: 33]
>>> mkAscendMap[2: 44, 3: 33].idelitem_(3)
mkAscendMap[2: 44]
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).idelitem_(2) # not right_end
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.DisorderKeyError: 2
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).idelitem_(3)
AscendMap(AscendSet([2, 3, 6]), Seq([44]), using_split_table = True)
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).idelitem_(6)
Traceback (most recent call last):
    ...
KeyError: 6



>>> mkAscendMap[2: 44, 3: 33].vpopitem_()
((3, 33), mkAscendMap[2: 44])
>>> mkAscendMap[2: 44, 3: 33].vpopitem_(1)
Traceback (most recent call last):
    ...
KeyError: 1
>>> mkAscendMap[2: 44, 3: 33].vpopitem_(2)
((2, 44), mkAscendMap[3: 33])
>>> mkAscendMap[2: 44, 3: 33].vpopitem_(3)
((3, 33), mkAscendMap[2: 44])
>>> mkAscendMap[2: 44, 3: 33].vpopitem_(1, 999)
((1, 999), mkAscendMap[2: 44, 3: 33])
>>> mkAscendMap[2: 44, 3: 33].vpopitem_(2, 999)
((2, 44), mkAscendMap[3: 33])
>>> mkAscendMap[2: 44, 3: 33].vpopitem_(3, 999)
((3, 33), mkAscendMap[2: 44])


>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vpopitem_()
((3, 33), AscendMap(AscendSet([2, 3, 6]), Seq([44]), using_split_table = True))
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vpopitem_(2)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.DisorderKeyError: 2
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vpopitem_(3)
((3, 33), AscendMap(AscendSet([2, 3, 6]), Seq([44]), using_split_table = True))
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vpopitem_(6)
Traceback (most recent call last):
    ...
KeyError: 6
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vpopitem_(2, 999)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.DisorderKeyError: 2
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vpopitem_(2.5, 999)
((2.5, 999), AscendMap(AscendSet([2, 3, 6]), Seq([44, 33]), using_split_table = True))
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vpopitem_(3, 999)
((3, 33), AscendMap(AscendSet([2, 3, 6]), Seq([44]), using_split_table = True))
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vpopitem_(6, 999)
((6, 999), AscendMap(AscendSet([2, 3, 6]), Seq([44, 33]), using_split_table = True))





>>> mkAscendMap[2: 44, 3: 33].wdiscard(1)
((), 0, mkAscendMap[2: 44, 3: 33])
>>> mkAscendMap[2: 44, 3: 33].wdiscard(2)
(((2, 44),), 0, mkAscendMap[3: 33])
>>> mkAscendMap[2: 44, 3: 33].wdiscard(2.5)
((), 1, mkAscendMap[2: 44, 3: 33])
>>> mkAscendMap[2: 44, 3: 33].wdiscard(3)
(((3, 33),), 1, mkAscendMap[2: 44])
>>> mkAscendMap[2: 44, 3: 33].wdiscard(4)
((), 2, mkAscendMap[2: 44, 3: 33])


>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).wdiscard(1)
((), 0, AscendMap(AscendSet([2, 3, 6]), Seq([44, 33]), using_split_table = True))
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).wdiscard(2)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.DisorderKeyError: 2
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).wdiscard(2.5)
((), 1, AscendMap(AscendSet([2, 3, 6]), Seq([44, 33]), using_split_table = True))
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).wdiscard(3)
(((3, 33),), 1, AscendMap(AscendSet([2, 3, 6]), Seq([44]), using_split_table = True))
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).wdiscard(6)
((), 2, AscendMap(AscendSet([2, 3, 6]), Seq([44, 33]), using_split_table = True))





vpop_
vpopitemR
vpopitem_at_key_
vpopitem_at_key7default_
vdiscard
idiscard

>>> mkAscendMap[2: 44, 3: 33].vpop_()
(33, mkAscendMap[2: 44])
>>> mkAscendMap[2: 44, 3: 33].vpop_(2)
(44, mkAscendMap[3: 33])
>>> mkAscendMap[2: 44, 3: 33].vpop_(1, 999)
(999, mkAscendMap[2: 44, 3: 33])


>>> mkAscendMap[2: 44, 3: 33].vpopitemR()
((3, 33), mkAscendMap[2: 44])
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vpopitemR()
((3, 33), AscendMap(AscendSet([2, 3, 6]), Seq([44]), using_split_table = True))

>>> mkAscendMap[2: 44, 3: 33].vpopitem_at_key_(2)
((2, 44), mkAscendMap[3: 33])
>>> mkAscendMap[2: 44, 3: 33].vpopitem_at_key_(1)
Traceback (most recent call last):
    ...
KeyError: 1
>>> mkAscendMap[2: 44, 3: 33].vpopitem_at_key_(1, 999)
((1, 999), mkAscendMap[2: 44, 3: 33])

>>> mkAscendMap[2: 44, 3: 33].vpopitem_at_key7default_(2)
((2, 44), mkAscendMap[3: 33])
>>> mkAscendMap[2: 44, 3: 33].vpopitem_at_key7default_(1)
((1, None), mkAscendMap[2: 44, 3: 33])
>>> mkAscendMap[2: 44, 3: 33].vpopitem_at_key7default_(1, 999)
((1, 999), mkAscendMap[2: 44, 3: 33])


>>> mkAscendMap[2: 44, 3: 33].vdiscard(2)
(((2, 44),), mkAscendMap[3: 33])
>>> mkAscendMap[2: 44, 3: 33].idiscard(2)
mkAscendMap[3: 33]
>>> mkAscendMap[1: 44, 3: 33].vdiscard(2)
((), mkAscendMap[1: 44, 3: 33])
>>> mkAscendMap[1: 44, 3: 33].idiscard(2)
mkAscendMap[1: 44, 3: 33]

>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vdiscard(3)
(((3, 33),), AscendMap(AscendSet([2, 3, 6]), Seq([44]), using_split_table = True))
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).idiscard(3)
AscendMap(AscendSet([2, 3, 6]), Seq([44]), using_split_table = True)
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vdiscard(2)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.DisorderKeyError: 2
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).idiscard(2)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table.DisorderKeyError: 2
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).vdiscard(6)
((), AscendMap(AscendSet([2, 3, 6]), Seq([44, 33]), using_split_table = True))
>>> AscendMap(AscendSet([2, 3, 6]), [44,33], using_split_table=True).idiscard(6)
AscendMap(AscendSet([2, 3, 6]), Seq([44, 33]), using_split_table = True)









py_adhoc_call   seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table   @f
]]]'''#'''
__all__ = r'''
AscendMap
    mkAscendMap

TableLenError
DisorderKeyError
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from collections.abc import Mapping as IMapping
from seed.types.attr.class_property import class_property
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.data_funcs.finger_tree.ft23_7sized_ascend_set import AscendSet, NotAscendError
    from seed.data_funcs.finger_tree.ft23_7sized_seq import Seq
    from seed.helper.repr_input import repr_helper
    from seed.tiny_.check import check_type_is# check_int_ge
    from seed.tiny_.bmk_pairs import bmk_pairs, show_ordered_pairs_as_bmk_pairs
    #def show_ordered_pairs_as_bmk_pairs(pairs, /, *, colon=': ', comma=', ', name='bmk_pairs', to_omit_None=False, to_shrink=False):



    from itertools import islice
    from seed.types.CachedProperty import CachedProperty# mk_cached_propertyT_
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property



#.#################################
___end_mark_of_excluded_global_names__0___ = ...

__all__









class TableLenError(Exception):pass
class DisorderKeyError(Exception):pass


class AscendMap(IMapping):
    r'''[[[
    [using_split_table is False]:
        [len(key_asc_set) == len(value_seq)]
    [using_split_table is True]:
        [len(key_asc_set) >= len(value_seq)]
        mutable_ops{alter size} can only perform at tail/right_end{value_seq}...

    ]]]'''#'''
    ___no_slots_ok___ = True
    def __new__(cls, mapping_or_pairs_or_key_asc_set=None, value_seq=None, /, *, using_split_table=False):
        check_type_is(bool, using_split_table)
        if using_split_table and None is value_seq:raise TypeError
        #if using_split_table and None is mapping_or_pairs_or_key_asc_set:raise TypeError
        if using_split_table and not isinstance(mapping_or_pairs_or_key_asc_set, AscendSet):raise TypeError
        while 1:
            if not None is value_seq:
                key_asc_set = mapping_or_pairs_or_key_asc_set
                if None is key_asc_set:raise TypeError
                break
            #########
            mapping_or_pairs = mapping_or_pairs_or_key_asc_set
            if None is mapping_or_pairs:
                if cls is __class__:
                    try:
                        return _empty_map
                    except NameError:
                        pass
                pairs = ()
            elif isinstance(mapping_or_pairs, IMapping):
                d = mapping_or_pairs
                if isinstance(d, cls):
                    sf = d
                    return sf
                elif not cls is __class__ and isinstance(d, __class__):
                    mapping_or_pairs_or_key_asc_set = d.key_asc_set
                    value_seq = d.value_seq
                    continue
                pairs = d.items()
            else:
                pairs = mapping_or_pairs
            pairs
            pairs = sorted(pairs)
            key_asc_set = [k for k, v in pairs]
            value_seq = [v for k, v in pairs]
            mapping_or_pairs_or_key_asc_set = key_asc_set
            continue
        #end-while 1:
        key_asc_set
        value_seq
        assert not None is value_seq
        assert not None is key_asc_set

        if not isinstance(key_asc_set, AscendSet):
            key_asc_set = AscendSet(key_asc_set, unordered_vs_ascend_vs_descend=1)
        if not isinstance(value_seq, Seq):
            value_seq = Seq(value_seq)
        if not key_asc_set:
            using_split_table = False

        if using_split_table:
            if not len(key_asc_set) >= len(value_seq):raise TableLenError(len(key_asc_set), len(value_seq))
        else:
            if not len(key_asc_set) == len(value_seq):raise TableLenError(len(key_asc_set), len(value_seq))



        if not key_asc_set and cls is __class__:
            try:
                return _empty_map
            except NameError:
                pass

        sf = super(__class__, cls).__new__(cls)
        sf._b = using_split_table
        sf._ks = key_asc_set
        sf._vs = value_seq
        return sf
    @class_property
    def bmk(cls, /):
        return _MkAscendMap(cls)
    @classmethod
    def from_pairs(cls, pairs, /):
        return cls(iter(pairs))
    @classmethod
    def from_key_and_value_tables(cls, using_split_table, key_asc_set, value_seq, /):
        if None is value_seq:raise TypeError
        if None is key_asc_set:raise TypeError
        return cls(key_asc_set, value_seq, using_split_table=using_split_table)

    @property
    def using_split_table(sf, /):
        return sf._b
    @property
    def key_asc_set(sf, /):
        return sf._ks
    @property
    def value_seq(sf, /):
        return sf._vs
    def __repr__(sf, /):
        if not sf:
            assert not sf.using_split_table
            return repr_helper(sf)
        if sf.using_split_table:
            return repr_helper(sf, sf.key_asc_set, sf.value_seq, using_split_table=True)
        #bug:return show_ordered_pairs_as_bmk_pairs(zip(sf.key_asc_set, sf.value_seq), name=type(sf).__name__)
        #.return repr_helper(sf, sf.key_asc_set, sf.value_seq)
        name = 'mkAscendMap' if type(sf) is AscendMap else (type(sf).__name__+'.bmk')
        return show_ordered_pairs_as_bmk_pairs(zip(sf.key_asc_set, sf.value_seq), name=name)

    @property
    def _args4hash(sf, /):
        return (type(sf), len(sf), sf.using_split_table, sf.key_asc_set, sf.value_seq)
    @CachedProperty
    def _hash(sf, /):
        return hash(sf._args4hash)
    def __hash__(sf, /):
        return sf._hash
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        if not type(sf) is type(ot):
            return NotImplemented
        if '_hash' in vars(sf) and '_hash' in vars(ot):
            if not hash(sf) == hash(ot):
                return False
        return sf._args4hash == ot._args4hash
        #.if not len(sf) == len(ot): return False

    def __len__(sf, /):
        return len(sf.value_seq) # <= len(sf.key_asc_set)
    @CachedProperty
    def _b_full_kvs(sf, /):
        #.return len(sf.key_asc_set) == len(sf.value_seq)
        return not sf.using_split_table or len(sf.key_asc_set) == len(sf.value_seq)
    def __iter__(sf, /):
        if sf._b_full_kvs:
            return iter(sf.key_asc_set)
        return islice(iter(sf.key_asc_set), 0, len(sf.value_seq))
    def __reversed__(sf, /):
        if sf._b_full_kvs:
            return reversed(sf.key_asc_set)
        #.return islice(reversed(sf.key_asc_set), len(sf.key_asc_set)-len(sf.value_seq), len(sf.key_asc_set))
        return reversed(sf.key_asc_set[:len(sf.value_seq)])
    def __contains__(sf, k, /):
        return not -1 == (j:=sf.key_asc_set.find_eq_(k, 0, len(sf.value_seq)))
    def __getitem__(sf, k, /):
        if not -1 == (j:=sf.key_asc_set.find_eq_(k, 0, len(sf.value_seq))):
            return sf.value_seq[j]
        raise KeyError(k)
    def idelitem_(sf, k, /):
        '-> AscendMap | ^KeyError | ^DisorderKeyError'
        (v, ot) = sf.vpop_(k)
        return ot
    def isetitem_(sf, k, v, /):
        '-> AscendMap | ^KeyError | ^DisorderKeyError'
        cls = type(sf)
        (setL, tmay_kM, setR) = sf.key_asc_set[:len(sf.value_seq)].partition_at_key_(k)
        if tmay_kM:
            j = len(setL)
            #if not -1 == (j:=sf.key_asc_set.find_eq_(k, 0, len(sf.value_seq))):
            #replace old value
            return cls.from_key_and_value_tables(sf.using_split_table, sf.key_asc_set, sf.value_seq.isetitem_(j, v))

        if sf.using_split_table:
            #append new value
            if setR:raise DisorderKeyError(k)
            if sf._b_full_kvs:raise DisorderKeyError(k)
            if not k in [sf.key_asc_set[len(sf.value_seq)]]:raise DisorderKeyError(k)
            return cls.from_key_and_value_tables(sf.using_split_table, sf.key_asc_set, sf.value_seq.ipushR(v))

        #insert new item
        #(setL, setR) = sf.key_asc_set.split_at_key_(k)
        new_keys = setL.ipushR(k) + setR
        return cls.from_key_and_value_tables(sf.using_split_table, new_keys, sf.value_seq.iput_at_(len(setL), v))
    def vpop_(sf, /, *kv):
        '-> (v, AscendMap) | ^KeyError | ^DisorderKeyError'
        ((k,v), ot) = sf.vpopitem_(*kv)
        return (v, ot)
    def vpopitem_(sf, /, *kv):
        '-> ((k,v), AscendMap) | ^KeyError | ^DisorderKeyError'
        if not len(kv) <=2:raise TypeError
        match kv:
            case ():
                return sf.vpopitemR()
            case (k,):
                return sf.vpopitem_at_key_(k)
            case (k, v):
                return sf.vpopitem_at_key7default_(k, v)
            case _:
                raise 000
        raise 000
    def vpopitemR(sf, /):
        '-> ((k,v), AscendMap) | ^KeyError'
        if not sf: raise KeyError('pop empty')
            #dict: KeyError: 'popitem(): dictionary is empty'
        (vR, seqL) = sf.value_seq.vpopR()
        vs = seqL
        if sf.using_split_table:
            kR = sf.key_asc_set[len(vs)]
            ks = sf.key_asc_set
        else:
            (kR, setL) = sf.key_asc_set.vpopR()
            ks = setL
        kvR = (kR, vR)
        cls = type(sf)
        ot = cls.from_key_and_value_tables(sf.using_split_table, ks, vs)
        return (kvR, ot)

    def vpopitem_at_key_(sf, k, /, *tmay_default):
        '-> ((k,v), AscendMap) | ^KeyError | ^DisorderKeyError'
        if not len(tmay_default) <=1:raise TypeError
        if not sf: raise KeyError(k)
        cls = type(sf)
        if sf.using_split_table:
            _k = sf.key_asc_set[len(sf)-1]
            if not k in [_k]:
                #.if not tmay_default or k in sf: raise KeyError(k)
                if k in sf: raise DisorderKeyError(k)
                if not tmay_default: raise KeyError(k)
                [default] = tmay_default
                kv = (k, default)
                ot = sf
                return (kv, ot)
            return sf.vpopitemR()
        (tmay_hit, j, ks) = sf.key_asc_set.wdiscard(k)
        match tmay_hit:
            case ():
                if not tmay_default: raise KeyError(k)
                [default] = tmay_default
                kv = (k, default)
                ot = sf
                return (kv, ot)
            case (_k,):
                pass
            case _:
                raise 000
        (_v, vs) = sf.value_seq.vpop_at_(j)
        _kv = (_k, _v)
        ot = cls.from_key_and_value_tables(sf.using_split_table, ks, vs)
        return (_kv, ot)
    def vpopitem_at_key7default_(sf, k, default=None, /):
        '-> ((k,v), AscendMap) | ^DisorderKeyError'
        return sf.vpopitem_at_key_(k, default)
    def wdiscard(sf, k, /):
        '-> (tmay_kv, idx, map) | ^DisorderKeyError iff [using_split_table][k in sf][k =!= sf.key_asc_set[len(sf)-1]]'
        cls = type(sf)
        if sf.using_split_table:
            ks_ = sf.key_asc_set[:len(sf)]
            (setL, tmay_k, setR) = ks_.partition_at_key_(k)
            if tmay_k and setR:raise DisorderKeyError(k)
            elif tmay_k and not setR:
                (kv, ot) = sf.vpopitemR()
                tmay_kv = (kv,)
                ot
            else:
                [] = tmay_k
                tmay_kv = ()
                ot = sf
            j = len(setL)
            return (tmay_kv, j, ot)

        (tmay_hit, j, ks) = sf.key_asc_set.wdiscard(k)
        match tmay_hit:
            case ():
                tmay_kv = ()
                ot = sf
                return (tmay_kv, j, ot)
            case (_k,):
                pass
            case _:
                raise 000
        (_v, vs) = sf.value_seq.vpop_at_(j)
        _kv = (_k, _v)
        tmay_kv = (_kv,)
        ot = cls.from_key_and_value_tables(sf.using_split_table, ks, vs)
        return (tmay_kv, j, ot)

    def vdiscard(sf, k, /):
        '-> (tmay_kv, map) | ^DisorderKeyError iff [using_split_table][k in sf][k =!= sf.key_asc_set[len(sf)-1]]'
        (tmay_kv, j, ot) = sf.wdiscard(k)
        return (tmay_kv, ot)
    def idiscard(sf, k, /):
        '-> map | ^DisorderKeyError iff [using_split_table][k in sf][k =!= sf.key_asc_set[len(sf)-1]]'
        (tmay_kv, ot) = sf.vdiscard(k)
        return ot

_empty_map = AscendMap()
class _MkAscendMap:
    def __init__(sf, T, /):
        sf._T = T
    def __getitem__(sf, k, /):
        return sf._T.from_pairs(bmk_pairs[k])
    def __call__(sf, /, *args, **kwds):
        return sf._T(*args, **kwds)
mkAscendMap = _MkAscendMap(AscendMap)


__all__
from seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table import AscendMap, mkAscendMap, TableLenError, DisorderKeyError
from seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table import *
