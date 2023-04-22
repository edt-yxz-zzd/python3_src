

r'''
usage:
if __name__ == '__main__':
    for n in list(globals()): print(n)
    del n; print()

if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    print_global_names(globals())

from seed.helper.print_global_names import print_global_names
    print_global_names_ex
        iter_global_names4export_ex

'''#'''

__all__ = '''
    print_global_names
    print_global_names_ex
        iter_global_names4export_ex
    '''.split()

import re


def print_global_names(names, /, prefix='    , '):
    for n in names:
        if n.startswith('_'): continue
        print(prefix+n)
    print()

def print_global_names_ex(names, /, *, prefix, excluded_names, ___begin_mark_pattern_of_excluded_global_names___, ___end_mark_pattern_of_excluded_global_names___):
    names = iter_global_names4export_ex(names, excluded_names=excluded_names, ___begin_mark_pattern_of_excluded_global_names___=___begin_mark_pattern_of_excluded_global_names___, ___end_mark_pattern_of_excluded_global_names___=___end_mark_pattern_of_excluded_global_names___)
    for nm in names:
        print(prefix+nm)
    print()
def iter_global_names4export_ex(names, /, *, excluded_names, ___begin_mark_pattern_of_excluded_global_names___, ___end_mark_pattern_of_excluded_global_names___):
    'excluded_names:eg. __all__ #to exclude_exported'
    begin_exclude_regex = re.compile(___begin_mark_pattern_of_excluded_global_names___)
    end_exclude_regex = re.compile(___end_mark_pattern_of_excluded_global_names___)
    excluded_names = {*excluded_names}

    exclude = False
    for nm in names:
        if exclude:
            if end_exclude_regex.fullmatch(nm):
                exclude = not exclude
        else:
            if begin_exclude_regex.fullmatch(nm):
                exclude = not exclude
            else:
                if nm.startswith('_'): continue
                if nm in excluded_names: continue
                yield nm

