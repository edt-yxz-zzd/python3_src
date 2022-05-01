r'''
see:
    view ../../python3_src/nn_ns/CJK/cjk_subsets/囗共享汉字集单字信息.py

e ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py

copy from:
    view ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集笔顺码.py
    .+1,$s/笔顺码/字形拆分树/g

from nn_ns.CJK.cjk_subsets.共享汉字集字形拆分树 import 只读囗共享汉字到字形拆分树
py -m nn_ns.app.debug_cmd   nn_ns.CJK.cjk_subsets.共享汉字集字形拆分树

py -m nn_ns.CJK.cjk_subsets.共享汉字集字形拆分树
    生成: ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py.out.另档.cjk_common_subset_2513.汉字到字形拆分树.txt
!du -h ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py.out.另档.cjk_common_subset_2513.汉字到字形拆分树.txt
    116K
view ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py.out.另档.cjk_common_subset_2513.汉字到字形拆分树.txt


字源分解？
,'乾'
:('⿸', [('⿰', [('hz', '𠦝'), ('hz', '𠂉')]), ('hz', '乙')])
,'修'
:('⿸', [('hz', '攸'), ('hz', '彡')])

引用外部部件
,'亥'
:('⿳', [('hz', '亠'), ('ref', '&GT-00154;'), ('hz', '人')])

人为边界？
,'亨'
:('⿱', [('⿱', [('hz', '亠'), ('hz', '口')]), ('hz', '了')])
,'亭'
:('⿱', [('⿳', [('hz', '亠'), ('hz', '口'), ('hz', '冖')]), ('hz', '丁')])
,'克'
:('⿱', [('hz', '古'), ('hz', '儿')])


使用部首汉字而非正字:𠆢人
,'今'
:('⿱', [('hz', '𠆢'), ('hz', '𪜊')])
使用部件字符而非部首汉字
,'先'
:('⿱', [('hz', '⺧'), ('hz', '儿')])
    #搜索: /[⺳タ具⺢⻖⺗直⺯刃⺜⺇⻀⺫𥄳⺃屮旣⺲⻏灰⺈⺊冗⺼⺧⻢穀⺣⺄⺆充⺪叟者⻞⺶⻃⺌⻤⻌]
    #   <<== view script/collect_hz_components.py


不完全分解？
,'亢'
:('⿱', [('hz', '亠'), ('hz', '几')])
,'伉'
:('⿰', [('hz', '亻'), ('hz', '亢')])


诡异的拆分？错误的拆分？
,'余'
:('⿱', [('ref', '&CDP-8AFC;'), ('hz', '朩')])



拆分有歧义？
,'元'
:('⿱', [('hz', '一'), ('hz', '兀')])


该拆不拆
,'兜'
:('hz', '兜')

#'''

__all__ = '''
    只读囗共享汉字到字形拆分树

    只读囗平凡繁简囗初步缩减囗共享汉字到字形拆分树
    只读囗初步缩减囗共享汉字到字形拆分树
    只读囗平凡繁简囗共享汉字到字形拆分树
    '''.split()

from seed.abc.abc__ver0 import override
from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file
from seed.tiny_.pprint4container__depth1 import pprint4container__depth1, show5pprint
from seed.tiny import MapView
from nn_ns.CJK.CJK_struct.CHISE_IDS_67b94ff_20191211.load_parse_result___CHISE_IDS import load_hz2tree___BMP_only, load_hz2tree___ipath, hz2mutable_tree__to__hz2immutable_tree, hz2mutable_tree__from__hz2immutable_tree, mutable_tree2immutable, mutable_tree5immutable

#[[[
#view ../../python3_src/seed/helper/IConfig4load_versioned_repr_txt_file.py
class Config4load_subset_result_file4汉字到字形拆分树(IConfig4load_versioned_repr_txt_file):
    r'''
    readonly_dataobj = MapView<hz2immutable_tree>
        #只读囗另档囗汉字到字形拆分树
    dataobj = hz2immutable_tree
        #另档囗汉字到字形拆分树
        #children :: tuple<tree>
        #subset_result of 汉字到字形拆分树
    st = hz2mutable_tree
        #children :: list<tree>
        #为何st与dataobj不同？主要是满足:
            def _mk4dump_by_name():
                if not {**只读囗另档囗汉字到字形拆分树} == 另档囗汉字到字形拆分树: raise logic-err

    ----:
    sf.dataobj_immutable = False
    sf.state_immutable = False
    #'''
    def __init__(sf, /, *, __file__, data_dir_rpath, basename_fmt, version_str__rex, encoding):
        dataobj_immutable = False
        state_immutable = False
        super().__init__(__file__=__file__, data_dir_rpath=data_dir_rpath, basename_fmt=basename_fmt, version_str__rex=version_str__rex, encoding=encoding, dataobj_immutable=dataobj_immutable, state_immutable=state_immutable)
    @override
    def state2dataobj___create(sf, st, /):
        #.state5dataobj___save
        hz2mutable_tree = st
        hz2immutable_tree = hz2mutable_tree__to__hz2immutable_tree(hz2mutable_tree)
        dataobj = hz2immutable_tree
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
        hz2immutable_tree = dataobj
        hz2mutable_tree = hz2mutable_tree__from__hz2immutable_tree(hz2immutable_tree)
        st = hz2mutable_tree
        return st




    @override
    def text5state___repr(sf, st, /):
        'can be overrided as: def text5state___repr(sf, st, /, *args4repr, **kwargs4repr):'
        #.text2state___eval
        #.check_extra_input4repr

        #汉字到字形拆分树 = st
        hz2mutable_tree = st
        txt = show5pprint('fout', pprint4container__depth1, hz2mutable_tree)

        return txt
    @override
    def check_extra_input4repr(sf, /):
        'can be overrided as: def check_extra_input4repr(sf, /, *args4repr, **kwargs4repr): #check len/keys #same as text5state___repr'
        #.text5state___repr
        pass



    @override#to avoid RecurView4Seq
    def dataobj2readonly___recur_view(sf, dataobj, /):
        #.dataobj5readonly___literal_rebuild
        'dataobj -> readonly_dataobj'
        #result_readonly=True
        readonly_dataobj = MapView(dataobj)
        return readonly_dataobj

_cfg = Config4load_subset_result_file4汉字到字形拆分树(
    __file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='共享汉字集字形拆分树.py.out.另档.{}.汉字到字形拆分树.txt'
    ,version_str__rex   =r'^cjk_common_subset_[0-9]+(?:_trivial_TS_[0-9]+)?$'
    ,encoding           ='utf8'
    )
#]]]




def _mk4dump_by_name():
    #另档 的 目的 在于『避免加载nn_ns.CJK.CJK_struct.CHISE_IDS_67b94ff_20191211.parse_result___CHISE_IDS::hz2tree___BMP_only』
    #   因此，只有 _main()使用 _mk4dump_by_name()
    #
    from seed.mapping_tools.dict_op import subset_keys__immutable
    import nn_ns.CJK.cjk_subsets.hanzi as hanzi_lib
    from nn_ns.CJK.cjk_subsets.hanzi import hz_sp_str2hz_set
    from nn_ns.CJK.CJK_struct.CHISE_IDS_67b94ff_20191211.parse_result___CHISE_IDS import hz2tree___BMP_only as 汉字到字形拆分树 #readonly__hz2tree #MapView+tuple children
    ######################
    def _gen(hz_sp_str, /):
        hz_set = hz_sp_str2hz_set(hz_sp_str)
        另档囗汉字到字形拆分树 = subset_keys__immutable(汉字到字形拆分树, hz_set)
        return 另档囗汉字到字形拆分树
    ######################
    def _gen_by_name(汉字字集名, /):
        if not 汉字字集名 in hanzi_lib.__all__:raise ValueError(汉字字集名)
        带空格汉字字集 = getattr(hanzi_lib, 汉字字集名)
        if not type(带空格汉字字集) is str: raise TypeError(汉字字集名)

        另档囗汉字到字形拆分树 = _gen(带空格汉字字集)
        return 另档囗汉字到字形拆分树
    def _dump_by_name(汉字字集名, /, force, may_path_bypass_version_str):
        #force=False, may_path_bypass_version_str=None
        另档囗汉字到字形拆分树 = _gen_by_name(汉字字集名)
        version_str = 汉字字集名
        _cfg.dump_data_file__ver(version_str, 另档囗汉字到字形拆分树, force=force, args4repr=[], kwargs4repr={}, args4dump=[], kwargs4dump={}, is_readonly_dataobj=False, may_path_bypass_version_str=may_path_bypass_version_str)
        只读囗另档囗汉字到字形拆分树 = load_readonly_by_name(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
        try:
            if not {**只读囗另档囗汉字到字形拆分树} == 另档囗汉字到字形拆分树: raise logic-err
        except:
            def f(hz2tree, /):
                print(len(hz2tree))
                print(repr(hz2tree['林']))
            f(只读囗另档囗汉字到字形拆分树)
                #RecurView4Seq(None, ('⿰', (('hz', '木'), ('hz', '木'))))
            f(另档囗汉字到字形拆分树)
                #('⿰', (('hz', '木'), ('hz', '木')))
            #==>> override:dataobj2readonly___recur_view
            raise
        return

    return _dump_by_name
def load_readonly_by_name(汉字字集名, /, may_path_bypass_version_str):
    'FileNotFoundError'
    version_str = 汉字字集名
    只读囗另档囗汉字到字形拆分树 = _cfg.load_data_file__ver(version_str, deepcopy_on_cached_state=False, result_readonly=True, may_path_bypass_version_str=may_path_bypass_version_str)
    return 只读囗另档囗汉字到字形拆分树





def _main():
    #另档 的 目的 在于『避免加载nn_ns.CJK.CJK_struct.CHISE_IDS_67b94ff_20191211.parse_result___CHISE_IDS::hz2tree___BMP_only』
    #   因此，只有 _main()使用 _mk4dump_by_name()
    #
    'FileExistsError'
    _dump_by_name = _mk4dump_by_name()

    汉字字集名 = 'cjk_common_subset_2513'
    _dump_by_name(汉字字集名, force=False, may_path_bypass_version_str=None)


def _load():
    def recur():
        try:
            只读囗共享汉字到字形拆分树 = load_readonly_by_name('cjk_common_subset_2513', may_path_bypass_version_str=None)
        except FileNotFoundError:
            _main()
                # FileExistsError
            return recur()
        return 只读囗共享汉字到字形拆分树
    return recur()
只读囗共享汉字到字形拆分树 = _load()
if __name__ == "__main__":
    pass


from nn_ns.CJK.cjk_subsets.共享汉字集字形拆分树 import 只读囗共享汉字到字形拆分树

######################


