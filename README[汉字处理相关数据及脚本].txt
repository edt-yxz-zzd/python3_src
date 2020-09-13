
汉字处理相关数据及脚本

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
        # 现代常用字部件的笔画顺序__依github_stroke_seq_MB #TODO


py script/py_repr2json.py -i ~/tmp/ids_all_2.txt -o ~/tmp/ids_all_2.json.txt
py script/handle_现代常用字部件表.py > ~/tmp/现代常用字部件及部件名称规范_GF0014_2009_main_result.json.txt





/storage/emulated/0/0my_files/tmp/after_ids_pp_2.txt
   'HandleParsedIDS__all_hz_ref':
      ({'total_cmpnts': 5077, 'total_cmpnts__ge2': 2791}
      ,{'&A-CDP-8D60;': ['薨', '蘉'], ...}
      )

    #结合 ucs-strokes.txt, ids_all_2.json.txt, 对5077个部件(实际只有1743个基本部件)按笔画数排序并给出笔画顺序(校验或计算笔画数，辅助搜索部件)
      $ py script/ids_basic_component2strokes.py > ~/tmp/prime_hz_cmpnt2num_strokes_ls.txt

