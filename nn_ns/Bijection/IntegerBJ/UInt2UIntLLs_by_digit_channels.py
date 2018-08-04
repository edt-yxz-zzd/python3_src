

'''
UInt <-> UIntRadixReprLE(R)
    1) <-> [UIntRadixReprLE(R)]{L} # remove channel tail 0s
        L channels
        R,L=3,2
        ([1,2,1,2,0,0,0,2,1,2,0], 2) ==>> [([1,1,0,0],1), ([2,2,0,2,2],2)]
    2) <-> ([[BiDigit(R-1)]]{L-1}, UIntRadixReprLE(R))  # channel ended by 0
        (L-1) channel
        R,L=6,4
        ([1,2,3,1,2,3,0,2,3,2,3,2,3,2,0,2,2,0,   2,0], 2)
        # 1     1
        #   2     2     2   2   2   2   2 2      2,2   2
        #     3     3     3   3   3
        ==>> ([[1,1], [2,2,2,2,2,2,2,2], [3,3,3,3,3]], {'channel2':([2,0],2)})

    3) <-> ([[BiDigit(R-1)]]{L-1}, UIntRadixReprLE(R))  # split chunks by 0
        L = 3
        ([1,1,1,0,2,2,2,0,3,3,0,3], 3) ==>> ([[1]*3, [2]*3], ([3,3,0,3],3))
        ([1,1,1,0,2,2], 2) ==>> ([[1]*3, [2]*3], ())
        ([1,1], 1) ==>> ([[1]*3, []], ())
            <==> UInt2UIntLLs_by_1digits_LE_2add_headMINs{head=tail}
'''


__all__ = '''
    BiDigitsLLs_UIntRadixReprLE_pair
    BiDigitsLLs_UIntRadixReprLE2UIntL1L1s
    UIntRadixReprLE2BiDigitChunks_UIntRadixReprLE_by_split0
    UIntRadixReprLE2BiDigitChannels_UIntRadixReprLE_by_endBy0

    UIntRadixReprLE2UIntLLs_by_split0
    UIntRadixReprLE2UIntLLs_by_channels_endby0
    aUIntRadixReprLE2UIntLLs_by_split0__R3L6
    aUIntRadixReprLE2UIntLLs_by_channels_endby0__R3L5
    '''.split()

from ..Bijection import Bijection
from ..NumberTVs import UIntRadixReprLE, BiDigit, UInt
from ..SeqBJ import SplitArrayLast
from .UInt2UIntRadixReprLE import UInt2UIntRadixReprLE
from .UInt2Digits import UInt2BiDigits__little_endian
from .import_split_seq import split_seq2seq1s, join
from .BiLink import BiLink

from itertools import chain


def BiDigitsLLs_UIntRadixReprLE2UIntL1L1s(aBiDigits2UInt, big_radix, fst_len):
    # ([BiDigit(R-1)]<->UInt) -> (([[BiDigit(R-1)]]{L}, UIntRadixReprLE(R)) <-> [UInt]{L+1})
    L = fst_len
    return +(+(aBiDigits2UInt[L, L] * ~UInt2UIntRadixReprLE(big_radix))
            >> ~SplitArrayLast(UInt[L+1,L+1]))

def UIntRadixReprLE2UIntLLs_by_split0(big_radix, L):
    assert L >= 1
    aBiDigits2UInt = ~UInt2BiDigits__little_endian(big_radix-1)
    b1 = UIntRadixReprLE2BiDigitChunks_UIntRadixReprLE_by_split0(big_radix, L-1)
    b2 = BiDigitsLLs_UIntRadixReprLE2UIntL1L1s(aBiDigits2UInt, big_radix, L-1)
    return +(b1 >> b2)
def UIntRadixReprLE2UIntLLs_by_channels_endby0(big_radix, L):
    assert L >= 1
    aBiDigits2UInt = ~UInt2BiDigits__little_endian(big_radix-1)
    b1 = UIntRadixReprLE2BiDigitChannels_UIntRadixReprLE_by_endBy0(big_radix, L-1)
    b2 = BiDigitsLLs_UIntRadixReprLE2UIntL1L1s(aBiDigits2UInt, big_radix, L-1)
    return +(b1 >> b2)
def BiDigitsLLs_UIntRadixReprLE_pair(big_radix, num_channels):
    return +(BiDigit(big_radix-1)[0,None][num_channels, num_channels]
            * UIntRadixReprLE(big_radix))
class UIntRadixReprLE2BiDigitChannels_UIntRadixReprLE_by_endBy0(Bijection):
    # UIntRadixReprLE(R) <-> ([[BiDigit(R-1)]]{L-1}, UIntRadixReprLE(R)) # endby0
    def __init__(self, radix, num_channels:'L-1'):
        assert radix >= 1, TypeError
        assert num_channels >= 0, TypeError
        self.radix = radix
        self.num_channels = L_1 = num_channels
        self.InputType = UIntRadixReprLE(radix)
        #self.OutputType = +(BiDigit(radix-1)[0,None][L_1,L_1] * self.InputType)
        self.OutputType = BiDigitsLLs_UIntRadixReprLE_pair(radix, num_channels)

    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        # if self.num_channels == 0: return ((), input)
        r = self.__untypechecked_forward(input)
        if self.num_channels == 0:
            assert r == ((), input)
        return r
    def __untypechecked_forward(self, input):
        # if self.num_channels == 0: return ((), input)
        if not input: return (((),)*self.num_channels, ())
        tail, head = input
        assert head

        digits = tail + (head,)
        d = BiLink.keys2single_link(range(self.num_channels))
        channel_idx = 0 # channel idx
        digits_idx = 0 # digits idx
        channels = [[] for _ in range(self.num_channels)]
        while d:
            for digits_idx in range(digits_idx, len(digits)):
                succ = d.succ(channel_idx)
                if digits[digits_idx]:
                    channels[channel_idx].append(digits[digits_idx])
                    channel_idx = succ
                else:
                    del d[channel_idx]
                    digits_idx += 1
                    channel_idx = succ
                    break
            else:
                digits_idx += 1
                assert d
                # no remain digits
                snd = ()
                break
        else:
            assert not d
            # remain digits
            remain_digits = digits[digits_idx:]
            assert remain_digits
            snd = (remain_digits[:-1], remain_digits[-1])
        return (tuple(map(tuple, channels)), snd)

    def untypechecked_backward(self, output):
        channels, remain_digits_head = output
        if self.num_channels:
            _, channel_idx_last = max(
                (len(channel), i) for i, channel in enumerate(channels))
        else:
            channel_idx_last = 0

        if remain_digits_head:
            remain_digits, head = remain_digits_head
            iter_remain_digits = chain(remain_digits, [head])
        else:
            iter_remain_digits = iter([])
        d = BiLink.keys2single_link(range(self.num_channels))
        digits = []
        channel_idx = 0
        channels = tuple(map(list, channels))
        for channel in channels: channel.reverse()
        while d:
            succ = d.succ(channel_idx)
            channel = channels[channel_idx]
            if channel:
                digits.append(channel.pop())
            else:
                digits.append(0)
                del d[channel_idx]
            channel_idx = succ
        assert channel_idx == channel_idx_last

        if remain_digits_head:
            digits = chain(digits, iter_remain_digits)
        else:
            while digits and not digits[-1]:
                digits.pop()
        digits = tuple(digits)

        if digits:
            return digits[:-1], digits[-1]
        return ()


    def get_construct_info(self):
        return self.make_args_kwargs(self.radix, self.num_channels)








class UIntRadixReprLE2BiDigitChunks_UIntRadixReprLE_by_split0(Bijection):
    'UIntRadixReprLE(R) <-> ([[BiDigit(R-1)]]{L-1}, UIntRadixReprLE(R))  # split chunks by 0'
    def __init__(self, radix, num_chunks:'L-1'):
        assert radix >= 1, TypeError
        assert num_chunks >= 0, TypeError
        self.radix = radix
        self.num_chunks = L_1 = num_chunks
        self.InputType = UIntRadixReprLE(radix)
        self.OutputType = BiDigitsLLs_UIntRadixReprLE_pair(radix, num_chunks)

    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        if not input: return (((),)*self.num_chunks, ())
        tail, head = input
        assert head

        chunks = split_seq2seq1s(tail+(head,), 0, tuple, self.num_chunks)
        L = len(chunks)
        if L <= self.num_chunks:
            chunks += ((),) * (self.num_chunks - L)
            return chunks, ()
        else:
            assert L == self.num_chunks+1
            chunks, remain = chunks[:-1], chunks[-1]
            assert remain
            return chunks, (remain[:-1], remain[-1])
    def untypechecked_backward(self, output):
        chunks, remain = output
        if remain:
            tail, head = remain
            remain = chain(tail, [head])
        chunks = chain(chunks, [remain])

        digits = join((0,), chunks, list)
        while digits and not digits[-1]:
            digits.pop()
        digits = tuple(digits)
        if digits:
            return digits[:-1], digits[-1]
        return ()

    def get_construct_info(self):
        return self.make_args_kwargs(self.radix, self.num_chunks)



aUIntRadixReprLE2UIntLLs_by_split0__R3L6 \
    = UIntRadixReprLE2UIntLLs_by_split0(3, 6)
aUIntRadixReprLE2UIntLLs_by_channels_endby0__R3L5 \
    = UIntRadixReprLE2UIntLLs_by_channels_endby0(3, 5)


