
__all__ = '''
    Box
    Unbox
    BoxUnbox
    '''.split()

from seed.tiny import echo

def echo_ifNone(f):
    if f is None:
        f = echo
    else:
        assert callable(f)
    return f
class Unbox:
    def __init__(ops, *, unbox):
        ops.__unbox = echo_ifNone(unbox)
    def unbox(ops, obj):
        return ops.__unbox(obj)
class Box:
    def __init__(ops, *, box):
        ops.__box = echo_ifNone(box)
    def box(ops, obj):
        return ops.__box(obj)

class BoxUnbox(Box, Unbox):
    def __init__(ops, *, unbox, box):
        Unbox.__init__(ops, unbox=unbox)
        Box.__init__(ops, box=box)
