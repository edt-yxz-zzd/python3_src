#__all__:goto
#from seed.math.factor_pint_as_pefect_power_ import is_kth_power_, is_square_, is_cube_
r'''[[[
# now:see: math.isqrt() vs floor_sqrt
#bug: O(bisearch-ver:floor_kth_root_) ~ O(log2(k)*log2(n)**2)
O(bisearch-ver:floor_kth_root_) ~ O(log2(n)**3/k) #bisection
O(floor_sqrt) ~ O(log2(n)**2)
O(floor_kth_root_) ~:
    ######################
    let [mmm:=min{k*log2(k), log2(n)}]
    let [lbN:=log2(n)][lblbN:=log2(log2(n))]
    let [lbK:=log2(k)]
    ######################
    ~ O(mmm**3 /k + (lbN -mmm)**2)
    ######################
    ~ [0 <= lbN < k]:O(1)
    ~ [k <= lbN < k*lbK]:O(lbN**3 /k)
    ~ worst[lbN == k*lbK][k==lbN/lblbN]:O(lbN**2 *lblbN)
    ~ [k*lbK < lbN < k*lbK**(3/2)][lbN/lblbN**(3/2) < k < lbN/lblbN]:O(k**2 *lbK**3)
    ~ [lbN > k*lbK**(3/2)]:O(lbN**2)
    ######################
    [lbN == k*lbK] => [k==lbN/lblbN]
    [lbN == k*lbK**(3/2)] => [k==lbN/lblbN**(3/2)]
    [k*lbK < lbN < k*lbK**(3/2)] => [lbN/lblbN**(3/2) < k < lbN/lblbN]
    ######################


[[TODO:
    主要模式:floor_scale_(n/d;expr)
        使用 分数/进一步:分子分母粗略整数分解(c*radix**exp)
        floor运算输入输出限制在整数
        floor之前的scale用于提供精度
    expr主要是:pow,log
        注意:floor_scale_与 浮点数运算的区别:float考虑 误差，误差 可正可负
    [floor_scale_pow(sn/sd;bn/bd;en/ed) =[def]= floor((sn/sd)*(bn/bd)**(en/ed))]
    [floor_scale_log(sn/sd;bn/bd;en/ed) =[def]= floor((sn/sd)*log_((bn/bd),(en/ed)))]
    #######
    参考 浮点数运算:py::decimal.Decimal
    cp ~/../usr/lib/python3.10/_pydecimal.py ~/my_tmp/
    view /sdcard/0my_files/tmp/_pydecimal.py
]]


e ../../python3_src/seed/math/floor_ceil.py
view others/数学/divmod加速.txt
view ../../python3_src/seed/math/floor_ceil_log__via_div_log2.py
view ../../python3_src/seed/math/log__bijective_numeration.py
view ../../python3_src/seed/math/floor_ceil__tiny.py


[[
ls ../../python3_src/seed/math/*{floor,log}*
view ../../python3_src/seed/math/floor_ceil.py
view ../../python3_src/seed/math/floor_ceil__tiny.py
view ../../python3_src/seed/math/discrete_logarithm.py
view ../../python3_src/seed/math/floor_log__Fraction_.py
view ../../python3_src/seed/math/floor_log__ops_.py
view ../../python3_src/seed/math/floor_ceil_log__via_div_log2.py
view ../../python3_src/seed/math/log.py
view ../../python3_src/seed/math/log__bijective_numeration.py
]]



__all__
py -m nn_ns.app.debug_cmd   seed.math.floor_ceil -x
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil:floor_log2 -ht
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil:ceil_log2 -ht

py -m nn_ns.app.doctest_cmd seed.math.floor_ceil:floor_kth_root_ -v
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil:floor_sqrt -v

python -m unittest seed.math.floor_ceil

py -m seed.math.floor_ceil
    now turnoff "timer" related code

py_adhoc_call   seed.math.floor_ceil @floor_log2 =57*59*60*61*71*72*73
42


from seed.math.floor_ceil import floor_div, ceil_div
from seed.math.floor_ceil import floor_div_, ceil_div_
from seed.math.floor_ceil import floor_log2, ceil_log2, floor_ceil_log2
from seed.math.floor_ceil import floor_log2_kth_root_, ceil_log2_kth_root_
from seed.math.floor_ceil import floor_log2_sqrt, ceil_log2_sqrt
from seed.math.floor_ceil import floor_log_, ceil_log_, floor_ceil_log_

# now: math.isqrt
from seed.math.floor_ceil import floor_sqrt, ceil_sqrt
from seed.math.floor_ceil import floor_kth_root_, ceil_kth_root_

#]]]'''

__all__ = r'''
    floor_log2
    ceil_log2
        floor_ceil_log2
    floor_log_
    ceil_log_
        floor_ceil_log_


    floor_log2_kth_root_
    ceil_log2_kth_root_
    floor_log2_sqrt
    ceil_log2_sqrt

    floor_sqrt
    ceil_sqrt

    floor_div
    ceil_div
        floor_div_
        ceil_div_

    offsetted_divmod



    floor_ceil_div
    floor_div
    ceil_div

    ceil_log2
    floor_log2
    offsetted_divmod
    floor_log2_kth_root_
    ceil_log2_kth_root_
    floor_log2_sqrt
    ceil_log2_sqrt
    ceil_sqrt
    floor_sqrt
    floor_kth_root_
    ceil_kth_root_
    floor_lshift_kth_root_
    floor_lshift_sqrt_
    floor_lshift_div_
    ceil_log2_div
    floor_log2_div
    imay_floor_log2
    extended_imay_floor_log2
    count_num_high_same_bits_of_two_uints
    ceil_log_
    floor_log_

    BaseError
        NotPerfectError
        NotPerfectError__div
        NotPerfectError__kth_root
    perfect_div
    perfect_kth_root_
    may_perfect_div
    tmay_perfect_div

    '''.split()#'''
    #load_tests
    #NotImplementedError:
        #floor_log2_pow
        #floor_lshift_log2_


___begin_mark_of_excluded_global_names__0___ = ...
r'''[[[
def __():
    from seed.for_libs.for_time import (
    Timer__print_err
        ,timer__print_err__thread_wide
        ,timer__print_err__process_wide
        ,timer__print_err__system_wide__highest_resolution
        ,timer__print_err__system_wide__monotonic
    )

    timer = timer__print_err__thread_wide
    _to_show_ = __name__ == "__main__"

    with timer(prefix='seed.math.max_power_of_base_as_factor_of_', _to_show_=_to_show_):
        from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers
        #from seed.math.max_power_of_base_as_factor_of_ import count_num_low_0bits_of_pint, count_num_low_1bits_of_uint
    with timer(prefix='seed.func_tools.recur5yield', _to_show_=_to_show_):
        from seed.func_tools.recur5yield import recur5yield__list__echo__echo

    if 0:
        with timer(prefix='unittest', _to_show_=_to_show_):
            import unittest
        with timer(prefix='doctest', _to_show_=_to_show_):
            import doctest
    with timer(prefix='seed.math.floor_ceil', _to_show_=_to_show_):
        if __name__ == "__main__":
            #from seed.math.floor_ceil import *
            pass

#]]]'''#'''

r'''[[[
py -m seed.math.floor_ceil
seed.math.max_power_of_base_as_factor_of_:duration: 0.0019553069999999895 *(unit: 0:00:01)
seed.func_tools.recur5yield:duration: 0.012787081000000033 *(unit: 0:00:01)
seed.math.floor_ceil:duration: 0.11146261600000001 *(unit: 0:00:01)
    ===
    timing 'import unittest, doctest' out from 'import seed.math.floor_ceil' -->:
    unittest:duration: 0.08069130800000002 *(unit: 0:00:01)
    doctest:duration: 0.029753538999999996 *(unit: 0:00:01)
    seed.math.floor_ceil:duration: 0.002877385999999982 *(unit: 0:00:01)

move 'import unittest, doctest' into seed.math.floor_ceil:load_tests() body -->:
    seed.math.max_power_of_base_as_factor_of_:duration: 0.0019774619999999854 *(unit: 0:00:01)
    seed.func_tools.recur5yield:duration: 0.012657305000000008 *(unit: 0:00:01)
    seed.math.floor_ceil:duration: 0.002952691999999979 *(unit: 0:00:01)


#]]]'''
#################################


___end_mark_of_excluded_global_names__0___ = ...
__all__


from seed.math.floor_ceil_tools.fc_perfect import BaseError, NotPerfectError, NotPerfectError__div, NotPerfectError__kth_root
from seed.math.floor_ceil_tools.fc_perfect import perfect_div, perfect_kth_root_, may_perfect_div, tmay_perfect_div


from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2, floor_ceil_log_, floor_ceil_log2
from seed.math.floor_ceil_tools.fc_log import floor_log2_kth_root_, ceil_log2_kth_root_, floor_log2_sqrt, ceil_log2_sqrt

from seed.math.floor_ceil_tools.fc_div import floor_ceil_div, floor_div, ceil_div, ceil_div_, floor_div_, offsetted_divmod



from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt, ceil_sqrt, floor_kth_root_, ceil_kth_root_
from seed.math.floor_ceil_tools.fc_kth_root import floor_lshift_sqrt_, floor_lshift_kth_root_


from seed.math.floor_ceil_tools.fc_log import ceil_log2_div, floor_log2_div
from seed.math.floor_ceil_tools.fc_log import imay_floor_log2, extended_imay_floor_log2, count_num_high_same_bits_of_two_uints
from seed.math.floor_ceil_tools.fc_log import ceil_log_, floor_log_

from seed.math.floor_ceil_tools.fc_div import floor_lshift_div_



















from seed.math.floor_ceil import *
___begin_mark_of_excluded_global_names__1___ = ...
def __():
    if 0 and __name__ == "__main__":
        _t2__floor_log_()
        _t1__floor_log_()
        #raise #0b01 #0b00
    if 0 and __name__ == "__main__":
        import doctest
        doctest.testmod()


    if 0 and __name__ == "__main__":
        assert (1<<1000_000) < float('inf')
        #print(_1_floor_log_.__doc__)

#if __name__ == "__main__":
if 1:
    def __():
        #move into load_tests() body
        #   see: timer()
        import unittest
        import doctest
    def load_tests(loader, tests, ignore):
        import doctest
        tests.addTests(doctest.DocTestSuite(__name__))
        return tests
    #考虑使用unittest+doctest


def __():
    if __name__ == "__main__":
        from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call, AdhocArgParserError, _NOP_
        adhoc_argparser__main__call(globals(), None)
            #main()
___end_mark_of_excluded_global_names__1___ = ...



from seed.math.floor_ceil import perfect_div, perfect_kth_root_
from seed.math.floor_ceil import *
if not __name__ == '__main__':
    raise DeprecationWarning('too slow to be imported, import directly from original module instead')
