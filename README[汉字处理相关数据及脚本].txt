
汉字处理相关数据及脚本

我的
  e /storage/emulated/0/0my_files/git_repos/python3_src/README\[汉字处理相关数据及脚本].txt
    本文件
  e ../../python3_src/nn_ns/CJK/CJK_data/raw/我的汉字分解原则.txt
  e /storage/emulated/0/0my_files/git_repos/txt_phone/txt/TODO2.txt
    临时
  e /storage/emulated/0/0my_files/git_repos/txt_phone/笔顺码分解/0000.txt
    进程:暂停:重新思考拆分原则
    太细致，细化到笔画 无用，应立于更粗颗粒的基础部件上
    转:汉字粗拆分

  view /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/我的所有折笔归类.txt
  view /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/unicode_CJK_Strokes_U31C0.pdf.txt
  e /storage/emulated/0/0my_files/git_repos/txt_phone/汉字粗拆分/汉字粗拆分working.txt
    进程:暂停:重新思考拆分原则、数据格式
    阶段性结果:
      view /storage/emulated/0/0my_files/git_repos/txt_phone/汉字粗拆分/汉字粗拆分working__1pause_20201022.txt
    对如何拆分仍有疑问，转:
      e hz/TODO-汉字拆分设计.txt
      e /storage/emulated/0/0my_files/git_repos/txt_phone/汉字粗拆分/2汉字粗拆分working2.txt


数据:
  [unicode]
      #E:\book\computer\standard\unicode\13.0.0[download_at][20200913]
      #$ cd /sdcard/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]/
      #cd /sdcard/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]
      #$ tree .
      .
      ├── ReadMe_TIME.txt
      ├── UnicodeStandard-13.0.pdf
      ├── charts
      │   ├── CodeCharts.pdf
      │   ├── RSIndex.pdf
      │   └── Readme.txt
      ├── charts-East_Asian_Scripts
      │   ├── U20000.pdf
      │   ├── U2A700.pdf
      │   ├── U2B740.pdf
      │   ├── U2B820.pdf
      │   ├── U2CEB0.pdf
      │   ├── U2E80.pdf
      │   ├── U2F00.pdf
      │   ├── U2F800.pdf
      │   ├── U2FF0.pdf
      │   ├── U30000.pdf
      │   ├── U3100.pdf
      │   ├── U31A0.pdf
      │   ├── U31C0.pdf
      │   ├── U3400.pdf
      │   ├── U4E00.pdf
      │   └── UF900.pdf
      └── zipped_UCD
          ├── ReadMe.txt
          ├── UCD.zip
          └── Unihan.zip
  py:
    codec
      encodings
    unicodedata
      name()
  国家规范:
    现代常用字部件及部件名称规范_GF0014_2009.pdf
    通用规范汉字表2013.txt
    现代常用独体字规范[GF0013_2009].pdf
    GB13000.1字符集汉字部首归部规范[GF0012_2009].pdf
    汉字部首表[GF0011_2009].pdf

    #$ cd /sdcard/0my_files/zip/zip_selected__e_book_data/汉字规范/
    #/sdcard/0my_files/unzip/e_book/汉字分解/现代常用字部件及部件名称规范/现代常用字部件及部件名称规范[GF0014_2009][3500一级字的部件共441组514个].pdf
    #/sdcard/0my_files/unzip/e_book/汉字分解/常见汉字及部件/通用规范汉字表2013.txt
  地方规范:
    香港电脑汉字参考字形
      #$ cd /sdcard/0my_files/zip/zip_selected__e_book_data/ 汉字规范/
      香港电脑汉字参考字形[2017][ReferenceGlyphs].pdf
      香港电脑汉字楷体及宋体字形参考指引[2002+2005][644个部件][glyph].pdf

    iso10646hk.net
      #$ cd /sdcard/0my_files/unzip/e_book/汉字分解/iso10646hk.net/
      #11
      'Decomposition for ISO_IEC 10646 ideographic characters (2002)(Lu Qin ).pdf'
      '[CJK 20902, ExtA and HKSCS字拆分成部件的序列表]normal_char.txt'
      '[按部件排列的CJK 20902, ExtA and HKSCS字表]ly_glyph11_ucode.txt'
      '[按部件碼（Cc-Code）排序的部件總表 (包括日、韓及簡化部件)]ly_glyph11_all_web_ccode_order.pdf'
      '[日本、韓國及越南字表]jkv_char.txt'
      '[星加坡字及簡體字表]simpl_singapore_char.txt'
      '[電腦漢字日本、韓國及簡化字部件表]ly_glyph11_other_web.pdf'
      '[香港電腦漢字印刷體 (宋體)字形基礎部件表]m_glyph_1img_web.pdf'
      '[香港電腦漢字印刷體(宋體)字形參考指引Song_Guide.pdf'
      '[香港電腦漢字楷體字形參考指引]Kai_Guide.pdf'
      '[香港電腦漢字楷體字形基礎部件表]ly_glyph11_imgcode_web.pdf'

  www/github:
    CHISE_IDS
    cjkvi-ids-master/ucs-strokes.txt
      # /sdcard/0my_files/unzip/e_book/汉字分解/cjkvi-ids[202008]/cjkvi-ids-master/ucs-strokes.txt
      # /sdcard/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/cjkvi-ids-master[20190207]/ucs-strokes.txt
      # 按笔画数分解，可引用已分解的成字部件
    ####
    #/sdcard/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/
    #  '汉字笔顺表[20200913]'
    #  '繁简转换[20200913]'
    ####
    [汉字笔顺表][20200913]
        stroke-seq_MB-master[汉字笔顺表][20200827].zip
            单字_笔顺码_29685个[stroke-seq_MB][汉字笔顺表][20200827].rar
        https://github.com/YQ-YSY/stroke-seq_MB
    [繁简转换][20200913]
        chinese-converter-master.zip
        chinese-utils-master.zip
        funNLP-master.zip
        nstools-master.zip
        ###
        https://github.com/luhuiguo/chinese-utils/tree/master/src/main/resources
        https://github.com/skydark/nstools/tree/master/zhtools
        https://github.com/miaolapd/chinese-converter/tree/master/ChineseConverter/ConverterMaps
        https://github.com/fighting41love/funNLP/blob/master/data/%E7%B9%81%E7%AE%80%E4%BD%93%E8%BD%AC%E6%8D%A2%E8%AF%8D%E5%BA%93/fanjian_suoyin.txt
            https://github.com/fighting41love/funNLP/blob/master/data/繁简体转换词库/fanjian_suoyin.txt

        # $ pwd
        # /sdcard/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]
        # $ tree .
        .
        ├── chinese-converter-master
        │   └── ConverterMaps
        │       ├── 00.Default.xml
        │       ├── 01.Wikipedia.xml
        │       ├── 02.HuoXingWen.xml
        │       ├── 03.Tools.xml
        │       └── 04.Kanzi_wulali.xml
        └── 04.Kanzi_wulali.xml
        ├── chinese-utils-master
        │   └── resources
        │       ├── pinyin.txt
        │       ├── polyphone.txt
        │       ├── simp.txt
        │       ├── simplified.txt
        │       ├── trad.txt
        │       ├── traditional.txt
        │       └── unknown.txt
        ├── funNLP-master
        │   └── fanjian_suoyin.txt
        └── nstools-master
            └── zhtools
                ├── Mandarin.dat
                ├── __init__.py
                ├── chconv.py
                ├── langconv.py
                ├── test_langconv.py
                ├── xpinyin.py
                └── zh_wiki.py

  www/yywzw/语言文字网:
    汉字零件表_胡敬禹_20061218
      file:///storage/emulated/0/0my_files/tmp-download/www.yywzw.com/jt/hjy/a-xfljb.htm
    汉字部件清单_潘德孚_20030617
      潘德孚::两种汉字部件研究方法的比较::汉字部件系统研究
      file:///storage/emulated/0/0my_files/tmp-download/www.yywzw.com/pan/pan-03b-02.htm
        五、部件定义的补充解释
        六、部件清单
          汉字部件清单
    working
      e ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字部件清单_潘德孚_20030617.txt
      e ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字零件表_胡敬禹_20061218.txt
  www/???:
    中华字经2003__重复字4000_不同字3980
    汉字单字字频总表_cedict_12041
    #/sdcard/0my_files/unzip/e_book/汉字分解/常见汉字及部件/中华字经[郭保华][2003].txt
    #/sdcard/0my_files/unzip/e_book/汉字词/汉字单字字频总表/汉字单字字频总表.txt

脚本:
  my py:
    seed
      seed.data_funcs.rngs
      seed.text.charset_filter
    nn_ns
      nn_ns/CJK/CJK_data/raw/parse_繁简.py
      #$ cd ../../python3_src/nn_ns/CJK/cjk_subsets/
      #$ tree .
      .
      ├── charset_filter.py.out
      │   ├── cjk_rngs.zip
      │   └── readme.txt
      ├── cjk_common_subset.py
      ├── cjk_subsets__relationship.py
      ├── cjk_subsets__relationship.py.out
      │   ├── cjk_rel.txt
      │   ├── cjk_rel_more.txt
      │   └── cjk_rel_more__le.txt
      ├── cjk_subsets__relationship.py.result.txt
      └── hanzi.py

    <phone>/~/txt/script/
      parse_CHISE_IDS.py
      after_parse_CHISE_IDS.py
      py_repr2json.py
      handle_现代常用字部件表.py
        #含手录数据: 
        # 现代常用字部件及部件名称规范
        # 现代常用字部件的笔画顺序__依github_stroke_seq_MB
      pre_hz_decomp.py


py script/py_repr2json.py -i ~/tmp/ids_all_2.txt -o ~/tmp/ids_all_2.json.txt
py script/handle_现代常用字部件表.py > ~/tmp/现代常用字部件及部件名称规范_GF0014_2009_main_result.json.txt
  # /sdcard/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/output/handle_现代常用字部件表.py.out/现代常用字部件及部件名称规范_GF0014_2009_main_result.json.txt
  # /sdcard/0my_files/git_repos/txt_phone/txt/others/汉语/现代常用字部件及部件名称规范_GF0014_2009/现代常用字部件及部件名称规范_GF0014_2009_main_result.json.txt





/storage/emulated/0/0my_files/tmp/after_ids_pp_2.txt
   'HandleParsedIDS__all_hz_ref':
      ({'total_cmpnts': 5077, 'total_cmpnts__ge2': 2791}
      ,{'&A-CDP-8D60;': ['薨', '蘉'], ...}
      )

    #结合 ucs-strokes.txt, ids_all_2.json.txt, 对5077个部件(实际只有1743个基本部件)按笔画数排序并给出笔画顺序(校验或计算笔画数，辅助搜索部件)
      $ py script/ids_basic_component2strokes.py > ~/tmp/prime_hz_cmpnt2num_strokes_ls.txt


py nn_ns/CJK/CJK_data/raw/parse_繁简.py >nn_ns/CJK/CJK_data/output/parse_繁简.py.out/简繁.txt 2>nn_ns/CJK/CJK_data/output/parse_繁简.py.out/简繁.err.txt

py script/pre_hz_decomp.py -o ~/tmp/笔顺码分解.txt -f
    27978 笔顺码
    单笔部件=True:54.7 MB
    单笔部件=False:42.4 MB
  py -m nn_ns.app.cut_text -n 500 -re '^\s*$' -cs tail -ofmt '{0:0>4}.txt' -od ~/tmp/笔顺码分解 -i /storage/emulated/0/0my_files/笔顺码分解.txt
    0000.txt .. 0055.txt
      56=ceil(27978/500)
  py script/pre_hz_decomp.py --_tmp_call 2 > /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/output/pre_hz_decomp.py.out/部件的单字符代表.txt
py -m nn_ns.CJK.CJK_data.raw.汉字相关字符范围 -do prepare_for_汉字粗拆分 -o ~/tmp/汉字粗拆分working.txt
  1.8 MB
  sorted by char ord
  working with 一汉字多字形 unicode 13.0.0 :: charts-East_Asian_Scripts :: *.pdf
  $ ls -1 '/sdcard/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]/charts-East_Asian_Scripts/'
    U20000.pdf
    U2A700.pdf
    U2B740.pdf
    U2B820.pdf
    U2CEB0.pdf
    U2E80.pdf
    U2F00.pdf
    U2F800.pdf
    U2FF0.pdf
    U30000.pdf
    U3100.pdf
    U31A0.pdf
    U31C0.pdf
    U3400.pdf
    U4E00.pdf
    UF900.pdf
py '/storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/my_patch.py'
  cd '/storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/'
  py my_patch.py > my_patch.py.out.txt
  view /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表\[20200913]/stroke-seq_MB-master\[汉字笔顺表]\[20200827]/my_patch.py.out.txt
  view /storage/emulated/0/0my_files/git_repos/txt_phone/汉字粗拆分/汉字粗拆分working__1day.txt
  view /storage/emulated/0/0my_files/git_repos/txt_phone/汉字粗拆分/汉字粗拆分working__1pause_20201022.txt


py -m nn_ns.CJK.CJK_data.raw.汉字相关字符范围 -do prepare_for_2汉字粗拆分2 -o ~/tmp/2汉字粗拆分working2.txt
  3.7 MB

