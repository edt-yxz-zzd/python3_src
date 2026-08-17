#__all__:goto
#TODO:++yield
#TODO:++catched suppress+reraise...
r'''[[[
e ../../python3_src/seed/func_tools/call_frame.py
see also:
    seed.iters.flatten_recur
        view ../../python3_src/seed/iters/flatten_recur.py
    seed.func_tools.recur5yield
        view ../../python3_src/seed/func_tools/recur5yield.py


seed.func_tools.call_frame
py -m nn_ns.app.debug_cmd   seed.func_tools.call_frame -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.func_tools.call_frame:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/all_factors_of_.py
]]

[[
lookup_callee5ID_(ID4callee) -> callee
callee.on_call_(ID4callee, rich_input) -> st|^exc
######caller.on_subcall_exit_(ID4caller, st6exit, either_exc_oresult5subcall) -> rich_output|^exc
caller.on_subcall_return_(ID4caller, st6exit, oresult5subcall) -> rich_output|^exc
caller.on_subcall_raise_(ID4caller, st6exit, exc5subcall, call_frame7spot) -> rich_output|^exc
callee.on_loop_(ID4callee, st) -> rich_output|^exc

rich_output =:
    |^exc
    # |Either(exc, oresult)
    |Return(oresult)
    |Raise(exc, may_call_frame7spot)

    |Call7into(?ID4caller, st6exit, ID4callee, rich_input)
    |Call7recur(?ID4caller, st6exit, rich_input)
    |Call7tail(?ID4caller, ID4callee, rich_input)

    |Call7into7st(?ID4caller, st6exit, ID4callee, st)
    |Call7recur7st(?ID4caller, st6exit, st)
    |Call7tail7st(?ID4caller, ID4callee, st)
        #|Jmp7long(?ID4caller, ID4callee, st)
    |Jmp7short(?ID4caller, st)
]]


'#'; __doc__ = r'#'
>>> class Ops4Callee7test7listing_all_factors5pairs(IOps4Callee):
...     ___no_slots_ok___ = True
...     def __repr__(sf, /):
...         return repr_helper(sf)
...     @override
...     def mk_initial_state4callee_(sf, ID4callee8this, rich_input, /):
...         (p_e_pairs, rglnkls8us, j) = rich_input
...         if not rglnkls8us:
...             rglnkls8us = (rglnkls8us, 1)
...         if j == len(p_e_pairs):
...             nm = 'return_'
...             payload = rglnkls8us
...         else:
...             u = rglnkls8us[-1]
...             nm = 'pass_to_sibling_'
...             payload = (p_e_pairs, j, e:=0, u, rglnkls8us)
...         st = (nm, payload)
...         return st
...     def return_(sf, ID4callee8this, x, payload, /):
...         match (x, payload):
...             case ((0,), rglnkls8us):
...                 return Return(rglnkls8us)
...         raise 000
...     def pass_to_sibling_(sf, ID4callee8this, x, payload, /):
...         match (x, payload):
...             case ((0,), (p_e_pairs, j, e, u, rglnkls8us)):
...                 jpp = 1+j
...                 rich_input = (p_e_pairs, rglnkls8us, jpp)
...                 st6exit = ('try_inc_exp_', (p_e_pairs, j, e, u))
...                 return Call7recur(st6exit, rich_input)
...         raise 000
...     def try_inc_exp_(sf, ID4callee8this, x, payload, /):
...         match (x, payload):
...             case ((1, rglnkls8us), (p_e_pairs, j, e, u)):
...                 (p, max4e) = p_e_pairs[j]
...                 if e == max4e:
...                     nm = 'return_'
...                     payload = rglnkls8us
...                 else:
...                     e += 1
...                     u *= p
...                     rglnkls8us = (rglnkls8us, u)
...                     nm = 'pass_to_sibling_'
...                     payload = (p_e_pairs, j, e, u, rglnkls8us)
...                 st = (nm, payload)
...                 return Jmp7short(st)
...         raise 000
>>> callee7divisors = Callee5ops(Ops4Callee7test7listing_all_factors5pairs())
>>> callee7divisors
Callee5ops(Ops4Callee7test7listing_all_factors5pairs())

>>> call_sys7divisors = CallSys5dict(dict(callee7divisors=callee7divisors))
>>> call_sys7divisors
CallSys5dict({'callee7divisors': Callee5ops(Ops4Callee7test7listing_all_factors5pairs())})


#def call_(call_sys, ID4callee, rich_input, /):
>>> call_(call_sys7divisors, 'callee7divisors', ([(2,3),(3,2),(5,1)], (), 0))
(((((((((((((((((((((((((), 1), 5), 3), 15), 9), 45), 2), 10), 6), 30), 18), 90), 4), 20), 12), 60), 36), 180), 8), 40), 24), 120), 72), 360)














py_adhoc_call   seed.func_tools.call_frame   @f
from seed.func_tools.call_frame import *
]]]'''#'''
__all__ = r'''
ICallSys
    Error4CallSys
        Error4CallSys__NameError
    CallSys5dict
    call_
        default_call_
            CallFrame
            mk_CallFrame_
                mk_root_CallFrame_
    ICallee
        Callee5ops
            IOps4Callee
        Types4rich_output
            Raise
            Return
            Call7into
            Call7recur
            Call7tail
            Call7into7st
            Call7recur7st
            Call7tail7st
            Jmp7long
            Jmp7short


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_type_le, check_may_
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple__check6make_
    from seed.helper.repr_input import repr_helper
#.#################################
___end_mark_of_excluded_global_names__0___ = ...



_debug = True


class ICallee(ABC):
    'callee'
    __slots__ = ()
    @abstractmethod
    def on_call_(callee, ID4callee, rich_input, /):
        '-> st|^exc'
    @abstractmethod
    def on_subcall_return_(caller, ID4caller, st6exit, oresult5subcall, /):
        '-> rich_output|^exc'
    @abstractmethod
    def on_subcall_raise_(caller, ID4caller, st6exit, exc5subcall, call_frame7spot, /):
        '-> rich_output|^exc'
    @abstractmethod
    def on_loop_(callee, ID4callee, st, /):
        '-> rich_output|^exc'


class Error4CallSys(Exception):pass
class Error4CallSys__NameError(Error4CallSys, NameError):pass
    # NameError --> [UnboundLocalError]
class ICallSys(ABC):
    'call_sys'
    __slots__ = ()
    @abstractmethod
    def _lookup_callee5ID_(sf, ID4callee, /):
        '-> callee/ICallee | ^LookupError{will be converted to Error4CallSys__NameError}'
    def lookup_callee5ID_(sf, ID4callee, /):
        '-> callee/ICallee | ^Error4CallSys__NameError'
        try:
            callee = sf._lookup_callee5ID_(ID4callee)
        except LookupError:
            raise Error4CallSys__NameError(ID4callee)
        if _debug:
            check_type_le(ICallee, callee)
        return callee

    def call_(sf, ID4callee, rich_input, /):
        'object -> object -> oresult|^exc'
        return default_call_(sf, ID4callee, rich_input)

def call_(call_sys, ID4callee, rich_input, /):
    'ICallSys -> object -> object -> oresult|^exc'
    return call_sys.call_(ID4callee, rich_input)

_CallFrame = mk_namedtuple__check6make_(__name__, '_CallFrame', 'may_parent ID4callee callee state')
class CallFrame(_CallFrame):
    'call_frame/fm'
    def _check6make_(sf, /):
        if _debug:
            check_may_([check_type_is, CallFrame], sf.may_parent)
            check_type_le(ICallee, sf.callee)
        pass
    def ireplace_state_(sf, state7new, /):
        return sf._replace(state=state7new)

def mk_root_CallFrame_(call_sys, ID4callee, rich_input, /):
    '-> CallFrame | ^Error4CallSys__NameError | ^exc{@ .on_call_()}'
    return mk_CallFrame_(call_sys, may_parent:=None, ID4callee, rich_input)
def mk_CallFrame_(call_sys, may_parent, ID4callee, rich_input, /, *, may_callee=None, to_treat_rich_input_as_state=False):
    '-> CallFrame | ^Error4CallSys__NameError | ^exc{@ .on_call_()}'
    callee = call_sys.lookup_callee5ID_(ID4callee) if None is may_callee else may_callee
        # ^Error4CallSys__NameError
    st = rich_input if to_treat_rich_input_as_state else callee.on_call_(ID4callee, rich_input)
        # ^exc{@ .on_call_()}
    fm = CallFrame(may_parent, ID4callee, callee, st)
    return fm
def default_call_(call_sys, ID4callee, rich_input, /, *, may_callee=None, to_treat_rich_input_as_state=False, call_frame=None, Exception7catched=BaseException):
    'ICallSys -> object -> object -> oresult|^exc'
    ######################
    if not issubclass(Error4CallSys__NameError, Exception7catched):
        Exception7catched = (Exception7catched, Error4CallSys__NameError)
    Exception7catched
    ######################
    fm = call_frame
    msg = ('call', fm, ID4callee, may_callee, to_treat_rich_input_as_state, rich_input)
    ######################
    while 1:
        match msg:
            case ('call', fm, ID4callee, may_callee, to_treat_rich_input_as_state, rich_input):
                # MAYBE:[fm is None]
                try:
                    fm = mk_CallFrame_(call_sys, fm, ID4callee, rich_input, may_callee=may_callee, to_treat_rich_input_as_state=to_treat_rich_input_as_state)
                        # ^Error4CallSys__NameError
                        # ^exc{@ .on_call_()}
                except Exception7catched as exc:
                    # MAYBE:[fm is None]
                    if None is fm:
                        msg = ('raise', exc, fm)
                    else:
                        # [fm is not None]
                        rich_output = Raise(exc, fm)
                        msg = ('switch', fm, rich_output)
                        # [fm is not None]
                    msg
                else:
                    fm2rich_output_ = _fm2rich_output__7loop_
                    msg = ('lazy', fm, fm2rich_output_, ())
                    # [fm is not None]
                msg
            case ('lazy', fm, fm2rich_output_, ex_args):
                # [fm is not None]
                try:
                    rich_output = fm2rich_output_(fm, *ex_args)
                        # ^exc
                except Exception7catched as exc:
                    rich_output = Raise(exc, fm)
                if _debug:
                    check_type_le(Types4rich_output, rich_output)
                rich_output
                msg = ('switch', fm, rich_output)
                # [fm is not None]
            case ('switch', fm, rich_output):
                # [fm is not None]
                msg = _4switch(fm, rich_output)
            case ('return', oresult):
                return oresult
            case ('raise', exc, fm):
                # MAYBE:[fm is None]
                raise exc
            case _:
                raise Exception(msg)
        #end-match msg:
    #end-while 1:
    raise 000
    ######################

_fm2rich_output__7loop_ = lambda fm,/:fm.callee.on_loop_(fm.ID4callee, fm.state)
_fm2rich_output__7raise_ = lambda fm,exc,call_frame7spot,/:fm.callee.on_subcall_raise_(fm.ID4callee, fm.state, exc, call_frame7spot)
_fm2rich_output__7return_ = lambda fm, oresult,/:fm.callee.on_subcall_return_(fm.ID4callee, fm.state, oresult)

def _4switch(fm, rich_output, /):
    match rich_output:
        case Return(oresult):
            fm = fm.may_parent
            # MAYBE:[fm is None]
            if None is fm:
                msg = ('return', oresult)
            else:
                # [fm is not None]
                fm2rich_output_ = _fm2rich_output__7return_
                msg = ('lazy', fm, fm2rich_output_, (oresult,))
                # [fm is not None]
            msg
        case Raise(exc, may_call_frame7spot):
            # [fm is not None]
            call_frame7spot = fm if None is may_call_frame7spot else may_call_frame7spot
            fm = fm.may_parent
            # MAYBE:[fm is None]
            if None is fm:
                msg = ('raise', exc, call_frame7spot)
            else:
                # [fm is not None]
                fm2rich_output_ = _fm2rich_output__7raise_
                msg = ('lazy', fm, fm2rich_output_, (exc, call_frame7spot))
                # [fm is not None]
            msg
        case Call7into(st6exit, ID4callee, rich_input):
            fm = fm.ireplace_state_(st6exit)
            may_callee = None
            to_treat_rich_input_as_state = False
            msg = ('call', fm, ID4callee, may_callee, to_treat_rich_input_as_state, rich_input)
            # MAYBE:[fm is None]
        case Call7recur(st6exit, rich_input):
            fm = fm.ireplace_state_(st6exit)
            ID4callee = fm.ID4callee
            may_callee = fm.callee
            to_treat_rich_input_as_state = False
            msg = ('call', fm, ID4callee, may_callee, to_treat_rich_input_as_state, rich_input)
            # MAYBE:[fm is None]
        case Call7tail(ID4callee, rich_input):
            fm = fm.may_parent
            # MAYBE:[fm is None]
            may_callee = None
            to_treat_rich_input_as_state = False
            msg = ('call', fm, ID4callee, may_callee, to_treat_rich_input_as_state, rich_input)
            # MAYBE:[fm is None]
        case Call7into7st(st6exit, ID4callee, st):
            #Call7into
            fm = fm.ireplace_state_(st6exit)
            may_callee = None
            to_treat_rich_input_as_state = True
            777;rich_input = st
            msg = ('call', fm, ID4callee, may_callee, to_treat_rich_input_as_state, rich_input)
            # MAYBE:[fm is None]
        case Call7recur7st(st6exit, st):
            #Call7recur
            fm = fm.ireplace_state_(st6exit)
            ID4callee = fm.ID4callee
            may_callee = fm.callee
            to_treat_rich_input_as_state = True
            777;rich_input = st
            msg = ('call', fm, ID4callee, may_callee, to_treat_rich_input_as_state, rich_input)
            # MAYBE:[fm is None]
        case Call7tail7st(ID4callee, st):
            #|Jmp7long(ID4callee, st)
            #Call7tail
            fm = fm.may_parent
            # MAYBE:[fm is None]
            may_callee = None
            to_treat_rich_input_as_state = True
            777;rich_input = st
            msg = ('call', fm, ID4callee, may_callee, to_treat_rich_input_as_state, rich_input)
            # MAYBE:[fm is None]
        case Jmp7short(st):
            fm = fm.ireplace_state_(st)
            fm2rich_output_ = _fm2rich_output__7loop_
            msg = ('lazy', fm, fm2rich_output_, ())
            # [fm is not None]
        case _:
            raise Exception(rich_output)
    #end-match rich_output:
    return msg












_Raise = mk_namedtuple__check6make_(__name__, '_Raise', 'exc, may_call_frame7spot')
class Raise(_Raise):
    def _check6make_(sf, /):
        if _debug:
            check_type_le(BaseException, sf.exc)
            check_may_([check_type_is, CallFrame], sf.may_call_frame7spot)
        pass

_Return = mk_namedtuple__check6make_(__name__, '_Return', 'oresult')
class Return(_Return):
    def _check6make_(sf, /):
        pass

_Call7into = mk_namedtuple__check6make_(__name__, '_Call7into', 'st6exit, ID4callee, rich_input')
class Call7into(_Call7into):
    def _check6make_(sf, /):
        pass

_Call7recur = mk_namedtuple__check6make_(__name__, '_Call7recur', 'st6exit, rich_input')
class Call7recur(_Call7recur):
    def _check6make_(sf, /):
        pass

_Call7tail = mk_namedtuple__check6make_(__name__, '_Call7tail', 'ID4callee, rich_input')
class Call7tail(_Call7tail):
    def _check6make_(sf, /):
        pass

_Call7into7st = mk_namedtuple__check6make_(__name__, '_Call7into7st', 'st6exit, ID4callee, st4callee')
class Call7into7st(_Call7into7st):
    def _check6make_(sf, /):
        pass

_Call7recur7st = mk_namedtuple__check6make_(__name__, '_Call7recur7st', 'st6exit, st4callee')
class Call7recur7st(_Call7recur7st):
    def _check6make_(sf, /):
        pass

_Call7tail7st = mk_namedtuple__check6make_(__name__, '_Call7tail7st', 'ID4callee, st4callee')
class Call7tail7st(_Call7tail7st):
    def _check6make_(sf, /):
        pass
Jmp7long = Call7tail7st

_Jmp7short = mk_namedtuple__check6make_(__name__, '_Jmp7short', 'st4callee')
class Jmp7short(_Jmp7short):
    def _check6make_(sf, /):
        pass

Types4rich_output = (
(Raise
,Return
,Call7into
,Call7recur
,Call7tail
,Call7into7st
,Call7recur7st
,Call7tail7st
,Jmp7short
))

r'''[[[
_X = mk_namedtuple__check6make_(__name__, '_X', 'x')
class X(_X):
    def _check6make_(sf, /):
        if _debug:
            check_type_le(Y, sf.x)
#]]]'''#'''

class CallSys5dict(ICallSys):
    ___no_slots_ok___ = True
    def __init__(sf, ID2callee, /):
        if not all(isinstance(callee, ICallee) for ID4callee, callee in ID2callee.items()):raise TypeError(ID2callee)
        sf._d = ID2callee
    @property
    def ID2callee(sf, /):
        '-> {ID4callee:ICallee}'
        return sf._d
    def __repr__(sf, /):
        return repr_helper(sf, sf.ID2callee)
    @override
    def _lookup_callee5ID_(sf, ID4callee, /):
        return sf.ID2callee[ID4callee]

class IOps4Callee(ABC):
    'ops4callee:[st :: (nm, payload)]: getattr(ops4callee, nm)(ID4callee{this}, ((-1,exc5subcall,call_frame7spot)|(0,)|(+1,oresult5subcall)), payload) -> rich_output'
    __slots__ = ()
    @abstractmethod
    def mk_initial_state4callee_(sf, ID4callee8this, rich_input, /):
        '-> st'
class Callee5ops(ICallee):
    ___no_slots_ok___ = True
    def __init__(sf, ops4callee, /):
        check_type_le(IOps4Callee, ops4callee)
        sf._ops = ops4callee
    @property
    def ops4callee(sf, /):
        '-> IOps4Callee'
        return sf._ops
    def __repr__(sf, /):
        return repr_helper(sf, sf.ops4callee)
    @override
    def on_call_(sf, ID4sf, rich_input, /):
        st = sf.ops4callee.mk_initial_state4callee_(ID4sf, rich_input)
        return st
    @override
    def on_subcall_return_(sf, ID4sf, st6exit, oresult5subcall, /):
        (nm, payload) = st6exit
        f = getattr(sf.ops4callee, nm)
        return f(ID4sf, (+1, oresult5subcall), payload)
    @override
    def on_subcall_raise_(sf, ID4sf, st6exit, exc5subcall, call_frame7spot, /):
        (nm, payload) = st6exit
        f = getattr(sf.ops4callee, nm)
        return f(ID4sf, (-1, exc5subcall, call_frame7spot), payload)
    @override
    def on_loop_(sf, ID4sf, st, /):
        (nm, payload) = st
        f = getattr(sf.ops4callee, nm)
        return f(ID4sf, (0,), payload)

__all__
from seed.func_tools.call_frame import Error4CallSys, Error4CallSys__NameError
from seed.func_tools.call_frame import default_call_, CallFrame, mk_CallFrame_, mk_root_CallFrame_


from seed.func_tools.call_frame import ICallSys, call_
#def call_(call_sys, ID4callee, rich_input, /):

from seed.func_tools.call_frame import ICallee, Types4rich_output, Raise, Return, Call7into, Call7recur, Call7tail, Call7into7st, Call7recur7st, Call7tail7st, Jmp7long, Jmp7short
from seed.func_tools.call_frame import CallSys5dict, Callee5ops, IOps4Callee



from seed.func_tools.call_frame import *
