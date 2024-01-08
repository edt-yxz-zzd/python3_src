#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_.py
usage:
    input: data from oeis of format:
        1 xxx
        2 xxx
        3 xxx
        4 xxx
        ... ...
        ... ...
    output:
        0 2 xxx
        1 3 xxx
        2 5 xxx
        3 7 xxx
        ... ...
        ... ...

nn_ns.math_nn.numbers._patch_prime_
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers._patch_prime_ -x
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers._patch_prime_:__doc__ -ff -v
from nn_ns.math_nn.numbers._patch_prime_ import *



ls ../../python3_src/nn_ns/math_nn/numbers/
view ../../python3_src/nn_ns/math_nn/numbers/b001918-least_positive_primitive_root_of_n_th_prime__fst_10000.txt
view ../../python3_src/nn_ns/math_nn/numbers/b002233-least_positive_prime_primitive_root_of_n_th_prime__except_0th__fst_10000.txt

py_adhoc_call   nn_ns.math_nn.numbers._patch_prime_   @main1 --ipath:../../python3_src/nn_ns/math_nn/numbers/b001918-least_positive_primitive_root_of_n_th_prime__fst_10000.txt
py_adhoc_call   nn_ns.math_nn.numbers._patch_prime_   @mains      :../../python3_src/nn_ns/math_nn/numbers/b001918-least_positive_primitive_root_of_n_th_prime__fst_10000.txt       :../../python3_src/nn_ns/math_nn/numbers/b002233-least_positive_prime_primitive_root_of_n_th_prime__except_0th__fst_10000.txt      --opath:../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt



#]]]'''
__all__ = r'''
    main1
    mains
'''.split()#'''
__all__

from contextlib import ExitStack
from nn_ns.math_nn.numbers.prime_number import PRIMES

from seed.io.may_open import open4wt, open4wt_err, open4rt
#def open4wt(may_opath, /, *, force, encoding):
#def open4rt(may_ipath, /, *, encoding):

def main1(*, ipath=None, opath=None, encoding='utf8', force=False, flush=False):
    with open4rt(ipath, encoding=encoding) as ifile:
        with open4wt(opath, encoding=encoding, force=force) as ofile:
            _mains_([ifile], ofile, flush=flush)
def mains(*may_ipaths, opath=None, encoding='utf8', force=False, flush=False):
    with ExitStack() as stack:
        ifiles = [stack.enter_context(open4rt(may_ipath, encoding=encoding)) for may_ipath in may_ipaths]
        with open4wt(opath, encoding=encoding, force=force) as ofile:
            _mains_(ifiles, ofile, flush=flush)

def _mains_(ifiles, ofile, /, *, flush):
    assert ifiles
    for i, j2str4payload in enumerate(zip(*map(_iter_payload_strs_, ifiles))):
        p = PRIMES[i]
        y = ' '.join(j2str4payload)
        s = f'{i} {p} {y}'
        print(s, file=ofile, flush=flush)

def _iter_payload_strs_(ifile, /):
    blank_line_occured = False
    for i, line in enumerate(ifile):
        ls = line.split()
        if not ls:
            # [line is blank]
            blank_line_occured = True
            continue
        # [not$ line is blank]
        if blank_line_occured: raise Exception('non-blank_line occurs after blank_line_occured')
        if not len(ls) == 2: raise Exception((i, line))
        str4k, str4payload = ls
        if not str4k == str(i+1): raise Exception((i, line))
        yield str4payload

if __name__ == "__main__":
    pass
__all__


from nn_ns.math_nn.numbers._patch_prime_ import *
