
汉字处理相关数据及脚本

数据:
  py:
    codec
      encodings
    unicodedata
      name()
  国家规范:
    现代常用字部件及部件名称规范_GF0014_2009.pdf
    通用规范汉字表2013.txt
  地方规范:
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
  www/???:
    中华字经2003__重复字4000_不同字3980
    汉字单字字频总表_cedict_12041

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



py script/py_repr2json.py -i ~/tmp/ids_all_2.txt -o ~/tmp/ids_all_2.json.txt
py script/handle_现代常用字部件表.py > ~/tmp/现代常用字部件及部件名称规范_GF0014_2009_main_result.json.txt


