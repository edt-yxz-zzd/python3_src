r'''
e ../../python3_src/seed/for_libs/for_operator/__call__.py

no operator.__call__

from seed.for_libs.for_operator.__call__ import caller, __call__, call


'''#'''
__all__ = '''
    caller

    __call__
        call
'''.split()#'''



from operator import __contains__, __eq__, methodcaller

def caller(*args, **kw):
    'vs: operator.methodcaller: caller(...) === methodcaller("__call__", ...)'
    def call(f, /):
        return f(*args, **kw)
    return call
def __call__(f, /, *args, **kw):
    'use case: find().tester: __eq__[value]/__contains__[container]/__call__[predicator]'
    return f(*args, **kw)
call = __call__



from seed.for_libs.for_operator.__call__ import caller, __call__, call

