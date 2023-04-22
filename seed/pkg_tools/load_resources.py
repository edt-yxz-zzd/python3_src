
#e ../../python3_src/seed/pkg_tools/load_resources.py
#view ../../python3_src/seed/types/SeqPrefixRegister.py
#seed.pkg_tools.load_resources


from seed.types.SeqPrefixRegister import *



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





from seed.pkg_tools.load_resources import IFileReader, IFileReader__using_importlib_resources, IFileReaderMaker, MainFuncs, a_FileReaderMakerRegister, TextReaderMaker, text_reader_mkr4gb, text_reader_mkr4u8, binary_reader_mkr


