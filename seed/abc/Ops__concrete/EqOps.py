

__all__ = '''
    EqOps
    python_eq_key_ops
    '''.split()



from .abc import override
from .IEqOps import IEqOps


class EqOps(IEqOps):
    __slots__ = '_EqOps__eq'.split()

    def __init__(self, __eq__):
        assert callable(__eq__)

        self.__eq = __eq__

    @property
    @override
    def eq(ops):
        return ops.__eq


    @override
    def get_args_for_eq_hash(ops):
        return (ops.__eq,)





import operator
python_eq_key_ops = EqOps(operator.__eq__)
del operator


if __name__ == '__main__':
    XXX = EqOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)
