
r'''
py -m nn_ns.app.debug_cmd seed.debug.audit

#'''


___begin_mark_of_excluded_global_names__0___ = ...
from seed.debug._debug import main__print_infos_of_modules#, print_unbound_names_of_modules, print_global_names_of_modules, print_toplevel_def_heads_of_modules
___end_mark_of_excluded_global_names__0___ = ...


def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='debugging py modules'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('module_qual_names', type=str, default=[], nargs='+'
                        , help='python module qual_names')

    args = parser.parse_args(args)
    qnames = args.module_qual_names
    main__print_infos_of_modules(qnames)


if __name__ == "__main__":
    main()






