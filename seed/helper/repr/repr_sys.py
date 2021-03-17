
r'''
seed.helper.repr_sys

see:
    seed.io.savefile.SaveFile
see:
    seed.helper.repr_sys
    seed.helper.repr_input
    seed.helper.stable_repr
    seed.text.escape_as_c_string
    seed.text.raw_text2html_content
    seed.text.repr_string_as_unicode


=====
repr sys:
    obj filter ordered+not filter+sink filter(once enter, noreturn or not test follows):
      is obj
      eq obj # type==
      in objs #tuple/set, type==
      cls==
      cls<=
      cls<
      #ducktype/protocol/interface/abc
      hasattr:
        hasattr.obj
        hasattr.cls
      getattr&call
        getattr.obj
        getattr.cls
      allow test
    =====
    call:
      <?>(.x, y=, *zs, .u, v= **kw)
      ([(x, may_repr)], [(y, may_repr, default)], ..., may (repr, repr))
    literal
    std type
      ()
      []
      {/}
      {:}
    ref __main__.default
    ref other src
s

#'''







from seed.types.Tester import is_good, ITester
from seed.types.Tester import
from seed.types.FrozenDict import FrozenDict
from seed.tiny import is_iterator, is_reiterable
from collections.abc import Sequence, Mapping
from collections import namedtuple



from seed.abc.IReprImmutableHelper import IReprImmutableHelper
from seed.abc.abc import ABC, abstractmethod, override


from seed.types.SinkTester import SinkTester


r'''
case_handler
case_unboxer
case_tester = ITester | SinkTester
unarged_suite_handler = (input_py_obj_params, input_arged_ref_params, import_unarged_refs, ordered_case_tester_case_unboxer_case_handler_triples)
    :: ({py_obj_param}, {arged_ref_param}, {unarged_ref}, [(case_tester, case_unboxer, case_handler)])
arged_suite_handler = (unarged_suite_handler, param2py_obj_arg, param2arged_suite_handler, override_import2unarged_ref) | tuple<arged_suite_handler>
main_suite_handler <: arged_suite_handler
main_suite_handler = default_arged_suite_handler

param <: name <: str
unarged_ref <: name
not (arged_ref <: name)

arged_ref :: input_arged_ref_param | (import_unarged_ref, py_objs, arged_refs, override_import2unarged_ref).| ''/None(main) | tuple<arged_ref>
overrided_arged_ref :: (outmost_unarged_ref, py_objs, overrided_arged_refs, override_import2outmost_unarged_ref).| ''/None(main) | tuple<overrided_arged_ref>
def unarged_ref<py_obj_param...>(arged_ref_param...){override_import...}
    ==>> (param2py_obj_arg, param2arged_suite_handler, override_import2unarged_ref)
    ==>> arged_suite_handler
    ==>> {unarged_ref:unarged_suite_handler}
    ==>> repr_sys(tree_config, main_suite_handler, unarged_ref2unarged_suite_handler)
    ==>> repr(obj, arged_ref(?+bg?)/overrided_arged_ref/arged_suite_handler, subtree_config, main_suite_handler, unarged_ref2unarged_suite_handler)

case_handler<arg...>(obj_st, subtree_config) -> iter record

xxx record = (str | sep | space | newline | indents | (arged_ref, obj, subtree_config) | (open, close, arged_ref/arged_refs, objs/objss, subtree_config))
record = (str | spaces0_sep_spaces0 | indent_block(records) | (obj, arged_ref?/overrided_arged_ref, subtree_config))
case_tester:ReprCaseTester = (SinkTester | ITester)
case_unboxer::ReprCaseUnboxer = obj -> state
case_handler::ReprCaseHandler = state -> subtree_config -> iter IReprRecord
ReprTreeConfig = mapping#FrozenDict
#'''


class ReprSystem:
    def __init__(sf, tree_config, default_arged_suite_handler, unarged_ref2unarged_suite_handler):
        if not is_arged_suite_handler(default_arged_suite_handler): raise TypeError
        if not isinstance(unarged_ref2unarged_suite_handler, Mapping): raise TypeError
        if not all(map(is_unarged_ref, unarged_ref2unarged_suite_handler)): raise TypeError
        if not all(map(is_unarged_suite_handler, unarged_ref2unarged_suite_handler.values())): raise TypeError
        sf.__main = default_arged_suite_handler
        sf.__vars = unarged_ref2unarged_suite_handler
        sf.__cfg = tree_config

    xxx overrided_arged_ref def repr(sf, obj, arged_ref, subtree_config):
        if is_tuple(arged_ref):
            if not (is_tuple(obj) and is_seq_sz(len(arged_ref), obj)): raise TypeError
            objs, arged_refs = obj, arged_refs
            yield from sf._on_tuple(objs, arged_refs, subtree_config)
        elif not arged_ref:
            if not (arged_ref is None or is_str(arged_ref)): raise TypeError
            arged_suite_handler = sf.__main
            yield from sf._on_arged_suite_handler(obj, arged_suite_handler, subtree_config)
        elif is_str(arged_ref):
            if not is_param(arged_ref): raise TypeError
            input_arged_ref_param = arged_ref
            raise logic-err---input-var--escaped-scope
        elif isinstance(arged_ref, ArgedImportUnargedRef):
            arged_import_unarged_ref = arged_ref
            yield from sf._on_ArgedImportUnargedRef(obj, arged_import_unarged_ref, subtree_config)
        else:
            raise logic-err

    def _on_tuple(sf, objs, arged_refs, subtree_config):
        yield ReprRecord__spaces0_sep_spaces0('(')

        yield ReprRecord__indented_tuple(objs, arged_refs, subtree_config)
        if len(objs) == 1:
            yield ReprRecord__spaces0_sep_spaces0(',')
        yield ReprRecord__spaces0_sep_spaces0(')')

    def _on_arged_suite_handler(sf, obj, arged_suite_handler, subtree_config):
        (unarged_suite_handler, param2py_obj_arg, param2arged_suite_handler, override_import2unarged_ref) | tuple<arged_suite_handler> = arged_suite_handler
        TODO...
    def repr__arged_ref(sf, obj, arged_ref, subtree_config, background__param2arged_suite_handler, background__override_import2unarged_ref):
        arged_suite_handler = sf.arged_ref_to_arged_suite_handler(arged_ref, background__param2arged_suite_handler, background__override_import2unarged_ref)
        return sf.repr__arged_suite_handler(obj, arged_suite_handler, subtree_config)
    def repr__arged_suite_handler(sf, obj, arged_suite_handler, subtree_config):
        'arged_suite_handler = (unarged_suite_handler, param2py_obj_arg, param2arged_suite_handler, override_import2unarged_ref) | tuple<arged_suite_handler>'
        if len(arged_suite_handler) == 4 and not is_tuple(arged_suite_handler[-1]):
            (unarged_suite_handler, param2py_obj_arg, param2arged_suite_handler, override_import2unarged_ref) = arged_suite_handler
            TODO...
        elif all(is_tuple, arged_suite_handler):
            # tuple<arged_suite_handler>'
            TODO...

    def arged_ref_to_arged_suite_handler(sf, arged_ref, background__param2arged_suite_handler, background__override_import2unarged_ref):
        'arged_ref -> arged_suite_handler'
        env = input_arged_ref_param2arged_suite_handler = background__param2arged_suite_handler
        def this_func(arged_ref):
            x = arged_ref
            if x is None:
                return sf.__main
            if is_str(x):
                if x == '':
                    return sf.__main
                else:
                #if is_param(x):
                    input_arged_ref_param = x
                    return env[input_arged_ref_param]
            'is arged import_unarged_ref'
            if isinstance(x, ArgedImportUnargedRef):
                arged_import_unarged_ref = x
                return sf.arged_import_unarged_ref_to_arged_suite_handler(arged_import_unarged_ref, background__param2arged_suite_handler, background__override_import2unarged_ref)
            if is_tuple(x):
                return tuple(map(this_func, x))
            if not is_arged_ref(arged_ref): raise.TypeError
            raise logic-err
        return this_func(arged_ref)

    def arged_import_unarged_ref_to_arged_suite_handler(sf, arged_import_unarged_ref, background__param2arged_suite_handler, background__override_import2unarged_ref):
        'ArgedImportUnargedRef -> arged_suite_handler'
        [ import_unarged_ref
        , py_objs
        , arged_refs
        , override_import2unarged_ref
        ] = arged_import_unarged_ref

        # bg! import_unarged_ref,arged_refs, override_import2unarged_ref
        def convert(import_unarged_ref):
            unarged_ref = background__override_import2unarged_ref.get(import_unarged_ref, import_unarged_ref)
            return unarged_ref

        import_unarged_ref =.convert(import_unarged_ref)
        override_import2unarged_ref = {k:convert(v) for k,v in override_import2unarged_ref.items()}
        #########################
        unarged_suite_handler = sf.__vars[import_unarged_ref]
        (input_py_obj_params, input_arged_ref_params, import_unarged_refs, ordered_case_tester_case_unboxer_case_handler_triples) = unarged_suite_handler

        if len(py_objs) != len(input_py_obj_params): raise TypeError
        if len(arged_refs) != len(input_arged_ref_params): raise TypeError
        if not set(override_import2unarged_ref) <= import_unarged_refs: raise TypeError

        def convert2(arged_ref):
            return sf.arged_ref_to_arged_suite_handler(arged_ref, background__param2arged_suite_handler, background__override_import2unarged_ref)
        param2py_obj_arg = dict(zip(input_py_obj_params, py_objs))
        param2arged_suite_handler = dict(zip(input_arged_ref_params, map(convert2, arged_refs)))
        arged_suite_handler = (unarged_suite_handler, param2py_obj_arg, param2arged_suite_handler, override_import2unarged_ref)
        return arged_suite_handler
    def _on_ArgedImportUnargedRef(sf, obj, arged_import_unarged_ref, subtree_config):
        unarged_suite_handler
        TODO...


ReprCaseTester = (SinkTester | ITester)
class IReprCaseHandler(ABC):
    @abstractmethod
    def obj_state2iter_repr_record(sf, st, subtree_config):
        '-> Iter IReprRecord'
class IReprRecord(IReprImmutableHelper):
    pass
class ReprRecord__str(IReprRecord):
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__s], {}
    def __init__(sf, s:str):
        if type(s) is not str: raise TypeError
        if not s: raise ValueError
        if s != s.strip(): raise ValueError
        sf.__s = s
class ReprRecord__spaces0_sep_spaces0(ReprRecord__str):
    pass
class IReprRecord__indented_records(IReprRecord):
    pass
    @abstractmethod
    def iter(sf):
        '-> Iter IReprRecord'
    r'''
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__s], {}
    def __init__(sf, records:'Iter IReprRecord'):
        if 1:
            if not is_reiterable(records): raise TypeError
        elif 0:
            if not is_iterator(records): raise TypeError
        else:
            records = tuple(records)
            if not all(isinstance(x, IReprRecord) for x in records): raise TypeError
        sf.__s = records
    #'''

class ReprRecord__recur(IReprRecord):
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__obj, sf.__arged_ref, sf.__subtree_config], {}
    def __init__(sf, obj, arged_ref, subtree_config):
        if not is_arged_ref(arged_ref): raise TypeError
        sf.__obj = obj
        sf.__arged_ref = arged_ref
        sf.__subtree_config = subtree_config

class _Head_Tail_iters:
    def __init__(sf, head_iter, tail_iter):
        assert is_reiterable(head_iter)
        assert is_reiterable(tail_iter)
        sf.__head_iter = head_iter
        sf.__tail_iter = tail_iter
        sf.__start = True
    def __iter__(sf):
        if sf.__start:
            sf.__start = False
            return iter(sf.__head_iter)
        else:
            return iter(sf.__tail_iter)
class _Head_Tail_iters__comma(_Head_Tail_iters):
    comma = ReprRecord__spaces0_sep_spaces0(',')
    head_iter = ()
    tail_iter = (comma,)
    def __init__(sf):
        cls = sf
        super().__init__(cls.head_iter, cls.tail_iter)

class ReprRecord__indented_tuple(IReprRecord__indented_records):
    'without "()"; take care on len==1 without ","'
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__objs, sf.__arged_refs, sf.__subtree_config], {}
    def __init__(sf, objs, arged_refs, subtree_config):
        if not is_seq_of(is_arged_ref, arged_refs): raise TypeError
        if not is_seq_sz(len(arged_refs), objs): raise TypeError
        sf.__objs = objs
        sf.__arged_refs = arged_refs
        sf.__subtree_config = subtree_config

    @override
    def iter(sf):
        '-> Iter IReprRecord'
        may_sep = _Head_Tail_iters__comma()
        for obj, arged_ref in zip(sf.__objs, sf.__arged_refs):
            yield from may_sep
            yield ReprRecord__recur(obj, arged_ref, sf.__subtree_config)

class ReprRecord__indented_list(IReprRecord__indented_records):
    'without "()","[]","{}"; take care on set(), ie {} is dict not set; take care on len==1 without ","; ordered!'
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__ordered_objs, sf.__arged_ref, sf.__subtree_config], {}
    def __init__(sf, ordered_objs, arged_ref, subtree_config):
        if not is_arged_ref(arged_ref): raise TypeError
        if not is_reiterable(ordered_objs): raise TypeError
        sf.__ordered_objs = ordered_objs
        sf.__arged_ref = arged_ref
        sf.__subtree_config = subtree_config

    @override
    def iter(sf):
        '-> Iter IReprRecord'
        may_sep = _Head_Tail_iters__comma()
        for obj in sf.__ordered_objs:
            yield from may_sep
            yield ReprRecord__recur(obj, sf.__arged_ref, sf.__subtree_config)


class ReprRecord__indented_dict(IReprRecord__indented_records):
    'without "{}"; ordered!'
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__ordered_items, sf.__arged_ref4key, sf.__arged_ref4val, sf.__subtree_config], {}
    def __init__(sf, ordered_items, arged_ref4key, arged_ref4val, subtree_config):
        if not is_arged_ref(arged_ref4key): raise TypeError
        if not is_arged_ref(arged_ref4val): raise TypeError
        if not is_seq_of_seq_sz(2, ordered_items): raise TypeError
        sf.__ordered_items = ordered_items
        sf.__arged_ref4key = arged_ref4key
        sf.__arged_ref4val = arged_ref4val
        sf.__subtree_config = subtree_config

    @override
    def iter(sf):
        '-> Iter IReprRecord'
        arged_ref4key = sf.__arged_ref4key
        arged_ref4val = sf.__arged_ref4val
        subtree_config = sf.__subtree_config

        may_sep = _Head_Tail_iters__comma()
        sc = ReprRecord__spaces0_sep_spaces0(':')
        def _key_val(k, v):
            yield from may_sep
            yield ReprRecord__recur(k, arged_ref4key)
            yield sc
            yield ReprRecord__recur(v, arged_ref4val)


        for k, v in sf.__ordered_items:
            yield from _key_val(k, v)


class ReprRecord__indented_func_signature(IReprRecord__indented_records):
    'without "()"'
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__arged_signature, sf.__signature_config], {}
    def __init__(sf, arged_signature, signature_config):
        check_ArgedFuncSignature4ReprRecord(arged_signature)
        check_FuncSignatureConfig4ReprRecord(signature_config)
        sf.__arged_signature = arged_signature
        sf.__signature_config = signature_config

        ###############
        [args, kwargs] = sf.__arged_signature
        [ positional_param_arged_refs
        , positional_param_default_arged_ref_pairs
        , may_packed_positional_params_arged_ref
        , keyword_param_arged_ref_pairs
        , keyword_param_default_arged_ref_triples
        , may_packed_keyword_params_arged_ref
        ] = sf.__signature_config

        if not len(positional_param_arged_refs) <= len(args): raise TypeError
        if not (may_packed_positional_params_arged_ref or len(args) <= len(positional_param_arged_refs)+len(positional_param_default_arged_ref_pairs)): raise TypeError
        if not set(map(fst, keyword_param_arged_ref_pairs)) <= set(kwargs): raise TypeError
        if not (may_packed_keyword_params_arged_ref or set(kwargs) <= set(map(fst, keyword_param_arged_ref_pairs)) | set(map(fst, keyword_param_default_arged_ref_triples))): raise TypeError

    @override
    def iter(sf):
        '-> Iter IReprRecord'
        [args, kwargs] = sf.__arged_signature
        [ positional_param_arged_refs
        , positional_param_default_arged_ref_pairs
        , may_packed_positional_params_arged_ref
        , keyword_param_arged_ref_pairs
        , keyword_param_default_arged_ref_triples
        , may_packed_keyword_params_arged_ref
        ] = sf.__signature_config

        na = len(positional_param_arged_refs)
        nb = len(positional_param_default_arged_ref_pairs)
        nc = len(may_packed_positional_params_arged_ref)
        nd = len(args)

        ka = set(map(fst, keyword_param_arged_ref_pairs))
        kb = set(map(fst, keyword_param_default_arged_ref_triples))
        nkc = len(may_packed_keyword_params_arged_ref)
        kd = set(kwargs)

        assert na <= nd <= (nd if nc else na+nb)
        assert ka <= kd <= (kd if nkc else ka|kb)

        subtree_config = sf.__subtree_config
        may_sep = _Head_Tail_iters__comma()
        eq = ReprRecord__spaces0_sep_spaces0('=')
        def _val(obj, arged_ref):
            yield from may_sep
            yield ReprRecord__recur(obj, arged_ref, subtree_config)

        def _kw_df_val(kw_param, default, arged_ref):
            obj = kwargs[kw_param]
            if default != obj:
                yield from _kw_val(kw_param, arged_ref)

        def _kw_val(kw_param, arged_ref):
            obj = kwargs[kw_param]
            yield from may_sep
            yield ReprRecord__str(kw_param)
            yield eq
            yield ReprRecord__recur(obj, arged_ref, subtree_config)

        for obj, arged_ref in zip(args, positional_param_arged_refs):
            yield from _val(obj, arged_ref)

        mids = args[na:na+nb]
        L = len(mids)
        pairs = positional_param_default_arged_ref_pairs
        if nd <= na+nb:
            for i in reversed(range(L)):
                if pairs[i][0] != mids[i]:
                    break
            else:
                i = -1
            i += 1
        else:
            assert L == nb
            assert nc
            i = L
        pairs = pairs[:i]
        for obj, (default, arged_ref) in zip(mids, pairs):
            yield from _val(obj, arged_ref)

        if not nd <= na+nb:
            [arged_ref] = may_packed_positional_params_arged_ref
            for obj in args[na+nb:]:
                yield from _val(obj, arged_ref)




        for kw_param, arged_ref in keyword_param_arged_ref_pairs:
            yield from _kw_val(kw_param, arged_ref)
        for kw_param, default, arged_ref in keyword_param_default_arged_ref_triples:
            yield from _kw_df_val(kw_param, default, arged_ref)
        if may_packed_keyword_params_arged_ref:
            [arged_ref] = may_packed_keyword_params_arged_ref
            ks = kd - ka - kb
            for kw_param in sorted(ks):
                yield from _kw_val(kw_param, arged_ref)


        return



FuncSignatureConfig4ReprRecord = namedtuple('FuncSignatureConfig4ReprRecord', r'''
        , positional_param_arged_refs
        , positional_param_default_arged_ref_pairs
        , may_packed_positional_params_arged_ref
        , keyword_param_arged_ref_pairs
        , keyword_param_default_arged_ref_triples
        , may_packed_keyword_params_arged_ref
        #'''.translate(dict(zip(',#', '  '))).split())

ArgedFuncSignature4ReprRecord = namedtuple('ArgedFuncSignature4ReprRecord', r'''
        , args
        , kwargs
        #'''.translate(dict(zip(',#', '  '))).split())
_ArgedImportUnargedRef = namedtuple('_ArgedImportUnargedRef', r'''
    , import_unarged_ref
    , py_objs
    , arged_refs
    , override_import2unarged_ref
        #'''.translate(dict(zip(',#', '  '))).split())
class ArgedImportUnargedRef(_ArgedImportUnargedRef):
    r'''
    , import_unarged_ref
        # unconverted, innermost unarged_ref
    , py_objs
    , arged_refs
        # unconverted, innermost unarged_ref
    , override_import2unarged_ref
        # values: unconverted, innermost unarged_ref
    #'''
    def __init__(sf, import_unarged_ref, py_objs, arged_refs, override_import2unarged_ref):
        super().__init__(import_unarged_ref, py_objs, arged_refs, override_import2unarged_ref)
        check_ArgedImportUnargedRef(sf)

def check_ArgedImportUnargedRef(arged_import_unarged_ref):
    if not isinstance(arged_import_unarged_ref, ArgedImportUnargedRef): raise TypeError
    [ import_unarged_ref
    , py_objs
    , arged_refs
    , override_import2unarged_ref
    ] = arged_import_unarged_ref
    if not is_unarged_ref(import_unarged_ref): raise TypeError
    if not is_seq(py_objs): raise TypeError
    if not is_seq_of(is_arged_ref, arged_refs): raise TypeError
    if not isinstance(override_import2unarged_ref, Mapping): raise TypeError
    if not all(map(is_unarged_ref, override_import2unarged_ref)): raise TypeError
    if not all(map(is_unarged_ref, override_import2unarged_ref.values())): raise TypeError

def check_ArgedFuncSignature4ReprRecord(arged_signature):
    if not isinstance(arged_signature, ArgedFuncSignature4ReprRecord): raise TypeError
    [args, kwargs] = arged_signature
    #may_func_name, args, kwargs
    #if not (may_func_name is None or type(may_func_name) is str): raise TypeError
    if not isinstance(args, Sequence): raise TypeError
    if not isinstance(kwargs, Mapping): raise TypeError


def is_may_arged_ref(x):
    return is_tuple(x) and (not x or is_seq_of_seq([is_arged_ref], x))
def is_arged_ref(x):
    'arged_ref :: input_arged_ref_param | (import_unarged_ref, py_objs, arged_refs, override_import2unarged_ref).| ''/None(main) | tuple<arged_ref>'
    def this_func(x):
        if x is None: return True
        if is_str(x):
            'is main'
            'is input_arged_ref_param'
            return x == '' or is_param(x)
        'is arged import_unarged_ref'
        if isinstance(x, ArgedImportUnargedRef):
            return True
        return is_tuple(x) and all(map(this_func, x))
    return this_func(x)

def is_unarged_ref(x):
    return is_param(x)
def is_unarged_suite_handler(x):
    'unarged_suite_handler = (input_py_obj_params, input_arged_ref_params, import_unarged_refs, ordered_case_tester_case_unboxer_case_handler_triples)'
    TODO...
def is_arged_suite_handler(x):
    'arged_suite_handler = (unarged_suite_handler, param2py_obj_arg, param2arged_suite_handler, override_import2unarged_ref) | tuple<arged_suite_handler>'
    TODO...

def is_obj(x):
    return True
def is_param(x):
    return is_str(x) and x.isidentifier()
def is_str(x):
    return type(x) is str
def is_tuple(x):
    return type(x) is tuple

def is_seq(x):
    return isinstance(x, Sequence)
def is_seq_sz(sz, x):
    return is_seq(x) and len(x) == sz
def is_seq_of_seq_sz(sz, x):
    return is_seq(x) and all(is_seq_sz(sz, y) for y in x)
def is_seq_of_seq(verifiers, x):
    assert is_seq(verifiers)
    sz = len(verifiers)
    return is_seq_of_seq_sz(sz, x) and all(all(f(z) for f, z in zip(verifiers, y)) for y in x)
def is_seq_of(verifier, x):
    return is_seq(x) and all(map(verifier, x))

def check_FuncSignatureConfig4ReprRecord(signature_config):
    if not isinstance(signature_config, FuncSignatureConfig4ReprRecord): raise TypeError
    [ positional_param_arged_refs
    , positional_param_default_arged_ref_pairs
    , may_packed_positional_params_arged_ref
    , keyword_param_arged_ref_pairs
    , keyword_param_default_arged_ref_triples
    , may_packed_keyword_params_arged_ref
    ] = signature_config

    if not is_seq_of(is_arged_ref, positional_param_arged_refs): raise TypeError
    if not is_seq_of_seq([is_obj, is_arged_ref], positional_param_default_arged_ref_pairs): raise TypeError
    if not is_may_arged_ref(may_packed_positional_params_arged_ref): raise TypeError

    if not is_seq_of_seq([is_param, is_arged_ref], keyword_param_arged_ref_pairs): raise TypeError
    if not is_seq_of_seq([is_param, is_obj, is_arged_ref], keyword_param_default_arged_ref_triples): raise TypeError
    if not is_may_arged_ref(may_packed_keyword_params_arged_ref): raise TypeError













====================================
====================================
====================================
====================================
====================================


class IReprRecord(IReprImmutableHelper):
    @abstractmethod
    #def virtual_repr(sf, num_indents, subtree_config, main_suite_handler, param2suite_handler):
    def virtual_repr(sf, num_indents, repr_sys:ReprSystem):
        '-> Iter (str | IReprRecord | IReprControl)'
#ReprCaseHandler = obj -> IReprRecord
class IReprRecord__func_signature(IReprRecord):
    @abstractmethod
    def get_signature_args_kwargs(sf):
        '-> (args, kwargs)'
    @abstractmethod
    def get_may_suite_handler_ref4signature_param(sf, obj):
        r'''obj -> mapping{
        , positional_param_suite_handler_refs
        , positional_param_default_suite_handler_ref_pairs
        , packed_positional_params_suite_handler_ref
        , keyword_param_suite_handler_ref_pairs
        , keyword_param_default_suite_handler_ref_triples
        , packed_keyword_params_suite_handler_ref
        }
        #'''
    def _virtual_repr(sf, *
        , args, kwargs
        , positional_param_suite_handler_refs
        , positional_param_default_suite_handler_ref_pairs
        , packed_positional_params_suite_handler_ref
        , keyword_param_suite_handler_ref_pairs
        , keyword_param_default_suite_handler_ref_triples
        , packed_keyword_params_suite_handler_ref
        ):
        '(x:X..., y:Y=y0..., *zs:Z, u:U..., v:V=v0..., **w:W)'
        ::::
    @override
    def virtual_repr(sf, num_indents, repr_sys:ReprSystem):
        '-> Iter (str | IReprRecord | IReprControl)'
        args, kwargs = sf.get_signature_args_kwargs()
        d = sf.get_may_suite_handler_ref4signature_param()
        return sf._virtual_repr(args=args, kwargs=kwargs, **d)











class IReprControl(IReprImmutableHelper):
    pass
class _ReprControl__no_args(IReprControl):
    @override
    def ___get_args_kwargs___(sf):
        return [], {}
class Newline(_ReprControl__no_args):
    pass
class MaybeSpace(_ReprControl__no_args):
    pass
class Space(_ReprControl__no_args):
    pass
class NewlineAutoIndent(_ReprControl__no_args):
    pass
class NewlineAutoDedent(_ReprControl__no_args):
    pass
class NewlineIndents(IReprControl):
    def __init__(sf, num_indents):
        num_indents = int(num_indents)
        if num_indents < 0: raise ValueError
        sf.__num_indents = num_indents
    @property
    def num_indents(sf):
        return sf.__num_indents
    @override
    def ___get_args_kwargs___(sf):
        return [sf.num_indents], {}

class ReprSystem:
    def __init__(sf, tree_config, __no_argsmain_suite_handler, param2suite_handler):
        sf._tree_config = FrozenDict(tree_config)
        sf._main_suite_handler = tuple((case_tester, case_unboxer, case_handler) for case_tester, case_unboxer, case_handler in main_suite_handler)
        sf._param2suite_handler = FrozenDict(param2suite_handler)
    def 









