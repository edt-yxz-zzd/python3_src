
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
    parser.add_argument('-x', '--exclude_exported', action='store_true'
                        , default = False
                        , help='exclude names listed in module.__all__')
    parser.add_argument('-off_defs', '--not_show_toplevel_def_heads', action='store_true'
                        , default = False
                        , help='not show head lines of module toplevel "def"/"class"/"="')

    args = parser.parse_args(args)
    qnames = args.module_qual_names
    exclude_exported = args.exclude_exported
    main__print_infos_of_modules(qnames, exclude_exported=exclude_exported, to_show_toplevel_def_heads=not args.not_show_toplevel_def_heads)


if __name__ == "__main__":
    main()






