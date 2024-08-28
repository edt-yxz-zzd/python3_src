#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/xml/unescape__entitydefs4xhtml_1_0.py


seed.recognize.xml.unescape__entitydefs4xhtml_1_0
py -m nn_ns.app.debug_cmd   seed.recognize.xml.unescape__entitydefs4xhtml_1_0 -x
py -m nn_ns.app.doctest_cmd seed.recognize.xml.unescape__entitydefs4xhtml_1_0:__doc__ -ht
py_adhoc_call   seed.recognize.xml.unescape__entitydefs4xhtml_1_0   @unescape__entitydefs4xhtml_1_0  :'&lt;...&gt;abc&amp;123&quot;'

#]]]'''
__all__ = r'''
unescape__entitydefs4xhtml_1_0
'''.split()#'''
__all__
import re
from html.entities import entitydefs as entitydefs4xhtml_1_0
assert not "'" in entitydefs4xhtml_1_0.values()
assert not "\\" in entitydefs4xhtml_1_0.values()
assert '"' in entitydefs4xhtml_1_0.values()

######################
_ref_regex = re.compile(r'(&\w*;)')
def unescape__entitydefs4xhtml_1_0(s, /, *, nm2s=entitydefs4xhtml_1_0):
    def _repl_(m, /, *, nm2s=nm2s):
        ref = m.group(0)
        nm = ref[1:-1]
        return nm2s[nm]
    return _ref_regex.sub(_repl_, s)
assert unescape__entitydefs4xhtml_1_0('kSemanticVariant="U+4E94&lt;kMatthews"') == 'kSemanticVariant="U+4E94<kMatthews"'
assert unescape__entitydefs4xhtml_1_0('&lt;...&gt;abc&amp;123&quot;') == '<...>abc&123"'
######################




__all__
from seed.recognize.xml.unescape__entitydefs4xhtml_1_0 import unescape__entitydefs4xhtml_1_0
from seed.recognize.xml.unescape__entitydefs4xhtml_1_0 import *
