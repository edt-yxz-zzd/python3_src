
"""
if __name__ == '__main__':
    classes = [XXX]
    excludes = '''
        logic
        error
        '''.split()

    from seed.helper.ongo import main
    main(modules=[__name__], classes=classes, excludes=excludes)
"""

__all__ = '''
    main
    '''.split()

def main(*, modules, classes, excludes):
    for_modules(*modules, excludes=excludes)
    for_classes(*classes)

def for_modules(*qnames, excludes=()):
    from seed.pkg_tools.dectect_all_unbound_names import DectectAllUnboundNames

    excludes = frozenset(excludes)
    for __name__ in qnames:
        print('='*70)
        print(f'module: {__name__}')
        unbound_names = forgots = (DectectAllUnboundNames.from_module_qname(__name__))
        unbound_names = frozenset(unbound_names)
        unbound_names -= excludes
        if unbound_names:
            print(f'module: {__name__} forgots:')
            for unbound_name in unbound_names:
                print('\t', unbound_name)

def for_classes(*XXXs):
    for XXX in XXXs:
        print('-'*50)
        print(f'class: {XXX}')
        for_class(XXX)

def for_class(XXX):
    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)





