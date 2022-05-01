r'''
e ../../python3_src/nn_ns/CJK/cjk_subsets/囗共享汉字集单字信息.py

py -m nn_ns.app.debug_cmd   nn_ns.CJK.cjk_subsets.囗共享汉字集单字信息
from nn_ns.CJK.cjk_subsets.囗共享汉字集单字信息 import IConfig4load_subset_result_file4汉字到单字信息




copy from:
    e ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py
    .+1,$s/字形拆分树/单字信息/g

from nn_ns.CJK.cjk_subsets.共享汉字集单字信息 import 只读囗共享汉字到单字信息
py -m nn_ns.app.debug_cmd   nn_ns.CJK.cjk_subsets.共享汉字集单字信息

py -m nn_ns.CJK.cjk_subsets.共享汉字集xxx
    生成: ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集xxx.py.out.另档.cjk_common_subset_2513.汉字到xxx.txt
!du -h ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集xxx.py.out.另档.cjk_common_subset_2513.汉字到xxx.txt
    xxxK
view ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集xxx.py.out.另档.cjk_common_subset_2513.汉字到xxx.txt



#'''

__all__ = '''
    只读囗共享汉字到单字信息

    只读囗平凡繁简囗初步缩减囗共享汉字到单字信息
    只读囗初步缩减囗共享汉字到单字信息
    只读囗平凡繁简囗共享汉字到单字信息
    '''.split()

from seed.abc.abc__ver0 import override, abstractmethod
from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file
#from seed.tiny_.pprint4container__depth1 import pprint4container__depth1, show5pprint
from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
from seed.helper.stable_repr import stable_repr
from seed.tiny import MapView
from seed.func_tools.fmapT.fmapT__tiny import fmapT__dict#, dot

#[[[
#view ../../python3_src/seed/helper/IConfig4load_versioned_repr_txt_file.py
class IConfig4load_subset_result_file4汉字到单字信息(IConfig4load_versioned_repr_txt_file):
    r'''
    readonly_dataobj = MapView<hz2immutable_hz_info>
        #只读囗另档囗汉字到单字信息
        #MapView {hz:immutable_hz_info}
        #
    dataobj = hz2immutable_hz_info
        #另档囗汉字到单字信息
        #{hz:immutable_hz_info}
        #subset_result of 汉字到单字信息
        #
    st = hz2hz_info
        #{hz:hz_info}
        #为何st与dataobj不同？主要是满足:
            def _mk4dump_by_name():
                if not {**只读囗另档囗汉字到单字信息} == 另档囗汉字到单字信息: raise logic-err
            ######################
            其中，
                * st 是 字面值/literal，主要是好看/好区分，比如：
                    tree::tuple<(case, (...|children))>
                    children::list<tree>
                    ==>> st::value 可能 mutable
                    ==>> st = hz2hz_info
                * dataobj=『另档囗汉字到单字信息』
                    readonly_dataobj=『只读囗另档囗汉字到单字信息』=MapView<dataobj>
                    由上面的『if not...raise』==>>dataobj::value 必须 immutable
                    ==>> dataobj = hz2immutable_hz_info

    ----:
    sf.dataobj_immutable = False
    sf.state_immutable = False

    ----:
    sf.hz_info_immutable = ???
    #'''
    def __init__(sf, /, *, __file__, data_dir_rpath, basename_fmt, version_str__rex, encoding, hz_info_immutable):
        dataobj_immutable = False
        state_immutable = False
        sf.hz_info_immutable = hz_info_immutable
        super().__init__(__file__=__file__, data_dir_rpath=data_dir_rpath, basename_fmt=basename_fmt, version_str__rex=version_str__rex, encoding=encoding, dataobj_immutable=dataobj_immutable, state_immutable=state_immutable)
    @abstractmethod
    def _slow_load_full_hz2xxx_hz_info_(sf, /):
        '-> (xxx_hz_info_immutable, full_hz2xxx_hz_info)'

    #@abstractmethod
    def hz_info2immutable(sf, hz_info, /):
        if sf.hz_info_immutable:
            immutable_hz_info = hz_info
        else:
            raise NotImplementedError
        return immutable_hz_info
    #@abstractmethod
    def hz_info5immutable(sf, immutable_hz_info, /):
        if sf.hz_info_immutable:
            hz_info = immutable_hz_info
        else:
            raise NotImplementedError
        return hz_info

    @override
    def state2dataobj___create(sf, st, /):
        #.state5dataobj___save
        hz2hz_info = st
        if sf.hz_info_immutable:
            hz2immutable_hz_info = hz2hz_info
        else:
            hz2immutable_hz_info = fmapT__dict(sf.hz_info2immutable)(hz2hz_info)
        dataobj = hz2immutable_hz_info
        return dataobj

    @override
    def check_extra_input4dump(sf, /):
        'can be overrided as: def check_extra_input4dump(sf, /, *args4dump, **kwargs4dump): #check len/keys #same as state5dataobj___save'
        #.state5dataobj___save
        pass

    @override
    def state5dataobj___save(sf, dataobj, /):
        'can be overrided as: def state5dataobj___save(sf, dataobj, /, *args4dump, **kwargs4dump):'
        #.check_extra_input4dump
        #.state2dataobj___create
        hz2immutable_hz_info = dataobj
        if sf.hz_info_immutable:
            hz2hz_info = hz2immutable_hz_info
        else:
            hz2hz_info = fmapT__dict(sf.hz_info5immutable)(hz2immutable_hz_info)
        st = hz2hz_info
        return st




    @override
    def text5state___repr(sf, st, /):
        'can be overrided as: def text5state___repr(sf, st, /, *args4repr, **kwargs4repr):'
        #.text2state___eval
        #.check_extra_input4repr

        hz2hz_info = st
        #txt = show5pprint('fout', pprint4container__depth1, hz2hz_info)
        txt = stable_repr__expand_top_layer(hz2hz_info)
        return txt
    @override
    def check_extra_input4repr(sf, /):
        'can be overrided as: def check_extra_input4repr(sf, /, *args4repr, **kwargs4repr): #check len/keys #same as text5state___repr'
        #.text5state___repr
        pass



    @override#to avoid RecurView
    def dataobj2readonly___recur_view(sf, dataobj, /):
        #.dataobj5readonly___literal_rebuild
        'dataobj -> readonly_dataobj'
        #result_readonly=True
        hz2immutable_hz_info = dataobj
        readonly__hz2immutable_hz_info = MapView(hz2immutable_hz_info)
        readonly_dataobj = readonly__hz2immutable_hz_info
        return readonly_dataobj

    def dataobj5readonly___literal_rebuild(sf, readonly_dataobj, /):
        #.dataobj2readonly___recur_view
        'readonly_dataobj -> dataobj'
        readonly__hz2immutable_hz_info = readonly_dataobj
        hz2immutable_hz_info = {**readonly__hz2immutable_hz_info}
        dataobj = hz2immutable_hz_info
        return dataobj




    def _mk4dump_by_name(sf, /):
        #另档 的 目的 在于『避免过于耗时的加载_slow_load_full_hz2xxx_hz_info_』
        #   因此，只有 _main4dump()使用 _mk4dump_by_name()
        #
        from seed.mapping_tools.dict_op import subset_keys__immutable
        import nn_ns.CJK.cjk_subsets.hanzi as hanzi_lib
        from nn_ns.CJK.cjk_subsets.hanzi import hz_sp_str2hz_set
        (xxx_hz_info_immutable, full_hz2xxx_hz_info) = sf._slow_load_full_hz2xxx_hz_info_()
        汉字到单字信息 = full_hz2xxx_hz_info
            #xxx_hz_info_immutable? readonly__hz2hz_info : hz2hz_info
        ######################
        def _gen(hz_sp_str, /):
            hz_set = hz_sp_str2hz_set(hz_sp_str)
            另档囗汉字到单字信息 = subset_keys__immutable(汉字到单字信息, hz_set)
            return 另档囗汉字到单字信息
        ######################
        def _gen_by_name(汉字字集名, /):
            if not 汉字字集名 in hanzi_lib.__all__:raise ValueError(汉字字集名)
            带空格汉字字集 = getattr(hanzi_lib, 汉字字集名)
            if not type(带空格汉字字集) is str: raise TypeError(汉字字集名)

            另档囗汉字到单字信息 = _gen(带空格汉字字集)
            return 另档囗汉字到单字信息
        def _dump_by_name(汉字字集名, /, force, may_path_bypass_version_str):
            #force=False, may_path_bypass_version_str=None
            另档囗汉字到单字信息 = _gen_by_name(汉字字集名)
            if not xxx_hz_info_immutable:
                hz2hz_info = 另档囗汉字到单字信息
                st = hz2hz_info
                dataobj = sf.state2dataobj___create(st)
            else:
                hz2immutable_hz_info = 另档囗汉字到单字信息
                dataobj = hz2immutable_hz_info
            dataobj

            version_str = 汉字字集名
            sf.dump_data_file__ver(version_str, dataobj, force=force, args4repr=[], kwargs4repr={}, args4dump=[], kwargs4dump={}, is_readonly_dataobj=False, may_path_bypass_version_str=may_path_bypass_version_str)
            readonly_dataobj = sf.load_readonly_by_name(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
            readonly__hz2immutable_hz_info = readonly_dataobj
            只读囗另档囗汉字到单字信息 = readonly__hz2immutable_hz_info

            try:
                if not {**只读囗另档囗汉字到单字信息} == 另档囗汉字到单字信息: raise logic-err
            except:
                def f(hz2hz_info, /):
                    print(len(hz2hz_info))
                    print(repr(hz2hz_info['林']))
                f(只读囗另档囗汉字到单字信息)
                    #RecurView4Seq(None, ('⿰', (('hz', '木'), ('hz', '木'))))
                f(另档囗汉字到单字信息)
                    #('⿰', (('hz', '木'), ('hz', '木')))
                #==>> override:dataobj2readonly___recur_view
                raise
            return

        return _dump_by_name
    def load_readonly_by_name(sf, 汉字字集名, /, may_path_bypass_version_str):
        'FileNotFoundError'
        version_str = 汉字字集名
        只读囗另档囗汉字到单字信息 = sf.load_data_file__ver(version_str, deepcopy_on_cached_state=False, result_readonly=True, may_path_bypass_version_str=may_path_bypass_version_str)
        return 只读囗另档囗汉字到单字信息





    def _main4dump(sf, /):
        #另档 的 目的 在于『避免过于耗时的加载_slow_load_full_hz2xxx_hz_info_』
        #   因此，只有 _main4dump()使用 _mk4dump_by_name()
        #
        'FileExistsError'
        _dump_by_name = sf._mk4dump_by_name()

        汉字字集名 = 'cjk_common_subset_2513'
        _dump_by_name(汉字字集名, force=False, may_path_bypass_version_str=None)


    def _main4load(sf, /):
        '-> 只读囗共享汉字到单字信息'
        def recur():
            try:
                只读囗共享汉字到单字信息 = sf.load_readonly_by_name('cjk_common_subset_2513', may_path_bypass_version_str=None)
            except FileNotFoundError:
                sf._main4dump()
                    # FileExistsError
                return recur()
            return 只读囗共享汉字到单字信息
        return recur()
#]]]

r'''
_cfg = Config4load_subset_result_file4汉字到单字信息(
    __file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='共享汉字集单字信息.py.out.另档.{}.汉字到单字信息.txt'
    ,version_str__rex   =r'^cjk_common_subset_[0-9]+(?:_trivial_TS_[0-9]+)?$'
    ,encoding           ='utf8'
    ,hz_info_immutable = ?
    )

只读囗共享汉字到单字信息 = _cfg._main4load()
if __name__ == "__main__":
    pass


from nn_ns.CJK.cjk_subsets.共享汉字集单字信息 import 只读囗共享汉字到单字信息
#'''

######################


