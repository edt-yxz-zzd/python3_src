
_debug_ = True
_debug_ = False

if _debug_:
    from seed.tiny import print_err
    from seed.tiny import print_ferr
else:
    from seed.tiny import no_op as print_err
    from seed.tiny import no_op as print_ferr


#print_ferr(lambda: f'{i}')


