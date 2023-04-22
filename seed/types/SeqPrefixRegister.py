#__all__:goto
r'''[[[
e ../../python3_src/seed/types/SeqPrefixRegister.py
    view ../../python3_src/seed/pkg_tools/load_resources.py
from seed.pkg_tools.load_resources import IFileReader, IFileReader__using_importlib_resources, IFileReaderMaker, MainFuncs, a_FileReaderMakerRegister, TextReaderMaker, text_reader_mkr4gb, text_reader_mkr4u8, binary_reader_mkr





seed.types.SeqPrefixRegister
py -m nn_ns.app.debug_cmd   seed.types.SeqPrefixRegister
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.types.SeqPrefixRegister   @f
py -m nn_ns.app.doctest_cmd seed.types.SeqPrefixRegister:__doc__ -v

from seed.types.SeqPrefixRegister import MainFuncs, a_FileReaderMakerRegister, TextReaderMaker, text_reader_mkr4gb, text_reader_mkr4u8, binary_reader_mkr
    #最简单应用:读字节、读utf8

from seed.types.SeqPrefixRegister import IFileReader, IFileReader__using_importlib_resources
    #首先，具象化IFileReader
from seed.types.SeqPrefixRegister import IFileReaderMaker
    #其次，具象化IFileReaderMaker=>实例化IFileReader
from seed.types.SeqPrefixRegister import MainFuncs, a_FileReaderMakerRegister
    #默认注册处:共享必要
    #再次，注册加载器+后缀名绑定加载器
    #   MainFuncs.register__def
    #   MainFuncs.register__ref
    #最后，加载数据
    #   MainFuncs.read_tmay(qname4pkg, basename4rsc)






view ../../python3_src/py_stdlib_api.txt
    see:[自定义模块导入囗囗概要]
用途:
    比如说:注册使用文件后缀名
    register(文件后缀名,解码器)
        importlib.resources.read_binary(__package__, basename4resource)->bytes
        FileFinder.path_hook :: *loader_details -> (path->PathEntryFinder|^ImportError)
        loader_details :: [(mk_loader,[suffix])]
        mk_loader :: qname -> path -> Loader
        importlib.machinery:
            FileFinder
            ===
            SOURCE_SUFFIXES
            BYTECODE_SUFFIXES
            EXTENSION_SUFFIXES
            ===
            SourceFileLoader <: SourceLoader&FileLoader
            SourcelessFileLoader <: FileLoader
            ExtensionFileLoader <: ExecutionLoader
            ===
    register(文件后缀名,解码器)
        拆分改进:
            *命名解码器--->register__def(模块名,解码器名,解码器)
                ==>>谁命名解码器为何名
            *赋予后缀名语义--->register__ref(包前缀限定,文件后缀名,模块名,解码器名)
                ==>>包前缀限定 目下，如何使用 文件后缀名
    ==>>需要这样一种容器:
        待命名容器<{包前缀限定:{文件后缀名:(模块名,解码器名)}}>
        待命名容器<{包前缀限定:v}>
            .枚举所有匹配的包前缀限定囗囗长度递降(模块名)->Iter<(包前缀限定,v)>





importlib.resources.open_binary(package, resource)->BinaryIO
importlib.resources.open_text(package, resource, encoding='utf-8', errors='strict')->TextIO
importlib.resources.read_binary(package, resource)->bytes
importlib.resources.read_text(package, resource, encoding='utf-8', errors='strict')->str
  虚拟路径、基本文件名
  package = pkg_qname|pkg_obj
  resource :: basename
      it may not contain path separators
      it may not have sub-resources (i.e. it cannot be a directory).
importlib.resources.contents(package)->Iter<name/resource-or-not>#目录
importlib.resources.is_resource(package, name)->bool

sys.path_hooks :: [((str|bytes)->(PathEntryFinder|^ImportError))]
PathEntryFinder
  .find_spec(fullname, target=None)->may spec

importlib.util.spec_from_file_location(name, location, *, loader=None, submodule_search_locations=None)->spec
importlib.util.spec_from_loader(name, loader, *, origin=None, is_package=None)->spec



>>> d = SeqPrefixRegister__using_mapping()
>>> d
SeqPrefixRegister__using_mapping()
>>> d['123abcdef'] = 9999
>>> d['12345678'] = 888
>>> d['123'] = 333
>>> d['1'] = 111
>>> d._root
_Node('1', _Node('23', {'4': _Node('5678', None, ('12345678', 888)), 'a': _Node('bcdef', None, ('123abcdef', 9999))}, ('123', 333)), ('1', 111))
>>> d[''] = 0
>>> d._root
_Node('', _Node('1', _Node('23', {'4': _Node('5678', None, ('12345678', 888)), 'a': _Node('bcdef', None, ('123abcdef', 9999))}, ('123', 333)), ('1', 111)), ('', 0))
>>> d['a'] = 1111
>>> d['abc'] = 3333
>>> d['12'] = 222
>>> d['1234'] = 444
>>> d['12345'] = 555
>>> d['1234a'] = 5555
>>> d['1234ab'] = 6666
>>> d['1234xyz'] = 6666
>>> d['1234uvw'] = 6666
>>> d
SeqPrefixRegister__using_mapping([('123abcdef', 9999), ('12345678', 888), ('1234xyz', 6666), ('1234uvw', 6666), ('1234ab', 6666), ('12345', 555), ('1234a', 5555), ('1234', 444), ('123', 333), ('abc', 3333), ('12', 222), ('1', 111), ('a', 1111), ('', 0)])
>>> d._root
_Node('', _Node('', {'a': _Node('', _Node('bc', None, ('abc', 3333)), ('a', 1111)), '1': _Node('', _Node('2', _Node('3', {'4': _Node('', _Node('', {'a': _Node('', _Node('b', None, ('1234ab', 6666)), ('1234a', 5555)), '5': _Node('', _Node('678', None, ('12345678', 888)), ('12345', 555)), 'x': _Node('yz', None, ('1234xyz', 6666)), 'u': _Node('vw', None, ('1234uvw', 6666))}, None), ('1234', 444)), 'a': _Node('bcdef', None, ('123abcdef', 9999))}, ('123', 333)), ('12', 222)), ('1', 111))}, None), ('', 0))













../../python3_src/seed/__README__.txt
../../python3_src/seed/__pycache__/__init__.cpython-38.pyc


>>> type(a_FileReaderMakerRegister)
<class 'seed.types.SeqPrefixRegister.FileReaderMakerRegister'>
>>> a_FileReaderMakerRegister = FileReaderMakerRegister()
>>> a_FileReaderMakerRegister
FileReaderMakerRegister()

>>> a_FileReaderMakerRegister.register__def(__name__, 'u8', a_FileReaderMaker__u8)
>>> a_FileReaderMakerRegister.register__def(__name__, 'raw', a_FileReaderMaker__raw)
>>> a_FileReaderMakerRegister
FileReaderMakerRegister([('seed.types.SeqPrefixRegister', [('raw', FileReaderMaker__()), ('u8', FileReaderMaker__u8())])])


>>> pkg = 'seed'
>>> a_FileReaderMakerRegister.register__ref(pkg, '.txt', __name__, 'u8')
>>> a_FileReaderMakerRegister.register__ref(pkg, '.pyc', __name__, 'raw')
>>> a_FileReaderMakerRegister
FileReaderMakerRegister([('seed.types.SeqPrefixRegister', [('raw', FileReaderMaker__()), ('u8', FileReaderMaker__u8())])], [('seed', [('.pyc', 'seed.types.SeqPrefixRegister', 'raw'), ('.txt', 'seed.types.SeqPrefixRegister', 'u8')])])


>>> a_FileReaderMakerRegister.read_tmay(pkg, '__README__.txt')
('\nshould not import nn_ns\n\n',)
>>> a_FileReaderMakerRegister.read_tmay(pkg, '__pycache__/__init__.cpython-38.pyc')
Traceback (most recent call last):
    ...
ValueError: '__pycache__/__init__.cpython-38.pyc' must be only a file name
>>> a_FileReaderMakerRegister.read_tmay(f'{pkg}.__pycache__', '__init__.cpython-38.pyc')
(b'U\r\r\n\x00\x00\x00\x00R\x9b\x03_\x00\x00\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00@\x00\x00\x00s\x04\x00\x00\x00d\x00S\x00)\x01N\xa9\x00r\x01\x00\x00\x00r\x01\x00\x00\x00r\x01\x00\x00\x00\xfa8/sdcard/0my_files/git_repos/python3_src/seed/__init__.py\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00',)





TextReader
TextReaderMaker
text_reader_mkr4gb
text_reader_mkr4u8
binary_reader_mkr

>>> a_FileReaderMakerRegister.register__def(__name__, 'gb', TextReaderMaker('gb18030'))
>>> a_FileReaderMakerRegister.register__def(__name__, 'utf8', TextReaderMaker('utf8'))
>>> a_FileReaderMakerRegister.register__def(__name__, 'binary', TextReaderMaker(''))

>>> a_FileReaderMakerRegister.register__ref(pkg, '.gb', __name__, 'gb')
>>> a_FileReaderMakerRegister.register__ref(pkg, '.u8', __name__, 'utf8')
>>> a_FileReaderMakerRegister.register__ref(pkg, '.dat', __name__, 'binary')


view ++enc=gb18030 ../../python3_src/seed/types/SeqPrefixRegister.py.testing-data.gb
view ++enc=utf8 ../../python3_src/seed/types/SeqPrefixRegister.py.testing-data.u8
view ++enc=utf16le ../../python3_src/seed/types/SeqPrefixRegister.py.testing-data.dat
测试中文编码

>>> a_FileReaderMakerRegister
FileReaderMakerRegister([('seed.types.SeqPrefixRegister', [('binary', TextReaderMaker('')), ('gb', TextReaderMaker('gb18030')), ('raw', FileReaderMaker__()), ('u8', FileReaderMaker__u8()), ('utf8', TextReaderMaker('utf8'))])], [('seed', [('.dat', 'seed.types.SeqPrefixRegister', 'binary'), ('.gb', 'seed.types.SeqPrefixRegister', 'gb'), ('.pyc', 'seed.types.SeqPrefixRegister', 'raw'), ('.txt', 'seed.types.SeqPrefixRegister', 'u8'), ('.u8', 'seed.types.SeqPrefixRegister', 'utf8')])])






>>> a_FileReaderMakerRegister.read_tmay(__package__, 'SeqPrefixRegister.py.testing-data.gb')
('e ++enc=gb18030 ../../python3_src/seed/types/SeqPrefixRegister.py.testing-data.gb\n测试中文编码\n\n',)

>>> a_FileReaderMakerRegister.read_tmay(__package__, 'SeqPrefixRegister.py.testing-data.u8')
('e ++enc=utf8 ../../python3_src/seed/types/SeqPrefixRegister.py.testing-data.u8\n测试中文编码\n',)

>>> a_FileReaderMakerRegister.read_tmay(__package__, 'SeqPrefixRegister.py.testing-data.dat')
(b'e\x00 \x00+\x00+\x00e\x00n\x00c\x00=\x00u\x00t\x00f\x001\x006\x00l\x00e\x00 \x00.\x00.\x00/\x00.\x00.\x00/\x00p\x00y\x00t\x00h\x00o\x00n\x003\x00_\x00s\x00r\x00c\x00/\x00s\x00e\x00e\x00d\x00/\x00t\x00y\x00p\x00e\x00s\x00/\x00S\x00e\x00q\x00P\x00r\x00e\x00f\x00i\x00x\x00R\x00e\x00g\x00i\x00s\x00t\x00e\x00r\x00.\x00p\x00y\x00.\x00t\x00e\x00s\x00t\x00i\x00n\x00g\x00-\x00d\x00a\x00t\x00a\x00.\x00d\x00a\x00t\x00\n\x00Km\xd5\x8b-N\x87e\x16\x7f\x01x\n\x00',)







#]]]'''
#from seed.types.SeqPrefixRegister import
__all__ = r'''
PrefixLookupError
    PrefixLookupError__existed
    PrefixLookupError__nonexisted

ISeqPrefixRegister
    ISeqPrefixRegister__using_mapping
    SeqPrefixRegister__using_mapping






QualNamePrefixRegister
ISeqPrefixRegister__default_target
    IQualNamePrefixRegister__default_target
    QualNamePrefixRegister__default_target_is_dict




check_file_suffix
sort__len_desc
LoadError

IBaseFileLoaderMakerRegister
    FileReaderMakerRegister
        a_FileReaderMakerRegister
MainFuncs

IFileReaderMaker
    FileReaderMaker__
    FileReaderMaker__raw
        a_FileReaderMaker__raw
    FileReaderMaker__u8
        a_FileReaderMaker__u8
    TextReaderMaker
        text_reader_mkr4gb
        text_reader_mkr4u8
        binary_reader_mkr
IFileReader
    IFileReader__using_importlib_resources
        FileReader__using_importlib_resources__functional

        FileReader__using_importlib_resources__
        FileReader__using_importlib_resources__raw
        FileReader__using_importlib_resources__u8

        TextReader

'''.split()#'''
    #_Node
__all__

def _():
    from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError

#from seed.tiny_.dict__add_fmap_filter import fmap4dict_value, group4dict_value#, filter4dict_value, dict_add__is, dict_add__eq, dict_add__new
from seed.tiny_.mk_fdefault import mk_default
    #def mk_default(imay_xdefault_rank, xdefault, /,*args4xdefault):
from seed.tiny_.check import check_pseudo_qual_name, check_pseudo_identifier, check_callable#, check_smay_pseudo_qual_name
from seed.helper.repr_input import repr_helper
from seed.abc.IReprHelper import IReprHelper
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import check_type_is, check_type_le, check_tmay, inf, null_tuple
#from seed.tiny import fst, snd, at
from seed.seq_tools.is_prefix_of_seq import is_prefix_of_seq as _is_prefix_of_seq_#, is_suffix_of_seq
#from seed.seq_tools.is_prefix_of_seq import seq_starts_with, seq_ends_with
from seed.seq_tools.lcp_of import lcp_of as _lcp_of_#, len_lcp_of
from seed.seq_tools.lcp_of import len_lcp_of_ex as _len_lcp_of_ex_#, view_seq_ex


from collections.abc import Sequence
from operator import __lt__, __le__
import sys
import os.path
import importlib.abc
import importlib.util
import importlib.machinery
import importlib.resources

os.path.join
os.path.exists




class PrefixLookupError(LookupError):pass
class PrefixLookupError__existed(PrefixLookupError):pass
class PrefixLookupError__nonexisted(PrefixLookupError):pass

class ISeqPrefixRegister(ABC):
    'len_asc vs len_desc <<== asc/ascend vs desc/descend'
    __slots__ = ()

    @abstractmethod
    def _register_at_seq_(sf, xs, tgt, /):
        '[x] -> tgt -> None|^PrefixLookupError__existed'
    @abstractmethod
    def _iter_prefix_target_pairs_of_(sf, xs, /, *, len_asc):
        '[x] -> *len_asc/bool -> Iter ([x], tgt)'
    @abstractmethod
    def _iter_all_prefix_target_pairs_(sf, /, *, len_asc):
        '*len_asc/bool -> Iter ([x], tgt)'
    @abstractmethod
    def _set_xdefault5registered_(sf, xs, fdefault, /):
        '[x] -> (()->tgt) -> tgt'
        try:
            return sf[xs]
        except PrefixLookupError__nonexisted:
            tgt = fdefault()
            sf[xs] = tgt
            return sf[xs]
    #@abstractmethod
    def _get_tmay5registered_(sf, xs, /):
        '[x] -> tmay tgt|^TypeError'
        it = sf.iter_prefix_target_pairs_of(xs, len_asc=False)
        for ys, tgt in it:
            break
        else:
            return null_tuple
        if len(ys) == len(xs):
            return null_tuple
        return (tgt,)
    #def _get_len_of_longest_prefix_(sf, /):
    def _check_seq_type_(sf, xs, /):
        '[x] -> None|^TypeError'
        check_type_le(Sequence, xs)
    def _check_target_type_(sf, tgt, /):
        'tgt -> None|^TypeError'
        return
    def __setitem__(sf, xs, tgt, /):
        '[x] -> tgt -> None|^PrefixLookupError__existed|^TypeError'
        sf._check_seq_type_(xs)
        sf._check_target_type_(tgt)
        return sf._register_at_seq_(xs, tgt)
    def __getitem__(sf, xs, /):
        '[x] -> tgt|^PrefixLookupError__nonexisted|^TypeError'
        tmay_tgt = sf.get_tmay5registered(xs)
        if not tmay_tgt:
            raise PrefixLookupError__nonexisted(xs)
        [tgt] = tmay_tgt
        return tgt
    def __contains__(sf, xs, /):
        '[x] -> bool|^TypeError'
        tmay_tgt = sf.get_tmay5registered(xs)
        return bool(tmay_tgt)
    def get_tmay5registered(sf, xs, /):
        '[x] -> tmay tgt|^TypeError'
        sf._check_seq_type_(xs)
        tmay_tgt = sf._get_tmay5registered_(xs)
        check_tmay(tmay_tgt)
        return tmay_tgt
    def get_xdefault5registered(sf, xs, imay_xdefault_rank, xdefault, /):
        '[x] -> imay_xdefault_rank -> xdefault -> tgt'
        tmay_tgt = sf.get_tmay5registered(xs)
        if not tmay_tgt:
            default = mk_default(imay_xdefault_rank, xdefault, sf, xs)
                #may not be tgt
                #   neeednot check
            return default
        [tgt] = tmay_tgt
        return tgt
    def set_xdefault5registered(sf, xs, imay_xdefault_rank, xdefault, /):
        '[x] -> imay_xdefault_rank -> xdefault -> tgt'
        sf._check_seq_type_(xs)
        def fdefault():
            tgt = mk_default(imay_xdefault_rank, xdefault, sf, xs)
                #must be tgt
                #   neeednot check
            sf._check_target_type_(tgt)
            return tgt
        tgt = sf._set_xdefault5registered_(xs, fdefault)
        return tgt

    def _itercheck4iter_prefix_target_pairs(sf, lt, M, it, /, *, len_asc):
        if it is not iter(it): raise TypeError
        if len_asc:
            f = gt = lambda x,y:lt(y,x)
            L = -1
        else:
            f = lt
            L = M
        for ys, tgt in it:
            if not f(len(ys), L):raise logic-err
            L = len(ys)
            yield ys, tgt
        if len_asc:
            if not f(M, L):raise logic-err
    def iter_prefix_target_pairs_of(sf, xs, /, *, len_asc):
        '[x] -> *len_asc/bool -> Iter ([x], tgt)'
        sf._check_seq_type_(xs)
        it = sf._iter_prefix_target_pairs_of_(xs, len_asc=len_asc)
        L = len(xs)+1
        return sf._itercheck4iter_prefix_target_pairs(__lt__, L, it, len_asc=len_asc)
    def iter_all_prefix_target_pairs(sf, /, *, len_asc):
        '*len_asc/bool -> Iter ([x], tgt)'
        it = sf._iter_all_prefix_target_pairs_(len_asc=len_asc)
        L = inf
        return sf._itercheck4iter_prefix_target_pairs(__le__, L, it, len_asc=len_asc)

class _Node:
    __slots__ = r'''
    lcp
    pld
    may_item
    '''.split()#'''
    @property
    def longest_common_prefix(sf, /):
        return sf.lcp
    @property
    def payload(sf, /):
        return sf.pld

    def __init__(sf, lcp, pld, may_item, /):
        sf.lcp = lcp
        sf.pld = pld
        sf.may_item = may_item
    def __repr__(sf, /):
        return repr_helper(sf, sf.lcp, sf.pld, sf.may_item)
    if 0:
      @override
      def ___get_args_kwargs___(sf, /):
        '-> (args:Seq, kwargs:Mapping)'
        return (sf.lcp, sf.pld, sf.may_item), {}

def _is_prefix_of_seq(may_prefix, seq, begin, /):
    return may_prefix is None or _is_prefix_of_seq_(may_prefix, seq, begin)
def _len_lcp_of_ex2(may_seq, seq, begin, /):
    return 0 if may_seq is None else _len_lcp_of_ex_([(may_seq,), (seq, begin)])
_slice_seq1 = lambda xs, begin, /:xs[begin:] if begin else xs
_slice_seq2 = lambda xs, begin, end, /:xs[begin:end] if not (begin==0 and end==len(xs)) else xs
_len_may_seq = lambda may_seq: 0 if may_seq is None else len(may_seq)
class ISeqPrefixRegister__using_mapping(ISeqPrefixRegister):
    r'''
    node :: _Node<may [x], (None|node|{x:node}{len>=2}), may item>
        #root.init==>>_Node(None,None)
    item = ([x], target)
    '''#'''
    __slots__ = ()

    @abstractmethod
    def _get_root_node_(sf, /):
        '->node'
    @abstractmethod
    def _get_len2items_(sf, /):
        '->len2items/seqss/[[[x]]]'
    def _mk_mapping4element_(sf, /):
        '->Map x node'
        return {}
    def _merge_item_(sf, old_item, new_item, /):
        'old_item/(ys,tgtL) -> new_item/(xs,tgtR){xs==ys} -> item'
        (xs,tgtR) = new_item
        raise PrefixLookupError__existed(xs)
    def _mk_mapping4element(sf, /):
        '->Map x node'
        d = sf._mk_mapping4element_()
        if type(d) is tuple:raise TypeError
            #<<== item :: Pair
        return d
    def _merge_item(sf, old_item, new_item, /):
        'old_item/(ys,tgtL) -> new_item/(xs,tgtR){xs==ys} -> item'
        (ys,tgtL) = old_item
        (xs,tgtR) = new_item
        assert xs == ys
        zs, tgt = item = sf._merge_item_(old_item, new_item)
        sf._check_seq_type_(zs)
        if not xs == zs:raise logic-err
        return item
    def _get_root_node(sf, /):
        '->node'
        root = sf._get_root_node_()
        check_type_is(_Node, root)
        return root
    def _get_len2items(sf, /):
        '->len2items/seqss/[[[x]]]'
        len2items = sf._get_len2items_()
        check_type_is(list, len2items)
        return len2items

    @classmethod
    def _find_deepmost_node_ex(cls, node, xs, begin, /):
        '[x] -> node_exs/[(node, begin, len_lcp)]'
        check_type_is(_Node, node)
        node_exs = []

        #begin = 0
        sz = len(xs)
        #while _is_prefix_of_seq(node.lcp, xs, begin):
        while 1:
            assert node.pld is None or type(node.pld) is _Node or len(node.pld) >= 2
            assert node.may_item is None or (type(node.may_item) is tuple and len(node.may_item) == 2)
            assert not (type(node.pld) is _Node and node.may_item is None)

            len_lcp = L = _len_lcp_of_ex2(node.lcp, xs, begin)
            n = _len_may_seq(node.lcp)
            node_ex = (node, begin, len_lcp)
            node_exs.append(node_ex)
            #
            if node.pld is None and node.may_item is None:
                #assert len(.)==0
                #assert node is root
                assert node.lcp is None
                break
            #xxx assert not node.lcp is None
                #may [len(node.lcp)==0]
            if node.pld is None and not node.may_item is None:
                #assert len(.)==1
                break
            if not L == n:
                break
            begin_ = begin+n
            if begin_ == sz:
                break
            assert begin_ < sz

            if type(node.pld) is _Node:
                #assert len(.)==2
                node = node.pld
                begin = begin_
                continue
            d = node.pld
            assert len(d) >= 2
            x = xs[begin_]
            if x not in d:
                break
            node = d[x]
            begin = begin_+1
            check_type_is(_Node, node)
        return node_exs
    @classmethod
    def _register_at_seq(cls, _mk_mapping4element, _merge_item, node, xs, begin, lazy_tgt, /):
        r'''
        [x] -> lazy tgt -> (ok, data)|^PrefixLookupError__existed
        ok = xs not in sf
        data = (node_exs, node4new_item, new_item)
            | (node_exs, args4todo_merge)
        args4todo_merge :: (node, begin, len_lcp, xs, lazy_tgt)
        new_item :: (xs, tgt)
        node_exs :: [(node, begin, len_lcp)]
        assert node4new_item.may_item is new_item
        node := node_exs[-1][0]
        assert node is args4todo_merge[0]
        assert node.may_item is not None
        assert node.may_item[0] == xs
        '''#'''
        if 0:
            '[x] -> lazy tgt -> merged/bool|^PrefixLookupError__existed'
            merged = False
        else:
            '[x] -> lazy tgt -> args4todo_merge/(False|(node, begin, len_lcp, xs, lazy_tgt))|^PrefixLookupError__existed'
            args4todo_merge = False
            del _merge_item
        node_exs = cls._find_deepmost_node_ex(node, xs, begin)
        (node, begin, len_lcp) = node_ex = node_exs[-1]
        n = _len_may_seq(node.lcp)
        tsz = len(xs)-begin
        L = len_lcp #_len_lcp_of_ex2(node.lcp, xs, begin)
        assert L <= min(tsz, n)

        #new_item = xs, tgt
        lazy_new_item = lambda:(xs, lazy_tgt())

        while 1:
            assert node.pld is None or type(node.pld) is _Node or len(node.pld) >= 2
            assert node.may_item is None or (type(node.may_item) is tuple and len(node.may_item) == 2)
            assert not (type(node.pld) is _Node and node.may_item is None)


            if L==tsz == n and not node.may_item is None:
                #_merge_item
                lazy_new_item
                ok = False
            else:
                new_item = lazy_new_item()
                del lazy_new_item
                ok = True

            if node.pld is None and node.may_item is None:
                #assert len(.)==0
                #assert node is root
                assert node.lcp is None
                node.lcp = _slice_seq1(xs, begin)
                node.may_item = new_item
                node4new_item = node
                break
            #assert len(.)>=1
            if L==tsz < n:
                _node = _Node(node.lcp[L:], node.pld, node.may_item)
                node.lcp = node.lcp[:L]
                node.pld = _node
                node.may_item = new_item
                node4new_item = node
                break
            if L==tsz == n and node.may_item is None:
                node.may_item = new_item
                assert L==tsz == n and not node.may_item is None
                    #==>>calc-ok()changed
                node4new_item = node
                break
            if L==tsz == n and not node.may_item is None:
                #_merge_item
                assert not ok
                ys, old_tgt = old_item = node.may_item
                assert len(xs)==len(ys)
                #assert xs==ys
                if 0:
                    new_item = lazy_new_item()
                    (zs, tgt_) = item = _merge_item(old_item, new_item)
                    #sf._check_seq_type_(zs)
                    node.may_item = item
                    merged = True
                else:
                    args4todo_merge = (node, begin, len_lcp, xs, lazy_tgt)
                break
            assert not L==tsz <= n
            assert L < tsz
            if L==n < tsz and node.pld is None:
                _node = _Node(_slice_seq1(xs, begin+L), None, new_item)
                node.pld = _node
                node4new_item = _node
                break

            x = xs[begin+L]
            _node0 = _Node(_slice_seq1(xs, begin+L+1), None, new_item)
            node4new_item = _node0
            if L==n < tsz and not node.pld is None:
                if type(node.pld) is _Node:
                    #assert len(.)==2
                    _node = node.pld
                    assert _node.lcp
                    z = _node.lcp[0]
                    assert not x == z#_find_deepmost_node_ex
                    d = _mk_mapping4element()
                    d[z] = _node
                    _node.lcp = _node.lcp[1:]
                    node.pld = d
                else:
                    d = node.pld
                    assert not x in d#_find_deepmost_node_ex
                assert d is node.pld
                d[x] = _node0
                break
            assert L < min(tsz, n)
            if 1:
                z = node.lcp[L]
                assert not x == z#_find_deepmost_node_ex
                _node1 = _Node(node.lcp[L+1:], node.pld, node.may_item)
                d = _mk_mapping4element()
                d[x] = _node0
                d[z] = _node1
                node.lcp = node.lcp[:L]
                node.pld = d
                node.may_item = None
                break
            raise logic-err
        #xxx assert ok is not (L==tsz == n and not node.may_item is None), (ok, not (L==tsz == n and not node.may_item is None))
        #   since @『L==tsz == n and node.may_item is None』
        assert ok is (not (L==tsz == n and not node.may_item is None)) or (ok and node.may_item is new_item)
        assert node_exs[-1][0] is node
        if ok:
            node_exs
            node4new_item
            new_item # (xs, tgt)
            assert node4new_item.may_item is new_item
            data = (node_exs, node4new_item, new_item)
        else:
            node_exs
            args4todo_merge # (node, begin, len_lcp, xs, lazy_tgt)
            assert node is args4todo_merge[0]
            assert node.may_item is not None
            assert node.may_item[0] == xs
            data = (node_exs, args4todo_merge)


        return (ok, data)
        return args4todo_merge
        return merged



    @override
    def _register_at_seq_(sf, xs, tgt, /):
        '[x] -> tgt -> None|^PrefixLookupError__existed'
        (ok, data) = sf.__register_at_seq(xs, lambda:tgt, ...)#(sf._merge_item)
        if not ok: raise PrefixLookupError__existed(xs)
        if not ok: raise NotImplementedError
            #需要删除old_item
            #有点麻烦
    def __register_at_seq(sf, xs, lazy_tgt, _merge_item, /):
        '-> (ok, data)'
        node = sf._get_root_node()
        begin = 0
        cls = type(sf)
        (ok, data) = cls._register_at_seq(sf._mk_mapping4element, _merge_item, node, xs, begin, lazy_tgt)
        if not ok:
            #需要删除old_item
            #有点麻烦
            return (ok, data)
        #sf.sz += not args4todo_merge
        len2items = sf._get_len2items()
        m = len(len2items)
        n = len(xs)
        if not n < m:
            len2items.extend([] for _ in range(n+1-m))
            m = len(len2items)
            assert n+1 == m
        assert n < m
        #new_item = (xs,tgt)
        (node_exs, node4new_item, new_item) = data
        len2items[n].append(new_item)
        return (ok, data)


    @override
    def _iter_prefix_target_pairs_of_(sf, xs, /, *, len_asc):
        '[x] -> *len_asc/bool -> Iter ([x], tgt)'
        node = sf._get_root_node()
        begin = 0
        cls = type(sf)
        node_exs = cls._find_deepmost_node_ex(node, xs, begin)
        f = iter if len_asc else reversed
        for node_ex in f(node_exs):
            (node, begin, len_lcp) = node_ex
            n = _len_may_seq(node.lcp)
            tsz = len(xs)-begin
            assert len_lcp <= min(tsz, n)
            if not node.may_item is None:
                ys, tgt = item = node.may_item
                yield item
    @override
    def _iter_all_prefix_target_pairs_(sf, /, *, len_asc):
        '*len_asc/bool -> Iter ([x], tgt)'
        len2items = sf._get_len2items()
        f = iter if len_asc else reversed
        for items in f(len2items):
            yield from items

    @override
    def _set_xdefault5registered_(sf, xs, fdefault, /):
        '[x] -> (()->tgt) -> tgt'
        (ok, data) = sf.__register_at_seq(xs, fdefault, ...)
        if ok:
            (node_exs, node4new_item, new_item) = data
            (ys, new_tgt) = new_item
            return new_tgt
        else:
            (node_exs, args4todo_merge) = data
            (node, begin, len_lcp, xs, lazy_tgt) = args4todo_merge
            old_item = node.may_item
            (ys, old_tgt) = old_item
            return old_tgt

class SeqPrefixRegister__using_mapping(ISeqPrefixRegister__using_mapping, IReprHelper):
    __slots__ = r'''
    _xsss
    _root
    '''.split()#'''
    @override
    def _get_root_node_(sf, /):
        '->node'
        return sf._root
    @override
    def _get_len2items_(sf, /):
        '->len2items/seqss/[[[x]]]'
        return sf._xsss
    def __init__(sf, items=None, /):
        sf._xsss = []
        sf._root = _Node(None, None, None)
        if items is not None:
            for xs, tgt in items:
                sf[xs] = tgt

    @override
    def ___get_args_kwargs___(sf, /):
        '-> (args:Seq, kwargs:Mapping)'
        items = [*sf.iter_all_prefix_target_pairs(len_asc=False)]
        if items:
            return [items], {}
        return [], {}
SeqPrefixRegister__using_mapping()




class _QualNamePrefixRegister__using_mapping(SeqPrefixRegister__using_mapping):
    'not-using-yet:check_pseudo_qual_name'
    __slots__ = ()
    @override
    def _check_seq_type_(sf, xs, /):
        check_type_is(str, xs)

class QualNamePrefixRegister(ISeqPrefixRegister, IReprHelper):
    'using:check_pseudo_qual_name'
    __slots__ = '_sf'
    @override
    def _check_seq_type_(sf, xs, /):
        check_type_is(str, xs)
        check_pseudo_qual_name(xs)

    def __init__(sf, items=None, /):
        sf._sf = _QualNamePrefixRegister__using_mapping()
        if items is not None:
            for xs, tgt in items:
                sf[xs] = tgt
    @override
    def ___get_args_kwargs___(sf, /):
        '-> (args:Seq, kwargs:Mapping)'
    ___get_args_kwargs___ = SeqPrefixRegister__using_mapping.___get_args_kwargs___

    @override
    def _register_at_seq_(sf, xs, tgt, /):
        '[x] -> tgt -> None|^PrefixLookupError__existed'
        sf._sf.register_at_seq(xs, tgt)
    @override
    def _iter_prefix_target_pairs_of_(sf, xs, /, *, len_asc):
        '[x] -> *len_asc/bool -> Iter ([x], tgt)'
        it = sf._sf.iter_prefix_target_pairs_of(xs, len_asc=len_asc)
        for ys, tgt in it:
            if len(ys)==len(xs) or xs[len(ys)]=='.':
                yield ys, tgt
    @override
    def _iter_all_prefix_target_pairs_(sf, /, *, len_asc):
        '*len_asc/bool -> Iter ([x], tgt)'
        return sf._sf.iter_all_prefix_target_pairs(len_asc=len_asc)
    @override
    def _set_xdefault5registered_(sf, xs, fdefault, /):
        '[x] -> (()->tgt) -> tgt'
        return sf._sf._set_xdefault5registered_(xs, fdefault)



class ISeqPrefixRegister__default_target(ISeqPrefixRegister):
    __slots__ = ()
    @abstractmethod
    def _mk_target_(sf, xs, /):
        '[x] -> tgt'
    def mk_target(sf, xs, /):
        '[x] -> tgt'
        sf._check_seq_type_(xs)
        tgt = sf._mk_target_(xs)
        sf._check_target_type_(tgt)
        return tgt
    @override
    def __getitem__(sf, xs, /):
        '[x] -> tgt|^TypeError'
        '[x] -> tgt|^PrefixLookupError__nonexisted|^TypeError'
        tgt = sf.set_xdefault5registered(xs, 1, sf.mk_target)
        return tgt
    if 0:
      def _check_target_type_(sf, tgt, /):
        'tgt -> None|^TypeError'
        return
class IQualNamePrefixRegister__default_target(QualNamePrefixRegister, ISeqPrefixRegister__default_target):
    __slots__ = ()
class QualNamePrefixRegister__default_target_is_dict(IQualNamePrefixRegister__default_target):
    __slots__ = ()
    @override
    def _mk_target_(sf, xs, /):
        '[x] -> tgt'
        return {}
QualNamePrefixRegister__default_target_is_dict()


sort__len_desc = lambda ss:sorted(ss, key=len, reverse=True)
def check_file_suffix(file_suffix, /):
    check_type_is(str, file_suffix)
    if not file_suffix[0]=='.': raise TypeError
class LoadError(ImportError):pass
    #FileReaderMakerRegister

class IBaseFileLoaderMakerRegister(IReprHelper, ABC__no_slots):
    r'''
    _author2fmt2loader_mkr :: Register{author:{fmt:loader_mkr}}
    _usr2suffix2author_fmt :: Register{usr:{suffix:(author,fmt)}}
    '''#'''
    @abstractmethod
    def _check_loader_mkr_type_(sf, loader_mkr, /):
        return
    @override
    def ___get_args_kwargs___(sf, /):
        '-> (args:Seq, kwargs:Mapping)'
        it = sf._author2fmt2loader_mkr.iter_all_prefix_target_pairs(len_asc=False)
        items4def = [(qname8author, sorted(fmt2loader_mkr.items())) for qname8author, fmt2loader_mkr in it]
        it = sf._usr2suffix2author_fmt.iter_all_prefix_target_pairs(len_asc=False)
        items4ref = [(qname8usr_pkg_prefix, sorted([(su, au, fmt)for su, (au, fmt) in suffix2author_fmt.items()])) for qname8usr_pkg_prefix, suffix2author_fmt in it]

        args = [items4def, items4ref]
        while args and not args[-1]:
            args.pop()
        return args, {}

    def __init__(sf, items4def=None, items4ref=None, /):
        sf._author2fmt2loader_mkr = QualNamePrefixRegister__default_target_is_dict()
        sf._usr2suffix2author_fmt = QualNamePrefixRegister__default_target_is_dict()
        if items4def is None:
            items4def = ()
        if items4ref is None:
            items4ref = ()
        for qname8author, fmt_name__loader_mkr__pairs in items4def:
            sf.register__defs(qname8author, fmt_name__loader_mkr__pairs)
        for qname8usr_pkg_prefix, file_suffix__qname8author__fmt_name__triples in items4ref:
            sf.register__refs(qname8usr_pkg_prefix, file_suffix__qname8author__fmt_name__triples)

    def register__def(sf, qname8author, fmt_name, loader_mkr, /):
        sf.register__defs(qname8author, [(fmt_name, loader_mkr)])

    def register__ref(sf, qname8usr_pkg_prefix, file_suffix, qname8author, fmt_name, /):
        sf.register__refs(qname8usr_pkg_prefix, [(file_suffix, qname8author, fmt_name)])

    def register__defs(sf, qname8author, fmt_name__loader_mkr__pairs, /):
        fmt2loader_mkr = sf._author2fmt2loader_mkr[qname8author]
        for (fmt_name, loader_mkr) in fmt_name__loader_mkr__pairs:
            check_type_is(str, fmt_name)
            sf._check_loader_mkr_type_(loader_mkr)
            fmt2loader_mkr[fmt_name] = loader_mkr
                #允许覆盖？？
    def register__refs(sf, qname8usr_pkg_prefix, file_suffix__qname8author__fmt_name__triples, /):
        suffix2author_fmt = sf._usr2suffix2author_fmt[qname8usr_pkg_prefix]
        check_author = sf._author2fmt2loader_mkr._check_seq_type_
        for (file_suffix, qname8author, fmt_name) in file_suffix__qname8author__fmt_name__triples:
            check_file_suffix(file_suffix)
            check_type_is(str, fmt_name)
            check_author(qname8author)
            suffix2author_fmt[file_suffix] = (qname8author, fmt_name)
                #允许覆盖？？


def _1load__qname_to_suffix2author_fmt(sf, qname, /):
    'qname -> suffix2author_fmt'
    it = sf._usr2suffix2author_fmt.iter_prefix_target_pairs_of(qname, len_asc=True)
    d = {}
    for qname8usr_pkg_prefix, suffix2author_fmt in it:
        d.update(suffix2author_fmt)
    suffix2author_fmt = d
    return suffix2author_fmt
def _2load__qname_to_suffix2author_fmt__ex(sf, qname, /):
    'qname -> (suffix2author_fmt, suffixes__len_desc)'
    suffix2author_fmt = _1load__qname_to_suffix2author_fmt(sf, qname)
    suffixes__len_desc = sort__len_desc(suffix2author_fmt)
    return (suffix2author_fmt, suffixes__len_desc)
    #author2suffix2author_fmt = group4dict_value(fst, suffix2author_fmt)
    #author2suffixes__len_desc = fmap4dict_value(sort__len_desc, author2suffix2author_fmt)

def _prepare4load(sf, qname4pkg, basename4rsc, /):
    '-> ()|(qname4pkg, basename4rsc, file_suffix, qname8author, fmt_name, loader_mkr)|^KeyError(fmt_name)'
    #importlib.resources.contents(package)->Iter<name/resource-or-not>#目录
    #importlib.resources.is_resource(package, name)->bool

    #check_pseudo_qual_name(qname4pkg)
    if not '.' in basename4rsc:
        return null_tuple
    if not importlib.resources.is_resource(qname4pkg, basename4rsc):
        return null_tuple

    suffix2author_fmt = _1load__qname_to_suffix2author_fmt(sf, qname4pkg)

    ilast = basename4rsc.rindex('.')
    i = -1
    while not i == ilast:
        i = basename4rsc.index('.', i+1)
        file_suffix = basename4rsc[i:]
        if file_suffix in suffix2author_fmt:
            break
    else:
        return null_tuple


    (qname8author, fmt_name) = suffix2author_fmt[file_suffix]
    while 1:
        try:
            loader_mkr = sf._author2fmt2loader_mkr[qname8author][fmt_name]
                #^KeyError
            break
        except KeyError:
            if not qname8author in sys.modules:
                try:
                    importlib.import_module(qname8author)
                    assert qname8author in sys.modules
                    continue
                except ImportError:
                    pass
            raise
    return (qname4pkg, basename4rsc, file_suffix, qname8author, fmt_name, loader_mkr)



#class FileLoaderMakerRegister(IBaseFileLoaderMakerRegister):
class FileReaderMakerRegister(IBaseFileLoaderMakerRegister):
    #@abstractmethod
    def _read_basic_(sf, qname4pkg, basename4rsc, file_suffix, qname8author, fmt_name, reader, /):
        '-> result|^LoadError'
        result = reader(qname4pkg, basename4rsc, file_suffix)
        return result
    @override
    def _check_loader_mkr_type_(sf, loader_mkr, /):
        check_type_le(IFileReaderMaker, loader_mkr)
        return
    def _check_reader_type_(sf, reader, /):
        check_type_le(IFileReader, reader)
        return
    def read_tmay(sf, qname4pkg, basename4rsc, /):
        'qname4pkg -> basename4rsc -> tmay_result|^LoadError'
        m = _prepare4load(sf, qname4pkg, basename4rsc)
        if not m:
            return null_tuple
        (qname4pkg, basename4rsc, file_suffix, qname8author, fmt_name, loader_mkr) = m
        reader_mkr = loader_mkr
        reader = reader_mkr(qname8author, fmt_name)
        sf._check_reader_type_(reader)
        result = sf._read_basic_(qname4pkg, basename4rsc, file_suffix, qname8author, fmt_name, reader)
        tmay_result = (result,)
        check_tmay(tmay_result)
        return tmay_result

a_FileReaderMakerRegister = FileReaderMakerRegister()
class MainFuncs:
    read_tmay = a_FileReaderMakerRegister.read_tmay
    register__def = a_FileReaderMakerRegister.register__def
    register__ref = a_FileReaderMakerRegister.register__ref
    register__defs = a_FileReaderMakerRegister.register__defs
    register__refs = a_FileReaderMakerRegister.register__refs
MainFuncs = MainFuncs()




def _open_or_readall(qname4pkg, basename4rsc, using_file_obj4read, smay_encoding, /):
    '->ifile_or_content #fin|bfin|str|bytes'
    if smay_encoding:
        encoding = smay_encoding
        kw = dict(encoding=encoding)
    else:
        kw = {}

    if 0:pass
    elif smay_encoding and using_file_obj4read:
        f = importlib.resources.open_text
    elif smay_encoding and not using_file_obj4read:
        f = importlib.resources.read_text
    elif not smay_encoding and using_file_obj4read:
        f = importlib.resources.open_binary
    elif not smay_encoding and not using_file_obj4read:
        f = importlib.resources.read_binary
    else:
        raise logic-err
    ifile_or_content = f(qname4pkg, basename4rsc, **kw)
    return ifile_or_content


class IFileReaderMaker(IReprHelper, ABC):
    r'''reader_mkr
    reader = reader_mkr(qname8author, fmt_name, using_file_obj4read, smay_encoding)
    result = reader(ifile_or_content)
    '''#'''
    __slots__ = ()
    @abstractmethod
    def _mk_reader_(sf, qname8author, fmt_name, /):
        'qname8author -> fmt_name -> IFileReader|^ImportError'
    def __call__(sf, qname8author, fmt_name, /):
        'qname8author -> fmt_name -> may IFileReader|^ImportError'
        check_pseudo_qual_name(qname8author)
        check_type_is(str, fmt_name)

        reader = sf._mk_reader_(qname8author, fmt_name)
        check_type_le(IFileReader, reader)
        return reader





class IFileReader(IReprHelper, ABC__no_slots):
    r'''reader
    '''#'''
    @abstractmethod
    def _read_(sf, qname4pkg, basename4rsc, file_suffix, /):
        '-> result|^LoadError'
    @override
    def ___get_args_kwargs___(sf, /):
        '-> (args:Seq, kwargs:Mapping)'
        return (sf.qname8author, sf.fmt_name), {}
    def __init__(sf, qname8author, fmt_name, /):
        check_pseudo_qual_name(qname8author)
        check_type_is(str, fmt_name)
        sf._qnm = qname8author
        sf._fmt = fmt_name
    @property
    def qname8author(sf, /):
        return sf._qnm
    @property
    def fmt_name(sf, /):
        return sf._fmt
    def __call__(sf, qname4pkg, basename4rsc, file_suffix, /):
        '-> result|^LoadError'
        check_pseudo_qual_name(qname4pkg)
        check_type_is(str, basename4rsc)
        check_file_suffix(file_suffix)
        result = sf._read_(qname4pkg, basename4rsc, file_suffix)
        return result
class IFileReader__using_importlib_resources(IFileReader):
    __slots__ = ()
    @abstractmethod
    def _get_using_file_obj4read_(sf, /):
        '-> using_file_obj4read/bool'
    @abstractmethod
    def _get_smay_encoding_(sf, qname4pkg, basename4rsc, file_suffix, /):
        '-> smay encoding/str#is_textfile'
    @abstractmethod
    def _read_ex_(sf, ifile_or_content, /):
        '-> result|^LoadError'

    def _get_using_file_obj4read_and_smay_encoding_(sf, qname4pkg, basename4rsc, file_suffix, /):
        '-> (using_file_obj4read/bool, smay encoding/str#is_textfile)'
        using_file_obj4read = sf._get_using_file_obj4read_()
        smay_encoding = sf._get_smay_encoding_(qname4pkg, basename4rsc, file_suffix)
        return using_file_obj4read, smay_encoding
    def get_using_file_obj4read_and_smay_encoding(sf, qname4pkg, basename4rsc, file_suffix, /):
        '-> (using_file_obj4read/bool, smay encoding/str#is_textfile)'
        (using_file_obj4read, smay_encoding) = sf._get_using_file_obj4read_and_smay_encoding_(qname4pkg, basename4rsc, file_suffix)
        check_type_is(bool, using_file_obj4read)
        check_type_is(str, smay_encoding)
        return (using_file_obj4read, smay_encoding)

    @override
    def _read_(sf, qname4pkg, basename4rsc, file_suffix, /):
        '-> result|^LoadError'
        (using_file_obj4read, smay_encoding) = sf.get_using_file_obj4read_and_smay_encoding(qname4pkg, basename4rsc, file_suffix)
        ifile_or_content = _open_or_readall(qname4pkg, basename4rsc, using_file_obj4read, smay_encoding)
        result = sf._read_ex_(ifile_or_content)
        return result


class FileReader__using_importlib_resources__functional(IFileReader__using_importlib_resources):
    @override
    def ___get_args_kwargs___(sf, /):
        '-> (args:Seq, kwargs:Mapping)'
        return (sf.qname8author, sf.fmt_name, sf.using_file_obj4read, sf.smay_encoding, sf._read_ex_), {}
    def __init__(sf, qname8author, fmt_name, using_file_obj4read, smay_encoding, _read_ex_, /):
        check_type_is(bool, using_file_obj4read)
        check_type_is(str, smay_encoding)
        check_callable(_read_ex_)

        super().__init__(qname8author, fmt_name)
        sf.using_file_obj4read = using_file_obj4read
        sf.smay_encoding = smay_encoding
        sf._read_ex_ = _read_ex_
    @override
    def _get_using_file_obj4read_(sf, /):
        '-> using_file_obj4read/bool'
        return sf.using_file_obj4read
    @override
    def _get_smay_encoding_(sf, qname4pkg, basename4rsc, file_suffix, /):
        '-> smay encoding/str#is_textfile'
        return sf.smay_encoding
    @override
    def _read_ex_(sf, ifile_or_content, /):
        '-> result|^LoadError'
        return sf._read_ex_




class FileReader__using_importlib_resources__(IFileReader__using_importlib_resources):
    using_file_obj4read = False
    smay_encoding = ''

    @override
    def _get_using_file_obj4read_(sf, /):
        '-> using_file_obj4read/bool'
        return sf.using_file_obj4read
    @override
    def _get_smay_encoding_(sf, qname4pkg, basename4rsc, file_suffix, /):
        '-> smay encoding/str#is_textfile'
        return sf.smay_encoding
    @override
    def _read_ex_(sf, ifile_or_content, /):
        '-> result|^LoadError'
        return ifile_or_content
        return ifile_or_content.read()
class FileReaderMaker__(IFileReaderMaker):
    __slots__ = ()
    _mk_reader_ = FileReader__using_importlib_resources__
    @override
    def ___get_args_kwargs___(sf, /):
        '-> (args:Seq, kwargs:Mapping)'
        return (), {}

FileReader__using_importlib_resources__raw = FileReader__using_importlib_resources__

FileReader__using_importlib_resources__raw('a', '2')
FileReaderMaker__()



class FileReader__using_importlib_resources__u8(FileReader__using_importlib_resources__):
    smay_encoding = 'u8'
class FileReaderMaker__u8(FileReaderMaker__):
    __slots__ = ()
    _mk_reader_ = FileReader__using_importlib_resources__u8

a_FileReaderMaker__u8 = FileReaderMaker__u8()
FileReaderMaker__raw = FileReaderMaker__
a_FileReaderMaker__raw = FileReaderMaker__raw()












class TextReader(IFileReader__using_importlib_resources):
    @override
    def ___get_args_kwargs___(sf, /):
        '-> (args:Seq, kwargs:Mapping)'
        return (sf.qname8author, sf.fmt_name, sf.smay_encoding), {}
    def __init__(sf, qname8author, fmt_name, smay_encoding, /):
        check_type_is(str, smay_encoding)
        super().__init__(qname8author, fmt_name)
        sf.smay_encoding = smay_encoding

    @override
    def _get_using_file_obj4read_(sf, /):
        '-> using_file_obj4read/bool'
        return False
    @override
    def _get_smay_encoding_(sf, qname4pkg, basename4rsc, file_suffix, /):
        '-> smay encoding/str#is_textfile'
        return sf.smay_encoding
    @override
    def _read_ex_(sf, ifile_or_content, /):
        '-> result|^LoadError'
        return ifile_or_content


class TextReaderMaker(IFileReaderMaker, ABC__no_slots):
    def __init__(sf, smay_encoding, /):
        check_type_is(str, smay_encoding)
        sf._smay_encoding = smay_encoding
    @override
    def _mk_reader_(sf, qname8author, fmt_name, /):
        'qname8author -> fmt_name -> IFileReader|^ImportError'
        return TextReader(qname8author, fmt_name, sf._smay_encoding)
    @override
    def ___get_args_kwargs___(sf, /):
        '-> (args:Seq, kwargs:Mapping)'
        return (sf._smay_encoding,), {}





text_reader_mkr4gb = TextReaderMaker('gb18030')
text_reader_mkr4u8 = TextReaderMaker('utf8')
binary_reader_mkr = TextReaderMaker('')

TextReader
TextReaderMaker
text_reader_mkr4gb
text_reader_mkr4u8
binary_reader_mkr


































































#[[[
r'''
class IxxxFileLoader(importlib.abc.FileLoader):
    #.?get_resource_reader(fullname)->ResourceReader
    def __init__(sf, qname8author, fmt_name, pkg, sterm, file_suffix, /):
        qname = f'{pkg}.{sterm}'
        basename = f'{sterm}{file_suffix}'
        pkg_obj = importlib.import_module(pkg)
        for folder_path in pkg_obj.__path__:
            fpath = os.path.join(folder_path, basename)
            if os.path.exists(fpath):
                break
        else:
            raise FileNotFoundError((pkg, basename))
        fpath
        super().__init__(qname, fpath)
        sf._args = (qname8author, fmt_name, pkg, sterm, file_suffix)

    @override
    def get_source(sf, qname, /):
        #InspectLoader.get_source(fullname)->may str|^ImportError
        return None
IxxxFileLoader(1,2, 'seed', '__README__', '.txt')
IxxxFileLoader

class IxxxFileLoader(importlib.abc.Loader):
    def __init__(sf, qname8author, fmt_name, pkg, sterm, file_suffix, /):
        qname = f'{pkg}.{sterm}'
        basename = f'{sterm}{file_suffix}'
        pkg_obj = importlib.import_module(pkg)
        for folder_path in pkg_obj.__path__:
            fpath = os.path.join(folder_path, basename)
            if os.path.exists(fpath):
                break
        else:
            raise FileNotFoundError((pkg, basename))
        fpath
        sf._argss = (qname8author, fmt_name, pkg, sterm, file_suffix), (qname, basename, fpath)

    @override
    def create_module(sf, spec, /):
        '.create_module(spec)->may module_obj'
        return None
    @override
    def exec_module(sf, module_obj, /):
        '.exec_module(module_obj)'
        qname = module_obj.__name__
        spec = module_obj.__spec__
        fpath = module_obj.__file__
        (qname8author, fmt_name, pkg, sterm, file_suffix), (qname, basename, fpath) = sf._argss
        raise
    def open(sf, /):
        (qname8author, fmt_name, pkg, sterm, file_suffix), (qname, basename, fpath) = sf._argss
        tmay_encoding = sf.get_tmay_encoding(qname8author, fmt_name, file_suffix)
        if tmay_encoding:
            [encoding]=tmay_encoding
            fin = importlib.resources.open_text(pkg, basename, encoding=encoding, errors='strict')
        else:
            []=tmay_encoding
            bfin = importlib.resources.open_binary(pkg, basename)
        return fin, bfin
    @abstractmethod
    def get_tmay_encoding(sf, qname8author, fmt_name, file_suffix, /):
        '-> tmay encoding'






class IFileLoaderMaker(ABC):
    'loader_mkr'
    __slots__ = ()
    @abstractmethod
    def _mk_may_loader_(sf, qname8author, fmt_name, pkg, sterm, file_suffix, /):
        'qname8author -> fmt_name -> pkg -> sterm -> file_suffix -> may Loader|^ImportError'
    def __call__(sf, qname8author, fmt_name, pkg, sterm, file_suffix, /):
        'qname8author -> fmt_name -> pkg -> sterm -> file_suffix -> may Loader|^ImportError'
        check_pseudo_qual_name(qname8author)
        check_type_is(str, fmt_name)

        check_pseudo_qual_name(pkg)
        check_pseudo_identifier(sterm)
        check_file_suffix(file_suffix)
        qname = f'{pkg}.{sterm}'
        basename = f'{sterm}{file_suffix}'
        assert importlib.resources.is_resource(pkg, basename)

        may_loader = sf._mk_may_loader_(qname8author, fmt_name, pkg, sterm, file_suffix)
        if may_loader is not None:
            loader = may_loader
            check_type_le(importlib.abc.Loader, loader)
        return may_loader

class _PathEntryFinder(importlib.abc.PathEntryFinder):
    def __init__(sf, path, /):
        check_type_is(str, path)
        sf._p = path
    def _get_file_loader_mkr_register_(sf, /):
        '-> FileLoaderMakerRegister'
        return _file_loader_mkr_register
    @override
    def find_spec(sf, qname, target=None, /):
        '->may spec'
        path = sf._p
        register = sf._get_file_loader_mkr_register_()
        may_spec = register.mk_may_spec(qname, path)
        return may_spec








class FileLoaderMakerRegister(IBaseFileLoaderMakerRegister):
    @override
    def _check_loader_mkr_type_(sf, loader_mkr, /):
        check_type_le(IFileLoaderMaker, loader_mkr)
        return
    def mk_may_spec(sf, qname, path, /):
        'qname -> path -> may_spec'
        #importlib.util.spec_from_file_location(name, location, *, loader=None, submodule_search_locations=None)->spec
        #importlib.util.spec_from_loader(name, loader, *, origin=None, is_package=None)->spec
        rs = sf._prepare4mk_may_loader(qname, path)
        if len(rs)>4:
            (qname,pkg,sterm,_,basename,file_suffix,qname8author,fmt_name,may_loader) = rs
        else:
            may_loader = None
        ######################
        if may_loader is None:
            return None
        loader = may_loader
        folder_path = path
        fpath = os.path.join(folder_path, basename)
        spec = importlib.util.spec_from_loader(qname, loader, origin=fpath)
        may_spec = spec
        return may_spec

    if 0:
      def mk_loader(sf, qname, path, /):
        'qname -> path -> Loader'
    def mk_may_loader(sf, qname, path, /):
        'qname -> path -> may Loader'
        rs = sf._prepare4mk_may_loader(qname, path)
        if len(rs)>4:
            (qname,pkg,sterm,_,basename,file_suffix,qname8author,fmt_name,may_loader) = rs
        else:
            may_loader = None
        return may_loader
    def _prepare4mk_may_loader(sf, qname, path, /):
        'qname -> path -> (qname,pkg,sterm,may[(basename,file_suffix)],basename,file_suffix,qname8author,fmt_name,may_loader)[:?]'
        #(suffix2author_fmt, suffixes__len_desc) = _2load__qname_to_suffix2author_fmt__ex(sf, qname)
        suffix2author_fmt = _1load__qname_to_suffix2author_fmt(sf, qname)
        #mk_loader :: qname -> path -> Loader
        #loader_details :: [(mk_loader,[suffix])]
        smay_pkg, smay, sterm = qname.rpartition('.')
        if not smay_pkg:
            return (qname,)
        pkg = smay_pkg

        #importlib.resources.contents(package)->Iter<name/resource-or-not>#目录
        #importlib.resources.is_resource(package, name)->bool
        it = importlib.resources.contents(pkg)
        ls = []
        for basename in it:
            if not basename.startswith(sterm):
                continue
            file_suffix = basename[len(sterm):]
            if file_suffix in suffix2author_fmt and importlib.resources.is_resource(pkg, basename):
                ls.append((basename, file_suffix))
        if not ls:
            return (qname,pkg,sterm)
        if len(ls)>=2:
            return (qname,pkg,sterm,ls)
        [(basename, file_suffix)] = ls
        (qname8author, fmt_name) = suffix2author_fmt[file_suffix]
        loader_mkr = sf._author2fmt2loader_mkr[qname8author][fmt_name]
            #^KeyError
        assert qname == f'{pkg}.{sterm}'
        assert basename == f'{sterm}{file_suffix}'
        may_loader = loader_mkr(qname8author, fmt_name, pkg, sterm, file_suffix)
        return (qname,pkg,sterm,None,basename,file_suffix,qname8author, fmt_name,may_loader)


if 1:
    _file_loader_mkr_register = FileLoaderMakerRegister()
    sys.path_hooks.append(_PathEntryFinder)
'''#''']]]



if __name__ == "__main__":
    pass







