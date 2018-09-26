
r'''
winreg helper


std lib winreg:
    # constants
    winreg.HKEY_* :: HKEY_CONSTANT # HKEY_* constants
    winreg.KEY_* :: KEY_CONSTANT # Access Rights
    winreg.REG_* :: REG_CONSTANT # Value Types

    # variables
    may_computer_name :: MaybeComputerName
        ComputerName = String # r'\\computer_name'
        MaybeComputerName = None | ComputerName
    root_hkey_constant :: HKEY_CONSTANT
    hkey :: Handle
    key :: HandleEx
    fkey :: FHandleEx
    may_key_or_path :: MayKeyOrPath
    sub_key :: RelativeRegPath
    may_sub_key :: MaybeRelativeRegPath
    maykey_pair :: MayKeyPair
    access :: KEY_CONSTANT
    value_name :: String
    value :: Value
    type_case :: REG_CONSTANT
        (type_case, value:Object) :: TypedValue
    no_ext_fname :: NoExtFilePath

    # types
    WindowsError
    HKEY_CONSTANT
    KEY_CONSTANT
    REG_CONSTANT

    Handle = PyHKEY
        returned by ConnectRegistry only!!!

        bool(hkey) ::= has not been closed or detached

        Handle.Close(self)
        Handle.Detach(self) -> int

        with ConnectRegistry(...) as hkey:
            ...

    HandleEx = HKEY_CONSTANT | Handle
    FHandleEx =  Handle | winreg.HKEY_USERS | winreg.HKEY_LOCAL_MACHINE
        HandleEx subset for LoadKey/SaveKey
    MaybeRelativeRegPath = None | RelativeRegPath
            RelativeRegPath = String
            RelativeRegPath not empty
            RelativeRegPath not beginswith '.' or '/'
    RootRelativeRegPath <: RelativeRegPath
        RootRelativeRegPath beginswith HKEY_CONSTANT
    KeyOrPath = HandleEx | RootRelativeRegPath
    MayKeyOrPath = None | HandleEx | RootRelativeRegPath
    MayKeyPair = (Handle, RelativeRegPath) | (HKEY_CONSTANT, MaybeRelativeRegPath)
    Value = Object # String | Int | Bytes | ...
    TypedValue = (REG_CONSTANT, Value)
    ValuedType = (Value, REG_CONSTANT)
    NoExtFilePath
        ::= existing file path which has not file extension
            | nonexisting file path

        assert not os.path.isdir(no_ext_fname)
        name = os.path.basename(no_ext_fname)
        assert name and '.' not in name

    ######################################
    # Handle not HandleEx
    ConnectRegistry(may_computer_name, root_hkey_constant) -> Handle
        MaybeComputerName -> HKEY_CONSTANT -> Handle
    CloseKey(hkey) -> None
        Handle -> None # not HandleEx!!

    ######################################
    # HandleEx not Handle
    # MaybeRelativeRegPath not RelativeRegPath
    # (key, may_sub_key) :: MayKeyPair
    CreateKeyEx(key, may_sub_key, *, access=KEY_WRITE) -> HandleEx
        (key, may_sub_key) :: MayKeyPair
    OpenKeyEx(key, may_sub_key, *, access=KEY_READ) -> HandleEx
        (key, may_sub_key) :: MayKeyPair

    ######################################
    # HandleEx
    # MaybeRelativeRegPath
    # (key, may_sub_key) need not be MayKeyPair
    # ValuedType not TypedValue
    QueryInfoKey(key) -> (num_sub_keys, num_values, last_modified_time:int)
    EnumKey(key, index) -> sub_key_name
    EnumValue(key, index) -> (value_name, value, type_case)

    #QueryValue(key, may_sub_key) -> String
        query unnamed value
        QueryValue(key, None) <==> QueryValueEx(key, '')[0]
        use QueryValueEx instead
    QueryValueEx(key, value_name:String) -> ValuedType
        query named value

    ######################################
    # HandleEx
    # RelativeRegPath not MaybeRelativeRegPath
    # (type_case, value) :: TypedValue
    FlushKey(key)
        HandleEx -> None

    DeleteKey(key, sub_key)
        HandleEx -> RelativeRegPath -> None
    DeleteKeyEx(key, sub_key, *, access=KEY_WOW64_64KEY)
    DeleteValue(key, value_name)
    SetValue(key, sub_key, type_case, value)
    SetValueEx(key, value_name, reserved, type_case, value)

    ######################################
    # FHandleEx
    # RelativeRegPath
    SaveKey(fkey, no_ext_fname)
        FHandleEx -> NoExtFilePath -> None
    LoadKey(fkey, sub_key, no_ext_fname)
        FHandleEx -> RelativeRegPath -> NoExtFilePath -> None


###############################################################

winreg.KEY_ALL_ACCESS
    = KEY_READ | KEY_CREATE_LINK | KEY_WRITE

winreg.KEY_WRITE
    = KEY_SET_VALUE | KEY_CREATE_SUB_KEY

winreg.KEY_READ
    = KEY_QUERY_VALUE | KEY_ENUMERATE_SUB_KEYS | KEY_NOTIFY



###############################################################
# OP_DELETE     = None  means "delete" for reg_update_from
# OP_READ       = ...   means "assign" for reg_read_into
# OP_NOT_FOUND  = False means "not found" after reg_read_into
# key not presented means "ignore" for both
#

Table = (KeyTable, ValueTable)
KeyTable = {KeyName : Op Table}
ValueTable = {ValueName : Op TypedValue}
Op x = x | None | Ellipsis | False # the "..." constant

reg_update_from(KeyTable) -> None
reg_read_into(KeyTable) -> None



#####################################
std lib bugs:
    1. from python3_src\seed\windows\_test_winreg_helper\_t_open_create.py
        assert not reg_exists_path(path_tmp, None)
        with reg_open(path_tmp, None, access=winreg.KEY_WRITE) as key_tmp:
            ...
        #OpenKeyEx(key, sub_key, access=winreg.KEY_WRITE)
        #    raise FileNotFoundError, which should be WindowsError
'''


__all__ = r'''
    OP_DELETE       # = None
    OP_READ         # = ...
    OP_NOT_FOUND    # = False

    reg_read_into
        # INOUT KeyTable -> None
    reg_update_from
        # IN KeyTable -> None

    reg_read_into_key_table
        # MayKeyOrPath -> INOUT KeyTable -> None
    reg_update_from_key_table
        # MayKeyOrPath -> IN KeyTable -> None

    # KeyOrPath vs MayKeyOrPath
    reg_read_into_value_table
        # KeyOrPath -> INOUT ValueTable -> None
    reg_update_from_value_table
        # KeyOrPath -> IN ValueTable -> None
    reg_read_into_table
        # KeyOrPath -> INOUT Table -> None
    reg_update_from_table
        # KeyOrPath -> IN Table -> None


    reg_read_table
        # KeyOrPath -> (KeyTable, ValueTable)
    reg_read_key_table
        # KeyOrPath -> KeyTable
    reg_read_value_table
        # KeyOrPath -> ValueTable

    reg_exists_path
        # MayKeyOrPath -> MaybeRelativeRegPath -> bool
    reg_open
        # MayKeyOrPath -> MaybeRelativeRegPath -> (access=KEY_READ) -> HandleEx
    reg_create
        # MayKeyOrPath -> MaybeRelativeRegPath -> (access=KEY_WRITE) -> HandleEx

    reg_delete_key_tree__by_path
        # NonRoot_RootRelativeRegPath -> None
    reg_delete_key_tree
        # KeyOrPath -> child_key_name -> None

    reg_split_path
        # RelativeRegPath -> [key_name]
    reg_path_split_root
        # RelativeRegPath -> (root_name, MaybeRelativeRegPath)
    get_root_key
        # root_name -> HKEY_CONSTANT
    '''

from seed.tiny import str2__all__
__all__ = str2__all__(__all__)



import winreg
import os.path
from seed.for_libs.for_os_path.split_path_into_parts import \
    split_path_into_parts


OP_DELETE       = None
OP_READ         = ...
OP_NOT_FOUND    = False


def reg_read_into(key_table:'KeyTable'):
    _reg_read_into_key_table(None, key_table)
def reg_update_from(key_table:'KeyTable'):
    return _reg_update_from_key_table(None, key_table)
def reg_read_into_key_table(may_key_or_path, key_table):
    # MayKeyOrPath -> INOUT KeyTable -> None
    may_key = _reg_open_path_ex(may_key_or_path, access=winreg.KEY_READ)
    _reg_read_into_key_table(may_key, key_table)
def reg_update_from_key_table(may_key_or_path, key_table):
    # MayKeyOrPath -> IN KeyTable -> None
    may_key = _reg_create_path_ex(may_key_or_path, access=winreg.KEY_WRITE)
    return _reg_update_from_key_table(may_key, key_table)



# not may_key_or_path :: MayKeyOrPath
def reg_read_into_value_table(key_or_path, value_table):
    # KeyOrPath -> INOUT ValueTable -> None
    key = _reg_open_path_ex(key_or_path, access=winreg.KEY_READ)
    _reg_read_into_value_table(key, value_table)
def reg_update_from_value_table(key_or_path, value_table):
    # KeyOrPath -> IN ValueTable -> None
    key = _reg_create_path_ex(key_or_path, access=winreg.KEY_WRITE)
    return _reg_update_from_value_table(key, value_table)

def reg_read_into_table(key_or_path, table):
    # KeyOrPath -> INOUT Table -> None
    key = _reg_open_path_ex(key_or_path, access=winreg.KEY_READ)
    _reg_read_into_table(key, table)
def reg_update_from_table(key_or_path, table):
    # KeyOrPath -> IN Table -> None
    key = _reg_create_path_ex(key_or_path, access=winreg.KEY_WRITE)
    return _reg_update_from_table(key, table)


################################
def reg_read_table(key_or_path) -> "Table":
    # KeyOrPath -> Table
    # KeyOrPath -> (KeyTable, ValueTable)
    key = reg_open(key_or_path, None)
    table = key_table, value_table = _reg_read_table(key)
    return table
def reg_read_key_table(key_or_path) -> "KeyTable":
    # KeyOrPath -> KeyTable
    key = reg_open(key_or_path, None)
    (num_sub_keys, num_values, last_modified_time
        ) = winreg.QueryInfoKey(key)
    return _reg_read_key_table(key, num_sub_keys)
def reg_read_value_table(key_or_path) -> "ValueTable":
    # KeyOrPath -> ValueTable
    key = reg_open(key_or_path, None)
    (num_sub_keys, num_values, last_modified_time
        ) = winreg.QueryInfoKey(key)
    return _reg_read_value_table(key, num_values)

################################
def reg_delete_key_tree__by_path(path:'RootRelativeRegPath nonroot'):
    # NonRoot_RootRelativeRegPath -> None
    parent_path, child_key_name = dirname, basename = os.path.split(path)
    if not parent_path: raise TypeError
    if not child_key_name: raise TypeError
    reg_delete_key_tree(parent_path, child_key_name)
def reg_delete_key_tree(key_or_path, child_key_name):
    # KeyOrPath -> child_key_name -> None
    # neednot KEY_SET_VALUE

    try:
        key = reg_open(key_or_path, None)
    except WindowsError:
        # not exists??
        return
    _reg_delete_key_tree(key,child_key_name)


################################

#fail why??? see: _reg_open_or_create_path version1->version2
def reg_exists_path(may_key_or_path, may_sub_path):
    # MayKeyOrPath -> MaybeRelativeRegPath -> bool
    try:
        reg_open(may_key_or_path, may_sub_path)
    except WindowsError:
        return False
    return True

def reg_open(may_key_or_path, may_sub_path, *, access=None):
    # MayKeyOrPath -> MaybeRelativeRegPath -> (access=KEY_READ) -> HandleEx
    # (may_key_or_path, may_sub_path) != (None, None)
    if access is None:
        access = winreg.KEY_READ
    return _reg_open_or_create(may_key_or_path, may_sub_path
        , winreg.OpenKeyEx, access=access)
def reg_create(may_key_or_path, may_sub_path, access=None):
    # MayKeyOrPath -> MaybeRelativeRegPath -> (access=KEY_WRITE) -> HandleEx
    # (may_key_or_path, may_sub_path) != (None, None)
    if access is None:
        access = winreg.KEY_WRITE
    return _reg_open_or_create(may_key_or_path, may_sub_path
        , winreg.CreateKeyEx, access=access)


def _reg_open_or_create(may_key_or_path, may_sub_path
    , open_or_create, *, access):
    # MayKeyOrPath -> MaybeRelativeRegPath -> (OpenKeyEx|CreateKeyEx) -> HandleEx
    # (may_key_or_path, may_sub_path) != (None, None)
    may_key = _reg_open_or_create_path_ex(may_key_or_path, open_or_create, access=access)
    if may_key is None:
        if may_sub_path is None:
            raise TypeError('both None: may_key_or_path, may_sub_path')
        sub_path = may_sub_path
        child_key = _reg_open_or_create_path(sub_path, open_or_create, access=access)
    else:
        key = may_key
        if may_sub_path is None:
            child_key = key
        else:
            sub_path = may_sub_path
            child_key = open_or_create(key, sub_path)
    return child_key



def reg_split_path(path:'RelativeRegPath'):
    # RelativeRegPath -> [key_name]
    key_names = parts = split_path_into_parts(path)
    if not key_names: raise TypeError
    return key_names

def reg_path_split_root(path:'RelativeRegPath'):
    # RelativeRegPath -> (root_name, MaybeRelativeRegPath)

    # path = 'root////sub_path/sub_path'
    # path = 'root////'
    it = enumerate(path)
    for i, c in it:
        if c in r'\/':
            root = path[:i]
            for i, c in it:
                if c not in r'\/':
                    sub_path = path[i:]
            else:
                sub_path = ''
            break
    else:
        root = path
        sub_path = ''

    if sub_path:
        may_sub_path = sub_path
    else:
        may_sub_path = None

    if not root: raise TypeError
    return root, may_sub_path

def get_root_key(root_name):
    # root_name -> HKEY_CONSTANT
    key = getattr(winreg, root_name)
    return key






########################################

def _reg_open_path_ex(may_key_or_path, *, access):
    # may_key_or_path -> may_key
    return _reg_open_or_create_path_ex(may_key_or_path, winreg.OpenKeyEx, access=access)
def _reg_create_path_ex(may_key_or_path, *, access):
    # may_key_or_path -> may_key
    return _reg_open_or_create_path_ex(may_key_or_path, winreg.CreateKeyEx, access=access)
def _reg_open_or_create_path_ex(may_key_or_path, open_or_create, *, access):
    # MayKeyOrPath -> (OpenKeyEx|CreateKeyEx) -> Maybe HandleEx
    # may_key_or_path -> open_or_create -> may_key
    if isinstance(may_key_or_path, str):
        path = may_key_or_path
        key = _reg_open_or_create_path(path, open_or_create, access=access)
        may_key = key
    else:
        may_key = may_key_or_path
    return may_key






def _reg_open_or_create_path(path:'RootRelativeRegPath', open_or_create:callable, *, access):
    # RootRelativeRegPath -> (OpenKeyEx|CreateKeyEx) -> HandleEx
    # open_or_create = OpenKeyEx | CreateKeyEx
    # path -> open_or_create -> key
    #

    # version2
    [root_name, *key_names] = reg_split_path(path)
    key = root_key = get_root_key(root_name)
    for child_key_name in key_names:
        key = open_or_create(key, child_key_name, access=access)
    return key


    # version1:
    '''bugs:
    print(reg_read_table(path_tmp))         # print many things
    reg_delete_key_tree__by_path(path_tmp)
    assert not reg_exists_path(path_tmp, None) # fire! even it not exists
    '''
    root_name, may_sub_path = reg_path_split_root(path)

    root_key = get_root_key(root_name)
    if not may_sub_path:
        key = root_key
    else:
        sub_path = may_sub_path
        key = open_or_create(root_key, sub_path)
    return key


#########################################
def _reg_delete_key_tree(parent_key, key_name):
    # neednot KEY_SET_VALUE
    assert '/' not in key_name
    assert '\\' not in key_name
    try:
        key = winreg.OpenKeyEx(parent_key, key_name)
    except WindowsError:
        # not exists??
        return
    with key:
        (num_sub_keys, num_values, last_modified_time
            ) = winreg.QueryInfoKey(key)
        #neednot: _reg_delete_all_values(key, num_values)
        _reg_delete_all_sub_keys(key, num_sub_keys)
    winreg.DeleteKey(parent_key, key_name)

def _reg_delete_all_values(key, num_values):
    # why fail??
    #   need KEY_SET_VALUE
    value_names = list(_reg_iter_value_names(key, num_values, reverse=True))
    assert len(value_names) == len(set(value_names))
    for value_name in value_names:
        try:
            winreg.DeleteValue(key, value_name)
        except WindowsError:
            print(key)
            print(repr(value_name))
            raise
def _reg_delete_all_sub_keys(key, num_sub_keys):
    sub_key_names = list(_reg_iter_sub_key_names(key, num_sub_keys, reverse=True))
    for sub_key_name in sub_key_names:
        _reg_delete_key_tree(key, sub_key_name)

#########################################
def _reg_read_into_key_table(may_key, key_table):
    items = list(key_table.items())
    if may_key is None:
        for child_name, child_op_table in items:
            child_key = get_root_key(child_name)
            _reg_read_child_into_key_table(child_key, key_table, child_name)
    else:
        key = may_key
        for child_name, child_op_table in items:
            try:
                child_key = winreg.OpenKeyEx(key, child_name)
                    # access=winreg.KEY_READ | winreg.KEY_SET_VALUE
                    # KEY_SET_VALUE for delete values
                    # but we can directly delete the key
                    #   has values but no sub_keys
            except WindowsError:
                key_table[child_name] = OP_NOT_FOUND
            else:
                with child_key:
                    _reg_read_child_into_key_table(child_key, key_table, child_name)

def _reg_read_child_into_key_table(key, parent_key_table, key_name):
    op_table = parent_key_table[key_name]
    if op_table is OP_NOT_FOUND or op_table is OP_DELETE:
        pass
    elif op_table is OP_READ:
        parent_key_table[key_name] = _reg_read_table(key)
    else:
        table = op_table
        _reg_read_into_table(key, table)


def _reg_read_into_table(key, table):
    key_table, value_table = table
    _reg_read_into_value_table(key, value_table)
    _reg_read_into_key_table(key, key_table)
def _reg_read_into_value_table(key, value_table):
    items = list(value_table.items())
    for value_name, op_typed_value in items:
        if op_typed_value is OP_DELETE or op_typed_value is OP_NOT_FOUND:
            pass
        elif op_typed_value is OP_READ:
            valued_type = winreg.QueryValueEx(key, value_name)
            value, type_case = valued_type
            typed_value = type_case, value
            value_table[value_name] = typed_value
        else:
            typed_value = op_typed_value
            type_case, value = typed_value


def _reg_read_table(key) -> "Table":
    (num_sub_keys, num_values, last_modified_time
        ) = winreg.QueryInfoKey(key)
    key_table = _reg_read_key_table(key, num_sub_keys)
    value_table = _reg_read_value_table(key, num_values)
    op_table = key_table, value_table
    return op_table


def _reg_read_value_table(key, num_values) -> "ValueTable":
    value_table = {}
    for i in range(num_values):
        (value_name, value, type_case) = winreg.EnumValue(key, i)
        typed_value = type_case, value
        op_typed_value = typed_value
        value_table[value_name] = op_typed_value
    return value_table
def _reg_read_key_table(key, num_sub_keys) -> "KeyTable":
    key_table = {}
    for i in range(num_sub_keys):
        child_key_name = winreg.EnumKey(key, i)
        with winreg.OpenKeyEx(key, child_key_name) as child_key:
            key_table[child_key_name] = _reg_read_table(child_key)
    return key_table


def _make_range(n, *, reverse:bool):
    return range(n-1, -1, -1) if reverse else range(n)
def _reg_iter_sub_key_names(key, num_sub_keys, *, reverse:bool):
    for i in _make_range(num_sub_keys, reverse=reverse):
        child_key_name = winreg.EnumKey(key, i)
        yield child_key_name

def _reg_iter_value_names(key, num_values, *, reverse:bool):
    for i in _make_range(num_values, reverse=reverse):
        (value_name, value, type_case) = winreg.EnumValue(key, i)
        yield value_name


##########################################
def _reg_update_from_key_table(may_key, key_table):
    if may_key is None:
        for root, op_table in key_table.items():
            key = get_root_key(root)
            _reg_update_from_op_table(key, None, op_table)
    else:
        key = may_key
        for child_key_name, child_op_table in key_table.items():
            _reg_update_from_op_table(key, child_key_name, child_op_table)

def _reg_update_from_op_table(key, may_sub_key, child_op_table):
    # (key, may_sub_key) :: MayKeyPair
    if child_op_table is OP_READ or child_op_table is OP_NOT_FOUND:
        pass
    elif child_op_table is OP_DELETE:
        #winreg.DeleteKey(key, may_sub_key)#???
        if may_sub_key is None:
            raise WindowsError('winreg.DeleteKey(key, None)')
        sub_key = may_sub_key
        #winreg.DeleteKey(key, sub_key)
        _reg_delete_key_tree(key, sub_key)
    else:
        child_table = child_op_table
        key_table, value_table = child_table

        if may_sub_key is None:
            # "with root_hkey_constant as child_key" may cause error??
            child_key = key
            _reg_update_from_table(child_key, child_table)
        else:
            sub_key = may_sub_key
            try:
                #child_key = winreg.CreateKeyEx(key, may_sub_key)
                child_key = winreg.CreateKeyEx(key, sub_key)
            except WindowsError:
                print(key)
                print(repr(may_sub_key))
                raise
            else:
                with child_key:
                    _reg_update_from_table(child_key, child_table)

def _reg_update_from_table(key, table):
    key_table, value_table = table
    _reg_update_from_value_table(key, value_table)
    _reg_update_from_key_table(key, key_table)
def _reg_update_from_value_table(key, value_table):
    for value_name, op_typed_value in value_table.items():
        if op_typed_value is OP_READ or op_typed_value is OP_NOT_FOUND:
            pass
        elif op_typed_value is OP_DELETE:
            winreg.DeleteValue(key, value_name)
        else:
            typed_value = op_typed_value
            type_case, value = typed_value
            winreg.SetValueEx(key, value_name, 0, type_case, value)


if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    from pprint import pprint
    print('__all__ =')
    pprint(__all__)
    print_global_names(globals())

