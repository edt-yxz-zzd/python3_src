#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/fileformat/font/freetype2/freetype2_ftdump.py
    view ../../python3_src/nn_ns/fileformat/font/freetype2/freetype2-note.txt
    #wrapper-script:xxx:cp ~/ex_src/font/ft2demos-2.10.2/bin/ftdump ~/../usr/bin/
    view  ../../python3_src/nn_ns/fileformat/font/freetype2/ftdump.c
    view ../../python3_src/nn_ns/fileformat/font/freetype2/ftdump



nn_ns.fileformat.font.freetype2.freetype2_ftdump
py -m nn_ns.app.debug_cmd   nn_ns.fileformat.font.freetype2.freetype2_ftdump -x
py -m nn_ns.app.doctest_cmd nn_ns.fileformat.font.freetype2.freetype2_ftdump:__doc__ --ndiff -ff -v
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @f
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %nn_ns.fileformat.font.freetype2.freetype2_ftdump:XXX@T    =T      ++exclude_prefixes:_
from nn_ns.fileformat.font.freetype2.freetype2_ftdump import *



[[[
view ../../python3_src/nn_ns/fileformat/font/freetype2/freetype2-note.txt
===
cp ~/ex_src/font/freetype-2.10.2/objs/.libs/*free* ~/ex_src/font/freetype2__bin/
    ...静态链接库 5~6Mb
    ...动态链接库 3~4Mb
cp ~/ex_src/font/ft2demos-2.10.2/bin/.libs/ftdump ~/ex_src/font/freetype2__bin/
    ...二进制可执行文件
    #wrapper-script:xxx:cp ~/ex_src/font/ft2demos-2.10.2/bin/ftdump  ../../python3_src/nn_ns/fileformat/font/freetype2/
        ...转发脚本

env - LD_LIBRARY_PATH=~/ex_src/font/freetype2__bin":$LD_LIBRARY_PATH"  ~/ex_src/font/freetype2__bin/ftdump  -c '/system/fonts/NotoSansLydian-Regular.ttf'
===
ftdump:输出格式:[
There are ??? faces in this file.
There is 1 face in this file.

----- Face number: ??? -----

font name entries
   ...
font type entries
   ...
charmaps (???)
   ???: format  ???, platform ???, encoding  ???   language ???
     ...
   ???: format  ???, platform ???, encoding  ???   language ??? (active)
     ...
??GX axes
   "Weight": [100;1000], default 550

----- Face number: ??? -----
...
]
===
]]]

===
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @print_txt5freetype2_ftdump_  :-C  :'/system/fonts/NotoSansLydian-Regular.ttf'

py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_  :'/system/fonts/NotoSansLydian-Regular.ttf'

py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @test4parse_output5freetype2_ftdump__charmap_coverage_


py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.txt5freetype2_ftdump_  :-c :'/system/fonts/NotoSansLydian-Regular.ttf'
[[[
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.txt5freetype2_ftdump_  :-C :'/system/fonts/NotoSansLydian-Regular.ttf'
    # NOTE: 『-C』char_ord->glyph_idx
    # NOTE: 『-c』[char_ord_rng]
===
There is 1 face in this file.

----- Face number: 0 -----

font name entries
   family:              Noto Sans Lydian
   style:               Regular
   postscript:          NotoSansLydian
   created:             2012-08-10
   modified:            2016-03-24
   revision:            1.03

font type entries
   FreeType driver:     truetype
   sfnt wrapped:        yes
   type:                scalable
   direction:           horizontal
   fixed width:         no
   glyph names:         no
   EM size:             2048
   global BBox:         (20,-40):(1883,1483)
   ascender:            2189
   descender:           -600
   height:              2789
   max_advance_width:   1913
   max_advance_height:  2789
   underline_position:  -205
   underline_thickness: 102
   glyph count:         31

charmaps (2)
   0: format  4, platform 3, encoding  1   language 0
      0x0000 => 1
      0x000d => 2
      0x0020 => 3
      0x00a0 => 3
      0xfeff => 1

   1: format 12, platform 3, encoding 10   language 0 (active)
      0x0000 => 1
      0x000d => 2
      0x0020 => 3
      0x00a0 => 3
      0xfeff => 1
      0x10920 => 4
      0x10921 => 5
      0x10922 => 6
      0x10923 => 7
      0x10924 => 8
      0x10925 => 9
      0x10926 => 10
      0x10927 => 11
      0x10928 => 12
      0x10929 => 13
      0x1092a => 14
      0x1092b => 15
      0x1092c => 16
      0x1092d => 17
      0x1092e => 18
      0x1092f => 19
      0x10930 => 20
      0x10931 => 21
      0x10932 => 22
      0x10933 => 23
      0x10934 => 24
      0x10935 => 25
      0x10936 => 26
      0x10937 => 27
      0x10938 => 28
      0x10939 => 29
      0x1093f => 30
===
]]]





[[[
===
txt5freetype2_ftdump_
===
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.txt5freetype2_ftdump_  :'/system/fonts/SysSans-Hant-Regular.ttf'
    #1版: 繁
... ...
family:              OPPOSansBig5 2.0
... ...
GX axes
   "Weight": [100;1000], default 550

py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.txt5freetype2_ftdump_  :'/system/fonts/SysSans-Hans-Regular.ttf'
    #1版: 简
... ...
family:              OPPOSans 2.0
... ...
GX axes
   "Weight": [100;1000], default 550

py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.txt5freetype2_ftdump_  :'/system/fonts/NotoSansCJK-Regular.ttc'
    #no:『GX axes』
    #10版:5*2: 日/韓/简/繁/港 * 不等宽/等宽
family:              Noto Sans CJK JP
family:              Noto Sans CJK KR
family:              Noto Sans CJK SC
family:              Noto Sans CJK TC
family:              Noto Sans CJK HK
family:              Noto Sans Mono CJK JP
family:              Noto Sans Mono CJK KR
family:              Noto Sans Mono CJK SC
family:              Noto Sans Mono CJK TC
family:              Noto Sans Mono CJK HK

py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.txt5freetype2_ftdump_  :'/system/fonts/NotoSerifCJK-Regular.ttc'
    #no:『GX axes』
    #4版: 日/韓/简/繁
family:              Noto Serif CJK JP
family:              Noto Serif CJK KR
family:              Noto Serif CJK SC
family:              Noto Serif CJK TC

===
ttc => multi font faces
ttf => single font face


===
freetype2_ftdump__charmap_coverage_
    +total_chars_only
===
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_  +total_chars_only :'/system/fonts/NotoSansLydian-Regular.ttf'
32
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_   +total_chars_only :'/system/fonts/SysSans-Hant-Regular.ttf'
14177
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_   +total_chars_only :'/system/fonts/SysSans-Hans-Regular.ttf'
28632
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_   +total_chars_only :'/system/fonts/NotoSansCJK-Regular.ttc'
44772
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_   +total_chars_only :'/system/fonts/NotoSerifCJK-Regular.ttc'
42995








===
freetype2_ftdump__charmap_coverage_
    +total_rngs_only
===
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_ +total_rngs_only  :'/system/fonts/NotoSansLydian-Regular.ttf'
32
NonTouchRanges(((0, 1), (13, 14), (32, 33), (160, 161), (65279, 65280), (67872, 67898), (67903, 67904)))

py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_   +total_rngs_only :'/system/fonts/SysSans-Hant-Regular.ttf'
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_   +total_rngs_only :'/system/fonts/SysSans-Hans-Regular.ttf'
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_   +total_rngs_only :'/system/fonts/NotoSansCJK-Regular.ttc'
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_   +total_rngs_only :'/system/fonts/NotoSerifCJK-Regular.ttc'
===

NotoSerifCJK-Regular.ttc
SysSans-Hans-Regular.ttf
NotoSansCJK-Regular.ttc
SysSans-Hant-Regular.ttf
NotoColorEmoji.ttf

===
accumulate_font_char_rngs_
    +total_chars_only
    --may_bg_rngs='[(0x3400,0x11_00_00)]'
===
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,accumulate_font_char_rngs_   --font_dir:'/system/fonts/' :'NotoSerifCJK-Regular.ttc' :'SysSans-Hans-Regular.ttf' :'NotoSansCJK-Regular.ttc' :'SysSans-Hant-Regular.ttf' --may_bg_rngs='[(0x3400,0x11_00_00)]' +total_chars_only
42071

===
accumulate_font_char_rngs_
    +compact
    +validate4compact
    --may_bg_rngs='[(0x3400,0x11_00_00)]'
===
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.accumulate_font_char_rngs_  +compact --font_dir:'/system/fonts/' :'NotoSansLydian-Regular.ttf'
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.accumulate_font_char_rngs_  +compact +validate4compact --font_dir:'/system/fonts/' :'NotoSansLydian-Regular.ttf'

==
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.accumulate_font_char_rngs_  +compact +validate4compact --may_bg_rngs='[(0x3400,0x11_00_00)]' --font_dir:'/system/fonts/' :'NotoSerifCJK-Regular.ttc' :'SysSans-Hans-Regular.ttf' :'NotoSansCJK-Regular.ttc' :'SysSans-Hant-Regular.ttf' > /sdcard/0my_files/tmp/out4py/nn_ns.fileformat.font.freetype2.freetype2_ftdump.accumulate_font_char_rngs_..cjk.out.txt
view /sdcard/0my_files/tmp/out4py/nn_ns.fileformat.font.freetype2.freetype2_ftdump.accumulate_font_char_rngs_..cjk.out.txt
du -h /sdcard/0my_files/tmp/out4py/nn_ns.fileformat.font.freetype2.freetype2_ftdump.accumulate_font_char_rngs_..cjk.out.txt
    12K
    copy to:
        e ./script/hz/部件拆分.py
===
]]]



[[[
#not-bug:xxx:bug:『rng miss end』
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   ,freetype2_ftdump__charmap_coverage_   +total_chars_only :'/system/fonts/NotoSansCJK-Regular.ttc'
    #不正常
        #原来是 截断！:『s[:80]』
        assert _double_num_charmaps == 2*num_charmaps, (num_charmaps, _double_num_charmaps, line_idx, line_idx4next_header, [s[:80] for s in ls[line_idx:line_idx4next_header]])
==>>:
    0: format  4, platform 0, encoding  3   language 0
     0020-007e,00a0-0103,0110-0113,011a,011b,0128-012b,0143,0144,0147,0148,014c-
   1: format 12, platform 0, encoding  4   language 0
     0020-007e,00a0-0103,0110-0113,011a,011b,0128-012b,0143,0144,0147,0148,014c-
   2: format 14, platform 0, encoding  5   (Unicode Variation Sequences)
     0020-007e,00a0-0103,0110-0113,011a,011b,0128-012b,0143,0144,0147,0148,014c-'
...
===
view  ../../python3_src/nn_ns/fileformat/font/freetype2/ftdump.c
===
『ftdump -c』==>>
    # 『else if ( coverage == 1 )』

  else if ( coverage == 1 )
  {
    FT_ULong  next, last = ~1;
    FT_UInt   gindex;

    const char*  f1 = "";
    const char*  f2 = "     %04lx";
    const char*  f3 = "";

    FT_Set_Charmap( face, face->charmaps[i] );

    next = FT_Get_First_Char( face, &gindex );
    while ( gindex )
    {
      if ( next == last + 1 )
      {
        f1 = f3;
        f3 = "-%04lx";
      }
      else
      {
        printf( f1, last );
        printf( f2, next );

        f1 = "";
        f2 = f3 = ",%04lx";
      }

      last = next;
      next = FT_Get_Next_Char( face, last, &gindex );
    }
    printf( f1, last );
    printf( "\n" );
  }
==>>:
1st round:
    [f1 := ''][f2 := '    {}']
    skip last
    print next
    [f1 := ''][f2 := f3 := ',{}']
    [last := next]
    [last be printed][discontinuous]
2nd_round:
    [last be printed][discontinuous]
    [f1 == ''][f2 == f3 == ',{}']
    * [no more next]:
        goto terminal
    * [last+1 == next]:
        [f1 := f3][f3 := '-{}']
        skip last <<==:
        [last := next]
        [last not be printed][continuous]
        [f1 == f2 == ',{}'][f3 == '-{}']
        goto 3rd_round
    * [last+1 =!= next]:
        skip last
        print ,next
        [f1 := ''][f2 := f3 := ',{}']
        [last := next]
        [last be printed][discontinuous]
        [f1 == ''][f2 == f3 == ',{}']
        goto 2nd_round
3rd_round:
    [last not be printed][continuous]
    [f1 == '[,-]{}'][f2 == ',{}'][f3 == '-{}']
    * [no more next]:
        goto terminal
    * [last+1 == next]:
        [f1 := f3][f3 := '-{}']
        skip last <<==:
        [last := next]
        [last not be printed][continuous]
        [f2 == ',{}'][f1 == f3 == '-{}']
        goto 3rd_round
    * [last+1 =!= next]:
        print [,-]last
        print ,next
        [f1 := ''][f2 := f3 := ',{}']
        [last := next]
        [last be printed][discontinuous]
        [f1 == ''][f2 == f3 == ',{}']
        goto 2nd_round
terminal:
    * from 2nd_round:
        [last be printed][discontinuous]
        [f1 == ''][f2 == f3 == ',{}']
        #printf( f1, last );
        skip last
    * from 3rd_round:
        [last not be printed][continuous]
        [f1 == '[,-]{}'][f2 == ',{}'][f3 == '-{}']
        #printf( f1, last );
        print [,-]last
===
#py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.txt5freetype2_ftdump_  :-C  :'/system/fonts/NotoSansCJK-Regular.ttc' | less
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @print_txt5freetype2_ftdump_  :-C  :'/system/fonts/NotoSansCJK-Regular.ttc' | less
    0: format  4, platform 0, encoding  3   language 0
      ... ...
      0x0144 => 205
      0x0147 => 206
      0x0148 => 207
      0x014c => 208
      0x014d => 209
      0x014e => 210
      0x014f => 211
      0x0152 => 212
      0x0153 => 213
      ... ...
      0xffec => 59215
      0xffed => 59216
      0xffee => 59217

   1: format 12, platform 0, encoding  4   language 0
      0x0020 => 1
      0x0021 => 2
      0x0022 => 3
      ... ...
      0x2f9de => 61851
      0x2f9df => 61852
      0x2f9f4 => 61853

   2: format 14, platform 0, encoding  5   (Unicode Variation Sequences)
      0x0020 => 1
      0x0021 => 2
      0x0022 => 3
      0x0023 => 4
      ... ...
===
env - LD_LIBRARY_PATH=~/ex_src/font/freetype2__bin":$LD_LIBRARY_PATH"  ~/ex_src/font/freetype2__bin/ftdump  -c '/system/fonts/NotoSansCJK-Regular.ttc'
    0: format  4, platform 0, encoding  3   language 0
     0020-007e,00a0-0103,0110-0113,011a,011b,0128-012b,0143,0144,0147,0148,014c-014f,0152,0153,...
    ...
    #正常！why??

===
py_adhoc_call   nn_ns.fileformat.font.freetype2.freetype2_ftdump   @str.txt5freetype2_ftdump_  :-c  :'/system/fonts/NotoSansCJK-Regular.ttc'
    #也正常！why??
===
]]]



#]]]'''
__all__ = r'''
prepare4run4freetype2_ftdump_
    print_txt5freetype2_ftdump_
    txt5freetype2_ftdump_
        freetype2_ftdump__charmap_coverage_
            accumulate_font_char_rngs_

freetype2_ftdump__charmap_coverage_
    txt5freetype2_ftdump_
    parse_txt5freetype2_ftdump__charmap_coverage_
        parse_charmap_list_
        test4parse_output5freetype2_ftdump__charmap_coverage_

'''.split()#'''
__all__


from seed.data_funcs.rngs import make_Ranges, NonTouchRanges
from seed.data_funcs.rngs import ranges2compact_txt_, ranges5compact_txt_

from seed.exec.text_of_stdout_of_call import text_of_stdout_of_call
from subprocess import Popen, PIPE, DEVNULL
import subprocess

from seed.tiny import check_type_is
from io import StringIO
from pathlib import Path

import os
import re
_regex4line_head_chars4output4ftdump = re.compile(r'T(-f *f *(f *)?(c *)?[ a-zA-Z0-9]*)*')
_regex4num_font_faces = re.compile(r'There (?:are|is) (?P<num_font_faces>\d+) faces? in this file[.]')
_regex4font_face_idx = re.compile(r'----- Face number: (?P<font_face_idx>\d+) -----')
_header4font_name_entries = r'font name entries'
_header4font_type_entries = r'font type entries'
_header4fixed_size = r'fixed size'

_regex4num_charmaps = re.compile(r'charmaps [(](?P<num_charmaps>\d+)[)]')
_regex4charmap_info = re.compile(r'(?P<charmap_idx>\d+): (?:synthetic|format  *(?P<format_idx>\d+)), platform  *(?P<platform_idx>\d+), encoding  *(?P<encoding_idx>\d+)  *(?:[(]Unicode Variation Sequences[)]|language  *(?P<language_idx>\d+)) *(?P<b_active>[(]active[)])?')



def prepare4run4freetype2_ftdump_(*args, LD_LIBRARY_PATH='', idir_path4freetype2_so='~/ex_src/font/freetype2__bin', nm4ftdump='ftdump', **kwds4run):
    _idir_path4freetype2_so = Path(idir_path4freetype2_so)
    idir_path4freetype2_so = _idir_path4freetype2_so.as_posix()

    if idir_path4freetype2_so[:2] in ('~', '~/'):
        _idir_path4freetype2_so = _idir_path4freetype2_so.expanduser()
        idir_path4freetype2_so = _idir_path4freetype2_so.as_posix()


    check_type_is(str, idir_path4freetype2_so)
    check_type_is(str, nm4ftdump)
    check_type_is(str, LD_LIBRARY_PATH)

    ipath4ftdump = (_idir_path4freetype2_so/nm4ftdump).as_posix()

    LD_LIBRARY_PATH = f'{idir_path4freetype2_so!s}:{LD_LIBRARY_PATH}'
    cmd = [ipath4ftdump, *args]
    if 0:
        cmd = ['env', '-', f'LD_LIBRARY_PATH={LD_LIBRARY_PATH}', *cmd]
        may_env = None
    else:
        env = os.environ
        env = {'LD_LIBRARY_PATH':LD_LIBRARY_PATH, **env}
        may_env = env
        cmd
    return (cmd, may_env, kwds4run)
def print_txt5freetype2_ftdump_(*args, **kwds):
    'args,kwds:see:prepare4run4freetype2_ftdump_()'
    (cmd, may_env, kwds4run) = prepare4run4freetype2_ftdump_(*args, **kwds)
    r = subprocess.run(cmd, check=True, env=may_env, **kwds4run)
    r.returncode
    #if 0b000:print(dir(r))
    return None # <<== [check:=True]
    return r.returncode
def txt5freetype2_ftdump_(*args, **kwds):
    'args,kwds:see:prepare4run4freetype2_ftdump_()'
    (cmd, may_env, kwds4run) = prepare4run4freetype2_ftdump_(*args, **kwds)
    txt = text_of_stdout_of_call(cmd, env=may_env, **kwds4run)
    return txt
#def accumulate_font_char_rngs_(ipaths4font, /, *, font_dir=None, total_chars_only=False, **kwds):
def accumulate_font_char_rngs_(*ipaths4font, font_dir=None, total_chars_only=False, may_bg_rngs=None, compact=False, validate4compact=False, **kwds):
    if not font_dir is None:
        font_dir = Path(font_dir)
        assert font_dir.is_dir()
        ipaths4font = (font_dir/ipath4font for ipath4font in ipaths4font)

    total_rngs = make_Ranges('')
    for ipath4font in ipaths4font:
        (_total_chars, _total_rngs) = freetype2_ftdump__charmap_coverage_(ipath4font, to_drop_char_rngs=True, total_rngs_only=True, total_chars_only=False, **kwds)
        total_rngs |= _total_rngs
    if not may_bg_rngs is None:
        bg_rngs = make_Ranges(may_bg_rngs)
        total_rngs &= bg_rngs
    total_chars = total_rngs.len_ints()
    if total_chars_only:
        return (total_chars,)
    if compact:
        return ranges2compact_txt_(total_rngs, validate=validate4compact)
    return (total_chars, total_rngs)
def freetype2_ftdump__charmap_coverage_(ipath4font, /, *, to_drop_char_rngs=False, total_rngs_only=False, total_chars_only=False, **kwds):
    'args,kwds:see:prepare4run4freetype2_ftdump_()'
    ipath4font = Path(ipath4font).as_posix()
    check_type_is(str, ipath4font)
    txt = txt5freetype2_ftdump_('-c', ipath4font, **kwds)
    #if 0b000:print(txt)
        #miss char ord list? why?
        #view /sdcard/0my_files/tmp/font/freetype/ft2demos-2.10.2/src/ftdump.c
        #   "-c, -C    Print charmap coverage.\n"
        # ==>> miss "-c"
    return parse_txt5freetype2_ftdump__charmap_coverage_(txt, to_drop_char_rngs=to_drop_char_rngs, total_rngs_only=total_rngs_only, total_chars_only=total_chars_only)
def test4parse_output5freetype2_ftdump__charmap_coverage_():
    txt = r'''
There is 1 face in this file.

----- Face number: 0 -----

font name entries
   family:              Noto Sans Lydian
   style:               Regular
   postscript:          NotoSansLydian
   created:             2012-08-10
   modified:            2016-03-24
   revision:            1.03

font type entries
   FreeType driver:     truetype
   sfnt wrapped:        yes
   type:                scalable
   direction:           horizontal
   fixed width:         no
   glyph names:         no
   EM size:             2048
   global BBox:         (20,-40):(1883,1483)
   ascender:            2189
   descender:           -600
   height:              2789
   max_advance_width:   1913
   max_advance_height:  2789
   underline_position:  -205
   underline_thickness: 102
   glyph count:         31

charmaps (2)
   0: format  4, platform 3, encoding  1   language 0
     0000,000d,0020,00a0,feff
   1: format 12, platform 3, encoding 10   language 0 (active)
     0000,000d,0020,00a0,feff,10920-10939,1093f

    '''#'''
    r = parse_txt5freetype2_ftdump__charmap_coverage_(txt, to_drop_char_rngs=False, total_rngs_only=False, total_chars_only=False)
    assert r == (32
    , NonTouchRanges(((0, 1), (13, 14), (32, 33), (160, 161), (65279, 65280), (67872, 67898), (67903, 67904)))
    , [({'family': 'Noto Sans Lydian', 'style': 'Regular', 'postscript': 'NotoSansLydian', 'created': '2012-08-10', 'modified': '2016-03-24', 'revision': '1.03'}
        #   #font_name_entries
        , {'FreeType driver': 'truetype', 'sfnt wrapped': 'yes', 'type': 'scalable', 'direction': 'horizontal', 'fixed width': 'no', 'glyph names': 'no', 'EM size': '2048', 'global BBox': '(20,-40):(1883,1483)', 'ascender': '2189', 'descender': '-600', 'height': '2789', 'max_advance_width': '1913', 'max_advance_height': '2789', 'underline_position': '-205', 'underline_thickness': '102', 'glyph count': '31'}
        #   #font_type_entries
        , [({'charmap_idx': 0, 'format_idx': 4, 'platform_idx': 3, 'encoding_idx': 1, 'language_idx': 0, 'b_active': False}, 5, NonTouchRanges(((0, 1), (13, 14), (32, 33), (160, 161), (65279, 65280))))
            , ({'charmap_idx': 1, 'format_idx': 12, 'platform_idx': 3, 'encoding_idx': 10, 'language_idx': 0, 'b_active': True}, 32, NonTouchRanges(((0, 1), (13, 14), (32, 33), (160, 161), (65279, 65280), (67872, 67898), (67903, 67904))))
        ]
        #   #charmap_idx2info_rngs_pair :: [(charmap_info, total_chars, charmap_rngs)]
        , []
        #   #extras
        )
    ]), r




def parse_txt5freetype2_ftdump__charmap_coverage_(txt, /, *, to_drop_char_rngs, total_rngs_only, total_chars_only):
    def __(txt, /):
        ifile = StringIO(txt)
        for line in ifile:
            s = line.rstrip() # '\n'
            if 0b000:
                print(repr(line))
                print(repr(s))
            if s:
                yield s
    [*ls] = __(txt)
    cs = ''.join(s[0] for s in ls)
    m = _regex4line_head_chars4output4ftdump.fullmatch(cs)
    if m is None: raise Exception(cs, ls)

    line_idx = 0
    m = _regex4num_font_faces.fullmatch(ls[line_idx])
    if m is None: raise 000
    num_font_faces = int(m['num_font_faces'])
    assert cs.count('-') == num_font_faces
    _, *tss = cs.split('-')
    line_idx += 1
    font_face_idx2data = []
    total_rngs = make_Ranges('')
    for _font_face_idx, ts in enumerate(tss):
        m = _regex4font_face_idx.fullmatch(ls[line_idx])
        if m is None: raise 000
        font_face_idx = int(m['font_face_idx'])
        assert _font_face_idx == font_face_idx
        line_idx += 1
        line_idx4next_round = line_idx + len(ts)

        dict8font_name_entries, line_idx = _extract_as_dict__header_(ls, line_idx, _header4font_name_entries)
        dict8font_type_entries, line_idx = _extract_as_dict__header_(ls, line_idx, _header4font_type_entries)
        if line_idx == len(ls):
            continue
        ch = ls[line_idx][0]
        if ch == 'f':
            #xxx:dict8fixed_size, line_idx = _extract_as_dict__header_(ls, line_idx, _header4fixed_size)
            assert ls[line_idx] == _header4fixed_size
            line_idx += 1
            (body, line_idx) = _extract_body(ls, line_idx)
                #skip, drop
            if line_idx == len(ls):
                continue
            ch = ls[line_idx][0]
        if ch == 'c':
            # [num_charmaps > 0]
            (_total_chars, _total_rngs, charmap_idx2info_rngs_pair), line_idx = _extract_charmaps(ls, line_idx, to_drop_char_rngs=to_drop_char_rngs)
            assert charmap_idx2info_rngs_pair
            total_rngs |= _total_rngs
        else:
            # [num_charmaps == 0]
            charmap_idx2info_rngs_pair = 0
        charmap_idx2info_rngs_pair

        extras = []
        while line_idx < len(cs) and not cs[line_idx] == '-':
            header = ls[line_idx]
            line_idx += 1
            (dict8body, line_idx) = _extract_as_dict(ls, line_idx)
            extras.append((header, dict8body))
        font_face_idx2data.append((dict8font_name_entries, dict8font_type_entries, charmap_idx2info_rngs_pair, extras))

        assert line_idx == line_idx4next_round
    assert len(font_face_idx2data) == num_font_faces
    total_chars = total_rngs.len_ints()
    if total_chars_only:
        return (total_chars,)
    elif total_rngs_only:
        return (total_chars, total_rngs)
    return (total_chars, total_rngs, font_face_idx2data)
    return font_face_idx2data
def _extract_body(ls, line_idx, /):
    for i in range(line_idx, len(ls)):
        if not ls[i][0] == ' ':
            break
    else:
        i = len(ls)
    line_idx4next_header = i
    body = ls[line_idx:line_idx4next_header]
    body = [s.strip() for s in body]
    return (body, line_idx4next_header)
def _extract_charmaps(ls, line_idx, /, *, to_drop_char_rngs):
    m = _regex4num_charmaps.fullmatch(ls[line_idx])
    if m is None: raise 000
    num_charmaps = int(m['num_charmaps'])
    line_idx += 1
    (body, line_idx4next_header) = _extract_body(ls, line_idx)
    if 000:
        _double_num_charmaps = (line_idx4next_header - line_idx)
        assert _double_num_charmaps == 2*num_charmaps, (num_charmaps, _double_num_charmaps, line_idx, line_idx4next_header, [s[:80] for s in ls[line_idx:line_idx4next_header]])
            #bug:
            #env - LD_LIBRARY_PATH=~/ex_src/font/freetype2__bin":$LD_LIBRARY_PATH"  ~/ex_src/font/freetype2__bin/ftdump  -c '/system/fonts/NotoSansCJK-Regular.ttc' | less
            #==>>: [..., '   3: format  6, platform 1, encoding  1   language 0', '   4: format  4, platform 3, encoding  1   language 0', ...]
            #
    pairs = []
    total_rngs = make_Ranges('')
    i = 0
    for charmap_idx in range(num_charmaps):
        s0 = body[i]
        i += 1
        m = _regex4charmap_info.fullmatch(s0)
        if m is None: raise Exception(s0)
        d = m.groupdict()
        d['b_active'] = bool(d['b_active'])
        d = {k:-1 if v is None else int(v) for k,v in d.items()}
        d['b_active'] = bool(d['b_active'])
        assert charmap_idx == d['charmap_idx']
        if i < len(body):
            s1 = body[i]
            if ':' in s1[:80]:
                # s1 is next_header
                rngs = make_Ranges('')
            else:
                i += 1
                rngs = parse_charmap_list_(s1)
            i, rngs
        else:
            rngs = make_Ranges('')
        i, rngs

        info = d
        num_chars = rngs.len_ints()
        if to_drop_char_rngs:
            charmap = (info, num_chars)
        else:
            charmap = (info, num_chars, rngs)
        charmap
        total_rngs |= rngs
        pairs.append(charmap)
    assert line_idx+i == line_idx4next_header
    assert len(pairs) == num_charmaps
    total_chars = total_rngs.len_ints()
    return (total_chars, total_rngs, pairs), line_idx4next_header
def parse_charmap_list_(s, /):
    return make_Ranges(_parse_charmap_list(s))
def _parse_charmap_list(s, /):
    for s in s.split(','):
        ls = s.split('-')
        assert 1 <= len(ls) <= 2
        ls = [int(a, 16) for a in ls]
        if len(ls) == 2:
            a,b = ls
        else:
            [a] = ls
            b = a
        yield (a, b+1)
def _extract_as_dict__header_(ls, line_idx, header, /):
    assert ls[line_idx] == header
    line_idx += 1
    return _extract_as_dict(ls, line_idx)
def _extract_as_dict(ls, line_idx, /):
    begin = line_idx
    (body, end) = _extract_body(ls, begin)
    d = {}
    for s in body:
        #assert s[0] == ' '
        #s = s.strip()
        k, _, v = s.partition(':')
        assert _
        v = v.strip()
        assert k == k.strip()
        d[k] = v
    assert len(d) == end-begin == len(body)
    line_idx = end
    return d, line_idx


if __name__ == "__main__":
    pass
__all__


from nn_ns.fileformat.font.freetype2.freetype2_ftdump import *
