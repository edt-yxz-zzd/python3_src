#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''

e ../../python3_src/seed/helper/IConfig4load_versioned_repr_txt_file.py
used in:
    nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0
        view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__PropList_txt.py
        view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parsed_result__of__Unihan_Variants_txt__of_ver13_0.py



seed.helper.IConfig4load_versioned_repr_txt_file
py -m    seed.helper.IConfig4load_versioned_repr_txt_file
py -m nn_ns.app.debug_cmd   seed.helper.IConfig4load_versioned_repr_txt_file

from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file, Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer

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
    IConfig4load_versioned_repr_txt_file
    Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...

from pathlib import Path
import re

from seed.abc.abc__ver0 import ABC, abstractmethod, override
from copy import deepcopy
from ast import literal_eval
from seed.helper.safe_eval import safe_eval
from json import loads as json_load__str
#import json
from seed.helper.stable_repr import stable_repr
from seed.helper.stable_repr import stable_repr__expand_top_layer
from seed.tiny import echo
from seed.func_tools.fmapT.TypeBasedFMapT__literal_rebuild import literal_rebuild
from seed.types.view.RecurView import default_cfg4RecurView
from seed.tiny import dict_add__is
from seed.tiny import MapView, check_type_is, check_pair


from seed.helper.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt

___end_mark_of_excluded_global_names__0___ = ...


#HHHHH
#[[[main_body_src_code:begin
#IConfig4load_versioned_repr_txt_file:goto
#zzzwww:goto

#[[[IConfig4load_versioned_repr_txt_file:begin

_basename_fmt__rex = re.compile(r'^[^?*{}]*[{][}][^?*{}]*$')
class IConfig4load_versioned_repr_txt_file(ABC):
    #state2dataobj___create
    #state5dataobj___save
    def __init__(sf, /, *, __file__, data_dir_rpath, basename_fmt, version_str__rex, encoding, dataobj_immutable, state_immutable):#, state2dataobj___create=None, state5dataobj___save=None
        #, py_literal_vs_json
        #   removed, since json.dict.key MUST BE str!!!
        r'''now become ABC
        if state2dataobj___create is not None:
            sf.state2dataobj___create = state2dataobj___create
        if state5dataobj___save is not None:
            sf.state5dataobj___save = state5dataobj___save
        #'''
        sf.dataobj_immutable = dataobj_immutable
        sf.state_immutable = state_immutable
        sf.encoding = encoding
        sf.pkg_path = Path(__file__).parent.resolve()
        sf.data_dir_rpath = data_dir_rpath
        sf.data_dir_path = (sf.pkg_path / sf.data_dir_rpath).resolve()
        sf.basename_fmt = basename_fmt
        sf.version_str__rex = re.compile(version_str__rex) if type(version_str__rex) is str else version_str__rex
        #sf.py_literal_vs_json = bool(py_literal_vs_json)
        if not data_dir_rpath.startswith('./'): raise ValueError(f"data_dir_rpath={data_dir_rpath!r} not startswith './'")
        if None is _basename_fmt__rex.fullmatch(basename_fmt): raise ValueError(f'not basename_fmt={basename_fmt!r} <- {_basename_fmt__rex.patterna!r}=basename_fmt__rexgex_pattern')
        prefix, suffix = basename_fmt.split('{}')
        glob_pattern4basename = f'{prefix!s}*{suffix!s}'
        assert glob_pattern4basename == basename_fmt.format('*')
        sf.glob_pattern4basename = glob_pattern4basename
        sf.prefix, sf.suffix = prefix, suffix

        ######################cache
        sf._cache__ver2st = {}
        sf._cache__ver2readonly_dataobj = {}
        sf._cache__ver2immutable_dataobj = {}
        ######################view of cache
        sf._view__version_str2readonly_dataobj = MapView(sf._cache__ver2readonly_dataobj)
        if sf.dataobj_immutable:
            sf._view__version_str2immutable_dataobj = MapView(sf._cache__ver2immutable_dataobj)
        if sf.state_immutable:
            sf._view__version_str2immutable_state = MapView(sf._cache__ver2st)
    def get_view_of_cache__version_str2readonly_dataobj(sf, /):
        return sf._view__version_str2readonly_dataobj
    def get_view_of_cache__version_str2immutable_dataobj(sf, /):
        if not sf.dataobj_immutable: raise TypeError
        return sf._view__version_str2immutable_dataobj
    def get_view_of_cache__version_str2immutable_state(sf, /):
        if not sf.state_immutable: raise TypeError
        return sf._view__version_str2immutable_state





    def verify_version_str(sf, version_str, /):
        if '\\' in version_str or '/' in version_str: return False
        m = sf.version_str__rex.fullmatch(version_str)
        return m is not None
    def version_str2data_file_path(sf, version_str, /, *, may_path_bypass_version_str=None):
        if not sf.verify_version_str(version_str): raise ValueError
        basename = sf.basename_fmt.format(version_str)
        path = sf.data_dir_path / basename
        if may_path_bypass_version_str is not None:
            path = may_path_bypass_version_str
            path = Path(path)
        return path
    def findout_available_version_strs(sf, /):
        #def findout_supported_versions(sf, /):
        '-> [version_str]'
        #path.iterdir() -> Iter path #not (Iter basename)
        #path.glob() -> [path] #not [basename]
        prefix, suffix = sf.prefix, sf.suffix
        len_prefix, len_suffix = len(prefix), len(suffix)
        paths = sf.data_dir_path.glob(sf.glob_pattern4basename)
        version_strs = []
        for path in paths:
            basename = path.name
            L = len(basename)
            assert L >= len_prefix + len_suffix
            assert basename.startswith(prefix)
            assert basename.endswith(suffix)
            middle = basename[len_prefix:L-len_suffix]
            if not basename == f'{prefix!s}{middle!s}{suffix!s}': raise logic-err
            if sf.verify_version_str(middle):
                version_str = middle
                if not path.resolve() == sf.version_str2data_file_path(version_str).resolve(): raise logic-err
                version_strs.append(version_str)
        version_strs.sort()
        return version_strs


    def file2text___read__path(sf, path, /):
        #.file5text___write__path
        path = Path(path)
        txt = path.read_text(encoding=sf.encoding)
        return txt
    def text2state___eval(sf, txt, /):
        #.text5state___repr
        #
        #json.loads if sf.py_literal_vs_json else literal_eval
        st = literal_eval(txt)
        return st
        safe_eval
        literal_eval
        json_load__str
    @abstractmethod
    def state2dataobj___create(sf, st, /):
        #.state5dataobj___save
        #see: seed.func_tools.fmapT
        dataobj = st
        return dataobj
    def dataobj2readonly___recur_view(sf, dataobj, /):
        #.dataobj5readonly___literal_rebuild
        'dataobj -> readonly_dataobj'
        #result_readonly=True
        if sf.dataobj_immutable:
            readonly_dataobj = dataobj
        else:
            cfg4RecurView4dataobj = sf.get_cfg4RecurView4dataobj()
            readonly_dataobj = cfg4RecurView4dataobj.to_view(dataobj)
        return readonly_dataobj
        #if result_readonly: raise NotImplementedError
    def get_cfg4RecurView4dataobj(sf, /):
        return default_cfg4RecurView
    def dataobj5readonly___literal_rebuild(sf, readonly_dataobj, /):
        #.dataobj2readonly___recur_view
        'readonly_dataobj -> dataobj'
        #un verbose? un view?
        #neat naive clean rebuild simplified
        if sf.dataobj_immutable:
            dataobj = readonly_dataobj
        else:
            #from seed.func_tools.fmapT import literal_rebuild
            dataobj = literal_rebuild(readonly_dataobj)
        return dataobj

    @abstractmethod
    def state5dataobj___save(sf, dataobj, /):
        'can be overrided as: def state5dataobj___save(sf, dataobj, /, *args4dump, **kwargs4dump):'
        #.check_extra_input4dump
        #.state2dataobj___create
        #see: seed.func_tools.fmapT
        st = dataobj
        return st
    def text5state___repr(sf, st, /, *, maybe_max_depth4repr):
        'can be overrided as: def text5state___repr(sf, st, /, *args4repr, **kwargs4repr):'
        #.text2state___eval
        #.check_extra_input4repr
        txt = stable_repr(st, depth=0, maybe_max_depth=maybe_max_depth4repr)
        return txt
    def file5text___write__path(sf, path, txt, /, *, force):
        #.file2text___read__path
        path = Path(path)
        with open(path, 'wt' if force else 'xt', encoding=sf.encoding) as fout:
            #fout.write(txt)
            print(txt, file=fout) #++newline
        return
        if not force and path.exists(): raise FileExistsError
        path.write_text(txt, encoding=sf.encoding)
            # from py-doc: An existing file of the same name is overwritten.
        return


    def dump_data_file__ver(sf, version_str, dataobj, /, *, force, args4dump, kwargs4dump, args4repr, kwargs4repr, is_readonly_dataobj, may_path_bypass_version_str):
        #.load_data_file__ver
        'version_str -> dataobj -> None'
        args4dump = (*args4dump,)
        kwargs4dump = {**kwargs4dump}
        sf.check_extra_input4dump(*args4dump, **kwargs4dump)

        args4repr = (*args4repr,)
        kwargs4repr = {**kwargs4repr}
        sf.check_extra_input4repr(*args4repr, **kwargs4repr)

        path = sf.version_str2data_file_path(version_str)
            #check version_str!!!

        if is_readonly_dataobj:
            readonly_dataobj = dataobj
            dataobj = sf.dataobj5readonly___literal_rebuild(readonly_dataobj)

        st = sf.state5dataobj___save(dataobj, *args4dump, **kwargs4dump)
        sf.dump_state2data_file__ver(version_str, st, force=force, may_path_bypass_version_str=may_path_bypass_version_str, args4repr=args4repr, kwargs4repr=kwargs4repr)
    def dump_state2data_file__ver(sf, version_str, st, /, *, force, may_path_bypass_version_str, args4repr, kwargs4repr):
        'version_str -> st -> None'
        args4repr = (*args4repr,)
        kwargs4repr = {**kwargs4repr}
        sf.check_extra_input4repr(*args4repr, **kwargs4repr)

        path = sf.version_str2data_file_path(version_str, may_path_bypass_version_str=may_path_bypass_version_str)

        txt = sf.text5state___repr(st, *args4repr, **kwargs4repr)
        sf.file5text___write__path(path, txt, force=force)
        sf.drop_cache_at(version_str)

    @abstractmethod
    def check_extra_input4dump(sf, /):
        'can be overrided as: def check_extra_input4dump(sf, /, *args4dump, **kwargs4dump): #check len/keys #same as state5dataobj___save'
        #.state5dataobj___save
        pass
    def check_extra_input4repr(sf, /, *, maybe_max_depth4repr):
        'can be overrided as: def check_extra_input4repr(sf, /, *args4repr, **kwargs4repr): #check len/keys #same as text5state___repr'
        #.text5state___repr
        pass
    def drop_cache_at(sf, version_str, /):
        if version_str in sf._cache__ver2st:
            del sf._cache__ver2st[version_str]
        if version_str in sf._cache__ver2readonly_dataobj:
            del sf._cache__ver2readonly_dataobj[version_str]
        if version_str in sf._cache__ver2immutable_dataobj:
            del sf._cache__ver2immutable_dataobj[version_str]
    def load_data_file__ver(sf, version_str, /, *, deepcopy_on_cached_state, result_readonly, may_path_bypass_version_str):
        #.dump_data_file__ver
        'version_str -> dataobj'
        if result_readonly:
            if version_str in sf._cache__ver2readonly_dataobj:
                readonly_dataobj = sf._cache__ver2readonly_dataobj[version_str]
                return readonly_dataobj

        if sf.dataobj_immutable:
            if version_str in sf._cache__ver2immutable_dataobj:
                immutable_dataobj = sf._cache__ver2immutable_dataobj[version_str]
                return immutable_dataobj


        st = sf.load_state5data_file__ver(version_str, deepcopy_on_cached_state=deepcopy_on_cached_state and not result_readonly, may_path_bypass_version_str=may_path_bypass_version_str)
        dataobj = sf.state2dataobj___create(st)
        if result_readonly:
            readonly_dataobj = sf.dataobj2readonly___recur_view(dataobj)
            dict_add__is(sf._cache__ver2readonly_dataobj, version_str, readonly_dataobj)
            return readonly_dataobj
        elif sf.dataobj_immutable:
            immutable_dataobj = dataobj
            dict_add__is(sf._cache__ver2immutable_dataobj, version_str, immutable_dataobj)
            return immutable_dataobj
        else:
            return dataobj
    def load_state5data_file__ver(sf, version_str, /, *, deepcopy_on_cached_state, may_path_bypass_version_str):
        'version_str -> deepcopy(cached st)'
        def recur():
            if version_str in sf._cache__ver2st:
                st = sf._cache__ver2st[version_str]
                return st

            path = sf.version_str2data_file_path(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
            txt = sf.file2text___read__path(path)
            st = sf.text2state___eval(txt)
            dict_add__is(sf._cache__ver2st, version_str, st)
            return recur()
        f = echo if not deepcopy_on_cached_state or sf.state_immutable or sf.dataobj_immutable else deepcopy
        #return st
        return f(recur())
            #st may be mutable, SHOULD be hidden
            #st come from literal_eval
            #   but dataobj may contain instance of userdefined class

#]]]IConfig4load_versioned_repr_txt_file:end

#[[[Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer:begin
#[[[
r'''
copy from:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__Blocks_txt.py
#'''

class Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer(IConfig4load_versioned_repr_txt_file):
    r'''
    dataobj = (parsed_result, extra_derived_result, compact_result)
    st = compact_result
    ----:
    xxx ++kw: str_instead_repr
    ++kw: state_rawtxt
    xxx ++kw: override__text5state___repr
    ++kw: override__text52state

    #'''
    def __init__(sf, helper4parse__xxx_txt, /, *, __file__, data_dir_rpath, basename_fmt, version_str__rex, encoding, dataobj_immutable, state_immutable, override__text52state=None, state_rawtxt=False):#, str_instead_repr=False
        assert isinstance(helper4parse__xxx_txt, IHelper4parse__xxx_txt)
        if override__text52state is not None:
            check_pair(override__text52state)
            override__text5state___repr, override__text2state___eval = override__text52state
            if override__text5state___repr is not None:
                check_callable(override__text5state___repr)
            if override__text2state___eval is not None:
                check_callable(override__text2state___eval)

        if state_rawtxt and not state_immutable: raise TypeError('state is str, must be immutable')
        if state_rawtxt and not override__text52state is None: raise TypeError('state is final raw text, not convertion take-place')
        sf._helper4parse = helper4parse__xxx_txt
        #sf.str_instead_repr = str_instead_repr
        sf.state_rawtxt = state_rawtxt
        sf.override__text52state = override__text52state
        super().__init__(__file__=__file__, data_dir_rpath=data_dir_rpath, basename_fmt=basename_fmt, version_str__rex=version_str__rex, encoding=encoding, dataobj_immutable=dataobj_immutable, state_immutable=state_immutable)

    @override
    def state2dataobj___create(sf, st, /):
        #.state5dataobj___save
        #see: seed.func_tools.fmapT
        dataobj = sf._helper4parse.state2dataobj___create(st)
        return dataobj







    @override
    def state5dataobj___save(sf, dataobj, /):
        'can be overrided as: def state5dataobj___save(sf, dataobj, /, *args4dump, **kwargs4dump):'
        #.check_extra_input4dump
        #.state2dataobj___create
        #see: seed.func_tools.fmapT
        st = sf._helper4parse.state5dataobj___save(dataobj)
        return st
    @override
    def check_extra_input4dump(sf, /):
        'can be overrided as: def check_extra_input4dump(sf, /, *args4dump, **kwargs4dump): #check len/keys #same as state5dataobj___save'
        #.state5dataobj___save
        pass

    def dataobj2readonly___recur_view(sf, dataobj, /):
        #.dataobj5readonly___literal_rebuild
        'dataobj -> readonly_dataobj'
        #result_readonly=True
        return sf._helper4parse.dataobj2readonly(dataobj)
    def dataobj5readonly___literal_rebuild(sf, readonly_dataobj, /):
        #.dataobj2readonly___recur_view
        'readonly_dataobj -> dataobj'
        #un verbose? un view?
        #neat naive clean rebuild simplified
        return sf._helper4parse.dataobj5readonly(readonly_dataobj)


    def check_extra_input4repr(sf, /):
        'can be overrided as: def check_extra_input4repr(sf, /, *args4repr, **kwargs4repr): #check len/keys #same as text5state___repr'
        #.text5state___repr
        pass
    def text5state___repr(sf, st, /):
        'can be overrided as: def text5state___repr(sf, st, /, *args4repr, **kwargs4repr):'
        #.text2state___eval
        #.check_extra_input4repr
        if sf.state_rawtxt:
            txt = st
        elif None is sf.override__text52state:
            txt = stable_repr__expand_top_layer(st)
        else:
            override__text5state___repr, override__text2state___eval = sf.override__text52state
            txt = override__text5state___repr(st)
        check_type_is(str, txt)
        return txt
    def text2state___eval(sf, txt, /):
        #.text5state___repr
        #
        #json.loads if sf.py_literal_vs_json else literal_eval
        check_type_is(str, txt)
        if sf.state_rawtxt:
            st = txt
        elif None is sf.override__text52state:
            st = super().text2state___eval(txt)
        else:
            override__text5state___repr, override__text2state___eval = sf.override__text52state
            st = override__text2state___eval(txt)
        return st



#]]]

#]]]Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer:end
#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    from seed.helper.IConfig4load_versioned_repr_txt_file import *
    from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file, Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


