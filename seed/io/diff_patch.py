r'''[[[
e ../../python3_src/seed/io/diff_patch.py


seed.io.diff_patch
view ../../python3_src/seed/hierarchy/plugin/framework.py
see:
    view ../../python3_src/seed/abc/eq_by_id/PermanentSymbol.py
    view ../../python3_src/seed/helper/symbol.py
    view ../../python3_src/seed/helper/register.py


#]]]'''

#common
from seed.helper.symbol import mk_compact_extensional_path, unpack_compact_extensional_path
from seed.helper.symbol import BaseSymbol, TmpSymbol, PermanentSymbol

#author-side
from seed.helper.symbol import register_new_PermanentSymbol__compact, register_new_PermanentSymbol, fill_module_with_registered_permanent_symbols

#user-side
from seed.helper.symbol import PermanentSymbol, load_PermanentSymbol__compact, load_PermanentSymbol, get_extensional_path5PermanentSymbol, get_intensional_description5PermanentSymbol, mk_compact_extensional_path5PermanentSymbol



from seed.helper.register import RegisterRegister, plugin_mkr_register_register
from seed.tiny_.null_dev import null_context, null_context5result_

from seed.types.ops.IEmplaceStackOps import the_emplace_stack_ops4list, the_emplace_stack_ops4HugeStack
from seed.func_tools.recur5yield import recur5yield__decoratorT__all_gi_protocols, child_gi_protocol__echo, child_gi_protocol__0func, child_gi_protocolT__0func5ref, tail_recur_gi_protocol__echo, tail_recur_gi_protocol__off
#def recur5yield__decoratorT__all_gi_protocols(emplace_stack_ops, child_gi_protocol, tail_recur_gi_protocol, /):
#    child_gi_protocol(exprlist5yield) -> generator_iterator
from seed.types.GetArgsKwargs import GetArgsKwargs, GetFuncArgsKwargs

class mk_child_gi_protocol__fix_bg_st:
    def __init__(sf, bg, acc_st, /):
        check_type_le(IBackground4RecurTypeInfo, bg)
        sf.bg = bg
        sf.acc_st = acc_st
    def __call__(sf, exprlist5yield, /):
        '(GetArgsKwargs(plugin,symbol4xxx, ...)|GetFuncArgsKwargs(f/(bg,acc_st), ...)|generator_iterator)-> generator_iterator'
        if type(exprlist5yield) is GetFuncArgsKwargs:
            f_args_kws = exprlist5yield
            generator_iterator = f_args_kws.call0_input_then_me_(sf.bg, sf.acc_st)
        elif type(exprlist5yield) is GetArgsKwargs:
            args_kws = exprlist5yield
            [plugin, symbol4xxx, *args], kws = args_kws.get_args_kwargs()
            f = bg.get_method(plugin, symbol4xxx)
            generator_iterator = f(sf.bg, sf.acc_st, *args, **kws)
        else:
            generator_iterator = exprlist5yield
        return generator_iterator
#def child_gi_protocol__fix_bg_st(exprlist5yield, /):
#child_gi_protocol__fix_bg_st = mk_child_gi_protocol__fix_bg_st(bg, acc_st)

if 0:
  def diff_(ops4bg, background4recur_typ, plugin4diff, __nm4diff__, acc_st4recur_call, curr_typ_info, lhs, rhs, /):
    __diff__ = ops4bg.get_attr(background4recur_typ, plugin4diff, curr_typ_info, __nm4diff__)
    ;   del curr_typ_info
    return __diff__(ops4bg, background4recur_typ, plugin4diff, __nm4diff__, acc_st4recur_call, lhs, rhs)

import contextlib # contextlib.ContextManager
@contextlib.ContextManager
def with_context4target_slot_in_accumulator_state_(bg, acc_st, symbol4target, /):
    existed = bg.setup_target_slot_in_accumulator_state_if_not_exists_(acc_st, symbol4target)
    try:
        yield
    finally:
        bg.clean_target_slot_in_accumulator_state_if_not_existed_(acc_st, symbol4target, existed)

class IPlugin4get_method4bg:
    __slots__ = ()
    def get_method__bg(plugin, bg, symbol4xxx, /):
        '-> xxx'
        raise NotImplementedError
class Plugin4get_method4bg__via_register(IPlugin4get_method4bg):
    #def __init__(plugin, /):
    def get_method__bg(plugin, bg, symbol4xxx, /):
        '-> xxx'
        return plugin.lookup(symbol4xxx)
    def lookup(plugin, symbol4xxx, /):
        return plugin.__dict__[symbol4xxx]
    def register(plugin, symbol4xxx, xxx, /):
        dict_add_is(plugin.__dict__, symbol4xxx, xxx)
default_plugin = Plugin4get_method4bg__via_register()
r'''
hs.class H a b
hs.instance H (A p q) (B x y)

hs.class H a b
    f :: a -> b
hs.class H_A_B p q x y
    f2 :: (A p q) -> (B x y)
hs.instance (H_A_B p q x y) => H (A p q) (B x y)
    f = f2


protocol === ops
{symbol4method:plugin_api_header}
protocol 虽然独立出来，但为了解耦protocol*plugin, plugin_api_header/typ_params/typ_info 必须 独立于protocol, 作为 通用接口，这样 用户代码 就能 调用protocol.mk_plugin(plugin_api_header, *typ_params)->plugin
{protocol:{plugin_api_header:plugin_mkr}}
protocol def what is bg/plugin/acc_st...
plugin_mkr :: *params -> plugin
    ??? user to mk plugin ???
plugin -> symbol4method -> method


symbol4method -> plugin_api_header
plugin_api_header -> (*typ_params) -> plugin
    search a match

plugin_mkr_register_register
'symbol4xxx -> plugin_header'
'plugin_header -> plugin_mkr'
'plugin_mkr(*typ_params) -> plugin'
'plugin -> symbol4xxx -> method4xxx'
class Plugin4get_method4bg__via_plugin_register_register(IPlugin4get_method4bg):
    def __init__(plugin, typ_cntr, /, *typ_params):
        sf._typ_cntr = typ_cntr
        sf._typ_params = typ_params
    @property
    def typ_cntr(sf, /):
class Plugin4get_method4bg__via_plugin_register_register(IPlugin4get_method4bg):
    def __init__(plugin, typ_cntr, /, *typ_params):
        sf._typ_cntr = typ_cntr
        sf._typ_params = typ_params
    @property
    def typ_cntr(sf, /):
        return sf._typ_cntr
    @property
    def typ_params(sf, /):
        return sf._typ_params
    def get_method__bg(plugin, bg, symbol4xxx, /):
        '-> xxx'
        plugin_mkr = plugin_mkr_register_register.lookup_lookup(symbol4xxx, sf.typ_cntr)
        _plugin = plugin_mkr(*sf.typ_params)
        return _plugin.get_method__bg(bg, symbol4xxx)
r'''#'''


class IBackground4RecurTypeInfo:
    #bg = ops4bg, background4recur_typ
    __slots__ = ()
    def get_info5symbol(sf, symbol, /):
        'symbol -> info'
        raise NotImplementedError

    def mk_accumulator_state4whole_calc_(bg, /):
        '-> acc_st #for recur_call'
        raise NotImplementedError
    def setup_target_slot_in_accumulator_state_if_not_exists_(bg, acc_st, symbol4target, /):
        '-> existed/bool'
        raise NotImplementedError
    def clean_target_slot_in_accumulator_state_if_not_existed_(bg, acc_st, symbol4target, existed, /):
        '-> None'
        raise NotImplementedError

    def get_method(bg, plugin, symbol4xxx, /):
        '-> xxx'
        raise NotImplementedError
    if 0:
        def get_attr(bg, plugin, symbol4xxx, /):
            '-> xxx'
            raise NotImplementedError
        def get_property(bg, plugin, symbol4xxx, /):
            '-> xxx'
            raise NotImplementedError

class IMixin4Background4RecurTypeInfo__using_sf_dict_as_symbol2info(IBackground4RecurTypeInfo):
    #xxx __slots__ = ()
    def get_info5symbol(sf, symbol, /):
        'symbol -> info'
        return sf.__dict__[symbol]

class IMixin4Background4RecurTypeInfo__using_IPlugin4get_method4bg(IBackground4RecurTypeInfo):
    __slots__ = ()
    def get_method(bg, plugin, symbol4xxx, /):
        '-> xxx'
        return plugin.get_method__bg(bg, symbol4xxx)
class IMixin4Background4RecurTypeInfo__get_method5plugin_dict(IBackground4RecurTypeInfo):
    __slots__ = ()
    def get_method(bg, plugin, symbol4xxx, /):
        '-> xxx'
        return plugin.__dict__[symbol4xxx]
class IMixin4Background4RecurTypeInfo__using_dict_as_acc_st(IBackground4RecurTypeInfo):
    __slots__ = ()
    def mk_accumulator_state4whole_calc_(bg, /):
        '-> acc_st #for recur_call'
        return {}
    def setup_target_slot_in_accumulator_state_if_not_exists_(bg, acc_st, symbol4target, /):
        '-> existed/bool'
        _st = {}
        st = acc_st.setdefault(symbol4target, _st)
        return not st is _st
    def clean_target_slot_in_accumulator_state_if_not_existed_(bg, acc_st, symbol4target, existed, /):
        '-> None'
        if existed:
            del acc_st[symbol4target]

class Background4RecurTypeInfo__plugin5register(IMixin4Background4RecurTypeInfo__using_dict_as_acc_st, IMixin4Background4RecurTypeInfo__using_IPlugin4get_method4bg, IMixin4Background4RecurTypeInfo__using_sf_dict_as_symbol2info):
    pass
_default_bg = Background4RecurTypeInfo__plugin5register()
default_plugin

cls2plugin
plugin.get_method__bg


def main4xxx_(bg, may_acc_st, __symbol4xxx__, __symbol4acc_st4xxx__, plugin4xxx4curr_typ, , /, *args, **kwds):
    acc_st = ifNonef(may_acc_st, bg.mk_accumulator_state4whole_calc_)
    child_gi_protocol__fix_bg_st = mk_child_gi_protocol__fix_bg_st(bg, acc_st)
    recur5yield__fix_bg_st = recur5yield__decoratorT__all_gi_protocols(the_emplace_stack_ops4list, child_gi_protocol__fix_bg_st, tail_recur_gi_protocol__echo)
    with with_context4target_slot_in_accumulator_state_(acc_st, __symbol4acc_st4xxx__):
        return recur5yield__fix_bg_st(_gi_xxx__)(__symbol4xxx__, plugin4xxx4curr_typ, *args, **kwds)
def _gi_xxx__(__symbol4xxx__, plugin4xxx4curr_typ, , /, *args, **kwds):
    result = yield GetArgsKwargs(plugin4xxx4curr_typ, __symbol4xxx__, *args, **kwds)
    return result
def mk_gi_xxx_(__symbol4xxx__, /):
    '-> gi_xxx_'
    gi_xxx_ = curry1(_gi_xxx__, __symbol4xxx__)
    return _gi_xxx__







def diff_(bg, may_acc_st, plugin4diff4curr_typ, lhs, rhs, /):
    return main4xxx_(bg, may_acc_st, __symbol4diff__, __symbol4acc_st4diff__, plugin4diff4curr_typ, lhs, rhs)
gi_diff_ = mk_gi_xxx_(__symbol4diff__)

if 0:
  def gi_diff_(plugin4diff4curr_typ, lhs, rhs, /):
    the_patch = yield GetArgsKwargs(plugin4diff4curr_typ, __symbol4diff__, lhs, rhs)
    return the_patch
if 0:
  def _diff_(bg, plugin4diff4curr_typ, acc_st4recur_call, lhs, rhs, /):
    diff4curr_typ_ = bg.get_method(plugin4diff4curr_typ, __symbol4diff__)
    the_patch = diff4curr_typ_(plugin4diff4curr_typ, acc_st4recur_call, lhs, rhs)
    return the_patch



if 0:
    __symbol4diff__ = object()
    __symbol4acc_st4diff__ = object()
else:
    register_new_PermanentSymbol__compact(f'seed.io.diff_patch:diff:'




