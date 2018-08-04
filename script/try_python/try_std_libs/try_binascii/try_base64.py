
'''
using 65 char 64+1('=')


'''


import base64
f = base64.standard_b64encode
def verify(input_bytes):
    result = base64.standard_b64encode(input_bytes)
    assert type(result) == bytes
    assert len(result) % 4 == 0
    pad_len = len(result.split(b'=')) - 1
    assert result.endswith(b'=' * pad_len)
    assert not result.endswith(b'=' * (pad_len+1))
    data_len = len(result)-pad_len
    assert set(result[data_len:]) <= set(b'=')
    assert b'=' not in result[:data_len]

    bit_len = len(input_bytes) * 8
    data_len2 = (bit_len + 6-1)//6
    pad_len2 = (data_len2 + 4-1)//4 * 4 - data_len2
    assert pad_len == pad_len2




allbytes = bytes(range(0x100))
int2byte = lambda i: bytes([i])
                           
# NOTE: the pad char '=' !!!!!!!!!
table_ = b''.join(sorted(set(f(int2byte(i))[:1] for i in range(0x100))))
table = b'+/0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
assert table == table_
assert len(table) == 64

assert f(b'\0') == b'AA=='
bs = b'012345678'
for i in range(len(bs)):
    data = bs[:i]
    print(f(data))
    verify(data)

