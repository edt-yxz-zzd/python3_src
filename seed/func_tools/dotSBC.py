
r'''
py -m nn_ns.app.debug_cmd   seed.func_tools.dotSBC

from seed.func_tools.dotSBC import dot, dotC__fT_g, dotB__f_gT, dotS__fT_gT, dotC__f1_g, dotB__f_g1, dotC__fm_g, dotB__f_gm, dotT__fs_gTs_hs, dotT__fs_g1s_hs, dotT__fs_gms_hs


mimic SKIBC
    S f g x = (f x) (g x)
    B f g x = f (g x)
    C f x y = f y x

used in:
    view ../../python3_src/seed/func_tools/fmapT/_xxxT__tiny.py
#'''


__all__ = '''
    dot

    dotS__fT_gT

    dotC__fT_g
    dotB__f_gT

    dotC__f1_g
    dotB__f_g1

    dotC__fm_g
    dotB__f_gm

    dotT__fs_gTs_hs
    dotT__fs_g1s_hs
    dotT__fs_gms_hs
    '''.split()


from seed.func_tools.dot2 import dot



dot = dot
def dotS__fT_gT(fT, gT, /):
    def fT_dot_gT(*args, **kwargs):
        return dot[fT(*args, **kwargs), gT(*args, **kwargs)]
    return fT_dot_gT

def dotC__fT_g(fT, g, /):
    def fT_dot_g(*args, **kwargs):
        return dot[fT(*args, **kwargs), g]
    return fT_dot_g
def dotB__f_gT(f, gT, /):
    def f_dot_gT(*args, **kwargs):
        return dot[f, gT(*args, **kwargs)]
    return f_dot_gT

def dotC__f1_g(f1, g, /):
    def f1_dot_g(x, /):
        return dot[f1(x), g]
    return f1_dot_g
def dotB__f_g1(f, g1, /):
    def f_dot_g1(x, /):
        return dot[f, g1(x)]
    return f_dot_g1

def dotC__fm_g(fm, g, /):
    def fm_dot_g(*args):
        return dot[fm(*args), g]
    return fm_dot_g
def dotB__f_gm(f, gm, /):
    def f_dot_gm(*args):
        return dot[f, gm(*args)]
    return f_dot_gm


def dotT__fs_gTs_hs(fs, gTs, hs, /):
    def fs_dot_gTs_dot_hs(*args, **kwargs):
        gs = (gT(*args, **kwargs) for gT in gTs)
        return dot[(*fs, *gs, *hs)]
    return fs_dot_gTs_dot_hs

def dotT__fs_g1s_hs(fs, g1s, hs, /):
    def fs_dot_g1s_dot_hs(x, /):
        gs = (g1(x) for g1 in g1s)
        return dot[(*fs, *gs, *hs)]
    return fs_dot_g1s_dot_hs

def dotT__fs_gms_hs(fs, gms, hs, /):
    def fs_dot_gms_dot_hs(*args):
        gs = (gm(*args) for gm in gms)
        return dot[(*fs, *gs, *hs)]
    return fs_dot_gms_dot_hs

