#__all__:goto
r'''[[[
e ../../python3_src/seed/lang/call_.py


seed.lang.call_
py -m nn_ns.app.debug_cmd   seed.lang.call_ -x
py -m nn_ns.app.doctest_cmd seed.lang.call_:__doc__ -ff -v
py_adhoc_call   seed.lang.call_   @call_ =dir

from seed.lang.call_ import call_

#]]]'''
__all__ = r'''
    call_
'''.split()#'''
__all__




lambda f, /, *args, **kw: f(*args, **kw)
def call_(f, /, *args, **kw):
    d = {**locals()}
    #d['__builtins__'] = {}
    return eval(_code, d, d)
    ###
    #bug:return f(*args, **kw)
    #   eg:f=dir/locals/globals
_code = compile(r'f(*args, **kw)', '<somewhere>', 'eval')


from seed.lang.call_ import call_
from seed.lang.call_ import *
