
r'''
00h : "OggS"
3Ah : "OggS"
67h/68h :
    "vorbis"
    + sized_bytes(#startswith "Xiph.Org"#)
    + int32le num_infos
    + sized_bytes[num_infos]
    # err:  + int32le 1 # xxxxxxxxxxx

sized_bytes = struct{int32le len; bytes[len];};
'''

import io
from sand import CheckError, DecodeUtils_32le # check_bytes, read_sized_bytes, read_sized_array
from read_generic_ogg_file import \
     iter_grouped_ogg_infos_from_path, \
     pages_of_logic_bitstream2iter_packets

def read_ogg_infos_from_path(path):
    it = iter_grouped_ogg_infos_from_path(path)
    for ID2pages, *_ in it:
        assert len(ID2pages) == 1
        for pages in ID2pages.values():
            second_packet = i = None
            for i, packet in enumerate(pages_of_logic_bitstream2iter_packets(pages)):
                if i == 1:
                    second_packet = packet
                    break
            assert i == 1
            break
        break

    file = io.BytesIO(second_packet)
    du = DecodeUtils_32le(file)
    du.check_bytes(b"\x03vorbis")

    return _read_ogg_infos__after_vorbis(du)

def _old__read_ogg_infos_from_path(path):
    with open(path, 'rb') as fin:
        return read_ogg_infos(fin)
    
def read_ogg_infos(file):
    'should open file in "rb" mode'
    du = DecodeUtils_32le(file)
    
    du.check_bytes(b"OggS", 0x00)
    du.check_bytes(b"OggS", 0x3A)
    try:
        du.check_bytes(b"vorbis", 0x67)
    except CheckError:
        du.check_bytes(b"vorbis", 0x68)

    return read_ogg_infos__after_vorbis(file)

def _read_ogg_infos__after_vorbis(du):
    fmt_info = du.read_sized_bytes()
    if not fmt_info.startswith(b"Xiph.Org"):
        raise ValueError('not fmt_info.startswith(b"Xiph.Org")')

    infos = du.read_sized_array(du.read_sized_bytes)
    #xxxx du.check_bytes(b"\x01\x00\x00\x00")
    return fmt_info, infos



def t():

    for fname in [r'E:\multimedia\audio\music\bgm\赤印_BGM\v11.ogg',
                  r'E:\multimedia\audio\music\bgm\赤印_BGM\v12.ogg',
                  r'E:\multimedia\audio\music\bgm\赤印_BGM\v13.ogg',
                  #r'E:\multimedia\audio\music\bgm\赤印_BGM\v14.ogg',
                  r'E:\multimedia\audio\music\bgm\赤印_BGM\v19.ogg',
                  #r'E:\multimedia\audio\music\bgm\赤印_BGM\s06.ogg',
                  #r'E:\multimedia\audio\music\bgm\赤印_BGM\s07.ogg',
                  r'C:\Users\Administrator\Desktop\天上人间.ogg']:
        print('----------------------------------------')
        print(fname)
        r = read_ogg_infos_from_path(fname)
        print(r)
        print()


t()


    
