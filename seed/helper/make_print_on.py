


def make_print_on(verbose):
    if verbose:
        oprint = print
    else:
        def oprint(*args, **kwargs):pass
    return oprint


