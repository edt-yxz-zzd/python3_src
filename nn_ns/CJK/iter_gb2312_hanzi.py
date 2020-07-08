
__all__ = ['iter_gb2312_hanzi']

import unicodedata as U
def iter_gb2312_hanzi():
    count=0
    OFFSET = 0xA0
    encoding = 'gb2312'
    total = 6763
    for i in range(16, 87+1):
        for j in range(1, 94+1):
            if i == 55 and j >= 90: continue
            bs = bytes([i+OFFSET, j+OFFSET])
            char = bs.decode(encoding)
            assert len(char) == 1
            assert U.name(char).startswith('CJK')
            count += 1
            yield char
    assert count == total

