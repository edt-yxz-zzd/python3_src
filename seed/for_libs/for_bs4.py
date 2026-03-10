#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_bs4.py
vs:
view ../../python3_src/seed/internet/html_ast.py

seed.for_libs.for_bs4
py -m nn_ns.app.debug_cmd   seed.for_libs.for_bs4 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_bs4:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/nn_ns/app/crypt/read_fun_chars.py
    try:
        soup = BeautifulSoup(fin, 'lxml')
    except FeatureNotFound:
        soup = BeautifulSoup(fin, 'html.parser')
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.for_libs.for_bs4   @mk_BeautifulSoup4html_ :'<br/>'
]]]'''#'''
__all__ = r'''
mk_BeautifulSoup4html_


mk_BeautifulSoup4features_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from bs4 import BeautifulSoup, FeatureNotFound
    # BeautifulSoup(markup: Union[str, bytes, IO[str], IO[bytes]] = '', features: Union[str, Sequence[str], NoneType] = None, builder: Union[bs4.builder.TreeBuilder, Type[bs4.builder.TreeBuilder], NoneType] = None, parse_only: Optional[bs4.filter.SoupStrainer] = None, from_encoding: Optional[str] = None, exclude_encodings: Optional[Iterable[str]] = None, element_classes: Optional[Dict[Type[bs4.element.PageElement], Type[bs4.element.PageElement]]] = None, **kwargs: Any)
    #
    # BeautifulSoup(markup = '', features = None, builder = None, parse_only = None, from_encoding = None, exclude_encodings = None, element_classes = None, **kwargs)
    #
    # features:
    #   + specific parser ("lxml", "lxml-xml", "html.parser", "html5lib")
    #   + type of markup to be used ("html", "html5", " xml")
    #
    #
___end_mark_of_excluded_global_names__0___ = ...


def _fail__mk_BeautifulSoup4html_(markup='', features=('lxml', 'html.parser'), *args, **kwds):
    soup = BeautifulSoup(markup, features)
        #GuessedAtParserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently
    return soup
def mk_BeautifulSoup4features_(markup, features, *args, **kwds):
    assert len(features)
    assert not type(features) is str
    assert all(type(feature) is str for feature in features)
    L = len(features)
    for sz, feature in enumerate(features, 1):
        assert type(feature) is str, feature
        try:
            soup = BeautifulSoup(markup, feature)
            break
        except FeatureNotFound:
            if sz == L:
                raise
            continue
    return soup
def mk_BeautifulSoup4html_(markup, *args, **kwds):
    features = ('lxml', 'html.parser')
    return mk_BeautifulSoup4features_(markup, features, *args, **kwds)
    try:
        soup = BeautifulSoup(markup, 'lxml')
    except FeatureNotFound:
        soup = BeautifulSoup(markup, 'html.parser')
    return soup





__all__
from seed.for_libs.for_bs4 import mk_BeautifulSoup4features_
from seed.for_libs.for_bs4 import mk_BeautifulSoup4html_
from seed.for_libs.for_bs4 import *
