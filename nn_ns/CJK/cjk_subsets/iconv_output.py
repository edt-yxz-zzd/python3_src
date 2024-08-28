#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/cjk_subsets/iconv_output.py
    charset rngs comes from iconv
        view ../lots/NOTE/encoding/iconv.txt
        view ../lots/NOTE/encoding/iconv.txt.py
view ../../python3_src/nn_ns/CJK/cjk_subsets/rngs4cjk_encodings5iconv.out.txt.7z


[[
fail:lzma open 7z file
===
from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
import lzma
bnm_7z = 'rngs4cjk_encodings5iconv.out.txt.7z'
bs_7z = read_under_pkg_('nn_ns.CJK.cjk_subsets', bnm_7z, xencoding=None)
bs = lzma.decompress(bs_7z)
    fail

from seed.exec.cmd_call import cmd_call
bnm_7z = 'rngs4cjk_encodings5iconv.out.txt.7z'
bnm_txt = 'rngs4cjk_encodings5iconv.out.txt'
r = cmd_call(cmd:=f'7z e dummy -si -so {bnm_txt}'.split(), input=bs_7z)
(outs, errs, returncode, is_timeout) = r
errs
    b'ERROR: \nCan not open encrypted archive. Wrong password?\n\nE_NOTIMPL\n'
if not returncode == 0 or errs:
    raise Exception(cmd, r)

s = outs.decode('ascii')
]]



py -m nn_ns.CJK.cjk_subsets.iconv_output
py -m nn_ns.app.debug_cmd   nn_ns.CJK.cjk_subsets.iconv_output -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.cjk_subsets.iconv_output:__doc__ -ht
[[
py_adhoc_call   nn_ns.CJK.cjk_subsets.iconv_output   @show_infos
===
######################
0:BIG5_2003_8hx2sz
1:BIG5-2003
2:BIG5-2003
3:13897
4:3833
5:None
######################
0:BIG5_HKSCS_1999_8hx2sz
1:BIG5-HKSCS:1999
2:BIG5-HKSCS:1999
3:18272
4:4906
5:None
######################
0:BIG5_HKSCS_2001_8hx2sz
1:BIG5-HKSCS:2001
2:BIG5-HKSCS:2001
3:18388
4:4903
5:None
######################
0:BIG5_HKSCS_2004_8hx2sz
1:BIG5-HKSCS:2004
2:BIG5-HKSCS:2004
3:18511
4:4962
5:None
######################
0:BIG5_HKSCS_8hx2sz
1:BIG5-HKSCS
2:BIG5-HKSCS BIG5-HKSCS:2008 BIG5HKSCS
3:18579
4:4977
5:None
######################
0:BIG_5_8hx2sz
1:BIG-5
2:BIG-5 BIG-FIVE BIG5 BIGFIVE CN-BIG5 CSBIG5
3:13831
4:3820
5:None
######################
0:C99_8hx2sz
1:C99
2:C99
3:974596
4:4
5:None
######################
0:CHINESE_8hx2sz
1:CHINESE
2:CHINESE GB_2312-80 ISO-IR-58 CSISO58GB231280
3:7445
4:3630
5:None
######################
0:CN_GB_8hx2sz
1:CN-GB
2:CN-GB EUC-CN EUCCN GB2312 CSGB2312
3:7573
4:3631
5:None
######################
0:CN_GB_ISOIR165_8hx2sz
1:CN-GB-ISOIR165
2:CN-GB-ISOIR165 ISO-IR-165
3:8387
4:3696
5:None
######################
0:CP1361_8hx2sz
1:CP1361
2:CP1361 JOHAB
3:17177
4:3390
5:None
######################
0:CP50221_8hx2sz
1:CP50221
2:CP50221 ISO-2022-JP-MS
3:13302
4:4325
5:buggy@52utf8:CP50221
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:CP936_8hx2sz
1:CP936
2:CP936 MS936 WINDOWS-936
3:21920
4:140
5:None
######################
0:CP949_8hx2sz
1:CP949
2:CP949 UHC
3:17176
4:3388
5:None
######################
0:DEC_HANYU_8hx2sz
1:DEC-HANYU
2:DEC-HANYU
3:20038
4:3185
5:None
######################
0:DEC_KANJI_8hx2sz
1:DEC-KANJI
2:DEC-KANJI
3:7007
4:4123
5:None
######################
0:EUC_JIS_2004_8hx2sz
1:EUC-JIS-2004
2:EUC-JIS-2004 EUC-JISX0213
3:11399
4:5266
5:None
######################
0:EUC_KR_8hx2sz
1:EUC-KR
2:EUC-KR EUCKR CSEUCKR
3:8355
4:5000
5:None
######################
0:EUC_TW_8hx2sz
1:EUC-TW
2:EUC-TW EUCTW CSEUCTW
3:55570
4:6690
5:None
######################
0:GB18030_8hx2sz
1:GB18030
2:GB18030
3:974596
4:4
5:None
######################
0:GBK_8hx2sz
1:GBK
2:GBK
3:21919
4:139
5:None
######################
0:HZ_8hx2sz
1:HZ
2:HZ HZ-GB-2312
3:7572
4:3632
5:buggy@52utf8:HZ
b'\niconv: (stdin):2:94: cannot convert\n'

######################
0:ISO_2022_CN_8hx2sz
1:ISO-2022-CN
2:ISO-2022-CN CSISO2022CN
3:16425
4:3908
5:buggy@52utf8:ISO-2022-CN
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_CN_EXT_8hx2sz
1:ISO-2022-CN-EXT
2:ISO-2022-CN-EXT
3:51411
4:6454
5:buggy@52utf8:ISO-2022-CN-EXT
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_JP_1_8hx2sz
1:ISO-2022-JP-1
2:ISO-2022-JP-1
3:13075
4:4313
5:buggy@52utf8:ISO-2022-JP-1
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_JP_2004_8hx2sz
1:ISO-2022-JP-2004
2:ISO-2022-JP-2004 ISO-2022-JP-3
3:11401
4:5265
5:buggy@52utf8:ISO-2022-JP-2004
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_JP_2_8hx2sz
1:ISO-2022-JP-2
2:ISO-2022-JP-2 CSISO2022JP2
3:18829
4:5848
5:buggy@52utf8:ISO-2022-JP-2
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_JP_8hx2sz
1:ISO-2022-JP
2:ISO-2022-JP CSISO2022JP
3:7008
4:4126
5:buggy@52utf8:ISO-2022-JP
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_KR_8hx2sz
1:ISO-2022-KR
2:ISO-2022-KR CSISO2022KR
3:8352
4:5002
5:buggy@52utf8:ISO-2022-KR
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_IR_149_8hx2sz
1:ISO-IR-149
2:ISO-IR-149 KOREAN KSC_5601 KS_C_5601-1987 KS_C_5601-1989 CSKSC56011987
3:8227
4:4999
5:None
######################
0:ISO_IR_87_8hx2sz
1:ISO-IR-87
2:ISO-IR-87 JIS0208 JIS_C6226-1983 JIS_X0208 JIS_X0208-1983 JIS_X0208-1990 X0208 CSISO87JISX0208
3:6879
4:4122
5:None
######################
0:JAVA_8hx2sz
1:JAVA
2:JAVA
3:974596
4:4
5:None
######################
0:MS_KANJI_8hx2sz
1:MS_KANJI
2:MS_KANJI SHIFT-JIS SHIFT_JIS SJIS CSSHIFTJIS
3:7070
4:4128
5:None
######################
0:SHIFT_JIS_2004_8hx2sz
1:SHIFT_JIS-2004
2:SHIFT_JIS-2004 SHIFT_JISX0213
3:11399
4:5267
5:None
######################
######################
0:BIG5_2003_8hx2sz
1:BIG5-2003
2:BIG5-2003
3:13897
4:3833
5:None
######################
0:BIG5_HKSCS_1999_8hx2sz
1:BIG5-HKSCS:1999
2:BIG5-HKSCS:1999
3:18272
4:4906
5:None
######################
0:BIG5_HKSCS_2001_8hx2sz
1:BIG5-HKSCS:2001
2:BIG5-HKSCS:2001
3:18388
4:4903
5:None
######################
0:BIG5_HKSCS_2004_8hx2sz
1:BIG5-HKSCS:2004
2:BIG5-HKSCS:2004
3:18511
4:4962
5:None
######################
0:BIG5_HKSCS_8hx2sz
1:BIG5-HKSCS
2:BIG5-HKSCS BIG5-HKSCS:2008 BIG5HKSCS
3:18579
4:4977
5:None
######################
0:BIG_5_8hx2sz
1:BIG-5
2:BIG-5 BIG-FIVE BIG5 BIGFIVE CN-BIG5 CSBIG5
3:13831
4:3820
5:None
######################
0:C99_8hx2sz
1:C99
2:C99
3:974596
4:4
5:None
######################
0:CHINESE_8hx2sz
1:CHINESE
2:CHINESE GB_2312-80 ISO-IR-58 CSISO58GB231280
3:7445
4:3630
5:None
######################
0:CN_GB_8hx2sz
1:CN-GB
2:CN-GB EUC-CN EUCCN GB2312 CSGB2312
3:7573
4:3631
5:None
######################
0:CN_GB_ISOIR165_8hx2sz
1:CN-GB-ISOIR165
2:CN-GB-ISOIR165 ISO-IR-165
3:8387
4:3696
5:None
######################
0:CP1361_8hx2sz
1:CP1361
2:CP1361 JOHAB
3:17177
4:3390
5:None
######################
0:CP50221_8hx2sz
1:CP50221
2:CP50221 ISO-2022-JP-MS
3:13302
4:4325
5:buggy@52utf8:CP50221
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:CP936_8hx2sz
1:CP936
2:CP936 MS936 WINDOWS-936
3:21920
4:140
5:None
######################
0:CP949_8hx2sz
1:CP949
2:CP949 UHC
3:17176
4:3388
5:None
######################
0:DEC_HANYU_8hx2sz
1:DEC-HANYU
2:DEC-HANYU
3:20038
4:3185
5:None
######################
0:DEC_KANJI_8hx2sz
1:DEC-KANJI
2:DEC-KANJI
3:7007
4:4123
5:None
######################
0:EUC_JIS_2004_8hx2sz
1:EUC-JIS-2004
2:EUC-JIS-2004 EUC-JISX0213
3:11399
4:5266
5:None
######################
0:EUC_KR_8hx2sz
1:EUC-KR
2:EUC-KR EUCKR CSEUCKR
3:8355
4:5000
5:None
######################
0:EUC_TW_8hx2sz
1:EUC-TW
2:EUC-TW EUCTW CSEUCTW
3:55570
4:6690
5:None
######################
0:GB18030_8hx2sz
1:GB18030
2:GB18030
3:974596
4:4
5:None
######################
0:GBK_8hx2sz
1:GBK
2:GBK
3:21919
4:139
5:None
######################
0:HZ_8hx2sz
1:HZ
2:HZ HZ-GB-2312
3:7572
4:3632
5:buggy@52utf8:HZ
b'\niconv: (stdin):2:94: cannot convert\n'

######################
0:ISO_2022_CN_8hx2sz
1:ISO-2022-CN
2:ISO-2022-CN CSISO2022CN
3:16425
4:3908
5:buggy@52utf8:ISO-2022-CN
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_CN_EXT_8hx2sz
1:ISO-2022-CN-EXT
2:ISO-2022-CN-EXT
3:51411
4:6454
5:buggy@52utf8:ISO-2022-CN-EXT
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_JP_1_8hx2sz
1:ISO-2022-JP-1
2:ISO-2022-JP-1
3:13075
4:4313
5:buggy@52utf8:ISO-2022-JP-1
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_JP_2004_8hx2sz
1:ISO-2022-JP-2004
2:ISO-2022-JP-2004 ISO-2022-JP-3
3:11401
4:5265
5:buggy@52utf8:ISO-2022-JP-2004
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_JP_2_8hx2sz
1:ISO-2022-JP-2
2:ISO-2022-JP-2 CSISO2022JP2
3:18829
4:5848
5:buggy@52utf8:ISO-2022-JP-2
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_JP_8hx2sz
1:ISO-2022-JP
2:ISO-2022-JP CSISO2022JP
3:7008
4:4126
5:buggy@52utf8:ISO-2022-JP
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_2022_KR_8hx2sz
1:ISO-2022-KR
2:ISO-2022-KR CSISO2022KR
3:8352
4:5002
5:buggy@52utf8:ISO-2022-KR
b'iconv: (stdin):2:0: cannot convert\n'

######################
0:ISO_IR_149_8hx2sz
1:ISO-IR-149
2:ISO-IR-149 KOREAN KSC_5601 KS_C_5601-1987 KS_C_5601-1989 CSKSC56011987
3:8227
4:4999
5:None
######################
0:ISO_IR_87_8hx2sz
1:ISO-IR-87
2:ISO-IR-87 JIS0208 JIS_C6226-1983 JIS_X0208 JIS_X0208-1983 JIS_X0208-1990 X0208 CSISO87JISX0208
3:6879
4:4122
5:None
######################
0:JAVA_8hx2sz
1:JAVA
2:JAVA
3:974596
4:4
5:None
######################
0:MS_KANJI_8hx2sz
1:MS_KANJI
2:MS_KANJI SHIFT-JIS SHIFT_JIS SJIS CSSHIFTJIS
3:7070
4:4128
5:None
######################
0:SHIFT_JIS_2004_8hx2sz
1:SHIFT_JIS-2004
2:SHIFT_JIS-2004 SHIFT_JISX0213
3:11399
4:5267
5:None
######################
===
]]


xxx from nn_ns.CJK.cjk_subsets.iconv_output import 
    CN_GB_ISOIR165_8hx2sz
    CN_GB_8hx2sz
    CP936_8hx2sz
    GB18030_8hx2sz
    GBK_8hx2sz
    HZ_8hx2sz
    ISO_2022_CN_EXT_8hx2sz
    ISO_2022_CN_8hx2sz
    ISO_2022_JP_2_8hx2sz
#]]]'''
if 0:
    __all__ = r'''
    C99_8hxXhxsz_ls
    C99_8hx2sz
    CN_GB_ISOIR165_8hxXhxsz_ls
    CN_GB_ISOIR165_8hx2sz
    CN_GB_8hxXhxsz_ls
    CN_GB_8hx2sz
    CP936_8hxXhxsz_ls
    CP936_8hx2sz
    GB18030_8hxXhxsz_ls
    GB18030_8hx2sz
    GBK_8hxXhxsz_ls
    GBK_8hx2sz
    HZ_8hxXhxsz_ls
    HZ_8hx2sz
    ISO_10646_UCS_4_8hxXhxsz_ls
    ISO_10646_UCS_4_8hx2sz
    ISO_2022_CN_EXT_8hxXhxsz_ls
    ISO_2022_CN_EXT_8hx2sz
    ISO_2022_CN_8hxXhxsz_ls
    ISO_2022_CN_8hx2sz
    ISO_2022_JP_2_8hxXhxsz_ls
    ISO_2022_JP_2_8hx2sz
    JAVA_8hxXhxsz_ls
    JAVA_8hx2sz
    UCS_4_INTERNAL_8hxXhxsz_ls
    UCS_4_INTERNAL_8hx2sz
    UCS_4_SWAPPED_8hxXhxsz_ls
    UCS_4_SWAPPED_8hx2sz
    UCS_4BE_8hxXhxsz_ls
    UCS_4BE_8hx2sz
    UCS_4LE_8hxXhxsz_ls
    UCS_4LE_8hx2sz
    UNICODE_1_1_UTF_7_8hxXhxsz_ls
    UNICODE_1_1_UTF_7_8hx2sz
    UTF_16_8hxXhxsz_ls
    UTF_16_8hx2sz
    UTF_16BE_8hxXhxsz_ls
    UTF_16BE_8hx2sz
    UTF_16LE_8hxXhxsz_ls
    UTF_16LE_8hx2sz
    UTF_32_8hxXhxsz_ls
    UTF_32_8hx2sz
    UTF_32BE_8hxXhxsz_ls
    UTF_32BE_8hx2sz
    UTF_32LE_8hxXhxsz_ls
    UTF_32LE_8hx2sz
    UTF_8_8hxXhxsz_ls
    UTF_8_8hx2sz
'''.split()#'''

__all__ = r'''
nm2info
nm4var_Z_nm
nm4var_Z_hx2sz
'''.split()#'''
__all__

from functools import cache


def __():
    #_read_the_output_txt
    from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
    bnm_7z = 'rngs4cjk_encodings5iconv.out.txt.7z'
    bs_7z = read_under_pkg_(__package__, bnm_7z, xencoding=None)
    import lzma

@cache
def _read_the_output_txt():
    bnm_7z = 'rngs4cjk_encodings5iconv.out.txt.7z'
    bnm_txt = 'rngs4cjk_encodings5iconv.out.txt'
    from seed.exec.cmd_call import cmd_call
    from pathlib import Path
    dir4pkg = Path(__file__).parent
    path_7z = dir4pkg / bnm_7z
    r = cmd_call(cmd:=[*'7z e -so'.split(), path_7z.as_posix(), bnm_txt])
    (outs, errs, returncode, is_timeout) = r
    if not returncode == 0 or errs:
        raise Exception(cmd, r)

    the_output_txt = outs.decode('utf8')
    assert len(the_output_txt) == 1601226, len(the_output_txt)
    return the_output_txt
if 0b000:
    _read_the_output_txt()

def _view_eval(s, /):
    from seed.tiny import MapView
    return MapView(eval(s))
def _frozen_eval(s, /):
    from seed.types.FrozenDict import FrozenDict
    return FrozenDict(eval(s))
@cache
def _parse_the_output_txt(the_output_txt=None, /):
    r'''[[[
######################
'C99'
'C99'
974596
4
C99_8hx2sz = (
{0x0
: 55296
,0xF900
: 919296
,0xFFFFE
: 2
,0x10FFFE
: 2
}
)
######################

... ...

######################
'CP932'
'CP932'
∠‖
2220:2016
，−
FF0C:2212
｝〜
FF5D:301C
ﾟ¢
FF9F:A2
skip:CP932
######################
'ISO-2022-JP CSISO2022JP'
buggy@52utf8:ISO-2022-JP
b'iconv: (stdin):2:0: cannot convert\n'
'ISO-2022-JP'
7008
4126
ISO_2022_JP_8hx2sz = (
{
... ...
}
)
######################

... ...

    #]]]'''#'''
    if the_output_txt is None:
        the_output_txt = _read_the_output_txt()
    from seed.tiny import MapView
    from seed.types.FrozenDict import FrozenDict
    from seed.types.LazyValueDict import LazyValueDict
    import re
    #rex = re.compile(r"(?<=\n)#{22}\n'[^']*'\n(buggy@52utf8:\S*\nb'[^']*'\n)?'[^']*'\n\d+\n\d+\n\w+ = [(]\n[{][^{}]*[}]\n[)]\n")
    rex = re.compile(r"(?<=\n)#{22}\n(?P<nms>'[^']*')\n(?P<buggy>buggy@52utf8:\S*\nb'[^']*'\n)?(?P<nm>'[^']*')\n(?P<num_chars>\d+)\n(?P<num_rngs>\d+)\n(?P<nm4var>\w+) = [(]\n(?P<hx2sz>[{][^{}]*[}])\n[)]\n")
    #groupss = rex.findall(the_output_txt)
        # :: [m.groups() for m in ms]
    [*ms] = rex.finditer(the_output_txt)
    assert len(ms) == 34, len(ms)
    nm4var_Z_nm = {}
    nm4var_Z_hx2sz = lazy_d = LazyValueDict()
    nm2info = {}
    for m in ms:
        #print(m)
        d = m.groupdict()
        if 0:
            if not (s:=d['buggy']) is None:
                print(s)
        nms = tuple(eval(d['nms']).split())
        nm = eval(d['nm'])
        buggy = d['buggy']
        num_chars = int(d['num_chars'])
        num_rngs = int(d['num_rngs'])
        nm4var = d['nm4var']
        #hx2sz = eval(d['hx2sz'])
        hx2sz__str = d['hx2sz']


        nm4var_Z_nm[nm4var] = nm
        lazy_d.set_lazy(nm4var, _frozen_eval, hx2sz__str)
        for _nm in nms:
            nm2info[_nm] = (FrozenDict
            (nms=nms
            ,nm=nm
            ,buggy=buggy
            ,num_chars=num_chars
            ,num_rngs=num_rngs
            ,nm4var=nm4var
            #,hx2sz__str=hx2sz__str
            ))
    return (FrozenDict(nm2info), FrozenDict(nm4var_Z_nm), MapView(nm4var_Z_hx2sz))
(nm2info, nm4var_Z_nm, nm4var_Z_hx2sz) = _parse_the_output_txt()
if 0b000:
    print(nm2info)
    print(nm4var_Z_nm)
    print(nm4var_Z_hx2sz[nm2info['C99']['nm4var']])

def show_infos(nm2info=None, nm4var_Z_nm=None, nm4var_Z_hx2sz=None):
    g = globals()
    if nm2info is None:
        nm2info = g['nm2info']
    if nm4var_Z_nm is None:
        nm4var_Z_nm = g['nm4var_Z_nm']
    if nm4var_Z_hx2sz is None:
        nm4var_Z_hx2sz = g['nm4var_Z_hx2sz']

    for nm4var, nm in sorted(nm4var_Z_nm.items()):
        print('#'*22)
        info = nm2info[nm]
        nms = info['nms']
        nms__str = ' '.join(nms)
        num_chars = info['num_chars']
        num_rngs = info['num_rngs']
        buggy = info['buggy']
        print(f'0:{nm4var}')
        print(f'1:{nm}')
        print(f'2:{nms__str}')
        print(f'3:{num_chars}')
        print(f'4:{num_rngs}')
        print(f'5:{buggy}')
    print('#'*22)
if 0b000:
    show_infos(nm2info, nm4var_Z_nm, nm4var_Z_hx2sz)



__all__
from nn_ns.CJK.cjk_subsets.iconv_output import *
