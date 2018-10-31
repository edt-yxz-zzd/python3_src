

__all__ = '''
    has_no_nonlocals
    get_nonlocals
    '''.split()


import inspect
'''
def has_no_closure(f):
    # ClosureVars(nonlocals, globals, builtins, unbound)
    raise
'''

def has_no_nonlocals(f):
    # ClosureVars(nonlocals, globals, builtins, unbound)
    return not get_nonlocals(f)

def get_nonlocals(f):
    # ClosureVars(nonlocals, globals, builtins, unbound)
    closure = inspect.getclosurevars(f)
    return closure.nonlocals









def show_closure(f):
    # ClosureVars(nonlocals, globals, builtins, unbound)
    closure = inspect.getclosurevars(f)
    print(f'nonlocals = {closure.nonlocals}')   # dict
    print(f'globals = {closure.globals}')       # dict
    print(f'builtins = {closure.builtins}')     # dict
    print(f'unbound = {closure.unbound}')       # set


if __name__ == "__main__":
    c = 'c'
    def k():
        return False
    def f1():
        a = 'a'
        def g():
            b = a
            d = c
            if k(): return e
            print(f'g() ==>> a={a}, c={c}')
            return b, d
        g_nonlocals = get_nonlocals(g)
        assert type(g_nonlocals) is dict
        assert g_nonlocals is not locals()
        #print(type(g_nonlocals))
        #print('g_nonlocals is locals(): {}'.format(g_nonlocals is locals()))
        #print('-'*10)
        #print()

        yield g
        for a in range(1):
            yield a

    def f2(range=range):
        a = 'a'
        def g(a=1, c=2):
            b = a
            d = c
            if k(): return e
            print(f'g() ==>> a={a}, c={c}')
            return b, d
        g_nonlocals = get_nonlocals(g)
        assert type(g_nonlocals) is dict
        assert g_nonlocals is not locals()
        #print(type(g_nonlocals))
        #print('g_nonlocals is locals(): {}'.format(g_nonlocals is locals()))
        #print('-'*10)
        #print()

        yield g
        for a in range(1):
            yield a


    def _t(f):
        print('='*60)
        show_closure(f)
        print()
        print()
        it = f()
        def show_g():
            show_closure(g)
            g()
            print()
        for g in it:
            show_g()
            break
        for a in it:
            show_g()
    _t(f1)
    _t(f2)
'''
============================================================
nonlocals = {}
globals = {}
builtins = {'range': <class 'range'>}
unbound = set()


nonlocals = {'a': 'a'}
globals = {'c': 'c', 'k': <function k at 0x00000000029FA2F0>}
builtins = {'print': <built-in function print>}
unbound = {'e'}
g() ==>> a=a, c=c

nonlocals = {'a': 0}
globals = {'c': 'c', 'k': <function k at 0x00000000029FA2F0>}
builtins = {'print': <built-in function print>}
unbound = {'e'}
g() ==>> a=0, c=c

============================================================
nonlocals = {}
globals = {}
builtins = {}
unbound = set()


nonlocals = {}
globals = {'k': <function k at 0x00000000029FA2F0>}
builtins = {'print': <built-in function print>}
unbound = {'e'}
g() ==>> a=1, c=2

nonlocals = {}
globals = {'k': <function k at 0x00000000029FA2F0>}
builtins = {'print': <built-in function print>}
unbound = {'e'}
g() ==>> a=1, c=2
'''
