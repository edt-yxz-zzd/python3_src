'''
// should I PyBuffer_Release() "y*" buffer?
yes from:
    when a Py_buffer structure gets filled, the underlying buffer is locked so that the caller can subsequently use the buffer even inside a Py_BEGIN_ALLOW_THREADS block without the risk of mutable data being resized or destroyed. As a result, you have to call PyBuffer_Release() after you have finished processing the data (or in any early abort case).
no from:
    "w* ... The caller have to call PyBuffer_Release() when it is done with the buffer. "
    BUT "y* ... This is the recommended way to accept binary data. " doesnot require to release like above!
YES! I try, not release y* will fail. success on release.


'''


import _try_buffer as t
import array
from sys import getrefcount

f = t._try_buffer
arr = array.array


N = 2**20*4
SUM = 0
org = arr('i', range(N))
for ith in range(700):
    print('loop ', ith)
    print('INT[SUM/2**20]', SUM/2**20)
    SUM += N

    w = arr('i', org)
    r = arr('i', org)
    w[0] = 1
    assert r[0] == 0
    
    wc0 = getrefcount(w)
    rc0 = getrefcount(r)
    # one for local var; another for getrefcount TupleArgs
    assert wc0 == rc0 == 2 
    
    wc1, rc1 = f(getrefcount, w, r)
    # 4 from: local var;     _try_buffer TupleArgs;
    #         Py_buffer.obj; getrefcount TupleArgs
    if not wc1 == rc1 == 4:
        print('not wc1 == rc1 == 4 :', wc1, rc1)
    assert wc1 == rc1 == 4 
    d = 2
    assert wc0 == wc1 - d
    assert rc0 == rc1 - d
    assert wc0 == getrefcount(w)
    assert rc0 == getrefcount(r)
    

    list(w[:4000])
    list(r[:5999])
    
    

