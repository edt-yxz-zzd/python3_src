

'''
def set_discards(mapping, *keyss):
    # difference_update(*others)
    # set -= other | ...
'''
__all__ = 'dict_discards'.split()
def dict_discards(mapping, *keyss):
    for keys in keyss:
        for key in keys:
            mapping.pop(key, 0)


from seed.mapping_tools.dict_discards import dict_discards
