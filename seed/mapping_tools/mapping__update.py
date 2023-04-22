#__all__:goto
r'''[[[
e ../../python3_src/seed/mapping_tools/mapping__update.py

 seed.mapping_tools.mapping__update

py -m nn_ns.app.debug_cmd seed.mapping_tools.mapping__update
py -m seed.mapping_tools.mapping__update
from seed.mapping_tools.mapping__update import mapping__update



[[[
dict__update
===
update(...) method of builtins.dict instance
D.update([E, ]**F) -> None.
Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:
      for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:
      for k, v in E: D[k] = v
    In either case, this is followed by:
      for k in F:  D[k] = F[k]
]]]

#]]]'''
__all__ = r'''
    mapping__update
'''.split()#'''
__all__

def mapping__update(sf, may_mapping_or_items=None, /, **kw):
    if may_mapping_or_items is None:
        pass
    else:
        mapping_or_items = mapping_or_items
        if hasattr('keys', mapping_or_items):
            mapping = mapping_or_items
            items = mapping.items()
        else:
            items = mapping_or_items

        for k,v in items:
            sf[k] = v
    ###
    for k,v in kw.items():
        sf[k] = v


from seed.mapping_tools.mapping__update import mapping__update

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

