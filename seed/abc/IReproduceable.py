#__all__:goto
r'''[[[
e ../../python3_src/seed/abc/IReproduceable.py

seed.abc.IReproduceable
py -m nn_ns.app.debug_cmd   seed.abc.IReproduceable -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.abc.IReproduceable:__doc__ -ht # -ff -df
#######

[[
move_to:
view ../../python3_src/seed/types/Reproduceable.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.abc.IReproduceable   @f
]]]'''#'''
__all__ = r'''
IStatedTransformOps
    IStatedTransformOps7fork
        IStatedTransformOps7fork7default_mixin
    IStatedTransformOps7flow
        IStatedTransformOps7flow7default_mixin
    IReproduceable
        IReproduceable7transform
            IReproduceable7fmap
            IReproduceable7transform_via_ops




IReproduceable
    is_reproduceable_
        check_reproduceable_

    xnext4reproduceable_
        xnext4reproduceable7check_
        check_result5xnext4reproduceable_
            ResultTypes4xnext
                NextEx
                StopEx

    Iter4IReproduceable
        iter_pairs4reproduceable_
            iter_fsts4reproduceable_
            iter_snds4reproduceable_
        list_pairs4reproduceable_
            list_fsts4reproduceable_
            list_snds4reproduceable_


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...
from seed.types.Reproduceable import (
IStatedTransformOps
,   IStatedTransformOps7fork
,       IStatedTransformOps7fork7default_mixin
,   IStatedTransformOps7flow
,       IStatedTransformOps7flow7default_mixin
,   IReproduceable
,       IReproduceable7transform
,           IReproduceable7fmap
,           IReproduceable7transform_via_ops
#
,IReproduceable
,   is_reproduceable_
,       check_reproduceable_
#
,   xnext4reproduceable_
,       xnext4reproduceable7check_
,       check_result5xnext4reproduceable_
,           ResultTypes4xnext
,               NextEx
,               StopEx
#
,   Iter4IReproduceable
,       iter_pairs4reproduceable_
,           iter_fsts4reproduceable_
,           iter_snds4reproduceable_
,       list_pairs4reproduceable_
,           list_fsts4reproduceable_
,           list_snds4reproduceable_
)





















__all__
from seed.abc.IReproduceable import IStatedTransformOps, IReproduceable, is_reproduceable_, check_reproduceable_
    # typing

from seed.abc.IReproduceable import xnext4reproduceable_, xnext4reproduceable7check_, check_result5xnext4reproduceable_, ResultTypes4xnext, NextEx, StopEx
    # basic tools

from seed.abc.IReproduceable import Iter4IReproduceable, iter_pairs4reproduceable_, iter_fsts4reproduceable_, iter_snds4reproduceable_, list_pairs4reproduceable_, list_fsts4reproduceable_, list_snds4reproduceable_
    # debug tools


from seed.abc.IReproduceable import *
