r'''
from nn_ns.CJK.cjk_subsets.共享汉字集笔顺码 import 只读囗共享汉字到笔顺码, 只读囗平凡繁简囗初步缩减囗共享汉字到笔顺码, 只读囗初步缩减囗共享汉字到笔顺码, 只读囗平凡繁简囗共享汉字到笔顺码

hz2513 -> 笔顺码
  另外 建档
    cjk_common_subset_2513 -> 只读囗共享汉字到笔顺码
    cjk_common_subset_1869_trivial_TS_1631 -> 只读囗平凡繁简囗初步缩减囗共享汉字到笔顺码
释名:
    cjk_common_subset_2513/共享汉字字集
    cjk_common_subset_1869/初步缩减囗共享汉字字集
    cjk_common_subset_1869_trivial_TS_1631/平凡繁简囗初步缩减囗共享汉字字集
    cjk_common_subset_2513_trivial_TS_2227/平凡繁简囗共享汉字字集

e ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集笔顺码.py
py -m nn_ns.CJK.cjk_subsets.共享汉字集笔顺码
    生成: ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集笔顺码.py.out.另档.cjk_common_subset_2513.汉字到笔顺码.txt
!du -h ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集笔顺码.py.out.另档.cjk_common_subset_2513.汉字到笔顺码.txt
    36K
view ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集笔顺码.py.out.另档.cjk_common_subset_2513.汉字到笔顺码.txt



view ../../python3_src/seed/helper/IConfig4load_versioned_repr_txt_file.py

[[old:using IConfig4load_versioned_repr_txt_file replace pprint

py -m nn_ns.CJK.cjk_subsets.共享汉字集笔顺码   >  ../../python3_src/nn_ns/CJK/CJK_data/raw/cjk_subsets.共享汉字集笔顺码.py.out.另档囗共享汉字到笔顺码.txt
view   ../../python3_src/nn_ns/CJK/CJK_data/raw/cjk_subsets.共享汉字集笔顺码.py.out.另档囗共享汉字到笔顺码.txt
!du -h   ../../python3_src/nn_ns/CJK/CJK_data/raw/cjk_subsets.共享汉字集笔顺码.py.out.另档囗共享汉字到笔顺码.txt
56K #pprint

!du -h ../../python3_src/nn_ns/CJK/cjk_subsets/hanzi.py
132K


!rm   ../../python3_src/nn_ns/CJK/CJK_data/raw/cjk_subsets.共享汉字集笔顺码.py.out.另档囗共享汉字到笔顺码.txt
]]

#'''

__all__ = '''
    只读囗共享汉字到笔顺码

    只读囗平凡繁简囗初步缩减囗共享汉字到笔顺码
    只读囗初步缩减囗共享汉字到笔顺码
    只读囗平凡繁简囗共享汉字到笔顺码
    '''.split()

from seed.abc.abc__ver0 import override
from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file

#[[[
class Config4load_versioned_repr_txt_file(IConfig4load_versioned_repr_txt_file):
    pass
class Config4load_subset_result_file4汉字到笔顺码(IConfig4load_versioned_repr_txt_file):
    r'''
    dataobj = subset_result of 汉字到笔顺码
    st = dataobj
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
        dataobj = st
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
        st = dataobj
        return st

    @override
    def text2state___eval(sf, txt, /):
        #.text5state___repr
        #
        汉字到笔顺码 = {}
        for line in txt.split():
            assert len(line) >= 2
            汉字 = line[0]
            笔顺码 = line[1:]
            汉字到笔顺码[汉字] = 笔顺码
        st = 汉字到笔顺码
        return st
    @override
    def text5state___repr(sf, st, /):
        'can be overrided as: def text5state___repr(sf, st, /, *args4repr, **kwargs4repr):'
        #.text2state___eval
        #.check_extra_input4repr
        汉字到笔顺码 = st
        txt = '\n'.join(sorted(汉字+笔顺码 for 汉字, 笔顺码 in 汉字到笔顺码.items()))

        return txt
    def check_extra_input4repr(sf, /):
        'can be overrided as: def check_extra_input4repr(sf, /, *args4repr, **kwargs4repr): #check len/keys #same as text5state___repr'
        #.text5state___repr
        pass
_cfg = Config4load_subset_result_file4汉字到笔顺码(
    __file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='共享汉字集笔顺码.py.out.另档.{}.汉字到笔顺码.txt'
    ,version_str__rex   =r'^cjk_common_subset_[0-9]+(?:_trivial_TS_[0-9]+)?$'
    ,encoding           ='utf8'
    )
#]]]




def _mk4dump_by_name():
    #另档 的 目的 在于『避免加载nn_ns.CJK.CJK_data.汉字笔顺』
    #   因此，只有 _main()使用 _mk4dump_by_name()
    #
    import nn_ns.CJK.cjk_subsets.hanzi as hanzi_lib
    from nn_ns.CJK.cjk_subsets.hanzi import hz_sp_str2hz_set
    from nn_ns.CJK.CJK_data.汉字笔顺 import 汉字到笔顺码
    ######################
    def _gen(hz_sp_str, /):
        hz_set = hz_sp_str2hz_set(hz_sp_str)
        另档囗汉字到笔顺码 = {hz:汉字到笔顺码[hz] for hz in hz_set}
        return 另档囗汉字到笔顺码
    ######################
    def _gen_by_name(汉字字集名, /):
        if not 汉字字集名 in hanzi_lib.__all__:raise ValueError(汉字字集名)
        带空格汉字字集 = getattr(hanzi_lib, 汉字字集名)
        if not type(带空格汉字字集) is str: raise TypeError(汉字字集名)

        另档囗汉字到笔顺码 = _gen(带空格汉字字集)
        return 另档囗汉字到笔顺码
    def _dump_by_name(汉字字集名, /, force, may_path_bypass_version_str):
        #force=False, may_path_bypass_version_str=None
        另档囗汉字到笔顺码 = _gen_by_name(汉字字集名)
        version_str = 汉字字集名
        _cfg.dump_data_file__ver(version_str, 另档囗汉字到笔顺码, force=force, args4repr=[], kwargs4repr={}, args4dump=[], kwargs4dump={}, is_readonly_dataobj=False, may_path_bypass_version_str=may_path_bypass_version_str)
        只读囗另档囗汉字到笔顺码 = load_readonly_by_name(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
        if not {**只读囗另档囗汉字到笔顺码} == 另档囗汉字到笔顺码: raise logic-err
        return

    return _dump_by_name
def load_readonly_by_name(汉字字集名, /, may_path_bypass_version_str):
    'FileNotFoundError'
    version_str = 汉字字集名
    只读囗另档囗汉字到笔顺码 = _cfg.load_data_file__ver(version_str, deepcopy_on_cached_state=False, result_readonly=True, may_path_bypass_version_str=may_path_bypass_version_str)
    return 只读囗另档囗汉字到笔顺码



r'''[[[
def _():
    from nn_ns.CJK.cjk_subsets.hanzi import (
    cjk_common_subset_2513
    ,cjk_common_subset_1869
    ,cjk_common_subset_2513_trivial_TS_2227
    ,cjk_common_subset_1869_trivial_TS_1631
    )
    from nn_ns.CJK.cjk_subsets.hanzi import (
    hz_sp_str2hz_str
    ,hz_sp_str2hz_set
    ,hz_set2sorted_hz_str
    )
    from pprint import pprint
    ######################
    ######################
    #其实 只需要 cjk_common_subset_2513 版，其他 无所谓
    共享汉字到笔顺码 = _gen(cjk_common_subset_2513, 汉字到笔顺码)

    ######################
    ######################

    pprint(共享汉字到笔顺码)
#]]]'''


def _main():
    #另档 的 目的 在于『避免加载nn_ns.CJK.CJK_data.汉字笔顺』
    #   因此，只有 _main()使用 _mk4dump_by_name()
    #
    'FileExistsError'
    _dump_by_name = _mk4dump_by_name()

    汉字字集名 = 'cjk_common_subset_2513'
    _dump_by_name(汉字字集名, force=False, may_path_bypass_version_str=None)


def _load():
    def recur():
        try:
            只读囗共享汉字到笔顺码 = load_readonly_by_name('cjk_common_subset_2513', may_path_bypass_version_str=None)
        except FileNotFoundError:
            _main()
                # FileExistsError
            return recur()
        return 只读囗共享汉字到笔顺码
    return recur()
只读囗共享汉字到笔顺码 = _load()
if __name__ == "__main__":
    pass


from nn_ns.CJK.cjk_subsets.共享汉字集笔顺码 import 只读囗共享汉字到笔顺码

######################

from seed.mapping_tools.dict_op import subset_keys__immutable
from nn_ns.CJK.cjk_subsets.hanzi import 平凡繁简囗初步缩减囗共享汉字字集, 初步缩减囗共享汉字字集, 平凡繁简囗共享汉字字集
from nn_ns.CJK.cjk_subsets.hanzi import hz_sp_str2hz_set
from seed.tiny import MapView

#只读囗平凡繁简囗初步缩减囗共享汉字到笔顺码 = MapView(subset_keys__immutable(只读囗共享汉字到笔顺码, hz_sp_str2hz_set(平凡繁简囗初步缩减囗共享汉字字集)))
def _tmp__subset_hz2xxx(hz_sp_str, /):
    return MapView(subset_keys__immutable(只读囗共享汉字到笔顺码, hz_sp_str2hz_set(hz_sp_str)))
只读囗平凡繁简囗初步缩减囗共享汉字到笔顺码 = _tmp__subset_hz2xxx(平凡繁简囗初步缩减囗共享汉字字集)
只读囗初步缩减囗共享汉字到笔顺码 = _tmp__subset_hz2xxx(初步缩减囗共享汉字字集)
只读囗平凡繁简囗共享汉字到笔顺码 = _tmp__subset_hz2xxx(平凡繁简囗共享汉字字集)









assert len(只读囗平凡繁简囗初步缩减囗共享汉字到笔顺码) == 1631
assert len(只读囗初步缩减囗共享汉字到笔顺码) == 1869
assert len(只读囗平凡繁简囗共享汉字到笔顺码) == 2227
assert len(只读囗共享汉字到笔顺码) == 2513

from nn_ns.CJK.cjk_subsets.共享汉字集笔顺码 import 只读囗共享汉字到笔顺码, 只读囗平凡繁简囗初步缩减囗共享汉字到笔顺码, 只读囗初步缩减囗共享汉字到笔顺码, 只读囗平凡繁简囗共享汉字到笔顺码


