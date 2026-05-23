
e ../../python3_src/seed/math/prime_sieve/README.txt
[[
main_exports:

PrimeList

iter_primes_
iter_sieve4primes_ge_lt_
iter_sieve4prime_factorizations_ge_lt_

list_primes__len_ge_
list_primes__lt_
tabulate_may_prime_factorization4uint_lt_

]]



[[
view ../../python3_src/seed/math/prime_sieve/PrimeList.py
===
#筛多次:使用:iter_sieve4primes_ge_lt_
#数组式用法:缓存结果，但不同于此前prime_gen，不再保存全局对象，若要需要则传递局部变量
PrimeList
===
]]
[[
view ../../python3_src/seed/math/prime_sieve/sieve_ge_le.py
===
main_exports:
#筛多次:点输迭代出模式
    iter_primes_

    #kw:reverse,with_interval
    iter_sieve4primes_ge_lt_
        iter_sieve4prime_chunks_ge_lt_
    iter_sieve4prime_factorss_ge_lt_
        iter_sieve4prime_factors_chunks_ge_lt_
    iter_sieve4prime_factorizations_ge_lt_
        iter_sieve4prime_factorization_chunks_ge_lt_







===
secondary_exports:
#筛多次:块迭代输出模式,点输迭代出模式
iter_sieve4prime_chunks_ge_lt_
    iter_sieve4prime_chunks_ge_
    reverse_iter_sieve4prime_chunks_lt_
    iter_sieve4primes_ge_lt_
        iter_sieve4primes_ge_
            iter_primes_===iter_primes__new_ver_
        reverse_iter_sieve4primes_lt_

iter_sieve4prime_factors_chunks_ge_lt_
    iter_sieve4prime_factors_chunks_ge_
    reverse_iter_sieve4prime_factors_chunks_lt_
    iter_sieve4prime_factorss_ge_lt_
        iter_sieve4prime_factorss_ge_
        reverse_iter_sieve4prime_factorss_lt_

iter_sieve4prime_factorization_chunks_ge_lt_
    iter_sieve4prime_factorization_chunks_ge_
    reverse_iter_sieve4prime_factorization_chunks_lt_
    iter_sieve4prime_factorizations_ge_lt_
        iter_sieve4prime_factorizations_ge_
        reverse_iter_sieve4prime_factorizations_lt_



===
#只筛一次:单块输出模式:要么从零开始，要么筛间隔
sieve_interval4primes__ge_lt
sieve_interval4offsetted_uint2is_prime__ge_lt
sieve_interval4prime_factorization__ge_lt
sieve_interval4prime_factors__ge_lt


===
#只筛一次:单块输出模式:筛间隔:内部核心算法
core_sieve4primes__ge_le
core_sieve4offsetted_uint2is_prime__ge_le
core_sieve4prime_factorization__ge_le
core_sieve4pairs8prime_factorization__ge_le
core_sieve4prime_factors__ge_le
===
]]
[[
view ../../python3_src/seed/math/prime_sieve/sieve_lt.py
===
main_exports:
list_primes__len_ge_
list_primes__lt_

tabulate_may_min_prime_factor4uint_lt_
tabulate_may_all_prime_factor_lflnkls4uint_lt_
    tabulate_may_all_prime_factors4uint_lt_
tabulate_may_prime_factorization4uint_lt_


===
分类注释:
===
#新版重置:不再依赖旧版迭代式筛法
#只筛一次:单块输出模式:根据最小长度估计最大素数上界
list_primes__len_ge_

#只筛一次:单块输出模式:根据最大素数上界
list_primes__lt_===list_all_strict_sorted_primes__lt_
    sieve4uint2is_prime__lt_

tabulate_may_min_prime_factor4uint_lt_
tabulate_may_all_prime_factors4uint_lt_
    tabulate_may_all_prime_factor_lflnkls4uint_lt_
    extract_prime_factorization5uint2may_all_prime_factor_lflnkls_


tabulate_may_pairs8prime_factorization4uint_lt_
    tabulate_may_prime_factorization4uint_lt_
                                            旧版接口:tabulate_may_factorization4uint_lt_


===
#旧版遗存:参数控制输出类型
#筛多次:点输迭代出模式:从零开始,内部保存平方根数量的小素数用于筛选
iter_primes__old_ver_===iter_all_strict_sorted_primes_
    ?iter_primes__old_ver_-->改用:见上面:iter_primes_
  def iter_all_strict_sorted_primes_(*, size=None, end=None, may_primes=None):
raw_list_all_strict_sorted_primes__lt_
    raw_iter_all_strict_sorted_primes__lt_
        raw_iter_all_strict_sorted_primes_
            raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_
                raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_











===
]]








