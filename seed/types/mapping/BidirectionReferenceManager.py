#__all__:goto
r'''[[[
e ../../python3_src/seed/types/mapping/BidirectionReferenceManager.py

seed.types.mapping.BidirectionReferenceManager
py -m nn_ns.app.debug_cmd   seed.types.mapping.BidirectionReferenceManager -x
py -m nn_ns.app.doctest_cmd seed.types.mapping.BidirectionReferenceManager:__doc__ -ht

[[[
required from:
    view ../../python3_src/seed/recognize/CFG/Grammar.py
        mk: {nonterminal:is_nullable}
        <<==:
        mk: {nonterminal:min_oolen}
        <<==:
        mk: {(nonterminal|producton_rule):min_oolen}
        def mk__node2min_oolen_sentence(...)
===
[reference <=> (src,dst) <=> dgraph.dedge]
[reference => inv_reference]
[inv_reference{reference} <=> (dst,src)]
===
sometimes we needs extra info:
    eg:iv2iiir2multiplicity@seed/recognize/CFG/Grammar.py

[reference <=> (src,dst,fwd_info)]
[inv_reference{reference} <=> (dst,src,bwd_info)]

===
[BidirectionReferenceManager == (forward_part, backward_part)]
[forward_part == unidirection_part{src,dst,fwd_info}]
[backward_part == unidirection_part{dst,src,bwd_info}]
[unidirection_part{u,v,info} := ({u:{v}} | {u:{v:info}})]


===
]]]






#]]]'''
__all__ = r'''
ReferenceManagerError
    Error__ref_existed

BidirectionReferenceManager
mk_UnidirectionReferenceManager
    UnidirectionReferenceManager__without_info
    UnidirectionReferenceManager__with_info

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_type_le# check_int_ge
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...


class ReferenceManagerError(Exception):pass
class Error__ref_existed(ReferenceManagerError):pass
class _UnidirectionReferenceManager:
    _has_extra_info_ = ...
    def __repr__(sf, /):
        return repr_helper(sf, sf._d)
    def __init__(sf, d=None, /):
        if d is None:
            d = {}
        sf._d = d
    ######################
    ######################
    def add(sf, u, v, /, *args, **kwds):
        if sf._has_extra_info_:
            f = sf.add__with_info
        else:
            f = sf.add__without_info
        return f(u, v, *args, **kwds)
    def remove(sf, u, v, /):
        if sf._has_extra_info_:
            f = sf.remove__with_info
        else:
            f = sf.remove__without_info
        return f(u, v)

    ######################
    ######################
    #def add__without_info(sf, u, v, /):
    def add__without_info(sf, u, v, info=None, /, *, acc=None, is_null_info_=None):
        'using same API as add__with_info to be used in BidirectionReferenceManager uniformly'
        if not sf._has_extra_info_:raise TypeError
        if not None is info is acc is is_null_info_:raise TypeError

        d = sf._d
        vs = d.setdefault(u, set())
        if v in vs:
            raise Error__ref_existed(u, v)
        vs.add(v)
    def remove__without_info(sf, u, v, /):
        if not sf._has_extra_info_:raise TypeError
        d = sf._d
        vs = d[u]
        vs.remive(v)
        if not vs:
            del d[u]

    ######################
    ######################
    def remove__with_info(sf, u, v, /):
        'see:add__with_info(become substract)'
        if sf._has_extra_info_:raise TypeError
        d = sf._d
        v2info = d[u]
        del v2info[v]
        if not v2info:
            del d[u]
    def add__with_info(sf, u, v, info, /, *, acc=None, is_null_info_=None):
        'may become remove'
        if sf._has_extra_info_:raise TypeError
        d = sf._d
        v2info = d.setdefault(u, {})
        while 1:
            if not (_info:=v2info.get(v, v2info)) is v2info:
                if acc is None:
                    raise Error__ref_existed(u, v, _info, info)
                if type(acc) is bool:
                    if not acc:
                        #no_new_info
                        new_info = _info
                        break #skip
                    #echo
                    new_info = info
                else:
                    # callable(acc)
                    new_info = acc(u, v, _info, info)
                new_info
            else:
                new_info = info
            new_info
            v2info[v] = new_info
            break
        new_info
        if not is_null_info_ is None:
            if is_null_info_(new_info):
                del v2info[v]
                if not v2info:
                    del d[u]
        return
    ######################
    ######################
class UnidirectionReferenceManager__without_info(_UnidirectionReferenceManager):
    _has_extra_info_ = False
class UnidirectionReferenceManager__with_info(_UnidirectionReferenceManager):
    _has_extra_info_ = True

_Ts4uni = (UnidirectionReferenceManager__without_info, UnidirectionReferenceManager__with_info)
def mk_UnidirectionReferenceManager(d=None, /, *, has_extra_info:bool):
    check_type_is(bool, has_extra_info)
    T = _Ts4uni[has_extra_info]
    return T(d)

class BidirectionReferenceManager:
    def __repr__(sf, /):
        return repr_helper(sf, sf._fwd, sf._bwd)
    def __init__(sf, forward_part, backward_part, /):
        check_type_le(_UnidirectionReferenceManager, forward_part)
        check_type_le(_UnidirectionReferenceManager, backward_part)

        sf._fwd = forward_part
        sf._bwd = backward_part
    ######################
    ######################
    def add__bidirection(sf, u, v, info4fwd, info4bwd, /, *, acc4fwd=None, is_null_info4fwd_=None, acc4bwd=None, is_null_info4bwd_=None):
        sf._fwd.add(u, v, info4fwd, acc=acc4fwd, is_null_info_=is_null_info4fwd_)
        sf._bwd.add(v, u, info4bwd, acc=acc4bwd, is_null_info_=is_null_info4bwd_)
    def remove__bidirection(sf, u, v, /):
        sf._fwd.remove(u, v)
        sf._fwd.remove(v, u)
    ######################
    ######################

__all__
from seed.types.mapping.BidirectionReferenceManager import BidirectionReferenceManager, mk_UnidirectionReferenceManager
from seed.types.mapping.BidirectionReferenceManager import *
