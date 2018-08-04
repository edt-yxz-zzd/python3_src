
import re

unicode_rex = re.compile(r'U\+(?P<unicode>[0-9A-F]+)')
def _repl_unicode(m):
    return chr(int(m.group('unicode'), base=16))

def replace_unicode(s, rex = unicode_rex):
    return rex.sub(_repl_unicode, s)
assert replace_unicode(' U+0 ') == ' \0 '


