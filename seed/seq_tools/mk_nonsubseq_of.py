#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/mk_nonsubseq_of.py

用途:
    view others/数学/编程/永恒代码/原貌字符串.txt
    原貌字串囗(原貌字串囗起止定位串,原貌字串囗内容串) := 原貌字串囗起始串囗(原貌字串囗起止定位串)++原貌字串囗内容串++原貌字串囗结束串囗(原貌字串囗起止定位串)

    原貌字串囗起始串囗(原貌字串囗起止定位串) := 原貌字串囗起始串囗固定前缀++原貌字串囗起止定位串++原貌字串囗起始串囗固定后缀

    原貌字串囗结束串囗(原貌字串囗起止定位串) := 原貌字串囗结束串囗固定前缀++原貌字串囗起止定位串++原貌字串囗结束串囗固定后缀

    要求:[len(原貌字串囗起止定位串) >= 1][原貌字串囗起止定位串 not in (原貌字串囗起止定位串[1:]++原貌字串囗起始串囗固定后缀++原貌字串囗内容串++原貌字串囗结束串囗固定前缀++原貌字串囗起止定位串[:-1])]

    简化要求:[len(原貌字串囗起止定位串) >= 1][原貌字串囗起止定位串::[原貌字串囗起止定位串囗许可字集]][原貌字串囗起止定位串 not in 原貌字串囗内容串][len(原貌字串囗起始串囗固定后缀)>=1][len(原貌字串囗结束串囗固定前缀)>=1][{*原貌字串囗起始串囗固定后缀,*原貌字串囗结束串囗固定前缀}/-\原貌字串囗起止定位串囗许可字集=={}]
        [原貌字串囗起止定位串::内容串囗非子串]
        [原貌字串囗起止定位串:=mk_nonsubseq_of(原貌字串囗内容串,...)]

seed.seq_tools.mk_nonsubseq_of
py -m nn_ns.app.debug_cmd   seed.seq_tools.mk_nonsubseq_of
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.seq_tools.mk_nonsubseq_of   @f
py -m nn_ns.app.doctest_cmd seed.seq_tools.mk_nonsubseq_of:__doc__ -v

from seed.seq_tools.mk_nonsubseq_of import check_antisubseq_, mk_a_nonsub_uint_seq_of_uint_seq_, mk_a_nonsubseq_of_
#def mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq, /)->antisubseq:
#def mk_a_nonsubseq_of_(key_seq, /, *, is_key_ok, extra_keys)->antisubseq:








>>> from seed.seq_tools.mk_nonsubseq_of import check_antisubseq_, mk_a_nonsub_uint_seq_of_uint_seq_, mk_a_nonsubseq_of_

#def mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq, /):
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [])
(0,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [0])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [1])
(0,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [0,0])
(0, 0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [0,1])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [1,0])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [1,1])
(0,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [1,1,1])
(0,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [0,1,1])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [1,0,1])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [1,1,0])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [0,0,1])
(0, 0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [0,1,0])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [1,0,0])
(0, 0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(1, [0,0,0])
(0, 0, 0, 0)




>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [])
(0,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [0])
(1,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [1])
(0,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [0,0])
(1,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [0,1])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [1,0])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [1,1])
(0,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [1,1,1])
(0,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [0,1,1])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [1,0,1])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [1,1,0])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [0,0,1])
(1, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [0,1,0])
(0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [1,0,0])
(0, 1)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [0,0,0])
(1,)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [0,0,0,1,0,1,1,1,0,0])
(0, 0, 0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [0,0,1,1,0])
(0, 0, 0)
>>> mk_a_nonsub_uint_seq_of_uint_seq_(2, [1,1,0,0,1])
(0, 0, 0)



#def mk_a_nonsubseq_of_(key_seq, /, *, is_key_ok, extra_keys):
>>> mk_a_nonsubseq_of_([], is_key_ok=1 .__gt__, extra_keys=[0,1])
(0,)
>>> mk_a_nonsubseq_of_([0], is_key_ok=1 .__gt__, extra_keys=[0,1])
(0, 0)
>>> mk_a_nonsubseq_of_([1], is_key_ok=1 .__gt__, extra_keys=[0,1])
(0,)
>>> mk_a_nonsubseq_of_([0,0], is_key_ok=1 .__gt__, extra_keys=[0,1])
(0, 0, 0)
>>> mk_a_nonsubseq_of_([0,1], is_key_ok=1 .__gt__, extra_keys=[0,1])
(0, 0)
>>> mk_a_nonsubseq_of_([1,0], is_key_ok=1 .__gt__, extra_keys=[0,1])
(0, 0)
>>> mk_a_nonsubseq_of_([1,1], is_key_ok=1 .__gt__, extra_keys=[0,1])
(0,)

>>> mk_a_nonsubseq_of_([0,0,1,1,0], is_key_ok=2 .__gt__, extra_keys=[0,1])
(0, 0, 0)

# [def__reorder__ok_keys]:goto
#   [not reorder] ==>> below line result would be (1, 1, 1)
>>> mk_a_nonsubseq_of_([1,1,0,0,1], is_key_ok=2 .__gt__, extra_keys=[0,1])
(0, 0, 0)
>>> mk_a_nonsubseq_of_([1,1,0,0,1], is_key_ok=2 .__gt__, extra_keys=[0,1], _reorder__ok_keys=False)
(1, 1, 1)

>>> mk_a_nonsubseq_of_([1,1,0,2,0,1], is_key_ok=2 .__gt__, extra_keys=[0,1])
(0, 0)
>>> mk_a_nonsubseq_of_([1,1,0,999,0,1], is_key_ok=2 .__gt__, extra_keys=[0,1])
(0, 0)

#]]]'''
__all__ = r'''
check_antisubseq_
    mk_a_nonsub_uint_seq_of_uint_seq_
    mk_a_nonsubseq_of_

'''.split()#'''
__all__




from seed.types.StackStyleSet import StackStyleSet#, MultiSetStyleStack

#from nn_ns.RMQ.make_suffix_tree_data import make_suffix_tree_data_from_uint_array
    #view ../../python3_src/nn_ns/RMQ/make_suffix_tree_data.py
    #def make_suffix_tree_data_from_uint_array(array):

from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le, check_callable
from seed.tiny import check_type_is, fst, snd, at
from seed.types.RadixNumberCounter import RadixNumberCounter
    # def to_little_endian_digit_tuple(sf, /, *, reverse=False):
    # def inc() -> overflow
from seed.types.RadixNumberCounter import iter_words_in_one_period_, iter_words_in_one_period_with_idx_
    #def iter_words_in_one_period_with_idx_(radix, sz, /, *, big_endian):

from seed.iters.find import find_subseq
    #view ../../python3_src/seed/iters/find.py
    #def find_subseq(seq, subseq, begin=None, end=None, failure_map=None, _ver=None):


def check_antisubseq_(typ, may_total_ok_keys, whole_seq, antisubseq, /):
    check_type_is(typ, antisubseq)
    assert 1 <= len(antisubseq) <= len(whole_seq)+1
    if may_total_ok_keys is None:
        assert len(antisubseq) == 1
        [extra_ok_key] = antisubseq
        assert extra_ok_key not in whole_seq
    else:
        total_ok_keys = may_total_ok_keys
        assert total_ok_keys**(len(antisubseq)-1) + (len(antisubseq)-1)-1 <= len(whole_seq)
    assert -1 == find_subseq(whole_seq, antisubseq) #antisubseq not in whole_seq
    assert not -1 == find_subseq(whole_seq, antisubseq[:-1]) #antisubseq[:-1] in whole_seq
    assert not -1 == find_subseq(whole_seq, antisubseq[1:]) #antisubseq[1:] in whole_seq

def mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq, /):
    r'''O(NlogN): bad_uint -> [uint%(bad_uint+1)] -> antisubseq/[ok_uint] #[ok_uint::uint%bad_uint] #[antisubseq not in uint_seq]

    [N := len(uint_seq)]
        # size of input seq
    [A := bad_uint]
        # size of alphabet
        # best: [A >= 2]
        #   [A >= 2] ==>> [reduce output size: len(antisubseq) == O(log_(A;N))]

    [TIME(mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq))
    =O(NlogN)
    ]

    proof:[[
    * [{0..<bad_uint} \-\ {*uint_seq} =!= {}]:
        # exits ok_uint not in uint_seq
        [TIME(mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq))
        =O(len(uint_seq)+len(ok_uints))
        =O(N+A)
        ]
        [TIME(mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq))
        =O(len(uint_seq)+len(partial ok_uints))
        =O(N)+O(N+1)
        =O(N)
        ]
    * [{0..<bad_uint} \-\ {*uint_seq} === {}]:
        [len(ok_uint) <= len(uint_seq)]
        [A <= N]
        * [bad_uint == 1]:
            [TIME(mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq))
            =O(N+A)+O(len(uint_seq))
            =O(N+A)+O(N)
            =O(N+A)
            =O(N)
            ]
        * [bad_uint >= 2]:
            [TIME(mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq))
            =O(N+A)+O(len(uint_seq)*len(antisubseq))
            =O(N+A)+O(N*log_(A;N))
            =O(N+A)+O(N*logN)
            =O(NlogN)
            ]
    ]]

    '''#'''
    check_int_ge(1, bad_uint)
    M = bad_uint+1
    uint_seq[:0]
    for u in uint_seq: check_uint_lt(M, u)
    antisubseq = _mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq)

    total_ok_uints = bad_uint
    check_antisubseq_(tuple, total_ok_uints, uint_seq, antisubseq)
    return antisubseq

    assert 1 <= len(antisubseq) <= len(uint_seq)+1
    assert total_ok_uints**(len(antisubseq)-1) + (len(antisubseq)-1)-1 <= len(uint_seq)
    assert -1 == find_subseq(uint_seq, antisubseq) #antisubseq not in uint_seq
    assert not -1 == find_subseq(uint_seq, antisubseq[:-1]) #antisubseq[:-1] in uint_seq
    assert not -1 == find_subseq(uint_seq, antisubseq[1:]) #antisubseq[1:] in uint_seq
    return antisubseq

def _mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq, /):
    #us = StackStyleSet(uint_seq)
    #us = MultiSetStyleStack(uint_seq)
    us = set(uint_seq)
    ok_uints = range(bad_uint)
    if 1:
        #why?
        #   bad_uint may be very huge (e.g. total unicode chars 0x11_0000)
        #   but len(uint_seq) may be smaller
        #   if uint_seq contains all ok_uints then below 『ok2isuffixes = [[] for _ in range(total_ok_uints)]』is not slow
        for ok_uint in ok_uints:
            if ok_uint not in us:
                antisubseq = (ok_uint,)
                return antisubseq
    del us, ok_uint
    ok_uints
    assert 0 < bad_uint == len(ok_uints) <= len(uint_seq)
    ###################
    if len(ok_uints)==1:
        #!! [len(ok_uints)**(len(antisubseq)-1) + (len(antisubseq)-1)-1 <= len(uint_seq)]
        #==>> should handle [len(ok_uints)==1] case specially to speedup
        ok = 0
        bad = 1
        sp = b' '[0]
        w = b'w'[0]
        bs = bytes(w if bit==ok else sp for bit in uint_seq)
        wss = bs.split()
        assert wss # <<== ok in uint_seq #below max(...) not fire
        L = max(map(len, wss))
        antisubseq = (ok,)*(L+1)
        return antisubseq
    ###################
    assert 2 <= bad_uint == len(ok_uints) <= len(uint_seq)
    total_ok_uints = len(ok_uints)
    if 1:
        # when sz == 0
        sz = 0
            # sz == len(subseq)
        subseq = ()
            # [ok_uint]{len=sz}
        isuffixes = range(1+len(uint_seq))
        #subseq2isuffixes = {subseq:isuffixes}
        u2isuffixes = uint8subseq_2_occur_isuffixes4subseq = [isuffixes] #{0:isuffixes}
            # isuffix <<== uint_seq[isuffix:?]==subseq
            # u = uint5big_endian_radix_digits(bad_uint, subseq)
    for sz in range(2+len(uint_seq)):
        assert len(u2isuffixes) == total_ok_uints**sz
        next__u2isuffixes = []
        for u, digitsLE in iter_words_in_one_period_with_idx_(total_ok_uints, sz, big_endian=True):
            #ok2exist = bytearray(total_ok_uints)
            #xok2exist = bytearray(1+total_ok_uints)
            ok2isuffixes = [[] for _ in range(total_ok_uints)]
                # 『1+』to allow『xok2exist[bad_uint]』
            subseq = digitsLE
            for isuffix in u2isuffixes[u]:
                j = isuffix+sz
                if not j < len(uint_seq): continue
                _post = uint_seq[j]
                if _post == bad_uint: continue
                ok = _post
                ok2isuffixes[ok].append(isuffix)
            if not all(ok2isuffixes):
                missed_ok = ok2isuffixes.index([])
                antisubseq = (*subseq, missed_ok)
                return antisubseq
            next__u2isuffixes += ok2isuffixes
        u2isuffixes = next__u2isuffixes
    raise logic-err
#end-def mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq, /):

def mk_a_nonsubseq_of_(key_seq, /, *, is_key_ok, extra_keys, _reorder__ok_keys=True):
    r'''(if [all is_key_ok extra_keys][unique extra_keys] then O(NlogN) else O(E+NlogN)): Hashable k => [k] -> (is_key_ok::k->bool) -> (extra_keys::Iter k) -> antisubseq/[k] #[all is_key_ok antisubseq][antisubseq not in key_seq]

    [[unique s] =[def]= [len({*s})==len(s)]]

    [N := len(uint_seq)]
        # size of input seq
    [E := len(extra_keys)]
        # size of extra alphabet
        # best: [extra_keys has determine order][E >= 2][all is_key_ok extra_keys][unique extra_keys]
        #   [extra_keys has determine order] ==>> [output has determine order]
        #   [E >= 2][all is_key_ok extra_keys][unique extra_keys] ==>> [reduce output size: len(antisubseq) == O(log_(E;N))]


    [TIME(mk_a_nonsubseq_of_(key_seq, is_key_ok=, extra_keys=))
    =(if [all is_key_ok extra_keys][unique extra_keys] then O(NlogN) else O(E+NlogN))
    ]

    proof:[[
    * [{k | [[k:<-extra_keys][is_key_ok k]]} \-\ {*key_seq} =!= {}]:
        # exits ok_key not in key_seq
        [TIME(mk_a_nonsubseq_of_(key_seq, is_key_ok=, extra_keys=))
        =O(len(key_seq)+len(extra_keys))
        =O(N+E)
        ]
        [all is_key_ok extra_keys][unique extra_keys]:
            [TIME(mk_a_nonsubseq_of_(key_seq, is_key_ok=, extra_keys=))
            =O(len(key_seq)+len(partial extra_keys))
            =O(N)+O(N+1)
            =O(N)
            ]
    * [{k | [[k:<-extra_keys][is_key_ok k]]} \-\ {*key_seq} === {}]:
        [{*filter(is_key_ok, extra_keys)} |<=| {*key_seq}]
        [len({*filter(is_key_ok, extra_keys)}) <= len(key_seq)]
        [A == len({*filter(is_key_ok, key_seq)}) <= N]
        [A == bad_uint == total_ok_uints <= len(uint_seq) == len(key_seq) == N]
        [TIME(mk_a_nonsubseq_of_(key_seq, is_key_ok=, extra_keys=))
        =O(N+E) + TIME(mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq))
        =O(N+E) + O(A+NlogN)
        =O(E+NlogN)
        ]

        [all is_key_ok extra_keys][unique extra_keys]:
            [len(extra_keys) <= len(key_seq)]
            [E <= N]
            [TIME(mk_a_nonsubseq_of_(key_seq, is_key_ok=, extra_keys=))
            =O(E+NlogN)
            =O(NlogN)
            ]
    ]]

    '''#'''
    key_seq[:0]
    extra_keys = iter(extra_keys)
    check_callable(is_key_ok)
    (antisubseq, may_total_ok_keys) = _mk_a_nonsubseq_of_ex_(_reorder__ok_keys, is_key_ok, extra_keys, key_seq)

    check_antisubseq_(tuple, may_total_ok_keys, key_seq, antisubseq)
    return antisubseq
def _mk_a_nonsubseq_of_ex_(_reorder__ok_keys, is_key_ok, extra_keys, key_seq, /):
    '-> (antisubseq, may_total_ok_keys)'
    s = StackStyleSet(filter(is_key_ok, key_seq))
    s_ = StackStyleSet()
    L = len(s)
    for k in filter(is_key_ok, extra_keys):
        s_.add(k)
        s.add(k)
        if not L == len(s):
            #assert k not in key_seq
            antisubseq = (k,)
            may_total_ok_keys = None
            return antisubseq, may_total_ok_keys
    del extra_keys
    if _reorder__ok_keys:
        #[def__reorder__ok_keys]
        #reorder ok_keys: such that ok_keys<extra_keys> before ok_keys<key_seq-extra_keys>
        s_.update(s); del s
        ok_keys = s_; del s_
    else:
        ok_keys = s; del s, s_
    ok_keys
    assert len(ok_keys) == L

    #ok_keys.key2idx
    #ok_keys.idx2key
    #ok2key = [*ok_keys]
        # ok_uint -> k
    bad_uint = total_ok_uints = total_ok_keys = L
    uint_seq = [ok_keys.key2idx(k) if k in ok_keys else bad_uint for k in key_seq]

    uint_antisubseq = mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq)
    antisubseq = tuple(ok_keys[i] for i in uint_antisubseq)

    may_total_ok_keys = total_ok_keys
    return antisubseq, may_total_ok_keys
    return antisubseq
#end-def mk_a_nonsubseq_of_(key_seq, /, *, is_key_ok, extra_keys):


r'''
'''#'''

from seed.seq_tools.mk_nonsubseq_of import check_antisubseq_, mk_a_nonsub_uint_seq_of_uint_seq_, mk_a_nonsubseq_of_
#def mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq, /)->antisubseq:
#def mk_a_nonsubseq_of_(key_seq, /, *, is_key_ok, extra_keys)->antisubseq:
