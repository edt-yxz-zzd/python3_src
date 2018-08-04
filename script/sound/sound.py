import wave # little-endian
import audioop
import aifc # big-endian 要手动翻转　应该是bug # 压缩好像是有损压缩　#　压缩时当作little-endian压缩,　无法正常压缩保存!



class file_open:
    def __init__(self, fopen, *args, **kwargs):
        self.file = fopen(*args, **kwargs)
        return
    def __enter__(self):
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False
    
class wave_open(file_open):
    def __init__(self, *args, **kwargs):
        super().__init__(wave.open, *args, **kwargs)
        return
    
class aifc_open(file_open):
    def __init__(self, *args, **kwargs):
        super().__init__(aifc.open, *args, **kwargs)
        return

def toInt(sample, nchannels, sampwidth, idx_frame, idx_channel):
    idx = idx_frame * nchannels * sampwidth + idx_channel * sampwidth
    bs = sample[idx : idx+sampwidth]
    i = int.from_bytes(bs, byteorder='little', signed=True)
    return i
def toInts(sample, sampwidth, *, byteorder='little'):
    ls = []
    for idx in range(0, len(sample), sampwidth):
        bs = sample[idx : idx+sampwidth]
        i = int.from_bytes(bs, byteorder=byteorder, signed=True)
        ls.append(i)
    return ls
def toIntsList(sample, nchannels, sampwidth, *, byteorder='little'):
    ints = toInts(sample, sampwidth, byteorder=byteorder)
    ints_ls = []
    for i in range(nchannels):
        ls = [ints[c+i] for c in range(0, len(ints), nchannels)]
        ints_ls.append(ls)
    return ints_ls

def reverse_each_sample(sample, width):
    if width == 1:
        return sample

    ls = []
    for i in range(0, len(sample), width):
        s = sample[i:i+width]
        ls.append(bytes(reversed(s)))
    r = b''.join(ls)
    return r
    
def mul_stereo(sample, width, lfactor, rfactor):
    lsample = audioop.tomono(sample, width, 1, 0)
    rsample = audioop.tomono(sample, width, 0, 1)
    lsample = audioop.mul(lsample, width, lfactor)
    rsample = audioop.mul(rsample, width, rfactor)
    lsample = audioop.tostereo(lsample, width, 1, 0)
    rsample = audioop.tostereo(rsample, width, 0, 1)
    return audioop.add(lsample, rsample, width)

def read_wave(fname):
    with wave_open(fname, 'rb') as fin:
        #(nchannels, sampwidth, framerate, nframes, comptype, compname)
        params = fin.getparams()
        (nchannels, sampwidth, framerate, nframes, comptype, compname) = params
        
        read = lambda pos, n=1: (fin.setpos(pos), fin.readframes(n))[-1]
        sample = read(0, nframes)

    return params, sample

def write_wave(fname, params, sample):
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = params
    with wave_open(fname, 'wb') as fout:
        #(nchannels, sampwidth, framerate, nframes, comptype, compname)
        fout.setparams(params)
        
        fout.writeframes(sample)
    return

def write_aifc(fname, params, sample):
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = params
    rsample = reverse_each_sample(sample, sampwidth)
    with aifc_open(fname, 'wb') as fout:
        fout.setparams(params)
        
        fout.writeframes(rsample)

    rps, rspl = read_aifc(fname)
    if rps != params:
        print(rps, params)
        raise
    if rspl != sample:
        assert len(rspl) == len(sample)
        for i, a, b in zip(range(len(rspl)), rspl, sample):
            if a != b:
                print(i, a, b)
                break

        L = (i+100) * sampwidth * nchannels
        print(L)
        assert L < len(rspl)
        show_sample(sample[:L], nchannels, sampwidth)
        show_sample(rspl[:L], nchannels, sampwidth)
    # fail: assert (params, sample) == read_aifc(fname)
    return

def print_info_aifc(fname):
    with aifc_open(fname, 'rb') as fin:
        params = fin.getparams()
        print('(nchannels, sampwidth, framerate, nframes, comptype, compname)'\
              ' =', params)
    return

def read_aifc(fname):
    with aifc_open(fname, 'rb') as fin:
        params = fin.getparams()
        (nchannels, sampwidth, framerate, nframes, comptype, compname) = params
        sample = fin.readframes(nframes)
        rsample = reverse_each_sample(sample, sampwidth)
    return params, rsample

'''
window = F(10,4) # F-Distribution
scipy.special.fdtr(x1, x2, x3)
scipy.interpolate.interp1d(x, y)

钢琴 27.5~4.86KHz
>>> b=261.6255653
>>> from math import log2
>>> log2(b)
8.031359713521358
>>> l2b = log2(b)
>>> l2s = [l2b + i/12 for i in range(12*3)]
>>> ls = [2**e for e in l2s]
>>> ls
[261.62556529999983, 277.1826309762378, 293.66476791673534, 311.12698372136884, 329.62755691211566, 349.22823143220444, 369.9944227107876, 391.9954359808523, 415.3046975789945, 439.99999999899296, 466.1637615170232, 493.88330125499357, 523.2511305999997, 554.3652619524756, 587.3295358334707, 622.2539674427377, 659.2551138242313, 698.4564628644089, 739.9888454215752, 783.9908719617046, 830.609395157989, 879.9999999979859, 932.3275230340464, 987.7666025099871, 1046.5022611999993, 1108.7305239049513, 1174.6590716669414, 1244.5079348854754, 1318.5102276484627, 1396.9129257288178, 1479.9776908431504, 1567.981743923409, 1661.218790315978, 1759.9999999959718, 1864.6550460680928, 1975.5332050199743]
'''
def C1c1():
    A2 = log2(27.5)
    c5 = log2(4860)
    df = (c5-A2)/(88-1)

    C1 = A2 + 3*df
    C1 = 2**C1

    c1 = A2 + (3+36)*df
    c1 = 2**c1
    return C1, c1 #32.871984280242835 279.73360448558344

def int2frequency(n):
    b=261.6255653 # let b == c1
    l2b = log2(b)
    e = l2b + n/12
    f = 2**e
    return f

def int_rng2frequency(n, m):
    # int_rng2frequency(-3, 4) == [32.70319566249998, .., 4186.009044799997]
    b=261.6255653 # let b == c1
    l2b = log2(b)
    l2s = [l2b + i/12 for i in range(12*n, 12*m+1)]
    ls = [2**e for e in l2s]
    return ls
    
from math import log2, isnan, pi
import numpy as np
from scipy.special import fdtr
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
'''
x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)
'''

class Window:
    def __init__(self, L, x, y):
        self._init(L, x, y)
        return
    def length(self):
        return self.L
    def __call__(self, L, x, y=None):
        x = x * self.length()/L # not x *= ... !!!!!
        
        fx = self.f(x)
        if y == None:
            return fx
        return fx * y
    def _init(self, L, x, y):
        #x = np.arange(0, L, dx);
        self.L = L
        self.x = x
        self.y = y
        self.f = interp1d(x, y, copy=False)
        return


def calcFDistribution(v1, v2, x):
    y = fdtr(v1, v2, x)
    N = y.size
    z = np.zeros(N)
    z[1:] = y[:-1]
    y -= z
    return y

class WindowFDistribution(Window):
    def __init__(self, L, x, v1=10, v2=1):
        y = calcFDistribution(v1, v2, x)
        super().__init__(L, x, y)
        return
    
class WindowOne(Window):
    def __init__(self, L, x):
        y = np.ones(x.size)
        super().__init__(L, x, y)
        return
    
class WindowRightAngledTrapezium(Window):
    def __init__(self, L, x):
        y = np.ones(x.size)
        # (L, 0) (L/2, 1)
        for i, a in enumerate(x):
            if 2*a <= L:
                continue
            b = (L-a) * 2/L
            y[i] = b
        super().__init__(L, x, y)
        return
class WindowBlackman(Window):
    def __init__(self, L, x):
        N = x.size
        M = 2*N - 1
        y = np.blackman(M)[-N:]
        super().__init__(L, x, y)
        return

class WindowKaiser(Window):
    def __init__(self, L, x, beta=14):
        N = x.size
        M = 2*N - 1
        y = np.kaiser(M, beta)[-N:]
        super().__init__(L, x, y)
        return

    
class Frequency:
    def __init__(self, c1eq0, L=1):
        if isnan(c1eq0):
            self.freq = c1eq0
            self.f = lambda x:np.zeros(x.size)
            self.L = L
            return
        
        self.freq = int2frequency(c1eq0)
        self.w = 2 * pi * self.freq
        x = np.arange(0, L, 1/44100);
        y = []
        n = 3
        m = 1
        ws = [n/i for i in range(n, n+m)] #[1, 1/2, 1/5, 1/10, 1/20]
        for times, amplitude in enumerate(ws, 1):
            w = self.w * times
            yk = amplitude * np.sin(w * x)
            y.append(yk)
        y = sum(y)

        self.x = x
        self.y = y
        self.f = interp1d(x, y, copy=False)
        self.L = L

##        print('freq, c1eq0, L =', self.freq, c1eq0, L)
##        plt.plot(x, y)
##        plt.show()
        return
    
    def __call__(self, L, x):
        assert L <= self.L
        fx = self.f(x)
        return fx
    

def note_dt_ls2wave(note_dt_ls, framerate=44100):
    step = 1/framerate
    window_kwargs = {'L': 10, 'x': np.arange(0, 10+step, step)}
    fwindow = WindowRightAngledTrapezium #WindowOne #WindowKaiser # WindowFDistribution WindowBlackman
    window = fwindow(**window_kwargs)
    
    note_dt_ls = [(note, dt) for note, dt in note_dt_ls]

    dts = set(dt for note, dt in note_dt_ls)
    dt2x = {dt:np.arange(0, dt, step) for dt in dts}
    L = max(dts)

    notes = set(note for note, dt in note_dt_ls)
    note2freq = {note:Frequency(note, L=L) for note in notes}

    dts = set(dt for note, dt in note_dt_ls)
    dt2x = {dt:np.arange(0, dt, step) for dt in dts}
    
    note_dt_set = set(note_dt_ls)
    def fnote_dt2wave(note_dt):
        note, dt = note_dt
        freq = note2freq[note]
        x = dt2x[dt]
        y = freq(dt, x)

        wave = window(dt, x, y)
        return wave
    note_dt2wave = {note_dt: fnote_dt2wave(note_dt) for note_dt in note_dt_ls}

    wave = []
    for note_dt in note_dt_ls:
        w = note_dt2wave[note_dt]
        wave.extend(w)

    return wave

def float_wave2int_with_scale(wave, width):
    fmax = max(wave, key = abs)
    imax = (1 << (8*width - 1)) - 1
    scale = imax / fmax

    wave = [int(w*scale) for w in wave]
    return wave
def int_wave2bytes(wave, width):
    wave = [w.to_bytes(width, byteorder='little', signed=True) for w in wave]
    sample = b''.join(wave)
    return sample


def gen_sample():
    nan = float('NaN')
    framerate = 44100
    shift = 0*12
    float_wave = note_dt_ls2wave([(shift+0, 2), (nan, 2), (shift+0, 2)], framerate=framerate)

    width = 2
    nchannels = 1
    sampwidth = width
    nframes = len(float_wave)
    comptype, compname = 'NONE', 'not compressed'
    params = nchannels, sampwidth, framerate, nframes, comptype, compname

    int_wave = float_wave2int_with_scale(float_wave, width = width)
    sample = int_wave2bytes(int_wave, width = width)
    
##    plt.plot(int_wave)
##    plt.show()
    return params, sample
def gen_wav(fname, postfix = '.wav'):
    params, sample = gen_sample()
    write_wave(fname+postfix, params, sample)
    return

def gen_aifc(fname, postfix = '.aifc'):
    params, sample = gen_sample()
    nchannels, sampwidth, framerate, nframes, comptype, compname = params
    comptype, compname = b'G722', b'G722'
    comptype, compname = b'ALAW', b'ALAW'
    comptype, compname = b'NONE', b'not compressed'
    params = nchannels, sampwidth, framerate, nframes, comptype, compname

    #sample = reverse_each_sample(sample, sampwidth)
    write_aifc(fname+postfix, params, sample)
    return



def showFDistribution(v1=10, v2=4, x = np.arange(0, 10, 0.1)):
    y = calcFDistribution(v1, v2, x)
    plt.plot(x, y)
    plt.show()



def show_sample(sample, nchannels, sampwidth):
    ints_ls = toIntsList(sample, nchannels, sampwidth)
    for ls in ints_ls:
        plt.plot(ls)
        plt.show()
    return

def show_wave(fname='x.wav'):
    params, sample = read_wave(fname)
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = params

    show_sample(sample, nchannels, sampwidth)


    #assert nchannels == 2
    #fsample = mul_stereo(sample, sampwidth, 2, 2)
    #write_wave('x_mul_2.wav', params, fsample)
    return

#showFDistribution()

gen_wav('test9')
show_wave('test9.wav')
        



