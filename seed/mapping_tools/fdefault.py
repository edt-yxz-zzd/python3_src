

__all__ = '''
    get_fdefault
    set_fdefault
    getitem_fdefault
    setitem_fdefault
    '''.split()

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

