
r'''
https://unicode-table.com/en/blocks/miscellaneous-symbols/
https://unicode-table.com/en/blocks/yijing-hexagram-symbols/
https://en.wikipedia.org/wiki/Bagua
https://en.wikipedia.org/wiki/Hexagram_(I_Ching)
https://en.wikipedia.org/wiki/List_of_hexagrams_of_the_I_Ching
https://en.wikipedia.org/wiki/Unicode_character_property#General_Category

https://unicode-table.com/en/blocks/tai-xuan-jing-symbols/
https://en.wikipedia.org/wiki/Taixuanjing


the eight trigrams - 八卦
    U+2630 &#x2630; ☰

the 64 hexagrams
    U+4DC0 &#x4DC0; ䷀


Miscellaneous Symbols 2600—26FF
    U+262F Yin Yang
        Unicode version: 1.1.5
    U+2630 ... 8 Trigram
        Unicode version: 4.1.0


    U+268A ... 2  Monogram
        Unicode version: 4.1.0
    U+268C ... 4  Digram
        Unicode version: 4.1.0


Yijing Hexagram Symbols 4DC0—4DFF
    U+4DC0 ... 64 Hexagram
        Unicode version: 1.1.5

Tai Xuan Jing Symbols 1D300—1D35F
    U+1D300 ... 87
        Unicode version: 4.1.0

==================================================
Sm|So
arrows:
    https://unicode-table.com/en/blocks/arrows/
    https://unicode-table.com/en/2190/
    Arrows 2190—21FF
    U+2190 ... 10
        Unicode version: 1.1.5
        first half (5 chars) <- Sm
        second half (5 chars) <- So
So
dice
    https://unicode-table.com/en/blocks/miscellaneous-symbols/
    https://unicode-table.com/en/2680/
    Miscellaneous Symbols 2600—26FF
    Die Face
    U+2680 ... 6
        Unicode version: 3.2.0
Ideographic Description Characters
    https://unicode-table.com/en/blocks/ideographic-description-characters/
    https://unicode-table.com/en/2FF0/
    Ideographic Description Characters 2FF0—2FFF
    U+2FF0 ... 12
        Unicode version: 3.0.0
Mahjong
    https://unicode-table.com/en/blocks/mahjong-tiles/
    https://unicode-table.com/en/1F000/
    Mahjong Tiles 1F000—1F02F
    U+1F000 ... 43
        Unicode version: 5.2.0
clock
    https://unicode-table.com/en/blocks/miscellaneous-symbols-and-pictographs/
    https://unicode-table.com/en/1F550/
    Miscellaneous Symbols and Pictographs 1F300—1F5FF
    Clock Face
    U+1F550 ... 24
        Unicode version: 6.0.0

'''

import unicodedata

class Data:
    grams_data =\
        {0x262F: 9
        ,0x268A: 6
        ,0x4DC0:64
        ,0x1D300:87
        }
    fun_chars_data =\
        {0x2190: 10
        ,0x2680: 6
        ,0x2FF0: 12
        ,0x1F000: 43
        ,0x1F550: 24
        }

def iter_chars(data):
    for k, num in data.items():
        for i in range(k, k+num):
            ch = chr(i)
            yield ch
def data2string(data):
    return ''.join(iter_chars(data))

# 'So' - Symbol, other
# 'Sm' - Symbol, math
def test_grams():
    assert 79+87 == 166 == 1+8 + 2+4 + 64 + (3-2)+(9-4)+81 == 9 + 6 + 64 + 87
    return test_data(Data.grams_data, 166, 'So'.split())
def test_fun_chars():
    assert 95 == 10 + 6 + 12 + 43 + 24 == (5+5) + 6 + 12 + (4+3 + 4+4 + 9*3 + 1) + (12+12)
    return test_data(Data.fun_chars_data, 95, 'So Sm'.split())
def test_data(data, length, categories):
    chars = data2string(data)
    assert len(chars) == length == len(set(chars)) # unique
    assert ''.join(sorted(chars)) == chars # sorted
    assert set(categories) == set(map(unicodedata.category, chars))
test_grams()
test_fun_chars()


old_print = print
def do_output(file, data):
    def print(*args, **kwargs): old_print(*args, file=file, **kwargs)

    for k, num in data.items():
        for i in range(k, k+num):
            ch = chr(i)
            #hex = f'{i:0>4X}'
            hex = f'{i:X}'
            s = f'U+{hex} &#x{hex}; {ch}'
            print(s)
        print()

    s = data2string(data)
    print(s)
    print(len(s))

def main(argv=None):
    import argparse
    from seed.io.may_open import may_open_stdout

    parser = argparse.ArgumentParser(
        description='show the 8 trigrams'
        )
    parser.add_argument('-o', '--output', type=str, default = None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-fun', '--output_fun_chars', action='store_true'
                        , default = False
                        , help='output fun_chars instead of grams')

    args = parser.parse_args(argv)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'
    data = Data.fun_chars_data if args.output_fun_chars else Data.grams_data

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        do_output(fout, data)


if __name__ == "__main__":
    main()



