
#e ../../python3_src/seed/abc/Ops__concrete/ITotalOrderingOps.py

__all__ = '''
    TotalOrderingOps
    python_total_key_ops
    '''.split()



from .abc import override
from .ITotalOrderingOps import ITotalOrderingOps, ITotalOrderingOps__via_cmp


class TotalOrderingOps(ITotalOrderingOps):
    __slots__ = '_TotalOrderingOps__le _TotalOrderingOps__eq'.split()

    def __init__(self, __le__, __eq__):
        assert callable(__le__)
        assert callable(__eq__)

        self.__le = __le__
        self.__eq = __eq__

    @property
    @override
    def le(ops):
        return ops.__le
    @property
    @override
    def eq(ops):
        return ops.__eq



    @override
    def get_args_for_eq_hash(ops):
        return (ops.__le, ops.__eq)

import operator
python_total_key_ops = TotalOrderingOps(operator.__le__, operator.__eq__)
del operator



def _t():
    assert python_total_key_ops.eq(1, 1)
    assert not python_total_key_ops.ne(1, 1)
    assert not python_total_key_ops.eq(1, 2)
    assert python_total_key_ops.ne(1, 2)
    assert not python_total_key_ops.eq(2, 1)
    assert python_total_key_ops.ne(2, 1)

    assert not python_total_key_ops.gt(1, 2)
    assert not python_total_key_ops.ge(1, 2)
    assert python_total_key_ops.lt(1, 2)
    assert python_total_key_ops.le(1, 2)

    assert not python_total_key_ops.le(2, 1)
    assert not python_total_key_ops.lt(2, 1)
    assert python_total_key_ops.ge(2, 1)
    assert python_total_key_ops.gt(2, 1)

    assert python_total_key_ops.le(1, 1)
    assert not python_total_key_ops.lt(1, 1)
    assert python_total_key_ops.ge(1, 1)
    assert not python_total_key_ops.gt(1, 1)


from seed.abc.Ops__concrete.TotalOrderingOps import TotalOrderingOps
from seed.abc.Ops__concrete.TotalOrderingOps import *

if __name__ == '__main__':
    _t()

if __name__ == '__main__':
    XXX = TotalOrderingOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)
