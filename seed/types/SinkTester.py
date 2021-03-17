
r'''
from seed.types.SinkTester import SinkTester
from seed.types.SinkTester import BaseTester, base_assert, base_test
from seed.types.SinkTester import BaseTesterError, BaseTesterError4then, BaseTesterError4if

see:
    seed.types.Tester
    seed.types.SinkTester
#'''


__all__ = '''
    SinkTester
        BaseTester
            base_assert
            base_test

    BaseTesterError
        BaseTesterError4then
        BaseTesterError4if
    '''.split()


from seed.types.Tester import is_good, ITester
from seed.abc.IReprImmutableHelper import IReprImmutableHelper
from seed.abc.abc import ABC, abstractmethod, override
class SinkTester(IReprImmutableHelper):
    def __init__(sf, if_tester:ITester, then_tester:ITester):
        if not isinstance(if_tester, ITester): raise TypeError
        if not isinstance(then_tester, ITester): raise TypeError
        sf.__if_tester = if_tester
        sf.__then_tester = then_tester
    def if_test(sf, x):
        return is_good(sf.__if_tester, x)
    def then_test(sf, x):
        return is_good(sf.__then_tester, x)
    @property
    def if_tester(sf):
        return sf.__if_tester
    @property
    def then_tester(sf):
        return sf.__then_tester
    @override
    def ___get_args_kwargs___(sf):
        return [sf.if_tester, sf.then_tester], {}






class BaseTesterError(Exception):pass
class BaseTesterError4then(BaseTesterError, ValueError):pass
class BaseTesterError4if(BaseTesterError, TypeError):pass

BaseTester = (ITester, SinkTester)
def base_assert(base_tester, obj):
    'BaseTester -> obj -> None|raise BaseTesterError4then/BaseTesterError4if'
    if not base_test(base_tester, obj): raise BaseTesterError4if
    return
def base_test(base_tester, obj):
    'BaseTester -> obj -> bool|raise BaseTesterError4then'
    if isinstance(base_tester, SinkTester):
        sink_tester = base_tester
        if sink_tester.if_test(obj):
            if sink_tester.then_test(obj):
                return True
            else:
                raise BaseTesterError4then#ValueError
        else:
            return False
    else:
        tester = base_tester
        return is_good(tester, obj)




BaseTesterError
BaseTesterError4then
BaseTesterError4if
BaseTester
base_assert
base_test

