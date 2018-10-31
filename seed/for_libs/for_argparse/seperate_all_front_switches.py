
'''
--option
    --switch
--option arg
--option=arg

why?
    to seperate raw unknown args
who use me?
    nn_ns.app.runpy_script_as_module
'''


__all__ = '''
    seperate_all_front_switches
    seperate_all_front_switches_ex
'''.split()


import sys

def seperate_all_front_switches(args):
    '''by insert '--'
'''
    input_switches, script_and_args = seperate_all_front_switches_ex(args)
    fine_args = (*input_switches, '--', *script_and_args)
    return fine_args

def seperate_all_front_switches_ex(args):
    # args unlike sys.argv
    #   sys.argv[0] is the "*.py"
    #   args ~=~ sys.argv[1:]
    #
    if args is None:
        args = sys.argv[1:]
    args = tuple(args)
    ################ insert '--' to seperate switches and args
    L = len(args)
    for i in range(L):
        #if args[i] not in known_switches:
        if args[i] == '--':
            j = i + 1
            break
        elif not args[i].startswith('-'):
            j = i
            break
    else:
        i = L

    input_switches = args[:i]
    script_and_args = args[j:]
    return input_switches, script_and_args






