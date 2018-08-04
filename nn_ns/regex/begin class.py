
__all__ = '''
    YYY
    '''.split()

from .abc import abstractmethod, not_implemented, override
from .IFAOps import IFAOps


if __name__ == '__main__':
    XXX = YYY

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)
