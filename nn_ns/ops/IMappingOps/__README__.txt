

mappings
value = obj[key]
1. value = f(obj)(key)
    read only, computation
2. value = getattr(g(key), f(obj)) # f(obj)->str
    read/write/delete/discard
    but has no __len__
    the underlying mapping was complete out of control
    trouble if multi-threading
3. value = unjust(fullmapping(obj)[key])
4. value = partialmapping(obj)[key]


(Immutable key, Eq key) ==>>:
SizedMappingOps
    size_of
    #computation-based/object-attribute-based mapping has no __len__
TestableMappingOps
    contains_key
    #write-only-mapping has no __contains__
ReadableMapping(TestableMapping)
    get_item
UpdatableMappingOps
    maybe_update_item
    #set only if exists otherwise no-op
GrowableMappingOps
    maybe_add_item
    #add only if not exists otherwise no-op
    # 'setdefault'
ShrinkableMappingOps
    maybe_delete_key
    #delete only if exists otherwise no-op
    # 'discard'
IterableMappingOps
    iter_keys
    iter_items
    # countable
    # finite ==>> sized




