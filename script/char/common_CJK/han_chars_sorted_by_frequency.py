
from seed.io.RCXW import make_rcxw__text

ofname = 'han_chars_sorted_by_frequency.u8'
oencoding = 'utf8'

def _make():
    from chinese_character_frequency_list import \
        chinese_character_frequency_list as objs
    return ''.join(obj.han for obj in objs)

han_chars_sorted_by_frequency = make_rcxw__text(_make
        , ofname, encoding=oencoding)()

assert 12041 == len(han_chars_sorted_by_frequency)
if __name__ == '__main__':
    print(len(han_chars_sorted_by_frequency))


