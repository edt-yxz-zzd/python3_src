

__all__ = '''
    mapping_on_key

    get_fdefault
    set_fdefault
    getitem_fdefault
    setitem_fdefault
    add_new_item
    '''.split()

def mapping_on_key(mapping, key, payload, handler):
    r'''
    handler :: mapping->key->payload->may_old_value->result
    #'''
    Nothing = object()
    r = mapping.get(key, Nothing)
    may_old_value = () if r is Nothing else (r,)
    return handler(mapping, key, payload, may_old_value)

def get_fdefault(mapping, key, fdefault):
    # fdefault :: () -> d
    # get_fdefault :: Map k v -> k -> (()->d) -> (v|d)
    Nothing = []
    r = mapping.get(key, Nothing)
    return fdefault() if r is Nothing else r
def set_fdefault(mapping, key, fdefault):
    # fdefault :: () -> d
    # set_fdefault :: Map k v -> k -> (()->v) -> None
    def miss():
        r = mapping[key] = fdefault()
        return r
    #bug:return mapping.get(key, miss)
    return get_fdefault(mapping, key, miss)


def getitem_fdefault(mapping, key, fdefault):
    # fdefault :: () -> d
    # getitem_fdefault :: Map k v -> k -> (()->d) -> (v|d)
    # v.s. get_fdefault:
    #   using try...except
    #   so, __missing__ may be called
    try:
        return mapping[key]
    except KeyError:
        return fdefault()
def setitem_fdefault(mapping, key, fdefault):
    # fdefault :: () -> d
    # setitem_fdefault :: Map k v -> k -> (()->v) -> None
    # v.s. set_fdefault:
    #   using try...except
    #   so, __missing__ may be called
    def miss():
        r = mapping[key] = fdefault()
        return r
    return getitem_fdefault(mapping, key, miss)

def add_new_item(mapping, key, new_value, *op_oldnew=None):
    if op_oldnew is None:
        def op_oldnew(old_value, new_value):
            raise KeyError('key existed!')
    def handler(mapping, key, payload, may_old_value):
        new_value = payload
        if may_old_value:
            [old_value] = may_old_value
            new_value = op_oldnew(old_value, new_value)
        else:
            #miss, add_new_item
            pass
        mapping[key] = new_value
    payload = new_value
    mapping_on_key(mapping, key, payload, handler)









