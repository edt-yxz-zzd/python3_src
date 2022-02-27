r'''
seed.mapping_tools.mapping_reversable_update__tmay

e ../../python3_src/seed/mapping_tools/mapping_reversable_update__tmay.py

from seed.mapping_tools.mapping_reversable_update__tmay import mapping_reversable_update__tmay

#'''

def mapping_reversable_update__tmay(mapping, key, tmay_new_value, /):
    '-> tmay_old_value'
    if key in mapping:
        tmay_old_value = (mapping[key],)
    else:
        tmay_old_value = ()

    if tmay_new_value:
        #set_item
        [v] = tmay_new_value
        mapping[key] = v
    else:
        #del_item
        if tmay_old_value:
            del mapping[key]
    return tmay_old_value


