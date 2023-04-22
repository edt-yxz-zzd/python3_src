
e ../../python3_src/nn_ns/CJK/CJK_data/output/parse_繁简.py.out/README.bug.txt


view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字繁简.py

bug:
'bug:包含:  ․˙‥¨′＇═〓「“」”『‘』’〞″䊷䌶'
bug:包含:\u25A1

grep $'\u25A1' -r '../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/' -l
../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/funNLP-master/fanjian_suoyin.txt
    只有一个文件


