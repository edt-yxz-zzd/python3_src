
from seed.windows.winreg_helper import (
    reg_exists_path
    , reg_delete_key_tree__by_path, reg_delete_key_tree
    , reg_open, reg_create
    , reg_read_table, reg_read_key_table, reg_read_value_table
    , reg_read_into_table, reg_update_from_table
    )
from pprint import pprint
import winreg
from seed.for_libs.for_os_path import split_path_into_parts

path_dir = 'HKEY_CURRENT_USER/Software' .replace('/', '\\')
name_tmp = '_tmp'
path_tmp = f'{path_dir}/{name_tmp}' .replace('/', '\\')


#print(reg_read_table(path_tmp))
reg_delete_key_tree__by_path(path_tmp)
assert not reg_exists_path(path_tmp, None)

with reg_create(path_tmp, None):pass
assert reg_exists_path(path_tmp, None)

reg_delete_key_tree__by_path(path_tmp)
assert not reg_exists_path(path_tmp, None)

try:
    reg_open(path_tmp, None, access=winreg.KEY_WRITE)
except FileNotFoundError:
    pass
else:
    raise logic-error

table_tmp = ({'a':({'c':({},{})},{}), 'b':({},{})}, {'1':(winreg.REG_SZ, 'afs')})

with reg_create(path_tmp, None, access=winreg.KEY_READ):pass
with reg_open(path_tmp, None, access=winreg.KEY_WRITE) as key_tmp:
    reg_update_from_table(key_tmp, table_tmp)
    table_output = ({'a':..., 'b':...}, {'1':...})
    try:
        reg_read_into_table(key_tmp, table_output)
    except WindowsError:
        pass
    else:
        raise logic-error
with reg_create(path_tmp, None, access=winreg.KEY_READ) as key_tmp:
    reg_read_into_table(key_tmp, table_output)
    assert table_tmp == table_output
    assert table_tmp == reg_read_table(key_tmp)
    assert table_tmp == (reg_read_key_table(key_tmp), reg_read_value_table(key_tmp))
assert table_tmp == reg_read_table(path_tmp)
assert table_tmp == (reg_read_key_table(path_tmp), reg_read_value_table(path_tmp))

assert reg_exists_path(path_tmp, None)
reg_delete_key_tree(path_dir, name_tmp)
assert not reg_exists_path(path_tmp, None)
reg_delete_key_tree(path_dir, name_tmp)







