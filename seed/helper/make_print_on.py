
__all__ = 'make_print_on'.split()

def make_print_on(verbose):
    if verbose:
        oprint = print
    else:
        def oprint(*args, **kwargs):pass
    return oprint

from seed.helper.make_print_on import make_print_on
