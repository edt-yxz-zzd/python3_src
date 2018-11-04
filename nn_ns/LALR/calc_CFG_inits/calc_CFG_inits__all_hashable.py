
__all__ = '''
    calc_CFG_inits__all_hashable
    '''.split()


from .calc_CFG_inits__all_hashable__using_MessageClosureExecutor import \
    calc_CFG_inits__all_hashable__using_MessageClosureExecutor
from .calc_CFG_inits import calc_CFG_inits
from .iter_rule_names_for_calc_CFG_inits import \
    iter_rule_names_for_calc_CFG_inits
from .make_rule_name2alternative_names import \
    make_rule_name2alternative_names
from .Ops.SetOps__alternative_name_set_ops import \
    SetOps__alternative_name_set_ops
from .Ops.MutableSetOps__alternative_name_mutable_set_ops import \
    MutableSetOps__alternative_name_mutable_set_ops
from .Ops.FullMappingOps__mapping__XXX_name_fullmapping_ops import \
    FullMappingOps__mapping__XXX_name_fullmapping_ops
from .Ops.FullMappingOps__sequence__XXX_name_fullmapping_ops import \
    FullMappingOps__sequence__XXX_name_fullmapping_ops

class _Box:
    # to provide box/unbox
    def __init__(self, obj):
        self.obj = obj
    @staticmethod
    def box(obj):
        self = __class__(obj)
        return self
    @staticmethod
    def unbox(self):
        return self.obj


def calc_CFG_inits__all_hashable(
    max_init_length
    ,alternative_name2rule_name
    ,alternative_name2ixsymbols
    ,*
    ,alternative_name_fullmapping_is_sequence : bool
    ,rule_name_fullmapping_is_sequence : bool
    ,naive : bool
    ):
    '''wrapper for calc_CFG_inits
requires: Hashable: rule_name, alternative_name, terminal_set_name

input:
    max_init_length             :: UInt
    alternative_name2rule_name  :: python.dict if not is_sequence else seq
    alternative_name2ixsymbols  :: python.dict if not is_sequence else seq
    alternative_name_fullmapping_is_sequence    :: bool
    rule_name_fullmapping_is_sequence           :: bool

output:
    rule_name2inits             :: python.dict or list
    alternative_name2initss     :: python.dict or list
        see: ..._is_sequence
see:
    calc_CFG_inits
'''
    if naive:
        f = calc_CFG_inits__all_hashable__naive
    else:
        f = calc_CFG_inits__all_hashable__using_MessageClosureExecutor
    return f(
        max_init_length
        ,alternative_name2rule_name
        ,alternative_name2ixsymbols
        ,alternative_name_fullmapping_is_sequence
            = alternative_name_fullmapping_is_sequence
        ,rule_name_fullmapping_is_sequence
            = rule_name_fullmapping_is_sequence
        )

def calc_CFG_inits__all_hashable__naive(
    max_init_length
    ,alternative_name2rule_name
    ,alternative_name2ixsymbols
    ,*
    ,alternative_name_fullmapping_is_sequence : bool
    ,rule_name_fullmapping_is_sequence : bool
    ):
    alternative_name_fullmapping_is_sequence = bool(alternative_name_fullmapping_is_sequence)
    rule_name_fullmapping_is_sequence = bool(rule_name_fullmapping_is_sequence)
    is_sequence = alternative_name_fullmapping_is_sequence

    if not is_sequence:
        assert set(alternative_name2rule_name) == set(alternative_name2ixsymbols)
    else:
        assert len(alternative_name2rule_name) == len(alternative_name2ixsymbols)



    box = _Box.box
    unbox = _Box.unbox
    alternative_name_set_ops = SetOps__alternative_name_set_ops(unbox=unbox)
    alternative_name_mutable_set_ops = MutableSetOps__alternative_name_mutable_set_ops(box=box, unbox=unbox)

    def mk_mapping_ops__dict(keys):
        return FullMappingOps__mapping__XXX_name_fullmapping_ops(keys, items2mapping=dict, unbox=unbox, box=box)
    def mk_mapping_ops__list(size):
        return FullMappingOps__sequence__XXX_name_fullmapping_ops(size, iterable2sequence=list, unbox=unbox, box=box)

    alternative_name_fullmapping_ops = (
        mk_mapping_ops__list(len(alternative_name2rule_name))
        if alternative_name_fullmapping_is_sequence else
        mk_mapping_ops__dict(frozenset(alternative_name2rule_name))
        )

    alternative_name2rule_name = box(alternative_name2rule_name)
    alternative_name2ixsymbols = box(alternative_name2ixsymbols)

    rule_names = frozenset(iter_rule_names_for_calc_CFG_inits(
                    alternative_name2rule_name
                    ,alternative_name2ixsymbols
                    ,alternative_name_fullmapping_ops
                    ))
    if rule_name_fullmapping_is_sequence:
        L = len(rule_names)
        if not rule_names:
            sz = 0
        else:
            M = max(rule_names)
            m = min(rule_names)
            if m < 0: raise ValueError
            sz = M+1
            if sz > 20+10*L:
                raise Warning(f'max rule name too large: len(rule_names)={L}, max(rule_names)={M}, rule_names={rule_names}')
        rule_name_fullmapping_ops = mk_mapping_ops__list(sz)
    else:
        rule_name_fullmapping_ops = mk_mapping_ops__dict(rule_names)

    rule_name2alternative_names = make_rule_name2alternative_names(
                                    alternative_name2rule_name
                                    , alternative_name_fullmapping_ops
                                    , rule_name_fullmapping_ops
                                    , alternative_name_mutable_set_ops
                                    )

    rule_name2inits, alternative_name2initss = calc_CFG_inits(
        max_init_length
        ,alternative_name2rule_name
        ,alternative_name2ixsymbols
        ,rule_name2alternative_names

        ,alternative_name_set_ops
        ,alternative_name_fullmapping_ops
        ,rule_name_fullmapping_ops
        )
    return unbox(rule_name2inits), unbox(alternative_name2initss)


