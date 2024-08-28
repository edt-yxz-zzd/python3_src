
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ReadMe.txt

copy some selected original unicode UCD files
  ?hard-handle?
  ?small?

[[[
alias@20240707
    PropertyAliases.txt
      12K
    PropertyValueAliases.txt
      76K
      属性值:跨属性后不唯一
      属性值 可能与 属性名 相同
      (属性名,属性值)唯一
      字符串属性:属性值不改动，其余属性:属性值可规范化:去除:空格/下划线/连字符，大小写无关...
      各种各样的特色:
        * 3列: 属性名牜短-短名-长名-另短名-另长名
        * 5列: 真值属性名牜短-短名-长名-另短名-另长名
        * 4列: ccc-整数值-短名-长名
        * 3列+可选项注释: gc-短名-长名-『#』单字符短名相关的所有双字符短名
        * 『# @missing ... ...』
          #可能有也可能没有列出 任一属性值
          # 字符串属性，数值属性，琐碎属性...
        ... ...
        ... ...
===
alias:
ls ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/
ls /sdcard/0my_files/unzip/unicode14_0/UCD/
PropertyAliases.txt
PropertyValueAliases.txt

view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/PropertyAliases.txt
view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/PropertyValueAliases.txt

view /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyAliases.txt
view /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyValueAliases.txt




du -h /sdcard/0my_files/unzip/e_book/unicode_13__UCD/PropertyAliases.txt
  12K
du -h /sdcard/0my_files/unzip/e_book/unicode_13__UCD/PropertyValueAliases.txt
  76K

du -h /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyAliases.txt
  12K
du -h /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyValueAliases.txt

  76K

[[
diff /sdcard/0my_files/unzip/e_book/unicode_13__UCD/PropertyAliases.txt /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyAliases.txt
===
1,3c1,3
< # PropertyAliases-13.0.0.txt
< # Date: 2019-10-23, 03:46:32 GMT
< # © 2019 Unicode®, Inc.
---
> # PropertyAliases-14.0.0.txt
> # Date: 2021-03-08, 19:35:48 GMT
> # © 2021 Unicode®, Inc.

===
]]

[[
diff /sdcard/0my_files/unzip/e_book/unicode_13__UCD/PropertyValueAliases.txt /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyValueAliases.txt
===
1,3c1,3
< # PropertyValueAliases-13.0.0.txt
< # Date: 2019-11-13, 21:52:10 GMT
< # © 2019 Unicode®, Inc.
---
> # PropertyValueAliases-14.0.0.txt
> # Date: 2021-05-10, 21:08:53 GMT
> # © 2021 Unicode®, Inc.
91a92
> age; 14.0                             ; V14_0
162a164
> blk; Arabic_Ext_B                     ; Arabic_Extended_B
218a221
> blk; Cypro_Minoan                     ; Cypro_Minoan
248a252
> blk; Ethiopic_Ext_B                   ; Ethiopic_Extended_B
287a292
> blk; Kana_Ext_B                       ; Kana_Extended_B
308a314,315
> blk; Latin_Ext_F                      ; Latin_Extended_F
> blk; Latin_Ext_G                      ; Latin_Extended_G
374a382
> blk; Old_Uyghur                       ; Old_Uyghur
435a444
> blk; Tangsa                           ; Tangsa
444a454
> blk; Toto                             ; Toto
447a458
> blk; UCAS_Ext_A                       ; Unified_Canadian_Aboriginal_Syllabics_Extended_A
451a463
> blk; Vithkuqi                         ; Vithkuqi
460a473
> blk; Znamenny_Music                   ; Znamenny_Musical_Notation
1034a1048,1049
> jg ; Thin_Yeh                         ; Thin_Yeh
> jg ; Vertical_Tail                    ; Vertical_Tail
1264a1280
> sc ; Cpmn                             ; Cypro_Minoan
1343a1360
> sc ; Ougr                             ; Old_Uyghur
1385a1403,1404
> sc ; Tnsa                             ; Tangsa
> sc ; Toto                             ; Toto
1387a1407
> sc ; Vith                             ; Vithkuqi
===
]]


mkdir ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ReadMe.txt

mkdir ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ucd_ver13_0/
mkdir ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ucd_ver14_0/

cp -iv /sdcard/0my_files/unzip/e_book/unicode_13__UCD/PropertyAliases.txt ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ucd_ver13_0/
cp -iv /sdcard/0my_files/unzip/e_book/unicode_13__UCD/PropertyValueAliases.txt ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ucd_ver13_0/

cp -iv /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyAliases.txt ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ucd_ver14_0/
cp -iv /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyValueAliases.txt ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ucd_ver14_0/

===
]]]

