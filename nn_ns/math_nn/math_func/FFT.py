

'''
现代数学手册(3)·计算机数学卷::第十九篇　并行与分布计算中的模型与算法
[page 839]


[radix-2 1D FFT]
    len(X) = n = 2^m
    w[n]^n = 1
    Y = FFT(X, n, w[n]) # 
    Y[j] ::= sum X[i]w[n]^(i*j) {i=0..n-1} for j = 0..n-1
    1/n * FFT(Y, n, w[n]^-1)[k]
    = 1/n sum Y[j]w[n]^(-j*k) {j=0..n-1}
    = 1/n sum sum X[i]w[n]^(i*j) {i=0..n-1} w[n]^(-j*k) {j=0..n-1}
    = 1/n sum sum X[i](w[n]^(i-k))^j {j=0..n-1} {i=0..n-1}
    = 1/n sum [mod n: i=k]*sum X[i](w[n]^(i-k))^j {j=0..n-1} + [mod n: i/=k]*sum X[i](w[n]^(i-k))^j {j=0..n-1} {i=0..n-1}
    = 1/n sum [mod n: i=k]*X[i]*n + [mod n: i/=k]*0 {i=0..n-1}
    = X[k]
    X = IFFT(Y, n, w[n]) = 1/n * FFT(Y, n, w[n]^-1)

    [recursive]
    Y[j]
    = sum X[i]w[n]^(i*j) {i=0..n-1}
    = sum X[i]w[n]^(i*j) {i=0,2..n-2} + sum X[i]w[n]^(i*j) {i=1,3..n-1}
    = sum X[2*i]w[n]^(2*i*j) {i=0..n/2-1} + sum X[2*i+1]w[n]^(2*i*j+j) {i=0..n/2-1}
    = sum X[2*i]w[n/2](i*j) {i=0..n/2-1} + w[n]^j * sum X[2*i+1]w[n/2]^(i*j) {i=0..n/2-1}
    = FFT(X[::2], n/2, w[n/2])[j mod n/2] + w[n]^j * FFT(X[1::2], n/2, w[n/2])[j mod n/2]

    = inplace_FFT(X)[(j mod n/2)*2] + w[n]^j * inplace_FFT(X)[1+(j mod n/2)*2]


time: starts, step, len; num_seq =
    0 : [0], 1, n; 1
    1 : [0, 1], 2, n/2; 2
    k :   [..., start, ...], step, len; num_seq
    k+1 : [..., start, start+step, ...], 2*step, len//2; num_seq*2
    ==>> step == num_seq = 2**time; len*step == n; len = n//2**time
    ==>> starts == [0..step-1]
    len == 1 ==>> time = log2 n = n.bit_length()-1 = m
    m :   [0..n-1], n, 1; n
    m-1 : [0..n/2-1], n/2, 2; n/2

    Y[time][seq_idx] ~ start=seq_idx < 2**time = step, len = n//2**time
        ~ Y[seq_idx : : 2**time]
    ~ Y[time+1][seq_idx] and Y[time+1][seq_idx+2**time]
    Y[time][seq_idx][j] ~ Y(time)[seq_idx + j*2**time]
    Y[time][seq_idx][j] = Y[time+1][seq_idx][j mod n//2**(time+1)] + w[n//2**time]^j * Y[time+1][seq_idx+2**time][j mod n//2**(time+1)]
    Y(time)[seq_idx + j*2**time] = Y(time+1)[seq_idx + (j*2**(time+1) mod n)] + w[n]^(j*2**time) * Y(time+1)[seq_idx+2**time + (j*2**(time+1) mod n)]
    let i = seq_idx + j*2**time;
    let i' = seq_idx + (j*2**(time+1) mod n);
    let i'' = seq_idx+2**time + (j*2**(time+1) mod n); e = j*2**time
    ==>> seq_idx = i%2**time, j = i//2**time
    let i = (b[m-1], ..., b[0])_2 = sum b[k]*2**k {k=0..m-1}
    ==>> i' = (b[m-2], ..., b[t], 0, b[t-1], ..., b[0])_2
    ==>> i'' = (b[m-2], ..., b[t], 1, b[t-1], ..., b[0])_2
    ==>> e = (b[m-1], ..., b[t], 0, ..., 0)_2
    Y(time)[i] = Y(time+1)[i'] + w[n]^e * Y(time+1)[i'']
'''

def IFFT(Y, ws, step, FFT):
    n = len(Y)
    # inv_w = ws[-step]
    nX = FFT(Y, ws, (-step) % len(ws))
    for i in range(n):
        nX[i] /= n
    X = nX ; del nX
    return X
def recursive_radix2_1dimensional_FFT(X, ws, step):
    '''\
n = len(X) <= len(ws);
0 <= step < len(ws)
n*step%len(ws) == 0
w[n] = ws[step];
w[n]^j = ws[j*step%len(ws)];
w[n]^n = ws[0] = 1
'''
    if len(X) < 2:
        Y = list(X)
        return Y
    
    FFT = recursive_radix2_1dimensional_FFT
    n = len(X)
    assert len(ws) >= len(X)
    assert 0 < step < len(ws)
    assert step * n % len(ws) == 0
    #assert w**n == 1
    #assert n == 2**(n.bit_length() - 1)
    assert n % 2 == 0

    # w2 = w*w
    step2 = 2*step % len(ws)
    even_FFT = FFT(X[::2], ws, step2)
    odd_FFT = FFT(X[1::2], ws, step2)

    Y = [None]*n
    j = -1
    step_j = -step # j*step
    half_n = n // 2
    #step_half_n = half_n * step
    
    for even_fft, odd_fft in zip(even_FFT, odd_FFT):
        j += 1
        step_j += step
        step_j %= len(ws)
        #step_j_ = step_j + step_half_n
        #step_j_ %= len(ws)
        Y[j] = even_fft + ws[step_j] * odd_fft
        #Y[j+half_n] = even_fft + ws[step_j_] * odd_fft
        Y[j+half_n] = even_fft - ws[step_j] * odd_fft

    return Y

def reversed_binary_nonnegative_integer(n, *, _v = True):
    'n = (1, a, b, c, ..., d)_2 ==>> r = (d, ..., c, b, a, 1)'
    assert n >= 0
    r = 0
    while n:
        r <<= 1
        if n & 1:
            r |= 1
        n >>= 1

    if _v:
        f = reversed_binary_nonnegative_integer
        assert r == f(f(r, _v = False), _v=False)
    return r

def iterative_radix2_1dimensional_FFT(X, ws, step):
    'Cooley-Tukey'

    n = len(X)
    m = n.bit_length() - 1
    assert 2**m == n
    assert len(X) <= len(ws)
    assert n * step % len(ws) == 0
    assert 0 <= step < len(ws)

    new = list(X)
    old = new.copy()

    #i2r = [reversed_binary_nonnegative_integer(i) for i in range(n)]
    
    exp2_t = 2**m
    for t in range(m-1, -1, -1):
        exp2_t >>= 1
        assert exp2_t == 2**t
        old, new = new, old

        for i in range(n):
            # i = (b[m-1], ..., b[0])_2
            #   = b[m-1] * 2**(m-1) + ... + b[0] * 2**0
            # j = (b[m-2], ..., b[t], 0, b[t-1], ..., b[0])_2
            # k = (b[m-2], ..., b[t], 1, b[t-1], ..., b[0])_2
            # e = (b[m-1], ..., b[t], 0, ..., 0)_2 of len m
            even_start = i % exp2_t
            e = i - even_start
            j = (i * 2) % n - even_start
            
            k = j | exp2_t
            new[i] = old[j] + old[k] * ws[e*step % len(ws)]

    Y = new
    #Y_ = recursive_radix2_1dimensional_FFT(X, ws, step)
    #print(X, Y, Y_, sep='\n')
    return Y












def vector_conjugate(v):
    return [x.conjugate() for x in v]

def vector_complex_square(v):
    return cross_product(v, vector_conjugate(v))

def cross_product(u, v):
    return sum(a*b for a, b in zip(u, v))
def vector_sub(u, v):
    return [a-b for a, b in zip(u, v)]


def test_complex_FFT(FFT):
    import random # random.random()
    import cmath, math
    from cmath import pi
    max_m = 14
    max_n = 2**max_m
    w = cmath.rect(1.0, 2*pi/max_n)
    ws = [cmath.rect(1.0, 2*i*pi/max_n) for i in range(max_n)]
##    a = max_n*pi/max_n
##    print(a)
##    print(cmath.rect(1.0, a))
##    print(math.cos(a), math.sin(a))
    for m in range(max_m+1):
        n = 2**m
        X = [random.random() for _ in range(n)]
        step = max_n//n % max_n
        Y = FFT(X, ws, step)
        X_ = IFFT(Y, ws, step, FFT)

        delta_X = vector_sub(X_, X)
        err = vector_complex_square(delta_X)
        try:
            assert err.imag == 0j
            assert 0.0 <= err.real <= 1e-20
        finally:
            print(err)


test_complex_FFT(iterative_radix2_1dimensional_FFT)
test_complex_FFT(recursive_radix2_1dimensional_FFT)
















