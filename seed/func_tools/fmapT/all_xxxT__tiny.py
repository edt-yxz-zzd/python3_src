#all_xxxT__common_utils/common_utils:goto
#fmapT__tiny/fmapT:goto
#predT__tiny/predicatorT/predT:goto
#filterT__tiny/filterT:goto
#alterT__tiny/alterT:goto
#checkT__tiny/checkT:goto
r'''
seed.func_tools.fmapT.all_xxxT__tiny
py -m    seed.func_tools.fmapT.all_xxxT__tiny
py -m nn_ns.app.debug_cmd   seed.func_tools.fmapT.all_xxxT__tiny

see: _xxxT__tiny.py
    py -m nn_ns.app.debug_cmd   seed.func_tools.fmapT.all_xxxT__tiny > $my_tmp/out4py/debug_cmd.fmapT.all_xxxT__tiny.txt
    view /sdcard/0my_files/tmp//out4py/debug_cmd.fmapT.all_xxxT__tiny.txt
#'''



#e ../../python3_src/seed/func_tools/fmapT/all_xxxT__tiny.py
#
#e ../../python3_src/seed/func_tools/fmapT/all_xxxT__common_utils.py
from seed.func_tools.fmapT.all_xxxT__common_utils import (dot
,items_of
,keys_of
,values_of
,zip__same_len
,chain_from_iterable
,dot
,to_True
,to_False
,to_None
,to_Ellipsis
,to_NotImplemented
,xor5iter
,unpack_star_args_of
,pack_star_args_of
)

#e ../../python3_src/seed/func_tools/fmapT/fmapT__tiny.py
from seed.func_tools.fmapT.fmapT__tiny import (dot
,fmapT__dict
,fmapT__list
,fmapT__iter
,fmapT__tuple
,fmapT__iter_tuple
,fmapT__tpls
,fmapT__pairs
,fmap_rngs2hex_repr
)

#e ../../python3_src/seed/func_tools/fmapT/predT__tiny.py
from seed.func_tools.fmapT.predT__tiny import (dot
,not_
,is_True
,is_False
,is_None
,is_Ellipsis
,is_NotImplemented
,is_not_True
,is_not_False
,is_not_None
,is_not_Ellipsis
,is_not_NotImplemented
,fix_predicator
,allT__pattern_tuple
,anyT__pattern_tuple
,anyT__pattern_list
,allT__pattern_list
,anyT__pattern_dict
,allT__pattern_dict
,type_isT
,type_leT
,isinstanceT
,issubclassT
,isT
,is_notT
,eqT
,neT
,ltT
,gtT
,leT
,geT
,ge_ltT
,pred__True
,pred__False
,not_dotT
,predT__NOT
,predT__bool_op_
,predT__AND
,predT__NOT_AND
,predT__AND_NOT
,predT__NOT_AND_NOT
,predT__OR
,predT__NOT_OR
,predT__OR_NOT
,predT__NOT_OR_NOT
,predT__XOR
,predT__NOT_XOR
,predT__XOR_NOT
,predT__NOT_XOR_NOT
,is_frozenset
,is_set
,is_dict
,is_bool
,is_int
,is_float
,is_complex
,is_bytes
,is_str
,is_tuple
,is_list
,predT__tuple
,predT__list
,predT__frozenset
,predT__set
,predT__dict
,predT_on_property
,len_eqT
,len_ltT
,len_geT
,len_ge_ltT
,is_empty
)

#e ../../python3_src/seed/func_tools/fmapT/filterT__tiny.py
from seed.func_tools.fmapT.filterT__tiny import (dot
,mk__x2tmay__from__pred
,predicator_to_x2xs
,mk_x2xs__pred
,filterT_
,filterT
,filterT_fix
,filterT__tuple
,mk_filterT__5xs_2xs
,filterT__list
,filterT__set
,filterT__dict
)

#e ../../python3_src/seed/func_tools/fmapT/alterT__tiny.py
from seed.func_tools.fmapT.alterT__tiny import (dot
,mk_alterT__5xs_2xs
,alterT__dict
,alterT__set
,alterT__list
,alterT__tuple__chain
,tuple2iter_tuples__product
)

#e ../../python3_src/seed/func_tools/fmapT/checkT__tiny.py
from seed.func_tools.fmapT.checkT__tiny import (dot
,icheckT
,checkT__pattern_tuple
,checkT__pattern_list
,checkT__pattern_dict
,checkT__pattern_dictKV
,checkT__pattern_tmay
,checkT__5pred
,checkT__AND
,checkT__type_is
,checkT__type_le
,checkT__type_is__AND
,checkT__type_le__AND
,check__pass
,check__fail
,checkT__ifelse
,checkT__if
,checkT__if_not
,checkT__is
,checkT__eq
,checkT__ne
,checkT__lt
,checkT__gt
,checkT__le
,checkT__ge
,checkT__ge_lt
,check_bool
,check_int
,check_float
,check_complex
,check_bytes
,check_str
,check_tuple
,check_list
,check_frozenset
,check_set
,check_dict
,check__is_None
,checkT__tmay
,checkT__smay
,checkT__may
,checkT__imay
,checkT__tuple
,checkT__list
,checkT__frozenset
,checkT__set
,checkT__dict
,checkT__dictKV
)

