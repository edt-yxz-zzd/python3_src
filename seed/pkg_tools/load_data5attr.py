#__all__:goto
r'''[[[
e ../../python3_src/seed/pkg_tools/load_data5attr.py
see also:
    view ../../python3_src/seed/types/DottedAttrCollector.py
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/xml/resource_loader.py

TODO:refactor:
    去掉多余功能
    另立:cache
    另立:dump_binary_loader
    ... ...

py -m seed.pkg_tools.load_data5attr
py -m nn_ns.app.debug_cmd   seed.pkg_tools.load_data5attr -x
py -m nn_ns.app.doctest_cmd seed.pkg_tools.load_data5attr:__doc__ -ht
py_adhoc_call   seed.pkg_tools.load_data5attr   @f


view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/xml/ver14_0_0/age.Age.ver14_0_0.xml.out.txt

age.Age.ver14_0_0.xml.out.txt
>>> import nn_ns.CJK.unicode.ucd_unihan.xml.ver14_0_0 as M
>>> from pathlib import Path
>>> [_dir] = M.__path__
>>> _dir = Path(_dir)

>>> def property_alias2basename4file(pa, /):
...     paths = _dir.glob(pa+'.*.out.txt')
...     if not paths:raise LookupError(pa)
...     [path4datafile] = paths
...     basename4datafile = path4datafile.name
...     return basename4datafile


>>> data_loader4raw_bytes = mk_data_loader5attr__ver1_params('data_loader4raw_bytes', 'nn_ns.CJK.unicode.ucd_unihan.xml.ver14_0_0', echo, xencoding='', parser='echo')
>>> data_loader4raw_txt__u8 = mk_data_loader5attr__ver1_params('data_loader4raw_txt__u8', 'nn_ns.CJK.unicode.ucd_unihan.xml.ver14_0_0', echo, xencoding='u8', parser='echo')
>>> data_loader4literal_eval__u8 = mk_data_loader5attr__ver1_params('data_loader4literal_eval__u8', 'nn_ns.CJK.unicode.ucd_unihan.xml.ver14_0_0', property_alias2basename4file, xencoding='u8', parser='literal_eval')
>>> data_loader4depth1__literal_eval__u8 = mk_data_loader5attr__ver1_params('data_loader4depth1__literal_eval__u8', 'nn_ns.CJK.unicode.ucd_unihan.xml.ver14_0_0', property_alias2basename4file, xencoding='u8', parser='literal_eval', imay_max_depth=1)


>>> data_loader4raw_bytes.version._.ver14_0_0.xml.out.txt
data_loader4raw_bytes.version._.ver14_0_0.xml.out.txt
>>> data_loader4raw_bytes.version._.ver14_0_0.xml.out.txt()
b"{'3.2.0'\n: {0xF951: 1}\n,'4.0.0'\n: {0x2F868: 1, 0x2F874: 1, 0x2F91F: 1, 0x2F95F: 1, 0x2F9BF: 1}\n}"

>>> data_loader4raw_txt__u8.version._.ver14_0_0.xml.out.txt
data_loader4raw_txt__u8.version._.ver14_0_0.xml.out.txt
>>> data_loader4raw_txt__u8.version._.ver14_0_0.xml.out.txt()
"{'3.2.0'\n: {0xF951: 1}\n,'4.0.0'\n: {0x2F868: 1, 0x2F874: 1, 0x2F91F: 1, 0x2F95F: 1, 0x2F9BF: 1}\n}"

>>> data_loader4literal_eval__u8.version
data_loader4literal_eval__u8.version
>>> data_view = data_loader4literal_eval__u8.version()
>>> data_view
RecurView4Mapping(None, {'3.2.0': {63825: 1}, '4.0.0': {194664: 1, 194676: 1, 194847: 1, 194911: 1, 195007: 1}})

#cached:
>>> data_view is data_loader4literal_eval__u8.version()
True
>>> data_view['3.2.0']
RecurView4Mapping(None, {63825: 1})
>>> data_view['3.2.0'][63825]
1
>>> data_loader4literal_eval__u8.version() is data_loader4literal_eval__u8.type()
False
>>> data_loader4literal_eval__u8.type()
RecurView4Mapping(None, {'abbreviation': {0: 33, 127: 34, 173: 1, 847: 1, 1564: 1, 6155: 5, 8203: 5, 8234: 6, 8287: 2, 8294: 4, 65024: 16, 65279: 1, 917760: 240}, 'alternate': {65279: 1}, 'control': {0: 32, 127: 1, 130: 23, 154: 6}, 'correction': {418: 2, 1801: 1, 3294: 1, 3741: 1, 3743: 1, 3747: 1, 3749: 1, 4048: 1, 4588: 4, 8472: 1, 9288: 2, 11130: 1, 11132: 1, 40981: 1, 43630: 1, 65048: 1, 74452: 2, 93782: 2, 93814: 2, 110593: 1, 118981: 1}, 'figment': {128: 2, 153: 1}})


>>> data_loader4depth1__literal_eval__u8
data_loader4depth1__literal_eval__u8
>>> data_loader4depth1__literal_eval__u8.version
RecurView4Mapping(None, {'3.2.0': {63825: 1}, '4.0.0': {194664: 1, 194676: 1, 194847: 1, 194911: 1, 195007: 1}})
>>> data_loader4depth1__literal_eval__u8.version is data_loader4depth1__literal_eval__u8.version
True
>>> data_loader4depth1__literal_eval__u8.version is data_loader4depth1__literal_eval__u8.type
False
>>> data_loader4depth1__literal_eval__u8.type
RecurView4Mapping(None, {'abbreviation': {0: 33, 127: 34, 173: 1, 847: 1, 1564: 1, 6155: 5, 8203: 5, 8234: 6, 8287: 2, 8294: 4, 65024: 16, 65279: 1, 917760: 240}, 'alternate': {65279: 1}, 'control': {0: 32, 127: 1, 130: 23, 154: 6}, 'correction': {418: 2, 1801: 1, 3294: 1, 3741: 1, 3743: 1, 3747: 1, 3749: 1, 4048: 1, 4588: 4, 8472: 1, 9288: 2, 11130: 1, 11132: 1, 40981: 1, 43630: 1, 65048: 1, 74452: 2, 93782: 2, 93814: 2, 110593: 1, 118981: 1}, 'figment': {128: 2, 153: 1}})






extended=True
>>> def _ex___property_alias2basename4file(qnm4pkg, ver_pa, /):
...     '!!+extended'
...     ver, _, pa = ver_pa.rpartition('.')
...     #fail:paths = [*_ex___dir.glob(ver_pa.replace('.', '_')+'.*.out.txt')]
...     paths = [*(_ex___dir/ver).glob(pa+'.*.out.txt')]
...     if not paths:raise LookupError(ver_pa)
...     if not len(paths) == 1:raise LookupError(ver_pa, paths)
...     [path4datafile] = paths
...     basename4datafile = path4datafile.name
...     qnm4new_pkg = '.'.join([qnm4pkg, ver])
...     return (qnm4new_pkg, basename4datafile)

>>> _qnm4pkg = 'nn_ns.CJK.unicode.ucd_unihan.xml'
>>> _ex___dir = dir5qnm4pkg(_qnm4pkg)
>>> data_loader4depth2__literal_eval__u8 = mk_data_loader5attr__ver1_params('data_loader4depth2__literal_eval__u8', _qnm4pkg, _ex___property_alias2basename4file, xencoding='u8', extended=True, parser='literal_eval', imay_max_depth=2, transformer=lambda v2i2sz:(v2i2sz, len(v2i2sz), sum(sz for i2sz in v2i2sz.values() for sz in i2sz.values())))
>>> data_loader4depth2__literal_eval__u8.ver14_0_0.version
RecurView4Seq(None, ({'3.2.0': {63825: 1}, '4.0.0': {194664: 1, 194676: 1, 194847: 1, 194911: 1, 195007: 1}}, 2, 6))

>>> data_loader4depth2__literal_eval__u8.ver14_0_0.type
RecurView4Seq(None, ({'abbreviation': {0: 33, 127: 34, 173: 1, 847: 1, 1564: 1, 6155: 5, 8203: 5, 8234: 6, 8287: 2, 8294: 4, 65024: 16, 65279: 1, 917760: 240}, 'alternate': {65279: 1}, 'control': {0: 32, 127: 1, 130: 23, 154: 6}, 'correction': {418: 2, 1801: 1, 3294: 1, 3741: 1, 3743: 1, 3747: 1, 3749: 1, 4048: 1, 4588: 4, 8472: 1, 9288: 2, 11130: 1, 11132: 1, 40981: 1, 43630: 1, 65048: 1, 74452: 2, 93782: 2, 93814: 2, 110593: 1, 118981: 1}, 'figment': {128: 2, 153: 1}}, 5, 444))
>>> data_loader4depth2__literal_eval__u8.ver14_0_0.version is data_loader4depth2__literal_eval__u8.ver14_0_0.version
True
>>> data_loader4depth2__literal_eval__u8.ver14_0_0.type is data_loader4depth2__literal_eval__u8.ver14_0_0.type
True
>>> data_loader4depth2__literal_eval__u8.ver14_0_0.type is data_loader4depth2__literal_eval__u8.ver14_0_0.version
False


#]]]'''
__all__ = r'''
mk_data_loader5attr__ver2_IDataLoaderMaker
    IFormatter
        Formatter__glob
            TooManyFileFoundError

    IDataLoaderMaker
        Maker4DataLoader__details__mixins__fmtr

    IDataLoader
        IDataLoader__details
            IDataLoader__details__mixins__pkg_nm_path
                IDataLoader__details__mixins__fmtr
                    DataLoader__details__mixins__fmtr






mk_data_loader5attr__ver1_params




rootdir_5or_qnm4pkg
    dir5qnm4pkg

_DEBUGGING_VERBOSE_
'''.split()#'''
    #_DEBUGGING_VERBOSE_:to print_err??
__all__
import os.path
from pathlib import Path, PurePosixPath
from importlib import import_module
from seed.pkg_tools.is_pkg import is_pkg_# is_module_

from seed.types.DottedAttrCollector import DottedAttrCollector, ReDefRepr
from seed.types.DottedAttrCollector import DottedAttrCollector___autocall_at_max_depth as _DataLoader___autocall_at_max_depth

from seed.types.view.RecurView import default_cfg4RecurView
from seed.pkg_tools.load_resource import read_under_pkg_

from seed.tiny_.check import check_type_le, check_type_is, check_int_ge
from seed.tiny_.check import check_callable
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name
from seed.tiny import echo, echo_args# null_tuple
from seed.tiny import print_err

from seed.helper.safe_eval import safe_eval
from ast import literal_eval

import pickle
from seed.pkg_tools.load_resource import open_under_pkg_, does_exist_under_pkg_
#from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
#from seed.pkg_tools.load_resource import list_potential_basenames_under_pkg_, sorted_potential_basenames_under_pkg_, iter_potential_basenames_under_pkg_, does_exist_under_pkg_, with_path_under_pkg_
from seed.io.may_open import open4w, open4w_err, open4r
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper




_DEBUGGING_VERBOSE_ = False



class IFormatter(ABC):
    __slots__ = ()
    @abstractmethod
    def format(sf, x, /):
        '-> str'
IFormatter.register(str)

#class IDataLoader(ABC):
#    __slots__ = ()
#    @abstractmethod
#    def load(sf, qnm4pkg4root, qattr4data, /):
#        'qnm4pkg4root -> qattr4data -> data_view'
class IDataLoaderMaker(ABC):
    __slots__ = ()
    @abstractmethod
    def mk_data_loader(sf, qnm4pkg4root, qattr4data, /):
        'qnm4pkg4root -> qattr4data -> data_loader'
class IDataLoader(ABC):
    __slots__ = ()
    @abstractmethod
    def load(sf, /):
        '-> data'
        #xxx:'-> (data_view|data)'


class IDataLoader__details(IDataLoader):
    r'''[[[
sf{<qnm4pkg4root, qattr4data>} =>:
data_source_file
    pkg4data_dir
    relpath4data_file :: relative_path{qnm4pkg4root}
    source_parser :: ifile4data -> raw_data

raw_data
++data_binary_dump_file
    pkg4dump_dir
    relpath4dump_file :: relative_path{qnm4pkg4root}
    binary_dumper :: ofile4dump -> raw_data -> None
    binary_loader :: ifile4dump -> raw_data

transformer :: raw_data -> data
data

no viewer?:
    viewer :: data -> data_view
    data_view


no cache here:
    *expecting external cache
        {(qnm4pkg4root, qattr4data):data_view}
    *or:no cache at all, generate fresh data each time without viewer

    #]]]'''#'''
    __slots__ = ()
    @override
    def load(sf, /):
        '-> data'
        may_binary_loader = sf.may_binary_loader
        done = False
        for ok in range(2)[::-1]:
            while not may_binary_loader is None:
                may_binary_dumper = sf.may_binary_dumper
                may_query_metadata4dump_file = sf.may_query_metadata4dump_file
                may_query_metadata4data_file = sf.may_query_metadata4data_file
                may_remove_dump_file = sf.may_remove_dump_file
                assert callable(may_binary_dumper)
                assert callable(may_binary_loader)
                assert callable(may_query_metadata4dump_file)
                assert callable(may_query_metadata4data_file)
                assert callable(may_remove_dump_file)

                binary_dumper = may_binary_dumper
                binary_loader = may_binary_loader
                query_metadata4dump_file = may_query_metadata4dump_file
                query_metadata4data_file = may_query_metadata4data_file
                remove_dump_file = may_remove_dump_file

                ######################
                try:
                    metadata4dump_file = query_metadata4dump_file()
                except FileNotFoundError:
                    #no dump_file found
                    break
                metadata4dump_file
                metadata4data_file = query_metadata4data_file()
                if not metadata4data_file['mtime'] <= metadata4dump_file['mtime']:
                    if not ok == 1:raise 000
                    if _DEBUGGING_VERBOSE_:print_err('='*22, '\n', __name__, 'remove_dump_file', sf)
                    remove_dump_file()
                    #xxx:if not metadata4data_file['size'] == metadata4dump_file['size']:raise Exception(sf)
                    try:
                        metadata4dump_file = query_metadata4dump_file()
                    except FileNotFoundError:
                        #no dump_file found
                        break
                    raise Exception(sf, 'remove_dump_file:not work properly')
                    #no dump_file found
                ######################
                try:
                    with sf.open_ifile4dump() as ifile4dump:
                        raw_data = binary_loader(ifile4dump)
                except FileNotFoundError:
                    #no dump_file found
                    raise Exception(sf, 'open_ifile4dump,query_metadata4data_file:mismatch')
                    break
                else:
                    raw_data
                    done = True
                    break
            if done:
                raw_data
                break
            ######################
            if not ok: raise 000
            ######################
            assert ok == 1
            #no dump_file found
            ######################

            with sf.open_ifile4data() as ifile4data:
                raw_data = sf.source_parser(ifile4data)
            raw_data

            if not may_binary_loader is None:
                #no dump_file found
                if _DEBUGGING_VERBOSE_:print_err('='*22, '\n', __name__, 'open_ofile4dump', sf)
                with sf.open_ofile4dump() as ofile4dump:
                    binary_dumper(ofile4dump, raw_data)
                assert ok == 1
                continue
            break
        else:
            raise 000
        raw_data

        data = sf.transformer(raw_data)
        return data
        ######################
        ######################
        ######################
        ######################
        #old:

        r'''[[[
        xencoding = ???
        path4data_file = sf.path4data_file
        may_path4dump_file = sf.may_path4dump_file
        may_binary_dumper = sf.may_binary_dumper
        may_binary_loader = sf.may_binary_loader

        with open4r(path4data_file, xencoding=xencoding) as ifile4data:
            raw_data = sf.source_parser(ifile4data)
        raw_data

        if not may_path4dump_file is None:
            assert callable(may_binary_dumper)
            assert callable(may_binary_loader)
            path4dump_file = may_path4dump_file
            binary_dumper = may_binary_dumper
            binary_loader = may_binary_loader
            with open4w(path4dump_file, force=False, xencoding=None) as ofile4dump:
                binary_dumper(ofile4dump, raw_data)
            with open4r(path4dump_file, xencoding=None) as ifile4dump:
                raw_data = binary_loader(ifile4dump)
            raw_data
        raw_data

        data = sf.transformer(raw_data)
        return data
        #]]]'''#'''

    @abstractmethod
    def open_ofile4dump(sf, /):
        '-> ofile4dump | ^FileExistsError | ^FileNotFoundError'
    @abstractmethod
    def open_ifile4dump(sf, /):
        '-> ifile4dump | ^FileNotFoundError'
    @abstractmethod
    def open_ifile4data(sf, /):
        '-> ifile4data | ^FileNotFoundError'

    #see:importlib.abc.SourceLoader::path_stats(self, path) -> metadata_dict{.mtime,.size/(optional)}
    @abstractmethod
    def may_query_metadata4dump_file(sf, /):
        'may (() -> metadata4dump_file{.mtime,.size?} | ^FileNotFoundError)'
    @abstractmethod
    def may_query_metadata4data_file(sf, /):
        'may (() -> metadata4data_file{.mtime,.size?} | ^FileNotFoundError)'
    @abstractmethod
    def may_remove_dump_file(sf, /):
        'may (() -> None | ^FileNotFoundError)'

    @abstractmethod
    def source_parser(sf, ifile4data, /):
        '-> raw_data'
    @abstractmethod
    def may_binary_dumper(sf, ofile4dump, raw_data, /):
        'may (ofile4dump -> raw_data -> None)) #<<==may_path4dump_file'
    @abstractmethod
    def may_binary_loader(sf, ifile4dump, /):
        'may (ifile4dump -> raw_data) #<<==may_path4dump_file'
    @abstractmethod
    def transformer(sf, raw_data, /):
        '-> data'

class IDataLoader__details__mixins__pkg_nm_path(IDataLoader__details):
    '[pkg_nm_path4data =[def]= (qnm4pkg4data, bnm4file4data)]'
    __slots__ = ()

    #@property
    #@abstractmethod
    #def may_path4dump_file(sf, /):
    #    '-> Path'

    #@property
    #@abstractmethod
    #def path4data_file(sf, /):
    #    '-> Path'

    @property
    @abstractmethod
    def xencoding4data_file(sf, /):
        '-> xencoding/may_smay_encoding/may str'
    @abstractmethod
    def mk_pkg_nm_path4data(sf, /):
        '-> pkg_nm_path4data/(qnm4pkg4data, bnm4file4data)'
    @abstractmethod
    def mk_may_pkg_nm_path4dump(sf, /):
        '-> may pkg_nm_path4dump/may (qnm4pkg4dump, bnm4file4dump)'

    @override
    def open_ofile4dump(sf, /):
        '-> ofile4dump | ^FileExistsError | ^FileNotFoundError'
        may_pkg_nm_path4dump = sf.mk_may_pkg_nm_path4dump()
        if may_pkg_nm_path4dump is None:
            raise FileNotFoundError
        pkg_nm_path4dump = may_pkg_nm_path4dump
        ofile4dump = _open_ofile4xxx(sf, pkg_nm_path4dump, xencoding=None)
        return ofile4dump
    @override
    def open_ifile4dump(sf, /):
        '-> ifile4dump | ^FileNotFoundError'
        may_pkg_nm_path4dump = sf.mk_may_pkg_nm_path4dump()
        if may_pkg_nm_path4dump is None:
            raise FileNotFoundError
        pkg_nm_path4dump = may_pkg_nm_path4dump
        ifile4dump = _open_ifile4xxx(sf, pkg_nm_path4dump, xencoding=None)
        return ifile4dump
    @override
    def open_ifile4data(sf, /):
        '-> ifile4data | ^FileNotFoundError'
        pkg_nm_path4data = sf.mk_pkg_nm_path4data()
        ifile4data = _open_ifile4xxx(sf, pkg_nm_path4data, xencoding=sf.xencoding4data_file)
        return ifile4data

def _open_ofile4xxx(sf, pkg_nm_path4xxx, /, *, xencoding):
    '-> ofile4xxx | ^FileExistsError'
    #xxx:readonlyIO:ofile4xxx = open_under_pkg_(qnm4pkg4xxx, bnm4file4xxx)
    path4xxx = _path5pkg_nm_path4xxx(pkg_nm_path4xxx, nonexist_vs_exist=False)
        # ^FileExistsError
    ofile4xxx = open4w(path4xxx, force=False, xencoding=xencoding)
    return ofile4xxx



def _open_ifile4xxx(sf, pkg_nm_path4xxx, /, *, xencoding):
    '-> ifile4xxx | ^FileNotFoundError'
    (qnm4pkg4xxx, bnm4file4xxx) = pkg_nm_path4xxx
    if not does_exist_under_pkg_(qnm4pkg4xxx, bnm4file4xxx):
        raise FileNotFoundError(pkg_nm_path4xxx)
    #path4xxx = _path5pkg_nm_path4xxx(pkg_nm_path4xxx, nonexist_vs_exist=True)
        # ^FileNotFoundError
    ifile4xxx = open_under_pkg_(qnm4pkg4xxx, bnm4file4xxx, xencoding=xencoding)
    return ifile4xxx






class IDataLoader__details__mixins__fmtr(IDataLoader__details__mixins__pkg_nm_path):
    __slots__ = ()
    @property
    @abstractmethod
    def qnm4pkg4root(sf, /):
        '-> qnm4pkg4root/str'
    @property
    @abstractmethod
    def qattr4data(sf, /):
        '-> qattr4data/str'

    @property
    @abstractmethod
    def fmtr4relpath4data_file5qattr4data(sf, /):
        '-> IFormatter/asif-str#[relpath4data_file:=fmtr4relpath4data_file5qattr4data.format(qattr4data)]'

    @property
    @abstractmethod
    def fmtr4smay_relpath4dump_file5qattr4data(sf, /):
        '-> IFormatter/asif-str#[smay_relpath4dump_file:=fmtr4smay_relpath4dump_file5qattr4data.format(qattr4data)]'

    @override
    def mk_pkg_nm_path4data(sf, /):
        '-> pkg_nm_path4data/(qnm4pkg4data, bnm4file4data)'

        qnm4pkg4root = sf.qnm4pkg4root
        qattr4data = sf.qattr4data
        fmtr4relpath4data_file5qattr4data = sf.fmtr4relpath4data_file5qattr4data

        m = _mk_may_pkg_nm_path4xxx(qnm4pkg4root, qattr4data, fmtr4relpath4data_file5qattr4data)
        if m is None:
            raise ValueError('relpath4data_file==""')
        (qnm4pkg4data, bnm4file4data) = m
        return m



    @override
    def mk_may_pkg_nm_path4dump(sf, /):
        '-> may pkg_nm_path4dump/may (qnm4pkg4dump, bnm4file4dump)'
        qnm4pkg4root = sf.qnm4pkg4root
        qattr4data = sf.qattr4data
        fmtr4smay_relpath4dump_file5qattr4data = sf.fmtr4smay_relpath4dump_file5qattr4data

        m = _mk_may_pkg_nm_path4xxx(qnm4pkg4root, qattr4data, fmtr4smay_relpath4dump_file5qattr4data)
        if m is None:
            pass
        else:
            (qnm4pkg4dump, bnm4file4dump) = m
        return m


    #@property
    #@override
    #def path4data_file(sf, /):
    #    '-> Path'
    #    dir4pkg = rootdir_5or_qnm4pkg(sf.qnm4pkg4root)
    #    qattr4data = sf.qattr4data
    #    fmtr4relpath4data_file5qattr4data = sf.fmtr4relpath4data_file5qattr4data

    #    relpath4data_file = fmtr4relpath4data_file5qattr4data.format(qattr4data)
    #    check_type_is(str, relpath4data_file)
    #    if not relpath4data_file:raise ValueError('relpath4data_file==""')

    #    path4data_file = dir4pkg / relpath4data_file
    #    return path4data_file

    #@property
    #@override
    #def may_path4dump_file(sf, /):
    #    '-> Path'
    #    dir4pkg = rootdir_5or_qnm4pkg(sf.qnm4pkg4root)
    #    qattr4data = sf.qattr4data
    #    fmtr4smay_relpath4dump_file5qattr4data = sf.fmtr4smay_relpath4dump_file5qattr4data

    #    smay_relpath4dump_file = fmtr4smay_relpath4dump_file5qattr4data.format(qattr4data)
    #    check_type_is(str, smay_relpath4dump_file)

    #    if not smay_relpath4dump_file:
    #        may_path4dump_file = None
    #    else:
    #        relpath4dump_file = smay_relpath4dump_file
    #        path4dump_file = dir4pkg / relpath4dump_file
    #        may_path4dump_file = path4dump_file
    #    may_path4dump_file

    #    return may_path4dump_file
def _mk_may_pkg_nm_path4xxx(qnm4pkg4root, qattr4data, fmtr4smay_relpath4xxx_file5qattr4data, /):
    '-> may (qnm4pkg4xxx, bnm4file4xxx)'
    smay_relpath4xxx_file = fmtr4smay_relpath4xxx_file5qattr4data.format(qattr4data)
    check_type_is(str, smay_relpath4xxx_file)
    if not smay_relpath4xxx_file:
        return None
        raise ValueError('relpath4xxx_file==""')
    relpath4xxx_file = smay_relpath4xxx_file

    relpath4xxx_file = Path(relpath4xxx_file)
    [*nms, bnm4file4xxx] = relpath4xxx_file.parts
    if not all(map(str.isidentifier, nms)): raise ValueError(relpath4xxx_file)
    nms.insert(0, qnm4pkg4root)
    qnm4pkg4xxx = '.'.join(nms)
    return (qnm4pkg4xxx, bnm4file4xxx)
if 0b000:
    IDataLoader__details__mixins__fmtr()
        #fmtr4relpath4data_file5qattr4data, fmtr4smay_relpath4dump_file5qattr4data, may_binary_dumper, may_binary_loader, qattr4data, qnm4pkg4root, source_parser, transformer, xencoding4data_file
        #-->
        #fmtr4relpath4data_file5qattr4data, fmtr4smay_relpath4dump_file5qattr4data, may_binary_dumper, may_binary_loader, qattr4data, qnm4pkg4root, source_parser, transformer, xencoding4data_file
        #++may_query_metadata4data_file, may_query_metadata4dump_file, may_remove_dump_file
class DataLoader__details__mixins__fmtr(IDataLoader__details__mixins__fmtr):
    ___no_slots_ok___ = True
    def __init__(sf, /, *, mk__fmtr4relpath4data_file, mk__fmtr4smay_relpath4dump_file, qattr4data, qnm4pkg4root, source_parser_, transformer_, xencoding4data_file):
        d = {**locals()}
        del d['sf']
        if 0:
            if (ks := d.keys() & sf.__dict__.keys()):raise Exception(ks)
            sf.__dict__.update(d)
        else:
            sf._d = d

    def __repr__(sf, /):
        return repr_helper(sf, **sf._d)
    @override
    def may_binary_dumper(sf, ofile4dump, raw_data, /):
        'may (ofile4dump -> raw_data -> None)) #<<==may_path4dump_file'
        pickle.dump(raw_data, ofile4dump)
    @override
    def may_binary_loader(sf, ifile4dump, /):
        'may (ofile4dump -> raw_data) #<<==may_path4dump_file'
        raw_data = pickle.load(ifile4dump)
        return raw_data

    @override
    def may_query_metadata4dump_file(sf, /):
        'may (() -> metadata4dump_file{.mtime,.size?} | ^FileNotFoundError)'
        may_pkg_nm_path4dump = sf.mk_may_pkg_nm_path4dump()
        if may_pkg_nm_path4dump is None:
            raise FileNotFoundError
        pkg_nm_path4dump = may_pkg_nm_path4dump
        metadata4dump_file = _query_metadata4xxx_file(pkg_nm_path4dump)
        return metadata4dump_file
    @override
    def may_query_metadata4data_file(sf, /):
        'may (() -> metadata4data_file{.mtime,.size?} | ^FileNotFoundError)'
        pkg_nm_path4data = sf.mk_pkg_nm_path4data()
        metadata4data_file = _query_metadata4xxx_file(pkg_nm_path4data)
        return metadata4data_file
    @override
    def may_remove_dump_file(sf, /):
        'may (() -> None | ^FileNotFoundError)'
        may_pkg_nm_path4dump = sf.mk_may_pkg_nm_path4dump()
        if may_pkg_nm_path4dump is None:
            raise FileNotFoundError
        pkg_nm_path4dump = may_pkg_nm_path4dump
        _remove_xxx_file(pkg_nm_path4dump)
        return
    ######################
    ######################
    ######################

    def _getattr(sf, nm, /):
        return sf._d[nm]

    ######################
    ######################
    ######################
    @property
    @override
    def qnm4pkg4root(sf, /):
        '-> qnm4pkg4root/str'
        return sf._getattr('qnm4pkg4root')
    @property
    @override
    def qattr4data(sf, /):
        '-> qattr4data/str'
        return sf._getattr('qattr4data')

    ######################
    ######################
    ######################
    @property
    @override
    def fmtr4relpath4data_file5qattr4data(sf, /):
        '-> IFormatter/asif-str#[relpath4data_file:=fmtr4relpath4data_file5qattr4data.format(qattr4data)]'
        mk__fmtr4relpath4data_file = sf._getattr('mk__fmtr4relpath4data_file')
        fmtr4relpath4data_file5qattr4data = mk__fmtr4relpath4data_file(sf)
        return fmtr4relpath4data_file5qattr4data

    @property
    @override
    def fmtr4smay_relpath4dump_file5qattr4data(sf, /):
        '-> IFormatter/asif-str#[smay_relpath4dump_file:=fmtr4smay_relpath4dump_file5qattr4data.format(qattr4data)]'
        mk__fmtr4smay_relpath4dump_file = sf._getattr('mk__fmtr4smay_relpath4dump_file')
        fmtr4smay_relpath4dump_file5qattr4data = mk__fmtr4smay_relpath4dump_file(sf)
        return fmtr4smay_relpath4dump_file5qattr4data


    @property
    @override
    def xencoding4data_file(sf, /):
        '-> xencoding/may_smay_encoding/may str'
        return sf._getattr('xencoding4data_file')

    @override
    def source_parser(sf, ifile4data, /):
        '-> raw_data'
        source_parser_ = sf._getattr('source_parser_')
        if source_parser_ is None:
            bs_or_txt = ifile4data.read()
            raw_data = bs_or_txt
        else:
            raw_data = source_parser_(sf, ifile4data)
        return raw_data

    @override
    def transformer(sf, raw_data, /):
        '-> data'
        transformer_ = sf._getattr('transformer_')
        if transformer_ is None:
            data = raw_data
        else:
            data = transformer_(sf, raw_data)
        return data

class TooManyFileFoundError(OSError):pass
class Formatter__glob(IFormatter):
    ___no_slots_ok___ = True
    @override
    def format(sf, x, /):
        '-> str'
        rootdir = sf._rootdir
        fmt4glob_pattern = sf._fmt4glob_pattern
        fmt_args5arg = sf._fmt_args5arg

        args = fmt_args5arg(x)
        glob_pattern = fmt4glob_pattern.format(*args)
        paths = iter(rootdir.glob(glob_pattern))
        for path in paths:
            break
        else:
            raise FileNotFoundError(x, rootdir, glob_pattern)
            raise LookupError(x, rootdir, glob_pattern)
        for path1 in paths:
            raise TooManyFileFoundError(x, rootdir, glob_pattern, [path, path1])
        relpath = path.relative_to(rootdir).as_posix()
        #relpath = PurePosixPath(path.relative_to(rootdir))
        #PurePosixPath(path.relative_to(root))

        return relpath
    def __init__(sf, rootdir, fmt4glob_pattern, fmt_args5arg, /):
        sf._rootdir = Path(rootdir)
        sf._fmt4glob_pattern = fmt4glob_pattern
        sf._fmt_args5arg = fmt_args5arg

def _remove_xxx_file(pkg_nm_path4xxx, /):
    path4xxx = _path5pkg_nm_path4xxx(pkg_nm_path4xxx, nonexist_vs_exist=True)
        # ^FileNotFoundError
    os.remove(path4xxx)
def _query_metadata4xxx_file(pkg_nm_path4xxx, /):
    '(qnm4pkg4xxx, bnm4file4xxx) -> metadata4data_file{.mtime,.size?} | ^FileNotFoundError'
    path4xxx = _path5pkg_nm_path4xxx(pkg_nm_path4xxx, nonexist_vs_exist=True)
        # ^FileNotFoundError
    #mtime = os.stat(path4xxx).st_mtime
    mtime = os.path.getmtime(path4xxx)
    metadata4xxx_file = dict(mtime=mtime)
    return metadata4xxx_file

def _path5pkg_nm_path4xxx(pkg_nm_path4xxx, /, *, nonexist_vs_exist):
    '-> path4xxx | ^(FileNotFoundError if nonexist_vs_exist else FileExistsError)'
    (qnm4pkg4xxx, bnm4file4xxx) = pkg_nm_path4xxx
    if not does_exist_under_pkg_(qnm4pkg4xxx, bnm4file4xxx):
        #not exist
        if nonexist_vs_exist:
            #expect exist
            raise FileNotFoundError(pkg_nm_path4xxx)
    else:
        #exist
        if not nonexist_vs_exist:
            #expect nonexist
            raise FileExistsError(pkg_nm_path4xxx)

    dir4pkg4xxx = rootdir_5or_qnm4pkg(qnm4pkg4xxx)
    path4xxx = dir4pkg4xxx / bnm4file4xxx
    return path4xxx




def _mk__fmtr4relpath4data_file(sf, /):
    qnm4pkg4root = sf.qnm4pkg4root
    qattr4data = sf.qattr4data
    def fmt_args5arg(qattr4data, /):
        return [qattr4data.replace('.', '/')]

    rootdir = rootdir_5or_qnm4pkg(qnm4pkg4root)
    fmt4glob_pattern = '{}.*.ver*.out.txt'
    fmtr = Formatter__glob(rootdir, fmt4glob_pattern, fmt_args5arg)
    return fmtr
def _mk__fmtr4smay_relpath4dump_file(sf, /):
    qnm4pkg4root = sf.qnm4pkg4root
    qattr4data = sf.qattr4data
    def fmt_args5arg(qattr4data, /):
        return [qattr4data]
        return ('__pycache__', qattr4data.replace('.', '/'))

    rootdir = rootdir_5or_qnm4pkg(qnm4pkg4root)
    fmt4glob_pattern = '__pycache__/{}.pickle.dump'
    fmtr = Formatter__glob(rootdir, fmt4glob_pattern, fmt_args5arg)
    return fmtr


DataLoader__details__mixins__fmtr(
mk__fmtr4relpath4data_file
=_mk__fmtr4relpath4data_file
, mk__fmtr4smay_relpath4dump_file
=_mk__fmtr4smay_relpath4dump_file
, qattr4data
='ver14_0_0.age'
, qnm4pkg4root
='nn_ns.CJK.unicode.ucd_unihan.xml'
, source_parser_
=lambda sf, ifile4data, /:literal_eval(ifile4data.read())
, transformer_
=None
, xencoding4data_file
='u8'
)
class Maker4DataLoader__details__mixins__fmtr(IDataLoaderMaker):
    'see:DataLoader__details__mixins__fmtr'
    ___no_slots_ok___ = True
    def __init__(sf, /, *, mk__fmtr4relpath4data_file, mk__fmtr4smay_relpath4dump_file, source_parser_, transformer_, xencoding4data_file):
        d = {**locals()}
        del d['sf']
        sf._d = d

    def __repr__(sf, /):
        return repr_helper(sf, **sf._d)
    @override
    def mk_data_loader(sf, qnm4pkg4root, qattr4data, /):
        'qnm4pkg4root -> qattr4data -> data_loader'
        return DataLoader__details__mixins__fmtr(**sf._d
        , qattr4data=qattr4data
        , qnm4pkg4root=qnm4pkg4root
        )

def mk_data_loader5attr__ver2_IDataLoaderMaker(qnm4data_loader, qnm4pkg4root, mkr4data_loader:IDataLoaderMaker, /, *, viewer=None, no_cache=False, imay_max_depth=-1):
    #-> _DataLoader___autocall_at_max_depth
    #mk_data_loader5attr__ver1_params
    check_int_ge(-1, imay_max_depth)
    if imay_max_depth == 0:raise Exception

    check_pseudo_qual_name(qnm4data_loader)
    check_pseudo_qual_name(qnm4pkg4root)

    call = _Call4DataLoader5attr__ver2_IDataLoaderMaker(qnm4pkg4root, mkr4data_loader, viewer=viewer, no_cache=no_cache)
    data_loader = DottedAttrCollector(call, qnm4data_loader, (), echo)

    _data_loader = _DataLoader___autocall_at_max_depth(data_loader, imay_max_depth)
    return _data_loader
_DataLoader___autocall_at_max_depth




######################
#ver2:above
######################
######################
######################
######################
#ver1:below
######################

def dir5qnm4pkg(qnm4pkg, /):
    pkg = import_module(qnm4pkg)
    if not is_pkg_(pkg):raise TypeError(qnm4pkg)
    m = pkg.__file__
    if not m is None:
        __init__6py = m
        assert __init__6py.name == '__init__.py'
        dir4pkg = __init__6py.parent
    else:
        paths = pkg.__path__
        if not len(paths) == 1:raise Exception(qnm4pkg, paths)
        dir4pkg = paths[0]
    return Path(dir4pkg)
def rootdir_5or_qnm4pkg(rootdir_or_qnm4pkg, /):
    if (not type(rootdir_or_qnm4pkg) is str) or '/' in rootdir_or_qnm4pkg:
        '/:./:../'
        rootdir = rootdir_or_qnm4pkg
    else:
        qnm4pkg = rootdir_or_qnm4pkg
        rootdir = dir5qnm4pkg(qnm4pkg)
    rootdir
    rootdir = Path(rootdir)
    if not rootdir.exists():raise FileNotFoundError(rootdir)
    if not rootdir.is_dir():raise NotADirectoryError(rootdir)
    return rootdir
#def mk_data_loader5attr__ver1_params(qnm4data_loader, rootdir_or_qnm4pkg, qattr4data_to_basename4datafile, /, *, xencoding, parser=None, no_cache=False, viewer=None, imay_max_depth=-1):
def mk_data_loader5attr__ver1_params(qnm4data_loader, qnm4pkg, qattr4data_to_basename4datafile, /, *, xencoding, extended=False, extended_transformer=False, parser=None, no_cache=False, transformer=None, viewer=None, imay_max_depth=-1):
    #-> _DataLoader___autocall_at_max_depth
    #mk_data_loader5attr__ver2_IDataLoaderMaker
    r'''[[[
    [no_cache == False]:
        using internal cache
    [no_cache == True]:
        forwarding
        using external cache

    [extended == False]:
        [qattr4data_to_basename4datafile :: qattr4data -> basename4datafile]
    [extended == True]:
        [qattr4data_to_basename4datafile :: qnm4pkg -> qattr4data -> (qnm4new_pkg, basename4datafile)]

    [xencoding :: may smay encoding]
    [xencoding == (None|'')]:
        [bs_or_txt :: bytes]
    [xencoding == encoding]:
        [bs_or_txt :: str]


    [parser :: bs_or_txt -> data0]

    [extended_transformer == False]:
        [transformer :: data0 -> data1]
    [extended_transformer == True]:
        [transformer :: qnm4pkg -> qattr4data -> qnm4new_pkg -> basename4datafile -> data0 -> data1]

    [viewer :: data1 -> readonly__data1]

    #]]]'''#'''
    #
    check_int_ge(-1, imay_max_depth)
    if imay_max_depth == 0:raise Exception

    check_pseudo_qual_name(qnm4data_loader)
    #rootdir = rootdir_5or_qnm4pkg(rootdir_or_qnm4pkg)
    call = _Call4DataLoader5attr__ver1_params(qnm4pkg, qattr4data_to_basename4datafile, xencoding=xencoding, extended=extended, extended_transformer=extended_transformer, parser=parser, no_cache=no_cache, transformer=transformer, viewer=viewer)
    data_loader = DottedAttrCollector(call, qnm4data_loader, (), echo)
    #if imay_max_depth > 0:
    if 1:
        #now callable# !! not callable ==>> [imay_max_depth > 0]
        #now: ++kw:imay_max_depth
        _data_loader = _DataLoader___autocall_at_max_depth(data_loader, imay_max_depth)
    return _data_loader
_DataLoader___autocall_at_max_depth


_may_nm2parser = (
{None:literal_eval
,'literal_eval':literal_eval
,'safe_eval':safe_eval
,'eval':eval
,'echo':echo
})
_g_viewer = default_cfg4RecurView.to_view
class _Call4DataLoader5attr__ver1_params:
    def __call__(sf, data_loader:DottedAttrCollector, /):
        'DottedAttrCollector -> data_view'
        qnm4pkg = sf._qnm4pkg
        qattr = type(data_loader).__mk_qname4attr__(data_loader)

        Nothing = []
        if not sf._no_cache and not Nothing is (data_view := sf._qattr2data_view.get(qattr, Nothing)):
            #data_view = sf._qattr2data_view[qattr]
            return data_view

        if not sf._extended:
            bnm = basename4datafile = sf._qattr2bnm(qattr)
            qnm4new_pkg = qnm4pkg
        else:
            (qnm4new_pkg, bnm) = basename4datafile = sf._qattr2bnm(qnm4pkg, qattr)
        qnm4new_pkg
        bnm
        bs_or_txt = read_under_pkg_(qnm4new_pkg, bnm, xencoding=sf._xencoding)
        _1_data = sf._parser(bs_or_txt)
        if sf._extended_transformer:
            _2_data = sf._transformer(qnm4pkg, qattr, qnm4new_pkg, bnm, _1_data)
        else:
            _2_data = sf._transformer(qnm4new_pkg, qattr, bnm, _1_data)
        _2_data
        data_view = sf._viewer(_2_data)
        if not sf._no_cache:
            sf._qattr2data_view[qattr] = data_view
        return data_view

    def __init__(sf, qnm4pkg, qattr4data_to_basename4datafile, /, *, xencoding, extended=False, extended_transformer=False, parser=None, no_cache=False, transformer=None, viewer=None):
        '#[parser:None-->literal_eval]'
        check_type_is(bool, extended)
        check_type_is(bool, extended_transformer)
        check_type_is(bool, no_cache)
        check_pseudo_qual_name(qnm4pkg)
        if qattr4data_to_basename4datafile is None:
            qattr4data_to_basename4datafile = echo if not extended else echo_args
        check_callable(qattr4data_to_basename4datafile)


        if parser is None or type(parser) is str:
            may_nm4parser = parser
            parser = _may_nm2parser[may_nm4parser]
        check_callable(parser)

        if transformer is None:
            transformer = echo if not extended_transformer else echo_args
        check_callable(transformer)

        if viewer is None:
            viewer = _g_viewer
        check_callable(viewer)

        if xencoding is None:
            xencoding = ''
                #binary!
        check_type_is(str, xencoding)



        sf._extended = extended
        sf._extended_transformer = extended_transformer
        sf._qnm4pkg = qnm4pkg
        sf._qattr2bnm = qattr4data_to_basename4datafile
        sf._xencoding = xencoding

        sf._parser = parser
        sf._no_cache = no_cache
        sf._transformer = transformer
        sf._viewer = viewer
        if not no_cache:
            sf._qattr2data_view = {}
#end-class _Call4DataLoader5attr__ver1_params:

class _Call4DataLoader5attr__ver2_IDataLoaderMaker:
    def __call__(sf, data_loader:DottedAttrCollector, /):
        'DottedAttrCollector -> data_view'
        mkr4data_loader = sf._mkr4data_loader
        qnm4pkg4root = sf._qnm4pkg4root
        qattr4data = type(data_loader).__mk_qname4attr__(data_loader)


        Nothing = []
        if not sf._no_cache and not Nothing is (data_view := sf._qattr2data_view.get(qattr4data, Nothing)):
            return data_view

        data_loader = mkr4data_loader.mk_data_loader(qnm4pkg4root, qattr4data)
        _2_data = data_loader.load()
        data_view = sf._viewer(_2_data)
        if not sf._no_cache:
            sf._qattr2data_view[qattr4data] = data_view
        return data_view

    def __init__(sf, qnm4pkg4root, mkr4data_loader, /, *, viewer=None, no_cache=False):
        '#[parser:None-->literal_eval]'
        check_type_le(IDataLoaderMaker, mkr4data_loader)
        check_type_is(bool, no_cache)
        check_pseudo_qual_name(qnm4pkg4root)
        if viewer is None:
            viewer = _g_viewer
        check_callable(viewer)


        sf._viewer = viewer
        sf._mkr4data_loader = mkr4data_loader
        sf._qnm4pkg4root = qnm4pkg4root
        sf._no_cache = no_cache
        if not no_cache:
            sf._qattr2data_view = {}
#end-class _Call4DataLoader5attr__ver2_IDataLoaderMaker:



__all__
from seed.pkg_tools.load_data5attr import mk_data_loader5attr__ver1_params
from seed.pkg_tools.load_data5attr import rootdir_5or_qnm4pkg, dir5qnm4pkg
from seed.pkg_tools.load_data5attr import *
