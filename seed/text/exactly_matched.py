
import re

__all__ = ('exactly_matched_raw', 'exactly_matched')
RexType = compiled_rex_type = type(re.compile(''))

def exactly_matched_raw(pattern, string):
    #if isinstance(pattern, (str, bytes, bytearray)):
    rex = re.compile(pattern)
    return exactly_matched(rex, string)

def exactly_matched(rex, string, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(string)
    m = rex.match(string, start, end)
    if m:
        assert m.start() == start
        return m.end() == end
    return False
