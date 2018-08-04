
'''
source: exclude given string / [CMath]8.4 FLIPPING COINS

true_period str = min {d | [d\len(str)][str[d:]=str[:len(str)-d]]}
fake_period str = 0 if [len(str)=0] else min {d>0 | [str[d:]=str[:len(str)-d]]}

num_notproper_trueperiod_types L = 1[when T=L] + sum [! T\L](num_period_types (L mod T)) {T=1..L} for [L>0]
num_period_types L = sum [T\L](num_notproper_trueperiod_types T) {T=1..L} for [L>0]
num_notproper_trueperiod_types 0 = 1
num_period_types 0 = 1

'''


from itertools import accumulate, count


def check_period_type(period_type):
    try:
        assert all(T > 0 and times > 0 for T, times in period_type)
        assert all(T1 > T2 for (T1,_), (T2,_) in zip(period_type, period_type[1:]))
        ls = [T*times for T, times in period_type]
        ls = list(accumulate(reversed(ls)))
        ls.reverse()
        assert all(T > after or
                   (T==after and period_type[idx+1][0] > ls[idx+2])
                   for idx, (T,_), after in zip(count(), period_type, ls[1:]))
    except AssertionError:
        print(period_type)
        raise
    
    return True

    

def num_notproper_trueperiod_types(L):
    assert L >= 0
    if L == 0:
        return 1

    return 1 + sum(num_period_types(L%T) for T in range(1,L+1) if L%T)
def num_period_types(L):
    assert L >= 0
    if L == 0:
        return 1
    return sum(num_notproper_trueperiod_types(T) for T in range(1,L+1) if not L%T)

num_notproper_trueperiod_types_ls = [1]
num_period_types_ls = [1]

def fill_num_ls_to(L):
    assert len(num_period_types_ls) == len(num_notproper_trueperiod_types_ls) > 0
    for L in range(len(num_period_types_ls), L):
        num_NP_TP_n = 1 + sum(num_period_types_ls[L%T]
                              for T in range(1,L+1) if L%T)
        num_notproper_trueperiod_types_ls.append(num_NP_TP_n)
        
        num_TP_n = sum(num_notproper_trueperiod_types_ls[T]
                       for T in range(1,L+1) if not L%T)
        num_period_types_ls.append(num_TP_n)


def num_period_types(L):
    assert L >= 0
    return get_num_period_types_ls_least(L+1)[L]


def num_notproper_trueperiod_types(L):
    assert L >= 0
    return get_num_notproper_trueperiod_types_ls_least(L+1)[L]


def get_num_period_types_ls_least(L):
    fill_num_ls_to(L)
    return num_period_types_ls

def get_num_notproper_trueperiod_types_ls_least(L):
    fill_num_ls_to(L)
    return num_notproper_trueperiod_types_ls


# num_ls[L] == len(ls[L]) == len(set(ls[L]))
# all(T1>T2 for typ in ls[L] for (T1,_), (T2,_) in zip(typ, typ[1:]))
# all(L == sum(T*times for T, times in typ) for typ in ls[L])
# 
notproper_trueperiod_types_ls = [[()]] 
period_types_ls = [[()]] 

def fill_types_ls_to(L):
    assert len(period_types_ls) == len(notproper_trueperiod_types_ls) > 0
    n = len(period_types_ls)
    
    for L in range(len(period_types_ls), L):
        ls = []
        for T in range(1,L+1):
            if L%T:
                curr_type = ((T, L//T),)
                for period_type in period_types_ls[L%T]:
                    ls.append(curr_type + period_type)
        if T == L:
            curr_type = ((T, L//T),)
            ls.append(curr_type)
        notproper_trueperiod_types_ls.append(ls)
        #assert len(ls) == len(set(ls))

        ls = []
        for T in range(1,L):
            if not L%T:
                curr_type = ((T, (L-1)//T),)
                for typ in notproper_trueperiod_types_ls[T]:
                    ls.append(curr_type + typ)
                assert ls[-1] == (curr_type[0], (T, 1))
                ls[-1] = ((T, L//T),)

        T = L
        ls.extend(notproper_trueperiod_types_ls[T])
        period_types_ls.append(ls)
##        if not len(ls) == len(set(ls)):
##            print(ls)
##            print(notproper_trueperiod_types_ls[-1])
##            assert len(ls) == len(set(ls))
    return


def get_period_types(L):
    assert L >= 0
    return get_period_types_ls_least(L+1)[L]


def get_notproper_trueperiod_types(L):
    assert L >= 0
    return get_notproper_trueperiod_types_ls_least(L+1)[L]


def get_period_types_ls_least(L):
    fill_types_ls_to(L)
    return period_types_ls

def get_notproper_trueperiod_types_ls_least(L):
    fill_types_ls_to(L)
    return notproper_trueperiod_types_ls


assert all(all(check_period_type(typ) for typ in types)
           for n in [10] for L, num, types in
           zip(range(n),
               get_num_period_types_ls_least(n),
               get_period_types_ls_least(n)))

assert all(len(types) == num == len(set(types))
           for n in [10] for L, num, types in
           zip(range(n),
               get_num_period_types_ls_least(n),
               get_period_types_ls_least(n)))


#print(get_period_types_ls_least(10))

assert all(all(T1 > T2 for typ in types
               for (T1,_), (T2,_) in zip(typ, typ[1:]))
           for n in [10] for L, num, types in
           zip(range(n),
               get_num_period_types_ls_least(n),
               get_period_types_ls_least(n)))


assert all(all(L == sum(T*times for T, times in typ) for typ in types)
           for n in [10] for L, num, types in
           zip(range(n),
               get_num_period_types_ls_least(n),
               get_period_types_ls_least(n)))

assert all(all((T > 0 and times > 0)
           for typ in types
           for T, times in typ)

           for n in [10] for L, num, types in
           zip(range(n),
               get_num_period_types_ls_least(n),
               get_period_types_ls_least(n)))




def num_strs_of_period_type(alphabet_size, period_type):pass
def str2period_type(s):
    typ = []
    L = len(s)
    while L:
        for T in range(1, L+1):
            if s[T:] == s[:L-T]:
                break
        else:
            raise logic-error

        times, L = divmod(L, T)
        typ.append((T, times))
        s = s[:L]

    typ = tuple(typ)
    return typ


def period_type2std_str(period_type):
    s = ''
    it = iter(reversed(period_type))
    for T, times in it:
        assert T > 0
        assert times > 0
        period_s = '1' + '0'*(T-1)
        s = period_s * times
        break
    
    for T, times in it:
        assert T > 0
        assert times > 0
        
        L = len(s)
        if T == L:
            s *= (times+1)
        else:
            assert T > L
            head = s
            tail = '0'*(T-L)
            period_s = head + tail
            s = period_s*times + s

    assert s == '' or s[0] == '1'
    return s


def period_type2std_num(period_type):
    s = period_type2std_str(period_type)
    n = int(s, 2) if s else 0

    assert n.bit_length() == len(s)
    return n

std_nums_ls = []
def get_std_nums_ls_least(L):
    assert L >= 0
    period_types_ls = get_period_types_ls_least(L)
    for L in range(len(std_nums_ls), L):
        types = period_types_ls[L]
        nums = [period_type2std_num(typ) for typ in types]
        std_nums_ls.append(nums)

        if not len(set(nums)) == len(nums):
            print(nums)
            print(types)
            assert len(set(nums)) == len(nums)

    return std_nums_ls
    
assert all(len(set(nums)) == len(nums) for nums in get_std_nums_ls_least(10))

print(get_num_period_types_ls_least(10))
print(get_period_types_ls_least(10))




















