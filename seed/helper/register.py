#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/register.py
see:
    view ../../python3_src/seed/abc/eq_by_id/PermanentSymbol.py
    view ../../python3_src/seed/helper/symbol.py
    view ../../python3_src/seed/helper/register.py


seed.helper.register
py -m nn_ns.app.debug_cmd   seed.helper.register -x
py -m nn_ns.app.doctest_cmd seed.helper.register:__doc__ -ff -v
py_adhoc_call   seed.helper.register   @f

from seed.helper.register import RegisterError, RegisterKeyError, RegisterPermissionError
from seed.helper.register import IRegister, Register__default_mixins
from seed.helper.register import Case4Existed
from seed.helper.register import RegisterRegister, plugin_mkr_register_register


#]]]'''

__all__ = r'''
RegisterError
    RegisterKeyError
        RegisterKeyError__nonexisted
        RegisterKeyError__existed
    RegisterPermissionError
        RegisterPermissionError__unregister
        RegisterPermissionError__register
        RegisterPermissionError__overwrite
        RegisterPermissionError__merge
Case4Existed
IRegister
    Register__default_mixins
    RegisterRegister
        plugin_mkr_register_register

'''.split()#'''
__all__
from enum import Enum
from seed.tiny import check_type_is, check_type_le
from seed.tiny import null_tuple
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.helper.symbol import BaseSymbol, TmpSymbol, PermanentSymbol

class RegisterError(Exception):pass

class RegisterKeyError(RegisterError, KeyError):pass
class RegisterPermissionError(RegisterError, PermissionError):pass

class RegisterKeyError__nonexisted(RegisterKeyError):pass
class RegisterKeyError__existed(RegisterKeyError):pass

class RegisterPermissionError__unregister(RegisterPermissionError):pass
class RegisterPermissionError__register(RegisterPermissionError):pass
class RegisterPermissionError__overwrite(RegisterPermissionError):pass
class RegisterPermissionError__merge(RegisterPermissionError):pass


Case4Existed = Enum('Case4Existed', r'''
    error
    skip
    replace
    merge
'''#'''
)

class IRegister(ABC):
    'why _mk_state_?:eg:register_("a.b.c") -> Symbol("a.b.c")'
    __slots__ = ()
    @abstractmethod
    def _get_storage_(sf, /):
        '-> Mapping<k,st>'
    @abstractmethod
    def _mk_state_(sf, key, /, *args4st, **kwds4st):
        '-> st'
    @abstractmethod
    def _merge_state_(sf, key, old_st, lazy_new_st_, /):
        '-> st'
    @abstractmethod
    def _get_target5state_(sf, st, /):
        '-> v'
    @abstractmethod
    def does_allow_register(sf, /):
        '-> bool # burn'
    @abstractmethod
    def does_allow_unregister(sf, /):
        '-> bool # burn or growing only'
    @abstractmethod
    def does_allow_overwrite(sf, /):
        '-> bool # burn'
    @abstractmethod
    def does_allow_merge(sf, /):
        '-> bool # burn'

    @abstractmethod
    def _check_key_(sf, key, /):
        '-> None | ^Exception'
    @abstractmethod
    def _check_state_(sf, st, /):
        '-> None | ^Exception'
    @abstractmethod
    def _check_value_(sf, value, /):
        '-> None | ^Exception'






    def register_(sf, case4existed, key, /, *args4st, **kwds4st):
        'case4existed/Case4Existed -> k -> *args4st -> **kwds4st -> None | ^RegisterPermissionError__register  | ^RegisterPermissionError__overwrite| ^RegisterKeyError__existed | ^TypeError-case4existed | ^from sf._check_key_(k) | ^from sf._check_state_(...) | ^from sf._check_value_(...)'
        if not does_allow_register():
            raise RegisterPermissionError__register
                # 1
        check_type_is(Case4Existed, case4existed)
        #check_int_ge_le(-1, +1, case4existed)
                # ^TypeError
                # 2

        lazy_new_st_ = lambda:sf._mk_state_(key, *args4st, **kwds4st)

        if existed := sf.is_registered(key):
                # ^from-sf._check_key_(key)
                # 3
            if case4existed is Case4Existed.error:
                raise RegisterKeyError__existed(key)
                # 4
            elif case4existed is Case4Existed.skip:
                # skip
                return None
            elif case4existed is Case4Existed.replace:
                #overwrite
                if not sf.does_allow_overwrite():
                    raise RegisterPermissionError__overwrite
                        # 5
                #value = lazy_value_()
                #sf._check_value_(value)
                    # ^...
                        # 6
                new_st = lazy_new_st_()
            elif case4existed is Case4Existed.merge:
                if not sf.does_allow_merge():
                    raise RegisterPermissionError__merge
                k2st = sf._get_storage_()
                old_st = k2st[key]
                #tmay_old_st = (old_st,)
                new_st = sf._merge_state_(key, old_st, lazy_new_st_)
            else:
                raise 000
        else:
            #not exist
            #tmay_old_st = ()
            new_st = lazy_new_st_()
        #tmay_old_st
        new_st
        sf._check_state_(new_st)
            # ^...
                # 6
        value = sf._get_target5state_(new_st)
        sf._check_value_(value)
            # ^...
                # 7
        sf._store_(existed, key, new_st)
        return None

    def is_registered(sf, key, /):
        '-> bool | ^from sf._check_key_(key)'
        sf._check_key_(key)
        return sf._is_registered_(key)
    def lookup(sf, key, /):
        '-> value | ^RegisterKeyError__nonexisted | ^from sf._check_key_(key)'
        if not sf.is_registered(key):
            raise RegisterKeyError__nonexisted(key)
        return sf._lookup_(key)
    def lookup__tmay(sf, key, /):
        '-> tmay value | ^from sf._check_key_(key)'
        if not sf.is_registered(key):
            return null_tuple
        return (sf._lookup_(key),)
    def unregister(sf, key, /, *, nonexist_ok):
        '-> None | ^RegisterKeyError__nonexisted | ^from sf._check_key_(key)'
        if not does_allow_unregister():
            raise RegisterPermissionError__unregister
        if not sf.is_registered(key):
            if nonexist_ok:
                return None
            raise RegisterKeyError__nonexisted(key)
        sf._unregister_(key)
        return

    def _store_(sf, existed, key, new_st, /):
        'checked => existed/bool -> k -> st -> None #new if not existed else overwrite'
        k2st = sf._get_storage_()
        k2st[key] = new_st
    def _is_registered_(sf, key, /):
        'checked => k -> bool'
        k2st = sf._get_storage_()
        return key in k2st
    def _lookup_(sf, key, /):
        'existed => k -> v'
        k2st = sf._get_storage_()
        return sf._get_target5state_(k2st[key])
    def _unregister_(sf, key, /):
        'existed => k -> None'
        k2st = sf._get_storage_()
        del k2st[key]
        return
    def __detitem__(sf, k, /):
        sf.unregister(k)
        return
    def __getitem__(sf, k, /):
        return sf.lookup(k)
    if 0:
        def __setitem__(sf, k, st, /):
            return sf.register_(k, st)

class Register__default_mixins(IRegister):
    __slots__ = ()
    @override
    def _get_storage_(sf, /):
        '-> Mapping<k,st>'
        return sf.__dict__
    @override
    #def _mk_state_(sf, key, /, *args4st, **kwds4st):
    def _mk_state_(sf, key, st, /):
        '-> st'
        return st
    @override
    def _merge_state_(sf, key, old_st, lazy_new_st_, /):
        '-> st'
        raise NotImplementedError
        raise logic-err
    @override
    def _get_target5state_(sf, st, /):
        '-> v'
        value = st
        return value
    @override
    def does_allow_register(sf, /):
        '-> bool # burn'
        return True
    @override
    def does_allow_unregister(sf, /):
        '-> bool # burn or growing only'
        return False
    @override
    def does_allow_overwrite(sf, /):
        '-> bool # burn'
        return False
    @override
    def does_allow_merge(sf, /):
        '-> bool # burn'
        return False

    @override
    def _check_key_(sf, key, /):
        '-> None | ^Exception'
        pass
    @override
    def _check_state_(sf, st, /):
        '-> None | ^Exception'
        pass
    @override
    def _check_value_(sf, value, /):
        '-> None | ^Exception'
        pass

    def __repr__(sf, /):
        s = repr_helper(sf, sf._get_target5state_())
        return f'<{s}>'


class RegisterRegister(Register__default_mixins):
    '[key :: BaseSymbol][value :: IRegister]'
    ___no_slots_ok___ = True
    @override
    def _check_key_(sf, key, /):
        '-> None | ^TypeError'
        '-> None | ^Exception'
        check_type_le(BaseSymbol, key)
    @override
    def _check_value_(sf, value, /):
        '-> None | ^TypeError'
        '-> None | ^Exception'
        check_type_le(IRegister, value)
    def lookup_lookup(sf, symbol, k, /):
        register4symbol = sf.lookup(symbol)
        v = register4symbol.lookup(k)
        return v
    def lookup_lookup__tmay(sf, symbol, k, /):
        tmay_register4symbol = sf.lookup__tmay(symbol)
        if not tmay_register4symbol:
            return null_tuple
        [register4symbol] = tmay_register4symbol
        tmay_v = register4symbol.lookup__tmay(k)
        return tmay_v

plugin_mkr_register_register = RegisterRegister()
    # :: {symbol:{typ_info:plugin_mkr_/(*typ_params->plugin)}}



from seed.helper.register import RegisterError, RegisterKeyError, RegisterPermissionError
from seed.helper.register import IRegister, Register__default_mixins
from seed.helper.register import Case4Existed
from seed.helper.register import RegisterRegister, plugin_mkr_register_register
from seed.helper.register import *
