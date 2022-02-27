#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.hierarchy.plugin_api4register.stable_repr4export_long_term_storage
py -m    seed.hierarchy.plugin_api4register.stable_repr4export_long_term_storage
py -m nn_ns.app.debug_cmd   seed.hierarchy.plugin_api4register.stable_repr4export_long_term_storage


mkdir ../../python3_src/seed/hierarchy/plugin_api4register/
py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/hierarchy/plugin_api4register/stable_repr4export_long_term_storage.py
e ../../python3_src/seed/hierarchy/plugin_api4register/stable_repr4export_long_term_storage.py


from seed.hierarchy.plugin_api4register.stable_repr4export_long_term_storage import ...

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.hierarchy.register.AttachmentDataRegister4cls import attachment_data_register4cls, IHandler4AttachmentDataRegister4cls, default_handler4AttachmentDataRegister4cls, FunctionalHandler4AttachmentDataRegister4cls
from seed.hierarchy.symbol.PrivateSymbol import PrivateSymbol
r"""
import ...
from seed.tiny import str2__all__
__all__ = str2__all__(r'''#)
    #(''')
from seed.abc.abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from seed.helper.repr_input import repr_helper
from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
from seed.helper.check.checkers import check_pair, check_type_is
  #from seed.helper.check.checkers import checks, checkers, check_funcs
  #view ../../python3_src/seed/helper/check/checkers.py
if 0b00:#[01_to_turn_off]
    #0b01
    print(fr'x={x}')
    from seed.tiny import print_err
    print_err(fr'x={x}')
    from pprint import pprint
    pprint(x)
#"""
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#Expression4Repr:goto
#ExpressionSnippet4Repr:goto
#zzzwww:goto

#[[[Expression4Repr:begin
Var #bool?
Literal #int, str, bytes ...
SpecialMethod #op, x.a, x[k], x(a)
Container #tuple, list, set, dict
helper-constructor:
    var.x -> Var('x')
    kw.x -> 'x'
    ordered-dict/kwargs:
            ordered_pairs[k:w, ...]
            ordered_pairs[kw.k:w, ...]


#class BaseExpression4Repr:
class BaseExpression(ABC):
    r'''
    .controller_holder
        .___getattr4symbol___(symbol4controller4expr) -> controller
            .does_accept_constructor('__or__')
           x+y ==>> __add__ ==>>
            m = getattr(controller, mkAdd, sf.mkAdd)
            if m is False: raise Rejected
                False to reject mkAdd
    pure form:
        #apply to at least one expr to get the controller_holder hence controller
        #   all controller_holder MUST BE identical
        includes special method:
            op x
            x op y
            x(a, *ls, k=w, **d)
            x[k, i:j:k]
            x.y
        includes nonempty_container-in-list-form:
                (x, *ls)
                [x, *ls]
                {x, *ls}
                {k:v, **d}

        donot include var, literal, empty_container...
            xxx
            ??? True, False, None
            111, 'xxx', b'xxx'
            (), [], {}
            ... #Ellipsis to repr recur...
            these are impure&basic, assigned with an obj which identify env+hierarchy+...，prevent/reject some construction
    #'''
    __slots__ = ()

    #excluded: __ixxx__
    ['__abs__', '__add__', '__and__', '__concat__', '__contains__', '__delitem__', '__eq__', '__floordiv__', '__ge__', '__getitem__', '__gt__'
    , '__iadd__', '__iand__', '__iconcat__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__inv__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__itruediv__', '__ixor__'
    , '__le__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__not__', '__or__', '__pos__', '__pow__', '__rshift__', '__setitem__', '__sub__', '__truediv__', '__xor__'
    ]
    def __getattribute__(sf, attr, /):

        return mkGetAttr(sf, attr)
    def __getitem__(sf, key, /):
        return mkGetItem(sf, key)
    def __call__(sf, *args, **kwargs, /):
        return mkCall(sf, *args, **kwargs)

GetAttr
GetItem



symbol4stable_repr4export_long_term_storage = PrivateSymbol('symbol4stable_repr4export_long_term_storage'
        , __doc__ = r'''
    user_supported_plugin4repr
        (obj, repr_func4detect_recuri, /) -> Expression4Repr

    repr_func4detect_recur
        {.mapping_view4env, .set_view4online_obj_refs, .mapping_view4offline_obj_ref2Expression}
        (obj, /) -> Expression4Repr; to_expr4repr(obj, env, /) -> Expression4Repr

    expr2repr(Expression4Repr, env, stable_case, /) -> str4repr

    stable_case <- {
        repr__per_call#unstable-unordered
        , repr__per_runtime#stable-only-in-current-py-process-ordered-allow-using-addr-to-form-invalid-expr
        , repr__longterm_stable#ordered-valid-expr-not-allow-using-addr
        }
    #''')


Expression4Repr-list-seq:
    expr.may_addr
    constraints:
        ordered vs unordered vs partial_ordered#DAG
        fixed-group-position: 内部位置可以调换 以 满足 偏序关系，群与群 之间 不能 调换；但 整群 可能 对调，若声明允许的话。
    (a, ...)
    [a, ...]
        ordered_list/tuple/set/dict
        unordered_list/tuple/set/dict
        eg. PermanentKeyRefDict([(k,v), ...]) using unordered_list
            => Var(PermanentKeyRefDict)(unordered_list(ordered_tuple(k, v), ...))
    {a, ...}
    {k:v, ...} #non_expr__item
    d[a, b:c:d, ...] #non_expr__slice
    f(a,  ..., k=w, ...) #non_expr__kwarg
    #expr.__call__/__getattribute__/__getitem__/... #non_expr donot has op
    ---bin op
    #expr.__add__/... #non_expr donot has op
    a + b + ...
    a * b * ...
    x  - a - b ...
    x  / a / b ...
    ??? x  % a % b ...
class X:
    def 
def stable_repr4export_long_term_storage


#]]]Expression4Repr:end

#[[[ExpressionSnippet4Repr:begin
#eg. comma-separated-list, dict-item, slice-as-key, kwargs-assignment...
#   ??? *args, **kwargs
#   ??? ... for ... in ... if ... for ... in ... if ...
#]]]ExpressionSnippet4Repr:end

#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    from seed.hierarchy.plugin_api4register.stable_repr4export_long_term_storage import *
    from seed.hierarchy.plugin_api4register.stable_repr4export_long_term_storage import ...
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


