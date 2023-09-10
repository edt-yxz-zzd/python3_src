#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/symbol.py
see:
    view ../../python3_src/seed/abc/eq_by_id/PermanentSymbol.py
    view ../../python3_src/seed/helper/symbol.py
    view ../../python3_src/seed/helper/register.py


seed.helper.symbol
py -m nn_ns.app.debug_cmd   seed.helper.symbol -x
py -m nn_ns.app.doctest_cmd seed.helper.symbol:__doc__ -ff -v

from seed.helper.symbol import BaseSymbol, TmpSymbol, PermanentSymbol




#common
from seed.helper.symbol import mk_compact_extensional_path, unpack_compact_extensional_path
from seed.helper.symbol import BaseSymbol, TmpSymbol, PermanentSymbol

#author-side
from seed.helper.symbol import register_new_PermanentSymbol__compact, register_new_PermanentSymbol, fill_module_with_registered_permanent_symbols

#user-side
from seed.helper.symbol import PermanentSymbol, load_PermanentSymbol__compact, load_PermanentSymbol, get_extensional_path5PermanentSymbol, get_intensional_description5PermanentSymbol, mk_compact_extensional_path5PermanentSymbol



#]]]'''
__all__ = r'''
BaseSymbol
    TmpSymbol
    PermanentSymbol
        get_intensional_description5PermanentSymbol
        get_extensional_path5PermanentSymbol
            mk_compact_extensional_path5PermanentSymbol
            mk_compact_extensional_path
            unpack_compact_extensional_path

        register_new_PermanentSymbol__compact
            register_new_PermanentSymbol
            fill_module_with_registered_permanent_symbols

        load_PermanentSymbol__compact
            load_PermanentSymbol



'''.split()#'''
__all__

#common
from seed.abc.eq_by_id.PermanentSymbol import mk_compact_extensional_path, unpack_compact_extensional_path
from seed.abc.eq_by_id.PermanentSymbol import BaseSymbol, TmpSymbol, PermanentSymbol

#author-side
from seed.abc.eq_by_id.PermanentSymbol import register_new_PermanentSymbol__compact, register_new_PermanentSymbol, fill_module_with_registered_permanent_symbols

#user-side
from seed.abc.eq_by_id.PermanentSymbol import PermanentSymbol, load_PermanentSymbol__compact, load_PermanentSymbol, get_extensional_path5PermanentSymbol, get_intensional_description5PermanentSymbol, mk_compact_extensional_path5PermanentSymbol



#################################
#################################
#################################
#################################
#################################
#################################






#common
from seed.helper.symbol import mk_compact_extensional_path, unpack_compact_extensional_path
from seed.helper.symbol import BaseSymbol, TmpSymbol, PermanentSymbol

#author-side
from seed.helper.symbol import register_new_PermanentSymbol__compact, register_new_PermanentSymbol, fill_module_with_registered_permanent_symbols

#user-side
from seed.helper.symbol import PermanentSymbol, load_PermanentSymbol__compact, load_PermanentSymbol, get_extensional_path5PermanentSymbol, get_intensional_description5PermanentSymbol, mk_compact_extensional_path5PermanentSymbol





from seed.helper.symbol import *
