

'''
def set_discards(mapping, *keyss):
    # difference_update(*others)
    # set -= other | ...
'''

def dict_discards(mapping, *keyss):
    for keys in keyss:
        for key in keys:
            mapping.pop(key, 0)



