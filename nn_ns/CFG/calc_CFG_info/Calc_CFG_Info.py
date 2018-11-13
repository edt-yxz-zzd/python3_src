
__all__ = '''
    Calc_CFG_Info
    '''.split()



from ..CFG import CFG

from .calc_CFG_inits import calc_CFG_inits
from .calc_CFG_nonterminal_idx2sorted_production_idc import (
    calc_CFG_nonterminal_idx2sorted_production_idc)
from .calc_CFG_production_idx2idxalternative import (
    calc_CFG_production_idx2idxalternative
    )
from .calc_CFG_nonterminal_idx2sorted_used_locations import (
    calc_CFG_nonterminal_idx2sorted_used_locations
    )
from .calc_CFG_nullable import (
    calc_CFG_nullable__basic
    ,calc_CFG_nullable__is_nullable
    ,calc_CFG_nullable__one_tree
    )
import weakref # ref
from types import MethodType

class _Global:
    attr__cfg = '_Calc_CFG_Info__cfg'
    attr__cache = '_Calc_CFG_Info__cache'
    key__nonterminal_idx2inits = '__nonterminal_idx2inits'
    key__alternative_tail_idx2inits = '__alternative_tail_idx2inits'

def _get_cfg(self):
    cfg = object.__getattribute__(self, _Global.attr__cfg)()
    return cfg
def _get_cache(self):
    cache = object.__getattribute__(self, _Global.attr__cache)
    return cache

def calc_inits__if_not_exists(self, max_length):
    if not (type(max_length) is int and max_length >= 0):
        raise TypeError(f'not UInt: {max_length!r}')

    cache = _get_cache(self)
    if max_length in cache[_Global.key__nonterminal_idx2inits]:
        return

    cfg = _get_cfg(self)
    (nonterminal_idx2inits, alternative_tail_idx2inits
    ) = calc_CFG_inits(max_length, cfg)

    cache[_Global.key__nonterminal_idx2inits][max_length] = nonterminal_idx2inits
    cache[_Global.key__alternative_tail_idx2inits][max_length] = alternative_tail_idx2inits



class Calc_CFG_Info:
    '''

wrapper for calc_CFG_XXX
usage:
    # used in CFG.__init__

    calc = Calc_CFG_Info(cfg) # weakref only
    calc.XXX
        # eval and cache
        #   = calc_CFG_...XXX...(cfg...)
        #

'''
    def __init__(__self, __cfg):
        #from ..CFG import CFG
        #from seed.tiny import print_err
        #print_err(type(__cfg))
        assert isinstance(__cfg, CFG)

        __self.__cfg = weakref.ref(__cfg)
        __self.__cache = {
            _Global.key__nonterminal_idx2inits:{}
            ,_Global.key__alternative_tail_idx2inits:{}
            }

    def __getattribute__(self, attr):
        if attr.startswith('_'): raise AttributeError(attr)

        if attr in CFG.all_CFG_attr_set:
            cfg = _get_cfg(self)
            return getattr(cfg, attr)
        if attr in ('nonterminal_idx2inits_of_max_length'
                    ,'alternative_tail_idx2inits_of_max_length'
                    ):
            return MethodType(getattr(__class__, attr), self)

        cache = _get_cache(self)
        Nothing = object()
        may_value = cache.get(attr, Nothing)
        if may_value is Nothing:
            cfg = _get_cfg(self)
            may_value = getattr(__class__, attr)(self, cfg, cache)
            if may_value is None:
                # assume set attr in cache inside the call
                value = cache[attr]
            else:
                assert attr not in cache
                cache[attr] = value = may_value
        else:
            value = may_value
        return value

    def nonterminal_idx2inits_of_max_length(self, max_length):
        calc_inits__if_not_exists(self, max_length)
        cache = _get_cache(self)
        return cache[_Global.key__nonterminal_idx2inits][max_length]
    def alternative_tail_idx2inits_of_max_length(self, max_length):
        calc_inits__if_not_exists(self, max_length)
        cache = _get_cache(self)
        return cache[_Global.key__alternative_tail_idx2inits][max_length]




    #def xxx(self, cfg, cache): -> may_value
    def nonterminal_idx2sorted_production_idc(self, cfg, cache):
        return calc_CFG_nonterminal_idx2sorted_production_idc(
                num_nonterminals=self.num_nonterminals
                ,production_idx2nonterminal_idx=self.production_idx2nonterminal_idx
                )
    def production_idx2idxalternative(self, cfg, cache):
        return calc_CFG_production_idx2idxalternative(
                production_idx2alternative_tail_idx=self.production_idx2alternative_tail_idx
                ,alternative_tail_idx2alternative_idx_maybe_pair=self.alternative_tail_idx2alternative_idx_maybe_pair
                )

    def nonterminal_idx2sorted_used_locations(self, cfg, cache):
        return calc_CFG_nonterminal_idx2sorted_used_locations(
                num_nonterminals=self.num_nonterminals
                ,production_idx2idxalternative=self.production_idx2idxalternative
                )



    def nullable_production_idc_in_bottomup_order(self, cfg, cache):
        _calc_CFG_nullable__basic(self, cfg, cache)
    def production_idx2maybe_nullable_bottomup_order_idx(self, cfg, cache):
        _calc_CFG_nullable__basic(self, cfg, cache)
    def nonterminal_idx2maybe_first_discovered_nullable_production_idx(self, cfg, cache):
        _calc_CFG_nullable__basic(self, cfg, cache)

    def production_idx2is_nullable(self, cfg, cache):
        _calc_CFG_nullable__is_nullable(self, cfg, cache)
    def nonterminal_idx2is_nullable(self, cfg, cache):
        _calc_CFG_nullable__is_nullable(self, cfg, cache)

    def nonterminal_idx2sorted_nullable_production_idc(self, cfg, cache):
        _calc_CFG_nullable__one_tree(self, cfg, cache)
    def nonterminal_idx2maybe_one_null_tree(self, cfg, cache):
        _calc_CFG_nullable__one_tree(self, cfg, cache)
    def has_ambiguous_nullable_nonterminal(self, cfg, cache):
        _calc_CFG_nullable__one_tree(self, cfg, cache)


def _calc_CFG_nullable__basic(self, cfg, cache):
    (nullable_production_idc_in_bottomup_order
    ,production_idx2maybe_nullable_bottomup_order_idx
    ,nonterminal_idx2maybe_first_discovered_nullable_production_idx
    ) = calc_CFG_nullable__basic(
        production_idx2nonterminal_idx=self.production_idx2nonterminal_idx
        ,production_idx2idxalternative=self.production_idx2idxalternative
        ,nonterminal_idx2sorted_used_locations=self.nonterminal_idx2sorted_used_locations
        )
    cache.update(
        nullable_production_idc_in_bottomup_order
            =nullable_production_idc_in_bottomup_order
        ,production_idx2maybe_nullable_bottomup_order_idx
            =production_idx2maybe_nullable_bottomup_order_idx
        ,nonterminal_idx2maybe_first_discovered_nullable_production_idx
            =nonterminal_idx2maybe_first_discovered_nullable_production_idx
        )
    return None

def _calc_CFG_nullable__is_nullable(self, cfg, cache):
    (production_idx2is_nullable, nonterminal_idx2is_nullable
    ) = calc_CFG_nullable__is_nullable(
        production_idx2maybe_nullable_bottomup_order_idx=self.production_idx2maybe_nullable_bottomup_order_idx
        ,nonterminal_idx2maybe_first_discovered_nullable_production_idx=self.nonterminal_idx2maybe_first_discovered_nullable_production_idx
        )
    cache.update(
        production_idx2is_nullable=production_idx2is_nullable
        ,nonterminal_idx2is_nullable=nonterminal_idx2is_nullable
        )
    return None

def _calc_CFG_nullable__one_tree(self, cfg, cache):
    (nonterminal_idx2sorted_nullable_production_idc
    ,nonterminal_idx2maybe_one_null_tree
    ,has_ambiguous_nullable_nonterminal
    ) = calc_CFG_nullable__one_tree(
        production_idx2nonterminal_idx=self.production_idx2nonterminal_idx
        ,nonterminal_idx2sorted_used_locations=self.nonterminal_idx2sorted_used_locations
        ,production_idx2maybe_nullable_bottomup_order_idx=self.production_idx2maybe_nullable_bottomup_order_idx
        ,nonterminal_idx2maybe_first_discovered_nullable_production_idx=self.nonterminal_idx2maybe_first_discovered_nullable_production_idx
        )
    cache.update(
        nonterminal_idx2sorted_nullable_production_idc
            =nonterminal_idx2sorted_nullable_production_idc
        ,nonterminal_idx2maybe_one_null_tree
            =nonterminal_idx2maybe_one_null_tree
        ,has_ambiguous_nullable_nonterminal
            =has_ambiguous_nullable_nonterminal
        )
    return None

