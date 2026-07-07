#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py
view ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers__7py_adhoc_call.py

view ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py.primes.dat
    _init_fill_zpow_le3000_
view ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py.default.db
    _iter_fill7fixed_base_
grep '^[^,]*$' ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py.default.db -n
grep '^[^,]*$' ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py.default.db -c
    246/2991:比率真低



seed.math.factor_pint.database4factors4cyclotomic_numbers
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.database4factors4cyclotomic_numbers -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.database4factors4cyclotomic_numbers:__doc__ -ht # -ff -df
#######

[[
come_from:
view others/app/termux/help/gp-example.txt
===
循环小数循环节长度:1/N:order_mod_(N;10), factorint(-1+10^k)
TODO:factorint(cyclotomic_polynomial(d)(b))
view ../../python3_src/seed/math/polynomial/eval_polynomial/cyclotomic_polynomial.py
view ../../python3_src/nn_ns/math_nn/factor_Mersenne_number_into_prime2exp.py.cached.txt
    [1..=3000]之间缺失815个
    [1..=3000]之间只有2185个
    首缺M1207
]]
[[
[cyclotomic_number{base;N} := poly_eval_(cyclotomic_polynomial{N};base)]
[[base::uint{>=2}][p::prime][base%p =!= 0] -> [N:=order_mod_(p;base)][ccltmc:=cyclotomic_number{base;N}][pwmm:=(-1+base**N)] -> [pwmm%p == 0][pwmm%ccltmc == 0][ccltmc%p == 0][(pwmm///ccltmc)%p =!= 0]]
    #但是 逆命题不成立: ccltmc的素因子q不见得有[N==order_mod_(q;base)]
[[base::uint{>=2}][N::uint{>=1}][ccltmc:=cyclotomic_number{base;N}][pwmm:=(-1+base**N)] -> [q::prime][ccltmc%q == 0] -> [pwmm%q == 0][base%q =!= 0][N%order_mod_(q;base) == 0]]

]]
[[
[order_of_mulgroup_of_finite_field{p;k} == (-1+p**k) == II[cyclotomic_number{p;d} | [[d:<-[1..=k]][k%d==0]]]]
    # [x**p**k == x]
    # [x*(-1+x**(-1+p**k)) == 0]
]]
[[
Cunningham numbers
===
6.2 Number field sieve
Special number field sieve (SNFS)
page299[309/604]
The SNFS has principally been used to factor many Cunningham numbers (these are numbers of the form b^k±1 for b = 2,3,5,6,7,10,11,12, see [Brillhart et al. 1988]).

[Brillhart et al. 1988] J. Brillhart, D. Lehmer, J. Selfridge, B. Tuckerman, and S. Wagstaff, Jr. Factorizations of b^n±1, b = 2,3,5,6,7,10,11,12 up to high powers. Second edition, volume 22 of Contemporary Mathematics. Amer. Math. Soc., 1988.
]]




'#'; __doc__ = r'#'
>>>



view ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers__7py_adhoc_call.py



py_adhoc_call   seed.math.factor_pint.database4factors4cyclotomic_numbers   @validate_cyclotomic_numbers6base_and_order_  =None  =7 =60 =None

py_adhoc_call   seed.math.factor_pint.database4factors4cyclotomic_numbers   @f

]]]'''#'''
__all__ = r'''
validate_cyclotomic_numbers6base_and_order_
db5may_db_
    load_default_db_
    iter_collect_missing_orders_
        iter_collect_missing_orders7flatten_
        set_record5external_

mk_database4factors4cyclotomic_numbers_
    mk_factor_pint_func5or_qname_or_timeout_
    Database4Factors4CyclotomicNumbers


load_database5ipath_
    load_database5ifile_
        iter_records5ifile_
            parse4record_
append_record2opath_
    append_record2ofile_
        repr4record_

GlobalPaths
'''.split()#'''
    #_init_fill_zpow_le3000_
    #_load_primes4zpowmm_
    #
    #_fill7fixed_base_
    #_iter_fill7fixed_base_
    #
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from collections.abc import Callable, Mapping, Sequence
from numbers import Number
from io import SEEK_END
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.all_factors_of_ import sorted_all_factors5factorization_
    from seed.math.prepare_p2e4N import prepare_p2e4N_
    #def prepare_p2e4N_(N, may_p2e4N_or_ps4N_or_factor_pint_func, /):
    from seed.math.polynomial.eval_polynomial.cyclotomic_polynomial import cyclotomic_polynomial5order_
    #def cyclotomic_polynomial5order_(cache, N, may_p2e4N_or_ps4N_or_factor_pint_func, /):
    from seed.math.polynomial.eval_polynomial.eval_polynomial7native import poly_eval_
    #def poly_eval_(add_, mul_, zero, coeffs8poly, x, /):
    from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division, semi_factor_pint_via_trial_division
    from seed.math.primality_test.strong_probable_prime import detect_strong_probable_prime__not_waste_too_much_time_
    from seed.math.factor_pint.factorint6PARI_GP_ import mk_factorint6PARI_GP__7fixed_timeout_
    from seed.pkg_tools.import_object import import_object
    from pathlib import Path
    from seed.tiny_.check_path import check_not_dir_path_ #check_dir_path_
    from seed.tiny_.check import check_type_is, check_callable, check_int_ge
    from seed.pkg_tools.load_resource import read_under_pkg_
    #def read_under_pkg_(pkg, basename, /, *, xencoding, **kwds):
    #def open_under_pkg_(pkg, basename, /, *, xencoding, **kwds):

    #from seed.math.prime_sieve.sieve_ge_le import iter_sieve4prime_factorizations_ge_lt_
    from seed.math.prime_sieve.sieve_lt import tabulate_may_prime_factorization4uint_lt_

    from seed.math.factor_pint.perfect_power.detect_perfect_power import is_perfect_power_

    from seed.for_libs.for_time import mk_rest_func_
    #def mk_rest_func_(休眠期, 苏醒期, /, *, time_kind='process_wide'):
    #usage:
    #   def f(..., 休眠期=0.0, 苏醒期=2.0, ...):
    #       _rest = mk_rest_func_(休眠期, 苏醒期)
    #       while ...:
    #           777;_rest()

    from time import sleep
    from ast import literal_eval
    from itertools import groupby, islice
#.    from functools import cached_property
#.#################################
___end_mark_of_excluded_global_names__0___ = ...
def _1_collect_missing_orders_(orders, /):
    '-> missing_orders/[order]'
    orders = sorted(orders)
    assert orders
    end = 1+orders[-1]
    begin = 1+orders[0]
    check_int_ge(1, begin)
    order_set = set(orders)
    assert len(order_set) == len(orders)
    whole_set = set(range(1, end))
    assert order_set <= whole_set
    missing_orders = tuple(sorted(whole_set -order_set))
    return missing_orders

def _2_iter_collect_missing_orders_(base2orders, bases7skipped, /):
    '-> Iter (base, missing_orders/[order]{len>0})'
    for base, orders in sorted(base2orders.items()):
        if base in bases7skipped:
            continue
        missing_orders = _1_collect_missing_orders_(orders)
        if missing_orders:
            yield (base, missing_orders)

class Database4Factors4CyclotomicNumbers:
    '[on_new_ :: (base, order, [prime]) -> None][on_del_ :: [(base, order, [prime])] -> None][factor_pint_func :: uint{>=1} -> {prime:exp{>=1}}|^TimeoutError]'
    def __init__(sf, on_new_, on_del_, factor_pint_func, may_base2order2factors=None, /, *, validate=False):
        #def __init__(sf, ipath_or_ifile_or_may_base2order2factors=None, /, *, validate=False):
        check_callable(on_new_)
        check_callable(on_del_)
        check_callable(factor_pint_func)
        sf._f = factor_pint_func
        sf._on_new = on_new_
        sf._on_del = on_del_
        sf._news = []
        sf._cache4base = {}
            # {base:ok/bool}
        sf._cache4poly = {}
            # {N:cs}
        sf._cache4number = {}
            # {base:{N:cyclotomic_number}}
        sf._cache4factors = sf._set_db_(may_base2order2factors)
            # {base:{N:[prime_factor]}}
        if validate: sf.validate_()
    def __del__(sf, /):
        sf._on_del(sf._news)
        try:
            f = super(__class__, type(sf)).__del__
        except AttributeError:
            pass
        else:
            f(sf)
        return
        #AttributeError: 'super' object has no attribute '__del__'
        super(__class__, type(sf)).__del__(sf)
        super(__class__, sf).__del__()
        super().__del__()

    @property
    def factor_pint_func(sf, /):
        return sf._f
    def _set_db_(sf, may_base2order2factors, /):
        if may_base2order2factors is None:
            d = {}
        else:
            base2order2factors = may_base2order2factors
            d = dict(base2order2factors)
            d = {base:dict(order2factors) for base, order2factors in d.items()}
            d = {base:{order:tuple(factors) for order, factors in order2factors.items()} for base, order2factors in d.items()}
        return d
    def collect_missing_orders_(sf, /, *, bases7skipped=None):
        '-> base2missing_orders/{base:[order]}'
        return dict(sf.iter_collect_missing_orders_(bases7skipped=bases7skipped))
    def iter_collect_missing_orders_(sf, /, *, bases7skipped=None):
        '-> Iter (base, missing_orders/[order]{len>0})'
        b2d2ps = sf._cache4factors
        bases7skipped = frozenset(bases7skipped) if bases7skipped else ()
        return _2_iter_collect_missing_orders_(b2d2ps, bases7skipped)
    def iter_collect_missing_orders7flatten_(sf, /, *, bases7skipped=None):
        '-> Iter (base, missing_order, p2e4order, cyclotomic_number)'
        ls = list(sf.iter_collect_missing_orders_(bases7skipped=bases7skipped))
        if not ls:
            return
        max4N = max(Ns[-1] for base, Ns in ls)
        u2p2e = tabulate_may_prime_factorization4uint_lt_(1+max4N)
        for base, Ns in ls:
            for N in Ns:
                p2e4N = u2p2e[N]
                ccltmc = sf.cyclotomic_number5base_and_order_(base, N, p2e4N)
                yield (base, N, p2e4N, ccltmc)

    def validate_(sf, may_factor_pint_func=None, /):
        b2d2ps = sf._cache4factors
        if may_factor_pint_func is None:
            may_factor_pint_func = sf.factor_pint_func
        for base, d2ps in sorted(b2d2ps.items()):
            sf._check_base_via_cache_(base)
            for N, ps in sorted(d2ps.items()):
                check_int_ge(1, N)
                sf._validate1_(base, N, ps, may_factor_pint_func)
    def _check_base_via_cache_(sf, base, /):
        check_int_ge(2, base)
        d = sf._cache4base
        if not None is (ok:=d.get(base)):
            if not ok:raise ValueError('is_perfect_power_:', base)
            return
        ok = not is_perfect_power_(base)
        check_type_is(bool, ok)
        d[base] = ok
        sf._check_base_via_cache_(base)
    def _validate1_(sf, base, N, ps, may_p2e4N_or_ps4N_or_factor_pint_func, /):
        check_type_is(tuple, ps)
        check_int_ge(1, N)
        sf._check_base_via_cache_(base)
        if may_p2e4N_or_ps4N_or_factor_pint_func is None:
            may_p2e4N_or_ps4N_or_factor_pint_func = sf.factor_pint_func
        for p in ps:
            check_int_ge(2, p)
            if not (p&1 or p==2):raise AssertionError(p)
            if 0 == detect_strong_probable_prime__not_waste_too_much_time_(p):raise AssertionError(p)
        ps
        ccltmc = sf.cyclotomic_number5base_and_order_(base, N, may_p2e4N_or_ps4N_or_factor_pint_func)
        p2e = complete_factor_pint_via_trial_division(ps, ccltmc)
        if not len(p2e) == len(ps):raise AssertionError(base, N, ps, p2e)
    def cyclotomic_polynomial5order_(sf, N, may_p2e4N_or_ps4N_or_factor_pint_func, /):
        check_int_ge(1, N)
        if may_p2e4N_or_ps4N_or_factor_pint_func is None:
            may_p2e4N_or_ps4N_or_factor_pint_func = sf.factor_pint_func
        return cyclotomic_polynomial5order_(sf._cache4poly, N, may_p2e4N_or_ps4N_or_factor_pint_func)
    def cyclotomic_number5base_and_order_(sf, base, N, may_p2e4N_or_ps4N_or_factor_pint_func, /):
        b2d2n = sf._cache4number
        try:
            return b2d2n[base][N]
        except KeyError:
            pass
        check_int_ge(1, N)
        sf._check_base_via_cache_(base)

        cs = sf.cyclotomic_polynomial5order_(N, may_p2e4N_or_ps4N_or_factor_pint_func)
        ccltmc = poly_eval_(int.__add__, int.__mul__, 0, cs, base)
        if not (pw:=pow(base, N, ccltmc)) == 1%ccltmc:raise AssertionError(base, N, cs, ccltmc, pw)
        b2d2n.setdefault(base, {}).setdefault(N, ccltmc)
        return sf.cyclotomic_number5base_and_order_(base, N, NotImplemented)

    def __contains__(sf, k, /):
        #check_type_is(tuple, k)
        b2d2ps = sf._cache4factors
        match k:
            case tuple((base, N)):
                return (d2ps:=b2d2ps.get(base)) and N in d2ps
            case int(base):
                return base in b2d2ps
            case _:
                raise TypeError(k)
    def _unpack_key(sf, k, /):
        check_type_is(slice, k)
        match k:
            case slice(start=base, stop=N, step=may_p2e4N_or_ps4N_or_factor_pint_func):
                pass
            case _:
                raise TypeError(k)
        return (base, N, may_p2e4N_or_ps4N_or_factor_pint_func)
    def __setitem__(sf, k, ps, /):
        (base, N, may_p2e4N_or_ps4N_or_factor_pint_func) = sf._unpack_key(k)
        sf._validate1_(base, N, ps, may_p2e4N_or_ps4N_or_factor_pint_func)
        b2d2ps = sf._cache4factors
        may_ps = b2d2ps.get(base, {}).get(N, None)
        is_new = may_ps is None
        _ps = b2d2ps.setdefault(base, {}).setdefault(N, ps)
        if not ps == _ps:raise AssertionError(base, N, ps, _ps)
        if is_new:
            record = (base, N, ps)
            sf._news.append(record)
            sf._on_new(record)
    def __getitem__(sf, k, /):
        (base, N, may_p2e4N_or_ps4N_or_factor_pint_func) = sf._unpack_key(k)
        b2d2ps = sf._cache4factors
        try:
            return b2d2ps[base][N]
        except KeyError:
            pass
        ccltmc = sf.cyclotomic_number5base_and_order_(base, N, may_p2e4N_or_ps4N_or_factor_pint_func)
        p2e = sf.factor_pint_func(ccltmc)
        ps = tuple(sorted(p2e))
        if 0:
            _p2e = complete_factor_pint_via_trial_division(ps, ccltmc)
            if not len(p2e) == len(_p2e):raise AssertionError(base, N, p2e, _p2e)
            b2d2ps.setdefault(base, {}).setdefault(N, ps)
        else:
            sf[base:N] = ps
        return sf[base:N]
#end-class Database4Factors4CyclotomicNumbers:

def __():
  def _load3_(ipath_or_ifile_or_may_base2order2factors, /):
    match ipath_or_ifile_or_may_base2order2factors:
        case None:
            base2order2factors = {}
        case Mapping(base2order2factors):
            pass
        case object(readline=Callable()) as ifile:
            base2order2factors = load_database5ifile_(ifile)
        case Sequence(ipath):
            with open(ipath, 'rt', encoding='u8') as ifile:
                base2order2factors = load_database5ifile_(ifile)
        case _:
            raise TypeError(ipath_or_ifile_or_may_base2order2factors)
    return base2order2factors
  def raw_mk_database4factors4cyclotomic_numbers_(on_new_, on_del_, factor_pint_func__or__qname__or__timeout, ipath_or_ifile_or_may_base2order2factors=None, /, *, validate=False):
    '[on_new_ :: (base, order, [prime]) -> None][on_del_ :: [(base, order, [prime])] -> None][factor_pint_func :: uint{>=1} -> {prime:exp{>=1}}|^TimeoutError]'
    factor_pint_func = mk_factor_pint_func5or_qname_or_timeout_(factor_pint_func__or__qname__or__timeout)
    base2order2factors = _load3_(ipath_or_ifile_or_may_base2order2factors)
    db = Database4Factors4CyclotomicNumbers(on_new_, on_del_, factor_pint_func, base2order2factors, validate=validate)
    return db
__




def mk_factor_pint_func5or_qname_or_timeout_(factor_pint_func__or__qname__or__timeout, /):
    match factor_pint_func__or__qname__or__timeout:
        case Callable() as factor_pint_func:
            pass
        case str() as qnm:
            factor_pint_func = import_object(qnm)
        case Number() as timeout:
            if not timeout >= 0:raise ValueError(timeout)
                #allow 0 to show all fails fast@_iter_fill7fixed_base_()
            factorint6PARI_GP_ = mk_factorint6PARI_GP__7fixed_timeout_(timeout)
            factor_pint_func = factorint6PARI_GP_
        case _:
            raise TypeError(factor_pint_func__or__qname__or__timeout)
    return factor_pint_func
def __():
  if 0:
    from seed.int_tools.int_repr7human7lex_order7alnum import encode_int2txt7human7lex_order7alnum7headU_, decode_int5txt7human7lex_order7alnum7headU_
        # encode_int2txt7human7lex_order7alnum7headU_(int, /, *, validate=True) -> str
        # decode_int5txt7human7lex_order7alnum7headU_(txt, begin=None, end=None, /, *, validate=True) -> int
# encode_int2txt7human7lex_order7alnum7headU_(int, /, *, validate=True) -> str
# decode_int5txt7human7lex_order7alnum7headU_(txt, begin=None, end=None, /, *, validate=True) -> int
  def _encode4base_(base, /):
    check_int_ge(2, base)
    str8base = encode_int2txt7human7lex_order7alnum7headU_(base)
    return str8base
  def _decode4base_(str4base, /):
    base = decode_int5txt7human7lex_order7alnum7headU_(str4base)
    check_int_ge(2, base)
    return base

def load_database5ipath_(ipath, /):
    with open(ipath, 'rt', encoding='ascii') as ifile:
        return load_database5ifile_(ifile)
def load_database5ifile_(ifile, /):
    base2order2factors = {}
    for (base, N, ps) in iter_records5ifile_(ifile):
        check_type_is(tuple, ps)
        order2factors = base2order2factors.setdefault(base, {})
        #order2factors.setdefault(N, ps)
        order2factors[N] = ps #overwrite
    return base2order2factors
def iter_records5ifile_(ifile, /):
    for line in ifile:
        s = line.strip()
        if not s or s.startswith('#'):continue
        yield parse4record_(s)
def parse4record_(s, /):
    (base, N, ps) = map(literal_eval, s.split(':', 2))
    check_int_ge(2, base)
    check_int_ge(1, N)
    check_type_is(list, ps)
    ps = tuple(ps)
    record = (base, N, ps)
    return record
def _check4record_(record, /):
    check_type_is(tuple, record)
    (base, N, ps) = record
    check_int_ge(2, base)
    check_int_ge(1, N)
    check_type_is(tuple, ps)
def repr4record_(record, /):
    _check4record_(record)
    (base, N, ps) = record
    ps = list(ps)
    return f'{base}:{N}:{ps}'
def append_record2ofile_(ofile, record, /):
    ofile.seek(0, SEEK_END)
    s = repr4record_(record)
    print(s, file=ofile, flush=True)
def append_record2opath_(opath, record, /):
    with open(opath, 'at', encoding='ascii') as ofile:
        append_record2ofile_(ofile, record)
def mk_database4factors4cyclotomic_numbers_(path4io, factor_pint_func__or__qname__or__timeout, /, *, hold_file=False, validate=False):
    factor_pint_func = mk_factor_pint_func5or_qname_or_timeout_(factor_pint_func__or__qname__or__timeout)
    path4io = Path(path4io)
    check_not_dir_path_(path4io)
    path4io.touch()
    base2order2factors = load_database5ipath_(path4io)
        #read before ofile

    if hold_file:
        ofile = open(path4io, 'at', encoding='ascii')
        def on_new_(record, /):
            append_record2ofile_(ofile, record)
        def on_del_(new_records, /):
            with ofile:pass
    else:
        def on_new_(record, /):
            append_record2opath_(path4io, record)
        def on_del_(new_records, /):
            pass; return
    #SaveFile
    #view ../../python3_src/seed/io/savefile/unbuffered_growonly_dict_in_file.py
    db = Database4Factors4CyclotomicNumbers(on_new_, on_del_, factor_pint_func, base2order2factors, validate=validate)
    return db
TimeoutError

__all__
class GlobalPaths:
    basename4primes4zpowmm = __name__.rpartition('.')[-1] +'.py.primes.dat'
    basename4default_db = __name__.rpartition('.')[-1] +'.py.default.db'
def _load_primes4zpowmm_():
    # [base==2]
    #view ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py.primes.dat
    s = read_under_pkg_(__package__, GlobalPaths.basename4primes4zpowmm, xencoding='utf8')
    d = {}
    exec(s, d)
    if 0:
        del d['__doc__']
        del d['__builtins__']
        try:
            [(nm, ps)] = d.items()
        except ValueError:
            #ValueError: too many values to unpack (expected 1)
            print(sorted(d))
            raise
        ps
    else:
        ps = d['_primes5p2e6doc']
    ps = tuple(ps)
    return ps

def load_default_db_(*, hold_file:bool, timeout:int):
    #def load_default_db_(*, hold_file=False, timeout=600):
    check_int_ge(0, timeout)
    path4io = Path(__file__).parent/ GlobalPaths.basename4default_db
    default_db = mk_database4factors4cyclotomic_numbers_(path4io, timeout, hold_file=hold_file)
    return default_db
def db5may_db_(may_db, /, *, timeout6default_db=600, hold_file6default_db=False):
    db = may_db if not may_db is None else load_default_db_(hold_file=hold_file6default_db, timeout=timeout6default_db)
    check_type_is(Database4Factors4CyclotomicNumbers, db)
    return db
def iter_collect_missing_orders7flatten_(may_db, /, *, bases7skipped=None, **kwds6default_db):
    '-> Iter (base, missing_order, p2e4order, cyclotomic_number)'
    db = db5may_db_(may_db, **kwds6default_db)
    return db.iter_collect_missing_orders7flatten_(bases7skipped=bases7skipped)
def iter_collect_missing_orders_(may_db, /, *, bases7skipped=None, **kwds6default_db):
    '-> Iter (base, missing_orders/[order]{len>0})'
    db = db5may_db_(may_db, **kwds6default_db)
    return db.iter_collect_missing_orders_(bases7skipped=bases7skipped)
def set_record5external_(may_db, record, may_p2e4N_or_ps4N_or_factor_pint_func, /, **kwds6default_db):
    'to use external known factorization to patch internal failures'
    _check4record_(record)
    (base, N, ps) = record
    db = db5may_db_(may_db, **kwds6default_db)
    db[base:N:may_p2e4N_or_ps4N_or_factor_pint_func] = ps
        #__setitem__
def _init_fill_zpow_le3000_(may_db, /, *, verbose=False, **kwds6default_db):
    db = db5may_db_(may_db, **kwds6default_db)

    base = 2
    max4N = 3000
    ps7lots = _load_primes4zpowmm_()
    if verbose:print('sz:', len(ps7lots))
    def try_factor_pint_(u, /, *, ps7lots=ps7lots):
        (p2e, _u) = semi_factor_pint_via_trial_division(ps7lots, u)
        may_p2e = None if not _u == 1 else p2e
        return may_p2e
    u2p2e = tabulate_may_prime_factorization4uint_lt_(1+max4N)
    it = enumerate(u2p2e)
    777;next(it)
    #vs:it = iter_sieve4prime_factorizations_ge_lt_(1, 1+max4N, with_uint=True)
    for N, p2e4N in it:
        if verbose:print('0:', N)
        if (base, N) in db:continue
        if verbose:print('1:', N)
        ccltmc = db.cyclotomic_number5base_and_order_(base, N, p2e4N)
        if verbose:print('2:', N, ccltmc)
        if not None is (p2e:=try_factor_pint_(ccltmc)):
            if verbose:print('3:', N)
            ps = tuple(sorted(p2e))
            db[base:N:p2e4N] = ps
                #__setitem__

def _iter_try_resting_(*, time4sleep6ok=0, try_resting_=None):
    #可能是调用子进程的缘故，try_resting_()的计时器只计算本线程耗时，导致无用
    #   => ++kw:may_time_kind
    check_int_ge(0, time4sleep6ok)
    if try_resting_ is None:
        def try_resting_():pass
    check_callable(try_resting_)
    j = 0
    while 1:
        j += 1
        yield j
        try_resting_()
        sleep(time4sleep6ok)
def _iter_fill7fixed_base_(may_db, base, min4N, max4N, /, *, verbose=False, stop6fail=False, time4sleep6ok=0, try_resting_=None, 休眠期=0.0, 苏醒期=2.0, time_kind='system_wide', **kwds6default_db):
    #可能是调用子进程的缘故，try_resting_()的计时器只计算本线程耗时，导致无用
    #   => ++kw:may_time_kind
    check_int_ge(0, time4sleep6ok)
    if try_resting_ is None:
        def try_resting_():pass
    check_callable(try_resting_)
    _rest = mk_rest_func_(休眠期, 苏醒期, time_kind=time_kind)

    check_int_ge(2, base)
    check_int_ge(1, min4N)
    check_int_ge(min4N, max4N)

    db = db5may_db_(may_db, **kwds6default_db)


    try_resting_()
    777;_rest()

    u2p2e = tabulate_may_prime_factorization4uint_lt_(1+max4N)
    it = enumerate(u2p2e)
    #777;next(it)
    777;it = islice(it, min4N, None)

    for N, p2e4N in it:
        if verbose:print('0:', N)
        if (base, N) in db:continue
        try_resting_()
        777;_rest()
        if verbose:print('1:', N)
        ok = True
        try:
            db[base:N:p2e4N]
            #__getitem__:calling:factor_pint_func
        except TimeoutError:
            ok = False
        if not ok:
            if verbose:print('-2:', N, 'timeout')
            assert not (base, N) in db
            yield ('fail:', base, N)
            if stop6fail:
                if verbose:print('stop6fail:', N)
                break
        else:
            if verbose:print('+2:', N, 'ok')
            assert (base, N) in db
            record = (base, N, db[base:N:p2e4N])
            yield record
            sleep(time4sleep6ok)

def _fill7fixed_base_(*args, **kwds):
    it = _iter_fill7fixed_base_(*args, **kwds)
    for _ in it:pass


def validate_cyclotomic_numbers6base_and_order_(may_db, base, N, may_p2e4N_or_ps4N_or_factor_pint_func, /, **kwds6default_db):
    check_int_ge(2, base)
    check_int_ge(1, N)

    db = db5may_db_(may_db, **kwds6default_db)
    if may_p2e4N_or_ps4N_or_factor_pint_func is None:
        may_p2e4N_or_ps4N_or_factor_pint_func = db.factor_pint_func

    p2e4N = prepare_p2e4N_(N, may_p2e4N_or_ps4N_or_factor_pint_func)
    acc = 1
    for ft, p2e4ft in sorted_all_factors5factorization_(p2e4N, with_factorization=True):
        ccltmc = db.cyclotomic_number5base_and_order_(base, ft, p2e4ft)
        acc *= ccltmc
    assert acc == -1+base**N
    return


__all__
from seed.math.factor_pint.database4factors4cyclotomic_numbers import mk_database4factors4cyclotomic_numbers_
from seed.math.factor_pint.database4factors4cyclotomic_numbers import *
