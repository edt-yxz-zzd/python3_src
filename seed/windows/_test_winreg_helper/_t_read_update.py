
from seed.windows.winreg_helper import reg_read_into, reg_update_from
from pprint import pprint
import winreg
from copy import deepcopy

key_table_update = {
    'HKEY_CURRENT_USER' : ({
        'Software' : ({
            '_tmp' :
                (   {'a' : ({} , {})
                    , 'b' : ({} , {})
                    }
                ,   {'1' : (winreg.REG_DWORD, 34) # not '34'
                    ,'2' : (winreg.REG_SZ, 'ab\0ba') # will become 'ab'
                    }
                )
        }, {})
    }, {})
}

reg_update_from(key_table_update)

key_table_read = {
    'HKEY_CURRENT_USER' : ({
        'Software' : ({
            '_tmp' :
                (   {'a' : ...
                    , 'b' : ...
                    }
                ,   {'1' : ...
                    ,'2' : ...
                    }
                )
        }, {})
    }, {})
}

if True:
    key_table_read2 = deepcopy(key_table_read)
    reg_read_into(key_table_read2)
    pprint(key_table_read2)
    assert key_table_read2 == \
        {'HKEY_CURRENT_USER': ({'Software': ({'_tmp':
        ({'a': ({}, {}), 'b': ({}, {})}, {'1': (4, 34), '2': (1, 'ab')})
        }, {})}, {})}


key_table_delete = {
    'HKEY_CURRENT_USER' : ({
        'Software' : ({
            '_tmp' : None
        }, {})
    }, {})
}


reg_update_from(key_table_delete)

if True:
    key_table_read2 = deepcopy(key_table_read)
    reg_read_into(key_table_read2)
    pprint(key_table_read2)
    assert key_table_read2 == \
        {'HKEY_CURRENT_USER': ({'Software': ({'_tmp': False}, {})}, {})}


