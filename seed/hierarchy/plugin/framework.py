#__all__:goto
r'''[[[
e ../../python3_src/seed/hierarchy/plugin/framework.py




seed.hierarchy.plugin.framework
py -m nn_ns.app.debug_cmd   seed.hierarchy.plugin.framework -x
py -m nn_ns.app.doctest_cmd seed.hierarchy.plugin.framework:__doc__ -ff -v
py_adhoc_call   seed.hierarchy.plugin.framework   @f
from seed.hierarchy.plugin.framework import *






bg = background4recur_typ
fg = local_binds
symbol require bg, fg
typ = symbol | typ_info<symbol>
plugin = IPlugin<symbol>

symbol4method -> cntr4plugin
mkr4plugin = cntr4plugin+inm2param
mkr4plugin :: ICallable

class (pluginA, pluginB) => pluginX<a,b,c>:
    yyy :: (pluginS, pluginT) => ...
    ...
instance (pluginC, pluginD) => pluginX<A,B,C>:
    ...

mk<pluginX>(pluginA..pluginD, A,B,C)
    curr_typ_info=A,B,C
    ==>> xxx def call_method_(ops4bg, background4recur_typ, plugin4xxx, nm4xxx_yyy, acc_st4recur_call, curr_typ_info, /, *args, **kw):

def call_method_(ops4bg, background4recur_typ, plugin4xxx, nm4xxx_yyy, acc_st4recur_call, /, *args, **kw):
    #remove curr_typ_info
xxx def diff_(ops4bg, background4recur_typ, plugin4diff, __nm4diff__, acc_st4recur_call, curr_typ_info, lhs, rhs, /):
    __diff__ = ops4bg.get_attr(background4recur_typ, plugin4diff, curr_typ_info, __nm4diff__)
    ;   del curr_typ_info
    return __diff__(ops4bg, background4recur_typ, plugin4diff, __nm4diff__, acc_st4recur_call, lhs, rhs)






#]]]'''
__all__ = r'''
'''.split()#'''
__all__


class ISignature4TypeDependentCallable:
    # forall *tnms4typ_param. (**pnms4plugin) => (**inm2typ4in) -> typ4out
    #   like F, some tnms4typ_param cannot be deduce
    tnm2whether_typ_param_deduceable
        #tnm = good_tnm | bad_tnm
    pnms4plugin
    inms4input
    inm2typ4in -> typ4out -> good_tnm2typ_param
    tnm2typ_param -> pnm2plugin
class ISignature4Callable(ISignature4Callable):
    # forall *tnms4typ_param. (**pnms4plugin) => (**inm2typ4in) -> typ4out
    #xxx tnm2whether_typ_param_deduceable
    #   all typ_param deduceable
    tnms4typ_param
    pnms4plugin
    inms4input
    #xxx inm2typ4in -> typ4out -> good_tnm2typ_param
    inm2typ4in -> typ4out -> tnm2typ_param
    tnm2typ_param -> pnm2plugin
class ISignature4Method(ICallable):
    ???似乎不需要
    需要的是 symbol4method -> cntr4plugin
    # the_plugin -> forall *tnms4typ_param. (**pnms4plugin) => (**inm2typ4in) -> typ4out
    cntr4the_plugin # :: ICallable
    pnms4plugin #except the_plugin
    tnms4typ_param # >= cntr4the_plugin.tnms4typ_param
    inms4input
    inm2typ4in -> typ4out -> tnm2typ_param
    #tnm2typ_param -> (the_plugin, pnm2plugin)
    #   neednot <<== cntr4the_plugin :: ICallable
    tnm2typ_param -> pnm2plugin
class ISignature4PluginConstructor(ICallable):
    pnms4plugin
    tnms4typ_param
    #xxx inm2typ4in -> typ4out -> tnm2typ_param
    #   typ4out always be Plugin
    inm2typ4in -> tnm2typ_param
    tnm2typ_param -> pnm2plugin
class IPlugin:
    symbol4plugin_cntr #global name
    signature4plugin_cntr :: ISignature4PluginConstructor
    symbol2method
class IMethod:
    signature4method
    call8method(sf, bg, the_plugin, pnm2plugin, inm2x)->y
class ICallable:
    signature4callable
    call8func(sf, bg, pnm2plugin, inm2x)->y
class IOps:
    def get_attr(ops4bg, background4recur_typ, plugin4xxx, nm4xxx_yyy, /):
        '-> __xxx_yyy__'
    def deduce_required_plugins_(ops4bg, background4recur_typ, curr_plugins, __zzz__, /):
        '-> plugins4zzz'
    def call_(ops4bg, background4recur_typ, plugins4zzz, __zzz__, /, *args, **kw):
        '-> ???'

def call_method_(ops4bg, background4recur_typ, curr_plugins, plugin4xxx, nm4xxx_yyy, acc_st4recur_call, /, *args, **kw):
    __xxx_yyy__ = ops4bg.get_attr(background4recur_typ, plugin4xxx, nm4xxx_yyy)
    ;   del nm4xxx_yyy, plugin4xxx
    return call_func_(ops4bg, background4recur_typ, curr_plugins, acc_st4recur_call, __xxx_yyy__, *args, **kw)
        #using acc_st4recur_call
def call_func_(ops4bg, background4recur_typ, curr_plugins, acc_st4recur_call, __zzz__, /, *args, **kw):
    plugins4zzz = ops4bg.deduce_required_plugins_(background4recur_typ, curr_plugins, __zzz__)
    ;   del curr_plugins
    return ops4bg.call_(background4recur_typ, plugins4zzz, __zzz__, *args, **kw)


from seed.hierarchy.plugin.framework import *
