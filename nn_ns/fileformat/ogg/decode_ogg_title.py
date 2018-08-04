r'''
i.e.
E:\multimedia\audio\music\bgm\赤印_BGM\s07.ogg
    AkanEromi - [Snow Night OST #07] Ç¨ÒÆÕß = 迁移者


show in foobar:
    'in ogg' ??           ==>> 'show in foobar' 'Ç¨ÒÆÕß'     ==>> 'as_bytes' b'\xc7\xa8\xd2\xc6\xd5\xdf' ==>> 'gbk' '迁移者'
    'in ogg' b'E\xc3\xb3' ==>> 'show in foobar|utf-8' 'Eó'
                          ==>> 'gbk' 'E贸'
    'in ogg' b'\xc3\x9e'  ==>> 'show in foobar|utf-8' 'Þ'    ==>> 'as_bytes' b'\xde' ==>> ??
                          ==>> 'gbk' '脼'
                          ==>> 'utf_16_le' '黃'
    'in ogg' b'\xc3\xaaN' ==>> 'show in foobar|utf-8' 'êN'   ==>> 'as_bytes' b'\xeaN' ==>> 'gbk' '闚'
                          ==>> 'gbk' '锚N'


two ways:
    'in ogg' get title_bytes
    1) title_bytes ==>> 'gbk' title
    2) title_bytes ==>> 'utf-8' xxx_name ==>> 'as_bytes' xxx_bytes ==>> 'gbk' title
'''


import os.path, sys, unicodedata as ud
from pprint import pprint
import glob

from sand import to_names, all_encodings
from extract_ogg_vorbis_info import read_ogg_infos_from_path

            
def as_bytes(string):
    return bytes(map(ord, string))

def oggs2iter_fname_titlebytes_ls(fnames):
    starts = b'title='
    for fname in fnames:
        #print(fname)
        _, infos = read_ogg_infos_from_path(fname)
        for info in infos:
            #print(info)
            if info.lower().startswith(starts):
                title_bytes = info[len(starts):]
                yield fname, title_bytes


def title_bytes2titles(title_bytes):
    ls = []
    title1 = None
    try:
        title1 = title_bytes.decode('gbk')
    except:
        pass
    ls.append(title1)

    title2 = None
    try:
        title2 = as_bytes(title_bytes.decode('utf-8')).decode('gbk')
    except:
        pass
    ls.append(title2)
    return ls


def oggs_to_ogg2titles(fnames):
    d = {}
    for fname, title_bytes in oggs2iter_fname_titlebytes_ls(fnames):
        ts = title_bytes2titles(title_bytes)
        d[fname] = ts
    return d

def show_folder_ogg_title(path = r'E:\multimedia\audio\music\bgm\赤印_BGM'):
    fnames = glob.iglob(os.path.join(path, '*.ogg'))
    d = oggs_to_ogg2titles(fnames)
    pprint(d)




def find_encoding(string, string_bytes):
    title = string
    title_bytes = string_bytes
    print(title, title_bytes)
    for e in all_encodings:
        try:
            bs = title.encode(e)
        except:
            pass
        else:
            if bs == title_bytes:
                print('encode:', e)
        try:
            name = title_bytes.decode(e)
        except:
            pass
        else:
            if name == title:
                print('decode:', e)


if 0:
    # what is the encoding used in "foobar"???
    # I cannot find it # copy failure: len(title) == 3
    # utf_8
    # 'Eó' == b'E\xc3\xb3'
    title = 'Eó'
    assert len(title) == 3
    title = 'Eó'
    assert len(title) == 2
    title_bytes = b'E\xc3\xb3'
    find_encoding(title, title_bytes)
    find_encoding('Ç¨ÒÆÕß', b'\xc7\xa8\xd2\xc6\xd5\xdf')
    
    raise

def correct_misdecode(misdecoded_name,
                      guess_encodings='gbk',
                      wrong_encoding='as_bytes',
                      *, show=True, append=b''):
    if type(misdecoded_name) is bytes:
        bs = misdecoded_name
    elif wrong_encoding == 'as_bytes':
        bs = bytes(map(ord, misdecoded_name))
    else:
        bs = misdecoded_name.encode(wrong_encoding)

    if append: bs += append
    if show:
        print(bs)

    if isinstance(guess_encodings, str):
        guess_encodings = to_names(guess_encodings)

    f = bs.decode
    d = {}
    for encoding in guess_encodings:
        try:
            name = f(encoding)
        except UnicodeError:
            continue
        except Exception as e:
            print(e, file=sys.stderr)
            continue
        else:
            if name not in d:
                d[name] = []
            d[name].append(encoding)
            #ls.append((encoding, name))
    return d
    return ls
    return list(map(f, guess_encodings)) # bs.encode(guess_encoding)
    

assert {'迁移者':['gbk']} == correct_misdecode('Ç¨ÒÆÕß', show=False)


guess_encodings = '''
ascii gbk gb18030
big5 big5hkscs hz
iso2022_jp iso2022_jp_1 iso2022_jp_2
iso2022_jp_2004 iso2022_jp_3 iso2022_jp_ext iso2022_kr
shift_jis shift_jis_2004 shift_jisx0213
utf_32 utf_32_be utf_32_le
utf_16 utf_16_be utf_16_le
utf_7 utf_8 utf_8_sig
mbcs palmos
'''


def show_result_of_correct(name, guess_encodings, *, show=True, append=b''):
    print('---------- {} -----------'.format(name))
    print(name)
    r = correct_misdecode(name, guess_encodings, show=show, append=append)
    pprint(r)
    print()

if 0:
    show_result_of_correct(b'E\xc3\xb3', all_encodings)
    raise

if 0:
    r = correct_misdecode('Þ', guess_encodings)
    print(r)

    n = ud.name('ﾞ')
    print(n)

    for name in ['Ç¨ÒÆÕß', b'\xc3\x87\xc2\xa8\xc3\x92\xc3\x86\xc3\x95\xc3\x9f', b'\xc7\xa8\xd2\xc6\xd5\xdf',
                 'Þ', b'\xc3\x9e',
                 'ÞÆî', b'\xde\xc6\xee',
                 'J}',
                 'êN', b'\xc3\xaaN',
                 'Eó', b'E\xc3\xb3',
                 'Æí', 'r¹âÉ°']:
        show_result_of_correct(name, guess_encodings)












