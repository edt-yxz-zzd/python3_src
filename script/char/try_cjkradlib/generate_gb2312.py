
import unicodedata as U
def generate_gb2312():
    for char in iter_gb2312():
        print(char)
def iter_gb2312():
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

generate_gb2312()
