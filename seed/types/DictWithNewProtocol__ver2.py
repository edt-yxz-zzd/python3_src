#__all__:goto
r'''[[[
e ../../python3_src/seed/types/DictWithNewProtocol__ver2.py
view ../../python3_src/seed/mapping_tools/determine_num_slots4hash_map.py

seed.types.DictWithNewProtocol__ver2
py -m nn_ns.app.debug_cmd seed.types.DictWithNewProtocol__ver2
py -m nn_ns.app.adhoc_argparser__main__call8module seed.types.DictWithNewProtocol__ver2

from seed.types.DictWithNewProtocol__ver2 import MappingProtocol, FacetMappingProtocol



#]]]'''
__all__ = r'''
    MappingProtocol
    FacetMappingProtocol
'''.split()#'''
__all__


from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
#from seed.mapping_tools.determine_num_slots4hash_map import IDetermineNumSlots4HashMap, determine_num_slots4hash_map

class MappingProtocol(ABC):
    r'''
move from FacetMappingProtocol:
    it seems FacetMappingProtocol === multiple non-facet-MappingProtocol which enable cross dict item

datatype in concept:
    raw_item
        ~=~ (.query_key, .target_value)

    storage_item
        ~=~ [.raw_item, .key_hash]
        # mutable-variant-of-storage_item_view

    storage_item_view
        ~=~ (.raw_item, .key_hash)
        # immutable-variant-of-storage_item

    target_value
        ~=~ (.hvalue, .other_data)

use_case:
    * use_case: query_key in d
    * use_case: storage_item_views := d.iter_storage_item_views_via_key(query_key)
        #query via key
    * use_case: storage_item_views := d.iter_storage_item_views_via_item(storage_item_view)
        #query via item


    #distinguish overwrite/setnew???
    * use_case: d.set_raw_item(raw_item)
    * use_case: d.set_storage_item(storage_item)
        # to enable cross dict item




    * use_case: d[0:query_key] := hvalue
    * use_case: d[1:raw_item] := hvalue
    * use_case: d[2:storage_item_view] := hvalue
        #!!!overwrite not setnew!!!
        #using raw_item/storage_item_view as key



    * use_case: hvalue := d[0:query_key]
    * use_case: hvalue := d[1:raw_item]
    * use_case: hvalue := d[2:storage_item_view]

    * use_case: hvalue := d[0:query_key, imay_xdefault_rank, xdefault]
    * use_case: hvalue := d[1:raw_item, imay_xdefault_rank, xdefault]
    * use_case: hvalue := d[2:storage_item_view, imay_xdefault_rank, xdefault]
        # imay_xdefault_rank, xdefault
        #       view ../../python3_src/seed/mapping_tools/fdefault.py





d :: Mapping_using_MappingProtocol
    mapping_protocol := d.get_mapping_protocol()
    * use_case: query_key in d
    * use_case: storage_item_views := d.iter_storage_item_views_via_key(query_key)
        #query via key
        .get_hash5query_key
        d.iter_storage_item_views_via_hash
            .eq__query_key__storage_item_view
    * use_case: storage_item_views := d.iter_storage_item_views_via_item(storage_item_view)
        #query via item
        .get_hash5storage_item_view
        d.iter_storage_item_views_via_hash
            .eq__storage_item_view
    * use_case: storage_item_views := d.iter_storage_item_views_via_hash(key_hash)
        #query via key_hash
        .view_storage_item


    #distinguish overwrite/setnew???
    * use_case: d.set_raw_item(raw_item)
        .raw_item2storage_item
        d.set_storage_item
    * use_case: d.set_storage_item(storage_item)
        # to enable cross dict item
        .view_storage_item
        .get_hash5storage_item_view
            .eq__storage_item_view




    * use_case: d[0:query_key] := hvalue
        d._iter_storage_items_via_key #d.iter_storage_item_views_via_key
            .emplace_update_target_value4storage_item_via_hvalue
    * use_case: d[1:raw_item] := hvalue
        .raw_item2storage_item
        .view_storage_item
        d[2:storage_item_view] := hvalue
    * use_case: d[2:storage_item_view] := hvalue
        #!!!overwrite not setnew!!!
        #using raw_item/storage_item_view as key
        d._iter_storage_items_via_item #d.iter_storage_item_views_via_item
            .emplace_update_target_value4storage_item_via_hvalue



    * use_case: hvalue := d[0:query_key]
    * use_case: hvalue := d[1:raw_item]
    * use_case: hvalue := d[2:storage_item_view]
        d.iter_storage_item_views_via_item
            .raw_item5storage_item_view
            .get_target_value5raw_item
            .get_hvalue5target_value

    * use_case: hvalue := d[0:query_key, imay_xdefault_rank, xdefault]
    * use_case: hvalue := d[1:raw_item, imay_xdefault_rank, xdefault]
    * use_case: hvalue := d[2:storage_item_view, imay_xdefault_rank, xdefault]

    '''#'''
    __slots__ = ()

    @abstractmethod
    def raw_item2storage_item(sf, raw_item, /):
        'raw_item -> storage_item #hard_work #eval&cached auxiliary_args, emplace_updateable'
    @abstractmethod
    def view_storage_item(sf, storage_item, /):
        'storage_item -> storage_item_view #O(1)'
    @abstractmethod
    def raw_item5storage_item_view(sf, storage_item_view, /):
        'storage_item_view -> raw_item  #O(1) #get original raw_item #[raw_item is raw_item5storage_item_view(view_storage_item(raw_item2storage_item(raw_item)))]'

    @abstractmethod
    def get_hash5storage_item_view(sf, storage_item_view, /):
        'storage_item_view -> key_hash'
    @abstractmethod
    def get_hash5query_key(sf, query_key, /):
        'query_key -> key_hash'

    @abstractmethod
    def eq__query_key__storage_item_view(sf, query_key, storage_item_view, /):
        'query_key -> storage_item_view -> bool'
    @abstractmethod
    def eq__storage_item_view(sf, lhs_storage_item_view, rhs_storage_item_view, /):
        'lhs_storage_item_view -> rhs_storage_item_view -> bool'

    @abstractmethod
    def get_target_value5raw_item(sf, raw_item, /):
        'raw_item -> target_value'
    @abstractmethod
    def get_hvalue5target_value(sf, target_value, /):
        'target_value -> hvalue'
    @abstractmethod
    def emplace_update_target_value4storage_item_via_hvalue(sf, hvalue, storage_item, /):
        'hvalue -> storage_item -> None'


#end-class MappingProtocol(ABC):
class FacetMappingProtocol(ABC):
    r'''
[hselect_facet_query_key =[def]= (partial_facet_query_key|as_facet_query_key|facet_query_key)]

use_case:
    * use_case: d.set_raw_item(raw_item)
        # normal user API:multimapping.__setitem__

    * use_case: d.set_storage_item(storage_item)
        # to enable cross dict item

    * use_case: storage_item_views := d.iter_storage_item_views(partial_facet_query_key)
        # select operator for multimapping
        # logic-AND:inter-facets

    * use_case: d[hselect_facet_query_key:facet_name] := facet_value
    * use_case: d[hselect_facet_query_key::facet_namesL] := facet_valuesL
        #!!!overwrite not setnew!!!
        # select_items_then_overwrite_facets operator
        #select_facet_names diff target_facet_names

    * use_case: d[as_facet_query_key] := tmay_facet_value
    * use_case: d[partial_facet_query_key] := tmay_partial_facet_value
        #why tmay? to match __getitem__

    * use_case: facet_values := d[hselect_facet_query_key:facet_name]
    * use_case: facet_valuesLs := d[hselect_facet_query_key::facet_namesL]

    * use_case: facet_values := d[as_facet_query_key]
    * use_case: partial_facet_values := d[partial_facet_query_key]
        # normal user API: multimapping.__getitem__

    * use_case: as_facet_query_key in d
    * use_case: partial_facet_query_key in d
        # normal user API: multimapping.__contains__
        # logic-AND:inter-facets

    * use_case: d.iter_facet_overlap_ex(storage_item_view) -> Iter (facet_name, storage_item_view, Iter facet_name)


#conceptually:
datatype in concept:
    as_facet_query_key
        ~=~ (.facet_name, .facet_query_key, .facet_hash)

    partial_facet_query_key
        ~=~ {facet_name:(.facet_query_key, .facet_hash)}
        ~=~ [(.facet_name, .facet_query_key, .facet_hash)]
        ~=~ [as_facet_query_key]
        <= whole_facet_query_key

    whole_facet_query_key
        ~=~ {facet_name:facet_query_key}

    partial_facet_value
        ~=~ {facet_name:facet_value}
        <= whole_facet_value
    whole_facet_value
        ~=~ {facet_name:facet_value}
    target_value
        ~=~ (.whole_facet_value, .other_data)


    raw_item
        ~=~ (.whole_query_key, .target_value)

    whole_facet_hash
        ~=~ {facet_name:facet_hash}

    storage_item
        ~=~ [.raw_item, .whole_facet_hash]
        # mutable-variant-of-storage_item_view

    storage_item_view
        ~=~ (.raw_item, .whole_facet_hash)
        # immutable-variant-of-storage_item


storage_item
storage_item_view
    raw_item
    storage_auxiliary_args
        #storage_auxiliary_args not changed when storage_item.raw_item changed
partial_facet_query_key
    as_facet_query_key
    facet_name
    facet_query_key
facet_names_or_num_facets :: tuple<facet_name> | pint
    [len(facet_names) > 0]
    [len(facet_names) == len({*facet_names})]
    [num_facets > 0]
        as-if:
            facet_names := [0..num_facets-1]

target_value
    facet_value

d :: Mapping_using_MappingProtocol
    mapping_protocol := d.get_mapping_protocol()

    * use_case: d.set_raw_item(raw_item)
        raw_item2storage_item
        d.set_storage_item

    * use_case: d.set_storage_item(storage_item)
        # to enable cross dict item
        view_storage_item
        get_facet_names_or_num_facets
            get_facet_hash5storage_item_view
            facet_eq__storage_item_view
            #overwrite all overlapped old storage_item
            #   to control overwrite, see: d.iter_facet_overlap_ex
            #or: multimapping per facet

    * use_case: storage_item_views := d.iter_storage_item_views(partial_facet_query_key)
        iter_as_facet_query_keys5partial_facet_query_key
            decompose_as_facet_query_key_ex
                decompose_as_facet_query_key
                get_facet_hash5query_key
            view_storage_item
            eq__facet_query_key__storage_item_view

    * use_case: d[hselect_facet_query_key:facet_name] := facet_value
    * use_case: d[hselect_facet_query_key::facet_namesL] := facet_valuesL
        #select_facet_names diff target_facet_names
        unify:hselect_facet_query_key -> (target_facet_name -> partial_facet_query_key)
            unify_hselect_facet_query_key
                distinguish_hselect_facet_query_key
                mk_as_facet_query_key
                mk_partial_facet_query_key
            handle only 'partial_facet_query_key' case

    * use_case: d[as_facet_query_key] := tmay_facet_value
        #why tmay? to match __getitem__
        #select_facet_names == target_facet_names
        decompose_as_facet_query_key
        d._iter_storage_items #==>> iter_storage_item_views
            emplace_update_target_value4storage_item_via_facet_value


    * use_case: d[partial_facet_query_key] := tmay_partial_facet_value
        #why tmay? to match __getitem__
        #select_facet_names diff target_facet_names
        d._iter_storage_items #==>> iter_storage_item_views
            iter_as_facet_values5partial_facet_value
                emplace_update_target_value4storage_item_via_facet_value

    * use_case: facet_values := d[hselect_facet_query_key:facet_name]
    * use_case: facet_valuesLs := d[hselect_facet_query_key::facet_namesL]

    * use_case: partial_facet_values := d[partial_facet_query_key]
    * use_case: facet_values := d[as_facet_query_key]
        decompose_as_facet_query_key
        d.iter_storage_item_views
            raw_item5storage_item_view
            get_target_value5raw_item
            get_facet_value5target_value

    * use_case: partial_facet_query_key in d
        #__contains__
        #logic-AND
        # <<== __getitem__

    * use_case: d.iter_facet_overlap_ex(storage_item_view) -> Iter (facet_name, storage_item_view, Iter facet_name)
        # <= set_raw_item

    '''#'''
    __slots__ = ()
    #body-class FacetMappingProtocol(ABC):

    @abstractmethod
    def get_facet_names_or_num_facets(sf, /):
        '-> (facet_names/[facet_name] | num_facets/pint)'
    @abstractmethod
    def raw_item2storage_item(sf, raw_item, /):
        'raw_item -> storage_item #hard_work #eval&cached auxiliary_args, emplace_updateable'
    @abstractmethod
    def view_storage_item(sf, storage_item, /):
        'storage_item -> storage_item_view #O(1)'
    @abstractmethod
    def raw_item5storage_item_view(sf, storage_item_view, /):
        'storage_item_view -> raw_item  #O(1) #get original raw_item #[raw_item is raw_item5storage_item_view(view_storage_item(raw_item2storage_item(raw_item)))]'
    @abstractmethod
    def get_facet_hash5storage_item_view(sf, facet_name, storage_item_view, /):
        'facet_name -> storage_item_view -> facet_hash'

    @abstractmethod
    def iter_as_facet_query_keys5partial_facet_query_key(sf, partial_facet_query_key, /):
        'partial_facet_query_key -> Iter as_facet_query_key #logic-AND'

    if 1:
        @abstractmethod
        def decompose_as_facet_query_key(sf, as_facet_query_key, /):
            'as_facet_query_key -> (facet_name, facet_query_key)'
        @abstractmethod
        def get_facet_hash5query_key(sf, facet_name, facet_query_key, /):
            'facet_name -> facet_query_key -> facet_hash'
        def decompose_as_facet_query_key_ex(sf, as_facet_query_key, /):
            'as_facet_query_key -> (facet_name, facet_query_key, facet_hash)'
            (facet_name, facet_query_key) = sf.decompose_as_facet_query_key(as_facet_query_key)
            facet_hash = sf.get_facet_hash5query_key(facet_name, facet_query_key)
            return (facet_name, facet_query_key, facet_hash)

        @abstractmethod
        def mk_as_facet_query_key(sf, facet_name, facet_query_key, may_facet_hash, /):
            'facet_name -> facet_query_key -> may facet_hash -> as_facet_query_key'
        @abstractmethod
        def mk_partial_facet_query_key(sf, as_facet_query_keys, /):
            'Iter as_facet_query_key -> partial_facet_query_key'
        @abstractmethod
        def distinguish_hselect_facet_query_key(sf, hselect_facet_query_key, /):
            '(partial_facet_query_key|as_facet_query_key|facet_query_key) -> [0..=2]'

    @abstractmethod
    def eq__facet_query_key__storage_item_view(sf, facet_name, facet_query_key, storage_item_view, /):
        'facet_name -> facet_query_key -> storage_item_view -> bool'
    @abstractmethod
    def facet_eq__storage_item_view(sf, facet_name, lhs_storage_item_view, rhs_storage_item_view, /):
        'facet_name -> lhs_storage_item_view -> rhs_storage_item_view -> bool'
    @abstractmethod
    def get_target_value5raw_item(sf, raw_item, /):
        'raw_item -> target_value'
    @abstractmethod
    def get_facet_value5target_value(sf, facet_name, target_value, /):
        'facet_name -> target_value -> facet_value'
    @abstractmethod
    def emplace_update_target_value4storage_item_via_facet_value(sf, facet_name, facet_value, storage_item, /):
        'facet_name -> facet_value -> storage_item -> None'

def unify_hselect_facet_query_key(sf, hselect_facet_query_key, /):
    '(partial_facet_query_key|as_facet_query_key|facet_query_key) -> (target_facet_names -> partial_facet_query_key)'
    i = distinguish_hselect_facet_query_key(sf, hselect_facet_query_key)
    if i == 2:
        def target_facet_name2partial_facet_query_key(target_facet_name, /):
            facet_query_key = hselect_facet_query_key
            as_facet_query_key = sf.mk_as_facet_query_key(target_facet_name, facet_query_key, None)
            partial_facet_query_key = sf.mk_partial_facet_query_key([as_facet_query_key])
            return partial_facet_query_key
    ######
    elif i == 1:
        def target_facet_name2partial_facet_query_key(target_facet_name, /):
            as_facet_query_key = hselect_facet_query_key
            partial_facet_query_key = sf.mk_partial_facet_query_key([as_facet_query_key])
            return partial_facet_query_key
    ######
    elif i == 0:
        def target_facet_name2partial_facet_query_key(target_facet_name, /):
            partial_facet_query_key = hselect_facet_query_key
            return partial_facet_query_key
    else:
        raise logic-err
    return target_facet_name2partial_facet_query_key
#end-def unify_hselect_facet_query_key(sf, hselect_facet_query_key, target_facet_name, /):
#end-class FacetMappingProtocol(ABC):


from seed.types.DictWithNewProtocol__ver2 import MappingProtocol, FacetMappingProtocol

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

